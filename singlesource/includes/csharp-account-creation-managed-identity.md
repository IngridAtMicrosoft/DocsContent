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

```csharp
var managedIdentity = new ResourceIdentifier(
    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources" +
    "/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity");

var account = await resourceGroup.GetMediaAccounts().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "myaccount",
    new MediaAccountData("global")
    {
        Identity = new ManagedServiceIdentity(ManagedServiceIdentityType.UserAssigned)
        {
            UserAssignedIdentities = { { managedIdentity, new UserAssignedIdentity() } }
        },
        DataLocation = AzureLocation.WestUS,
        PublicNetworkAccess = PublicNetworkAccess.Disabled
    });
```
