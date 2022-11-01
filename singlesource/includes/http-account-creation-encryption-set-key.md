---
title: include file
description: include file
author: jonpayne
ms.topic: include
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
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
Date:Tue, 01 Nov 2022 15:43:36 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "global",
  "tags": {},
  "properties": {
    "accountId": "ab21141b-b123-4501-bc64-3a3314bceec1",
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
        "clientId": "d5576630-14e0-4551-889e-235dd928288d",
        "principalId": "fdf87c84-82ce-431d-900e-3f68415c7917"
      }
    }
  }
}

```
