---
title: Media Streams
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 01/01/2023
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 01/01/2023
ms.service: media-services
---

# Media Streams

Media streams can be used to stream live and recorded media. Media Services manages the storage and streaming resources for streaming.
A media account may contain up to one million media stream resources.

> [!NOTE]
> Media streams combine the Media Services asset, streaming locator, streaming endpoint and live event resources. Unlike Media Services
accounts, there is no need to manage storage resources and CDNs used to store and stream media.

When a viewer watches a media stream, Media Services automatically adapts the media data to match the viewer's playback device capabilities
and network bandwidth. The selection of the streaming protocol (HLS, low-latency HLS, or DASH), media codec, and media bitrate are all
managed by Media Services.

Each media stream contains a collection of **outputs** which describe how the content may be accessed. A media stream may define multiple
outputs if different groups of viewers access the stream in different ways (for example, using different authentication options).

## Creating a media stream

Media streams can be created using the Azure Portal, ARM templates, client SDKs, or using HTTP requests. The request to create a media
stream specifies the outputs for the stream; the media stream creation response includes the streaming URLs for each output.

#### [C#](#tab/csharp/)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media stream creation:

[!INCLUDE [<csharp-account-creation>](../includes/csharp-media-stream-rtmp-create.md)]

#### [HTTP](#tab/http/)

[!INCLUDE [<http-account-creation](../includes/http-media-stream-rtmp-create.md)]

---

## Streaming media to a media stream using RTMP

After creating a media stream, you can stream media to the stream using RTMP.

#### [C#](#tab/csharp/)

[!INCLUDE [<csharp-account-creation>](../includes/csharp-media-stream-start-rtmp-ingest.md)]

#### [HTTP](#tab/http/)

[!INCLUDE [<http-account-creation](../includes/http-media-stream-start-rtmp-ingest.md)]

---

The response from the service contains the RTMP ingest URL. This can be used with source encoders to
stream to the media stream.

#### [Streaming with OBS]

![Media Services resources](../media/obs.png)

#### [Streaming with ffmpeg]

```cmd
ffmpeg `
  -re `
  -i myvideo.mp4 `
  -c:v libx264 `
  -c:v aac `
  -f flv rtmps://rtmp.ingest.azure.media.net/a15e2ed0-8524-41e6-b074-1b759177ce22?key=b4e3567447a3219c7313
```

---


- outputs define ways of streaming videos
- example using rtmp source
- no support for queries

