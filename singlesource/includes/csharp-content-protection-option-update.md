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
await mediaProtectionOption.UpdateAsync(
    new MediaProtectionOptionData
    {
        TokenValidation = new TokenRestriction
        {
            TokenSigningCertificateIdentifier =
                "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate-2"
        }
    });
```
