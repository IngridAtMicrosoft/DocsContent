---
title: Azure Media Services linking and managing storage accounts
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-accounts-linking-storage-accts"
  cloudenvironments="public,fairfax,usnat,ussec"
  description="Azure Media Services supports multiple storage accounts. You can link an existing storage account, or create a new storage account prior to the creation of your Media Services account and pass it in to the create call. Learn to do this by following recommended steps."
  ms.author="johndeu,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Learn to link and manage storage accounts in Azure Media Services"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="1b279143-929c-86e1-4c6c-18bc6a7fe2c5" />-->

# Azure Media Services linking and managing storage accounts v2

## Link and manage storage accounts in Azure Media Services

Azure Media Services supports multiple storage accounts. You can link an existing storage account, or create a new storage account prior to the creation of your Media Services account and pass it in to the create call.

The Media Services account and all associated storage accounts must be in the same Azure subscription. We strongly recommend using storage accounts in the same location as the Media Services account to avoid additional latency and data egress costs.

Follow these instructions on how to create a new Media Services account with a new storage account - [Create an Azure Media Services account with storage accounts](/azure/media-services/latest/create-account-cli-how-to#create-a-storage-account)

### Add a storage account to your Media Services account using the CLI

1. Open the Cloud Shell or CLI locally and run the following command to see the options:

   ```
   az ams account storage -h
   ```

2. To attach a "secondary" storage account, use the following CLI command to see the options:

   ```
   az ams account storage add -h
   ```

3. To remove a "secondary" storage account, use the following CLI command to see the options:

   ```
   az ams account storage remove -h
   ```

### Troubleshoot access issues with linked storage accounts

It is possible for keys to be rotated on a storage account and get out of sync with the Media Services account. To forces a resync of the storage keys, run the following CLI command to see the options.

```
az ams account storage sync-storage-keys -h
```

### Resources

* [Azure Media Services v3 overview](/azure/media-services/latest/media-services-overview)
* [Cloud upload and storage](/azure/media-services/latest/storage-account-concept)
* [Create an Azure Media Services account with storage accounts](/azure/media-services/latest/create-account-cli-how-to#create-a-storage-account)

<!--### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>-->
