"""
CRI container runtime interface
kubelet使用gRPC框架通过UNIX Socket与CRI代理进行通信，这个过程中kubelet是客户端，CRI代理是服务端
Protocol Buffers包含两个gRPC服务，
imageservice: 拉取镜像，查看，移除镜像的功能
runtimeservice: Pod，容器生命周期管理，以及与容器交互(exec attach port-forward),
                CRI代理可以使用一个Socket同时提供两个服务，
                在kubelet中: --container-runtime-endpoint
                            --image-server-endpoint
"""
"""
Pod和container生命周期管理
启动Pod之前，kubelet调用RuntimeService.RunPodSandbox创建环境
"""
"""
kubectl命令行语法
$kubectl command type name flag
        command: 操作资源对象 create,get,describe,delete
        type: 资源对象类型 pod pods po
        name: 资源对象名称 
        flag: 子命令可选参数 -s或--server设置APIServer的URL地址
ex
    获取多个相同类型资源信息 $kubectl get pod example1 example2 
    获取多个不同类型资源信息 $kubectl get pod/example1 replicationcontroller/example2
    应用多个YAML文件 $kubectl get pod -f pod1.yaml -f pod2.yaml
                   $kubectl create -f pod1.yaml -f rc1.yaml -f service1.yaml
"""
"""
command
alpha               $kubectl alpha [subcommand] [flag]
                    显示alpha版本的可用命令，例debug
annotate            $kubectl annotate (-f filename|type name|type/name) key1=val1...kn=vn [--overwrite] [--all] [--resource-version] [flag] 注释
                    添加或更新资源对象的注释信息
api-versions        $kubectl api-versions [flag]
                    列出当前系统版本支持的API列表，格式为group/version
apply               $kubectl apply -f filename [flag]
                    从配置文件或stdin中对资源对象进行配置更新
attach              $kubectl attach POD -c CONTAINER [flag] 依附
                    附着在一个正在运行的容器上
auth                $kubectl auth [flag] [options] 授权
                    检测RBAC权限设置
autoscale           $kubectl autoscale (-f filename|type name|type/name) [--min=MINPODS] --max=MAXPODS [--cpu-percent=CPU] [flag] 改变尺寸
                    对deployment replicaSet或ReplicationController进行自动水平扩容缩容
certificate         $kubectl certificate subcommand [options] 证书
                    修改证书资源
cluster-info        $kubectl cluster-info [flag]
                    显示集群master和内置服务信息
completion          $kubectl completion SHELL [flag] 完成
                    输出shell命令的运行结果码（bash/zsh）
config              $kubectl config subcommand [flag]
                    修改kubeconfig文件
convert             $kubectl convert -f filename [flag] 转换
                    转换配置文件为不同的API版本，文件类型可为yaml/json
cordon              $kubectl cordon NODE [flag] 隔离带
                    将node标记为unschedulable(计划外)，隔离出集群调度范围
cp                  $kubectl cp <file-spec-src> <file-spec-dest> [options]
                    从容器中复制文件/目录到主机，反之亦然
create              $kubectl create -f filename [flag]
                    从配置文件/stdin中创建资源对象
delete              $kubectl delete (-f filename|type [name|/name|-l label|--all]) [flag]
                    根据配置文件，stdin，资源名称或label selector删除资源
describe            $kubectl describe (-f filename|type [name_prefix|/name|-l label]) [flag]
                    描述一个或多个资源对象的详细信息
diff                $kubectl diff -f filename [options]
                    查看配置文件与当前系统中正在运行的资源的差异
drain               $kubectl drain NODE [flag] 排出
                    将NODE设为离群，然后删除在NODE上运行的所有POD，但不会删除不由APIserver管理的POD
edit                $kubectl edit (-f filename|type name|type/name) [flag]
                    编辑资源对象的属性，在线更新
exec                $kubectl exec POD [-c container] [-i] [-t] [flag] [-- command[args...]]
                    运行一个容器中的命令
explain             $kubectl explain [--include-extended-apis=true] [--recursive(循环)=false] [flag]
                    对资源对象属性的详细说明
expose              $kubectl expose (-f filename|type name|type/name) [--port=port] [--protocol=TCP/UDP] [--target-port=number-or-name] [--name=name] [--external(外部的)-api=external-ip-of-service] [--type=type] [flag] 暴露
                    将一个已经存在的RC，Service，Deployment或Pod暴露为一个新的Service
get                 $kubectl get (-f filename|type [name|/name|-l label]) [--watch] [--sort-by=FIELD] [[-o|--output]=OUTPUT_FORMAT] [flag]
                    显示一个或多个资源的概要信息
kustomize           $kubectl kustomize <dir> [flag] [options] 
                    列出基于kustomization.yaml配置文件生成的API资源对象，参数必须是包含kustomization.yaml目录名或一个Git库的URL地址









"""
