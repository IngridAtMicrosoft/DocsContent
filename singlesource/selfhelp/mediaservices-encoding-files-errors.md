---
title: Diagnose and resolve Encoding errors for Media Services v3
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
	pageTitle="Diagnose and resolve Encoding errors for Media Services v3/v2"
	description="Diagnose and resolve Encoding errors for Media Services v3/v2"
	service="microsoft.media"
	resource="mediaservices"
	authors="juliako"
	ms.author="juliako"
	displayOrder="1"
	articleId="mediaservices-encoding-files-errors"
	diagnosticScenario=""
	selfHelpType="generic"
	supportTopicIds="32632089"
	resourceTags=""
	productPesIds="14885"
	cloudEnvironments="public, fairfax, usnat, ussec"
	ownershipId="StorageMediaEdge_Media"
/>-->

# Diagnose and resolve Encoding errors for Media Services v3/v2

## **Recommended Documents**

**Media Services v3** (latest)

* [Encoding with Media Services v3](/azure/media-services/latest/encoding-concept)<br>

The following error codes could be returned in case an error was encountered during the encoding task:

* ApiErrorCode.BadRequest
* ApiErrorCode.NotFound
* ApiErrorCode.InvalidResource
* ApiErrorCode.QuotaExceeded
* ApiErrorCode.InternalServerError

The message property will have more details of the error that should be meaningful to the customer. For additional information, review [Feature gaps with respect to v2 APIs](/azure/media-services/latest/migrate-from-v2-to-v3).

**Media Services v2** (legacy)

* [Encoding error codes](/azure/media-services/previous/media-services-encoding-error-codes)
