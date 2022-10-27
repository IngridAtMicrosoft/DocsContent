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
Date:Thu, 27 Oct 2022 22:39:15 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/8575932d04dd4b5d850571d58ac8230c",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "t7B9W4s5gwzZhv92i6MtQjY-NbBknuB1AKxH0m13p1H5Fh-36-WjXSHrLKyU2p2SXpcsyDsPWpGI8xlj-vTCSFvwPinWdZAItZumsmsLUp4KSo01WM5zoSJzrjc9WwoAW4qamG_xu5zbkt2xhLfcpclGToZM7KBo2v8OXiUfhYmyDYsujynGDEl8-IwCLLxCDXklj32hieJt6SFa7CpxVJPEw9JGq50yC1g8OO8dMBfOQ0DbU5t8PfZ1gv_HjWTLgrH0s2CBStBzO1P7znnQHEBjaDbA2-g1_GK9JqXacg0ZP14SKItG8Bj4x0KPSSd8T7dmly5EB7vqSyX3Q_1GtQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1666910356,
    "updated": 1666910356,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
