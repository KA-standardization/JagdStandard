"""
https://github.com/kubernetes/kubernetes
https://dl.k8s.io/v1.23.1/kubernetes-server-linux-amd64.tar.gz
kubernetes.tar.gz包含了k8s的全部服务二进制文件和容器镜像文件 server binaries node binaries
master: etcd kube-apiserver kube-controller-manager kube-scheduler
worker: docker kubelet kube-proxy
"""
"""
master: kube-apiserver
使用openssl创建kube-apiserver的服务端CA证书，apiserver.key和apiserver.crt保存到/etc/kubernetes/pki
openssl genrsa -out apiserver.key 2048
openssl req -new -key apiserver.key -config master_ssl.cnf -subj "/CN=10.0.28.204" -out apiserver.csr
openssl x509 -req -in apiserver.csr -CA ca.crt -CAkey ca.key -CAcreateserial -days 36500 -extensions v3_req -extfile master_ssl.cnf -out apiserver.crt

master_ssl.cnf
[req]
req_extensions=v3_req
distinguished_name=req_distinguished_name
[req_distinguished_name]

[v3_req]
basicConstraints=CA:FALSE
keyUsage=nonRepudiation,digitalSignature,keyEncipherment
subjectAltName=@alt_names

[alt_names]
DNS.1=kubernetes
DNS.2=kubernetes.default
DNS.3=kubernetes.default.svc
DNS.4=kubernetes.default.cluster.local
DNS.5=k8s-1
DNS.6=k8s-2
DNS.7=k8s-3
IP.1=169.169.0.1
IP.2=10.0.28.204
IP.3=10.0.28.205
IP.4=10.0.28.206
IP.5=10.0.28.100

systemd /usr/lib/systemd/system/kube-apiserver.service
[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes

[Service]
EnvironmentFile=/etc/kubernetes/apiserver
ExecStart=/usr/bin/kube-apiserver $KUBE_API_ARGS
Restart=always

[Install]
WantedBy=multi-user.target

/etc/kubernetes/apiserver
KUBE_API_ARGS="\
--insecure-port=0 \
--secure-port=6443 \
--tls-cert-file=/etc/kubernetes/pki/apiserver.crt \
--tls-private-key-file=/etc/kubernetes/pki/apiserver.key \
--client-ca-file=/etc/kubernetes/pki/ca.crt \
--apiserver-count=3 \
--endpoint-reconciler-type=master-count \
--etcd-servers=https://10.0.28.204:2379,https://10.0.28.205:2379,https://10.0.28.206:2379 \
--etcd-cafile=/etc/kubernetes/pki/ca.crt \
--etcd-certfile=/etc/etcd/pki/etcd_client.crt \
--etcd-keyfile=/etc/etcd/pki/etcd_client.key \
--service-cluster-ip-range=169.169.0.0/16 \
--service-node-port-range=30000-32767 \
--allow-privileged=true \
--logtostderr=false \
--log-dir=/var/log/kubernetes --v=0\
"

systemctl start kube-apiserver && systemctl enable kube-apiserver
"""