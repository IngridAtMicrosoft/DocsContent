---
ms.topic: include
ms.date: 04/16/2025
ms.custom: microsoft.kubernetesconfiguration/extensions, naam

# NOTE:  This content is automatically generated using API calls to Azure. Any edits made on these files will be overwritten in the next run of the script. 
 
---




### Category: Traffic
|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Active PDU Sessions**<br><br>Number of Active PDU Sessions |`ActiveSessionCount` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |No|
|**Authentication Attempts**<br><br>Authentication attempts rate (per minute) |`AuthAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Authentication Failures**<br><br>Authentication failure rate (per minute) |`AuthFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Result`|PT1M |Yes|
|**Authentication Successes**<br><br>Authentication success rate (per minute) |`AuthSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Connected NodeBs**<br><br>Number of connected gNodeBs or eNodeBs |`ConnectedNodebs` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**DeRegistration Attempts**<br><br>UE deregistration attempts rate (per minute) |`DeRegistrationAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**DeRegistration Successes**<br><br>UE deregistration success rate (per minute) |`DeRegistrationSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Paging Attempts**<br><br>Paging attempts rate (per minute) |`PagingAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Paging Failures**<br><br>Paging failure rate (per minute) |`PagingFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Provisioned Subscribers**<br><br>Number of provisioned subscribers |`ProvisionedSubscribers` |Count |Total (Sum) |`PccpId`, `SiteId`|PT1M |No|
|**RAN Setup Failures**<br><br>RAN setup failure rate (per minute) |`RanSetupFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Cause`|PT1M |Yes|
|**RAN Setup Requests**<br><br>RAN setup reuests rate (per minute) |`RanSetupRequest` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**RAN Setup Responses**<br><br>RAN setup response rate (per minute) |`RanSetupResponse` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Registered Subscribers**<br><br>Number of registered subscribers |`RegisteredSubscribers` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Registered Subscribers Connected**<br><br>Number of registered and connected subscribers |`RegisteredSubscribersConnected` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Registered Subscribers Idle**<br><br>Number of registered and idle subscribers |`RegisteredSubscribersIdle` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Registration Attempts**<br><br>Registration attempts rate (per minute) |`RegistrationAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Registration Failures**<br><br>Registration failure rate (per minute) |`RegistrationFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Result`|PT1M |Yes|
|**Registration Successes**<br><br>Registration success rate (per minute) |`RegistrationSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Service Request Attempts**<br><br>Service request attempts rate (per minute) |`ServiceRequestAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Service Request Failures**<br><br>Service request failure rate (per minute) |`ServiceRequestFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Result`, `Tai`|PT1M |Yes|
|**Service Request Successes**<br><br>Service request success rate (per minute) |`ServiceRequestSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Session Establishment Attempts**<br><br>PDU session establishment attempts rate (per minute) |`SessionEstablishmentAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Dnn`|PT1M |Yes|
|**Session Establishment Failures**<br><br>PDU session establishment failure rate (per minute) |`SessionEstablishmentFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Dnn`|PT1M |Yes|
|**Session Establishment Successes**<br><br>PDU session establishment success rate (per minute) |`SessionEstablishmentSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`, `Dnn`|PT1M |Yes|
|**Session Releases**<br><br>Session release rate (per minute) |`SessionRelease` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**UE Context Release Commands**<br><br>UE context release command message rate (per minute) |`UeContextReleaseCommand` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**UE Context Release Completes**<br><br>UE context release complete message rate (per minute) |`UeContextReleaseComplete` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**UE Context Release Requests**<br><br>UE context release request message rate (per minute) |`UeContextReleaseRequest` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**User Plane Bandwidth**<br><br>User plane bandwidth in bits/second. |`UserPlaneBandwidth` |BitsPerSecond |Total (Sum) |`PcdpId`, `SiteId`, `Direction`, `Interface`|PT1M |No|
|**User Plane Packet Drop Rate**<br><br>User plane packet drop rate (packets/sec) |`UserPlanePacketDropRate` |CountPerSecond |Total (Sum) |`PcdpId`, `SiteId`, `Cause`, `Direction`, `Interface`|PT1M |No|
|**User Plane Packet Rate**<br><br>User plane packet rate (packets/sec) |`UserPlanePacketRate` |CountPerSecond |Total (Sum) |`PcdpId`, `SiteId`, `Direction`, `Interface`|PT1M |No|
|**Xn Handover Attempts**<br><br>Handover attempts rate (per minute) |`XnHandoverAttempt` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Xn Handover Failures**<br><br>Handover failure rate (per minute) |`XnHandoverFailure` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|
|**Xn Handover Successes**<br><br>Handover success rate (per minute) |`XnHandoverSuccess` |Count |Total (Sum) |`3gppGen`, `PccpId`, `SiteId`|PT1M |Yes|