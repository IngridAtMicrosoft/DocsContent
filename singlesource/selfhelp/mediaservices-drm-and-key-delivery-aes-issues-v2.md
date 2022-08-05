---
title:   "Issues encrypting with AES-128 clear key"
description: "Apollo migrated file - Issues encrypting with AES-128 clear key"
ms.author: inhenkel"juliako"
articleid: "apollo-mediaservices-drm-and-key-delivery-aes-issues"
selfhelptype: "apollo"
productpesids: "14885"
cloudenvironments: "public, fairfax, usnat, ussec"
ownershipid: "StorageMediaEdge_Media"
supporttopicids: "c5ede9ef-49ba-821d-6805-804357b50aa0"
resourcerequired: "false"
author: IngridAtMicrosoft
ms.service: media-services
---

# Issues encrypting with AES-128 clear key

## Fix this problem now using our expert solution
Expert solutions are written by Azure engineers to help you quickly resolve the problem on your own.
<br><br><br>


**Does offline playback work with AES-128 clear key encryption?**

 No. Offline download/playback of files encrypted with AES-128 is not supported by Media Services.

**Media Services v3 (latest)**

**NOTE**: Currently, you cannot use the Azure portal to manage v3 resources. Use the [REST API](https://aka.ms/ams-v3-rest-ref), [CLI](https://aka.ms/ams-v3-cli-ref), or one of the supported [SDKs](https://docs.microsoft.com/azure/media-services/latest/developers-guide).

To get details on all failing Key delivery service request, enable the Azure monitoring diagnostic logs. For more information, see [Monitor Media Services metrics and diagnostic logs](https://docs.microsoft.com/azure/media-services/latest/media-services-metrics-diagnostic-logs).

* [Concept: Content protection overview](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview)<br>
* [FAQs](https://docs.microsoft.com/azure/media-services/latest/frequently-asked-questions#content-protection)<br>
* [Tutorial: Use AES-128 dynamic encryption and the key delivery service](https://docs.microsoft.com/azure/media-services/latest/protect-with-aes128)

**Media Services v2 (legacy)**

* [Use AES-128 dynamic encryption and the key delivery service](https://docs.microsoft.com/azure/media-services/previous/media-services-protect-with-aes128)

### Recommended resources

[Concept: Content protection overview](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview)


### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>