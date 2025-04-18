---
title: Media Services v3 Assets samples
description: This article contains a list of all the samples available for Media Services Assets in Node.JS, Python, and Java.
author: IngridAtMicrosoft
ms.service: azure-monitor
ms.topic: overview
ms.date: 01/26/2023
ms.author: inhenkel
---

# Media Services v3 Assets samples

This article contains a list of all the samples available for Media Services Assets.

## List assets

A basic example of how to connect and list assets.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/HelloWorld-ListAssets/list-assets.ts)| | python | java |

## Get the storage contain from an asset

Demonstrates how to find the Azure storage account container used to store the contents of this asset. This can be used to then edit sources, modify, or copy contents using the Azure storage SDK library.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/get-container-from-asset.ts)| python | java |

## List assets using filters

Use filters in your list assets calls to find assets by date and order them.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-assets-filtered.ts)| python | Java |

## List the streaming locators on an asset using filters

Use filters to list the streaming locators attached to your assets.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-assets-filtered.ts)| python | java |

## List tracks in an asset

Use the tracks collection to list all of the track names and track types (audio, video, or text) available on an asset

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-tracks-in-asset.ts)| |  python | java |

## Add a WebVTT/IMSC1/TTML subtitle or caption to an existing asset

Use the tracks API on an Asset to add a new WebVTT or TTML/IMSC1 text profile caption or subtitle to an existing asset

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/add-WebVTT-tracks.ts)| python | java |

## Add an additional audio track to an existing asset using the Tracks API

Use the tracks API on an Asset to add an additional audio language or descriptive audio track to an existing asset. This sample demonstrates how to upload, encode using content aware encoding, and then late bind an additional audio track for a new language to the asset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/add-audio-language-track.ts)| python | java |

