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
var mediaStream = (await mediaAccount.GetMediaStreams().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "mymovie",
    new MediaStreamData
    {
        Outputs =
        {
            {
                "output1",
                new MediaStreamOutput(enabled: true)
                {
                    MediaProtectionOptionId = mediaProtectionOption.Id
                }
            }
        }
    })).Value;

Console.WriteLine(mediaStream.Data.Outputs["output1"].StreamingUri);
```
