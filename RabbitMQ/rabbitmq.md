# RabbitMQ

```shell
rabbitmqctl set_vm_memory_high_watermark 0.7
```

```
docker run -d --name rabbitmq3 -p 5672:5672 -p 15672:15672 -v `pwd`/rabbitmq_data:/var/lib/rabbitmq --hostname JagdRabbit -e RABBITMQ_DEFAULT_VHOST=jagd_vhost  -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=root 799381c528ac
vi /etc/docker/daemon.json
	{
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
	}
docker pull rabbitmq:management

x-max-length
docker run -d --name rabbitmq3 -p 5672:5672 -p 15672:15672 -v `pwd`/rabbitmq_data:/var/lib/rabbitmq --hostname JagdRabbit -e RABBITMQ_DEFAULT_VHOST=jagd_vhost  -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=root -e RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS="-rabbit length_max 10000000" 799381c528ac
```

