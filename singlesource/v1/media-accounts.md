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

Media accounts provide a simple, scalable, and reliable way to manage media using Azure. Media accounts can be used to stream live events to audiances of any size.

![Media Services resources](../media/resources.png)

Media accounts provide are an alternative to exiting Media Services accounts. Media accounts make streaming media simple, but do not provide as much flexalbity as Media Services accounts.

| Feature | Media Services | Media accounts |
|:---|:---|:---|
| Account location | Any one of 50+ Azure regions | Global |
| Data storage | Media data is stored in one or more Azure Storage accounts, managed by the account owner | Service managed storage |
| Streaming scale | Optional CDN integration, configured by the account owner | Service managed high-scale streaming |
| Content protection | Clear key and DRM protection, using user defined token authentication | Clear key protection using simple tokens |
| API | APIs for managing, streaming, protecting, and encoding media | Simple APIs for streaming live media |

## Creating a Media Account

Media accounts are created using Azure Resource Manager. 

#### [C#](#tab/csharp/)

```csharp
var account = await resourceGroup.GetMediaAccounts().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "test1",
    new MediaAccountData(AzureLocation.WestUS)
    {
    });
```

NuGet package `Azure.ResourceManager.Media`, version 2.x.x or later is required to create media accounts.

#### [HTTP](#tab/http/)

```http
PUT https://{{armEndpoint}}/subscriptions/{{subscription}}/resourceGroups/{{resourceGroup}}?api-version=2016-09-01
Authorization: Bearer (token)
Content-Type: application/json; charset=utf-8

{"tags":{},"location":"westus","properties":{}} }
```

The `jq` utility is available in many cases, but not all. If the `jq` utility is missing, use `| python -m json.tool` instead.

---