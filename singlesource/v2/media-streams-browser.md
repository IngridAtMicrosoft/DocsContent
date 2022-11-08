---
title: Streaming from browsers
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Streaming from browsers

[!INCLUDE [<prerelease-api>](../includes/future-api.md)]

Media can be sent to a media stream directly from a web browser. Streaming from a web browser allows content
to be ingested from webcams without installing any software.

## Creating a media stream

Media streams can be created using the Azure Portal, ARM templates, client SDKs, or using HTTP requests. The request to create a media
stream specifies the outputs for the stream; the media stream creation response includes the streaming URLs for each output.

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media stream creation:

[!INCLUDE [<csharp-media-stream-browser-create>](../includes/csharp-media-stream-browser-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-browser-create](../includes/http-media-stream-browser-create.md)]

---

## Streaming media to a media stream from a browser

After creating a media stream, you can stream media to the stream from a browser.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-start-browser-ingest>](../includes/csharp-media-stream-start-browser-ingest.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-start-browser-ingest](../includes/http-media-stream-start-browser-ingest.md)]

---

The response from the service contains the WebRTC ingest URL. This can be used with the Media Services Studio
to stream media directly from a web browser.

**TODO**

## Getting the media stream status

When the media stream starts receiving data, the state of the media stream will change to `Live`.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-browser-get>](../includes/csharp-media-stream-browser-get.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-browser-get](../includes/http-media-stream-browser-get.md)]

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

When a live stream is complete, browser ingest can be stopped. 

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-start-browser-ingest>](../includes/csharp-media-stream-stop-browser-ingest.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-start-browser-ingest](../includes/http-media-stream-stop-browser-ingest.md)]

---

When ingest is stopped, the media stream will transition to on-demand streaming. Players will switch from the live
view to video playback mode.

![player](../media/player-ondemand.png)
