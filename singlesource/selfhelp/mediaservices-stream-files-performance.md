---
title:   "Streaming files performance"
description: "Streaming files performance"
service: "microsoft.media"
resource:
authors: "juliako"
ms.author: inhenkel"juliako"
displayOrder: "1"
articleid: "mediaservices-stream-files-performance"
diagnosticScenario: ""
selfhelptype: "generic"
supporttopicids: "32632110"
resourcetags:
productpesids: "14885"
cloudenvironments: "public, fairfax, usnat, ussec"
ownershipid: "StorageMediaEdge_Media"
author: IngridAtMicrosoft
ms.service: media-services
---

# Streaming files performance

**Streaming Endpoint types**

There are two **Streaming Endpoint** types: **Standard** and **Premium**. The type is defined by the number of scale units (*scaleUnits*) you allocate for the streaming endpoint.

The table describes the types:

|Type|Scale units|Description|
|--------|--------|--------|
|**Standard Streaming Endpoint** (recommended)|0|The **Standard** type is the recommended option for virtually all streaming scenarios and audience sizes. The **Standard** type scales outbound bandwidth automatically. <brauthor: IngridAtMicrosoft
ms.service: media-services
---For customers with extremely demanding requirements Media Services offer **Premium** streaming endpoints, which can be used to scale out capacity for the largest internet audiences. If you expect large audiences and concurrent viewers, contact us at amsstreaming@microsoft.com for guidance on whether you need to move to the **Premium** type. |
|**Premium Streaming Endpoint**|>0|**Premium** streaming endpoints are suitable for advanced workloads, providing dedicated and scalable bandwidth capacity. You move to a **Premium** type by adjusting *scaleUnits*. *scaleUnits* provide you with dedicated egress capacity that can be purchased in increments of 200 Mbps. When using the **Premium** type, each enabled unit provides additional bandwidth capacity to the application. |

**Working with CDN**

In most cases, you should have CDN enabled. However, if you are anticipating max concurrency lower than 500 viewers then it is recommended to disable CDN since CDN scales best with concurrency.

Note that the Streaming Endpoint *hostname* and the streaming URL remains the same whether or not you enable CDN.

## **Recommended Documents**

* [Pricing](https://azure.microsoft.com/pricing/details/media-services/)<br>
* [Streaming Endpoints](https://docs.microsoft.com/azure/media-services/latest/streaming-endpoint-concept)
