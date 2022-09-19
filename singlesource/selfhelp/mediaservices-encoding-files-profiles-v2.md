---
title: Standard Encoder Configuration and Management
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-encoding-files-profiles"
  cloudenvironments="public,fairfax,usnat,ussec"
  description="This document describes errors and troubleshooting methods for the AMS Standard Encoder."
  ms.author="jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Standard Encoder Configuration"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="86821d54-477e-9c74-fefa-9045782f6695" />
-->

# Standard Encoder Configuration and Management v2

## Resolve encoding issues with the Azure Media Services standard encoder

Azure Media Services (AMS) is a cloud-based platform that enables you to build solutions that achieve broadcast-quality video streaming, enhance accessibility and distribution, analyze content, and much more. Whether you're an app developer, a call center, a government agency, or an entertainment company, Media Services helps you create apps that deliver media experiences of outstanding quality to large audiences on today's most popular mobile devices and browsers.

The [BuiltInStandardEncoderPreset](https://docs.microsoft.com/en-us/rest/api/media/transforms/create-or-update?tabs=HTTP#builtinstandardencoderpreset) is used to set a built-in preset for encoding the input video with the Standard Encoder.

If you're experiencing issues with the Standard Encoder, use our guidance to help you resolve your issues.

### Standard Encoder offerings
The Standard Encoder currently offers a wide variety of codecs, bitrates, and resolutions. If you would like to see the full list of input and output codecs, see the doc [Standard Encoder formats and codecs](/azure/media-services/latest/encode-media-encoder-standard-formats-reference).

### Encoding job errors
If you get any job error codes when running an encoding job using the Standard Encoder, see the doc [REST API Job Error Code](/rest/api/media/jobs/get?tabs=HTTP#joberrorcode).

For other troubleshooting errors, our [troubleshooting page](/azure/media-services/latest/troubleshooting) provides solutions to common issues.


### Encoding billing
If you have questions on how pricing and billing works, refer to our [pricing page](https://azure.microsoft.com/pricing/details/media-services/) and select the "Encoding" tab.

**Note**: Encoding prices are for each layer of output. For example, if you are using the Adaptive Streaming preset, this will result in multiple output layers. (See [Encode with an auto-generated bitrate ladder](/azure/media-services/latest/encode-autogen-bitrate-ladder)). Azure Media Services charges per layer of output. If you have three layers of output for a video, where two are SD and one is HD, the total charge will be the sum of all three layers.


### Resources

Media Services v3 (latest)

* [Encoding with Media Services v3](/azure/media-services/latest/encode-concept)<br>
* [Media Encoder Standard formats and codecs](/azure/media-services/latest/encode-media-encoder-standard-formats-reference)<br>
* [Dynamic Packaging](/azure/media-services/latest/encode-dynamic-packaging-concept)<br>
* [Migrate to V3](/azure/media-services/latest/migrate-v-2-v-3-migration-introduction)

<!--### Here are some relevant results from the web
<azureKB>
    <client>Portal</client>
</azureKB>-->