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
        "useSystemAssignedIdentity": true
      }
    }
  }
}

201 Created
Date:Thu, 27 Oct 2022 22:39:17 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "global",
  "tags": {},
  "properties": {
    "accountId": "f32d5b0b-bc48-48f2-8049-e9fd192abc8e",
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
        "useSystemAssignedIdentity": true
      }
    }
  },
  "identity": {
    "type": "UserAssigned",
    "userAssignedIdentities": {
      "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity": {
        "clientId": "a338b9ef-fd65-4a05-a5f2-c333ad37226a",
        "principalId": "050d1d3d-bb9a-48c7-bcae-624223a5d807"
      }
    }
  }
}

```
