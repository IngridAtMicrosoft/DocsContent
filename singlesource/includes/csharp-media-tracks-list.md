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
var mediaStream = armClient.GetMediaStreamResource(MediaStreamResource.CreateResourceIdentifier(
    subscriptionId: "00000000-0000-0000-0000-000000000000",
    resourceGroupName: "myResources",
    mediaAccountName: "myaccount",
    mediaStreamName: "mymovie"));

var mediaTracks = mediaStream.GetMediaTracks();

await foreach (var mediaTrack in mediaTracks)
{
    var textTrack = mediaTrack.Data.TextTrack;
    if (textTrack != null)
    {
        Console.WriteLine($"Text track: {textTrack.DisplayName}");
    }

    var audioTrack = mediaTrack.Data.AudioTrack;
    if (audioTrack != null)
    {
        Console.WriteLine($"Audio track: {audioTrack.DisplayName}");
    }

    var videoTrackBitRate = mediaTrack.Data.VideoTrackBitRate;
    if (videoTrackBitRate != null)
    {
        Console.WriteLine($"Video track: {videoTrackBitRate}");
    }
}
```
