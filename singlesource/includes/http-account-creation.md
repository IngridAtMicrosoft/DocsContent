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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/test1?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "tags": {},
  "location": "westus",
  "properties": {}
}

201 Created
Date:Thu, 27 Oct 2022 19:43:29 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "test1",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/test1",
  "type": "Microsoft.Media/mediaAccounts",
  "location": "westus",
  "tags": {},
  "properties": {
    "accountId": "00000000-0000-0000-0000-000000000000",
    "dataLocation": null,
    "provisioningState": "Succeeded"
  }
}

```
