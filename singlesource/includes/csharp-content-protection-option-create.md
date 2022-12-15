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
var managedIdentity = new ResourceIdentifier(
    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources" +
    "/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity");

var mediaProtection = (await mediaAccount.GetMediaProtections().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "protection-option-1",
    new MediaProtectionData
    {
        TokenValidation = new TokenRestriction
        {
            TokenSigningCertificateIdentifier = certificateUri,
            Identity = new ResourceIdentity(useSystemAssignedIdentity: false)
            {
                UserAssignedIdentity = managedIdentity
            }
        },
        ClearKeyEnabled = true
    })).Value;
```
