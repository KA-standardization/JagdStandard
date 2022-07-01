```install
# root @ 8-200 in / [15:44:44] C:1
$ yum install -y etcd kubernetes   
```

```start
systemctl start etcd
systemctl start docker 
systemctl start kube-apiserver 
systemctl start kube-controller-manager 
systemctl start kube-scheduler 
systemctl start kubelet 
systemctl start kube-proxy

systemctl stop etcd
systemctl stop docker 
systemctl stop kube-apiserver 
systemctl stop kube-controller-manager 
systemctl stop kube-scheduler 
systemctl stop kubelet 
systemctl stop kube-proxy
```

```kubectl
$ kubectl --help  
Kubernetes command line client

Usage:
  Kubernetes command line client [flags]

Available Flags:
      --allow-verification-with-non-compliant-keys   Allow a SignatureVerifier to use keys which are technically non-compliant with RFC6962.
      --alsologtostderr                              log to standard error as well as files
      --application-metrics-count-limit int          Max number of application metrics to store (per container) (default 100)
      --as string                                    Username to impersonate for the operation
      --azure-container-registry-config string       Path to the file container Azure container registry configuration information.
      --boot-id-file string                          Comma-separated list of files to check for boot-id. Use the first one that exists. (default "/proc/sys/kernel/random/boot_id")
      --certificate-authority string                 Path to a cert. file for the certificate authority
      --client-certificate string                    Path to a client certificate file for TLS
      --client-key string                            Path to a client key file for TLS
      --cluster string                               The name of the kubeconfig cluster to use
      --container-hints string                       location of the container hints file (default "/etc/cadvisor/container_hints.json")
      --context string                               The name of the kubeconfig context to use
      --docker string                                docker endpoint (default "unix:///var/run/docker.sock")
      --docker-env-metadata-whitelist string         a comma-separated list of environment variable keys that needs to be collected for docker containers
      --docker-only                                  Only report docker containers in addition to root stats
      --docker-root string                           DEPRECATED: docker root is read from docker info (this is a fallback, default: /var/lib/docker) (default "/var/lib/docker")
      --enable-load-reader                           Whether to enable cpu load reader
      --event-storage-age-limit string               Max length of time for which to store events (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is a duration. Default is applied to all non-specified event types (default "default=0")
      --event-storage-event-limit string             Max number of events to store (per type). Value is a comma separated list of key values, where the keys are event types (e.g.: creation, oom) or "default" and the value is an integer. Default is applied to all non-specified event types (default "default=0")
      --global-housekeeping-interval duration        Interval between global housekeepings (default 1m0s)
      --google-json-key string                       The Google Cloud Platform Service Account JSON Key to use for authentication.
  -h, --help                                         help for hyperkube
      --housekeeping-interval duration               Interval between container housekeepings (default 10s)
      --insecure-skip-tls-verify                     If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure
      --ir-data-source string                        Data source used by InitialResources. Supported options: influxdb, gcm. (default "influxdb")
      --ir-dbname string                             InfluxDB database name which contains metrics required by InitialResources (default "k8s")
      --ir-hawkular string                           Hawkular configuration URL
      --ir-influxdb-host string                      Address of InfluxDB which contains metrics required by InitialResources (default "localhost:8080/api/v1/proxy/namespaces/kube-system/services/monitoring-influxdb:api")
      --ir-namespace-only                            Whether the estimation should be made only based on data from the same namespace.
      --ir-password string                           Password used for connecting to InfluxDB (default "root")
      --ir-percentile int                            Which percentile of samples should InitialResources use when estimating resources. For experiment purposes. (default 90)
      --ir-user string                               User used for connecting to InfluxDB (default "root")
      --kubeconfig string                            Path to the kubeconfig file to use for CLI requests.
      --log-backtrace-at traceLocation               when logging hits line file:N, emit a stack trace (default :0)
      --log-cadvisor-usage                           Whether to log the usage of the cAdvisor container
      --log-dir string                               If non-empty, write log files in this directory
      --log-flush-frequency duration                 Maximum number of seconds between log flushes (default 5s)
      --logtostderr                                  log to standard error instead of files (default true)
      --machine-id-file string                       Comma-separated list of files to check for machine-id. Use the first one that exists. (default "/etc/machine-id,/var/lib/dbus/machine-id")
      --match-server-version                         Require server version to match client version
  -n, --namespace string                             If present, the namespace scope for this CLI request
      --password string                              Password for basic authentication to the API server
      --request-timeout string                       The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests. (default "0")
  -s, --server string                                The address and port of the Kubernetes API server
      --stderrthreshold severity                     logs at or above this threshold go to stderr (default 2)
      --storage-driver-buffer-duration duration      Writes in the storage driver will be buffered for this duration, and committed to the non memory backends as a single transaction (default 1m0s)
      --storage-driver-db string                     database name (default "cadvisor")
      --storage-driver-host string                   database host:port (default "localhost:8086")
      --storage-driver-password string               database password (default "root")
      --storage-driver-secure                        use secure connection with database
      --storage-driver-table string                  table name (default "stats")
      --storage-driver-user string                   database username (default "root")
      --token string                                 Bearer token for authentication to the API server
      --user string                                  The name of the kubeconfig user to use
      --username string                              Username for basic authentication to the API server
  -v, --v Level                                      log level for V logs
      --version version[=true]                       Print version information and quit
      --vmodule moduleSpec                           comma-separated list of pattern=N settings for file-filtered logging

```

```shell
kubeadm reset

rm -rf ~/.kube/
rm -rf /etc/kubernetes/
rm -rf /etc/systemd/system/kubelet.service.d
rm -rf /etc/systemd/system/kubelet.service
rm -rf /usr/bin/kube*
rm -rf /etc/cni
rm -rf /opt/cni
rm -rf /var/lib/etcd
rm -rf /var/etcd
yum clean all
yum remove kube*
```

