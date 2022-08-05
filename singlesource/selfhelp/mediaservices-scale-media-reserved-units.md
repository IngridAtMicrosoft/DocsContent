---
	title: "Need to scale Media Reserved Units"
	description: "Need to scale Media Reserved Units"
	service="microsoft.media"
	resource="mediaservices"
	authors="juliako"
	ms.author: "juliako"
	displayOrder="1"
	articleid: "mediaservices-scale-media-reserved-units"
	diagnosticScenario=""
	selfhelptype: "generic"
	supporttopicids: "32632090"
	resourcetags: ""
	productpesids: "14885"
	cloudenvironments: "public, fairfax, usnat, ussec"
	ownershipid: "StorageMediaEdge_Media"
---

# Need to scale Media Reserved Units

Azure Media Services enables you to scale media processing in your account by managing Media Reserved Units (MRUs).

For the Audio Analysis and Video Analysis Jobs that are triggered by Media Services v3 or Video Indexer, it is highly recommended to provision your account with 10 S3 MRUs. You can open a support ticket to increase this quota. Make sure to include detailed information in the request on the desired quota changes, use-case scenarios, and regions required.

## **Recommended Documents**

* [Scale media processing with CLI](https://docs.microsoft.com/azure/media-services/latest/media-reserved-units-cli-how-to)
