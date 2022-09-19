---
title: Live streaming and RTMP error v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-live-streaming-rtmp-errors"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Live streaming and RTMP error"
  isofficial="True"
  ms.author="juliako,inhenkel,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Live streaming and RTMP error"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="6b04f8ed-155d-1d1a-7bfe-58acefe85b73" />
-->

# Live streaming and RTMP error

## Learn about live streaming and RTMP errors in Azure Media Services

Use the following guidance to learn how to stream via RTMP, understand encoders that output RTMP, and more.

### Before you begin

When streaming via RTMP, check firewall and/or proxy settings to confirm that outbound TCP ports 1935 and 1936 are open.

### On-premises live encoders that output RTMP

Media Services recommends using one of the following live encoders that have RTMP as output. The supported URL schemes are `rtmp://` or `rtmps://`.

- Adobe Flash Media Live Encoder 3.2
- Haivision KB
- Haivision Makito X HEVC
- OBS Studio
- Switcher Studio (iOS)
- Telestream Wirecast 8.1+
- Telestream Wirecast S
- Teradek Slice 756
- TriCaster 8000
- Tricaster Mini HD-4
- VMIX
- xStream

**Note**: When streaming via **RTMP**, check firewall and/or proxy settings to confirm that outbound TCP ports 1935 and 1936 are open. When streaming via **RTMPS**, check firewall and/or proxy settings to confirm that outbound TCP ports 2935 and 2936 are open.


### Media Services v3 (latest)

**Note**: Currently, you can't use the Azure portal to manage v3 resources. Use the [REST API](https://docs.microsoft.com/rest/api/media/account-filters), [Azure CLI](https://docs.microsoft.com/cli/azure/ams?view=azure-cli-latest), or one of the supported [SDKs](https://docs.microsoft.com/azure/media-services/latest/all-sdks).

[Live events](https://docs.microsoft.com/azure/media-services/latest/live-event-outputs-concept) are responsible for ingesting and processing the live video feeds. When you create a live event, an input endpoint is created that you can use to send a live signal from a remote encoder. The remote live encoder sends the contribution feed to that input endpoint using either the [RTMP](https://rtmp.veriskope.com/docs/spec/) or [Smooth Streaming](https://msdn.microsoft.com/library/ff469518.aspx) (fragmented-MP4) protocol. For the RTMP ingest protocol, the supported URL schemes are `rtmp://` or `rtmps://`.

**Live event ingest URLs**

- In Media Services v3, [live events](https://docs.microsoft.com/azure/media-services/latest/live-event-outputs-concept) are responsible for ingesting and processing the live video feeds. Once the live event is created, you can get ingest URLs that you'll provide to the live on-premises encoder. The live encoder uses these URLs to input a live stream. See the recommended on-premises live encoders above. You can either use non-vanity URLs or vanity URLs.

  - A non-vanity URL is the default mode in Azure Media Services v3. You can potentially get the live event quickly, but the ingest URL is known only when the live event is started. The URL will change if you stop/start the live event. Non-vanity is useful in scenarios when an end user wants to stream using an app where the app wants to get a live event as soon as possible, and having a dynamic ingest URL isn't a problem.

  - A vanity mode is preferred by large media broadcasters who use hardware broadcast encoders and don't want to reconfigure their encoders when they start the live event. They want a predictive ingest URL, which doesn't change over time.

**Note**: For an ingest URL to be predictive, you need to use vanity mode and pass your own access token (to avoid a random token in the URL).

**Live ingest URL naming rules**

The `random` string below is a 128-bit hex number (which is composed of 32 characters of 0-9 a-f).

The `access token` below is what you need to specify for a fixed URL. It's also a 128-bit hex number.

Non-vanity RTMP URL:

* `rtmp://<random 128bit hex string>.channel.media.azure.net:1935/<access token>`
* `rtmp://<random 128bit hex string>.channel.media.azure.net:1936/<access token>`
* `rtmps://<random 128bit hex string>.channel.media.azure.net:2935/<access token>`
* `rtmps://<random 128bit hex string>.channel.media.azure.net:2936/<access token>`

Vanity RTMP URL

* `rtmp://<live event name>-<ams account name>-<region abbrev name>.channel.media.azure.net:1935/<access token>`
* `rtmp://<live event name>-<ams account name>-<region abbrev name>.channel.media.azure.net:1936/<access token>`
* `rtmps://<live event name>-<ams account name>-<region abbrev name>.channel.media.azure.net:2935/<access token>`
* `rtmps://<live event name>-<ams account name>-<region abbrev name>.channel.media.azure.net:2936/<access token>`

### Media Services v2 (legacy)

In Media Services v2, [channels](https://docs.microsoft.com/azure/media-services/previous/media-services-manage-channels-overview) are responsible for ingesting and processing the live video feeds.

### Resources

* [Live Events](https://docs.microsoft.com/azure/media-services/latest/live-event-outputs-concept)
* [CDN Overview](https://docs.microsoft.com/azure/cdn/cdn-overview)

### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
