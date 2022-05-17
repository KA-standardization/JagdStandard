yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl start kubelet
systemctl enable kubelet
swapoff -a
vi /etc/docker/daemon.json


