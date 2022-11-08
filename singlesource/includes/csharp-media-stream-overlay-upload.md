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

await containerClient.GetBlobClient("logo.jpg")
    .UploadAsync(@"c:\media\logo.jpg", overwrite: true);

await containerClient.GetBlobClient("free-trial.jpg")
    .UploadAsync(@"c:\media\free-trial.jpg", overwrite: true);
```
