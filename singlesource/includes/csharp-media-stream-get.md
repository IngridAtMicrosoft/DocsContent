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
mediaStream = await mediaStream.GetAsync();

Console.WriteLine(mediaStream.Data.StreamState); // prints "Live" when the media stream is receiving RTMP data
```
