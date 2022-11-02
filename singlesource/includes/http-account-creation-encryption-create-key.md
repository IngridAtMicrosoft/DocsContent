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
Date:Tue, 01 Nov 2022 23:10:31 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/2fc42265fe7b43a0baf10dc03bf2f048",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "z2d3ocN_zHdqiUOgT_LnGxaKKgJrHSWO4fcv2JibhgkHVJMDYlujvHpWsv30jRgfj117JcUmauBdmTzG0qytXoT_cZnb3gwyCBRLZyH6lRAviH_O9bh4oP1i410ewoIfQpHqBxVyFWXAVFexinVVN6Gy4ZpKfJv2EVS0AowebkmxLu9YFNPQGzY-44r0cD-kobzbGtun3TwWCCHnMjRMcjjhVxZgLHOTfcUbx2qLiwHtDzrmXMlzPXEd0giGKNzjKMkONVWb10ZT_VLvn2PaqwzsPTSgr6Da-Pcwd4gsGDhLWlCtxz9oDy_pLsBeu2Ebxkv62aOlWBXlRbWTXQMr6Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667344231,
    "updated": 1667344231,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
