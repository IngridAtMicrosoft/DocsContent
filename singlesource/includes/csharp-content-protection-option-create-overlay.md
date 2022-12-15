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
var mediaAccount = armClient.GetMediaAccountResource(
    MediaAccountResource.CreateResourceIdentifier(
        subscriptionId: "00000000-0000-0000-0000-000000000000",
        resourceGroupName: "myResources",
        mediaAccountName: "myaccount"));

var managedIdentity = new ResourceIdentifier(
    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResources" +
    "/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myIdentity");

var mediaProtection = (await mediaAccount.GetMediaProtections().CreateOrUpdateAsync(
    WaitUntil.Completed,
    "protection-option-subscriber",
    new MediaProtectionData
    {
        TokenValidation = new TokenRestriction
        {
            TokenSigningCertificateIdentifier = certificateUri,
            Identity = new ResourceIdentity(useSystemAssignedIdentity: false)
            {
                UserAssignedIdentity = managedIdentity
            }
        },
        ClearKeyEnabled = true
    })).Value;
```
