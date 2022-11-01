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
Date:Tue, 01 Nov 2022 15:43:35 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/c5af6b077b704b24bd943c024916d4a0",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "vPpGvVSSVuaYoicl-xeTGo7EJiJsbv97xZfnZ9IHj2A0rfbwAcBJJDaqwfyaIZjvviAvs_sY4H5ozIs6UQGB50tUIHtQYioxJvxagvePNZ80w_FkphESnpPoFDgFJWXX9JdAG31AhxxJZcERJV_aDdAe6JrAbwlaCkrayMLyItYljHbURby_iAqdtMrJfYZiLuA_R5wSty4WFtv3mdQR3-RYYnM0Tq_BdBlZzV2qWG_50c_sU11o_RMLC-Y2_MAwX-C3FtlEJIQpPKW9LybK49K6kRFpvZgixxaao03C0WfPpUqkCIGdp0tfpnmeB6uVlT2si9Ppx8-GdfHZshjppQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667317415,
    "updated": 1667317415,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
