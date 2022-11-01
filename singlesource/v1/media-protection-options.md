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

