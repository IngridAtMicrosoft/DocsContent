---
title: Streaming endpoint v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: azure-monitor
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-stream-files-streaming-endpoints"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Streaming endpoints"
  isofficial="True"
  ms.author="juliako,inhenkel,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Streaming endpoints"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="16c919c7-e8da-2796-4e7d-69f69fac0e1a" />
-->

# Streaming endpoint v2

## Learn about Streaming endpoints

A common Media Services scenario is to encode your content and stream files using different streaming formats and content protection formats to a variety of client technologies (for example, iOS and XBOX).

[Streaming Endpoints](/azure/media-services/latest/stream-streaming-endpoint-concept) is the dynamic packaging and streaming service in Media Services used to deliver media content to client players or to a Content Delivery Network (CDN) for further distribution. Dynamic Packaging is a feature that comes standard on all streaming endpoints (Standard or Premium).

**Dynamic Packaging**

To take advantage of Dynamic Packaging, you need to have an Asset with a set of adaptive bitrate MP4 files and streaming configuration files needed by Media Services Dynamic Packaging. Encode your mezzanine (source) file with Media Services to get the files. The encoding job will produce an output Asset.

**Making videos available to clients**

To make videos in the output Asset available to clients for playback, you have to create a Streaming Locator and build streaming URLs. When creating the Streaming Locator, in addition to the Asset's name, you need to specify a Streaming Policy. Streaming Policies enable you to define streaming protocols and encryption options (if any) for your Streaming Locators.

Based on the specified format in the streaming client manifest (HLS, DASH, or Smooth), your clients can receive the stream in the chosen protocol.

**Delivery Protocols**

|Protocol|Example|
|---|---|
|HLS V4	|`https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest(format=m3u8-aapl)`|
|HLS V3	|`https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest(format=m3u8-aapl-v3)`|
|HLS CMAF| `https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest(format=m3u8-cmaf)`|
|MPEG DASH CSF| `https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest(format=mpd-time-csf)` |
|MPEG DASH CMAF|`https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest(format=mpd-time-cmaf)` |
|Smooth Streaming| `https://amsv3account-usw22.streaming.media.azure.net/21b17732-0112-4d76-b526-763dcd843449/ignite.ism/manifest`|

### Resources

* [Troubleshooting Guide](/azure/media-services/latest/troubleshooting) <br>
* [Streaming Endpoints](/azure/media-services/latest/stream-streaming-endpoint-concept)<br>
* [Dynamic packaging](/azure/media-services/latest/encode-dynamic-packaging-concept)<br>
* [Tutorial: Upload, encode, and stream videos using .NET](/azure/media-services/latest/stream-files-tutorial-with-api)<br>
* [Download the results from the specified output asset](https://github.com/Azure-Samples/media-services-v3-dotnet-tutorials/blob/master/AMSV3Tutorials/UploadEncodeAndStreamFiles/Program.cs#L464)


<!--### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>-->
