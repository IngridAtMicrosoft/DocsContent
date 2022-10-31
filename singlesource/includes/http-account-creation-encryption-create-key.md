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
Date:Mon, 31 Oct 2022 20:52:18 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/6064ea5b2633430d8385cde4124a7d4d",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "2EFtz3coLM_ljhWOfLq2aYIZw1wGpwnn4-xzj6C6Kd8UNo29K_JZ-8d7CxeqKv18VhqpRsz1srzEM28V826QIBLu1Ct0kjOJywms5_mCiu5OsbMMfhWzZNOvvsuAOdximS5iw4atfy-8Mq0MduvaKBBXBnYP0ooHX-ZH3hhW9oaGUbec0kJpxcrRN8ToJDXulNr24cIkxbApMihi2xXtgOyKkRVlqv3hGCov56Q7T1BVvfU3Qn_Pc-DljNSd2ZGg69YwXWl_1vX1MzZ_E7iBLOsQtEQkO8SBO94eOoH9D4SfoMMDkT-OlDy8jYwdvcfVcnG2rPrmeA-yxJsS8_0KDQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667249539,
    "updated": 1667249539,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
