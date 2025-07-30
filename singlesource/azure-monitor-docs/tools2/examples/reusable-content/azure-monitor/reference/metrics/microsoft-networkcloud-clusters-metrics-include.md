---
ms.topic: include
ms.date: 04/16/2025
ms.custom: Microsoft.NetworkCloud/clusters, naam

# NOTE:  This content is automatically generated using API calls to Azure. Any edits made on these files will be overwritten in the next run of the script. 
 
---




### Category: API Server
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**APIServer Audit Requests Rejected Total**<br><br>Counter of API server requests rejected due to an error in the audit logging backend. In the absence of data, this metric will retain the most recent value emitted. |`ApiserverAuditRequestsRejectedTotal` |Count |Average |`Component`, `Pod Name`|PT1M |No|
|**APIServer Clnt Cert Exp Sec Sum (Preview)**<br><br>Sum of API server client certificate expiration. In the absence of data, this metric will retain the most recent value emitted. |`ApiserverClientCertificateExpirationSecondsSum` |Seconds |Average |`Component`, `Pod Name`|PT1M |No|
|**APIServer Storage Data Key Gen Fail**<br><br>Total number of operations that failed Data Encryption Key (DEK) generation. In the absence of data, this metric will retain the most recent value emitted. |`ApiserverStorageDataKeyGenerationFailuresTotal` |Count |Average |`Component`, `Pod Name`|PT1M |No|
|**APIServer TLS Handshake Err (Preview)**<br><br>Number of requests dropped with 'TLS handshake' error. In the absence of data, this metric will retain the most recent value emitted. |`ApiserverTlsHandshakeErrorsTotal` |Count |Average |`Component`, `Pod Name`|PT1M |No|

### Category: Calico
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Felix Active Local Endpoints**<br><br>Number of active endpoints on this host. In the absence of data, this metric will retain the most recent value emitted. |`FelixActiveLocalEndpoints` |Count |Average |`Host`|PT1M |No|
|**Felix Cluster Num Host Endpoints**<br><br>Total number of host endpoints cluster-wide. In the absence of data, this metric will retain the most recent value emitted. |`FelixClusterNumHostEndpoints` |Count |Average |`Host`|PT1M |No|
|**Felix Cluster Number of Hosts**<br><br>Total number of Calico hosts in the cluster. In the absence of data, this metric will retain the most recent value emitted. |`FelixClusterNumHosts` |Count |Average |`Host`|PT1M |No|
|**Felix Cluster Nmbr Workload Endpoints**<br><br>Total number of workload endpoints cluster-wide. In the absence of data, this metric will retain the most recent value emitted. |`FelixClusterNumWorkloadEndpoints` |Count |Average |`Host`|PT1M |No|
|**Felix Interface Dataplane Failures**<br><br>Number of times dataplane updates failed and will be retried. In the absence of data, this metric will retain the most recent value emitted. |`FelixIntDataplaneFailures` |Count |Average |`Host`|PT1M |No|
|**Felix Ipset Errors**<br><br>Number of 'ipset' command failures. In the absence of data, this metric will retain the most recent value emitted. |`FelixIpsetErrors` |Count |Average |`Host`|PT1M |No|
|**Felix Ipsets Calico**<br><br>Number of active Calico IP sets. In the absence of data, this metric will retain the most recent value emitted. |`FelixIpsetsCalico` |Count |Average |`Host`|PT1M |No|
|**Felix IP Tables Restore Errors**<br><br>Number of 'iptables-restore' errors. In the absence of data, this metric will retain the most recent value emitted. |`FelixIptablesRestoreErrors` |Count |Average |`Host`|PT1M |No|
|**Felix IP Tables Save Errors**<br><br>Number of 'iptables-save' errors. In the absence of data, this metric will retain the most recent value emitted. |`FelixIptablesSaveErrors` |Count |Average |`Host`|PT1M |No|
|**Felix Resyncs Started**<br><br>Number of times Felix has started resyncing with the datastore. In the absence of data, this metric will retain the most recent value emitted. |`FelixResyncsStarted` |Count |Average |`Host`|PT1M |No|
|**Felix Resync State**<br><br>Current datastore state. In the absence of data, this metric will retain the most recent value emitted. |`FelixResyncState` |Unspecified |Average |`Host`|PT1M |No|
|**Typha Client Latency Secs**<br><br>Per-client latency: how far behind the current state each client is. In the absence of data, this metric will retain the most recent value emitted. |`TyphaClientLatencySecsCount` |Count |Average |`Pod Name`|PT1M |No|
|**Typha Connections Accepted**<br><br>Total number of connections accepted over time. In the absence of data, this metric will retain the most recent value emitted. |`TyphaConnectionsAccepted` |Count |Average |`Pod Name`|PT1M |No|
|**Typha Connections Dropped**<br><br>Total number of connections dropped due to rebalancing. In the absence of data, this metric will retain the most recent value emitted. |`TyphaConnectionsDropped` |Count |Average |`Pod Name`|PT1M |No|
|**Typha Ping Latency**<br><br>Round-trip ping latency to client. Typha's protocol includes a regular ping keepalive to verify that the connection is still up. In the absence of data, this metric will retain the most recent value emitted. |`TyphaPingLatencyCount` |Count |Average |`Pod Name`|PT1M |No|

### Category: Container
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Container FS I/O Time Seconds Total (Preview)**<br><br>Time taken for container Input/Output (I/O) operations. In the absence of data, this metric will retain the most recent value emitted. |`ContainerFsIoTimeSecondsTotal` |Seconds |Average |`Device`, `Host`|PT1M |No|
|**Container Memory Fail Count**<br><br>Number of times a container's memory usage limit is hit. In the absence of data, this metric will default to 0. |`ContainerMemoryFailcnt` |Count |Average |`Container`, `Host`, `Namespace`, `Pod`|PT1M |No|
|**Container Memory Usage Bytes**<br><br>Current memory usage, including all memory regardless of when it was accessed. In the absence of data, this metric will default to 0. |`ContainerMemoryUsageBytes` |Bytes |Average |`Container`, `Host`, `Namespace`, `Pod`|PT1M |No|
|**Container Scrape Error**<br><br>Indicates whether there was an error while getting container metrics. In the absence of data, this metric will retain the most recent value emitted. |`ContainerScrapeError` |Unspecified |Average |`Host`|PT1M |No|
|**Container Tasks State**<br><br>Number of tasks or processes in a given state (sleeping, running, stopped, uninterruptible, or waiting) in a container. In the absence of data, this metric will retain the most recent value emitted. |`ContainerTasksState` |Count |Average |`Container`, `Host`, `Namespace`, `Pod`, `State`|PT1M |No|

### Category: Controller
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Controller Reconcile Errors Total (Deprecated)**<br><br>Total number of reconciliation errors per controller. In the absence of data, this metric will retain the most recent value emitted. |`ControllerRuntimeReconcileErrorsTotal` |Count |Average |`Controller`, `Namespace`, `Pod Name`|PT1M |No|
|**Controller Reconcile Errors Total**<br><br>Total number of reconciliation errors per controller. In the absence of data, this metric will retain the most recent value emitted. |`ControllerRuntimeReconcileErrorsTotal2` |Count |Average |`Controller`, `Namespace`, `Pod Name`|PT1M |No|
|**Controller Reconciliations Total (Deprecated)**<br><br>Total number of reconciliations per controller. In the absence of data, this metric will retain the most recent value emitted. |`ControllerRuntimeReconcileTotal` |Count |Average |`Controller`, `Namespace`, `Pod Name`|PT1M |No|
|**Controller Reconciliations Total**<br><br>Total number of reconciliations per controller. In the absence of data, this metric will retain the most recent value emitted. |`ControllerRuntimeReconcileTotal2` |Count |Average |`Controller`, `Namespace`, `Pod Name`|PT1M |No|

### Category: CoreDNS
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**CoreDNS Requests Total**<br><br>Total number of DNS requests recieved by a CoreDNS server. In the absence of data, this metric will retain the most recent value emitted. |`CorednsDnsRequestsTotal` |Count |Average |`Family`, `Pod Name`, `Proto`, `Server`, `Type`|PT1M |No|
|**CoreDNS Responses Total**<br><br>Total number of DNS responses sent by a CoreDNS server. In the absence of data, this metric will retain the most recent value emitted. |`CorednsDnsResponsesTotal` |Count |Average |`Pod Name`, `Server`, `Rcode`|PT1M |No|
|**CoreDNS Frwd Hlthchk Broken (Deprecated)**<br><br>Total number of times the health checks for all upstream DNS servers has failed. In the absence of data, this metric will retain the most recent value emitted. |`CorednsForwardHealthcheckBrokenTotal` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|
|**CoreDNS Frwd Hlthchk Broken**<br><br>Total number of times the health checks for all upstream DNS servers has failed. In the absence of data, this metric will retain the most recent value emitted. |`CorednsForwardHealthcheckBrokenTotal2` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|
|**CoreDNS Frwd Max Concurrent Rejects (Deprecated)**<br><br>Total number of rejected queries due to concurrent queries reaching the maximum limit. In the absence of data, this metric will retain the most recent value emitted. |`CorednsForwardMaxConcurrentRejectsTotal` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|
|**CoreDNS Frwd Max Concurrent Rejects**<br><br>Total number of rejected queries due to concurrent queries reaching the maximum limit. In the absence of data, this metric will retain the most recent value emitted. |`CorednsForwardMaxConcurrentRejectsTotal2` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|
|**CoreDNS Health Request Failures Total**<br><br>The number of times the self health check failed for a CoreDNS server. In the absence of data, this metric will retain the most recent value emitted. |`CorednsHealthRequestFailuresTotal` |Count |Average |`Pod Name`|PT1M |No|
|**CoreDNS Panics Total**<br><br>Total number of unexpected errors (panics) that have occurred in a CoreDNS server. In the absence of data, this metric will retain the most recent value emitted. |`CorednsPanicsTotal` |Count |Average |`Pod Name`|PT1M |No|
|**CoreDNS Reload Failed Total (Deprecated)**<br><br>Total number of failed attempts CoreDNS has had when reloading its configuration. In the absence of data, this metric will retain the most recent value emitted. |`CorednsReloadFailedTotal` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|
|**CoreDNS Reload Failed Total**<br><br>Total number of failed attempts CoreDNS has had when reloading its configuration. In the absence of data, this metric will retain the most recent value emitted. |`CorednsReloadFailedTotal2` |Count |Average |`Pod Name`, `Namespace`|PT1M |No|

### Category: Daemonset
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Daemonsets Current Number Scheduled**<br><br>Number of daemonsets currently scheduled. In the absence of data, this metric will default to 0. |`KubeDaemonsetStatusCurrentNumberScheduled` |Count |Average |`Daemonset`, `Namespace`|PT1M |No|
|**Daemonsets Desired Number Scheduled**<br><br>Number of daemonsets desired scheduled. In the absence of data, this metric will default to 0. |`KubeDaemonsetStatusDesiredNumberScheduled` |Count |Average |`Daemonset`, `Namespace`|PT1M |No|
|**Daemonsets Not Scheduled**<br><br>Number of daemonsets not scheduled. In the absence of data, this metric will default to 150. |`KubeDaemonsetStatusNotScheduled` |Count |Average |`Daemonset`, `Namespace`|PT1M |No|

### Category: Deployment
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Deployment Replicas Available**<br><br>Number of deployment replicas available. In the absence of data, this metric will default to 0. |`KubeDeploymentStatusReplicasAvailable` |Count |Average |`Deployment`, `Namespace`|PT1M |No|
|**Deployment Replicas Available Percent**<br><br>Percentage of deployment replicas available. In the absence of data, this metric will default to 0. |`KubeDeploymentStatusReplicasAvailablePercent` |Percent |Average |`Deployment`, `Namespace`|PT1M |No|
|**Deployment Replicas Ready**<br><br>Number of deployment replicas ready. In the absence of data, this metric will retain the most recent value emitted. |`KubeDeploymentStatusReplicasReady` |Count |Average |`Deployment`, `Namespace`|PT1M |No|
|**Deployment Replicas Unavailable**<br><br>Number of deployment replicas unavailable. In the absence of data, this metric will retain the most recent value emitted. |`KubeDeploymentStatusReplicasUnavailable` |Count |Average |`Deployment`, `Namespace`|PT1M |No|
|**NFS Volume Size Bytes**<br><br>Total Size of the NFS volume. In the absence of data, this metric will retain the most recent value emitted. |`NfsVolumeSizeBytes` |Bytes |Average |`CSN Name`|PT1M |No|
|**NFS Volume Used Bytes**<br><br>Size of NFS volume used. In the absence of data, this metric will retain the most recent value emitted. |`NfsVolumeUsedBytes` |Bytes |Average |`CSN Name`|PT1M |No|
|**Storage control-plane connectivity (Preview)**<br><br>Cluster's connectivity status to the storage appliance. In the absence of data, this metric will default to 0. |`StorageControlPlaneConnectivity` |Count |Average |`Appliance Name`, `Node`, `Endpoint`, `State`|PT1M |No|

### Category: Etcd
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Etcd Database Utilization Percentage**<br><br>The percentage of the Etcd Database utilized. In the absence of data, this metric will default to 0. |`EtcdDBUtilizationPercent` |Percent |Average |`Pod Name`|PT1M |No|
|**Etcd Disk Backend Commit Duration Sec**<br><br>The cumulative sum of the time taken for etcd to commit transactions to its backend disk storage. In the absence of data, this metric will retain the most recent value emitted. |`EtcdDiskBackendCommitDurationSecondsSum` |Seconds |Total (Sum) |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Disk WAL Fsync Duration Sec**<br><br>The cumulative sum of of the time that etcd has spent performing fsync operations on the write-ahead log (WAL) file. In the absence of data, this metric will retain the most recent value emitted. |`EtcdDiskWalFsyncDurationSecondsSum` |Seconds |Total (Sum) |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Health Failures**<br><br>Total number of failed health checks performed on an etcd server. In the absence of data, this metric will default to 0. |`EtcdServerHealthFailures` |Count |Average |`Pod Name`|PT1M |No|
|**Etcd Server Is Leader**<br><br>Indicates whether an etcd server the leader of the cluster; 1 if is, 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerIsLeader` |Unspecified |Count |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Is Learner**<br><br>Indicates whether an etcd server a learner within the cluster; 1 if is, 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerIsLearner` |Unspecified |Count |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Leader Changes Seen Total**<br><br>The number of leader changes seen within the etcd cluster. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerLeaderChangesSeenTotal` |Count |Average |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Proposals Applied Total**<br><br>The total number of consensus proposals that have been successfully applied. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerProposalsAppliedTotal` |Count |Average |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Proposals Committed Total**<br><br>The total number of consensus proposals that have been committed. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerProposalsCommittedTotal` |Count |Average |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Proposals Failed Total**<br><br>The total number of failed consensus proposals. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerProposalsFailedTotal` |Count |Average |`Component`, `Pod Name`, `Tier`|PT1M |No|
|**Etcd Server Slow Apply Total (Preview)**<br><br>The total number of etcd apply requests that took longer than expected. In the absence of data, this metric will retain the most recent value emitted. |`EtcdServerSlowApplyTotal` |Count |Average |`Pod Name`, `Tier`|PT1M |No|

### Category: Job
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Jobs Active**<br><br>Number of jobs active. In the absence of data, this metric will default to 0. |`KubeJobStatusActive` |Count |Average |`Job`, `Namespace`|PT1M |No|
|**Jobs Failed**<br><br>Number and reason of jobs failed. In the absence of data, this metric will retain the most recent value emitted. |`KubeJobStatusFailedReasons` |Count |Average |`Job`, `Namespace`, `Reason`|PT1M |No|
|**Jobs Succeeded**<br><br>Number of jobs succeeded. In the absence of data, this metric will default to 0. |`KubeJobStatusSucceeded` |Count |Average |`Job`, `Namespace`|PT1M |No|

### Category: Kubelet
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Kubelet Running Containers**<br><br>Number of containers currently running. In the absence of data, this metric will retain the most recent value emitted. |`KubeletRunningContainers` |Count |Average |`Container State`, `Host`|PT1M |No|
|**Kubelet Running Pods**<br><br>Number of pods running on the node. In the absence of data, this metric will retain the most recent value emitted. |`KubeletRunningPods` |Count |Average |`Host`|PT1M |No|
|**Kubelet Runtime Operations Errors Total**<br><br>Cumulative number of runtime operation errors by operation type. In the absence of data, this metric will retain the most recent value emitted. |`KubeletRuntimeOperationsErrorsTotal` |Count |Average |`Host`, `Operation Type`|PT1M |No|
|**Kubelet Started Pods Errors Total**<br><br>Cumulative number of errors when starting pods. In the absence of data, this metric will retain the most recent value emitted. |`KubeletStartedPodsErrorsTotal` |Count |Average |`Host`|PT1M |No|

### Category: Network Cloud
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**CPU Pinning Map (Preview)**<br><br>Pinning map of virtual CPUs (vCPUs) to CPUs. In the absence of data, this metric will retain the most recent value emitted. |`NcVmiCpuAffinity` |Count |Average |`CPU`, `NUMA Node`, `VMI Namespace`, `VMI Node`, `VMI Name`|PT1M |No|

### Category: Nexus Cluster
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Cluster Heartbeat Connection Status**<br><br>Indicates whether the Cluster is having issues communicating with the Cluster Manager. The value of the metric is 0 when the connection is healthy and 1 when it is unhealthy. In the absence of data, this metric will retain the most recent value emitted. |`NexusClusterHeartbeatConnectionStatus` |Count |Average |`Reason`|PT1M |No|
|**Cluster Machine Group Upgrade**<br><br>Tracks Cluster Machine Group Upgrades performed. The value of the metric is 0 when the result is successful and 1 for all other results. In the absence of data, this metric will retain the most recent value emitted. |`NexusClusterMachineGroupUpgrade` |Count |Average |`Machine Group`, `Result`, `Upgraded From Version`, `Upgraded To Version`|PT1M |No|

### Category: Node
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Node Resources Allocatable**<br><br>Node resources allocatable for pods. In the absence of data, this metric will retain the most recent value emitted. |`KubeNodeStatusAllocatable` |Count |Average |`Node`, `Resource`, `Unit`|PT1M |No|
|**Node Resources Capacity**<br><br>Total amount of node resources available. In the absence of data, this metric will retain the most recent value emitted. |`KubeNodeStatusCapacity` |Count |Average |`Node`, `Resource`, `Unit`|PT1M |No|
|**Node Status Condition**<br><br>The condition of a node. In the absence of data, this metric will retain the most recent value emitted. |`KubeNodeStatusCondition` |Count |Average |`Condition`, `Node`, `Status`|PT1M |No|

### Category: Pod
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Container Resources Limits**<br><br>The container's resources limits. In the absence of data, this metric will default to 0. |`KubePodContainerResourceLimits` |Count |Average |`Container`, `Namespace`, `Node`, `Pod`, `Resource`, `Unit`|PT1M |No|
|**Container Resources Requests**<br><br>The container's resources requested. In the absence of data, this metric will default to 0. |`KubePodContainerResourceRequests` |Count |Average |`Container`, `Namespace`, `Node`, `Pod`, `Resource`, `Unit`|PT1M |No|
|**Container State Started (Preview)**<br><br>Unix timestamp start time of a container. In the absence of data, this metric will default to 0. |`KubePodContainerStateStarted` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Status Last Terminated Reason**<br><br>The reason of a container's last terminated status. In the absence of data, this metric will default to 0. |`KubePodContainerStatusLastTerminatedReason` |Count |Average |`Container`, `Namespace`, `Pod`, `Reason`|PT1M |No|
|**Container Status Ready**<br><br>Describes whether the container's readiness check succeeded. In the absence of data, this metric will default to 0. |`KubePodContainerStatusReady` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Restarts**<br><br>The number of container restarts. In the absence of data, this metric will retain the most recent value emitted. |`KubePodContainerStatusRestartsTotal` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Status Running**<br><br>The number of containers with a status of 'running'. In the absence of data, this metric will default to 0. |`KubePodContainerStatusRunning` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Status Terminated**<br><br>The number of containers with a status of 'terminated'. In the absence of data, this metric will default to 0. |`KubePodContainerStatusTerminated` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Status Terminated Reason**<br><br>The number and reason of containers with a status of 'terminated'. In the absence of data, this metric will retain the most recent value emitted. |`KubePodContainerStatusTerminatedReasons` |Count |Average |`Container`, `Namespace`, `Pod`, `Reason`|PT1M |No|
|**Container Status Waiting**<br><br>The number of containers with a status of 'waiting'. In the absence of data, this metric will default to 0. |`KubePodContainerStatusWaiting` |Count |Average |`Container`, `Namespace`, `Pod`|PT1M |No|
|**Container Status Waiting Reason**<br><br>The number and reason of containers with a status of 'waiting'. In the absence of data, this metric will default to 0. |`KubePodContainerStatusWaitingReason` |Count |Average |`Container`, `Namespace`, `Pod`, `Reason`|PT1M |No|
|**Pod Deletion Timestamp (Preview)**<br><br>The timestamp of the pod's deletion. In the absence of data, this metric will default to 0. |`KubePodDeletionTimestamp` |Count |Average |`Namespace`, `Pod`|PT1M |No|
|**Pod Init Container Ready**<br><br>The number of ready pod init containers. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusReady` |Count |Average |`Namespace`, `Container`, `Pod`|PT1M |No|
|**Pod Init Container Restarts**<br><br>The number of pod init containers restarts. In the absence of data, this metric will retain the most recent value emitted. |`KubePodInitContainerStatusRestartsTotal` |Count |Average |`Namespace`, `Container`, `Pod`|PT1M |No|
|**Pod Init Container Running**<br><br>The number of running pod init containers. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusRunning` |Count |Average |`Namespace`, `Container`, `Pod`|PT1M |No|
|**Pod Init Container Terminated**<br><br>The number of terminated pod init containers. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusTerminated` |Count |Average |`Namespace`, `Container`, `Pod`|PT1M |No|
|**Pod Init Container Terminated Reason**<br><br>The number of pod init containers with terminated reason. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusTerminatedReason` |Count |Average |`Namespace`, `Container`, `Pod`, `Reason`|PT1M |No|
|**Pod Init Container Waiting**<br><br>The number of pod init containers waiting. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusWaiting` |Count |Average |`Namespace`, `Container`, `Pod`|PT1M |No|
|**Pod Init Container Waiting Reason**<br><br>The reason the pod init container is waiting. In the absence of data, this metric will default to 0. |`KubePodInitContainerStatusWaitingReason` |Count |Average |`Namespace`, `Container`, `Pod`, `Reason`|PT1M |No|
|**Pod Status Phase**<br><br>The pod status phase. In the absence of data, this metric will default to 0. |`KubePodStatusPhases` |Count |Average |`Namespace`, `Pod`, `Phase`|PT1M |No|
|**Pod Ready State**<br><br>Signifies if the pod is in ready state. In the absence of data, this metric will default to 0. |`KubePodStatusReady` |Count |Average |`Namespace`, `Pod`, `Condition`|PT1M |No|
|**Pod Status Reason**<br><br>NodeAffinity |`KubePodStatusReason` |Count |Average |`Namespace`, `Pod`, `Reason`|PT1M |No|

### Category: Statefulset
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Statefulset Desired Replicas Number**<br><br>The desired number of statefulset replicas. In the absence of data, this metric will retain the most recent value emitted. |`KubeStatefulsetReplicas` |Count |Average |`Namespace`, `Statefulset`|PT1M |No|
|**Statefulset Replicas Difference**<br><br>The difference between desired and current number of replicas per statefulset. In the absence of data, this metric will default to 0. |`KubeStatefulsetStatusReplicaDifference` |Count |Average |`Namespace`, `Statefulset`|PT1M |No|
|**Statefulset Replicas Number**<br><br>The number of replicas per statefulset. In the absence of data, this metric will default to 0. |`KubeStatefulsetStatusReplicas` |Count |Average |`Namespace`, `Statefulset`|PT1M |No|

### Category: Telegraf
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Telegraf Internal Agent Gather Errors**<br><br>This metric tracks the number of errors that occur during the gather phase of the Telegraf agent's operation. These errors can happen for various reasons, such as issues with input plugins or problems accessing data sources. In the absence of data, this metric will retain the most recent value emitted. |`TelegrafInternalAgentGatherErrors` |Count |Average |`Host`|PT1M |No|
|**Telegraf Internal Agent Gather Timeouts**<br><br>The number of Telegraf internal agent gather timeouts. Timeouts can happen if the data sources are slow to respond or if there are network issues. In the absence of data, this metric will retain the most recent value emitted. |`TelegrafInternalAgentGatherTimeouts` |Count |Average |`Host`|PT1M |No|
|**Telegraf Internal Agent Metrics Dropped**<br><br>This metric tracks the number of metrics that have been dropped by the Telegraf agent during its operation. Metrics can be dropped for various reasons, such as buffer overflows, write errors, or other issues that prevent the metrics from being successfully processed and sent to the output destination. In the absence of data, this metric will retain the most recent value emitted. |`TelegrafInternalAgentMetricsDropped` |Count |Average |`Host`|PT1M |No|
|**Telegraf Internal Agent Metrics Gathered**<br><br>This metric tracks the number of metrics that have been successfully gathered by the Telegraf agent. In the absence of data, this metric will retain the most recent value emitted. |`TelegrafInternalAgentMetricsGathered` |Count |Average |`Host`|PT1M |No|
|**Telegraf Internal Agent Metrics Written**<br><br>This metric tracks the number of metrics that have been successfully written by the Telegraf agent to the output destination. In the absence of data, this metric will retain the most recent value emitted. |`TelegrafInternalAgentMetricsWritten` |Count |Average |`Host`|PT1M |No|
|**Telegraf Write Buffer Percent Used**<br><br>Percentage of metric write buffer that is being used. In the absence of data, this metric will default to 0. |`TelegrafWriteBufferPercentUsed` |Percent |Average |`Host`, `Output`|PT1M |Yes|

### Category: VMOrchestrator
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Kubevirt Info**<br><br>Kubevirt version information. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtInfo` |Unspecified |Average |`Kube Version`|PT1M |No|
|**Kubevirt Virt Controller Leading (Deprecated)**<br><br>Indication of whether the virt-controller is leading. The value is 1 if the virt-controller is leading, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtControllerLeading` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt Virt Controller Leading**<br><br>Indication of whether the virt-controller is leading. The value is 1 if the virt-controller is leading, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtControllerLeadingStatus` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt Virt Controller Ready (Deprecated)**<br><br>Indication for a virt-controller that is ready to take the lead. The value is 1 if the virt-controller is ready, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtControllerReady` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt Virt Controller Ready**<br><br>Indication for a virt-controller that is ready to take the lead. The value is 1 if the virt-controller is ready, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtControllerReadyStatus` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt Virt Operator Ready (Deprecated)**<br><br>Indication for a virt operator being ready. The value is 1 if the virt operator is ready, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtOperatorReady` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt Virt Operator Ready**<br><br>Indication for a virt operator being ready. The value is 1 if the virt operator is ready, 0 otherwise. In the absence of data, this metric will default to 0. |`KubevirtVirtOperatorReadyStatus` |Unspecified |Average |`Pod Name`|PT1M |No|
|**Kubevirt VMI Memory Balloon Bytes**<br><br>Current balloon size. In the absence of data, this metric will default to 0. |`KubevirtVmiMemoryActualBalloonBytes` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Memory Available Bytes**<br><br>Amount of usable memory as seen by the domain. This value may not be accurate if a balloon driver is in use or if the guest OS does not initialize all assigned pages. In the absence of data, this metric will default to 0. |`KubevirtVmiMemoryAvailableBytes` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Mem Dom Bytes**<br><br>The amount of memory allocated to the domain. The memory value in the domain XML file. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemoryDomainBytes` |Bytes |Average |`Node`|PT1M |No|
|**Kubevirt VMI Mem Dom Bytes (Deprecated)**<br><br>The amount of memory allocated to the domain. The memory value in the domain XML file. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemoryDomainBytesTotal` |Bytes |Average |`Node`|PT1M |No|
|**Kubevirt VMI Mem Swp In Traffic Bytes**<br><br>The total amount of data read from swap space of the guest. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemorySwapInTrafficBytes` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Mem Swp In Traffic Bytes (Deprecated)**<br><br>The total amount of data read from swap space of the guest. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemorySwapInTrafficBytesTotal` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Mem Swp Out Traffic Bytes**<br><br>The total amount of memory written out to swap space of the guest. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemorySwapOutTrafficBytes` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Mem Swp Out Traffic Bytes (Deprecated)**<br><br>The total amount of memory written out to swap space of the guest. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiMemorySwapOutTrafficBytesTotal` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Memory Unused Bytes**<br><br>The amount of memory left completely unused by the system. Memory that is available but used for reclaimable caches should NOT be reported as free. In the absence of data, this metric will default to 0. |`KubevirtVmiMemoryUnusedBytes` |Bytes |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Memory Usage**<br><br>The amount of memory used as a percentage. In the absence of data, this metric will default to 0. |`KubevirtVmiMemoryUsage` |Percent |Average |`Name`, `Node`|PT1M |No|
|**Kubevirt VMI Outdated Count**<br><br>Indication for the total number of VirtualMachineInstance (VMI) workloads that are not running within the most up-to-date version of the virt-launcher environment. In the absence of data, this metric will default to 0. |`KubevirtVmiNumberOfOutdatedInstances` |Count |Average |\<none\>|PT1M |No|
|**Kubevirt VMI Outdated Count (Deprecated)**<br><br>Indication for the total number of VirtualMachineInstance (VMI) workloads that are not running within the most up-to-date version of the virt-launcher environment. In the absence of data, this metric will default to 0. |`KubevirtVmiOutdatedInstances` |Count |Average |\<none\>|PT1M |No|
|**Kubevirt VMI Phase Count**<br><br>Sum of Virtual Machine Instances (VMIs) per phase and node. Phase can be one of the following: Pending, Scheduling, Scheduled, Running, Succeeded, Failed, Unknown. In the absence of data, this metric will default to 0. |`KubevirtVmiPhaseCount` |Count |Average |`Node`, `Phase`, `Workload`|PT1M |No|
|**Kubevirt VMI Storage IOPS Read Total**<br><br>Total number of Input/Output (I/O) read operations. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageIopsReadTotal` |Count |Average |`Drive`, `Name`, `Node`|PT1M |No|
|**Kubevirt VMI Storage IOPS Write Total**<br><br>Total number of Input/Output (I/O) write operations. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageIopsWriteTotal` |Count |Average |`Drive`, `Name`, `Node`|PT1M |No|
|**Kubevirt VMI Storage Read Times Total (Deprecated)**<br><br>Total time spent on read operations from storage. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageReadTimesMsTotal` |Milliseconds |Average |`Drive`, `Name`, `Node`|PT1M |No|
|**Kubevirt VMI Storage Read Times Total**<br><br>Total time spent on read operations from storage. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageReadTimesSecondsTotal` |Seconds |Average |`Drive`, `Name`, `Node`|PT1M |No|
|**Kubevirt VMI Storage Write Times Total (Deprecated)**<br><br>Total time spent on write operations to storage. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageWriteTimesMsTotal` |Milliseconds |Average |`Drive`, `Name`, `Node`|PT1M |No|
|**Kubevirt VMI Storage Write Times Total**<br><br>Total time spent on write operations to storage. In the absence of data, this metric will retain the most recent value emitted. |`KubevirtVmiStorageWriteTimesSecondsTotal` |Seconds |Average |`Drive`, `Name`, `Node`|PT1M |No|