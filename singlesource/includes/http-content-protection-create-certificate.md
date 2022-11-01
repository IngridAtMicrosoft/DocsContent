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
Date:Tue, 01 Nov 2022 21:55:29 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQRhwko0JlzOM00jOIXrIYS07zo6UC6T5A8BOqSAKF4Cfg/twyE9Q9D7DChi7sDFAcR0C/eyTITQI5YZRkwW+IDoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhANCOvdySShZ3d1pstqdIsghOB2uEDAxswt+FSLyvSQGhAiBAFgwJqrElbk3QDA58UJDRI+aPlr75GTfGwf4vN1ot2w==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "574c9205054b45309207d2b6962919c2"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 01 Nov 2022 21:55:50 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/f8dfb1485ea245c49055125506d34b79",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/f8dfb1485ea245c49055125506d34b79",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/f8dfb1485ea245c49055125506d34b79",
  "x5t": "U6vULQ45khofJdJJ9W8xcpT_214",
  "cer": "MIIB2TCCAX6gAwIBAgIQRDcI9FicQSWv9WS1XJC6KjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTAxMjE0NTQ2WhcNMjMxMTAxMjE1NTQ2WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQRhwko0JlzOM00jOIXrIYS07zo6UC6T5A8BOqSAKF4Cfg/twyE9Q9D7DChi7sDFAcR0C/eyTITQI5YZRkwW+IDo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUCRxeUHDL0f8zGqHg070PW7rWYtIwHQYDVR0OBBYEFAkcXlBwy9H/Mxqh4NO9D1u61mLSMAoGCCqGSM49BAMCA0kAMEYCIQDP1pi+WDhVnsg0p9IwrjG64OO7FigX/5XENNqg40UF6gIhAM9QQwRHPCVCVag9uXI6gxvWpAUxAGWy6F7/YEpzd5g5",
  "attributes": {
    "enabled": true,
    "nbf": 1667339146,
    "exp": 1698875746,
    "created": 1667339746,
    "updated": 1667339746,
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
      "updated": 1667339730
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
