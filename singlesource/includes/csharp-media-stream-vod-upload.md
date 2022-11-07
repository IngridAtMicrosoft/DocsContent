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
var containerClient = new BlobContainerClient(startRtmpIngestResponse.IngestUri);

var blobClient = containerClient.GetBlobClient("video.mp4");
await blobClient.UploadAsync(@"c:\media\video.mp4", overwrite: true);
```
