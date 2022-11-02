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
POST https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/stopRtmpIngest?api-version=2023-01-01
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{}

200 OK
Date:Tue, 01 Nov 2022 23:11:01 GMT
Content-Type:application/json; odata.metadata=none

{}

```
