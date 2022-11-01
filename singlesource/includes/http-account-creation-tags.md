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
  "tags": {
    "department": "studios",
    "cost-center": "marketing"
  },
  "location": "global",
  "properties": {
    "dataLocation": "westus"
  }
}

201 Created
Date:Tue, 01 Nov 2022 21:55:23 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "global",
  "tags": {
    "department": "studios",
    "cost-center": "marketing"
  },
  "properties": {
    "accountId": "19988f26-c6dc-46f2-bea2-22fa3dbe82fb",
    "dataLocation": "westus",
    "provisioningState": "Succeeded"
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
