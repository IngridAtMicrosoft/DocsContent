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
var keysClient = new KeyClient(
    new Uri("https://mykeys.vault.azure.net/"),
    new DefaultAzureCredential(),
    new KeyClientOptions { Diagnostics = { IsLoggingContentEnabled = true } });

KeyVaultKey key = await keysClient.CreateRsaKeyAsync(
    new CreateRsaKeyOptions("account-encryption-key")
    {
        KeySize = 2048
    });

// Building the path from components rather than using key.Id allows us to
// use a key URL without a version.
var keyUri = key.Properties.VaultUri + "keys/" + key.Properties.Name;
```
