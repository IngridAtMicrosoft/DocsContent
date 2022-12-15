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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Thu, 15 Dec 2022 23:12:41 GMT
Content-Type:application/json; odata.metadata=none

{
  "value": [
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
            "streamingUri": "https://stream.azure.media.net/1db9df34-899c-bf6f-b419-2e4111a8135a"
          },
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
  ]
}

```
