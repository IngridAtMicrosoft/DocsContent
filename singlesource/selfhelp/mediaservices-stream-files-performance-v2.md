---
articleid: "apollo-mediaservices-stream-files-performance"
cloudenvironments: "public,fairfax,usnat,ussec,mooncake,blackforest"
description: "Use our guidance to learn about streaming endpoint types, and working with Azure Content Delivery Network (CDN)."
ms.author: inhenkel"juliako,jiayali,inhenkel"
ownershipid: "StorageMediaEdge_Media"
title:  "Learn about streaming files performance"
problemids: ""
productpesids: "14885"
resourcerequired: "False"
resourcetags:
selfhelptype: "apollo"
supporttopicids: "8fbb1ca9-ab3b-598c-4dae-a1dd9bd13cde" author: IngridAtMicrosoft
ms.service: media-services
---
# Streaming files performance

## Learn about streaming files performance

Use our guidance to learn about Streaming Endpoint types, and working with Azure Content Delivery Network (CDN).

### Streaming endpoint types

The two types of Streaming Endpoints, Standard and Premium, are defined by the number of scale units (scaleUnits) you allocate.

|Type|Scale units|Description|
|--------|--------|--------|
|Standard Streaming Endpoint (recommended)|0|Recommended for virtually all streaming scenarios and audience sizes. It scales outbound bandwidth automatically. For customers with demanding requirements, Media Services offer Premium Streaming Endpoint to scale out capacity for the largest internet audiences. For large audiences and concurrent viewers, contact us at amsstreaming@microsoft.com for guidance on which type to use. |
|Premium Streaming Endpoint|>0|These endpoints are suitable for advanced workloads, providing dedicated and scalable bandwidth capacity. Move to Premium by adjusting scaleUnits, which have dedicated egress capacity that can be purchased in increments of 200 Mbps. Each enabled unit provides additional bandwidth capacity to the application. |

### Working with CDN

For most cases, enable CDN. However, with maximium concurrency lower than 500 viewers, disable CDN. It scales best with concurrency. The Streaming Endpoint hostname and the streaming URL remains the same whether or not you enable CDN.

Learn more: [Azure CDN Overview](https://docs.microsoft.com/azure/cdn/cdn-overview)

### Resources

* [Media Services pricing](https://azure.microsoft.com/pricing/details/media-services/)
* [Streaming Endpoints (Origin) in Azure Media Services](https://docs.microsoft.com/azure/media-services/latest/stream-streaming-endpoint-concept)

### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
