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
Date:Thu, 05 Jan 2023 17:02:14 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/ed0e58f39e6645c3b10c0e85d0ac2b4f",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "seWMeF4SFmN2RA4mZDv8yxtMfhmdKc3iwegm_YehkrjZQ7mHQ50QGyVaVDMqThPdMWETxeJgq0ubTj8-Tz2esmMbWjHGsuKk3Qu9sbjnKPu4OnViACEbVPX6rlJi2AWtkMgNUZdVMR0FpCCTPsqhLYIKvoUqneIaYcAKIilAAh1Vlmq0NTYy8R80_CNVzx63W9pqiT4L0rkul7-52CY0U51z761Z32DRR6-FMqVJPQh4bQd2T_f2bS7xZO-FLIGcADoNF1_Di_lkWrUH_KzLBjXKvmzU37ma3RjzNwW8aLLHiLsAu94GVJoaReYazIYdumDFvpdG5eYSXtdUUe_uPQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1672938134,
    "updated": 1672938134,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
