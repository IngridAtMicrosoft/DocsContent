---
title: include file
description: include file
author: jonpayne
ms.topic: include
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

```http
POST https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/startRtmpIngest?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{
  "foo": "asdf"
}

200 OK
Date:Tue, 01 Nov 2022 15:44:05 GMT
Content-Type:application/json; odata.metadata=none

{
  "ingestUri": "https://rtmp.ingest.azure.media.net/a15e2ed0-8524-41e6-b074-1b759177ce22?key=b4e3567447a3219c7313"
}

```
