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
Date:Thu, 15 Dec 2022 23:13:32 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQwKgVP0ezen2j4Cf0CwNOxfe6eyIux/0NOWXnZ1DywYItuq6l7I6eTVowmdWFMegH3SWIrUDQZb5MTDF77ckCAoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhANPkIKNg2Mc6gfwszsAj7M2UjuitbUF94HmFEB8NSfykAiEAjlPRpynJcwiMF8zlulFqVTjaOf7RXZXnsLZma8vEmik=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "eda8fe9790cd4ef295bdf2a18a782bfe"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Thu, 15 Dec 2022 23:14:02 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/863ff8a5c0d94ebc91c1669667bbed9d",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/863ff8a5c0d94ebc91c1669667bbed9d",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/863ff8a5c0d94ebc91c1669667bbed9d",
  "x5t": "8qbcShmRjFe8684vnTil78u5Lsc",
  "cer": "MIIB2DCCAX6gAwIBAgIQBslPp+qdSNOoBjyBjrFLTDAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMjE1MjMwMzUzWhcNMjMxMjE1MjMxMzUzWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQwKgVP0ezen2j4Cf0CwNOxfe6eyIux/0NOWXnZ1DywYItuq6l7I6eTVowmdWFMegH3SWIrUDQZb5MTDF77ckCAo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUvtabn3w94gYo4PVOmR08lWTO03AwHQYDVR0OBBYEFL7Wm598PeIGKOD1TpkdPJVkztNwMAoGCCqGSM49BAMCA0gAMEUCIErEORlY8dOixilHWYZlsGlTn1XqFUqyx9sGNjmm/FbiAiEA5ydPquOBbUeNHCwpCLqLqN7eNDEoAxwY/7Pd+ueNbhc=",
  "attributes": {
    "enabled": true,
    "nbf": 1671145433,
    "exp": 1702682033,
    "created": 1671146033,
    "updated": 1671146033,
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
      "updated": 1671146012
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
