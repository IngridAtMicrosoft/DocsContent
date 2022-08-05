---
	title: "Manage access policies quotas"
	description: "Manage access policies quotas"
	service="microsoft.media"
	resource="mediaservices"
	authors="juliako"
	ms.author: "juliako"
	displayOrder="1"
	articleid: "mediaservices-policies-quotas"
	diagnosticScenario=""
	selfhelptype: "generic"
	supporttopicids: "32632075"
	resourcetags: ""
	productpesids: "14885"
	cloudenvironments: "public, fairfax, usnat, ussec"
	ownershipid: "StorageMediaEdge_Media"
---

# Manage access policies quotas

You should try to design a limited set of policies in your Media Services account and reuse them when possible.

In Media Services v3, **Streaming Policies** have a default (soft) limit of 100. You should try to reuse them for your **Streaming Locators** whenever the same encryption options and protocols are needed.

In Media Services v2 (legacy), there is a default limit of 1,000,000 policies for different policies (for example, for Locator policy or ContentKeyAuthorizationPolicy). You should use the same policy ID if you are always using the same days/access permissions, for example, policies for locators that are intended to remain in place for a long time (non-upload policies).

## **Recommended Documents**

* [Azure Media Services v3 quotas and limitations](https://docs.microsoft.com/azure/media-services/latest/limits-quotas-constraints) <br>
 * [Media Services v2 (legacy) quotas and limitations](https://docs.microsoft.com/azure/media-services/previous/media-services-quotas-and-limitations)
