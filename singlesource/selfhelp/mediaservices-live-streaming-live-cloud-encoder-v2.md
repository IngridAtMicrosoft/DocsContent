---
title: Live streaming with a live cloud encoder v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-live-streaming-live-cloud-encoder"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="To use live encoding with Media Services, configure your on-premises live encoder to send a single bitrate video as the contribution feed to the Channel (v2)/Live Event (v3) using RTMP or Fragmented-Mp4 protocol. The Channel/Live Event encodes that incoming single bitrate stream to a [multiple bitrate video stream](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming), making it available for delivery to playback devices via protocols like MPEG-DASH, HLS, and Smooth Streaming. "
  ms.author="juliako,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Learn about live streaming with a live cloud encoder"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="596c66d3-32a1-65b4-bf17-d1b11113b0da" />
-->

# Live streaming with a live cloud encoder v2

## Learn about live streaming with a live cloud encoder

To use live encoding with Media Services, configure your on-premises live encoder to send a single bitrate video as the contribution feed to the Channel (v2)/Live Event (v3) using RTMP or Fragmented-Mp4 protocol. The Channel/Live Event encodes that incoming single bitrate stream to a [multiple bitrate video stream](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming), making it available for delivery to playback devices via protocols like MPEG-DASH, HLS, and Smooth Streaming.

You can send the contribution feed at up to 1080p resolution at a frame rate of 30 frames/second, with H.264/AVC video codec and AAC (AAC-LC, HE-AACv1, or HE-AACv2) audio codec. See the [Live Event types comparison](/azure/media-services/latest/live-event-types-comparison) article for more details.

When using live encoding, the encoding preset defines how the incoming stream is encoded into multiple bitrates or layers. See [System presets](/azure/media-services/latest/live-event-types-comparison#system-presets).

**Important**: Update your Azure Media Services REST API and SDKs to v3 by February 29, 2024. Version 3 of Azure Media Services REST API and client SDKs for .NET and Java offers more capabilities than version 2. We’re retiring version 2 of the Azure Media Services REST API and client SDKs for .NET and Java. Review the [v2 to v3 migration guide](/azure/media-services/latest/migrate-v-2-v-3-migration-introduction) for more details on how to transition your code.

### Resources

Media Services v3 (latest)

* [Recommended live encoders to use with Media Services](/azure/media-services/latest/recommended-on-premises-live-encoders)
* [Overview of live streaming with the v3 API](/azure/media-services/latest/live-streaming-overview)
* [Live Events and Live Outputs](/azure/media-services/latest/live-events-outputs-concept)
* [States and billing](/azure/media-services/latest/live-event-states-billing)
* [Migrate from Media Services v2 to v3](/azure/media-services/latest/migrate-v-2-v-3-migration-introduction)

Media Services v2 (legacy)

* [Live streaming with v2](/azure/media-services/previous/media-services-manage-live-encoder-enabled-channels)

### Here are some relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
