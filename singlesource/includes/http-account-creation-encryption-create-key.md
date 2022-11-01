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
Date:Tue, 01 Nov 2022 21:31:56 GMT
Content-Type:application/json; charset=utf-8

{
  "key": {
    "kid": "https://mykeys.vault.azure.net/keys/account-encryption-key/796fa5b311b34d51bb898b9d6e68718b",
    "kty": "RSA",
    "key_ops": [
      "encrypt",
      "decrypt",
      "sign",
      "verify",
      "wrapKey",
      "unwrapKey"
    ],
    "n": "5sQzO4AsNBixAjYpO0VYgG6ykkHW79t0Wr-UwSVOU65FY_33fIxTEPxDXrPbKqSDFqAe7Yiz2aUrptbKZfkJUrWXq0-I3wBcn7ArbWA3FlzFBOnXVdK4wch2fhUnZHdlaxHAKjrT3ThoK9bMGOKl9ws1xpXzBq90isFuSxnpkE5ZyYXo06Kxe84eRMJqn23H6w-mHvoVbOx8RKuojvL-3Ty5ReZWeb-0URbJDM1sQ8r26z0jhbiG9WCC740wf6ecJEjIujlqFAaIS6O-cjWz7yS4UxjGYFgJ-k4EBlc7B_v4HKahYf_hp7b1bwbYL6HQTwxO3XHRAB3z3dlZp_2FbQ",
    "e": "AQAB"
  },
  "attributes": {
    "enabled": true,
    "created": 1667338316,
    "updated": 1667338316,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90,
    "exportable": false
  }
}

```
