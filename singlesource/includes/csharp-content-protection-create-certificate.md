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
var keyVaultCertificates = new CertificateClient(
    new Uri("https://mykeys.vault.azure.net/"),
    new DefaultAzureCredential());

var certificateOperation = await keyVaultCertificates.StartCreateCertificateAsync(
    "content-protection-token-certificate",
    new CertificatePolicy(issuerName: "Self", subject: "CN=content-protection-token-certificate")
    {
        KeyType = CertificateKeyType.Ec,
        KeyCurveName = CertificateKeyCurveName.P256,
    });

var certificate = (await certificateOperation.WaitForCompletionAsync()).Value;

// Building the path from components rather than using certificate.Id allows us to
// use a certificate URL without a version.
var certificateUri = certificate.Properties.VaultUri + "certificates/" + certificate.Properties.Name;
```
