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
Date:Mon, 07 Nov 2022 17:39:03 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/5eb254d0fc854705a00371f392aec04b",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "6VuHXVc_Wg-rIMhSSJpWytUqblJ6rVFPrla6sXZoI4d4pE-D2YN5bf5WW_aMEEJnpPX0p_tceaMmmuHV22qTpEfVFiPcJZGbIPx3Kaw_jOJH7GTJcIYVKRCDCT6V-GPIkBw02q8XNQZldVQp0bP-Jxu-wUFjJ8912AoLsn5EfIKn9kjAFtaHnGd-OjC6Fqn0XiFOsWEoxNYeqkLoWBjLvdCDUA5pyoAxTtW7TIFz5bMFDGrMzrrTZIjRkrfwqdAgM5s_435ykmwnrrg8oKK__aq-EqQNv04F0gIbd6Nx4-Jp7py7kOC5ts2d5K3IkeY4qMmohoKmDg94JoStUW2ObQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667842743,
    "updated": 1667842743,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
