---
title: What's new in Windows Server 
description: This article describes what's new for Windows Server
author: IngridAtMicrosoft
ms.topic: article
ms.author: inhenkel
ms.date: 08/26/2021
ms.service: media-services
---

# What's new in Windows Server

:::moniker range="windows-server-2008"
[!INCLUDE [hr-logo-2008](../includes/hr-logo-2008.md)]
:::moniker-end
:::moniker range="windows-server-2012"
[!INCLUDE [hr-logo-2012](../includes/hr-logo-2012.md)]
:::moniker-end
:::moniker range="windows-server-2016"
[!INCLUDE [hr-logo-2016](../includes/hr-logo-2016.md)]
:::moniker-end
:::moniker range="windows-server-2019"
[!INCLUDE [hr-logo-2019](../includes/hr-logo-2019.md)]
:::moniker-end
:::moniker range="windows-server-2022"
[!INCLUDE [hr-logo-2019](../includes/hr-logo-2022.md)]
:::moniker-end

:::moniker range="windows-server-2022"

## Windows Server 2022

This article describes some of the new features in Windows Server 2022. Windows Server 2022 is built on the strong foundation of Windows Server 2019 and brings many innovations on three key themes: security, Azure hybrid integration and management, and application platform. Also, Windows Server 2022 Datacenter: Azure Edition helps you use the benefits of cloud to keep your VMs up to date while minimizing downtime.

## Security

The new security capabilities in Windows Server 2022 combine other security capabilities in Windows Server across multiple areas to provide defense-in-depth protection against advanced threats. Advanced multi-layer security in Windows Server 2022 provides the comprehensive protection that servers need today.

### Secured-core server

Secured-core server provides protections that are useful against sophisticated attacks and can provide increased assurance when handling mission critical data in some of the most data sensitive industries.  It is built on three key pillars: simplified security, advanced protection, and preventative defense.

#### Simplified security

When you buy hardware from an OEM for Secured-core server, you have assurance that the OEM has provided a set of hardware, firmware, and drivers that satisfy the Secured-core promise. Windows Server systems will have easy configuration experiences in the Windows Admin Center to enable the security features of Secured-core.

#### Advanced protection

Secured-core servers use hardware, firmware, and operating system capabilities to the fullest extent to provide protection against current and future threats. The protections enabled by a Secured-core server are targeted to create a secure platform for critical applications and data used on that server. The Secured-core functionality spans the following areas:

* **Hardware root-of-trust**

  Trusted Platform Module 2.0 TPM 2.0 come standard with servers capable of using Secured-core servers. TPM 2.0 provides a secure store for sensitive keys and data, such as measurements of the components loaded during boot. This hardware root-of-trust raises the protection provided by capabilities like BitLocker, which uses TPM 2.0 and facilitates creating attestation-based workflows that can be incorporated into zero-trust security strategies.

* **Firmware protection**

  There is a clear rise in security vulnerabilities being reported in the firmware space given the high privileges that firmware runs with and the relative opacity of what happens in firmware to traditional anti-virus solutions. Recent reports show that malware and ransomware platforms are adding firmware capabilities raising the risk of firmware attacks that have already been seen targeting enterprise resources like Active Directory domain controllers. Using processor support for Dynamic Root of Trust of Measurement DRTM technology, along with DMA protection, Secured-core systems isolate the security critical hypervisor from attacks such as this.

* **Virtualization-based security VBS**

  Secured-core servers support VBS and hypervisor-based code integrity HVCI. VBS and HVCI protect against the entire class of vulnerabilities used in cryptocurrency mining attacks given the isolation VBS provides between the privileged parts of the operating system such as the kernel and the rest of the system. VBS also provides more capabilities that customers can enable, such as Credential Guard, which better protects domain credentials.

#### Preventative defense

Enabling Secured-core functionality helps proactively defend against and disrupt many of the paths attackers may use to exploit a system. This set of defenses also enables IT and SecOps teams better utilize their time across the many areas that need their attention.

### Secure connectivity

#### Transport: HTTPS and TLS 1.3 enabled by default on Windows Server 2022

Secure connections are at the heart of today’s interconnected systems. Transport Layer Security TLS 1.3 is the latest version of the internet’s most deployed security protocol, which encrypts data to provide a secure communication channel between two endpoints. HTTPS and TLS 1.3 is now enabled by default on Windows Server 2022, protecting the data of clients connecting to the server. It eliminates obsolete cryptographic algorithms, enhances security over older versions, and aims to encrypt as much of the handshake as possible. Learn more about supported TLS versions/windows/win32/secauthn/protocols-in-tls-ssl--schannel-ssp- and about supported cipher suites/windows/win32/secauthn/tls-cipher-suites-in-windows-server-2022.

#### Secure DNS: Encrypted DNS name resolution requests with DNS-over-HTTPS

DNS Client in Windows Server 2022 now supports DNS-over-HTTPS DoH which encrypts DNS queries using the HTTPS protocol. This helps keep your traffic as private as possible by preventing eavesdropping and your DNS data being manipulated. Learn more about configuring the DNS client to use DoH../networking/dns/doh-client-support.md.

#### Server Message Block SMB: SMB AES-256 encryption for the most security conscious

Windows Server now supports AES-256-GCM and AES-256-CCM cryptographic suites for SMB encryption and signing. Windows will automatically negotiate this more advanced cipher method when connecting to another computer that also supports it, and it can also be mandated through Group Policy. Windows Server still supports AES-128 for down-level compatibility.

#### SMB: East-West SMB encryption controls for internal cluster communications

Windows Server failover clusters now support granular control of encrypting and signing intra-node storage communications for Cluster Shared Volumes CSV and the storage bus layer SBL. This means that when using Storage Spaces Direct, you can decide to encrypt or sign east-west communications within the cluster itself for higher security.

#### SMB over QUIC

SMB over QUIC updates the SMB 3.1.1 protocol in Windows Server 2022 Datacenter: Azure Edition and supported Windows clients to use the QUIC protocol instead of TCP. By using SMB over QUIC along with TLS 1.3, users and applications can securely and reliably access data from edge file servers running in Azure. Mobile and telecommuter users no longer need a VPN to access their file servers over SMB when on Windows. More information can be found at the SMB over QUIC documentation../storage/file-server/smb-over-quic.md.

## Azure hybrid capabilities

You can increase your efficiency and agility with built-in hybrid capabilities in Windows Server 2022 that allow you to extend your data centers to Azure more easily than ever before.

### Azure Arc enabled Windows Servers

Azure Arc enabled servers with Windows Server 2022 brings on-premises and multi-cloud Windows Servers to Azure with Azure Arc. This management experience is designed to be consistent with how you manage native Azure virtual machines. When a hybrid machine is connected to Azure, it becomes a connected machine and is treated as a resource in Azure. More information can be found at the Azure Arc enables servers documentation/azure/azure-arc/servers/overview.

### Windows Admin Center

Improvements to Windows Admin Center to manage Windows Server 2022 include capabilities to both report on the current state of the Secured-core features mentioned above, and where applicable, allow customers to enable the features. More information on these and many more improvements to Windows Admin Center can be found at the Windows Admin Center documentation../manage/windows-admin-center/understand/what-is.md.

### Azure Automanage - Hotpatch

Hotpatch, part of Azure Automanage, is supported in Windows Server 2022 Datacenter: Azure Edition. Hotpatching is a new way to install updates on new Windows Server Azure Edition virtual machines VMs that doesn’t require a reboot after installation. More information can be found at the Azure Automanage documentation/azure/automanage/automanage-hotpatch.

## Application platform

There are several platform improvements for Windows Containers, including application compatibility and the Windows Container experience with Kubernetes. A major improvement includes reducing the Windows Container image size by up to 40%, which leads to a 30% faster startup time and better performance.

You can now also run applications that depend on Azure Active Directory with group Managed Services Accounts gMSA without domain joining the container host/virtualization/windowscontainers/manage-containers/manage-serviceaccounts, and Windows Containers now support Microsoft Distributed Transaction Control MSDTC and Microsoft Message Queuing MSMQ.

There are several other enhancements that simplify the Windows Container experience with Kubernetes. These enhancements include support for host-process containers for node configuration, IPv6, and consistent network policy implementation with Calico.

In addition to platform improvements, Windows Admin Center has been updated to make it easy to containerize .NET applications. Once the application is in a container, you can host it on Azure Container Registry to then deploy it to other Azure services, including Azure Kubernetes Service.

With support for Intel Ice Lake processors, Windows Server 2022 supports business-critical and large-scale applications, such as SQL Server, that require up to 48 TB of memory and 2,048 logical cores running on 64 physical sockets. Confidential computing with Intel Secured Guard Extension SGX on Intel Ice Lake improves application security by isolating applications from each other with protected memory.

## Other key features

### Nested virtualization for AMD processors

Nested virtualization is a feature that allows you to run Hyper-V inside of a Hyper-V virtual machine VM. Windows Server 2022 brings support for nested virtualization using AMD processors, giving more choices of hardware for your environments. More information can be found at the nested virtualization documentation/virtualization/hyper-v-on-windows/user-guide/nested-virtualization.

### Microsoft Edge browser

Microsoft Edge is included with Windows Server 2022, replacing Internet Explorer. It is built on Chromium open source and backed by Microsoft security and innovation. It can be used with Server Core or Server with Desktop Experience installation options. More information can be found at the Microsoft Edge Enterprise documentation/DeployEdge/. Note that Microsoft Edge, unlike the rest of Windows Server, follows the Modern Lifecycle for its support lifecycle. For details, see Microsoft Edge lifecycle documentation/lifecycle/products/microsoft-edge.

### Storage

#### Storage Migration Service

Enhancements to Storage Migration Service in Windows Server 2022 makes it easier to migrate storage to Windows Server or to Azure from more source locations. Here are the features that are available when running the Storage Migration Server orchestrator on Windows Server 2022:

* Migrate local users and groups to the new server.
* Migrate storage from failover clusters, migrate to failover clusters, and migrate between standalone servers and failover clusters.
* Migrate storage from a Linux server that uses Samba.
* More easily sync migrated shares into Azure by using Azure File Sync.
* Migrate to new networks such as Azure.
* Migrate NetApp CIFS servers from NetApp FAS arrays to Windows servers and clusters.

#### Adjustable storage repair speed

User adjustable storage repair speed/azure-stack/hci/manage/storage-repair-speed is a new feature in Storage Spaces Direct that offers more control over the data resync process by allocating resources to either repair data copies resiliency or run active workloads performance. This helps improve availability and allows you to service your clusters more flexibly and efficiently.

#### Storage bus cache with Storage Spaces on standalone servers

Storage bus cache is now available for standalone servers. It can significantly improve read and write performance, while maintaining storage efficiency and keeping the operational costs low. Similar to its implementation for Storage Spaces Direct, this feature binds together faster media for example, NVMe or SSD with slower media for example, HDD to create tiers. A portion of the faster media tier is reserved for the cache. To learn more, see Enable storage bus cache with Storage Spaces on standalone servers../storage/storage-spaces/storage-spaces-storage-bus-cache.md.

#### SMB compression

Enhancement to SMB in Windows Server 2022 and Windows 11 allows a user or application to compress files as they transfer over the network. Users no longer have to manually zip files in order to transfer much faster on slower or more congested networks. For details, see SMB Compression../storage/file-server/smb-compression.md.

:::moniker-end
<!-- end 2022 -->
<!-- 2019 -->
:::moniker range="windows-server-2019"

## Windows Server 2019

This article describes some of the new features in Windows Server 2019. Windows Server 2019 is built on the strong foundation of Windows Server 2016 and brings numerous innovations on four key themes: Hybrid Cloud, Security, Application Platform, and Hyper-Converged Infrastructure HCI.

## General

### Windows Admin Center

Windows Admin Center is a locally deployed, browser-based app for managing servers, clusters, hyper-converged infrastructure, and Windows 10 PCs. It comes at no additional cost beyond Windows and is ready to use in production.

You can install Windows Admin Center on Windows Server 2019 as well as Windows 10 and earlier versions of Windows and Windows Server, and use it to manage servers and clusters running Windows Server 2008 R2 and later.

For more info, see Windows Admin Center../manage/windows-admin-center/overview.md.

### Desktop experience

Because Windows Server 2019 is a Long-Term Servicing Channel LTSC release, it includes the **Desktop Experience**. Semi-Annual Channel \SAC\ releases don't include the Desktop Experience by design; they are strictly Server Core and Nano Server container image releases. As with Windows Server 2016, during setup of the operating system you can choose between Server Core installations or Server with Desktop Experience installations.

### System Insights

System Insights is a new feature available in Windows Server 2019 that brings local predictive analytics capabilities natively to Windows Server. These predictive capabilities, each backed by a machine-learning model, locally analyze Windows Server system data, such as performance counters and events, providing insight into the functioning of your servers and helping you reduce the operational expenses associated with reactively managing issues in your Windows Server deployments.

## Hybrid Cloud

### Server Core App Compatibility Feature on Demand

The Server Core App Compatibility Feature on Demand FOD../get-started-19/install-fod-19.md significantly improves the app compatibility of the Windows Server Core installation option by including a subset of binaries and components from Windows Server with the Desktop Experience, without adding the Windows Server Desktop Experience graphical environment itself.  This is done to increase the functionality and compatibility of Server Core while keeping it as lean as possible.

This optional feature on demand is available on a separate ISO and can be added to Windows Server Core installations and images only, using DISM.

## Security

### Windows Defender Advanced Threat Protection ATP

ATP's deep platform sensors and response actions expose memory and kernel level attacks and respond by suppressing malicious files and terminating malicious processes.

- For more information about Windows Defender ATP, see Overview of Windows Defender ATP capabilities/windows/security/threat-protection/windows-defender-atp/overview.

- For more information on onboarding servers, see Onboard servers to Windows Defender ATP service/windows/security/threat-protection/windows-defender-atp/configure-server-endpoints-windows-defender-advanced-threat-protection.

**Windows Defender ATP Exploit Guard** is a new set of host-intrusion prevention capabilities. The four components of Windows Defender Exploit Guard are designed to lock down the device against a wide variety of attack vectors and block behaviors commonly used in malware attacks, while enabling you to balance security risk and productivity requirements.

- Attack Surface ReductionASR/windows/security/threat-protection/windows-defender-exploit-guard/attack-surface-reduction-exploit-guard?ocid=cx-blog-mmpc is set of controls that enterprises can enable to prevent malware from
    getting on the machine by blocking suspicious malicious files for example,
    Office files, scripts, lateral movement, ransomware behavior, and
    email-based threats.

- Network protection/windows/security/threat-protection/microsoft-defender-atp/network-protection
    protects the endpoint against web-based threats by blocking any outbound
    process on the device to untrusted hosts/IP addresses through Windows
    Defender SmartScreen.

- Controlled folder accesshttps://cloudblogs.microsoft.com/microsoftsecure/2017/10/23/stopping-ransomware-where-it-counts-protecting-your-data-with-controlled-folder-access/?ocid=cx-blog-mmpc?source=mmpc
    protects sensitive data from ransomware by blocking untrusted processes from
    accessing your protected folders.

- Exploit protection/windows/security/threat-protection/windows-defender-exploit-guard/exploit-protection-exploit-guard is a set of mitigations for vulnerability exploits replacing EMETthat can
    be easily configured to protect your system and applications.

- Windows Defender Application Control/windows/security/threat-protection/windows-defender-application-control/windows-defender-application-control also known as Code Integrity CI policy was released in Windows Server 2016. Customer feedback has suggested that it is a great concept, but hard to deploy. To address this, we have built default CI policies, which allows all Windows in-box files and Microsoft applications, such as SQL Server, and block known executables that can bypass CI.

### Security with Software Defined Networking SDN

Security with SDN../networking/sdn/security/sdn-security-top.md delivers many features to increase customer confidence in running workloads, either on-premises, or as a service provider in the cloud.

These security enhancements are integrated into the comprehensive SDN platform introduced in Windows Server 2016.

For a complete list of what's new in SDN see, What's New in SDN for Windows Server 2019../networking/sdn/sdn-whats-new.md.

### Shielded Virtual Machines improvements

- **Branch office improvements**

    You can now run shielded virtual machines on machines with intermittent connectivity to the Host Guardian Service by using the new fallback HGS../security/guarded-fabric-shielded-vm/guarded-fabric-manage-branch-office.md#fallback-configuration and offline mode../security/guarded-fabric-shielded-vm/guarded-fabric-manage-branch-office.md#offline-mode features. Fallback HGS allows you to configure a second set of URLs for Hyper-V to try if it can't reach your primary HGS server.

    Offline mode allows you to continue to start up your shielded VMs, even if HGS can't be reached, as long as the VM has started successfully once, and the host's security configuration has not changed.

- **Troubleshooting improvements**

    We've also made it easier to troubleshoot your shielded virtual machines../security/guarded-fabric-shielded-vm/guarded-fabric-troubleshoot-shielded-vms.md by enabling support for VMConnect Enhanced Session Mode and PowerShell Direct. These tools are particularly useful if you've lost network connectivity to your VM and need to update its configuration to restore access.

    These features do not need to be configured, and they become available automatically when a shielded VM is placed on a Hyper-V host running Windows Server version 1803 or later.

- **Linux support**

    If you run mixed-OS environments, Windows Server 2019 now supports running Ubuntu, Red Hat Enterprise Linux, and SUSE Linux Enterprise Server inside shielded virtual machines.

### HTTP/2 for a faster and safer Web

- Improved coalescing of connections to deliver an uninterrupted and properly encrypted browsing experience.

- Upgraded HTTP/2's server-side cipher suite negotiation for automatic mitigation of connection failures and ease of deployment.

- Changed our default TCP congestion provider to Cubic to give you more throughput!

## Storage

Here are some of the changes we've made to storage in Windows Server 2019. For details, see What's new in Storage../storage/whats-new-in-storage.md.

### Storage Migration Service

Storage Migration Service is a new technology that makes it easier to migrate servers to a newer version of Windows Server. It provides a graphical tool that inventories data on servers, transfers the data and configuration to newer servers, and then optionally moves the identities of the old servers to the new servers so that apps and users don't have to change anything. For more info, see Storage Migration Service../storage/storage-migration-service/overview.md.

### Storage Spaces Direct

Here's a list of what's new in Storage Spaces Direct. For details, see What's new in Storage Spaces Direct../storage/whats-new-in-storage.md#storage-spaces-direct. Also see Azure Stack HCI/azure-stack/operator/azure-stack-hci-overview for info on acquiring validated Storage Spaces Direct systems.

- Deduplication and compression for ReFS volumes
- Native support for persistent memory
- Nested resiliency for two-node hyper-converged infrastructure at the edge
- Two-server clusters using a USB flash drive as a witness
- Windows Admin Center support
- Performance history
- Scale up to 4 PB per cluster
- Mirror-accelerated parity is 2X faster
- Drive latency outlier detection
- Manually delimit the allocation of volumes to increase fault tolerance

### Storage Replica

Here's what's new in Storage Replica. For details, see What's new in Storage Replica../storage/whats-new-in-storage.md#storage-replica.

- Storage Replica is now available in Windows Server 2019 Standard Edition.
- Test failover is a new feature that allows mounting of destination storage to validate replication or backup data. For more information, see Frequently Asked Questions about Storage Replica../storage/storage-replica/storage-replica-frequently-asked-questions.yml.
- Storage Replica log performance improvements
- Windows Admin Center support

## Failover Clustering

Here's a list of what's new in Failover Clustering. For details, see What's new in Failover Clustering../failover-clustering/whats-new-in-failover-clustering.md.

- Cluster sets
- Azure-aware clusters
- Cross-domain cluster migration
- USB witness
- Cluster infrastructure improvements
- Cluster Aware Updating supports Storage Spaces Direct
- File share witness enhancements
- Cluster hardening
- Failover Cluster no longer uses NTLM authentication

## Application Platform

### Linux containers on Windows

It is now possible to run Windows and Linux-based containers on the same container host, using the same docker daemon. This enables you to have a heterogeneous container host environment while providing flexibility to application developers.

### Built-in support for Kubernetes

Windows Server 2019 continues the improvements to compute, networking, and storage from the Semi-Annual Channel releases needed to support Kubernetes on Windows. More details are available in upcoming Kubernetes releases.

- Container Networking../networking/sdn/technologies/containers/container-networking-overview.md in Windows Server 2019 greatly improves usability of Kubernetes on Windows by enhancing platform networking resiliency and support of container networking plugins.

- Deployed workloads on Kubernetes are able to use network security to protect both Linux and Windows services using embedded tooling.

### Container improvements

- **Improved integrated identity**

    We've made integrated Windows authentication in containers easier and more reliable, addressing several limitations from prior versions of Windows Server.

- **Better application compatibility**

    Containerizing Windows-based applications just got easier: The app compatibility for the existing **windowsservercore** image has been increased. For applications with additional API dependencies, there is now a third base image: **windows**.

- **Reduced size and higher performance**

    The base container image download sizes, size on disk and startup times have been improved. This speeds up container workflows

- **Management experience using Windows Admin Center \preview\**

    We've made it easier than ever to see which containers are running on your computer and manage individual containers with a new extension for Windows Admin Center. Look for the "Containers" extension in the Windows Admin Center public feed../manage/windows-admin-center/configure/using-extensions.md.

### Encrypted Networks

Encrypted Networks../networking/sdn/sdn-whats-new.md - Virtual network encryption allows encryption of virtual network traffic between virtual machines that communicate with each other within subnets marked as **Encryption Enabled**.
It also utilizes Datagram Transport Layer Security DTLS on the virtual subnet to encrypt packets. DTLS protects against eavesdropping, tampering, and forgery by anyone with access to the physical network.

### Network performance improvements for virtual workloads

Network performance improvements for virtual workloads../networking/technologies/hpn/hpn-insider-preview.md maximizes the network throughput to virtual machines without requiring you to constantly tune or over-provision your host. This lowers the operations and maintenance cost while increasing the available density of your hosts. These new features are:

- Receive Segment Coalescing in the vSwitch

- Dynamic Virtual Machine Multi-Queue d.VMMQ

### Low Extra Delay Background Transport

Low Extra Delay Background Transport LEDBAT is a latency optimized, network congestion control provider designed to automatically yield bandwidth to users and applications, while consuming the entire bandwidth available when the network is not in use. This technology is intended for use in deploying large, critical updates across an IT environment without impacting customer facing services and associated bandwidth.

### Windows Time Service

The Windows Time Service../networking/windows-time-service/insider-preview.md includes true UTC-compliant leap second support, a new time protocol called Precision Time Protocol, and end-to-end traceability.

### High performance SDN gateways

High performance SDN gateways../networking/sdn/gateway-performance.md in Windows Server 2019 greatly improves the performance for IPsec and GRE connections, providing ultra-high-performance throughput with much less CPU utilization.

### New Deployment UI and Windows Admin Center extension for SDN

Now, with Windows Server 2019, it's easy to deploy and manage through a new deployment UI and Windows Admin Center extension that enable anyone to harness the power of SDN.

### Persistent Memory support for Hyper-V VMs

To leverage the high throughput and low latency of persistent memory also known as storage class memory in virtual machines, it can now be projected directly into VMs. This can help to drastically reduce database transaction latency or reduce recovery times for low latency in-memory databases on failure.
:::moniker-end
<!-- end 2019 -->
<!-- 2016 -->
:::moniker range="windows-server-2016"
## Windows Server 2016

This article describes some of the new features in Windows Server 2016 that are the ones most likely to have the greatest impact as you work with this release.

## Compute

The Virtualization area../virtualization/virtualization.yml includes virtualization products and features for the IT professional to design, deploy, and maintain Windows Server.

### General

Physical and virtual machines benefit from greater time accuracy due to improvements in the Win32 Time and Hyper-V Time Synchronization Services. Windows Server can now host services that are compliant with upcoming regulations that require a 1ms accuracy with regard to UTC.

### Hyper-V

- What's new in Hyper-V on Windows Server 2016../virtualization/hyper-v/What-s-new-in-Hyper-V-on-Windows.md. This topic explains the new and changed functionality of the Hyper-V role in Windows Server 2016, Client Hyper-V running on Windows 10, and Microsoft Hyper-V Server 2016.

- Windows Containers/virtualization/windowscontainers/:  Windows Server 2016 container support adds performance improvements, simplified network management, and support for Windows containers on Windows 10. For some additional information on containers, see Containers: Docker, Windows and Trendshttps://azure.microsoft.com/blog/2015/08/17/containers-docker-windows-and-trends/.

### Nano Server

What's New in Nano Servergetting-started-with-nano-server.md. Nano Server now has an updated module for building Nano Server images, including more separation of physical host and guest virtual machine functionality as well as support for different Windows Server editions.

There are also improvements to the Recovery Console, including separation of inbound and outbound firewall rules as well as the ability to repair the configuration of WinRM.

### Shielded Virtual Machines

Windows Server 2016 provides a new Hyper-V-based Shielded Virtual Machine to protect any Generation 2 virtual machine from a compromised fabric. Among the features introduced in Windows Server 2016 are the following:

- A new **Encryption Supported** mode that offers more protections than for an ordinary virtual machine, but less than **Shielded** mode, while still supporting vTPM, disk encryption, Live Migration traffic encryption, and other features, including direct fabric administration conveniences such as virtual machine console connections and PowerShell Direct.

- Full support for converting existing non-shielded Generation 2 virtual machines to shielded virtual machines, including automated disk encryption.

- Hyper-V Virtual Machine Manager can now view the fabrics upon which a shielded virtual is authorized to run, providing a way for the fabric administrator to open a shielded virtual machine's key protector KP and view the fabrics it is permitted to run on.

- You can switch Attestation modes on a running Host Guardian Service. Now you can switch on the fly between the less secure but simpler Active Directory-based attestation and TPM-based attestation.

- End-to-end diagnostics tooling based on Windows PowerShell that is able to detect misconfigurations or errors in both guarded Hyper-V hosts and the Host Guardian Service.

- A recovery environment that offers a means to securely troubleshoot and repair shielded virtual machines within the fabric in which they normally run while offering the same level of protection as the shielded virtual machine itself.

- Host Guardian Service support for existing safe Active Directory – you can direct the Host Guardian Service to use an existing Active Directory forest as its Active Directory instead of creating its own Active Directory instance

For more details and instructions for working with shielded virtual machines, see Guarded Fabric and Shielded VMs../security/guarded-fabric-shielded-vm/guarded-fabric-and-shielded-vms-top-node.md.

## Identity and Access

New features in Identity../identity/Identity-and-Access.yml improve the ability for organizations to secure Active Directory environments and help them migrate to cloud-only deployments and hybrid deployments, where some applications and services are hosted in the cloud and others are hosted on premises.

### Active Directory Certificate Services

Active Directory Certificate Services AD CS in Windows Server 2016 increases support for TPM key attestation: You can now use Smart Card KSP for key attestation, and devices that are not joined to the domain can now use NDES enrollment to get certificates that can be attested for keys being in a TPM.

### Active Directory Domain Services

Active Directory Domain Services includes improvements to help organizations secure Active Directory environments and provide better identity management experiences for both corporate and personal devices. For more information, see What's new in Active Directory Domain Services AD DS in Windows Server 2016../identity/whats-new-active-directory-domain-services.md.

### Active Directory Federation Services

What's New in Active Directory Federation Services. Active Directory Federation Services AD FS in Windows Server 2016 includes new features that enable you to configure AD FS to authenticate users stored in Lightweight Directory Access Protocol LDAP directories. For more information, see What's New in AD FS for Windows Server 2016../identity/ad-fs/overview/whats-new-active-directory-federation-services-windows-server.md.

### Web Application Proxy

The latest version of Web Application Proxy focuses on new features that enable publishing and pre-authentication for more applications and improved user experience. Check out the full list of new features that includes pre-authentication for rich client apps such as Exchange ActiveSync and wildcard domains for easier publishing of SharePoint apps. For more information, see Web Application Proxy in Windows Server 2016../remote/remote-access/web-application-proxy/web-application-proxy-windows-server.md.

## Administration

The Management and Automation area../administration/manage-windows-server.yml focuses on tool and reference information for IT pros who want to run and manage Windows Server 2016, including Windows PowerShell.

Windows PowerShell 5.1 includes significant new features, including support for developing with classes and new security features that extend its use, improve its usability, and allow you to control and manage Windows-based environments more easily and comprehensively. See New Scenarios and Features in WMF 5.1/powershell/wmf/5.1/scenarios-features for details.

New additions for Windows Server 2016 include: the ability to run PowerShell.exe locally on Nano Server no longer remote only, new Local Users & Groups cmdlets to replace the GUI, added PowerShell debugging support, and added support in Nano Server for security logging & transcription and JEA.

Here are some other new administration features:

### PowerShell Desired State Configuration DSC in Windows Management Framework WMF 5

Windows Management Framework 5 includes updates to Windows PowerShell Desired State Configuration DSC, Windows Remote Management WinRM, and Windows Management Instrumentation WMI.

For more info about testing the DSC features of Windows Management Framework 5, see the series of blog posts discussed in Validate features of PowerShell DSChttps://devblogs.microsoft.com/powershell/validate-features-of-powershell-dsc/. To download, see Windows Management Framework 5.1/powershell/scripting/wmf/setup/install-configure.

### PackageManagement unified package management for software discovery, installation, and inventory

Windows Server 2016 and Windows 10 includes a new PackageManagement feature formerly called OneGet that enables IT Professionals or DevOps to automate software discovery, installation, and inventory SDII, locally or remotely, no matter what the installer technology is and where the software is located.

For more info, see https://github.com/OneGet/oneget/wikihttps://github.com/OneGet/oneget/wiki.

### PowerShell enhancements to assist digital forensics and help reduce security breaches

To help the team responsible for investigating compromised systems - sometimes known as the "blue team" - we've added additional PowerShell logging and other digital forensics functionality, and we've added functionality to help reduce vulnerabilities in scripts, such as constrained PowerShell, and secure CodeGeneration APIs.

For more info, see the PowerShell ♥ the Blue Teamhttps://devblogs.microsoft.com/powershell/powershell-the-blue-team/ blog post.

## Networking

The Networking area../networking/index.yml addresses networking products and features for the IT professional to design, deploy, and maintain Windows Server 2016.

### Software-Defined Networking

You can now both mirror and route traffic to new or existing virtual appliances. Together with a distributed firewall and Network security groups, this enables you to dynamically segment and secure workloads in a manner similar to Azure. Second, you can deploy and manage the entire Software-defined networking SDN stack using System Center Virtual Machine Manager. Finally, you can use Docker to manage Windows Server container networking, and associate SDN policies not only with virtual machines but containers as well. For more information, see Plan a Software Defined Network Infrastructure/azure-stack/hci/concepts/plan-software-defined-networking-infrastructure.

### TCP performance improvements

The default Initial Congestion Window ICW has been increased from 4 to 10 and TCP Fast Open TFO has been implemented. TFO reduces the amount of time required to establish a TCP connection and the increased ICW allows larger objects to be transferred in the initial burst. This combination can significantly reduce the time required to transfer an Internet object between the client and the cloud.

In order to improve TCP behavior when recovering from packet loss we have implemented TCP Tail Loss Probe TLP and Recent Acknowledgment RACK. TLP helps convert Retransmit TimeOuts RTOs to Fast Recoveries and RACK reduces the time required for Fast Recovery to retransmit a lost packet.

## Security and Assurance

The Security and Assurance area../security/Security-and-Assurance.yml Includes security solutions and features for the IT professional to deploy in your data center and cloud environment. For information about security in Windows Server 2016 generally, see Security and Assurance../security/Security-and-Assurance.yml.

### Just Enough Administration

Just Enough Administration in Windows Server 2016 is security technology that enables delegated administration for anything that can be managed with Windows PowerShell. Capabilities include support for running under a network identity, connecting over PowerShell Direct, securely copying files to or from JEA endpoints, and configuring the PowerShell console to launch in a JEA context by default. For more details, see JEA on GitHubhttps://aka.ms/JEA.

### Credential Guard

Credential Guard uses virtualization-based security to isolate secrets so that only privileged system software can access them. See Protect derived domain credentials with Credential Guard/windows/security/identity-protection/credential-guard/credential-guard.

### Remote Credential Guard

Credential Guard includes support for RDP sessions so that the user credentials remain on the client side and are not exposed on the server side. This also provides Single Sign On for Remote Desktop. See Protect derived domain credentials with Windows Defender Credential Guard/windows/access-protection/credential-guard/credential-guard.

### Device Guard Code Integrity

Device Guard provides kernel mode code integrity KMCI and user mode code integrity UMCI by creating policies that specify what code can run on the server. See Introduction to Windows Defender Device Guard: virtualization-based security and code integrity policies/windows/device-security/device-guard/introduction-to-device-guard-virtualization-based-security-and-code-integrity-policies.

### Windows Defender

Windows Defender Overview for Windows Server 2016../security/windows-defender/windows-defender-overview-windows-server.md. Windows Server Antimalware is installed and enabled by default in Windows Server 2016, but the user interface for Windows Server Antimalware is not installed. However, Windows Server Antimalware will update antimalware definitions and protect the computer without the user interface. If you need the user interface for Windows Server Antimalware, you can install it after the operating system installation by using the Add Roles and Features Wizard.

### Control Flow Guard

Control Flow Guard CFG is a platform security feature that was created to combat memory corruption vulnerabilities. See Control Flow Guard/windows/win32/secbp/control-flow-guard for more information.

## Storage

Storage../storage/storage.yml in Windows Server 2016 includes new features and enhancements for software-defined storage, as well as for traditional file servers. Below are a few of the new features, for more enhancements and further details, see What's New in Storage in Windows Server 2016../storage/whats-new-in-storage.md.

### Storage Spaces Direct

Storage Spaces Direct enables building highly available and scalable storage using servers with local storage. It simplifies the deployment and management of software-defined storage systems and unlocks use of new classes of disk devices, such as SATA SSD and NVMe disk devices, that were previously not possible with clustered Storage Spaces with shared disks.

For more info, see Storage Spaces Direct../storage/storage-spaces/storage-spaces-direct-overview.md.

### Storage Replica

Storage Replica enables storage-agnostic, block-level, synchronous replication between servers or clusters for disaster recovery, as well as stretching of a failover cluster between sites. Synchronous replication enables mirroring of data in physical sites with crash-consistent volumes to ensure zero data loss at the file-system level. Asynchronous replication allows site extension beyond metropolitan ranges with the possibility of data loss.

For more info, see Storage Replica../storage/storage-replica/storage-replica-overview.md.

### Storage Quality of Service QoS

You can now use storage quality of service QoS to centrally monitor end-to-end storage performance and create management policies using Hyper-V and CSV clusters in Windows Server 2016.

For more info, see Storage Quality of Service../storage/storage-qos/storage-qos-overview.md.

## Failover Clustering../failover-clustering/whats-new-in-failover-clustering.md

Windows Server 2016 includes a number of new features and enhancements for multiple servers that are grouped together into a single fault-tolerant cluster using the Failover Clustering feature. Some of the additions are listed below; for a more complete listing, see What's New in Failover Clustering in Windows Server 2016../failover-clustering/whats-new-in-failover-clustering.md.

### Cluster Operating System Rolling Upgrade

Cluster Operating System Rolling Upgrade enables an administrator to upgrade the operating system of the cluster nodes from  Windows Server 2012 R2  to Windows Server 2016 without stopping the Hyper-V or the Scale-Out File Server workloads. Using this feature, the downtime penalties against Service Level Agreements SLA can be avoided.

For more info, see Cluster Operating System Rolling Upgrade../failover-clustering/Cluster-Operating-System-Rolling-Upgrade.md.

### Cloud Witness

Cloud Witness is a new type of Failover Cluster quorum witness in Windows Server 2016 that leverages Microsoft Azure as the arbitration point. The Cloud Witness, like any other quorum witness, gets a vote and can participate in the  quorum calculations. You can configure cloud witness as a quorum witness using the Configure a Cluster Quorum Wizard.

For more info, see Deploy Cloud Witness../failover-clustering/deploy-cloud-witness.md.

### Health Service

The Health Service improves the day-to-day monitoring, operations, and maintenance experience of cluster resources on a Storage Spaces Direct cluster.

For more info, see Health Service../failover-clustering/health-service-overview.md.

## Application development

### Internet Information Services IIS 10.0

New features provided by the IIS 10.0 web server in Windows Server 2016 include:

- Support for the HTTP/2 protocol in the Networking stack and integrated with IIS 10.0, allowing IIS 10.0 websites to automatically serve HTTP/2 requests for supported configurations. This allows numerous enhancements over HTTP/1.1 such as more efficient reuse of connections and decreased latency, improving load times for web pages.
- Ability to run and manage IIS 10.0 in Nano Server. See IIS on Nano Serveriis-on-nano-server.md.
- Support for Wildcard Host Headers, enabling administrators to set up a web server for a domain and then have the web server serve requests for any subdomain.
- A new PowerShell module IISAdministration for managing IIS.

For more details see IIShttps://iis.net/learn.

### Distributed Transaction Coordinator MSDTC

Three new features are added in Microsoft Windows 10 and Windows Server 2016:

- A new interface for Resource Manager Rejoin can be used by a resource manager to determine the outcome of an in-doubt transaction after a database restarts due to an error. See IResourceManagerRejoinable::Rejoin/previous-versions/windows/desktop/mt203799v=vs.85 for details.

- The DSN name limit is enlarged from 256 bytes to 3072 bytes. See IDtcToXaHelperFactory::Create/previous-versions/windows/desktop/ms686861v=vs.85, IDtcToXaHelperSinglePipe::XARMCreate/previous-versions/windows/desktop/ms679248v=vs.85, or IDtcToXaMapper::RequestNewResourceManager/previous-versions/windows/desktop/ms680310v=vs.85 for details.

- Improved tracing allowing you to set a registry key to include an image file path in the trace log file name so you can tell which trace log file to check. See How to enable diagnostic tracing for MS DTC on a Windows-based computerhttps://support.microsoft.com/kb/926099 for details on configuring tracing for MSDTC.

:::moniker-end
<!-- end 2016 -->
<!-- 2012 -->
:::moniker range="windows-server-2012"
Add what's new for 2012 here.
:::moniker-end
<!-- end 2012 -->
<!-- 2008 -->
:::moniker range="windows-server-2008"
Add what's new for 2008 here.
:::moniker-end
<!-- end 2008 -->