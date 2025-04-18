---
title: How-to encrypt with DRM and use a license delivery service
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: azure-monitor
ms.date: 9/19/2022
---

<!--
<properties
	pageTitle="How-to encrypt with DRM and use a license delivery service"
	description="How-to encrypt with DRM and use a license delivery service"
	service="microsoft.media"
	resource="mediaservices"
	authors="juliako"
	ms.author="juliako"
	displayOrder="1"
	articleId="mediaservices-drm-and-key-delivery-howto"
	diagnosticScenario=""
	selfHelpType="generic"
	supportTopicIds="32632097"
	resourceTags=""
	productPesIds="14885"
	cloudEnvironments="public, fairfax, usnat, ussec"
	ownershipId="StorageMediaEdge_Media"
/>-->

# How-to encrypt with DRM and use a license delivery service

Before implementing DRM encryption, review [Content protection overview](/azure/media-services/latest/content-protection-overview). It is highly recommended to focus and fully test each part described in the [Main components of a content protection system](/azure/media-services/latest/content-protection-overview#main-components-of-a-content-protection-system) section before moving onto the next part. To test your "content protection" system, use the tools specified in the section.

## **Recommended Documents**

**Media Services v3 (latest)**

**NOTE**: Currently, you cannot use the Azure portal to manage v3 resources. Use the [REST API](https://aka.ms/ams-v3-rest-ref), [CLI](https://aka.ms/ams-v3-cli-ref), or one of the supported [SDKs](/azure/media-services/latest/developers-guide).

Concepts:

* [Design of a multi-DRM content protection system with access control](/azure/media-services/latest/design-multi-drm-system-with-access-control)<br>
* [Streaming Policies](/azure/media-services/latest/streaming-policy-concept)<br>
* [Content Key Policies](/azure/media-services/latest/content-key-policy-concept)<br>

Tutorials and how-tos:

* [Tutorial: Use AES-128 dynamic encryption and the key delivery service](/azure/media-services/latest/protect-with-aes128)<br>
* [Use DRM dynamic encryption and license delivery service](/azure/media-services/latest/protect-with-drm)<br>
* [Get a signing key from the existing policy](/azure/media-services/latest/get-content-key-policy-dotnet-howto)<br>
* [Offline FairPlay Streaming for iOS](/azure/media-services/latest/offline-fairplay-for-ios)

**Media Services v2 (legacy)**

* [Use PlayReady and/or Widevine dynamic common encryption](/azure/media-services/previous/media-services-protect-with-playready-widevine)