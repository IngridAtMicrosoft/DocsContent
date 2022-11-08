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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount?api-version=2023-01-01
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
    "dataLocation": "United States",
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
Date:Tue, 08 Nov 2022 19:49:39 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount",
  "type": "Microsoft.Media/mediaStreamAccounts",
  "location": "global",
  "tags": {},
  "properties": {
    "accountId": "ceec671e-b803-4fc3-b0fe-66ceda190a78",
    "dataLocation": "United States",
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
        "clientId": "d2794670-c7cd-42a1-a102-0152ff0e0667",
        "principalId": "8750f1d6-3cfc-43dc-a8cc-6c80092100b7"
      }
    }
  }
}

```
