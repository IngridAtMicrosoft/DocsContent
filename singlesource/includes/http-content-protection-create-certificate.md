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
Date:Fri, 28 Oct 2022 17:47:15 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNDCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAToVci2mt1ytnuSrXN44mzkSX6H4/9UcyUtc32fHU53IwCsSreirl4HaKzZyvzYRdlsZykeT8vHfJwUfba+XoeSoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDRwAwRAIgF7FDaD42+w9lAehpPOdzv0SXVoKJjaGDiulR5USW2acCIH9edpX+37e7UCe+BTxkiDUVx8a2nCIjE4dOcJepjjoT",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "170f3241433345e584744873ad279f09"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Fri, 28 Oct 2022 17:47:35 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/d0d4dc8859c54422b9476d5f5cb2d240",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/d0d4dc8859c54422b9476d5f5cb2d240",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/d0d4dc8859c54422b9476d5f5cb2d240",
  "x5t": "WThdlc7Ec0LWK8zZlYwGMWEZ-74",
  "cer": "MIIB2TCCAX6gAwIBAgIQb2KxVxH2RnSGK2GcGP+O0zAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMDI4MTczNzI2WhcNMjMxMDI4MTc0NzI2WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAToVci2mt1ytnuSrXN44mzkSX6H4/9UcyUtc32fHU53IwCsSreirl4HaKzZyvzYRdlsZykeT8vHfJwUfba+XoeSo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUgvDKaz8/gt3zI7BSpitmpICs0mEwHQYDVR0OBBYEFILwyms/P4Ld8yOwUqYrZqSArNJhMAoGCCqGSM49BAMCA0kAMEYCIQD0iqFmZ7S+g/YrTUILsFXb8wkJrcGjLVWU5KbNonoq2gIhAL3xB7VVAr4xbLIrcNyx52bWW3GvqB+Q0ZsaOP8todbu",
  "attributes": {
    "enabled": true,
    "nbf": 1666978646,
    "exp": 1698515246,
    "created": 1666979246,
    "updated": 1666979246,
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
      "updated": 1666979236
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
