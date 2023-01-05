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
Date:Thu, 05 Jan 2023 17:02:53 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARuPh6D+cEryBgKXjgJCsN6M12NPTVdMW+9RuaPbc4jVYJbeRJLmlXTcbON00obrF/DN/by3hyz6Ctpls0lFYSHoEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgTv1EonjU2vRoiHhUkndKREPgcH+6vj4JYATRfI1UBc0CIQDj3Ql1bC2VsW0Qc1I6wo8E9AdkzeQDoqjRyzqys0g9Kg==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "81e9298570ea4472a6e2dc23b761109e"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Thu, 05 Jan 2023 17:03:14 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/403d659f268e428dbade92b0b285dbe6",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/403d659f268e428dbade92b0b285dbe6",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/403d659f268e428dbade92b0b285dbe6",
  "x5t": "ezwbNw0GTp5SYPr4a2m3wRuTiec",
  "cer": "MIIB2TCCAX6gAwIBAgIQLa+sjeNeSz+5V9aqnzTCAjAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjMwMTA1MTY1MzA3WhcNMjQwMTA1MTcwMzA3WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARuPh6D+cEryBgKXjgJCsN6M12NPTVdMW+9RuaPbc4jVYJbeRJLmlXTcbON00obrF/DN/by3hyz6Ctpls0lFYSHo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUwBOMdVt8Nq+dwzPsICk25C/WdY0wHQYDVR0OBBYEFMATjHVbfDavncMz7CApNuQv1nWNMAoGCCqGSM49BAMCA0kAMEYCIQD7kX7lqarsas9J1PuNADtAI0/Sp+A0FO6YYAqNA1MLOgIhAPzP3XaEMlogccgt35xzZJxdmPqt6coCoAUoavxCuXVd",
  "attributes": {
    "enabled": true,
    "nbf": 1672937587,
    "exp": 1704474187,
    "created": 1672938187,
    "updated": 1672938187,
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
      "updated": 1672938173
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
