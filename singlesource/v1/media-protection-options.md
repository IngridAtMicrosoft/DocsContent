---
title: Media Protection Options
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Protection Options

**TODO**

#### [C#](#tab/csharp)

Creating a certificate for token validation:

[!INCLUDE [<csharp-content-protection-create-certificate>](../includes/csharp-content-protection-create-certificate.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-create-certificate](../includes/http-content-protection-create-certificate.md)]

---

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Creating a media protection option:

[!INCLUDE [<csharp-content-protection-option-create>](../includes/csharp-content-protection-option-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-create](../includes/http-content-protection-option-create.md)]

---


---

#### [C#](#tab/csharp)

```csharp
var signingCertificate = GetSigningCertificate();

var token = new JsonWebTokenHandler().CreateToken(new SecurityTokenDescriptor
{
    Claims = new Dictionary<string, object>
    {
        {
            "urn:microsoft:azure:mediaservices:contentkeyidentifier",
            "c10a564b-c70d-4f77-9d48-1f7f870e90c9"
        }
    },
    Expires = DateTime.UtcNow.AddHours(4),
    Audience = "urn:microsoft:azure:mediaservices",
    SigningCredentials = new X509SigningCredentials(signingCertificate),
});
```

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-create](../includes/http-content-protection-option-create.md)]

---