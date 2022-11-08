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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtections/protection-option-1?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "properties": {
    "tokenValidation": {
      "tokenSigningCertificateIdentifier": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate",
      "identity": {
        "userAssignedIdentity": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity",
        "useSystemAssignedIdentity": false
      }
    },
    "clearKey": {
      "enabled": true
    }
  }
}

201 Created
Date:Tue, 08 Nov 2022 18:32:30 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "protection-option-1",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtections/protection-option-1",
  "type": "Microsoft.Media/mediaAccounts/mediaProtections",
  "properties": {
    "provisioningState": "Succeeded",
    "tokenValidation": {
      "tokenSigningCertificateIdentifier": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate",
      "currentTokenSigningCertificateIdentifier": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate/00000000000000000000000000000000",
      "identity": {
        "userAssignedIdentity": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity",
        "useSystemAssignedIdentity": false
      }
    },
    "clearKey": {
      "enabled": true
    }
  },
  "systemData": {
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "createdByType": "Application",
    "createdAt": "2023-01-01T00:00:00Z",
    "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
    "lastModifiedByType": "Application",
    "lastModifiedAt": "2023-01-01T00:00:00Z"
  }
}

```
