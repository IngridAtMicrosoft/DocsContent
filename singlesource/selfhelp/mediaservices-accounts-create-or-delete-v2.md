---
articleid: "apollo-mediaservices-accounts-create-or-delete"
cloudenvironments: "blackforest,fairfax,mooncake,public,usnat,ussec"
description: "Azure Media Services accounts can be created or deleted directly in the portal, using the Azure CLI (cloud shell or local), or by using the REST API and one of the many client libraries. Follow the recommended steps."
ms.author: inhenkel
ownershipid: "StorageMediaEdge_Media"
title:  "Learn to create or delete an Azure Media Services account"
problemids: ""
productpesids: "14885"
resourcerequired: "False"
resourcetags:
selfhelptype: "apollo"
supporttopicids: "45383072-cde0-c5cd-c5f9-330714cc0f49"
author: IngridAtMicrosoft
ms.service: media-services
---
# Azure Media Services v2 account creation and deletion

## Create or delete an Azure Media Services account

Azure Media Services accounts can be created or deleted directly in the portal using the Azure CLI (cloud shell or local), or by using the REST API and one of the many client libraries.


### Create or delete an Azure Media Services account with the CLI and connect to the API

1. [Create a new Media Services account with the Azure CLI or cloud shell](https://docs.microsoft.com/azure/media-services/latest/account-create-how-to?tabs=portal).
2. [Use Azure CLI to create an Azure AD app and configure it to access Media Services API](https://docs.microsoft.com/azure/media-services/previous/media-services-cli-create-and-configure-aad-app).
3. Start [developing with client SDKs](https://docs.microsoft.com/azure/media-services/latest/all-sdks) like .NET, Java, Node.js, Python, Go, or Ruby.

### Create a Media Services account using the CLI

Open the Cloud Shell or CLI locally and run the following command to see the available options:

```
az ams account create -h
```

### Delete a Media Services account using the CLI

Open the Cloud Shell or CLI locally and run the following command to see the available options:

```
az ams account delete -h
```

### Resources

* [Azure Media Services v3 overview](https://docs.microsoft.com/azure/media-services/latest/media-services-overview)
* [Create a new Media Services account](https://docs.microsoft.com/azure/media-services/latest/account-create-how-to)

### Here are some relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
