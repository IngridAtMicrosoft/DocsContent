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
Date:Mon, 07 Nov 2022 18:12:25 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASr2lXxk6rJ5wz5+VtuaG71ot4ckbJzemY28WIzvuODXsKlAE9Tx5qp6I7UCHQpmbSpQsuXCDAsszeQYquDadj1oEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgXRLmGHcj3LEwQcUnFEoNoe3OmyCfVzq5tZdpT9AJDAoCIQDbUbXz6gkhIBNHzgZ3yVJFANKjs9C2Xm1iJj+dovZ4Vg==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "b1862f6d66d24966a0e501fa1f886aec"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 18:12:46 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/43f44feacab7470eb16726ba36f91c6b",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/43f44feacab7470eb16726ba36f91c6b",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/43f44feacab7470eb16726ba36f91c6b",
  "x5t": "whCMRp3_T76T1F3dzRJsfBr5xO8",
  "cer": "MIIB2TCCAX6gAwIBAgIQE9l/wLxZQEW5n1OJRw36OjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MTgwMjQwWhcNMjMxMTA3MTgxMjQwWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAASr2lXxk6rJ5wz5+VtuaG71ot4ckbJzemY28WIzvuODXsKlAE9Tx5qp6I7UCHQpmbSpQsuXCDAsszeQYquDadj1o3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUFR4iMWI+Xsk7acOA85y750bfLGwwHQYDVR0OBBYEFBUeIjFiPl7JO2nDgPOcu+dG3yxsMAoGCCqGSM49BAMCA0kAMEYCIQDGoF8/I4tQIWs5kOJvlz7/FRQOnWmKPi46n72IPeDfQQIhANEUfIvxZsZl5CLhgxyQKVvcw7q37mh38Sgw1OjO+ACi",
  "attributes": {
    "enabled": true,
    "nbf": 1667844160,
    "exp": 1699380760,
    "created": 1667844760,
    "updated": 1667844760,
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
      "updated": 1667844746
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
