---
title: Windows Server How-To list 
description: This article is a curated list of things you would do with Windows Server.
author: IngridAtMicrosoft
ms.author: inhenkel
ms.topic: article
ms.date: 08/26/2021
ms.service: media-services
---

# Windows Server How-To list

This article is a curated list of things you would do with Windows Server. The following list is taken from the objective domain for the Windows Server 2016 MCSA Certification.  08/25/2021: This is a starting point for all how-to articles to be developed for the Windows Server content overhaul. I will be adding items from the newest objective domain for the cert that is currently in development.

## Install Windows Servers in Host and Compute Environments

### Install, upgrade, and migrate servers and workloads

- Determine Windows Server installation requirements.
- Determine appropriate Windows Server 2016 editions per workloads.
- Install Windows Server.
- Install Windows Server features and roles.
- Install and- Configure Windows Server Core.
- Manage Windows Server Core installations using Windows PowerShell, command line, and remote- Management capabilities.
- Implement Windows PowerShell Desired State Configuration (DSC) to install and maintain integrity of installed environments.
- Perform upgrades and migrations of servers and core workloads from Windows Server 2008 and Windows Server 2012 to Windows Server 2016.
- Determine the appropriate activation model for server installation, such as Automatic Virtual Machine Activation (AVMA), Key- Management Service (KMS), and Active Directory-based Activation.

### Create,- Manage, and maintain images for deployment

- Plan for Windows Server virtualization
- Assess virtualization workloads using the Microsoft Assessment and Planning (MAP) Toolkit
- Determine considerations for deploying workloads into virtualized environments
- Update images with patches, hotfixes, last cumulative updates and drivers.
- Install roles and features in offline images.
- Manage and maintain Windows Server Core, and VHDs using Windows PowerShell

## Implement Storage Solutions

### Configure disks and volumes

- Configure sector sizes appropriate for various workloads.
- Configure GUID partition table (GPT) disks.
- Create VHD and VHDX files using Disk- Management or Windows PowerShell.
- Mount virtual hard disks.
- Determine when to use NTFS and ReFS file systems.
- Configure NFS and SMB shares using Server- Manager.
- Configure SMB share and session settings using Windows PowerShell.
- Configure SMB server and SMB client configuration settings using Windows PowerShell.
- Configure file and folder permissions.

### Implement server storage

- Configure storage pools.
- Implement simple, mirror, and parity storage layout options for disks or enclosures.
- Expand storage pools.
- Configure Tiered Storage.
- Configure iSCSI target and initiator.
- Configure iSNS.
- Configure Datacenter Bridging (DCB).
- Configure Multi-Path IO (MPIO).
- Determine usage scenarios for Storage Replica.
- Implement Storage Replica for server-to-server, cluster-to-cluster, and stretch cluster scenarios.

### Implement data deduplication

- Implement and- Configure deduplication.
- Determine appropriate usage scenarios for deduplication.
- Monitor deduplication.
- Implement a backup and- Restore solution with deduplication.

## Implement Hyper-V

### Install and- Configure Hyper-V

- Determine hardware and compatibility requirements for installing Hyper-V.
- Install Hyper-V.
- Install- Management tools.
- Upgrade from existing versions of Hyper-V.
- Delegate virtual machine- Management.
- Perform remote- Management of Hyper-V hosts.
- Use Windows PowerShell Direct.
- Implement nested virtualization.

### Configure virtual machine (VM) settings

- Add or remove memory in a running VM.
- Configure dynamic memory.
- Configure Non-Uniform Memory Access (NUMA) support.
- Configure smart paging.
- Configure Resource Metering.
- Manage Integration Services.
- Create and configure Generation 1 and 2 VMs and- Determine appropriate usage scenarios.
- Implement enhanced session mode.
- Create Linux and FreeBSD VMs.
- Install and- Configure Linux Integration Services (LIS).
- Install and- Configure FreeBSD Integration Services (BIS).
- Implement Secure Boot for Windows and Linux environments.
- Move and convert VMs from previous versions of Hyper-V to Windows Server 2016 Hyper-V.
- Export and import VMs.
- Implement Discrete Device Assignment (DDA), Troubleshoot VM configuration versions.

### Configure Hyper-V storage

- Create VHDs and VHDX files using Hyper-V- Manager.
- Create shared VHDX files.
- Configure differencing disks.
- Modify virtual hard disks.
- Configure pass-through disks.
- Resize a virtual hard disk.
- Manage checkpoints.
- Implement production checkpoints.
- Implement a virtual Fibre Channel adapter.
- Configure storage Quality of Service (QoS)

### Configure Hyper-V networking

- Add and remove virtual network interface cards (vNICs).
- Configure Hyper-V virtual switches.
- Optimize network- Performance.
- Configure MAC addresses.
- Configure network isolation.
- Configure synthetic and legacy virtual network adapters.
- Configure NIC teaming in VMs.
- Configure virtual machine queue (VMQ).
- Enable Remote Direct Memory Access (RDMA) on network adapters bound to a Hyper-V virtual switch using Switch Embedded Teaming (SET).
- Configure Bandwidth- Management

## Implement Windows Containers

### Deploy Windows containers

- Determine installation requirements and appropriate scenarios for Windows Containers.
- Install and- Configure Windows Server container host in physical or virtualized environments.
- Install and- Configure Windows Server container host to Windows Server Core in a physical or virtualized environment.
- Install Docker Enterprise Edition on Windows Server.
- Configure Docker start-up options.
- Install a base container image.
- Tag an image.
- Remove a container.
- Create Windows Server containers.
- Create Hyper-V containers

### Manage Windows containers

- Manage Windows containers by using Docker CLI.
- Manage container networking.
- Manage container data volumes.
- Manage Resource Control.
- Create new container images using Dockerfile.
- Manage container images using DockerHub repository for public and private scenarios.
- Manage container images using Microsoft Azure

## Implement High Availability

### Implement high availability and disaster recovery options in Hyper-V

- Implement Hyper-V Replica.
- Implement Live Migration including Shared Nothing Live Migration.
- Configure CredSSP or Kerberos authentication protocol for Live Migration.
- Implement storage migration

### Implement failover clustering

- Implement Workgroup, Single, and Multi Domain clusters.
- Configure quorum.
- Configure cluster networking.
- Restore single node or cluster configuration.
- Configure cluster storage.
- Implement Cluster-Aware Updating.
- Implement Cluster Operating System Rolling Upgrade.
- Configure and optimize cluster shared volumes (CSVs).
- Configure clusters without network names.
- Implement Scale-Out File Server (SoFS).
- Determine different scenarios for the use of SoFS vs. File Server for general use.
- Determine usage scenarios for implementing guest clustering.
- Implement a Clustered Storage Spaces solution using Shared SAS storage enclosures.
- Implement Storage Replica.
- Implement Cloud Witness.
- Implement VM resiliency.
- Implement shared VHDX as a storage solution for guest clusters

### Implement Storage Spaces Direct

- Determine scenario requirements for- Implementing Storage Spaces Direct.
- Enable Storage Spaces Direct using Windows PowerShell.
- Implement a disaggregated Storage Spaces Direct scenario.
- Implement a hyper-converged Storage Spaces Direct scenario

### Manage failover clustering

- Configure role-specific settings, including continuously available shares.
- Configure VM monitoring.
- Configure failover and preference settings.
- Implement stretch and site-aware failover clusters.
- Enable and configure node fairness.

### Manage VM movement in clustered nodes

- Perform a live migration.
- Perform a quick migration.
- Perform a storage migration.
- Import, export, and copy VMs.
- Configure VM network health protection.
- Configure drain on shutdown

### Implement Network Load Balancing (NLB)

- Install NLB nodes.
- Configure NLB prerequisites.
- Configure affinity.
- Configure port rules.
- Configure cluster operation mode.
- Upgrade an NLB cluster

## Maintain and Monitor Server Environments (10-15%)

## Maintain server installations

- Implement Windows Server Update Services (WSUS) solutions.
- Configure WSUS groups.
- Manage patch- Management in mixed environments.
- Implement an antimalware solution with Windows Defender.
- Integrate Windows Defender with WSUS and Windows Update.
- Perform backup and- Restore operations using Windows Server Backup.
- Determine backup strategies for different Windows Server roles and workloads, including Hyper-V Host, Hyper-V Guests, Active Directory, File Servers, and Web Servers using Windows Server native tools and solutions

### Monitor server installations

- Monitor workloads using- Performance Monitor, Server- Manager, Event Viewer.
- Configure Data Collector Sets.
- Determine appropriate CPU, memory, disk, and networking counters for storage and compute workloads.
- Configure alerts.
- Monitor workloads using Resource Monitor
- Manage and monitor Windows Server by using Windows Admin Center

## Implement Domain Name System (DNS)

### Install and Configure DNS servers

- Determine DNS installation requirements.
- Install DNS.
- Configure forwarders.
- Configure Root Hints.
- Configure delegation.
- Implement DNS policies.
- Configure DNS Server settings using Windows PowerShell.
- Configure Domain Name System Security Extensions (DNSSEC).
- Configure DNS Socket Pool.
- Configure cache locking.
- Enable Response Rate Limiting.
- Configure DNS-based Authentication of Named Entities (DANE).
- Configure DNS logging.
- Configure delegated administration.
- Configure recursion settings.
- Implement DNS- Performance tuning.
- Configure global settings

### Create and Configure DNS zones and records

- Create primary zones.
- Configure Active Directory primary zones.
- Create and configure secondary zones.
- Create and configure stub zones.
- Configure a GlobalNames zone.
- Analyze zone-level statistics.
- Create and configure DNS Resource Records (RR), including A, AAAA, PTR, SOA, NS, SRV, CNAME, and MX records.
- Configure zone scavenging.
- Configure record options, including Time To Live (TTL) and weight.
- Configure round robin.
- Configure secure dynamic updates.
- Configure unknown record support.
- Use DNS audit events and analytical (query) events for auditing and troubleshooting.
- Configure Zone Scopes.
- Configure records in Zone Scopes.
- Configure policies for zones.

## Implement DHCP and IPAM

### Install and configure DHCP

- Install and- Configure DHCP servers.
- Authorize a DHCP server.
- Create and configure scopes.
- Create and configure superscopes and multicast scopes.
- Configure a DHCP reservation.
- Configure DHCP options.
- Configure DNS options from within DHCP.
- Configure policies.
- Configure client and server for PXE boot.
- Configure DHCP Relay Agent.
- Implement IPv6 addressing using DHCPv6.
- Perform export and import of a DHCP server.
- Perform DHCP server migration

### Manage and maintain DHCP

- Configure a lease period.
- Back up and restore the DHCP database.
- Configure high availability using DHCP failover.
- Configure DHCP name protection.
- Troubleshoot DHCP

### Implement and Maintain IP Address- Management (IPAM)

- Provision IPAM manually or by using Group Policy.
- Configure server discovery.
- Create and manage IP blocks and ranges.
- Monitor utilization of IP address space.
- Migrate existing workloads to IPAM.
- Configure IPAM database storage using SQL Server.
- Determine scenarios for using IPAM with System Center Virtual Machine Manager for physical and virtual IP address space management.
- Manage DHCP server properties using IPAM.
- Configure DHCP scopes and options.
- Configure DHCP policies and failover.
- Manage DNS server properties using IPAM.
- Manage DNS zones and records.
- Manage DNS and DHCP servers in multiple Active Directory forests.
- Delegate administration for DNS and DHCP using role-based access control (RBAC).
- Audit the changes- Performed on the DNS and DHCP servers.
- Audit the IPAM address usage trail.
- Audit DHCP lease events and user logon events.

## Implement Network Connectivity and Remote Access Solutions

### Implement network connectivity solutions

- Implement Network Address Translation (NAT).
- Configure routing

### Implement virtual private network (VPN) and DirectAccess solutions

- Implement remote access and site-to-site (S2S) VPN solutions using remote access gateway.
- Configure different VPN protocol options.
- Configure authentication options.
- Configure VPN reconnect.
- Create and configure connection profiles.
- Determine when to use remote access VPN and site-to-site VPN and- Configure appropriate protocols.
- Install and configure DirectAccess.
- Implement server requirements.
- Implement client configuration.
- Troubleshoot DirectAccess.

### Implement Network Policy Server (NPS)

- Configure a RADIUS server including RADIUS proxy.
- Configure RADIUS clients.
- Configure NPS templates.
- Configure RADIUS accounting.
- Configure certificates.
- Configure Connection Request Policies.
- Configure network policies for VPN and wireless and wired clients.
- Import and export NPS policies

## Implement Core and Distributed Network Solutions

### Implement IPv4 and IPv6 addressing

- Configure IPv4 addresses and options.
- Determine and- Configure appropriate IPv6 addresses.
- Configure IPv4 or IPv6 subnetting.
- Implement IPv6 stateless addressing.
- Configure interoperability between IPv4 and IPv6 by using ISATAP, 6to4, and Teredo scenarios.
- Configure Border Gateway Protocol (BGP).
- Configure IPv4 and IPv6 routing

### Implement Distributed File System (DFS) and Branch Office solutions

- Install and- Configure DFS namespaces.
- Configure DFS replication targets.
- Configure replication scheduling.
- Configure Remote Differential Compression (RDC) settings.
- Configure staging.
- Configure fault tolerance.
- Clone a Distributed File System Replication (DFSR) database.
- Recover DFSR databases.
- Optimize DFS Replication.
- Install and configure BranchCache.
- Implement distributed and hosted cache modes.
- Implement BranchCache for web, file, and application servers.
- Troubleshoot BranchCache.

## Implement an Advanced Network Infrastructure

### Implement high performance network solutions

- Implement NIC Teaming or the Switch Embedded Teaming (SET) solution and identify when to use each.
- Enable and- Configure Receive Side Scaling (RSS).
- Enable and- Configure network Quality of Service (QoS) with Data Center Bridging (DCB).
- Enable and- Configure SMB Direct on Remote Direct Memory Access (RDMA)- Enabled network adapters.
- Configure SMB Multichannel.
- Enable and- Configure virtual Receive Side Scaling (vRSS) on a Virtual Machine Queue (VMQ) capable network adapter.
- Enable and- Configure Virtual Machine Multi-Queue (VMMQ).
- Enable and- Configure Single-Root I/O Virtualization (SRIOV) on a supported network adapter.

### Determine scenarios and requirements for- Implementing Software Defined Networking (SDN)

- Determine deployment scenarios and network requirements for deploying SDN.
- Determine requirements and scenarios for- Implementing Hyper-V Network Virtualization (HNV) using Network Virtualization Generic Route Encapsulation (NVGRE) encapsulation or Virtual Extensible LAN (VXLAN) encapsulation.
- Determine scenarios for implementation of Software Load Balancer (SLB) for North-South and East-West load balancing.
- Determine- Implementation scenarios for various types of Windows Server Gateways, including L3, GRE, and S2S, and their use.
- Determine requirements and scenarios for Datacenter firewall policies and network security groups

## Install and configure Active Directory Domain Services (AD DS)

### Install and configure domain controllers

- Install a new forest.
- Add or remove a domain controller from a domain.
- Upgrade a domain controller.
- Install AD DS on a Server Core installation.
- Install a domain controller from Install from Media (IFM).
- Resolve DNS SRV record registration issues.
- Configure a global catalog server.
- Transfer and seize operations master roles.
- Install and- Configure a read-only domain controller (RODC).
- Configure domain controller cloning

### Create and- Manage Active Directory users and computers

- Automate the creation of Active Directory accounts.
- Create, copy,- Configure, and delete users and computers.
- Configure templates.
- Perform bulk Active Directory operations.
- Configure user rights.
- Implement offline domain join.
- Manage inactive and disabled accounts.
- Automate unlocking of disabled accounts.
- Automate password resets.

### Create and manage Active Directory groups and organizational units (OUs)

- Configure group nesting.
- Convert groups, including security, distribution, universal, domain local, and global.
- Manage group membership using Group Policy.
- Enumerate group membership.
- Automate group membership- Management using Windows PowerShell.
- Delegate the creation and- Management of Active Directory groups and OUs.
- Manage default Active Directory containers.
- Create, copy, configure, and delete groups and OUs.

## Manage and Maintain AD DS

### Configure service authentication and account policies

- Create and configure Service Accounts.
- Create and configure Group- Managed Service Accounts (gMSAs).
- Configure Kerberos Constrained Delegation (KCD).
- Manage Service Principal Names (SPNs).
- Configure virtual accounts.
- Configure domain and local user password policy settings.
- Configure and apply Password Settings Objects (PSOs).
- Delegate password settings- Management.
- Configure account lockout policy settings.
- Configure Kerberos policy settings within Group Policy,- Configure Authentication Policies and Authentication Policy Silos

### Maintain Active Directory

- Back up Active Directory and SYSVOL.
- Manage Active Directory offline.
- Perform offline defragmentation of an Active Directory database.
- Clean up metadata.
- Configure Active Directory snapshots.
- Perform object- and container-level recovery.
- Perform Active Directory Restore.
- Configure and- Restore objects by using the Active Directory Recycle Bin.
- Configure replication to Read-Only Domain Controllers (RODCs).
- Configure Password Replication Policy (PRP) for RODC.
- Monitor and- Manage replication.
- Upgrade SYSVOL replication to Distributed File System Replication (DFSR)

### Configure Active Directory in a complex enterprise environment

- Configure a multi-domain and multi-forest Active Directory infrastructure.
- Deploy Windows Server domain controllers within a preexisting Active Directory environment.
- Upgrade existing domains and forests.
- Configure domain and forest functional levels.
- Configure multiple user principal name (UPN) suffixes.
- Configure external, forest, shortcut, and realm trusts.
- Configure trust authentication.
- Configure SID filtering.
- Configure name suffix routing.
- Configure sites and subnets.
- Create and configure site links.
- Manage site coverage.
- Manage registration of SRV records.
- Move domain controllers between sites.

## Create and- Manage Group Policy

### Create and manage Group Policy Objects (GPOs)

- Configure a central store.
- Manage starter GPOs.
- Configure GPO links.
- Configure multiple local Group Policies.
- Back up, import, copy, and- Restore GPOs.
- Create and configure a migration table.
- Reset default GPOs.
- Delegate Group Policy- Management.
- Detect health issues using the Group Policy Infrastructure Status page.

### Configure Group Policy processing

- Configure processing order and precedence.
- Configure blocking of inheritance.
- Configure enforced policies.
- Configure security filtering and Windows- Management Instrumentation (WMI) filtering.
- Configure loopback processing.
- Configure and- Manage slow-link processing and Group Policy caching.
- Configure client-side extension (CSE) behavior.
- Force a Group Policy update.

### Configure Group Policy settings

- Configure software installation.
- Configure folder redirection.
- Configure scripts.
- Configure administrative templates.
- Import security templates.
- Import a custom administrative template file.
- Configure filtering for administrative template

### Configure Group Policy preferences

- Configure printer preferences.
- Define network drive mappings.
- Configure power options.
- Configure custom registry settings.
- Configure Control Panel settings.
- Configure Internet Explorer settings.
- Configure file and folder deployment.
- Configure shortcut deployment.
- Configure item-level targeting

## Implement Active Directory Certificate Services (AD CS)

### Install and configure AD CS

- Install Active Directory Integrated Enterprise Certificate Authority (CA).
- Install offline root and subordinate CAs.
- Install standalone CAs.
- Configure Certificate Revocation List (CRL) distribution points.
- Install and- Configure Online Responder.
- Implement administrative role separation.
- Configure CA backup and recovery

### Manage certificates

- Manage certificate templates.
- Implement and- Manage certificate deployment, validation, and revocation.
- Manage certificate renewal.
- Manage certificate enrolment and renewal for computers and users using Group Policies.
- Configure and- Manage key archival and recovery

## Implement Identity Federation and Access Solutions

### Install and- Configure Active Directory Federation Services (AD FS)

- Upgrade and migrate previous AD FS workloads to Windows Server 2016.
- Implement claims-based authentication, including Relying Party Trusts.
- Configure authentication policies.
- Configure multi-factor authentication.
- Implement and- Configure device registration.
- Integrate AD FS with Microsoft Passport.
- Configure for use with Microsoft Azure and Office 365.
- Configure AD FS to- Enable authentication of users stored in LDAP directories.

### Implement Web Application Proxy (WAP)

- Install and configure WAP.
- Implement WAP in pass-through mode.
- Implement WAP as AD FS proxy. integrate WAP with AD FS.
- Configure AD FS requirements.
- Publish web apps via WAP.
- Publish Remote Desktop Gateway applications.
- Configure HTTP to HTTPS redirects.
- Configure internal and external Fully Qualified Domain Names (FQDNs)

### Install and- Configure Active Directory Rights- Management Services (AD RMS)

- Install a licensor certificate AD RMS server.
- Manage AD RMS Service Connection Point (SCP).
- Manage AD RMS templates.
- Configure Exclusion Policies.
- Back up and restore AD RMS.
