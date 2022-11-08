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
Date:Tue, 08 Nov 2022 19:50:30 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAT4ZrYohm4JtQ/ECZRQtI5XQieFKembGBFasK5wWqJkwWcgXjLOc/UWWa0sP+kSjPhEohYbPExwCMrAxMofnBv1oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhAM2VhBTFh6PKYmhNNmV1RH7DsfX2M1BNTXZ84ievp6WWAiEA//uY8ey5OlYyUSNIrTp8O70vL8eSqUiiPn4kYBYFHhc=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "9d2e1a1e868647f49dfcd73b496f5ab9"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 19:50:52 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/482cc7716df14955862ea73e773156f1",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/482cc7716df14955862ea73e773156f1",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/482cc7716df14955862ea73e773156f1",
  "x5t": "c1CQpIcz5cAvX4Ds9AcEdgjc0To",
  "cer": "MIIB1zCCAX6gAwIBAgIQb/nGu8bUTdyPOQeaooYBdjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTk0MDQ4WhcNMjMxMTA4MTk1MDQ4WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAT4ZrYohm4JtQ/ECZRQtI5XQieFKembGBFasK5wWqJkwWcgXjLOc/UWWa0sP+kSjPhEohYbPExwCMrAxMofnBv1o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAU2rb/xVamKl6xUZdzqth2foNr0mwwHQYDVR0OBBYEFNq2/8VWpipesVGXc6rYdn6Da9JsMAoGCCqGSM49BAMCA0cAMEQCIGjjUaMsn5KpoDmc0m6Lf0Is6MN8/jNoI6QGidIXCeH3AiBrRrtr998PsZVs9m7nAaTwNfOuVe/OgS7tEvyGdVxzJg==",
  "attributes": {
    "enabled": true,
    "nbf": 1667936448,
    "exp": 1699473048,
    "created": 1667937048,
    "updated": 1667937048,
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
      "updated": 1667937031
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
