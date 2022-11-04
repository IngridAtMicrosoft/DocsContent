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
Date:Fri, 04 Nov 2022 16:41:06 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATKpKok52o8GIX4C7ErqRgthB0tN0Y1BimuWu8bGKLBXPtf7cAiKaHpmILmpFjPp7Xufe3vLgrEgwxKQN/Jae7poEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAOZqwdJVmlJv+OHgY77SQIMszwCpIbQizhqofzRnj5X3AiAmJd1UI7Ojb4dAg5UfA5yCOwqBW7pIiYQW35ton3sY/w==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "e05aaeba950d42a6ad43aa106bd4e30d"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 04 Nov 2022 16:41:28 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/54d36f2bad42450b9afb8c1df912786f",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/54d36f2bad42450b9afb8c1df912786f",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/54d36f2bad42450b9afb8c1df912786f",
  "x5t": "QqUeBRViCdN5tyYU1Gjrj9Wd2hA",
  "cer": "MIIB2DCCAX6gAwIBAgIQZb/LyCXPT1eK6GDP2Mi0vjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA0MTYzMTE5WhcNMjMxMTA0MTY0MTE5WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATKpKok52o8GIX4C7ErqRgthB0tN0Y1BimuWu8bGKLBXPtf7cAiKaHpmILmpFjPp7Xufe3vLgrEgwxKQN/Jae7po3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUcO7fVb3CssFU9TYiqHz3ED2Q7NMwHQYDVR0OBBYEFHDu31W9wrLBVPU2Iqh89xA9kOzTMAoGCCqGSM49BAMCA0gAMEUCIFj5cZRXRh200hkHF8eaCHnj6EeO37eN96BfMnha6+gQAiEA7qq6KP+LnmlN74jjekZxu8EJk0jNYRD3mg9ghG30S2c=",
  "attributes": {
    "enabled": true,
    "nbf": 1667579479,
    "exp": 1699116079,
    "created": 1667580080,
    "updated": 1667580080,
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
      "updated": 1667580067
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
