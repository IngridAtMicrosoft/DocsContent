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
    "publicNetworkAccess": "Disabled"
  }
}

201 Created
Date:Tue, 01 Nov 2022 21:31:47 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "global",
  "tags": {},
  "properties": {
    "accountId": "76ea5ffa-890e-4283-be36-3124603a8a50",
    "dataLocation": "westus",
    "publicNetworkAccess": "Disabled",
    "provisioningState": "Succeeded"
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
        "clientId": "e43ffa00-9867-4766-8584-28fd67bb0a35",
        "principalId": "b24091cf-e12b-492b-9814-85ab0e292315"
      }
    }
  }
}

```
