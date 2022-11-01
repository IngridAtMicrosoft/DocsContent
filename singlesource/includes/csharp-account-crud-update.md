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
await mediaAccount.UpdateAsync(
    new MediaAccountData("global")
    {
        PublicNetworkAccess = PublicNetworkAccess.Disabled,
    });
```
