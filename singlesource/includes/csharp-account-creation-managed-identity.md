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
var managedIdentity = new ResourceIdentifier(
    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources" +
    "/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity");

var mediaAccount = (await resourceGroup.GetMediaAccounts().CreateOrUpdateAsync(
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
    })).Value;
```
