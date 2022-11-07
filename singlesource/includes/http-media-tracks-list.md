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
GET https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED

200 OK
Date:Mon, 07 Nov 2022 18:06:22 GMT
Content-Type:application/json; odata.metadata=none

{
  "value": [
    {
      "name": "video",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks/video",
      "type": "Microsoft.Media/mediaAccounts/mediaStreams/mediaTracks",
      "properties": {
        "provisioningState": "Succeeded",
        "videoTrack": {
          "bitRate": 120000
        }
      }
    },
    {
      "name": "audio-en",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks/audio-en",
      "type": "Microsoft.Media/mediaAccounts/mediaStreams/mediaTracks",
      "properties": {
        "provisioningState": "Succeeded",
        "audioTrack": {
          "displayName": "English",
          "languageCode": "en-EN",
          "mpeg4TrackId": 1,
          "bitRate": 11000
        }
      }
    },
    {
      "name": "audio-es",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks/audio-es",
      "type": "Microsoft.Media/mediaAccounts/mediaStreams/mediaTracks",
      "properties": {
        "provisioningState": "Succeeded",
        "audioTrack": {
          "displayName": "Spanish",
          "languageCode": "es-ES",
          "mpeg4TrackId": 2,
          "bitRate": 11000
        }
      }
    },
    {
      "name": "text-en",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks/text-en",
      "type": "Microsoft.Media/mediaAccounts/mediaStreams/mediaTracks",
      "properties": {
        "provisioningState": "Succeeded",
        "textTrack": {
          "displayName": "English",
          "languageCode": "en-EN",
          "playerVisibility": "Visible"
        }
      }
    },
    {
      "name": "text-es",
      "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/mediaTracks/text-es",
      "type": "Microsoft.Media/mediaAccounts/mediaStreams/mediaTracks",
      "properties": {
        "provisioningState": "Succeeded",
        "textTrack": {
          "displayName": "Spanish",
          "languageCode": "es-ES",
          "playerVisibility": "Visible"
        }
      }
    }
  ]
}

```
