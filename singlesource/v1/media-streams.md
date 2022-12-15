---
title: Media Streams
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Streams

Media streams store media and define how the media can be streamed. A media account may contain up to one million media stream resources.

> [!NOTE]
> Media streams combine the Media Services asset, streaming locator, and streaming endpoint resources. Unlike Media Services
accounts, there is no need to manage storage resources and CDNs used to store and stream media.

When a viewer watches a media stream, Media Services automatically adapts the media data to match the viewer's playback device capabilities
and network bandwidth. The selection of the streaming protocol (HLS, low-latency HLS, or DASH), media codec, and media bitrate are all
managed by Media Services.

Each media stream contains a collection of **outputs** which describe how the content may be accessed. A media stream may define multiple
outputs to preset the same content in multiple ways (for example, using different authentication options for different groups of users).

## Creating a media stream

Media streams can be created using the Azure Portal, ARM templates, client SDKs, or using HTTP requests. The request to create a media
stream specifies the outputs for the stream; the media stream creation response includes the streaming URLs for each output.

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media stream creation:

[!INCLUDE [<csharp-media-stream-rtmp-create>](../includes/csharp-media-stream-rtmp-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-rtmp-create](../includes/http-media-stream-rtmp-create.md)]

---

## Media stream operations

### Updating a media stream

Media streams can be updated to add or remove outputs. The enabled property of outputs may also be updated.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-update>](../includes/csharp-media-stream-update.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-update](../includes/http-media-stream-update.md)]

---

### Listing media streams

Media streams may be listed using the service API.

> [!NOTE]
> The API does not provide support for filtering or sorting lists of media streams. If your application requires a large number
of media streams, consider using a database to store media stream metadata.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-list>](../includes/csharp-media-stream-list.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-list](../includes/http-media-stream-list.md)]

---

### Deleting a media stream

Deleting a media stream deletes the media associated with the stream, stops any RTMP input, and disables streaming from
each of the outputs defined in the media stream.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-delete>](../includes/csharp-media-stream-delete.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-delete](../includes/http-media-stream-delete.md)]

---

## Media stream limits and billing

A media account may have up to one million media streams. Media streams are billed for the number of minutes of content stored,
the number of minutes of ingest, and the number of minutes of content streamed.