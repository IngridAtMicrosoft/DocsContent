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
Date:Tue, 08 Nov 2022 18:32:39 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQS9HrXjVTfdmhaXYqJnYdXq+ENUaQGnDvRTyoWfn8mmkALPeAsRRpLHrT+jxTXT9UAvCK0JLT68oiGXwx3Cw13oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhALYMKwZEYWHJ+EtB0pVflTEVa7Ij1C5JUfQLb7dGhZaTAiEA6fkMnNDROEYOwl/wYd6/vuT1F2P/jBODFepME9PiiYM=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "ce21e8eb74064eacbbadfbba25ce68d4"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 18:32:59 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/0539af26104e427a89a0585907e068ef",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/0539af26104e427a89a0585907e068ef",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/0539af26104e427a89a0585907e068ef",
  "x5t": "ZNaoPkqqG-JTgqJCNsyHX5H8OpE",
  "cer": "MIIB2DCCAX6gAwIBAgIQHaKjgQD6Rc2Iei4oFUe0CTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTgyMjUxWhcNMjMxMTA4MTgzMjUxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQS9HrXjVTfdmhaXYqJnYdXq+ENUaQGnDvRTyoWfn8mmkALPeAsRRpLHrT+jxTXT9UAvCK0JLT68oiGXwx3Cw13o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUC2ufhwUwvFE0Io8Og7VR/b4gQ6YwHQYDVR0OBBYEFAtrn4cFMLxRNCKPDoO1Uf2+IEOmMAoGCCqGSM49BAMCA0gAMEUCIQCYkDk10IxSEGdObh/0udfO337EhGaEMEqqb4D/nE42PwIgNmO5XpLKcRjje7sSuoenbYb1uYlaWVVzY1dUGa4jNKc=",
  "attributes": {
    "enabled": true,
    "nbf": 1667931771,
    "exp": 1699468371,
    "created": 1667932371,
    "updated": 1667932371,
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
      "updated": 1667932359
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
