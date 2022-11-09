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
Date:Wed, 09 Nov 2022 17:30:46 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASiw5ja27IKjU3twSQghHk9qEH5DA/PRT7uIrir7EyuQR1mxgtP/Ravukmh/u05sKMQK1+vfQD0kYS/s40XdRo2oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhAP3Mf+XrV1TkoPAL1zHqpnMjnfCPeM9ldKj4vdCKBQL0AiEAuxVn6mlFNNbFK8BaWdmQ6D4Nzo4GCngwP9rFm9r4jL0=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "b98ef893d8844611a6813e46c14cf968"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Wed, 09 Nov 2022 17:30:57 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/cc681bd2be6a4f7bba9ebc6934557583",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/cc681bd2be6a4f7bba9ebc6934557583",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/cc681bd2be6a4f7bba9ebc6934557583",
  "x5t": "koaKnLrOWGKJqqIJCC_BYQ4-Qq4",
  "cer": "MIIB2DCCAX6gAwIBAgIQXcK17CXoRJeT3bC3ftM74jAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA5MTcyMDU0WhcNMjMxMTA5MTczMDU0WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASiw5ja27IKjU3twSQghHk9qEH5DA/PRT7uIrir7EyuQR1mxgtP/Ravukmh/u05sKMQK1+vfQD0kYS/s40XdRo2o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUcemO4UCYfaLveHc5eNy4kQkHV+8wHQYDVR0OBBYEFHHpjuFAmH2i73h3OXjcuJEJB1fvMAoGCCqGSM49BAMCA0gAMEUCIQDVEpT69jLP4n3xksJcuwNJgA5Tp7RdSzCvH26f4OJETQIgHuMf4eh4aEQzhG6G6v4D/f2CHk9PhSW4RxUG+vFer/4=",
  "attributes": {
    "enabled": true,
    "nbf": 1668014454,
    "exp": 1699551054,
    "created": 1668015055,
    "updated": 1668015055,
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
      "updated": 1668015047
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
