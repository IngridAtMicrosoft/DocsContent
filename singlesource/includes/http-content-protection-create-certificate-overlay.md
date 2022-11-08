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
Date:Tue, 08 Nov 2022 19:51:02 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASaOxEBVRh72bnf1IEFJwkKPmW9wjI+3FDPQTKEIS4TAqfGtSbn/XhzXiGr7OxW8QsishtkR2MjIURIHPbb/spuoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgULtOp6WjsM66Y2849Ru5/Jna9AVeMIgGkFJYC08uuA0CIQDfw20TYjfyKE9NwPfwgx7+7Sg3IKdiVtW24i45ii9+Yg==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "43d161773e03445a9271b7e34ea7ec76"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 19:51:13 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/c9a01660192b43b8abc2ec155f1b8e7c",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/c9a01660192b43b8abc2ec155f1b8e7c",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/c9a01660192b43b8abc2ec155f1b8e7c",
  "x5t": "egKLXfM8kkDR1sidlviiko4evTg",
  "cer": "MIIB2TCCAX6gAwIBAgIQP2hPTPV+SUWPe8PT8kONxTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTk0MTEwWhcNMjMxMTA4MTk1MTEwWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASaOxEBVRh72bnf1IEFJwkKPmW9wjI+3FDPQTKEIS4TAqfGtSbn/XhzXiGr7OxW8QsishtkR2MjIURIHPbb/spuo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUimSo66SvCjRNfH18ASyQ3SbjxlswHQYDVR0OBBYEFIpkqOukrwo0TXx9fAEskN0m48ZbMAoGCCqGSM49BAMCA0kAMEYCIQDW+va0WwhS63OmMy4qOCBZDDEMRXsrAANNSAZ5RPpgOwIhANrCrC+FJ8UkXeimQ6UEFW4MRp471SsM8Y+wFsEyzOPb",
  "attributes": {
    "enabled": true,
    "nbf": 1667936470,
    "exp": 1699473070,
    "created": 1667937070,
    "updated": 1667937070,
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
      "updated": 1667937062
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
