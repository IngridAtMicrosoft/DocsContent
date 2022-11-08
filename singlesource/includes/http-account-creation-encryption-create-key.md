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
Date:Tue, 08 Nov 2022 18:31:36 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/7dda34e1037746d384ddc89be1a9e64d",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "vmURnaxULXTIGIizqetFUS2i7787OLzhkHmKHFMbZyCOh2hDPkpzhteEw3aTZDlgfxyb52WmKlPwbVWq_5sD-XMzc92CKYSt-cbfRG9y-rvE32n3JZ_OofnQjG2NnxIZVtk61xHjNoCQi6ceheEEbuwNRymRXMUcki1raix6YJtexVafAPi_5O9f70w9HHjCZazDnBpCbK15wWVrpZNqfkPBeK6LtClQgtN0fTv-ML4oysuk8cI6C48rtOAZV1DaSRPWJGLZqre4mE9sbm6d6hb_yt5y5cyPEgT6wm5nZ3X8uasrO0JakipS6r77kHk57CeCIERtMOTBCWQt-vDM3Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667932297,
    "updated": 1667932297,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
