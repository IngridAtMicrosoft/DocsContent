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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Thu, 15 Dec 2022 23:12:41 GMT
Content-Type:application/json; odata.metadata=none

{
  "value": [
    {
      "name": "myaccount",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount",
      "type": "Microsoft.Media/mediaAccounts",
      "location": "global",
      "tags": {},
      "properties": {
        "accountId": "89b1e8a7-dacf-45d7-bffc-24cbaa197178",
        "dataLocation": "United States",
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
      }
    }
  ]
}

```
