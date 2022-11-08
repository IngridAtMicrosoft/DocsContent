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
Date:Tue, 08 Nov 2022 18:32:07 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQOao/Vn22a03CiNsNGP1moMKj5AOPhTZqDyt3Jd90U1/96YjaINqJLciUyjf5t2CRzNr0aRqcM9sKHlXJQLEYWoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgdGiul+pgxJvP3pdKM8NtEUdAbaXOSt7ynF2llrEJhYgCIGApBN7cs3RMy0hmleZpuN76JfXity7s0HQXC0El/ETD",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "b0f0ae3765ff41e5aa089979a5a7e2ce"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 18:32:28 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/f569c8b7ec214737944fc9e554c1518b",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/f569c8b7ec214737944fc9e554c1518b",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/f569c8b7ec214737944fc9e554c1518b",
  "x5t": "Sk3NzI0hS3PpCpCEuo1EBaski5A",
  "cer": "MIIB2DCCAX6gAwIBAgIQU+y++2gtRiuQt8YlJ2KGlTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTgyMjIxWhcNMjMxMTA4MTgzMjIxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQOao/Vn22a03CiNsNGP1moMKj5AOPhTZqDyt3Jd90U1/96YjaINqJLciUyjf5t2CRzNr0aRqcM9sKHlXJQLEYWo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUNAaU9JqtmvZmEpSsV7omhrcDNXUwHQYDVR0OBBYEFDQGlPSarZr2ZhKUrFe6Joa3AzV1MAoGCCqGSM49BAMCA0gAMEUCIQCxEWv2GuTHI6LDsE6Jz+qZDLGVd/6C1yMxs/PeZ6Me0gIgHqANnRXF8OidBlabnctnfGaN7CfHvGB2Bq3x4bgTiQ8=",
  "attributes": {
    "enabled": true,
    "nbf": 1667931741,
    "exp": 1699468341,
    "created": 1667932341,
    "updated": 1667932341,
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
      "updated": 1667932327
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
