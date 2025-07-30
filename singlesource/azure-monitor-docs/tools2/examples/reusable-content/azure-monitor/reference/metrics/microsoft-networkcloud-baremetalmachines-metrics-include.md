---
ms.topic: include
ms.date: 04/16/2025
ms.custom: Microsoft.NetworkCloud/bareMetalMachines, naam

# NOTE:  This content is automatically generated using API calls to Azure. Any edits made on these files will be overwritten in the next run of the script. 
 
---




### Category: CPU
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**CPU Guest Usage**<br><br>Percentage of time that the CPU is running a virtual CPU for a guest operating system. In the absence of data, this metric will default to 0. |`CpuUsageGuest` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Guest Nice Usage**<br><br>Percentage of time that the CPU is running low-priority processes on a virtual CPU for a guest operating system. In the absence of data, this metric will default to 0. |`CpuUsageGuestNice` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage Idle**<br><br>Percentage of time that the CPU is idle. In the absence of data, this metric will default to 0. |`CpuUsageIdle` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage IO Wait**<br><br>Percentage of time that the CPU is waiting for I/O operations to complete. In the absence of data, this metric will default to 0. |`CpuUsageIowait` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage IRQ**<br><br>Percentage of time that the CPU is servicing hardware interrupt requests. In the absence of data, this metric will default to 0. |`CpuUsageIrq` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage Nice**<br><br>Percentage of time that the CPU is in user mode, running low-priority processes. In the absence of data, this metric will default to 0. |`CpuUsageNice` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage Soft IRQ**<br><br>Percentage of time that the CPU is servicing software interrupt requests. In the absence of data, this metric will default to 0. |`CpuUsageSoftirq` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage Steal**<br><br>Percentage of time that the CPU is in stolen time, which is time spent in other operating systems in a virtualized environment. In the absence of data, this metric will default to 0. |`CpuUsageSteal` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage System**<br><br>Percentage of time that the CPU is in system mode. In the absence of data, this metric will default to 0. |`CpuUsageSystem` |Count |Average |`Host`, `CPU`|PT1M |No|
|**CPU Usage Total**<br><br>Percentage of time that the CPU is active (not idle). In the absence of data, this metric will default to 150. |`CpuUsageTotal` |Percent |Average |`Host`, `CPU`|PT1M |Yes|
|**CPU Usage User**<br><br>Percentage of time that the CPU is in user mode. In the absence of data, this metric will default to 0. |`CpuUsageUser` |Count |Average |`Host`, `CPU`|PT1M |No|
|**Host Specific CPU Utilization (Preview)**<br><br>A counter metric quantifying the CPU time that each CPU has spent in different states (or 'modes'). In the absence of data, this metric will retain the most recent value emitted. |`HostSpecificCPUUtilization` |Seconds |Average |`Cpu`, `Host`, `Mode`|PT1M |No|
|**Total CPUs Available to Nexus per NUMA**<br><br>Total number of CPUs available to Nexus per NUMA. This metric is only emitted on compute nodes. In the absence of data, this metric will retain the most recent value emitted. |`NcTotalCpusPerNuma` |Count |Average |`Hostname`, `NUMA Node`|PT1M |No|
|**CPUs per NUMA Allocated for Nexus K8s**<br><br>Total number of CPUs per NUMA allocated for Nexus Kubernetes and Tenant Workloads. This metric is only emitted on compute nodes. In the absence of data, this metric will retain the most recent value emitted. |`NcTotalWorkloadCpusAllocatedPerNuma` |Count |Average |`Hostname`, `NUMA Node`|PT1M |No|
|**CPUs per NUMA Available for Nexus K8s**<br><br>Total number of CPUs per NUMA available for use by Nexus Kubernetes and Tenant Workloads. This metric is only emitted on compute nodes. In the absence of data, this metric will retain the most recent value emitted. |`NcTotalWorkloadCpusAvailablePerNuma` |Count |Average |`Hostname`, `NUMA Node`|PT1M |No|

### Category: Disk
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Host Disk Reads Completed**<br><br>Total number of disk reads completed successfully. In the absence of data, this metric will retain the most recent value emitted. |`HostDiskReadCompleted` |Count |Average |`Device`, `Host`|PT1M |No|
|**Host Disk Read Seconds (Preview)**<br><br>Total time spent reading from disk. In the absence of data, this metric will retain the most recent value emitted. |`HostDiskReadSeconds` |Seconds |Average |`Device`, `Host`|PT1M |No|
|**Total Number of Writes Completed**<br><br>Total number of disk writes completed successfully. In the absence of data, this metric will retain the most recent value emitted. |`HostDiskWriteCompleted` |Count |Average |`Device`, `Host`|PT1M |No|
|**Host Disk Write Seconds (Preview)**<br><br>Total time spent writing to disk. In the absence of data, this metric will retain the most recent value emitted. |`HostDiskWriteSeconds` |Seconds |Average |`Device`, `Host`|PT1M |No|
|**Node NVMe Info (Preview)**<br><br>Non-Volatile Memory express (NVMe) information, value is always 1. Provides state for a device. In the absence of data, this metric will default to 0. |`NodeNvmeInfo` |Count |Count |`Device`, `State`|PT1M |No|

### Category: Filesystem
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Host Entropy Available Bits (Preview)**<br><br>Available node entropy, in bits. In the absence of data, this metric will retain the most recent value emitted. |`HostEntropyAvailableBits` |Count |Average |`Host`|PT1M |No|
|**Host Filesystem Available Bytes**<br><br>Bytes in the filesystem on nodes which are available to non-root users. In the absence of data, this metric will default to 0. |`HostFilesystemAvailBytes` |Count |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Device Errors**<br><br>Indicates if there was an error getting information from the filesystem. Value is 1 if there was an error, 0 otherwise. In the absence of data, this metric will default to 0. |`HostFilesystemDeviceError` |Count |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Files**<br><br>Total number of permitted inodes (file nodes). In the absence of data, this metric will default to 0. |`HostFilesystemFiles` |Count |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Total Number of Free inodes**<br><br>Total number of free (not occupied or reserved) inodes (file nodes). In the absence of data, this metric will default to 0. |`HostFilesystemFilesFree` |Count |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Files Percent Free**<br><br>Percentage of permitted inodes which are free to be used. In the absence of data, this metric will default to 150. |`HostFilesystemFilesPercentFree` |Percent |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Read Only**<br><br>Indication of whether a filesystem is readonly or not. Value is 1 if readonly, 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`HostFilesystemReadOnly` |Unspecified |Count |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Size In Bytes**<br><br>Host filesystem size in bytes. In the absence of data, this metric will retain the most recent value emitted. |`HostFilesystemSizeBytes` |Count |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|
|**Host Filesystem Usage In Percentage**<br><br>Percentage of filesystem which is in use. In the absence of data, this metric will default to 150. |`HostFilesystemUsage` |Percent |Average |`Device`, `FSType`, `Host`, `Mountpoint`|PT1M |No|

### Category: HardwareMonitor
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Host Hardware Monitor Temp**<br><br>Temperature (in Celsius) of different hardware components. In the absence of data, this metric will retain the most recent value emitted. |`HostHwmonTempCelsius` |Count |Average |`Chip`, `Host`, `Sensor`|PT1M |No|
|**Host Hardware Monitor Temp Max**<br><br>Maximum temperature (in Celsius) of different hardware components. In the absence of data, this metric will retain the most recent value emitted. |`HostHwmonTempMax` |Count |Average |`Chip`, `Host`, `Sensor`|PT1M |No|
|**Host Hardware Inlet Temp**<br><br>Inlet temperature for hardware nodes (in Celsius). In the absence of data, this metric will retain the most recent value emitted. |`HostInletTemp` |Count |Average |`Host`|PT1M |No|
|**IDRAC Power Capacity Watts**<br><br>IDRAC Power Capacity in Watts. In the absence of data, this metric will retain the most recent value emitted. |`IdracPowerCapacityWatts` |Unspecified |Average |`Host`, `PSU`|PT1M |No|
|**IDRAC Power Input Watts**<br><br>IDRAC Power Input in Watts. In the absence of data, this metric will retain the most recent value emitted. |`IdracPowerInputWatts` |Unspecified |Average |`Host`, `PSU`|PT1M |No|
|**IDRAC Power On**<br><br>IDRAC Power On Status. Value is 1 if on, 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`IdracPowerOn` |Unspecified |Count |`Host`|PT1M |No|
|**IDRAC Power Output Watts**<br><br>IDRAC Power Output in Watts. In the absence of data, this metric will retain the most recent value emitted. |`IdracPowerOutputWatts` |Unspecified |Average |`Host`, `PSU`|PT1M |No|
|**IDRAC Sensors Temperature**<br><br>IDRAC sensor temperature (in Celsius). In the absence of data, this metric will retain the most recent value emitted. |`IdracSensorsTemperature` |Unspecified |Average |`Host`, `Name`, `Units`|PT1M |No|

### Category: Mellanox
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Effective Physical BER**<br><br>This point in time metric represents the number of errors that occurred in the physical layer of the network since the last collection. This metric is used for assessing the quality and reliability of the network link. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxEffectivePhysicalBer` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**Effective Physical Errors**<br><br>This point in time metric represents the number of physical layer errors that have been detected and could not be corrected by error correction mechanisms since the last collection. These errors are critical for assessing the quality and reliability of the network link. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxEffectivePhysicalErrors` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**MST Register Temperature**<br><br>Temperature (in Celsius) reported by the MST (Mellanox Software Tools) register. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxMstregTemperature` |Unspecified |Average |`Host`, `Interface Name`|PT1M |No|
|**Received Bytes**<br><br>This point in time metric represents the number of bytes that have been successfully received by the network interface at the physical layer since the last collection. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxBytesPhy` |Bytes |Average |`Host`, `Interface Name`|PT1M |No|
|**Corrected Bits**<br><br>This point in time metric represents the number of bits corrected by the network device since the last collection. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxCorrectedBitsPhy` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**Corrected Bit Rate**<br><br>Rate of corrected bits by the network device, the rate is determined by the number of corrected bits divided by the number of RX bytes recieved in the given time frame. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxCorrectedRate` |Percent |Average |`Host`, `Interface Name`|PT1M |No|
|**CRC Errors**<br><br>This point in time metric represents the number of CRC errors encountered by the network device since the last collection. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxCrcErrorsPhy` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**Network Error Rate**<br><br>Rate of errors encountered by the network device as determined by the number of MellanoxRxPcsSymbolErrPhy errors divided by the number of RX bytes in a specific time frame and indicates the errors that FEC could not correct. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxErrorRate` |Percent |Average |`Host`, `Interface Name`|PT1M |No|
|**PCS Symbol Errors**<br><br>This point in time metric represents the number of PCS symbol errors encountered by the network device since the last collection. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxPcsSymbolErrPhy` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**Symbol Errors**<br><br>This point in time metric represents the number of symbol errors encountered by the network device since the last collection. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxRxSymbolErrPhy` |Count |Average |`Host`, `Interface Name`|PT1M |No|
|**Status Opcode**<br><br>The status code indicates the status or condition of a Mellanox network device. For example a status opcode of 0 indicates that the device is functioning normally with no errors detected. See Mellanox documentation for the definition of error codes. In the absence of data, this metric will retain the most recent value emitted. |`MellanoxStatusOpcode` |Count |Average |`Host`, `Interface Name`|PT1M |No|

### Category: Memory
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Average Load In 1 Minute (Preview)**<br><br>1-minute load average of the system, as a measure of the system activity over the last minute, expressed as a fractional number (i.e. values >1.0 may indicate overload). In the absence of data, this metric will retain the most recent value emitted. |`HostLoad1` |Count |Average |`Host`|PT1M |No|
|**Average Load In 15 Minutes (Preview)**<br><br>15-minute load average of the system, as a measure of the system activity over the last 15 minutes, expressed as a fractional number (i.e. values >1.0 may indicate overload). In the absence of data, this metric will retain the most recent value emitted. |`HostLoad15` |Count |Average |`Host`|PT1M |No|
|**Average load in 5 minutes (Preview)**<br><br>5-minute load average of the system, as a measure of the system activity over the last 5 minutes, expressed as a fractional number (i.e. values >1.0 may indicate overload). In the absence of data, this metric will retain the most recent value emitted. |`HostLoad5` |Count |Average |`Host`|PT1M |No|
|**Host Memory Available Bytes**<br><br>Memory available, in bytes. In the absence of data, this metric will retain the most recent value emitted. |`HostMemAvailBytes` |Count |Average |`Host`|PT1M |No|
|**Memory Free Huge Pages**<br><br>Total memory in huge pages that is free. In the absence of data, this metric will retain the most recent value emitted. |`HostMemHugePagesFree` |Bytes |Average |`Host`|PT1M |No|
|**Memory Total Huge Pages**<br><br>Total memory in huge pages on nodes. In the absence of data, this metric will retain the most recent value emitted. |`HostMemHugePagesTotal` |Bytes |Average |`Host`|PT1M |No|
|**Total Memory In Corrupted Pages**<br><br>Memory corrupted due to hardware issues, in bytes. In the absence of data, this metric will retain the most recent value emitted. |`HostMemHWCorruptedBytes` |Count |Average |`Host`|PT1M |No|
|**Host Memory Swap Available Percentage**<br><br>Percentage of swap memory that is available. In the absence of data, this metric will default to 0. |`HostMemSwapAvailableSpace` |Percent |Average |`Host`|PT1M |No|
|**Host Memory Swap Free Bytes**<br><br>Total swap memory that is free. In the absence of data, this metric will retain the most recent value emitted. |`HostMemSwapFreeBytes` |Bytes |Average |`Host`|PT1M |No|
|**Host Memory Swap Total Bytes**<br><br>Total amount of swap memory. In the absence of data, this metric will retain the most recent value emitted. |`HostMemSwapTotalBytes` |Bytes |Average |`Host`|PT1M |No|
|**Host Memory Total Bytes**<br><br>Total amount of physical memory on nodes. In the absence of data, this metric will retain the most recent value emitted. |`HostMemTotalBytes` |Bytes |Average |`Host`|PT1M |No|
|**Node Memory Huge Pages Free (Preview)**<br><br>Free memory in NUMA huge pages. In the absence of data, this metric will retain the most recent value emitted. |`NodeMemHugePagesFree` |Bytes |Average |`Host`, `Node`|PT1M |No|
|**Node Memory Huge Pages Total**<br><br>Total memory in NUMA huge pages. In the absence of data, this metric will retain the most recent value emitted. |`NodeMemHugePagesTotal` |Bytes |Average |`Host`, `Node`|PT1M |No|
|**Node Memory NUMA (Free Memory)**<br><br>Total amount of free NUMA memory. In the absence of data, this metric will retain the most recent value emitted. |`NodeMemNumaFree` |Bytes |Average |`Host`, `Node`|PT1M |No|
|**Node Memory NUMA (Shared Memory)**<br><br>Total amount of NUMA memory that is shared between nodes. In the absence of data, this metric will retain the most recent value emitted. |`NodeMemNumaShem` |Bytes |Average |`Host`, `Node`|PT1M |No|
|**Node Memory NUMA (Used Memory)**<br><br>Total amount of used NUMA memory. In the absence of data, this metric will retain the most recent value emitted. |`NodeMemNumaUsed` |Bytes |Average |`Host`, `Node`|PT1M |No|

### Category: Network
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Network Device Receive Errors**<br><br>Total number of errors encountered by network devices while receiving data. In the absence of data, this metric will retain the most recent value emitted. |`NcNodeNetworkReceiveErrsTotal` |Count |Average |`Hostname`, `Interface Name`|PT1M |No|
|**Network Device Transmit Errors**<br><br>Total number of errors encountered by network devices while transmitting data. In the absence of data, this metric will retain the most recent value emitted. |`NcNodeNetworkTransmitErrsTotal` |Count |Average |`Hostname`, `Interface Name`|PT1M |No|
|**Node Bonding Active (Preview)**<br><br>Total number of active network interfaces per bonding interface. In the absence of data, this metric will retain the most recent value emitted. |`NodeBondingActive` |Count |Average |`Master`|PT1M |No|
|**Node Bond Aggregate ID Mismatch**<br><br>Total number of mismatches between the expected and actual link-aggregator ids. In the absence of data, this metric will retain the most recent value emitted. |`NodeBondingAggregateIdMismatch` |Count |Average |`Host`, `Interface`|PT1M |No|
|**Node Network Carrier Changes**<br><br>Total number of network carrier changes. In the absence of data, this metric will retain the most recent value emitted. |`NodeNetworkCarrierChanges` |Count |Average |`Device`, `Host`|PT1M |No|
|**Node Network Max Transmission**<br><br>Maximum Transmission Unit (MTU) for node network interfaces. In the absence of data, this metric will default to 0. |`NodeNetworkMtuBytes` |Bytes |Average |`Device`, `Host`|PT1M |No|
|**Node Network Received Multicast Total**<br><br>Total amount of multicast traffic received by the node network interfaces. In the absence of data, this metric will retain the most recent value emitted. |`NodeNetworkReceiveMulticastTotal` |Bytes |Average |`Device`, `Host`|PT1M |No|
|**Node Network Received Packets**<br><br>Total number of packets received by the node network interfaces. In the absence of data, this metric will retain the most recent value emitted. |`NodeNetworkReceivePackets` |Count |Average |`Device`, `Host`|PT1M |No|
|**Node Network Speed Bytes**<br><br>Current network speed, in bytes per second, for the node network interfaces. In the absence of data, this metric will default to 0. |`NodeNetworkSpeedBytes` |Bytes |Average |`Device`, `Host`|PT1M |No|
|**Node Network Up**<br><br>Indicates the operational status of the nodes network interfaces. Value is 1 if operstate is 'up', 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`NodeNetworkStatus` |Count |Count |`Device`, `Host`|PT1M |No|
|**Node Network Transmited Packets**<br><br>Total number of packets transmitted by the node network interfaces. In the absence of data, this metric will retain the most recent value emitted. |`NodeNetworkTransmitPackets` |Count |Average |`Device`, `Host`|PT1M |No|

### Category: System
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Host Boot Seconds (Preview)**<br><br>Unix timestamp of the last boot of the host. In the absence of data, this metric will retain the most recent value emitted. |`HostBootTimeSeconds` |Seconds |Average |`Host`|PT1M |No|
|**Host DMI Info**<br><br>Environment information about the Desktop Management Interface (DMI), value is always 1. Includes labels about the system's manufacturer, model, version, serial number and UUID. In the absence of data, this metric will default to 0. |`HostDmiInformation` |Unspecified |Count |`BiosDate`, `BiosRelease`, `BiosVendor`, `BiosVersion`, `BoardName`, `BoardVendor`, `BoardVersion`, `Host`, `ProductFamily`, `ProductName`, `ProductSku`, `SystemVendor`|PT1M |No|
|**Node NTP Leap**<br><br>The raw leap flag value of the local NTP daemon. This indicates the status of leap seconds. Value is 0 if no adjustment is needed, 1 to add a leap second, 2 to delete a leap second, and 3 if the clock is unsynchronized. In the absence of data, this metric will retain the most recent value emitted. |`NodeNtpLeap` |Count |Average |`Host`|PT1M |No|
|**Node NTP Root Delay Seconds**<br><br>Indicates the delay to synchronize with the root server. In the absence of data, this metric will retain the most recent value emitted. |`NodeNtpRootDelaySeconds` |Seconds |Average |`Host`|PT1M |No|
|**Node NTP RTT (Deprecated)**<br><br>Round-trip time from node exporter collector to local NTP daemon. In the absence of data, this metric will retain the most recent value emitted. |`NodeNtpRtt` |Seconds |Average |`Host`|PT1M |No|
|**Node NTP Sanity**<br><br>The aggregate health of the local NTP daemon. This includes checks for stratum, leap flag, freshness, root distance, and causality violations. Value is 1 if all checks pass, 0 otherwise. In the absence of data, this metric will retain the most recent value emitted. |`NodeNtpSanity` |Count |Average |`Host`|PT1M |No|
|**Node NTP Stratum**<br><br>The stratum level of the local NTP daemon. This indicates the distance from the reference clock, with lower numbers representing closer proximity and higher accuracy. Values range from 1 (directly connected to reference clock) to 15 (further away), with 16 indicating the clock is unsynchronized. In the absence of data, this metric will retain the most recent value emitted. |`NodeNtpStratum` |Count |Average |`Host`|PT1M |No|
|**Node OS Info**<br><br>Node OS information, value is always 1. Provides name and version for a device. In the absence of data, this metric will retain the most recent value emitted. |`NodeOsInfo` |Count |Count |`Host`, `Name`, `Version`|PT1M |No|
|**Node Processes State**<br><br>The number of processes in each state. The possible states are D (UNINTERRUPTABLE_SLEEP), R (RUNNING & RUNNABLE), S (INTERRUPTABLE_SLEEP), T (STOPPED) and Z (ZOMBIE). In the absence of data, this metric will retain the most recent value emitted. |`NodeProcessState` |Count |Average |`Host`, `State`|PT1M |No|
|**Node Timex Max Error Seconds**<br><br>Maximum time error between the local system and reference clock. In the absence of data, this metric will retain the most recent value emitted. |`NodeTimexMaxErrorSeconds` |Seconds |Average |`Host`|PT1M |No|
|**Node Timex Offset Seconds**<br><br>Time offset between the local system and reference clock. In the absence of data, this metric will retain the most recent value emitted. |`NodeTimexOffsetSeconds` |Seconds |Average |`Host`|PT1M |No|
|**Node Timex Sync Status**<br><br>Indicates whether the clock is synchronized to a reliable server. Value is 1 if synchronized, 0 if unsynchronized. In the absence of data, this metric will retain the most recent value emitted. |`NodeTimexSyncStatus` |Count |Average |`Host`|PT1M |No|

### Category: VM Stat
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Node VM Out Of Memory Kill**<br><br>Total number of times a process has been terminated due to a critical lack of memory. In the absence of data, this metric will retain the most recent value emitted. |`NodeVmOomKill` |Count |Average |`Host`|PT1M |No|
|**Node VM PSWP In**<br><br>Total number of pages swapped in from disk to memory on the node. In the absence of data, this metric will retain the most recent value emitted. |`NodeVmstatPswpIn` |Count |Average |`Host`|PT1M |No|
|**Node VM PSWP Out**<br><br>Total number of pages swapped out from memory to disk on the node. In the absence of data, this metric will retain the most recent value emitted. |`NodeVmstatPswpout` |Count |Average |`Host`|PT1M |No|