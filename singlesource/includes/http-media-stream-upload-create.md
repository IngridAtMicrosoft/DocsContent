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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount/mediaStreams/mymovie?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "properties": {
    "outputs": {
      "output1": {
        "enabled": true
      }
    }
  }
}

201 Created
Date:Wed, 09 Nov 2022 17:31:00 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "mymovie",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount/mediaStreams/mymovie",
  "type": "Microsoft.Media/mediaStreamAccounts/mediaStreams",
  "properties": {
    "provisioningState": "Succeeded",
    "streamState": "Idle",
    "outputs": {
      "output1": {
        "enabled": true,
        "streamingUri": "https://stream.azure.media.net/8bcfcbb1-0c01-6717-6eb5-872e8e7faa30"
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
  }
}

```
