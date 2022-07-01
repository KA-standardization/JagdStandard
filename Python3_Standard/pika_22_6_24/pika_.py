import json
import pika
import datetime
import pytz, arrow
from elasticsearch.helpers import streaming_bulk
from elasticsearch import Elasticsearch

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='10.0.4.108',
    port=5672,
    virtual_host='frame',
    credentials=pika.PlainCredentials('mquser', '654321')
))
channel = connection.channel()

channel.queue_declare(queue='douyin.search', durable=True, arguments={"x-queue-mode": "lazy"})
channel.queue_bind('douyin.search', exchange='douyin', routing_key='sousuo')
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, data):
    try:
        body = json.loads(data)
        # print(body)
        es_conf = Elasticsearch('http://eswriter:ZDM4MTUwZDNi@10.0.4.102:4040', dead_timeout=5, retry_on_timeout=True)
        body['timestamp'] = datetime.datetime.now().astimezone(pytz.timezone('Asia/Shanghai'))
        init_time = arrow.get(body['post_create_time']).astimezone(pytz.timezone('Asia/Shanghai'))
        ori_index = lambda x: '%d.%02d' % (x.year, x.month)
        # index = 'post_douyin-v1_1-' + ori_index(init_time)
        index = 'post_douyin-v1_1-' + ori_index(init_time)
        # print(index)
        action = [{
            "_op_type": 'index',
            "_index": index,
            # "_type": '_doc',
            "_id": body['post_id'],
            "_source": body
        }]
        res = streaming_bulk(es_conf, action, chunk_size=3000, raise_on_error=False, raise_on_exception=False,
                             max_retries=5, request_timeout=3)
        # print(res.send())
        for k, v in res:
            print(k, v)
            if k == 'ok':
                pass
            else:
                print(v)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except:
        print('入库失败')


channel.basic_qos(prefetch_count=10)
channel.basic_consume('douyin.search', on_message_callback=callback, auto_ack=False)
channel.start_consuming()
