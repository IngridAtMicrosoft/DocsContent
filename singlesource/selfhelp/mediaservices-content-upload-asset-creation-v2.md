---
title: Create an Asset v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-content-upload-asset-creation"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="You need to create an Asset if you want to encode or analyze your on-demand content, or if you have a Live Output that is associated with an Asset. A Live Output uses an Asset to store recorded videos."
  ms.author="juliako,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Create an Asset"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="4fd1b35e-df2d-4bd0-01a4-c03527ad5c1e" />

-->

# Create an Asset v2

## Create an Asset
You need to create an Asset if you want to encode or analyze your on-demand content, or if you have a Live Output that is associated with an Asset. A Live Output uses an Asset to store recorded videos.

Use our guidance to learn how to upload digital files, create a new asset, and more.

**NOTE:** This topic references Media Services v3 API documentation. v3 is the latest Media Services version.


### Upload digital files into Assets

The following steps describe how to upload a file and then encode or analyze the uploaded file. [Learn more about asset uploads](/azure/media-services/latest/asset-upload-media-how-to?tabs=portal).<br>

1. Use the Media Services v3 API to create a new "input" Asset. This operation creates a container in the storage account associated with your Media Services account. The API returns the container name (for example: `"container": "asset-b8d8b68a-2d7f-4d8c-81bb-8c7bbbe67ee4"`). If you already have a blob container that you want to associate with an Asset, you can specify the container name when creating the Asset. Media Services currently only supports blobs in the container root and without paths in the file name. Thus, a container with the `input.mp4` file name will work, whereas a container with a name of `videos/inputs/input.mp4` will not work.

	You can use the Azure CLI to upload directly to any storage account and container that you have rights to in your subscription.

	The container name must be unique and follow storage naming guidelines. The name doesn't have to follow the Media Services Asset container name (Asset-GUID) formatting. `az storage blob upload -f /path/to/file -c MyContainer -n MyBlob`.<br>

2. Get an SAS URL with read-write permissions that will be used to upload digital files into the Asset container. You can use the Media Services API to [list the asset container URLs](/rest/api/media/assets/listcontainersas).<br>
3. Use the Azure Storage APIs or SDKs (for example, the [Storage REST API](/azure/storage/common/storage-rest-api-auth), [JAVA SDK](/azure/storage/blobs/storage-quickstart-blobs-java-v10), or [.NET SDK](/azure/storage/blobs/storage-quickstart-blobs-dotnet?tabs=windows)) to upload files into the Asset container.<br>
4. Use Media Services v3 APIs to create a transform and a job to process your "input" Asset. See [Transforms and Jobs](/azure/media-services/latest/transforms-jobs-concept).

### Create a new asset

**REST**

```
    PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{amsAccountName}/assets/{assetName}?api-version=2018-07-01
```

Also, see [Create an Asset with REST](/rest/api/media/assets/createorupdate#examples). The example shows how to create the **Request Body** where you can specify useful information like description, container name, storage account, and other information.

**cURL**

```
    curl -X PUT \
      'https://management.azure.com/subscriptions/00000000-0000-0000-000000000000/resourceGroups/resourceGroupName/providers/Microsoft.Media/mediaServices/amsAccountName/assets/myOutputAsset?api-version=2018-07-01' \
      -H 'Accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "properties": {
        "description": "",
      }
    }'
```

**.NET**

```
    Asset asset = await client.Assets.CreateOrUpdateAsync(resourceGroupName, accountName, assetName, new Asset());
```

Also, see [.NET example](/azure/media-services/latest/job-input-from-local-file-how-to).

### Resources

* [Encoding with Media Services v3](/azure/media-services/latest/encoding-concept)<br>
* [Assets Overview](/azure/media-services/latest/assets-concept)<br>
* [API Access](/azure/media-services/latest/access-api-howto?tabs=portal)<br>
* [AMS API Functions List](/cli/azure/ams?view=azure-cli-latest)<br>
* [Using a cloud DVR](/azure/media-services/latest/live-event-cloud-dvr)<br>
* [Tutorial: Encode a remote file based on URL and stream the video - REST](/azure/media-services/latest/stream-files-tutorial-with-rest)

<!--### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>-->