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
Date:Mon, 07 Nov 2022 23:39:05 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQjP/pTCHsIIpSTzNOq0idDbZ6v0nOqDDQ4WA7lJjUklLATYX7cMfDjgpXz2k1Nutn7Amwott1WEq+0/ynBW2uXoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAIsmbwdX54qEg7sFke+Lcz80et4+8PhAQfhps6jSmbyIAiAzi5wi0irl1VMiJMqvKVyi7ElZADkHjUEBFdcneiD96w==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "aff617846e5b437e9a6a2906bb915103"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 23:39:15 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/8e977e55c6a34ea1ba3ee13602de195d",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/8e977e55c6a34ea1ba3ee13602de195d",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/8e977e55c6a34ea1ba3ee13602de195d",
  "x5t": "C69xXL73hAqy1BPDDLohDmZVmbI",
  "cer": "MIIB2DCCAX6gAwIBAgIQLrdkZ6C5QFKKhyB/PjMk0TAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MjMyOTExWhcNMjMxMTA3MjMzOTExWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQjP/pTCHsIIpSTzNOq0idDbZ6v0nOqDDQ4WA7lJjUklLATYX7cMfDjgpXz2k1Nutn7Amwott1WEq+0/ynBW2uXo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUr83yDXhYuRcTquLeNQNXgMFq/wwwHQYDVR0OBBYEFK/N8g14WLkXE6ri3jUDV4DBav8MMAoGCCqGSM49BAMCA0gAMEUCIDNKbPbDh8c10elLT1hrF7C1NCojgwuZIiBnRlX34k0ZAiEA5mzkEAr3mfXLUtX0+fWavbEsY9dyTDvIqp7kj7ERc00=",
  "attributes": {
    "enabled": true,
    "nbf": 1667863751,
    "exp": 1699400351,
    "created": 1667864351,
    "updated": 1667864351,
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
      "updated": 1667864346
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
