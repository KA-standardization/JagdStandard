import time
import json
import asyncio

import requests

from asyncio_5_30.dongfeng.base_url import urls
from asyncio_5_30.dongfeng.config import ZhiHuClient, redis_cluster


async def request(queue, url, headers):
    try:
        # response = requests.get(url, headers=headers, proxies=ZhiHuClient.get_ip(), timeout=3)
        response = requests.get("https://www.baidu.com", timeout=3)
        if response.status_code == 200:
            res = response.json()
            return res
        # if res and res != -1:
        #     datas = res['data']
        #     url_token = url.split('/')[4]
        #     for data in datas:
        #         key = data['url_token']  # 拿到数据把json里的urltoken 洗出来当hash key
        #         redis_cluster.hset(f'zhihu:ftest:{url_token}', key, json.dumps(data, ensure_ascii=False))

        else:
            queue.put(url)
            return -1
    except:
        queue.put(url)
        return -1


async def parse(loop, queue, url, referer):
    headers2 = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        "x-zse-93": "101_3_2.0",
        "x-requested-with": "fetch",
    }
    domain = 'https://www.zhihu.com'
    # d0 = "APAcmUSAuhSPTtfJNHxjVKzfyovrBKi3S_w=|1648893257"
    # x_81 = "3_2.0VhnTj77m-qofgh3TxTnq2_Qq2LYuDhV80wSL7T9yr6nxeTtqXRFZSTrZgcO9kUS_IHkmWgLBpukYWgxmIQPYqbpfZUnPS0FZG0Yq-6C1ZhSYVCxm1uV_70RqSMCBVuky16P0riRCyufOovxBXgSCiiR0ELYuUrxmtDomqU7ynXtOnAoTh_PhRDSTFLw8bhY14B2YebpqFCwLpgOyGiLLeJufNwFsprSYG8YyhJxCfrHMeXV9YeSTvAO02LxmV9c9hq20HcuLLDHLybeCxDVBbDo0-UCfXG20mcXCeUUGhDoXSMo0cqwLIcN0HUoYJ0YYBBe1xvNYrDc82_N8NcL9kLLZevxxkXS_RCC_fgg9Cqkw3Gg8lrHKyvXytcx9sCx9sQxOpr9_3hVx_vNYHCFfrQgKA9XmC9O8f4eVjge1zBFLQGgG1MYYpJgmc9xfr6xmA9SYrM7OOqgYVbHqcJS8bhp1whLKoBHC"
    # to_encrypt = "101_3_2.0+" + url + "+" + d0 + "+" + x_81
    # encrypt = ZhiHuClient.get_encrypt_b(to_encrypt)
    # headers2.update(
    #     {
    #         "referer": referer,
    #         "x-zse-96": "2.0_%s" % encrypt,
    #         "cookie": f'd_c0={d0};',
    #         'x-zst-81': x_81,
    #     }
    # )
    res = await loop.create_task(request(queue, domain + url, headers2))
    print(res)


if __name__ == '__main__':
    start_time = time.time()
    queue = asyncio.Queue()
    loop = asyncio.get_event_loop()
    tasks = []

    for url in urls:
        for key, value in url.items():
            task = asyncio.ensure_future(parse(loop, queue, key, value))
            tasks.append(task)
    print(1111111111)
    loop.run_until_complete(asyncio.wait(tasks, timeout=3.1))
    # print(queue)
    print("TIME: {}".format(time.time() - start_time))
