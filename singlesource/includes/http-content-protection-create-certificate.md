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
Date:Tue, 01 Nov 2022 16:36:05 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAT6IQMVlnM5f3ojI/38MnPNadGWNgTHLl8lshbjaD3wvQV8Am1ga9iZjIRHFioDGTPKoXsJkM1exklHulmGQB7QoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgQgyX/DR3iteg7wp+iNo3TS4K1QcYR6C+SAxtX74AHc4CIGGhSQ59DqMknYKF78hyzE1tmqVAOre6nBTguJ98UB59",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "47098f368e1d4d8ba75ffeef5cfa569e"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 01 Nov 2022 16:36:26 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/3d26a1843a9c43d1b81e79ec260ee003",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/3d26a1843a9c43d1b81e79ec260ee003",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/3d26a1843a9c43d1b81e79ec260ee003",
  "x5t": "R626PdMrf4WQcLyUY_OfzpIgIt0",
  "cer": "MIIB2DCCAX6gAwIBAgIQcaTzl+nDRXWYT1OOPlwQxzAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTAxMTYyNjE3WhcNMjMxMTAxMTYzNjE3WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAT6IQMVlnM5f3ojI/38MnPNadGWNgTHLl8lshbjaD3wvQV8Am1ga9iZjIRHFioDGTPKoXsJkM1exklHulmGQB7Qo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAU/QdI0wQg9bX/DCrl2Wz/BDl2EycwHQYDVR0OBBYEFP0HSNMEIPW1/wwq5dls/wQ5dhMnMAoGCCqGSM49BAMCA0gAMEUCIQDLDqiaue1q+Vg2fefX2zrK0rzvGy5vcTAz4kJGoq/DhgIgK38K5BEnp7GMQwdfKnzLFCnX+lvMI5NK13zOf7rEuE8=",
  "attributes": {
    "enabled": true,
    "nbf": 1667319977,
    "exp": 1698856577,
    "created": 1667320578,
    "updated": 1667320578,
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
      "updated": 1667320565
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
