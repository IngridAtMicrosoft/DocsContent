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
POST https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaAccounts/myaccount/mediaStreams/mymovie/stopWebIngest?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{}

200 OK
Date:Mon, 07 Nov 2022 18:12:47 GMT
Content-Type:application/json; odata.metadata=none

{}

```
