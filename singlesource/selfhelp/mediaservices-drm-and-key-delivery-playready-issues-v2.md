---
title: Issues encrypting with PlayReady v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
	pageTitle="Issues encrypting with PlayReady"
	description="Apollo migrated file - Issues encrypting with PlayReady"
	ms.author="juliako"
	articleId="apollo-mediaservices-drm-and-key-delivery-playready-issues"
	selfHelpType="apollo"
	productPesIds="14885"
	cloudEnvironments="public, fairfax, usnat, ussec"
	ownershipId="StorageMediaEdge_Media"
    supportTopicIds="b5aa7c16-f1c1-3092-0bb3-feaf27e6e4ee"
    resourcerequired="false"
/>
-->

# Issues encrypting with PlayReady v2

## Fix this problem now using our expert solution
Expert solutions are written by Azure engineers to help you quickly resolve the problem on your own.
<br><br><br>


**Media Services v3 (latest)**

**NOTE**: Currently, you cannot use the Azure portal to manage v3 resources. Use the [REST API](https://aka.ms/ams-v3-rest-ref), [CLI](https://aka.ms/ams-v3-cli-ref), or one of the supported [SDKs](/azure/media-services/latest/developers-guide).

Before implementing DRM encryption, review [Content protection overview](/azure/media-services/latest/content-protection-overview). It is highly recommended to focus and fully test each part described in the [Main components of a content protection system](/azure/media-services/latest/content-protection-overview#main-components-of-a-content-protection-system) section before moving onto the next part. To test your "content protection" system, use the tools specified in the section.

To get details on all failing Key delivery service request, enable the Azure monitoring diagnostic logs. For more information, see [Monitor Media Services metrics and diagnostic logs](/azure/media-services/latest/media-services-metrics-diagnostic-logs).

To specify the PlayReady encryption Streaming Policy, use the "Predefined_MultiDrmCencStreaming". The "Predefined_MultiDrmCencStreaming" policy supports envelope and cenc encryption and sets two content keys on the Streaming Locator. For an example of how to configure a PlayReady Content Key Policy option, see [Create Content Key Policies](https://github.com/Azure-Samples/media-services-v3-dotnet-tutorials/blob/master/AMSV3Tutorials/EncryptWithDRM/Program.cs#L180)

**Concepts**

* [Content protection overview](/azure/media-services/latest/content-protection-overview)<br>
* [Design of a multi-DRM content protection system with access control](/azure/media-services/latest/design-multi-drm-system-with-access-control)<br>
* [Streaming Policies](/azure/media-services/latest/streaming-policy-concept)<br>
* [Content Key Policies](/azure/media-services/latest/content-key-policy-concept)<br>
* [Media Services PlayReady license template](/azure/media-services/latest/playready-license-template-overview)<br>
* [FAQs](/azure/media-services/latest/design-multi-drm-system-with-access-control#faqs)<br>

**Tutorials and how-tos**

* [Tutorial: Use AES-128 dynamic encryption and the key delivery service](/azure/media-services/latest/protect-with-aes128)<br>
* [Use DRM dynamic encryption and license delivery service](/azure/media-services/latest/protect-with-drm)<br>
* [Get a signing key from the existing policy](/azure/media-services/latest/get-content-key-policy-dotnet-howto)<br>
* [Offline PlayReady Streaming for Windows 10](/azure/media-services/latest/offline-plaready-streaming-for-windows-10)

**Media Services v2 (legacy)**

[Use PlayReady and/or Widevine dynamic common encryption](/azure/media-services/previous/media-services-protect-with-playready-widevine)

### Recommended resources

* [Content protection overview](/azure/media-services/latest/content-protection-overview).

### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>