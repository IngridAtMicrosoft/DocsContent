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
Date:Thu, 15 Dec 2022 23:12:50 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATGpQOMPsdtw+ghBlmPM1tpwKBfyt9BT8O6uy0UiUS9tM3mfWf1+VChY2E0opZvEHiYoDVdELprfUZEtkGVzBxLoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgIRuzQcwzCjkP/2xoVMPL+JuACF8QDLwYnsEByEaczfgCIQCrmslB/x8ruGmcP/c3tDbn9ToFCCGcvrMQe3ubX3S7ag==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "4353980efc734e6c84a69d8a8aa65b40"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Thu, 15 Dec 2022 23:13:21 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/fa38d39831884abe8d3c91ba0bb6db08",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/fa38d39831884abe8d3c91ba0bb6db08",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/fa38d39831884abe8d3c91ba0bb6db08",
  "x5t": "j5iQbm4q5VFQWQiSGwB6oDUCxdQ",
  "cer": "MIIB1zCCAX6gAwIBAgIQG9Dg2q7jTO6kdqiM2J+iJjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMjE1MjMwMzE4WhcNMjMxMjE1MjMxMzE4WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATGpQOMPsdtw+ghBlmPM1tpwKBfyt9BT8O6uy0UiUS9tM3mfWf1+VChY2E0opZvEHiYoDVdELprfUZEtkGVzBxLo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUUMw0h9pOthfw3PhC5i8m34eZnNwwHQYDVR0OBBYEFFDMNIfaTrYX8Nz4QuYvJt+HmZzcMAoGCCqGSM49BAMCA0cAMEQCIB35lHutC+0yRJ3kV1L2zgigBTxSLklYj7jW/UKjc/eQAiA01tAJtfAL8gfQ/2Yo+qc0FtWlo1MTF4jz7TV9Cg+vlQ==",
  "attributes": {
    "enabled": true,
    "nbf": 1671145398,
    "exp": 1702681998,
    "created": 1671145998,
    "updated": 1671145998,
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
      "updated": 1671145971
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
