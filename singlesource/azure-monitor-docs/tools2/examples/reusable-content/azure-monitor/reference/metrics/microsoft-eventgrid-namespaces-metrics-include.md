---
ms.topic: include
ms.date: 04/16/2025
ms.custom: Microsoft.EventGrid/namespaces, naam

# NOTE:  This content is automatically generated using API calls to Azure. Any edits made on these files will be overwritten in the next run of the script. 
 
---


|Metric|Name in REST API|Unit|Aggregation|Dimensions|Time Grains|DS Export|
|---|---|---|---|---|---|---|
|**Acknowledge Operations Latency**<br><br>The observed latency in milliseconds for acknowledge events operation. |`AcknowledgeLatencyInMilliseconds` |MilliSeconds |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|
|**Failed Acknowledged Events**<br><br>The number of events for which acknowledgements from clients failed. |`FailedAcknowledgedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`, `Error`, `ErrorType`|PT1M |No|
|**Failed Publish Events**<br><br>The number of events that weren't accepted by Event Grid. This count excludes events that were published but failed to reach Event Grid due to a network issue, for example. |`FailedPublishedEvents` |Count |Total (Sum) |`Topic`, `Error`, `ErrorType`|PT1M |No|
|**Failed Received Events**<br><br>The number of events that were requested by clients but weren't delivered successfully by Event Grid. |`FailedReceivedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`, `Error`, `ErrorType`|PT1M |No|
|**Failed Released Events**<br><br>The number of events for which release failed. |`FailedReleasedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`, `Error`, `ErrorType`|PT1M |No|
|**MQTT: Connections**<br><br>The number of active connections in the namespace. |`Mqtt.Connections` |Count |Total (Sum) |`Protocol`|PT1M |Yes|
|**MQTT: Dropped Sessions**<br><br>The number of dropped sessions by the namespace. |`Mqtt.DroppedSessions` |Count |Total (Sum) |`DropReason`|PT1M |Yes|
|**MQTT: Failed Published Messages**<br><br>The number of MQTT messages that failed to be published into the namespace. |`Mqtt.FailedPublishedMessages` |Count |Total (Sum) |`QoS`, `Protocol`, `Error`|PT1M |Yes|
|**MQTT: Failed Routed Messages**<br><br>The number of failed routed messages by the namespace. |`Mqtt.FailedRoutedMessages` |Count |Total (Sum) |`Error`|PT1M |Yes|
|**MQTT: Failed Subscription Operations**<br><br>The number of failed subscription operations (Subscribe, Unsubscribe). This metric is incremented for every topic filter within a subscription request. |`Mqtt.FailedSubscriptionOperations` |Count |Total (Sum) |`Protocol`, `OperationType`, `Error`|PT1M |Yes|
|**MQTT: Request Count**<br><br>The number of MQTT requests. |`Mqtt.RequestCount` |Count |Total (Sum) |`OperationType`, `Protocol`, `Error`, `Result`|PT1M |Yes|
|**MQTT: Successful Delivered Messages**<br><br>The number of messages delivered by the namespace. There are no failures for this operation. |`Mqtt.SuccessfulDeliveredMessages` |Count |Total (Sum) |`QoS`, `Protocol`|PT1M |Yes|
|**MQTT: Successful Published Messages**<br><br>The number of MQTT messages that were published successfully into the namespace. |`Mqtt.SuccessfulPublishedMessages` |Count |Total (Sum) |`QoS`, `Protocol`|PT1M |Yes|
|**MQTT: Successful Routed Messages**<br><br>The number of successful routed messages by the namespace. |`Mqtt.SuccessfulRoutedMessages` |Count |Total (Sum) |\<none\>|PT1M |Yes|
|**MQTT: Successful Subscription Operations**<br><br>The number of successful subscription operations (Subscribe, Unsubscribe). This metric is incremented for every topic filter within a subscription request. |`Mqtt.SuccessfulSubscriptionOperations` |Count |Total (Sum) |`Protocol`, `OperationType`|PT1M |Yes|
|**MQTT: Throttling Enforcements**<br><br>The number of times Event Grid throttled a request because it exceeded the limit. |`Mqtt.ThrottlingEnforcements` |Count |Total (Sum) |`ThrottleType`|PT1M |Yes|
|**MQTT: Throughput**<br><br>The number of bytes published to or delivered by the namespace. |`Mqtt.Throughput` |Bytes |Total (Sum) |`Direction`|PT1M |Yes|
|**Publish Operations Latency**<br><br>The observed latency in milliseconds for publish events operation. |`PublishLatencyInMilliseconds` |MilliSeconds |Total (Sum) |`Topic`|PT1M |No|
|**Receive Operations Latency**<br><br>The observed latency in milliseconds for receive events operation. |`ReceiveLatencyInMilliseconds` |MilliSeconds |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|
|**Reject Operations Latency**<br><br>The observed latency in milliseconds for reject events operation. |`RejectLatencyInMilliseconds` |MilliSeconds |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|
|**Successful Acknowledged Events**<br><br>The number of events for which delivery was successfully acknowledged by clients. |`SuccessfulAcknowledgedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|
|**Successful Publish Events**<br><br>The number of events published successfully to a topic or topic space within a namespace. |`SuccessfulPublishedEvents` |Count |Total (Sum) |`Topic`|PT1M |No|
|**Successful Received Events**<br><br>The total number of events that were successfully returned to (received by) clients by Event Grid. |`SuccessfulReceivedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|
|**Successful Released Events**<br><br>The number of events that were released successfully by queue subscriber clients. |`SuccessfulReleasedEvents` |Count |Total (Sum) |`Topic`, `EventSubscriptionName`|PT1M |No|