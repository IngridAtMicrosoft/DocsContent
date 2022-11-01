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
var mediaProtectionOptions = mediaAccount.GetMediaProtectionOptions().GetAllAsync();

await foreach (var m in mediaProtectionOptions)
{
    Console.WriteLine(m.Id);
}
```
