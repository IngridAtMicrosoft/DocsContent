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
var mediaStream = (await mediaStreamAccount.GetMediaStreams().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "mymovie",
    new MediaStreamData
    {
        Outputs =
        {
            {
                "outputWithLogoOverlay",
                new MediaStreamOutput(enabled: true)
                {
                    StreamOverlay = new Overlay
                    {
                        Image = "logo.jpg",
                        Position = new Rectangle(left: 50, top: 50, width: 200, height: 90)
                    },
                    MediaProtectionId = mediaProtection.Id
                }
            },
            {
                "outputWithPreviewTextOverlay",
                new MediaStreamOutput(enabled: true)
                {
                    StreamOverlay = new Overlay
                    {
                        Image = "freetrial.jpg",
                        Position = new Rectangle(left: 0, top: 0, width: 1920, height: 1080)
                    }
                }
            }
        }
    })).Value;

Console.WriteLine(mediaStream.Data.Outputs["outputWithLogoOverlay"].StreamingUri);
Console.WriteLine(mediaStream.Data.Outputs["outputWithPreviewTextOverlay"].StreamingUri);
```
