---
title: Integration with Media Services assets
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Streaming Media Services assets

[!INCLUDE [<prerelease-api>](../includes/future-api.md)]

Just adding a line here to test gitbook.

Media streams can be created from Media Services assets. When a Media Services asset is used for the source of a media stream, the
media data is copied and converted into format that can be streamed.

## Creating a media stream from a Media Services asset

To copy a Media Services asset to a media stream, a new media stream must be created:

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media stream creation:

[!INCLUDE [<csharp-media-stream-asset-create>](../includes/csharp-media-stream-asset-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-asset-create](../includes/http-media-stream-asset-create.md)]

---

After creating a media stream, media content can be copied from a Media Services asset:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-start-asset-ingest>](../includes/csharp-media-stream-start-asset-ingest.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-start-asset-ingest](../includes/http-media-stream-start-asset-ingest.md)]

---

Media Services may need to process the content before it can be streamed. While the content is being processed, the
media stream state will be `Processing`:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-asset-get-1>](../includes/csharp-media-stream-asset-get-1.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-asset-get-1](../includes/http-media-stream-asset-get-1.md)]

---

When the media stream is ready to be viewed, the media stream state will be `OnDemand`:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-asset-get-2>](../includes/csharp-media-stream-asset-get-2.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-asset-get-2](../includes/http-media-stream-asset-get-2.md)]

---

## Viewing the media stream

Once the media content has been processed, it may be viewed using a player. Media can be streamed in a web page using Azure Media Player:

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

![player](../media/player-ondemand.png)
