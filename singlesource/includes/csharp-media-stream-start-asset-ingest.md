---
title: include file
description: include file
author: jonpayne
ms.topic: include
ms.date: 01/01/2023
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 01/01/2023
ms.service: media-services
---

```csharp
var startRtmpIngestResponse = (await mediaStream.IngestAssetAsync(
    new IngestAssetContent
    {
        AssetId = "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaservices/mymedia/assets/asset1"
    })).Value;
```
