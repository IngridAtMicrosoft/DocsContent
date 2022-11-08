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
Date:Tue, 08 Nov 2022 19:49:38 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/6e815715d0c64a4f9aa48acf98b3ddde",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "zb-m4OsDEw5kPSfLE5Mp_y08E8THXHoMqXe50HxS11rojFbHPSgWxEQVo0MB7ISj2igkiNoS_Yj77SoXZ_X2NvnBkUQ3dIIdT0BzUF8SFLOf1QSV1IdcZe5MVLXrjMegmRqI9vo2nYt4Ph0MSnT77xzCJnFrkfVKkAfDJlQ-d5w2GrqZ19wsAHFwY8O6M0wgTPyBq_u4gSJKiu_xgOWkSFaHjfrZklOlx9Gb_f0Z4t-tzkYvWEie9L4t-banguGI_mHWCz4n7UT79CJlG99q9cfP3hRqIr1fNHz3RQsXlcmxM4wOrzGU49mcNFjo58_8RSPVclLp12NS0kFGg7fAuQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667936979,
    "updated": 1667936979,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
