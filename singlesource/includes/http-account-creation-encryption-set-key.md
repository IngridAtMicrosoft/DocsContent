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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "identity": {
    "type": "UserAssigned",
    "userAssignedIdentities": {
      "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity": {}
    }
  },
  "tags": {},
  "location": "global",
  "properties": {
    "dataLocation": "westus",
    "encryption": {
      "type": "CustomerKey",
      "keyVaultProperties": {
        "keyIdentifier": "https://mykeys.vault.azure.net/keys/account-encryption-key"
      },
      "identity": {
        "userAssignedIdentity": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity",
        "useSystemAssignedIdentity": false
      }
    }
  }
}

201 Created
Date:Mon, 31 Oct 2022 20:52:19 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "global",
  "tags": {},
  "properties": {
    "accountId": "18206f98-7aca-4ff7-8547-d6f981a53637",
    "dataLocation": "westus",
    "provisioningState": "Succeeded",
    "encryption": {
      "type": "CustomerKey",
      "keyVaultProperties": {
        "keyIdentifier": "https://mykeys.vault.azure.net/keys/account-encryption-key",
        "currentKeyIdentifier": "https://mykeys.vault.azure.net/keys/account-encryption-key/00000000000000000000000000000000"
      },
      "identity": {
        "userAssignedIdentity": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity",
        "useSystemAssignedIdentity": false
      }
    }
  },
  "systemData": {
    "createdBy": "00000000-0000-0000-0000-000000000000",
    "createdByType": "Application",
    "createdAt": "2023-01-01T00:00:00Z",
    "lastModifiedBy": "00000000-0000-0000-0000-000000000000",
    "lastModifiedByType": "Application",
    "lastModifiedAt": "2023-01-01T00:00:00Z"
  },
  "identity": {
    "type": "UserAssigned",
    "userAssignedIdentities": {
      "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity": {
        "clientId": "386a15aa-5c86-4e05-b783-0c2136300c1a",
        "principalId": "9b854d9b-5c94-47b6-84b4-108b17571715"
      }
    }
  }
}

```
