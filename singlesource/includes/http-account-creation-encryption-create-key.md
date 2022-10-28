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
Date:Fri, 28 Oct 2022 17:25:37 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/073dc9fdc8ce43908894c7ac2813fe93",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "xjVp18eQza_Yi10g16bVQoXaNUoEq_oNHVwIZoiVH8cOtHXyJCaAJ-yq9vIX_Y6lEmBUYGF38Phgp_DNlsG7479gXcUkU4V6f2QQ5Y6RdDv7n7KCruYWWMWp6L5BSefM4vf8fz6ngcizPhLPd-EZ2Bu0atXCkoNHoGwssy7dmaoHsmp-FZbcEwdCOuDnji-OsfDSMpM5lDungw6ffrDdoo8ex51MUBFn2uxBT2-edXPuBmEsCFw7BMH89S-VISsKk00DQEOvWcoaGF39x9W8fRMS1-d8ZeS6aIeqq3N2oVMLGnFj8TkAZjwMHwAWoz00ISKYy-N876LhePIeI3eYfQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1666977938,
    "updated": 1666977938,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
