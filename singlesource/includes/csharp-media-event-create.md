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

var mediaEvent = (await mediaAccount.GetMediaEvents().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "myevent",
    new MediaEventData
    {
        Rtmps = new RtmpsOptions(enabled: true)
    })).Value;

Console.WriteLine(mediaEvent.Data.Rtmps.IngestUri);
```
