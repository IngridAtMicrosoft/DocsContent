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
var mediaAccount = (await resourceGroup.GetMediaAccounts().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "myaccount",
    new MediaAccountData("global")
    {
        DataLocation = AzureLocation.WestUS
    })).Value;
```
