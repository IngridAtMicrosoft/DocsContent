---
title: How to configure live streaming? v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: azure-monitor
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-live-streaming-configure-channels-live-events"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Use our guidance to learn how to configure live streaming, including supported live encoders, using live events in the v3 API, and more."
  ms.author="juliako,jiayali,inhenkel"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Configure live streaming"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="35ba9292-e626-9c0b-fb2c-be68ffcf4e97" />
-->

# How to configure live streaming? v2

## Learn to configure live streaming

Use the following guidance to learn how to configure live streaming, and learn about supported live encoders, using live events in the v3 API, and more.

### Troubleshoot live encoding issues

If you're having an issue with live encoding, try testing with one of the recommended [encoder configurations for Azure Media Services](/azure/media-services/latest/encode-recommended-on-premises-live-encoders).

### Using live events in the v3 API

**Note**: Currently, you can't use the Azure portal to manage v3 resources. Use the [REST API](/rest/api/media/account-filters), [CLI](/cli/azure/ams?view=azure-cli-latest), or one of the supported [SDKs](/azure/media-services/latest/all-sdks).

* Azure Media Services enables you to deliver live events to your customers on the Azure cloud, see [Live streaming with Azure Media Services v3](/azure/media-services/latest/stream-live-streaming-concept).

* Review this tutorial to learn more about [streaming live with v3 API and .NET](/azure/media-services/latest/stream-live-tutorial-with-api).

### Monitoring live events with Event Grid

If you'd like to create and/or monitor the status and health of your live events, refer to the following documents for step-by-step instructions with the Azure portal or CLI.

* [Azure portal](/azure/media-services/latest/monitoring/monitor-events-portal-how-to)
* [Azure CLI](/azure/media-services/latest/monitoring/job-state-events-cli-how-to)

### Using channels in the v2 API (legacy)

A channel represents a pipeline for processing live streaming content, see [Overview of Live Streaming using Azure Media Services](/azure/media-services/previous/media-services-manage-channels-overview/).

**How to configure live streaming**

* [Working with channels that receive multi-bitrate live stream from on-premises encoders](/azure/media-services/previous/media-services-live-streaming-with-onprem-encoders)
* [Live streaming using Azure Media Services cloud encoder](/azure/media-services/previous/media-services-manage-live-encoder-enabled-channels)

### Resources

* [Transforms and jobs in Media Services](/azure/media-services/latest/transform-jobs-concept)
<!--
### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
-->
