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
Date:Mon, 07 Nov 2022 17:08:08 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQu2Ll79+tYTuWV7mxDzqwwrxEfi6svytwzlVJLOIaegSj1MZ6ZDbxO+mCnNf1deCGfia67LRKAUO/4Df4tEAB8oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgFhDrJvWVR6bQLHjkq2ktfYo+dZ+YXSuaA7Vlt2kZ0G4CIQD75reXkzJbYciDkJkNnF1qQ4UkdWN2Z/REi3ZoZZamrA==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "d5febffdc8f048edbf4fbfcc54222a37"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 17:08:29 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/e58e02f5a3ef4d94ac72b1cb24f33f47",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/e58e02f5a3ef4d94ac72b1cb24f33f47",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/e58e02f5a3ef4d94ac72b1cb24f33f47",
  "x5t": "H1HNb0PB_PPvBOCQ0LOtrkgCyxU",
  "cer": "MIIB2DCCAX6gAwIBAgIQfugxHXQJQROHs4W7RweIuDAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MTY1ODIxWhcNMjMxMTA3MTcwODIxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQu2Ll79+tYTuWV7mxDzqwwrxEfi6svytwzlVJLOIaegSj1MZ6ZDbxO+mCnNf1deCGfia67LRKAUO/4Df4tEAB8o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUmrJjC9sd30g4oGusAB/YrO9N6GMwHQYDVR0OBBYEFJqyYwvbHd9IOKBrrAAf2KzvTehjMAoGCCqGSM49BAMCA0gAMEUCIFR6StXO2fQmyZp9Ie3AVgt8pHXLgJYLjafXHMXlT+81AiEAl2Z0auEdbK0ZWDwWktvQlDs62j48B1Qh/nywjJTXSbk=",
  "attributes": {
    "enabled": true,
    "nbf": 1667840301,
    "exp": 1699376901,
    "created": 1667840901,
    "updated": 1667840901,
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
      "updated": 1667840888
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
