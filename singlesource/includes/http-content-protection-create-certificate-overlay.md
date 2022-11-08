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
Date:Tue, 08 Nov 2022 18:02:05 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNjCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATZQxDvYY+THaaA3aBWV9F6DBApG8OAWWkhvGRIUaz5DaeXsIkZR35rZih60T+ILjizMrXh+26tDYPPYJ5hpzGYoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSQAwRgIhAJVqReSIaDn5uhAwYhaTxBAzg5WeZMQ3QC719IcmWACpAiEAjHIoN/GYsBX4SmbDxM2o597DueAlrjY88W/bCJS78pw=",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "61790a041caa4b1f9cf09adbdc058faa"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 18:02:16 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/019cb31703094703a98995b757d6c66f",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/019cb31703094703a98995b757d6c66f",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/019cb31703094703a98995b757d6c66f",
  "x5t": "3sQ-7ZbAuUl9KEOw0UOkW6NaD9Q",
  "cer": "MIIB1zCCAX6gAwIBAgIQPgzaIgsPSJyijmIKvYbnKjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTc1MjEyWhcNMjMxMTA4MTgwMjEyWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATZQxDvYY+THaaA3aBWV9F6DBApG8OAWWkhvGRIUaz5DaeXsIkZR35rZih60T+ILjizMrXh+26tDYPPYJ5hpzGYo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUBtj+m9dHZ2xAZhVIp3zw8eli9nowHQYDVR0OBBYEFAbY/pvXR2dsQGYVSKd88PHpYvZ6MAoGCCqGSM49BAMCA0cAMEQCIHmbRJ8n3NBmwKPkquK+JkdM9rOvnRoJocMJi8C1gC0aAiAiSz6xdKGs+B5NvtVyJRcgI83Ye4mBneTaBl8B7YDntw==",
  "attributes": {
    "enabled": true,
    "nbf": 1667929932,
    "exp": 1699466532,
    "created": 1667930532,
    "updated": 1667930532,
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
      "updated": 1667930526
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
