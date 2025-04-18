---
title: Client Latency v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: azure-monitor
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-client-latency"
  cloudenvironments="public,mooncake,fairfax,usnat,ussec"
  description="Apollo migrated file - Client Latency"
  ms.author="akucer,jiayali,inhenkel"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Client Latency"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="4706e3b6-8e87-89a7-42cc-174d25a5a531,bb39ff08-5d16-e549-af8e-3b30554e31cc" />
-->


# Client Latency v2

## Resolve client latency issues in Azure Media Services

Use the following guidance to resolve client latency issues.

### Common issues and solutions

* Make sure you're using Azure Media Services in an Azure region that is geographically closest to the majority of your customers.
* Enable [Azure Content Delivery Network (CDN)](https://azure.microsoft.com/pricing/details/cdn/) for your streaming endpoint if many clients will be simultaneously accessing content. Azure CDN can be enabled directly using either media services APIs or the Azure portal.
* For livestreaming, use a [recommended on-premises encoder](/azure/media-services/previous/media-services-recommended-encoders).
* Preload the media player on your webpage.

### Resources
* [Live streaming best practices guide](/azure/media-services/latest/live-event-streaming-best-practices-guide)
* [Live event low latency settings](/azure/media-services/latest/live-event-latency-reference)

<!--
### Rome relevant results from the web

<azureKB>
	<client>portal</client>
</azureKB>
-->