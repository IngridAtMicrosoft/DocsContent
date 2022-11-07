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
Date:Mon, 07 Nov 2022 17:07:55 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/2e6c87c210874cada797dad1e874f25b",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "2RPAlFcNIh8JbvbkUvy2CACJ_70x6toMcOhAt4yH8FYZSHTX0gJBjyzCCVfS-TnGc5Eo8LX79SCQMbXmlAeR0Frjgomfw0CYnxCzYVVTKkY9s0DvuyKG4U7JKj4NSJiOqGWi9rh1wwPgRB71zOe185PJuF35vf-BYLClz4MFnO3JU4wlJ9HpZBdUpn-CeS-5v5bIwciomsiGd_Ccrft4gnNDiGAKGFhzBj_pVk5vwlBpohGWD6fpJpO9UK7kflN_6QvvKf_8lkyxoiDD5OlsZ5jkYVEsytOEjCzcfHK-fM4SoNEz-wlZVPujq_MsR1kJugnrhS0tRQpKYhd23kfZ6Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667840876,
    "updated": 1667840876,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
