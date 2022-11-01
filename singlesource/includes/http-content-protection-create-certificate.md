---
title: include file
description: include file
author: jonpayne
ms.topic: include
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
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
Date:Tue, 01 Nov 2022 15:43:43 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASfAHNNoHjuYvVsm/libDDTScMpiJuKJPzCN1h61Uc+iURHZvVaSzLpf2YQeurDXGyV5myk01D8wG21bai9vtqjoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhAMPWE/yzlggkOvovsYF+8N7jNUVbBV/gDotkKw7cq71wAiEA36igH1vm+PYTACDnVyv13CYlK+pkzZG6ki7m3rPosc0=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "7c13bc236dba4a17961e87babe30edd5"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 01 Nov 2022 15:44:04 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/078df9f388424e9c909a04a04cae5187",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/078df9f388424e9c909a04a04cae5187",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/078df9f388424e9c909a04a04cae5187",
  "x5t": "Q9FPELpFOElwcwios5jdF4yOZUA",
  "cer": "MIIB1zCCAX6gAwIBAgIQEBk0baeaQPKk189VUt9eMTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTAxMTUzNDAxWhcNMjMxMTAxMTU0NDAxWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASfAHNNoHjuYvVsm/libDDTScMpiJuKJPzCN1h61Uc+iURHZvVaSzLpf2YQeurDXGyV5myk01D8wG21bai9vtqjo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUEoiLPaH1RIMToMHwkKzb0wdtijQwHQYDVR0OBBYEFBKIiz2h9USDE6DB8JCs29MHbYo0MAoGCCqGSM49BAMCA0cAMEQCIENvxnvEo11bO8/KO7/iX5hbTiJrgwvKcT4pktbqsuQHAiANZ9tfHAY49vlDXCBDtuerZv4tEFn8M0hQoSMUrFl+Tw==",
  "attributes": {
    "enabled": true,
    "nbf": 1667316841,
    "exp": 1698853441,
    "created": 1667317441,
    "updated": 1667317441,
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
      "updated": 1667317424
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
