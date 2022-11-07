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
Date:Mon, 07 Nov 2022 18:05:48 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/5b5d2829845141fd84bb4560e337b0da",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "5e7ixwOJiEMZP8563VBIlA7NV2V105d5ywqdcGKfH1RgwKZDQVnNsiUJNko4yvaeat_Psm4nc9uGWuVDckYkLvfBsgN3-gNBoCVAmXXuYEU09E_ddGf1M0UTLXc2E1cAv-qO9BGNGejvaRbOHmy_QGSKsdCt2cagBGaHNivVoxErBiDzKNYeuDtNuk2w0PnVKk7r-GrFz7TpWzdU40w88IkVuC5_s2NxSWqSacJQz3bTPj-ZIEJ9lN8E_TZl48rIF_M9wTJTmwmeSIODi0fCxM789LsG1EybBVXIbu_on9h7I4Sn2EFQgF4uSBrb0qqcw16OjLR2cZHbItr-ma_OKQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667844348,
    "updated": 1667844348,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
