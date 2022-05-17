"""
Master高可用架构
集群中的各资源对象的状态则被保存在etcd数据库中
1. master的 kube-apiserver kube-controller-mansger kube-scheduler服务至少以3个节点的多实例方式部署
2. master启用基于CA认证的HTTPS安全机制
3. etcd至少以3个节点的集群模式部署
4. etcd集群启用基于CA认证的HTTPS安全机制
5. master启用RBAC授权模式
"""
"""
自签名的CA证书来完成安全配置
etcd和k8s在制作CA证书时，均需要CA根证书
CA根证书命令，包括私钥文件ca.key和证书文件ca.crt
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -subj "/CN=10.0.28.204" -days 36500 -out ca.crt
将生成的ca.key和ca.crt文件保存在/etc/kubernetes/pki目录下
"""
"""
etcd高可用集群
etcd作为k8s集群的主数据库，在安装k8s各服务之前需要首先安装和启动
1. 下载etcd二进制文件，配置systemd服务
github官网下载etcd二进制
解压后得到etcd和etcdctl文件，复制到/usr/bin下
然后将其部署为一个systemd服务
创建/usr/lib/systemd/system/etcd.service
[Unit]
Description=etcd key-value store
Documentation=https://github.com/etcd-io/etcd
After=network.target

[Service]
EnvironmentFile=/etc/etcd/etcd.conf
ExecStart=/usr/bin/etcd
Restart=always

[Install]
WantedBy=multi-user.target
"""
"""
/etc/etcd/etcd.conf
ETCD_NAME=etcd1
ETCD_DATA_DIR=/etc/etcd/data
ETCD_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_CLIENT_CERT_AUTH=true
ETCD_LISTEN_CLIENT_URLS=https://10.0.28.204:2379
ETCD_ADVERTISE_CLIENT_URLS=https://10.0.28.204:2379
ETCD_PEER_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_PEER_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_PEER_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_LISTEN_PEER_URLS=https://10.0.28.204:2380
ETCD_INITIAL_ADVERTISE_PEER_URLS=https://10.0.28.204:2380
ETCD_INITIAL_CLUSTER_TOKEN=etcd-cluster
ETCD_INITIAL_CLUSTER="etcd1=https://10.0.28.204:2380,etcd2=https://10.0.28.205:2380,etcd3=https://10.0.28.206:2380"
ETCD_INITIAL_CLUSTER_STATE=new

ETCD_NAME=etcd2
ETCD_DATA_DIR=/etc/etcd/data
ETCD_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_CLIENT_CERT_AUTH=true
ETCD_LISTEN_CLIENT_URLS=https://10.0.28.205:2379
ETCD_ADVERTISE_CLIENT_URLS=https://10.0.28.205:2379
ETCD_PEER_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_PEER_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_PEER_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_LISTEN_PEER_URLS=https://10.0.28.205:2380
ETCD_INITIAL_ADVERTISE_PEER_URLS=https://10.0.28.205:2380
ETCD_INITIAL_CLUSTER_TOKEN=etcd-cluster
ETCD_INITIAL_CLUSTER="etcd1=https://10.0.28.204:2380,etcd2=https://10.0.28.205:2380,etcd3=https://10.0.28.206:2380"
ETCD_INITIAL_CLUSTER_STATE=new

ETCD_NAME=etcd3
ETCD_DATA_DIR=/etc/etcd/data
ETCD_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_CLIENT_CERT_AUTH=true
ETCD_LISTEN_CLIENT_URLS=https://10.0.28.206:2379
ETCD_ADVERTISE_CLIENT_URLS=https://10.0.28.206:2379
ETCD_PEER_CERT_FILE=/etc/etcd/pki/etcd_server.crt
ETCD_PEER_KEY_FILE=/etc/etcd/pki/etcd_server.key
ETCD_PEER_TRUSTED_CA_FILE=/etc/kubernetes/pki/ca.crt
ETCD_LISTEN_PEER_URLS=https://10.0.28.206:2380
ETCD_INITIAL_ADVERTISE_PEER_URLS=https://10.0.28.206:2380
ETCD_INITIAL_CLUSTER_TOKEN=etcd-cluster
ETCD_INITIAL_CLUSTER="etcd1=https://10.0.28.204:2380,etcd2=https://10.0.28.205:2380,etcd3=https://10.0.28.206:2380"
ETCD_INITIAL_CLUSTER_STATE=new
"""
"""
创建etcd的CA证书
1创建一个x509 v3配置文件etcd_ssl.cnf
[req]
req_extensions=v3_req
distinguished_name=req_distinguished_name
[req_distinguished_name]
[v3_req]
basicConstraints=CA:FALSE
keyUsage=nonRepudiation,digitalSignature,keyEncipherment
subjectAltName=@alt_names
[alt_names]
IP.1=10.0.28.204
IP.2=10.0.28.205
IP.3=10.0.28.206

创建etcd服务端客户端使用的CA证书将其保存在/etc/etcd/pki下
openssl genrsa -out etcd_server.key 2048
openssl req -new -key etcd_server.key -config etcd_ssl.cnf -subj "/CN=etcd-server" -out etcd_server.csr
openssl x509 -req -in etcd_server.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -days 36500 -extensions v3_req -extfile etcd_ssl.cnf -out etcd_server.crt
openssl genrsa -out etcd_client.key 2048
openssl req -new -key etcd_client.key -config etcd_ssl.cnf -subj "/CN=etcd-client" -out etcd_client.csr
openssl x509 -req -in etcd_client.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -days 36500 -extensions v3_req -extfile etcd_ssl.cnf -out etcd_client.crt

hostnamectl set-hostname etcd1
cat << EOF >> /etc/hosts
10.0.28.204 etcd1
10.0.28.205 etcd2
10.0.28.206 etcd3
EOF

启动etcd集群
systemctl restart etcd && systemctl enable etcd
验证集群状态
etcdctl --cacert=/etc/kubernetes/pki/ca.crt --cert=/etc/etcd/pki/etcd_client.crt --key=/etc/etcd/pki/etcd_client.key --endpoints=https://10.0.28.204:2379,https://10.0.28.205:2379,https://10.0.28.206:2379 endpoint health
"""






