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
Date:Mon, 07 Nov 2022 18:33:14 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASNclwSLH//4uWJSJFH5FwX72f1mDaP73201Ci/BiSMsOR+c7tnBdfTBd+53wERWc8U0nJIpq0DwkBrXLMrHc35oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAOCEZn6yLH2VrHIKz614h+B6Y+EvnxwM+mF+Okl96ysEAiBHj5pyqQuV+sj2yAG+eIjqWxH8zz6wqPkBLMIa2brryg==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "ebbba84173484cd7b4775f5b74bdd0a0"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 18:33:35 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/ccca48c859f845859f8b400a6c5d5cce",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/ccca48c859f845859f8b400a6c5d5cce",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/ccca48c859f845859f8b400a6c5d5cce",
  "x5t": "z-KN0bGvqrAD4E6VUJJP4r9y5wY",
  "cer": "MIIB2DCCAX6gAwIBAgIQEfEQBb4iSEGn2FSjRoxZ3DAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MTgyMzI2WhcNMjMxMTA3MTgzMzI2WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASNclwSLH//4uWJSJFH5FwX72f1mDaP73201Ci/BiSMsOR+c7tnBdfTBd+53wERWc8U0nJIpq0DwkBrXLMrHc35o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUk7lBG3jB06qFbgAw7SedlcFc2iAwHQYDVR0OBBYEFJO5QRt4wdOqhW4AMO0nnZXBXNogMAoGCCqGSM49BAMCA0gAMEUCIQDv75tqNsChSNwBh1AMDRmAIVsjsvhbRCnHFdYgGQckdQIgN1Us9wF9+qODM90tmGguu3vQ9yzYVkWC8Yus/wWlaEQ=",
  "attributes": {
    "enabled": true,
    "nbf": 1667845406,
    "exp": 1699382006,
    "created": 1667846007,
    "updated": 1667846007,
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
      "updated": 1667845994
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
