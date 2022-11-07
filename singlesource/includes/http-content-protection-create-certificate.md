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
Date:Mon, 07 Nov 2022 18:32:37 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARLtXmypwfnEARJfUjv1MOVZUa4wpKBVNtmKt5IvVICXOx0LK9+6hs2Qe5PAJspfvpcu/FccmTRjy8dwlxLDW33oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAIwy0kzoctsv5YDSk9LpLyHO1F5U/cCMUQbCIRslm4lUAiBLAq+rUP/5Av+GbCXTFfph+afWTRkiJCi89YRU1XSPRA==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "73c08b2e2d5645ba9d69c935a6357b9d"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 18:32:58 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/fe7af3529f954ba992c780391dd64e9a",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/fe7af3529f954ba992c780391dd64e9a",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/fe7af3529f954ba992c780391dd64e9a",
  "x5t": "0dpYgPFPmfnwHycvvpfVTpr2OkA",
  "cer": "MIIB2DCCAX6gAwIBAgIQUWJpj5W9TFGyHO3xMxcTaTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MTgyMjUxWhcNMjMxMTA3MTgzMjUxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARLtXmypwfnEARJfUjv1MOVZUa4wpKBVNtmKt5IvVICXOx0LK9+6hs2Qe5PAJspfvpcu/FccmTRjy8dwlxLDW33o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUE/K90WphLPE7jcEdXbrPbMuvpJQwHQYDVR0OBBYEFBPyvdFqYSzxO43BHV26z2zLr6SUMAoGCCqGSM49BAMCA0gAMEUCIQDV/h2ZcsuXgdvDRKLAFHMSvmtKCMQ3uruhfV63LvSIVgIgG8ysJWbwEmWNlvhHDjXDRrR/Fkly/7ZjYRhMJ/vY0aw=",
  "attributes": {
    "enabled": true,
    "nbf": 1667845371,
    "exp": 1699381971,
    "created": 1667845971,
    "updated": 1667845971,
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
      "updated": 1667845958
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
