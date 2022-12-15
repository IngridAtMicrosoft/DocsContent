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
POST https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/startWebIngest?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "autoStopDelay": "PT5M"
}

200 OK
Date:Thu, 15 Dec 2022 23:14:04 GMT
Content-Type:application/json; odata.metadata=none

{
  "ingestUri": "https://webrtc.ingest.azure.media.net/a15e2ed0-8524-41e6-b074-1b759177ce22?key=b4e3567447a3219c7313"
}

```
