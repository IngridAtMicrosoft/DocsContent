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
Date:Tue, 01 Nov 2022 21:29:39 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASjhUVn+LiPvdf4oRaXkFAdxwLhwmwcqr6XXxR1BYIhg5zEMWPFIjFujO8qhMS7wwJSxZXnem4P9pSNGw5ifla4oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgAntMDz94to64PhaUDkhLCXeVoqXN15YN4vTw1yVrK1cCIQDiPH89xoil8tRH0aFbToWDB7zxDtLfbzpxMmuk9iNVCw==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "61b88eb3535844acbda0e200b1168100"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 01 Nov 2022 21:29:49 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/6520e6199eb6465b88525428c4344ce3",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/6520e6199eb6465b88525428c4344ce3",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/6520e6199eb6465b88525428c4344ce3",
  "x5t": "oTAZ2qVzoDQOuKiB68pdgdl_zpM",
  "cer": "MIIB2DCCAX6gAwIBAgIQQLKmlGjxRYOa8WXneN9dhjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTAxMjExOTQ3WhcNMjMxMTAxMjEyOTQ3WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASjhUVn+LiPvdf4oRaXkFAdxwLhwmwcqr6XXxR1BYIhg5zEMWPFIjFujO8qhMS7wwJSxZXnem4P9pSNGw5ifla4o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUD6VQJm/see0NkEKNXY/dF15bnvYwHQYDVR0OBBYEFA+lUCZv7HntDZBCjV2P3RdeW572MAoGCCqGSM49BAMCA0gAMEUCIBbxbB9UYMSh5uO3dEkHFmfbb2XJIZjo8y22LHdyEJ5wAiEA0P0yAYQ7U8Zygb06EzDb2bbUepRpxjcI+u1xnQcNTu8=",
  "attributes": {
    "enabled": true,
    "nbf": 1667337587,
    "exp": 1698874187,
    "created": 1667338187,
    "updated": 1667338187,
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
      "updated": 1667338179
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
