---
ms.topic: include
ms.date: 04/16/2025
ms.custom: Microsoft.NetworkCloud/storageAppliances, naam

# NOTE:  This content is automatically generated using API calls to Azure. Any edits made on these files will be overwritten in the next run of the script. 
 
---




### Category: Host
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Nexus Storage Host Bandwidth Bytes**<br><br>Host bandwidth of the pure storage array in bytes per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHostPerformanceBandwidthBytes` |Bytes |Average |`Dimension`, `Host`|PT1M |No|
|**Nexus Storage Host Latency**<br><br>Latency of the pure storage array hosts. In the absence of data, this metric will default to 0. |`PurefaHostPerformanceLatencyMs` |MilliSeconds |Average |`Dimension`, `Host`|PT1M |No|
|**Nexus Storage Host Performance Throughput Iops**<br><br>The host throughput in I/O operations per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHostPerformanceThroughputIops` |Count |Average |`Host`, `Dimension`|PT1M |No|
|**Nexus Storage Host Space Bytes**<br><br>Storage array host space. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHostSpaceBytesV2` |Bytes |Average |`Host`, `Space`|PT1M |No|
|**Nexus Storage Host Space Data Reduction Ratio**<br><br>Host space data reduction ratio. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHostSpaceDataReductionRatioV2` |Count |Average |`Host`|PT1M |No|

### Category: Storage Array
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Nexus Storage Alerts Open**<br><br>Number of open alert events. In the absence of data, this metric will default to 0. |`PurefaAlertsOpen2` |Count |Average |`Code`, `Component Type`, `Issue`, `Severity`, `Summary`|PT1M |No|
|**Nexus Storage Array Performance Average Bytes**<br><br>The average operations size by dimension, where dimension can be mirrored_write_bytes_per_sec, read_bytes_per_sec or write_bytes_per_sec. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArrayPerformanceAverageBytes` |Bytes |Average |`Dimension`|PT1M |No|
|**Nexus Storage Array Bandwidth Bytes**<br><br>Performance of the pure storage array bandwidth in bytes per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArrayPerformanceBandwidthBytes` |Bytes |Average |`Dimension`|PT1M |No|
|**Nexus Storage Array Latency**<br><br>Latency of the pure storage array. In the absence of data, this metric will default to 0. |`PurefaArrayPerformanceLatencyMs` |MilliSeconds |Average |`Dimension`|PT1M |No|
|**Nexus Storage Array Performance Queue Depth Operations**<br><br>The array queue depth size by number of operations. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArrayPerformanceQueueDepthOps` |Count |Average |\<none\>|PT1M |No|
|**Nexus Storage Array Performance Throughput Iops**<br><br>The array throughput in operations per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArrayPerformanceThroughputIops` |Count |Average |`Dimension`|PT1M |No|
|**Nexus Storage Array Space Bytes**<br><br>The amount of array space. The space filter can be used to filter the space by type. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArraySpaceBytes` |Bytes |Average |`Space`|PT1M |No|
|**Nexus Storage Array Space Data Reduction Ratio**<br><br>Storage array overall data reduction ratio. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArraySpaceDataReductionRatioV2` |Count |Average |\<none\>|PT1M |No|
|**Nexus Storage Array Space Utilization**<br><br>Array space utilization in percent. In the absence of data, this metric will retain the most recent value emitted. |`PurefaArraySpaceUtilization` |Percent |Average |\<none\>|PT1M |No|
|**Nexus Storage Hardware Component Status**<br><br>Status of a hardware component. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHwComponentStatus` |Count |Average |`Component Name`, `Component Type`, `Component Status`|PT1M |No|
|**Nexus Storage Hardware Component Temperature Celsius**<br><br>Temperature of the temperature sensor component in Celsius. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHwComponentTemperatureCelsius` |Unspecified |Average |`Component Name`|PT1M |No|
|**Nexus Storage Hardware Component Voltage**<br><br>Voltage used by the power supply component in volts. In the absence of data, this metric will retain the most recent value emitted. |`PurefaHwComponentVoltageVolt` |Unspecified |Average |`Component Name`|PT1M |No|
|**Nexus Storage Info (Preview)**<br><br>Storage array system information. In the absence of data, this metric will default to 0. |`PurefaInfo` |Unspecified |Average |`Array Name`|PT1M |No|
|**Nexus Storage Network Interface Performance Errors**<br><br>The number of network interface errors per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaNetworkInterfacePerformanceErrors` |Count |Average |`Dimension`, `Name`, `Type`|PT1M |No|

### Category: Volume
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Nexus Storage Volume Performance Bandwidth Bytes**<br><br>Volume throughput in bytes per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaVolumePerformanceBandwidthBytesV2` |Bytes |Average |`Name`, `Dimension`|PT1M |No|
|**Nexus Storage Volume Latency**<br><br>Latency of the pure storage array volumes. In the absence of data, this metric will default to 0. |`PurefaVolumePerformanceLatencyMsV2` |MilliSeconds |Average |`Dimension`, `Name`|PT1M |No|
|**Nexus Storage Volume Performance Throughput Iops**<br><br>Volume throughput in operations per second. In the absence of data, this metric will retain the most recent value emitted. |`PurefaVolumePerformanceThroughputIops` |Count |Average |`Name`, `Dimension`|PT1M |No|
|**Nexus Storage Volume Space Bytes**<br><br>Pure storage array volume space. In the absence of data, this metric will retain the most recent value emitted. |`PurefaVolumeSpaceBytesV2` |Bytes |Average |`Name`, `Space`|PT1M |No|
|**Nexus Storage Volume Space Data Reduction Ratio**<br><br>Volume space data reduction ratio. In the absence of data, this metric will retain the most recent value emitted. |`PurefaVolumeSpaceDataReductionRatioV2` |Unspecified |Average |`Name`|PT1M |No|