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
          "image": "freetrial.jpg",
          "position": {
            "left": 0,
            "top": 0,
            "width": 1920,
            "height": 1080
          }
        }
      }
    }
  }
}

201 Created
Date:Tue, 08 Nov 2022 18:02:16 GMT
Content-Type:application/json; odata.metadata=none

{
  "name": "mymovie",
  "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie",
  "type": "Microsoft.Media/mediaAccounts/mediaStreams",
  "properties": {
    "provisioningState": "Succeeded",
    "streamState": "Idle",
    "outputs": {
      "outputWithLogoOverlay": {
        "enabled": true,
        "mediaProtectionOptionId": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaProtectionOptions/protection-option-subscriber",
        "contentKeyId": "0cf9b8d1-a3e1-ac8e-aff4-9b43eb0e68a8",
        "streamingUri": "https://stream.azure.media.net/15cbc6b7-a668-7e18-bce5-c02000a1c5a0",
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
        "streamingUri": "https://stream.azure.media.net/919de0bf-73de-48d5-8118-53b007a41d6f",
        "streamOverlay": {
          "image": "freetrial.jpg",
          "position": {
            "left": 0,
            "top": 0,
            "width": 1920,
            "height": 1080
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
