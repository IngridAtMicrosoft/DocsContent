---
title: Managed Account Creation
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 01/01/2023
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 01/01/2023
ms.service: media-services
---

# Managed Account Creation

Start

#### [Windows](#tab/windows/)

```powershell
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -NoProxy -Uri "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64
```

`-NoProxy` requires PowerShell V6 or greater. See our [samples repository](https://github.com/microsoft/azureimds) for examples with older PowerShell versions.

#### [Linux](#tab/linux/)

```http
PUT https://{{armEndpoint}}/subscriptions/{{subscription}}/resourceGroups/{{resourceGroup}}?api-version=2016-09-01
Authorization: Bearer (token)
Content-Type: application/json; charset=utf-8

{
    "location": "{{location}}xxx"
}
```

The `jq` utility is available in many cases, but not all. If the `jq` utility is missing, use `| python -m json.tool` instead.

---