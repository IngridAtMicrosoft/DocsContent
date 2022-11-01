---
title: include file
description: include file
author: jonpayne
ms.topic: include
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

```csharp
var mediaAccount = armClient.GetMediaAccountResource(
    MediaAccountResource.CreateResourceIdentifier(
        subscriptionId: "00000000-0000-0000-0000-000000000000",
        resourceGroupName: "myResources",
        mediaAccountName: "myaccount"));
```
