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
  "tags": {
    "department": "studios",
    "cost-center": "marketing"
  },
  "location": "global",
  "properties": {
    "dataLocation": "United States"
  }
}

201 Created
Date:Wed, 09 Nov 2022 17:29:52 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "myaccount",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount",
  "type": "Microsoft.Media/mediaStreamAccounts",
  "location": "global",
  "tags": {
    "department": "studios",
    "cost-center": "marketing"
  },
  "properties": {
    "accountId": "814ea641-c2a7-498b-a5ba-cf723bbeb73c",
    "dataLocation": "United States",
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
