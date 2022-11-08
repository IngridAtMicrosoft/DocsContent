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
Date:Tue, 08 Nov 2022 18:01:44 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASPkpe7gZA+vGWD4p0ZXcA1aGJFesVg/d5q3vUS4MVgPuKe3nH3YM5o4ZLFavxUxGffGMw/vC/XGG4TI/mpYCCaoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgOzGD5L1Y2GJROPJxSiVYWGGoLCMbOe2Fj/3YcjzP0J0CIErZUiBW3pyr8CMyBqO5YyO2JqwVn0PwAaR7y/tUP9yu",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "e91568715a454e78b716d1a5b5b68bb6"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 18:01:54 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/6edb8c33aa204e6a917a7a2bfce12381",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/6edb8c33aa204e6a917a7a2bfce12381",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/6edb8c33aa204e6a917a7a2bfce12381",
  "x5t": "4CVFUg_fKuRzjTbkCR3lp9FNpBg",
  "cer": "MIIB2DCCAX6gAwIBAgIQGhe7reDNTSeMS+rxRzM+6DAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTc1MTUxWhcNMjMxMTA4MTgwMTUxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASPkpe7gZA+vGWD4p0ZXcA1aGJFesVg/d5q3vUS4MVgPuKe3nH3YM5o4ZLFavxUxGffGMw/vC/XGG4TI/mpYCCao3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUq2+124XwunUg5CsgoHKGuCTuvocwHQYDVR0OBBYEFKtvtduF8Lp1IOQrIKByhrgk7r6HMAoGCCqGSM49BAMCA0gAMEUCIQCTLhZdHeSFjM1thyTO2/RbHoP1xZoUAMwqr71hjSZ5tgIgLPYC7gfmrjkifBtSiP6s3QjcyviMKc5aUbuwCzlhJRk=",
  "attributes": {
    "enabled": true,
    "nbf": 1667929911,
    "exp": 1699466511,
    "created": 1667930511,
    "updated": 1667930511,
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
      "updated": 1667930504
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
