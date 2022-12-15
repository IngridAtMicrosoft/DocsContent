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
var mediaAccount = armClient.GetMediaAccountResource(
    MediaAccountResource.CreateResourceIdentifier(
        subscriptionId: "00000000-0000-0000-0000-000000000000",
        resourceGroupName: "myResources",
        mediaAccountName: "myaccount"));

var mediaStream = (await mediaAccount.GetMediaStreams().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "mymovie",
    new MediaStreamData
    {
        Outputs =
        {
            {
                "output1",
                new MediaStreamOutput(enabled: true) { }
            },
            {
                "outputRelayToSocialMedia",
                new MediaStreamOutput(enabled: true)
                {
                    RelayUri = "rtmps://rtmp.socialmedia.example.com/ingest/abcabcabc"
                }
            },
            {
                "outputRelayToContentAnalyzer",
                new MediaStreamOutput(enabled: true)
                {
                    RelayUri = "rtmps://rtmp.contentanalyzer.example.com/ingest/abcabcabc"
                }
            }
        }
    })).Value;

Console.WriteLine(mediaStream.Data.Outputs["output1"].StreamingUri);
```
