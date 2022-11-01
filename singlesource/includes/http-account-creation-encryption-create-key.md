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
Date:Tue, 01 Nov 2022 16:35:57 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/93a39fe761db486a88231572bb50fbc2",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "47IWsqZsMuksDNLyarQ6tR33fJ6IB6ztgULNlo6rXf35YM5gVNGXGz44M1LuN8tgXrZGej1YVl_eRBltuLvfLQ01twFVBjS8Z766Y0Nry1oZJtd6Oaj-E7VaUN71HuonAm8ig11q8tsOzYVyky5aiJb-w0PE1z9X-YXIZMFlRuLExl0jakSp3UrZhxX-wYKMeuIUlKO3H0o4pVYylFtP8QKBjss1fJ7c71b7qxC5mAtNifrSWYadxLhRy314nCiuk9ut74blZrr0VbPodsQlyHWs3zAOdbfuzZrOUb35whwTGfsewayv3dW0200e1NP-E078SYCOa51Ljoxovg-37Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667320557,
    "updated": 1667320557,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
