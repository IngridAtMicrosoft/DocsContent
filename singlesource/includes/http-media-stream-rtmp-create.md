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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie?api-version=2023-01-01
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
Date:Tue, 01 Nov 2022 18:19:11 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "mymovie",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie",
  "type": "Microsoft.Media/mediaAccounts/mediaStreams",
  "properties": {
    "provisioningState": "Succeeded",
    "streamState": "Idle",
    "outputs": {
      "output1": {
        "enabled": true,
        "streamingUri": "https://stream.azure.media.net/a15e2ed0-8524-41e6-b074-1b759177ce22"
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
