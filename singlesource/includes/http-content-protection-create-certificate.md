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

```http
POST https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/create?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

202 Accepted
Date:Fri, 28 Oct 2022 17:30:47 GMT
Content-Type:application/json; charset=utf-8

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 28 Oct 2022 17:30:47 GMT
Content-Type:application/json; charset=utf-8

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 28 Oct 2022 17:30:57 GMT
Content-Type:application/json; charset=utf-8

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 28 Oct 2022 17:31:07 GMT
Content-Type:application/json; charset=utf-8

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 28 Oct 2022 17:31:07 GMT
Content-Type:application/json; charset=utf-8

```
