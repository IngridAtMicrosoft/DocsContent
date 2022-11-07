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
PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "properties": {
    "outputs": {
      "outputWithLogoOverlay": {
        "enabled": true,
        "mediaProtectionOptionId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtectionOptions/protection-option-subscriber",
        "streamOverlay": {
          "image": "logo.jpg",
          "position": {
            "left": 50,
            "top": 50,
            "width": 200,
            "height": 90
          }
        }
      },
      "outputWithPreviewTextOverlay": {
        "enabled": true,
        "streamOverlay": {
          "image": "logo.jpg",
          "position": {
            "left": 50,
            "top": 50,
            "width": 200,
            "height": 90
          }
        }
      }
    }
  }
}

201 Created
Date:Mon, 07 Nov 2022 23:39:50 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "mymovie",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie",
  "type": "Microsoft.Media/mediaAccounts/mediaStreams",
  "properties": {
    "provisioningState": "Succeeded",
    "streamState": "Idle",
    "outputs": {
      "outputWithPreviewTextOverlay": {
        "enabled": true,
        "streamingUri": "https://stream.azure.media.net/2ddc6abd-2d3d-4b30-a696-754bb90d3a8a",
        "streamOverlay": {
          "image": "logo.jpg",
          "position": {
            "left": 50,
            "top": 50,
            "width": 200,
            "height": 90
          }
        }
      },
      "outputWithLogoOverlay": {
        "enabled": true,
        "mediaProtectionOptionId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtectionOptions/protection-option-subscriber",
        "contentKeyId": "47f91083-74b4-455a-8d9b-86efbc86e0b0",
        "streamingUri": "https://stream.azure.media.net/2ddc6abd-2d3d-4b30-a696-754bb90d3a8a",
        "streamOverlay": {
          "image": "logo.jpg",
          "position": {
            "left": 50,
            "top": 50,
            "width": 200,
            "height": 90
          }
        }
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
