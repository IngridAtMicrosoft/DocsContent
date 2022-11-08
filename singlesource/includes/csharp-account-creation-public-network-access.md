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
var mediaAccount = (await resourceGroup.GetMediaStreamAccounts().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "myaccount",
    new MediaStreamAccountData("global")
    {
        DataLocation = "United States",
        PublicNetworkAccess = PublicNetworkAccess.Disabled
    })).Value;
```
