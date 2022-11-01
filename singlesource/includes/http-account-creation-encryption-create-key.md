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
Date:Tue, 01 Nov 2022 21:55:22 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/9612150fc04f4cbb945f286d7835bfba",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "tZZ0y22bylYtITEaQ84ndznTItp_2FF5YDszhkP0747XdYygU73SzGViCGTqOJYjUEJhm6-AcRZtpjmuLh9UmGE1xEX3rRiayimmicjJhW6sT3Ia9zapn3i6ijTVNQaKFJvc5LXDYBgK2lS5NGwRvKqVhdmncHSSDQlTd-wX2OKlbB_7Wzq1t-4fsUDnlwHJBCp3guGAJ_libNKlyJ5QM6m4F3wAFo4ZbELfVOR8uXXtUIUZ_YcdRssPlqV5B_fkwtbMrh2bN2BQhVtHMnLbiRA-dma5UWhvNZCDQZ5nXv-HiQjurQAKGwyX-s_iR6-Bu5RpTfzbPDi3bw65BqOK-Q",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667339722,
    "updated": 1667339722,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
