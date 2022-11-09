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
POST https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources/providers/Microsoft.Media/mediaStreamAccounts/myaccount/mediaStreams/mymovie/startUpload?api-version=2023-03-03
Accept:application/json
Authorization:REDACTED
Content-Type:application/json

{}

200 OK
Date:Wed, 09 Nov 2022 17:31:00 GMT
Content-Type:application/json; odata.metadata=none

{
  "uploadUri": "https://mediastore.blob.core.windows.net/asset-100?sp=cw&st=2022-11-01T00:00:00Z&se=2022-11-01T02:00:00Z&spr=https&sv=2021-06-08&sr=c&sig=REDACTED"
}

```
