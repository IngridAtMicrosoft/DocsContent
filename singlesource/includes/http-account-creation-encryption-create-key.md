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
POST https://mykeys.vault.azure.net/keys/account-encryption-key/create?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "kty": "RSA",
  "key_size": 2048
}

200 OK
Date:Thu, 27 Oct 2022 23:50:43 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/27a6851038c040aca7c014cbb6ce3fa6",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "wsRkqWawsgXhrdkW7rFzKWeD1aN9JvrTi99yuIYNpVwsLYMkEdeZ4yzRjmgsC8gXBBsUy-loH87zqnf2-Njs-5BSldOmJ3BxrWwWv4avrmAkA4JC6kXREA-2TPGPddV_epnxCruMRQ7fu04KUxek3BQ6XCPfyq-M_vqbyqLys6ohQxrCFsN9n9YRvMjwy8AGCi0DlEas1rW7WZNaFCkA74EqH8iIXa3sgJ0nvVnjexCw8Wj0kzQY0sCMTcJ6VIgHBUSaWIjPJbhBhJI0pAVAH8EgR2fRIDFBSG6FI4qd8QoBcDgxFt_pfbwaTskOvPYI4clDJe4bOdJq_schSAwbCQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1666914644,
    "updated": 1666914644,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
