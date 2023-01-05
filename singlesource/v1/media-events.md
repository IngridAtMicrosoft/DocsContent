---
title: Media Events
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Events

Media events can be used to stream live media to a media stream.

## Creating a media event

Media events can be created using the Azure Portal, ARM templates, client SDKs, or using HTTP requests. The request to create a media
event specifies ingest protocol for the event.

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media event creation:

[!INCLUDE [<csharp-media-event-create>](../includes/csharp-media-event-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-event-create](../includes/http-media-event-create.md)]

---

## Using a media event to stream RTMP media to a media stream

After creating a media stream, you can stream media to the stream using RTMP.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-start-rtmp-ingest>](../includes/csharp-media-stream-start-rtmp-ingest.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-start-rtmp-ingest](../includes/http-media-stream-start-rtmp-ingest.md)]

---

The response from the service contains the RTMP ingest URL. This can be used with source encoders to
stream to the media stream.

#### [Streaming with OBS](#tab/obs)

![OBS stream setup](../media/obs.png)

#### [Streaming with ffmpeg](#tab/ffmpeg)

```powershell
ffmpeg `
  -re `
  -i myvideo.mp4 `
  -c:v libx264 `
  -c:v aac `
  -f flv rtmps://rtmp.ingest.azure.media.net/a15e2ed0-8524-41e6-b074-1b759177ce22?key=b4e3567447a3219c7313
```

---

## Getting the media stream status

When the media stream starts receiving RTMP data, the state of the media stream will change to `Live`.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-get>](../includes/csharp-media-stream-get.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-get](../includes/http-media-stream-get.md)]

---

## Live streaming

The live stream can be viewed using a player. Media can be streamed in a web page using Azure Media Player:

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <title>Playback</title>
  <link href="//amp.azure.net/libs/amp/latest/skins/amp-default/azuremediaplayer.min.css" rel="stylesheet">
  <script src="//amp.azure.net/libs/amp/latest/azuremediaplayer.min.js"></script>
</head>

<body>
  <video class="azuremediaplayer amp-default-skin" autoplay controls width="640" height="400">
    <source src="//stream.azure.media.net/8bcfcbb1-0c01-6717-6eb5-872e8e7faa30" type="application/vnd.ms-sstr+xml" />
</video>
</body>

</html>
```

![player](../media/player-live.png)

## Stopping a live stream

When a live stream is complete, RTMP ingest can be stopped. 

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-start-rtmp-ingest>](../includes/csharp-media-stream-stop-rtmp-ingest.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-start-rtmp-ingest](../includes/http-media-stream-stop-rtmp-ingest.md)]

---

When ingest is stopped, the media stream will transition to on-demand streaming. Players will switch from the live
view to video playback mode.

![player](../media/player-ondemand.png)

---

## Media event limits and billing

A media account may have up to one million media events. Media events are billed for the number of minutes of content ingested.