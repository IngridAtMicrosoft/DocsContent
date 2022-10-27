---
title: Media Accounts
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 01/01/2023
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 01/01/2023
ms.service: media-services
---

# Media Accounts

[!INCLUDE [<prerelease-api>](../includes/prerelease-api.md)]

Media accounts provide a simple, scalable, and reliable way to manage media using Azure. Media accounts can be used to stream live events to audiences of any size.

![Media Services resources](../media/resources.png)

Media accounts provide are an alternative to exiting Media Services accounts. Media accounts make streaming media simple, but do not provide as much flexibility as Media Services accounts.

| Feature | Media Services | Media accounts |
|---|---|---|
| Account location | Any of 50+ Azure regions | Global |
| Data storage | Media data is stored in one or more Azure Storage accounts, managed by the account owner | Service managed storage |
| Streaming scale | Optional CDN integration, configured by the account owner | Service managed high-scale streaming |
| Content protection | Clear key and DRM protection, using user defined token authentication | Clear key protection using simple tokens |
| API | APIs for managing, streaming, protecting, and encoding media | Simple APIs for streaming live media |

Media accounts contain [media streams](media-streams.md) for streaming media content and [media protection options](media-protection-options.md) for protecting media content.

## Creating a media account

Media accounts can be created using the Azure Portal, ARM templates, client SDKs, or using HTTP requests. 

#### [C#](#tab/csharp/)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media account creation:

[!INCLUDE [<csharp-account-creation>](../includes/csharp-account-creation.md)]

#### [HTTP](#tab/http/)

[!INCLUDE [<http-account-creation.md](../includes/http-account-creation.md)]

---

## Media account options

### Data location

### Public network access

### Encryption

### Managed identity

### Tags

### System data

## Media account limits and billing

An Azure subscription may contain up to five media accounts. There is no charge for media accounts (but resources within the media account are billed).