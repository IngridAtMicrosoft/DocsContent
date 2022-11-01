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
var startRtmpIngestResponse = (await mediaStream.StartRtmpIngestAsync(
    new StartRtmpIngestContent
    {
        AutoStopDelay = TimeSpan.FromMinutes(5)
    })).Value;
    
Console.WriteLine(startRtmpIngestResponse.IngestUri);
```
