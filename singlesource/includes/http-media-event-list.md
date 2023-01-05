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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaEvents?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Thu, 05 Jan 2023 17:02:43 GMT
Content-Type:application/json; odata.metadata=none

{
  "value": [
    {
      "name": "myevent",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaEvents/myevent",
      "type": "Microsoft.Media/mediaAccounts/mediaEvents",
      "properties": {
        "provisioningState": "Succeeded",
        "streamState": "Live",
        "rtmps": {
          "enabled": true,
          "ingestUri": "rtmps://rtmp.ingest.media.azure.com/967721b3-689a-bf0a-4aad-a3d63999c61c?key=69c749ea-22e0-6ad5-d3be-c4e067a10a63"
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
