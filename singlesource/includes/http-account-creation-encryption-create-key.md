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
Date:Wed, 09 Nov 2022 17:29:51 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/d5f1c5ba55d7462cb211add041d4a992",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "57AxNNgMZ9U3NHw0xddssun3_n-X9IgUVEKMHTGINyzWDnoCwtlyvW6ImMfiE-DhMnyx3kNLPDp-LPmKfILwkx8DsSOMmxvP5sjxgUCi1l0VdbOBMQcD9G2AvXAzrBwVQUdQMmi1XeN1kE7wfzsm3m0o78YwXR-PDtTcfYsgbdKV2keWNpCzSXDdP7T6WVDqwGpYnlpjtA2_8dI0aEReStbRA9LGJlFVWnu19I_oVbSKoZ6INrn3pdtc_6O62nbK9c0ZEzEt3grtejpG4yHIELlGoD6rOxFSMzDVx8trdw4qgvwywtIjG-aA0onTDFzfIhvKN2jKB-VqEim0WYeFWQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1668014991,
    "updated": 1668014991,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
