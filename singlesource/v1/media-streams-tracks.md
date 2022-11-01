---
title: Media Stream Tracks
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Tracks

The media tracks resource lists each of the tracks in a media stream.

> [!NOTE]
> The media tracks API lists the primary tracks within a media stream. When a stream is viewed, Media Services
may generate video and audio tracks with different bit rates.

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Media stream creation:

[!INCLUDE [<csharp-media-tracks-list>](../includes/csharp-media-tracks-list.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-tracks-list](../includes/http-media-tracks-list.md)]

---