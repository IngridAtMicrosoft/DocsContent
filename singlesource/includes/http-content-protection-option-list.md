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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtectionOptions?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Mon, 07 Nov 2022 17:39:37 GMT
Content-Type:application/json; odata.metadata=none

{
  "value": [
    {
      "name": "protection-option-1",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtectionOptions/protection-option-1",
      "type": "Microsoft.Media/mediaAccounts/mediaProtectionOptions",
      "properties": {
        "provisioningState": "Succeeded",
        "tokenValidation": {
          "tokenSigningCertificateIdentifier": "https://mykeys.vault.azure.net/certificates/content-protection-token-certificate-2",
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
  ]
}

```
