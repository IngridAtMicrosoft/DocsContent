---
title: ""
description: "Description goes here."
ms.author: "inhenkel"
ms.service: media-services
author: IngridAtMicrosoft
---

<!-- <properties
  articleid="apollo-mediaservices-player-analytics"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Azure Media Player analytics"
  ms.author="jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Azure Media Player analytics"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="a9036f12-bfde-7afb-6d76-7a3b7bad3096" /> -->
# Azure Media Player analytics

## Understanding the client experience using analytics with Azure Media Player

Often with distance learning, corporate compliance, and advertising viewership, it is necessary to determine what video was watched and for how long. There are three methods to determine video usage for an account, but one to determine client behavior. We recommend you use plugins to enhance the Azure Media Player experience.

### Back-end tracking telemetry

Telemetry is the back-end tracking with Azure Media Services. See, [Media Services Telemetry](https://docs.microsoft.com/azure/media-services/previous/media-services-telemetry-overview). However, this is a summary of the streaming endpoint level, and all users on that endpoint. While adaptive streaming has advantages for video playback but there is no persistent connection relationship between the client and server. This makes it difficult to track the exact actions of a client. Typically the Content Delivery Network (CDN) is used in front of the streaming endpoint. The streaming endpoint sees requests for fragments that are cache misses from the CDN. Often this means the streaming endpoint sees a fraction of the actual client load.

### Content Delivery Network information

CDN provides information about the general bandwidth, cache hit ratio, and cache status of the linked Media Services streaming endpoint via the Verizon CDN Core Reports. See [CDN usage patterns](https://docs.microsoft.com/azure/cdn/cdn-analyze-usage-patterns) for more information. This is similar to Media Services telemetry, but also has summary information of all users.

### Plugins

For getting client playback experience and statistics, use the Azure Media Player plugin model with an analytics plugin. See, [AMP plugins](https://amp.azure.net/libs/amp/latest/docs/PLUGINS.html). These use the Azure Media Player API events to feed a database with the playback metrics. For more information on the Application Insights plugin see [Player analytics with Azure Media Player plugins](https://azure.microsoft.com/blog/player-analytics-azure-media-player-plugin/).

**Plugins for Azure Media Player analytics**

* [Azure Application Insights plugin](https://azure.microsoft.com/blog/player-analytics-azure-media-player-plugin/)<br>
* [Google Analytics plugin](https://github.com/Azure-Samples/media-services-javascript-azure-media-player-google-analytics-plugin)

### Resources

* [Player events for Azure Media Player](https://amp.azure.net/libs/amp/latest/docs/index.html#amp.eventname)<br>
* [Azure Media Player plugins](https://amp.azure.net/libs/amp/latest/docs/PLUGINS.html)<br>
* [Azure Media Player overview](https://docs.microsoft.com/azure/media-services/azure-media-player/azure-media-player-overview)<br>
* [Azure Media Player documentation](http://amp.azure.net/libs/amp/latest/docs/index.html)<br>
* [Azure Media Player sample streams](https://amp.azure.net/libs/amp/latest/docs/samples.html)

### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
