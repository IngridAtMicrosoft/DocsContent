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
Date:Tue, 01 Nov 2022 23:10:39 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARJJCZtNcfLOB6m+N2iIJ7vLXPZjqi3+tBdRu/NpKr6i8x3kKwp4If/e0/5lmSlSTBLUJY+zH7DDyyMHcD3kkQUoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgYBlEmKXhRdTJpdekhtF9UFNWd3pYRXrGCSaUySWxiGACIDUx3CGmNE5fGy+lLzrhIRNO5xQzCtKBTCF+HbcJQkUh",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "521ef2d1d9024c4f8ec004c7b0fbd971"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 01 Nov 2022 23:10:59 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/cde6f539d4f74d479f73d1a67f517f31",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/cde6f539d4f74d479f73d1a67f517f31",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/cde6f539d4f74d479f73d1a67f517f31",
  "x5t": "rM4pTxFBxCJGk9hhiBj5dVaq0A4",
  "cer": "MIIB1zCCAX6gAwIBAgIQXV3Z7NbNTFqAkpoJXhn4dDAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTAxMjMwMDUyWhcNMjMxMTAxMjMxMDUyWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARJJCZtNcfLOB6m+N2iIJ7vLXPZjqi3+tBdRu/NpKr6i8x3kKwp4If/e0/5lmSlSTBLUJY+zH7DDyyMHcD3kkQUo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAU/sQPmh3EvWfL7RCP6ZxlOKTeGR4wHQYDVR0OBBYEFP7ED5odxL1ny+0Qj+mcZTik3hkeMAoGCCqGSM49BAMCA0cAMEQCIEFtgzrf2t2YV1C88ptpG4xrqUCUTD2+mTjcGiGLgaQHAiArmttN46+srhvhVqUsExkqQ3H3GeIH8yvVDWLly5N07A==",
  "attributes": {
    "enabled": true,
    "nbf": 1667343652,
    "exp": 1698880252,
    "created": 1667344252,
    "updated": 1667344252,
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
      "updated": 1667344240
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
