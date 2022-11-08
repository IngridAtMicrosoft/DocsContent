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
Date:Tue, 08 Nov 2022 19:16:47 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATx3UTWBZpyfjFMSSH1qW2H05DNvlrZhIdxBGibtl2EF5tulfH9h30atjsVgSvIahoSgDofM/T80tDd5iVfX6VDoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgS8lrSVRoTWM3fn9S98REeZVnU1TvrSWkMb2RtEOwNScCIQDngwfICNL6Wdwauhvej1L7DG7Ordk+siK9ABIsrh4twA==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "1c2e79ffd00d4636a145f35d8bad9f5b"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 19:17:08 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/a614f2ca9dbf47c1b53d28f9514bcd79",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/a614f2ca9dbf47c1b53d28f9514bcd79",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/a614f2ca9dbf47c1b53d28f9514bcd79",
  "x5t": "RMWf1Pya8IEkoM_z4JjOTFARzNI",
  "cer": "MIIB2DCCAX6gAwIBAgIQNlboX8oNRGiJ8HJpCEt/ZzAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTkwNzA0WhcNMjMxMTA4MTkxNzA0WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATx3UTWBZpyfjFMSSH1qW2H05DNvlrZhIdxBGibtl2EF5tulfH9h30atjsVgSvIahoSgDofM/T80tDd5iVfX6VDo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUoI0+tnJhFUorSFE3y+TacwDT9n8wHQYDVR0OBBYEFKCNPrZyYRVKK0hRN8vk2nMA0/Z/MAoGCCqGSM49BAMCA0gAMEUCIQDXLUduTM6ZUgjnwhVPtobn1epU8rbf8zRdwEdj/6aekwIgTr5oaRnp6jNTowDu/lbshysTIRTTcgNs5n4okse/I4c=",
  "attributes": {
    "enabled": true,
    "nbf": 1667934424,
    "exp": 1699471024,
    "created": 1667935024,
    "updated": 1667935024,
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
      "updated": 1667935008
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
