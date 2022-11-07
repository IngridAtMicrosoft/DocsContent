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
POST https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/create?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "policy": {
    "key_props": {
      "kty": "EC",
      "crv": "P-256"
    },
    "x509_props": {
      "subject": "CN=content-protection-token-certificate"
    },
    "issuer": {
      "name": "Self"
    }
  }
}

202 Accepted
Date:Mon, 07 Nov 2022 23:39:27 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR+nhFN+G6yIV+xz2uV/Ca1x3tXnSOBfhW6jaI1syQ/hZlthjHQtunuk7/T9943quH4OZWG850yOnpHVlgZggxsoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAJPwWQdlzVd2B4jkcQhanlyRQLtZx4sfxI9sTP0wSTZbAiBiC778DbFSkTtvuzgD2qn/0WOrFgQELQ8XhkGtalE+pQ==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "01079ad6bbd74048a145125b9ac2aaaa"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 23:39:49 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/c88062ceb735487f904a71cac4034b46",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/c88062ceb735487f904a71cac4034b46",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/c88062ceb735487f904a71cac4034b46",
  "x5t": "w4Yd21BaezyYo4cQGtULGsXewTw",
  "cer": "MIIB2DCCAX6gAwIBAgIQbnr0wn1wRf2VkDwZYalzHjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MjMyOTQzWhcNMjMxMTA3MjMzOTQzWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR+nhFN+G6yIV+xz2uV/Ca1x3tXnSOBfhW6jaI1syQ/hZlthjHQtunuk7/T9943quH4OZWG850yOnpHVlgZggxso3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAU0xlw/phN5V6b7bvtkzd6HVoMMZQwHQYDVR0OBBYEFNMZcP6YTeVem+277ZM3eh1aDDGUMAoGCCqGSM49BAMCA0gAMEUCIQDw/3OQ8kJLtwjgpk5KlxESjTS7ot+ed5hspt7TY0R+zAIgduMBoN0GnqCaclW7fIp6J5J3wEwcYZK2G/Z9jSUnTro=",
  "attributes": {
    "enabled": true,
    "nbf": 1667863783,
    "exp": 1699400383,
    "created": 1667864383,
    "updated": 1667864383,
    "recoveryLevel": "Recoverable",
    "recoverableDays": 90
  },
  "policy": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/policy",
    "key_props": {
      "exportable": true,
      "kty": "EC",
      "key_size": 256,
      "reuse_key": false,
      "crv": "P-256"
    },
    "secret_props": {
      "contentType": "application/x-pkcs12"
    },
    "x509_props": {
      "subject": "CN=content-protection-token-certificate",
      "ekus": [
        "1.3.6.1.5.5.7.3.1",
        "1.3.6.1.5.5.7.3.2"
      ],
      "key_usage": [
        "digitalSignature"
      ],
      "validity_months": 12,
      "basic_constraints": {
        "ca": false
      }
    },
    "lifetime_actions": [
      {
        "trigger": {
          "lifetime_percentage": 80
        },
        "action": {
          "action_type": "AutoRenew"
        }
      }
    ],
    "issuer": {
      "name": "Self"
    },
    "attributes": {
      "enabled": true,
      "created": 1666977950,
      "updated": 1667864368
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
