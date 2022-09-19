---
title: Issues encrypting with Widevine v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-drm-and-key-delivery-widevine-issues"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Issues encrypting with Widevine"
  ms.author="jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Issues encrypting with Widevine"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="020b987b-bb9e-b5a1-4284-e2ff977c3318" />=-->

# Issues encrypting with Widevine v2

## Resolve issues encrypting with Widevine

**Note**: This topic refers to Media Services v3 API documentation. v3 is the latest Media Services version.
Currently, you cannot use the Azure portal to manage v3 resources. Use the [REST API](https://docs.microsoft.com/rest/api/media/account-filters), [CLI](https://docs.microsoft.com/cli/azure/ams?view=azure-cli-latest), or one of the supported [SDKs](https://docs.microsoft.com/azure/media-services/latest/media-services-apis-overview).

Before implementing DRM encryption, review [Content protection overview](https://docs.microsoft.com/azure/media-services/latest/drm-content-protection-concept). It is recommended you test each part in the [Main components of a content protection system](https://docs.microsoft.com/azure/media-services/latest/drm-content-protection-concept#main-components-of-a-content-protection-system).

To get details on failing Key delivery service request, enable the Azure monitoring diagnostic logs. See [Monitor Media Services metrics and diagnostic logs](https://docs.microsoft.com/azure/media-services/latest/monitoring/media-services-diagnostic-logs-howto).

To specify the Widevine encryption Streaming Policy, use the "Predefined_MultiDrmCencStreaming" policy. The "Predefined_MultiDrmCencStreaming" policy supports envelope and cenc encryption and sets two content keys on the Streaming Locator. For an example of how to configure a Widevine Content Key Policy option, see [Create Content Key Policies](https://github.com/Azure-Samples/media-services-v3-dotnet-tutorials/blob/master/AMSV3Tutorials/EncryptWithDRM/Program.cs#L180)

### Resources

**Concepts**

* [Design of a multi-DRM content protection system with access control](https://docs.microsoft.com/azure/media-services/previous/media-services-cenc-with-multidrm-access-control)<br>
* [Streaming Policies](https://docs.microsoft.com/azure/media-services/latest/stream-streaming-policy-concept)<br>
* [Content Key Policies](https://docs.microsoft.com/azure/media-services/latest/drm-content-key-policy-concept)<br>
* [Widevine license template](https://docs.microsoft.com/azure/media-services/previous/media-services-widevine-license-template-overview)<br>


**Tutorials and how-tos**

* [Tutorial: Use AES-128 dynamic encryption and the key delivery service](https://docs.microsoft.com/azure/media-services/latest/drm-protect-with-aes128-tutorial)<br>
* [Use DRM dynamic encryption and license delivery service](https://docs.microsoft.com/azure/media-services/latest/drm-protect-with-drm-tutorial)<br>
* [Get a signing key from the existing policy](https://docs.microsoft.com/azure/media-services/latest/drm-get-content-key-policy-how-to?tabs=net)<br>
* [Offline Widevine streaming for Android](https://docs.microsoft.com/azure/media-services/latest/drm-offline-widevine-for-android?tabs=net)

### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
