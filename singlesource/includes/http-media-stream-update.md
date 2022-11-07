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
PATCH https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "properties": {
    "outputs": {
      "output2": {
        "enabled": true
      }
    }
  }
}

200 OK
Date:Mon, 07 Nov 2022 17:39:38 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "mymovie",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie",
  "type": "Microsoft.Media/mediaAccounts/mediaStreams",
  "properties": {
    "provisioningState": "Succeeded",
    "streamState": "OnDemand",
    "outputs": {
      "output2": {
        "enabled": true,
        "streamingUri": "https://stream.azure.media.net/0b8d316b-e1d6-4a35-a865-1edecec7b28d"
      },
      "output1": {
        "enabled": true,
        "streamingUri": "https://stream.azure.media.net/2ddc6abd-2d3d-4b30-a696-754bb90d3a8a"
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
