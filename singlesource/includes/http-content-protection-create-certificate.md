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
Date:Tue, 08 Nov 2022 19:16:26 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQo77BnjChaMrYfJFc1xm9LbcAecVuEpXNK5EBIMU/aNRH82PX+8xIAJlkrTDxv4h9gm5vt590rYtVTPTPbzrHEoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIhAJPe2+YnvLpdDGqiqeUU11u+9ax0bwdAGBNoZZd4Ni68AiBVYd9vze0aoUhPYlCmtMYkWbMskXa/4GnsA/sXeWyTCQ==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "3dca62d6ab084fc195e95a49d5b9e220"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Tue, 08 Nov 2022 19:16:36 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/3f2da98555b3402b925941eb99c40436",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/3f2da98555b3402b925941eb99c40436",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/3f2da98555b3402b925941eb99c40436",
  "x5t": "odJPN-q8wrlm9YLH4jP6YS6n2mU",
  "cer": "MIIB2DCCAX6gAwIBAgIQNHolyKueRBmCIXf7Ug1ahTAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA4MTkwNjMzWhcNMjMxMTA4MTkxNjMzWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQo77BnjChaMrYfJFc1xm9LbcAecVuEpXNK5EBIMU/aNRH82PX+8xIAJlkrTDxv4h9gm5vt590rYtVTPTPbzrHEo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAU5M4zDig+39mmSFAqFjK/XB/oj7gwHQYDVR0OBBYEFOTOMw4oPt/ZpkhQKhYyv1wf6I+4MAoGCCqGSM49BAMCA0gAMEUCIFG9JxbnwrK26VV6/PGpMUBA2FM/k3ccDTyED568zTSGAiEA6apDAhDiF78fr4XaVi7Zn8Ia+yNo/oIgOjF2z/KYtzQ=",
  "attributes": {
    "enabled": true,
    "nbf": 1667934393,
    "exp": 1699470993,
    "created": 1667934993,
    "updated": 1667934993,
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
      "updated": 1667934986
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
