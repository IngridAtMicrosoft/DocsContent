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
Date:Mon, 31 Oct 2022 20:52:31 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQgpe5iLq+agmP5j9X35nkXT0fnORxhCfGdHIRHuGZQbbquYV59zshwc2EW0+JIl8FvGNZNvY2OPk8xV4pISAz/oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgQsyEtlxfddHP1kjF4op3AzyAl9D8NFj+C5Nyi90tG2YCIFWp6rSx+92k1JvFG06+biCtgfno1QPstP8m+Kme97v5",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "63546461223f44e194eeb26321a7b397"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 31 Oct 2022 20:52:41 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/524c0e823bc74703b1de9d0f50584820",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/524c0e823bc74703b1de9d0f50584820",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/524c0e823bc74703b1de9d0f50584820",
  "x5t": "dt0iBIbKSKB4dMQy0eFO5DTTiak",
  "cer": "MIIB2DCCAX6gAwIBAgIQWpARt33+Rue/6+p8MmY4xjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMDMxMjA0MjQwWhcNMjMxMDMxMjA1MjQwWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQgpe5iLq+agmP5j9X35nkXT0fnORxhCfGdHIRHuGZQbbquYV59zshwc2EW0+JIl8FvGNZNvY2OPk8xV4pISAz/o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUkPOTJoDopKPAxZw/AQ/lkRBi9ZgwHQYDVR0OBBYEFJDzkyaA6KSjwMWcPwEP5ZEQYvWYMAoGCCqGSM49BAMCA0gAMEUCIGrccEO/2i73B+z7q1jiB6bLPLDv6aYbRj1NsiTreKjeAiEAwhI96F+rEv9jI2sZwVl0zUDPWdSRcrFoRw0vdlam7do=",
  "attributes": {
    "enabled": true,
    "nbf": 1667248960,
    "exp": 1698785560,
    "created": 1667249560,
    "updated": 1667249560,
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
      "updated": 1667249552
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
