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
Date:Tue, 08 Nov 2022 19:15:45 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/3296d1d3c03a43f9a204962e6d3c2d85",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "10qVrvxKq5WVWFKJ0fNf45whPK39fJQYuzpVECDK8s6h0yI8tf3tfRQ5S5hqQyCo8OP1gP2p1D4fTSyMPj2Rl0HxVamsFcj8cVwe7GgmybcmC1n3IoZzDHlp4rKuh5YlLq_cwd5MsMDFwkK6HtTyI1rIjeVGqXAwMMTFnjay6og-OkDA-RijDkTm9scJZgdvjg0DlIhXIwoc4HD06n0Fv7f9qNw0xCqPai0LjLcjnDrxOtocfRtDAUcWuFzKeFsd-5oPHAjZyGrezG_9zxQQd9DoCIdozwx-oP2dM9JyB46eRxz4Qlf5ZemzeaO4dLhmePWNNs-mNxhOc-kge_zJ9Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667934945,
    "updated": 1667934945,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
