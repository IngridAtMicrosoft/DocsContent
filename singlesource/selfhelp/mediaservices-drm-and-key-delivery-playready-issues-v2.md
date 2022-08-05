---
title:   "Issues encrypting with PlayReady"
description: "Apollo migrated file - Issues encrypting with PlayReady"
ms.author: inhenkel"juliako"
articleid: "apollo-mediaservices-drm-and-key-delivery-playready-issues"
selfhelptype: "apollo"
productpesids: "14885"
cloudenvironments: "public, fairfax, usnat, ussec"
ownershipid: "StorageMediaEdge_Media"
supporttopicids: "b5aa7c16-f1c1-3092-0bb3-feaf27e6e4ee"
resourcerequired: "false"
author: IngridAtMicrosoft
ms.service: media-services
---

# Issues encrypting with PlayReady

## Fix this problem now using our expert solution
Expert solutions are written by Azure engineers to help you quickly resolve the problem on your own.
<br><br><br>


**Media Services v3 (latest)**

**NOTE**: Currently, you cannot use the Azure portal to manage v3 resources. Use the [REST API](https://aka.ms/ams-v3-rest-ref), [CLI](https://aka.ms/ams-v3-cli-ref), or one of the supported [SDKs](https://docs.microsoft.com/azure/media-services/latest/developers-guide).

Before implementing DRM encryption, review [Content protection overview](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview). It is highly recommended to focus and fully test each part described in the [Main components of a content protection system](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview#main-components-of-a-content-protection-system) section before moving onto the next part. To test your "content protection" system, use the tools specified in the section.

To get details on all failing Key delivery service request, enable the Azure monitoring diagnostic logs. For more information, see [Monitor Media Services metrics and diagnostic logs](https://docs.microsoft.com/azure/media-services/latest/media-services-metrics-diagnostic-logs).

To specify the PlayReady encryption Streaming Policy, use the "Predefined_MultiDrmCencStreaming". The "Predefined_MultiDrmCencStreaming" policy supports envelope and cenc encryption and sets two content keys on the Streaming Locator. For an example of how to configure a PlayReady Content Key Policy option, see [Create Content Key Policies](https://github.com/Azure-Samples/media-services-v3-dotnet-tutorials/blob/master/AMSV3Tutorials/EncryptWithDRM/Program.cs#L180)

**Concepts**

* [Content protection overview](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview)<br>
* [Design of a multi-DRM content protection system with access control](https://docs.microsoft.com/azure/media-services/latest/design-multi-drm-system-with-access-control)<br>
* [Streaming Policies](https://docs.microsoft.com/azure/media-services/latest/streaming-policy-concept)<br>
* [Content Key Policies](https://docs.microsoft.com/azure/media-services/latest/content-key-policy-concept)<br>
* [Media Services PlayReady license template](https://docs.microsoft.com/azure/media-services/latest/playready-license-template-overview)<br>
* [FAQs](https://docs.microsoft.com/azure/media-services/latest/design-multi-drm-system-with-access-control#faqs)<br>

**Tutorials and how-tos**

* [Tutorial: Use AES-128 dynamic encryption and the key delivery service](https://docs.microsoft.com/azure/media-services/latest/protect-with-aes128)<br>
* [Use DRM dynamic encryption and license delivery service](https://docs.microsoft.com/azure/media-services/latest/protect-with-drm)<br>
* [Get a signing key from the existing policy](https://docs.microsoft.com/azure/media-services/latest/get-content-key-policy-dotnet-howto)<br>
* [Offline PlayReady Streaming for Windows 10](https://docs.microsoft.com/azure/media-services/latest/offline-plaready-streaming-for-windows-10)

**Media Services v2 (legacy)**

[Use PlayReady and/or Widevine dynamic common encryption](https://docs.microsoft.com/azure/media-services/previous/media-services-protect-with-playready-widevine)

### Recommended resources

* [Content protection overview](https://docs.microsoft.com/azure/media-services/latest/content-protection-overview).

### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>