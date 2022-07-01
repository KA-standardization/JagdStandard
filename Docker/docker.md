```shell
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

```shell
yum install -y yum-utils
yum makecache fast
```

```she
yum-config-manager \
    --add-repo \
    http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

```shell
yum install docker-ce docker-ce-cli containerd.io
```

```shell
systemctl start docker
```

```shell
docker run hello-world
```

```shell
[root@localhost ~]# docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    d1165f221234   3 months ago   13.3kB

docker -a -q

[root@localhost ~]# ls /var/lib/docker/
buildkit  containers  image  network  overlay2  plugins  runtimes  swarm  tmp  trust  volumes
```

```docker
docker rmi -f 镜像id
```



```docker
docker run [] image
--name="xxx"		容器名字
-d 后台方式
-it 使用交互方式,进入后台查看内容
-P 指定容器端口 8080(宿主机):8080(容器)  map映射
	-p ip:主机端口:容器端口
	-p 主机端口:容器端口
	-p 容器端口
	容器端口
-p 随机指定端口
```

```docker
docker pull centos
docker run -it centos /bin/bash

docker ps 正再运行的
docker ps -a 曾经运行过的

exit 停止退出
CTRL  p q

docker rm -f 容器id
docker ps -aq|xargs docker rm

docker start 容器id
docker restart 容器id
docker stop 容器id
docker kill 容器id
```

```docker
docker run -d centos

docker run -d centos /bin/bash -c "while true;do echo Jager;sleep 1;done"

docker logs -tf --tail 容器id

docker top 容器id

docker inspect 容器id

```

```docker
[root@localhost ~]# docker inspect $(docker ps -q)
[
    {
        "Id": "99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af",
        "Created": "2021-06-13T05:46:08.472303191Z",
        "Path": "/bin/bash",
        "Args": [
            "-c",
            "while true;do echo Jager;sleep 1;done"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 138561,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-06-13T05:46:08.860033249Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:300e315adb2f96afe5f0b2780b87f28ae95231fe3bdd1e16b9ba606307728f55",
        "ResolvConfPath": "/var/lib/docker/containers/99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af/hostname",
        "HostsPath": "/var/lib/docker/containers/99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af/hosts",
        "LogPath": "/var/lib/docker/containers/99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af/99ec32b5690d9533dc2490d112151ad437b73cac4dd3f835596b661c1fd9c5af-json.log",
        "Name": "/interesting_haslett",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0c30bd58611d9d5d852c8ab3e6bec9eea0ed57bebff203ff7d9d0a9eb927dc84-init/diff:/var/lib/docker/overlay2/1d4f53fceb97a2169517f651ea960b3660632d8595193919c3e0f635226e3bf0/diff",
                "MergedDir": "/var/lib/docker/overlay2/0c30bd58611d9d5d852c8ab3e6bec9eea0ed57bebff203ff7d9d0a9eb927dc84/merged",
                "UpperDir": "/var/lib/docker/overlay2/0c30bd58611d9d5d852c8ab3e6bec9eea0ed57bebff203ff7d9d0a9eb927dc84/diff",
                "WorkDir": "/var/lib/docker/overlay2/0c30bd58611d9d5d852c8ab3e6bec9eea0ed57bebff203ff7d9d0a9eb927dc84/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "99ec32b5690d",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash",
                "-c",
                "while true;do echo Jager;sleep 1;done"
            ],
            "Image": "centos",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "org.label-schema.build-date": "20201204",
                "org.label-schema.license": "GPLv2",
                "org.label-schema.name": "CentOS Base Image",
                "org.label-schema.schema-version": "1.0",
                "org.label-schema.vendor": "CentOS"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "4a7eef4d62eb047985dfc3c147c16229d2776361fd873868d3dfbf6e7fff05b2",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/4a7eef4d62eb",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "c999cdf3f2f5eefcead4c7d30e99cc4c9a5ad6c12375952446a12bcef8bc4145",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "bef7dabce0323b2e7fefecb3676b925734115105186fb10cb0f34774da19c310",
                    "EndpointID": "c999cdf3f2f5eefcead4c7d30e99cc4c9a5ad6c12375952446a12bcef8bc4145",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

```docker
docker exec -it 容器id /bin/bash	开启新的终端
docker attach 容器id 				进入正再执行的终端

docker cp 容器id:路径 宿主机路径
```

```docker
docker pull nginx
docker run -d --name jagd-nginx -p 3344:80 nginx
curl 127.0.0.1:3344
```

```docker
docker run -it --rm tomcat:9.0  用完即删
```

```elasticsearch
docker run -d --name elasticsearch --net somenetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.13.1

docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.13.1

docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" elasticsearch:7.13.1
```

```docker
docker run -d -p 8088:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --privileged=true portainer/portainer

docker commit -m="first" -a="wangyu" 容器id jagd-tomcat:1.0 
```

### 容器数据卷

```docker
docker run centos -it -v /home/test:/home /bin/bash

docker run -d --name jagd-mysql -p 3310:3306 -v /home/mysql/conf:/etc/mysql/conf.d -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:5.7.34

docker volume ls 
			  inspect 

docker run -d -P --name jagd-nginx -v 具名:/etc/nginx nginx
	/var/lib/docker/volumes/xxx/_data
	
docker run -d -P --name jagd-nginx -v 具名:/etc/nginx:ro nginx  只读
docker run -d -P --name jagd-nginx -v 具名:/etc/nginx:rw nginx  读写
```

### Docker File

```docker
FROM centos

VOLUME ["v1","v2"]

CMD echo "___end___"
CMD /bin/bash

docker build -f xxx -t xxx/centos:1.0 .
```

```contos
FROM centos
MAINTAINER Kaiser<5323368@qq.com>

ENV MYPATH /user/local
WORKDIR $MYPATH

RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80

CMD echo $MYPATH
CMD /bin/bash
```

```tomcat
DROM centos
MAINTAINER Kaiser<5323368@qq.com>

COPY text.txt /usr/local/readme.txt

ADD jdk-8u291-linux-x64.tar.gz /usr/local
ADD apache-tomcat-9.0.46.tar.gz /usr/local

RUN yum -y install vim
RUN yum -y install net-tools

ENV MYPATH /usr/local
WORKDIR $MYPATH

ENV JAVA_HOME /usr/local/jdk1.8.0_291
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-9.0.46
ENV CATALINA_BASE /usr/local/apache-tomcat-9.0.46
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/lib

EXPOSE 8080

CMD /usr/local/apache-tomcat-9.0.46/bin/startup.sh && tail -F /usr/local/apache-tomcat-9.0.46/bin/logs/catalina.out

CMD "---build end---"


docker build -t kaisercat .

docker run -d -p 9090:8080 --name kaisercat01 -v /home/kaiser/tomcat:/usr/local/apache-tomcat-9.0.46/wabapps/test -v /home/kaiser/tomecat/logs:/usr/local/apache-tomcat-9.0.46/logs 
```



```dockerfole
FROM 基础镜像
MAINTAINER 镜像制作人
RUN 镜像构建时运行的命令
ADD 添加压缩包
COPY 类似ADD,将我们的文件拷贝到镜像中
WORKDIR 镜像工作目录
VOLUME 挂在的目录
EXPOSE 暴露端口
CMD 这个容器启动时运行的命令,替换
ENTRYPOINT 这个容器启动时运行的命令,可以追加命令
ONBUILD 构建一个被继承 dockerfile 触发指令
ENV 设置镜像环境变量
```

```DOCKER
docker history 镜像id
```

```docker
docker network create --driver bridge --subnet 172.111.0.0/16 --gateway 172.111.0.1 buch
```

```redis
for port in $(seq 1 6); \
do \
mkdir -p /mydata/redis/node-${port}/conf
touch /mydata/redis/node-${port}/conf/redis.conf
cat  EOF /mydata/redis/node-${port}/conf/redis.conf
port 6379 
bind 0.0.0.0
cluster-enabled yes 
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 172.38.0.1${port}
cluster-announce-port 6379
cluster-announce-bus-port 16379
appendonly yes
EOF
done
```

```redis
docker run -p 6371:6379 -p 16371:16379 --name redis-1 \
    -v /mydata/redis/node-1/data:/data \
    -v /mydata/redis/node-1/conf/redis.conf:/etc/redis/redis.conf \
    -d --net redis --ip 172.38.0.11 redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf
```

```centos
centos8
firewall-cmd --zone=public --add-masquerade --permanent
firewall-cmd --reload
systemctl restart docker
```

```docker
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
```

```server
# root @ 8-200 in / [10:48:16] 
$ docker server --help

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/root/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  app*        Docker App (Docker Inc., v0.9.1-beta3)
  builder     Manage builds
  buildx*     Build with BuildKit (Docker Inc., v0.5.1-docker)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  scan*       Docker Scan (Docker Inc., v0.8.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/
```

```swarm
docker swarm init --advertise-addr 10.0.17.100

docker swarm join-token manager
docker swarm join-token worker

docker info

docker service rm helloworld

docker swarm leave
docker swarm init
```

```rm
yum remove docker \
docker-client \
docker-client-latest \
docker-common \
docker-latest \
docker-latest-logrotate \
docker-logrotate \
docker-selinux \
docker-engine-selinux \
docker-engine


rm -rf /etc/systemd/system/docker.service.d
 
rm -rf /var/lib/docker
 
rm -rf /var/run/docker
```

### elasticsearch&kinbana

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins elasticsearch:7.13.1
docker run -d --name kibana -e ELASTICSEARCH_HOSTS=http://10.0.24.100:9200 -p 5601:5601 kibana:7.13.1
server.port: 5601
server.host: 0.0.0.0
elasticsearch.hosts: [ "http://自己的IP地址:9200" ]
i18n.locale: "Zh-CN"
```



```
 9770  systemctl status docker
 9771  systemctl stop docker
 9772  systemctl status docker
 9773  yum remove docker \\
 9774                    docker-client \\
 9775                    docker-client-latest \\
 9776                    docker-common \\
 9777                    docker-latest \\
 9778                    docker-latest-logrotate \\
 9779                    docker-logrotate \\
 9780                    docker-engine
 9781  yum remove docker \\
 9782  docker-client \\
 9783  docker-client-latest \\
 9784  docker-common \\
 9785  docker-latest \\
 9786  docker-latest-logrotate \\
 9787  docker-logrotate \\
 9788  docker-selinux \\
 9789  docker-engine-selinux \\
 9790  docker-engine
 9791  rm -rf /etc/systemd/system/docker.service.d
 9792  rm -rf /var/lib/docker
 9793  rm -rf /var/run/docker
 9794  yum install -y yum-utils
 9795  yum makecache fast
 9796  yum-config-manager \\
 9797      --add-repo \\
 9798      http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
 9799  yum install docker-ce docker-ce-cli containerd.io
 9800  systemctl start docker
 9801  docker run hello-world
 9802  docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" elasticsearch:7.13.1
 9803  ls
 9804  df -h
 9805  docker imges
 9806  docker --help
 9807  docker image
 9808  htop
 9809  docker --help
 9810  docker images
 9811  docker stats
 9812  docker --help
 9813  docker images
 9814  docker pull kibana:7.13.1
 9815  docker images
 9816  cd /partita
 9817  ls
 9818  cd zhihu
 9819  ls
 9820  cd ..
 9821  mkdir -p elasticsearch/{config,data}
 9822  cd elasticsearch
 9823  ls
 9824  cd config
 9825  ls
 9826  cd ..
 9827  ll
 9828  chmod 777 config
 9829  ll
 9830  chmod 777 data
 9831  ls
 9832  cd data
 9833  ls
 9834  cd ..
 9835  cd config
 9836  vi elasticsearch.yml
 9837  docker status
 9838  docker --help
 9839  docker stats
 9840  docker stop b59e175c58d5
 9841  docker stats
 9842  docker run --name elasticsearch -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx128m" -v /mydata/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /mydata/elasticsearch/data:/usr/share/elasticsearch/data -v /mydata/elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.6.2
 9843  docker images
 9844  cd ..
 9845  mkdir plugins
 9846  ls
 9847  chmod 777 plugins
 9848  ll
 9849  cd plugins
 9850  ls
 9851  cd ..
 9852  docker run --name elasticsearch -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx128m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.13.1
 9853  docker ps
 9854  docker ps -a
 9855  docker rm $(docker ps -aq)
 9856  docker ps
 9857  docker ps -a
 9858  docker images
 9859  docker run --name elasticsearch -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx128m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.13.1
 9860  docker ps
 9861  docker ps -a
 9862  docker ps 
 9863  docker rm $(docker ps -aq)
 9864  docker run --name elasticsearch -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx128m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch
 9865  docker run --name es -p 9200:9200 -p 9300:9300  -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms1024m -Xmx2048m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins -d elasticsearch:7.13.1
 9866  docker ps
 9867  docker ps -a
 9868  docker log
 9869  docker --help
 9870  history
 9871  docker rm $(docker ps -aq)
 9872  docker ps
 9873  docker ps -a
 9874  docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins elasticsearch:7.13.1
 9875  docker ps -a
 9876  docker ps
 9877  docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins elasticsearch:7.13.1
 9878  cd ..
 9879  ls
 9880  cd elasticsearch
 9881  ls
 9882  rm -rf *
 9883  ls
 9884  cd ..
 9885  cd elasticsearch
 9886  mkdir {config,data}
 9887  ls
 9888  chmod 777 data
 9889  ls
 9890  echo "http.host: 0.0.0.0" >> /partita/elasticsearch/config/elasticsearch.yml
 9891  cd config
 9892  ls
 9893  ll
 9894  chmod 777 elasticsearch.yml
 9895  ls
 9896  cd 
 9897  docker rm $(docker ps -aq)
 9898  docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms8192m -Xmx16384m" -v /partita/elasticsearch/config/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -v /partita/elasticsearch/data:/usr/share/elasticsearch/data -v /partita/elasticsearch/plugins:/usr/share/elasticsearch/plugins elasticsearch:7.13.1
 9899  docker ps
 9900  docker run -d --name kibana -e ELASTICSEARCH_HOSTS=http://10.0.24.100:9200 -p 5601:5601 kibana:7.13.1
 9901  docker ps
 9902  docker exec -it 7b9e98b11345 /bin/bash
```

### web go

```
docker run -p 8001:8001 --name web_go_kuai -v /partita/goldberg:/partita/goldberg -d 
```































