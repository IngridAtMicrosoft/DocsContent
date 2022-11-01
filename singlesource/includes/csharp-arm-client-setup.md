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

```csharp
const string SubscriptionId = "00000000-0000-0000-0000-000000000000";
const string ResourceGroupName = "myResources";

var credential = new DefaultAzureCredential();
var armClient = new ArmClient(credential);

var resourceGroup = armClient.GetResourceGroupResource(
    ResourceGroupResource.CreateResourceIdentifier(SubscriptionId, ResourceGroupName));
```
