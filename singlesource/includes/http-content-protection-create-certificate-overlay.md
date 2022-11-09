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
Date:Wed, 09 Nov 2022 17:31:12 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR2zG2BCEt7aOIKSTgrQ73YGl2OacrNfYwpAoyOyz1az0P+QkiQcegbUprjwAz9ap+12aqE5td1Xa1xY0OpqEPDoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgFwJRZus6iDNtH5crjamU+yIqmiW4KavUFbM55vraS7ACIQD7Dvbi9jUExppERvUIv07FXX8E5WiRXCQFkR7wCGhcnw==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "f25767872c4e488f9b0565b4e5de8ad5"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Wed, 09 Nov 2022 17:31:22 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/dcc1b32ed7354ecb8f77a562cec0aef6",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/dcc1b32ed7354ecb8f77a562cec0aef6",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/dcc1b32ed7354ecb8f77a562cec0aef6",
  "x5t": "WX7DYXKUiKEYjrpOCBDhBYXMhN4",
  "cer": "MIIB1zCCAX6gAwIBAgIQO0cMiZMOSP2jtp9/dLByRjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA5MTcyMTIyWhcNMjMxMTA5MTczMTIyWjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAR2zG2BCEt7aOIKSTgrQ73YGl2OacrNfYwpAoyOyz1az0P+QkiQcegbUprjwAz9ap+12aqE5td1Xa1xY0OpqEPDo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUKnm9/vHlaLk0YNMlULjvu8MRnicwHQYDVR0OBBYEFCp5vf7x5Wi5NGDTJVC477vDEZ4nMAoGCCqGSM49BAMCA0cAMEQCIGSb5LZGva8fNjz3j1kocEtaMYilfRL7F6NYsmfjGRLLAiA5s5gROL2uQTqhRdsYGcB1yzwiEOvC8YpfEhSdG35cMA==",
  "attributes": {
    "enabled": true,
    "nbf": 1668014482,
    "exp": 1699551082,
    "created": 1668015082,
    "updated": 1668015082,
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
      "updated": 1668015073
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
