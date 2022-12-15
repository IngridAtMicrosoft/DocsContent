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
Date:Thu, 15 Dec 2022 23:12:21 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/6e162de7a9854d5e943634a7a5e077a3",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "vdSRbtPogxg--uRdEvj74yApO07aSqxpm1WuVbytBw9qFFLfRndbAmdjnwwZrxQVpWGFXCPh5yzZdbmnPm7dGdeklW9ohXh1B0q2Kydd-be1w76TpMHBclL8VxBY5dH89qUv4TZBanIqTW8YStBQdbSrwEsiBRdgD7-yXiGWEjHEwpLw78XI_v1JTJVErcqBEM3sDoW9BKMGn2KtVBFzQYgrUG8NHqjmO7uihquoWPklpXefHrMJLHJN4VJSfovbKk8axSi0-txJNGidxIba4eGLBeWGEakc_PeovdR1EDy-dofnFLRCHOnTMT9gqMUhyS5BqwGIsF4PhhT8rMeNNQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1671145941,
    "updated": 1671145941,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
