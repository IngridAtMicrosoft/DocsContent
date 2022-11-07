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
Date:Mon, 07 Nov 2022 17:39:16 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending",
  "issuer": {
    "name": "Self"
  },
  "csr": "MIIBNTCB3AIBADAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQQDrnjA2IG1Ptbsy65yfa8lhjm1KZRbNH+51HHb3MdPSW1cPs8kAINCQOvf4NMOwxOnZD6vDmEokikmQzfxmUooEswSQYJKoZIhvcNAQkOMTwwOjAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAkGA1UdEwQCMAAwCgYIKoZIzj0EAwIDSAAwRQIgCPxU+xjLUEpbphvE2UVrmMReCMkElLlALvh9+K85mxwCIQCN3CkCXTZ+DD4DULGZnv/dc/jpaJMrlK2k+BHGiXKmVA==",
  "cancellation_requested": false,
  "status": "inProgress",
  "status_details": "Pending certificate created. Certificate request is in progress. This may take some time based on the issuer provider. Please check again later.",
  "request_id": "265d1ea8392b43139cf9a3bea7f2da6f"
}

GET https://mykeys.vault.azure.net/certificates/content-protection-token-certificate?api-version=7.3
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

200 OK
Date:Mon, 07 Nov 2022 17:39:37 GMT
Content-Type:application/json; charset=utf-8

{
  "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/4afe399b97444b18b2a96aac136abb6a",
  "kid": "https://mykeys.vault.azure.net/keys/content-protection-token-certificate/4afe399b97444b18b2a96aac136abb6a",
  "sid": "https://mykeys.vault.azure.net/secrets/content-protection-token-certificate/4afe399b97444b18b2a96aac136abb6a",
  "x5t": "asGQ8S-ojeQ-9kgUGGeHM9MkIGA",
  "cer": "MIIB1zCCAX6gAwIBAgIQHK4vZqiNS7ybCb8H0NcXrzAKBggqhkjOPQQDAjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwHhcNMjIxMTA3MTcyOTM0WhcNMjMxMTA3MTczOTM0WjAvMS0wKwYDVQQDEyRjb250ZW50LXByb3RlY3Rpb24tdG9rZW4tY2VydGlmaWNhdGUwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQQDrnjA2IG1Ptbsy65yfa8lhjm1KZRbNH+51HHb3MdPSW1cPs8kAINCQOvf4NMOwxOnZD6vDmEokikmQzfxmUoo3wwejAOBgNVHQ8BAf8EBAMCB4AwCQYDVR0TBAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0jBBgwFoAUOK8RIvHpVrpCoKLVpHb2dOOVhDYwHQYDVR0OBBYEFDivESLx6Va6QqCi1aR29nTjlYQ2MAoGCCqGSM49BAMCA0cAMEQCIBfCJXVNFg1kREx+A9p+rZWQ5hAgPBtpVnnUAKjxryDIAiBB12NYcB4dKEiPtqouv1W/t+6JFWymiex0k69DlBai9Q==",
  "attributes": {
    "enabled": true,
    "nbf": 1667842174,
    "exp": 1699378774,
    "created": 1667842774,
    "updated": 1667842774,
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
      "updated": 1667842756
    }
  },
  "pending": {
    "id": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/pending"
  }
}

```
