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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Tue, 01 Nov 2022 15:44:05 GMT
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
        "accountId": "96236504-8e7b-413f-997d-d8cff75cf492",
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
      }
    }
  ]
}

```
