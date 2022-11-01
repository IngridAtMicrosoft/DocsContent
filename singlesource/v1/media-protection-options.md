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

Access to media streams can be restricted by setting a media protection option for a media stream output.
Each media stream output with media protection enabled is encrypted with a different content keys. Viewers
can access the content key required to view an output by presenting a valid token to the content key server.

Tokens used to request content keys are encrypted with a token signing key, stored in Azure Key Vault. The token
signing key is accessed a Managed Identity of the media account.

## Creating a token validation certificate

Each media protection option requires a token signing certificate, stored in an Azure Key Vault.

Creating a certificate for token validation:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-create-certificate>](../includes/csharp-content-protection-create-certificate.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-create-certificate](../includes/http-content-protection-create-certificate.md)]

---

## Creating a media protection option

To create a token protection option, specify the enabled content protection methods (currently only clear key is supported),
the token protection certificate, and the managed identity that should be used to access the token protection certificate.

The managed identity must be associated with the media account and must be granted the `Sign` permission for the Key Vault
certificate.

The token signing certificate may either be specified as a Key Vault certificate URI with a version identifier or a URI without
version information. When version information is not provided, Media Services will accept tokens signed with any matching, valid,
and enabled certificate.
