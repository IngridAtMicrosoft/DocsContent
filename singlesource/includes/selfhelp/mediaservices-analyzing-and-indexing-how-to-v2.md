---
title: Analyze and index audio and video files in Azure Media Services
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-analyzing-indexing-how-to"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Azure Media Services enables you to extract insights from your video and audio files with Video Indexer through Media Services v3 presets. Learn to do this by using recommended steps. For detailed insights, use the Video Indexer APIs directly."
  isofficial="True"
  ms.author="akucer,jiayali,inhenkel"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Analyze and index audio and video files in Azure Media Services"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="50572256-2e9f-4da9-2849-35cab985386e" />-->

# Analyzing and indexing how to v2

## Learn to analyze and index audio and video files in Azure Media Services

Azure Media Services enables you to extract insights from your video and audio files with Video Indexer through Media Services v3 presets. Learn to do this by using the following guidance.

### Before you begin

For detailed insights, use the [Video Indexer APIs](https://api-portal.videoindexer.ai/) directly.

To understand the differences between the Video Indexer APIs and Media Services v3 APIs, see the [comparison document](/azure/azure-video-analyzer/video-analyzer-for-media-docs/compare-video-indexer-with-media-services-presets).

### Analyze your video and audio files in Azure Media Services

To analyze your content using Media Services v3 presets, [create a transform](/azure/media-services/latest/transform-create-transform-how-to?tabs=cli) and submit a job that uses one of these presets: VideoAnalyzerPreset or AudioAnalyzerPreset.

### Resources

* [Analyzing Video and Audio Files Overview](/azure/media-services/latest/analyze-video-audio-files-concept)
* [Scale Media Analytics and Indexing](/azure/media-services/previous/media-services-scale-media-processing-overview)
* [Video Indexer Developer Portal and APIs](https://api-portal.videoindexer.ai/)
* [Pricing for Analytics and Indexing (see Analytics & Indexing tab)](https://azure.microsoft.com/pricing/details/media-services/)
* [CODE SAMPLES](/azure/media-services/latest/samples-overview)
<!--
### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
-->