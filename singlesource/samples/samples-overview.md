---
title: Media Services v3 samples
description: This article is a listing of all of the Media Services code samples for Node.JS, Python, and Java.
author: IngridAtMicrosoft
ms.service: media-services
ms.topic: overview
ms.date: 01/26/2023
ms.author: inhenkel
---

# Media Services v3 samples

This article contains a list of all the samples available for Media Services organized by method and SDK.

## 3rd party player samples

Try various players such as Shaka, Video.js, and THEOPlayer with the [3rd party player samples](https://github.com/Azure-Samples/media-services-3rdparty-player-samples).

## [Accounts](#tab/accounts/)

## Create a Media Services account

The sample shows how to create a Media Services account and set the primary storage account, in addition to advanced configuration settings including Key Delivery IP allowlist, Managed Identity, storage auth, and bring your own encryption key.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Create an account](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Account/create-account.ts) | python | java |

## Create an account with a user assigned managed identity

The sample shows how to create a Media Services account and set the primary storage account, in addition to advanced configuration settings including Key Delivery IP allowlist, user or system assigned Managed Identity, storage auth, and bring your own encryption key.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Create an account with user assigned managed identity](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Account/create-account_with_managed_identity.ts)| python | java |

## [Assets](#tab/assets/)

## List assets

A basic example of how to connect and list assets.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[List assets](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/HelloWorld-ListAssets/list-assets.ts)| | python | java |

## Get the storage contain from an asset

Demonstrates how to find the Azure storage account container used to store the contents of this asset. This can be used to then edit sources, modify, or copy contents using the Azure storage SDK library.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Get the storage container from an asset](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/get-container-from-asset.ts)| python | java |

## List assets using filters

Use filters in your list assets calls to find assets by date and order them.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[List assets using filters](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-assets-filtered.ts)| python | Java |

## List the streaming locators on an asset using filters

Use filters to list the streaming locators attached to your assets.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[List the streaming locators on an asset using filters](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-assets-filtered.ts)| python | java |

## List tracks in an asset

Use the tracks collection to list all of the track names and track types (audio, video, or text) available on an asset

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[List tracks in an asset](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/list-tracks-in-asset.ts)| |  python | java |

## Add a WebVTT/IMSC1/TTML subtitle or caption to an existing asset

Use the tracks API on an Asset to add a new WebVTT or TTML/IMSC1 text profile caption or subtitle to an existing asset

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Add a WebVTT/IMSC1/TTML subtitle or caption to an existing asset](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/add-WebVTT-tracks.ts)| python | java |

## Add an additional audio track to an existing asset using the Tracks API

Use the tracks API on an Asset to add an additional audio language or descriptive audio track to an existing asset. This sample demonstrates how to upload, encode using content aware encoding, and then late bind an additional audio track for a new language to the asset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Add an additional audio track to an existing asset using the tracks API](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Assets/add-audio-language-track.ts)| python | java |

## [Streaming](#tab/streaming/)

## Live stream with standard passthrough

Standard passthrough live streaming example.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Live stream with standard passthrough](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Standard_Passthrough_Live_Event/index.ts)| python | java |

## Live stream with standard passthrough with Event Hub

Demonstrates how to use Event Hubs to subscribe to events on the live streaming channel. Events include encoder connections, disconnections, heartbeat, latency, discontinuity, and drift issues.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Live stream with standard passthrough with Event Hubs](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Standard_Passthrough_Live_Event_with_EventHub/index.ts)| python | java |

## Live stream with basic passthrough

Shows how to set up the basic passthrough live event if you only need to broadcast a low-cost UGC channel.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Live stream with basic passthrough](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Basic_Passthrough_Live_Event/index.ts)| python | java |

## Low Latency (LL-HLS) live streaming with 720p standard encoding

Enable low latency live streaming with Apple's LL-HLS protocol and encode with the new 3-layer 720P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Low Latency Live (LL-HLS) with 720P standard encoding](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live//720P_Low_Latency_Encoding_Live_Event/index.ts)|python | java |

## Live stream with 720p standard encoding

Use live encoding in the cloud with the 720P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Live stream with 720P standard encoding](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/720P_Encoding_Live_Event/index.ts)| python | java |
## Live stream with 1080p encoding

Use live encoding in the cloud with the 1080P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Live stream with 1080P encoding](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/720P_Encoding_Live_Event/index.ts)| python | java |

## FFmpeg command line samples for RTMP and Smooth

Example command lines for using FFmpeg locally to stream over RTMP or Smooth streaming. Demonstrates various scenarios including audio only, multi-audio, and screen recording

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[FFmpeg command line samples for RTMP and Smooth](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/FFmpeg/ffmpeg_commands.md)| python | java |

## Upload and stream HLS and DASH

Basic example for uploading a local file or encoding from a source URL. Sample shows how to use storage SDK to download content, and shows how to stream to a player

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Upload and stream HLS and DASH](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Streaming/StreamFilesSample/index.ts)| python | java |

## Upload a file and stream with Clear Key encryption

Basic example for uploading a local file, encoding it with Content Aware Encoding, and Streaming it using AES Clear Key encryption using Azure Media Player. Sample demonstrates how to create a basic JWT token for playback of AES encrypted content in the browser

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Upload a file and stream with Clear Key encryption](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Streaming/StreamFileWithAESClearKey/index.ts)| python | java |

## [Content Protection](#tab/contentprotection/)

## Upload and stream HLS and DASH with PlayReady and Widevine DRM

Demonstrates how to encode and stream using Widevine and PlayReady DRM

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Upload and stream HLS and DASH with PlayReady and Widevine DRM](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Streaming/StreamFilesWithDRMSample/index.ts)| python | java |

## Basic Playready DRM content protection and streaming

Demonstrates how to encode and stream using PlayReady DRM

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Basic Playready DRM content protection and streaming](https://github.com/Azure-Samples/media-services-v3-node-tutorials/tree/main/ContentProtection/BasicPlayReady/index.ts)| python | java |

## Basic Widevine DRM content protection and streaming

Demonstrates how to encode and stream using Widevine DRM

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Basic Widevine DRM content protection and streaming](https://github.com/Azure-Samples/media-services-v3-node-tutorials/tree/main/ContentProtection/BasicWidevine/index.ts)| python | java |

## [Encoding](#tab/encoding/)

## Create transform, use job preset overrides (v2-to-v3 API migration)

If you need a workflow where you desire to submit custom preset jobs to a single queue, you can use this base sample that shows how to create a (mostly) empty Transform, and then you can use the preset override property on the Job to submit custom presets to the same transform. This allows you to treat the v3 AMS API a lot more like the legacy v2 API Job queue if you desire.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Create transform, use job preset overrides (v2-to-v3 API migration)](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/CreateTransform_Job_PresetOverride/index.ts)| python | java |

## Copy Audio and Video to MP4 without re-encoding

Uses the built in preset that rapidly copies the source video and audio into a new MP4 file that is ready to be streamed as on-demand through AMS.  This is an extremely useful preset for pre-encoded content or externally encoded content to be quickly readied for streaming in AMS.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Copy Audio and Video to MP4 without re-encoding](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_BuiltIn_CopyCodec/) | python | java |

## Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy

Same as above sample, but adds an additional fast encoded proxy resolution. Very useful when creating a CMS or preview of an Asset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main//VideoEncoding/Encoding_BuiltIn_CopyCodecWithProxy/) | python | java |

## Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy and VTT sprite thumbnail

Same as above samples, with the addition of a VTT sprite thumbnail for use in building a web page, CMS, or custom asset management application

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy and VTT sprite thumbnail](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main//VideoEncoding/Encoding_Custom_CopyCodec_Sprite%2BProxy/) | python | java |

## Encode with H264

Shows how to use the standard encoder to encode a source file into H264 format with AAC audio and PNG thumbnails

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Encode with H264](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264/index.ts)| python | java |

## Encode with H264 with Event Hubs/Event Grid

Shows how to use the standard encoder and receive and process Event Grid events from Media Services through an Event Hubs. First set up an Event Grid subscription that pushes events into an Event Hubs using the Azure portal or CLI to use this sample.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Encode with H264 with Event Hubs/Event Grid](https://github.com/Azure-Samples/media-services-v3-node-tutorials/tree/main/VideoEncoding/Encoding_H264_with_EventHub/index.ts)| python | java |

## Create a thumbnail sprite (VTT) in JPG format

Shows how to generate a VTT Sprite Thumbnail in JPG format and how to set the columns and number of images. This also shows a speed encoding mode in H264 for a 720P layer.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Create a thumbnail sprite (VTT) in JPG format](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Sprite_Thumbnail/index.ts)| python | java |

## Content aware encoding with H264

Example of using the standard encoder with Content Aware encoding to automatically generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Content aware encoding with H264](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_ContentAware/index.ts)| python | java |

## Content aware encoding constrained with H264

Demonstrates how to control the output settings of the Content Aware encoding preset to make the outputs more deterministic to your encoding needs and costs. This will still auto generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents, but constrain the output to your desired ranges.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Content aware encoding constrained with H264](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_ContentAware_Constrained/index.ts)| python | java |

## Use an overlay image

Shows how to upload an image file and overlay on top of video with output to MP4 container

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Use an overlay image](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_OverlayImage/index.ts)| python | java |

## Rotate a video

Shows how to use the rotation filter to rotate a video by 90 degrees.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Rotate a video](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_Rotate90degrees/index.ts)| python | java |

## Output to MPEG transport stream format

Shows how to use the standard encoder to encode a source file and output to MPEG Transport Stream format using H264 format with AAC audio and PNG thumbnail.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Output to MPEG transport stream format](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_To_TransportStream/index.ts)| python | java |

## Encode with HEVC

Shows how to use the standard encoder to encode a source file into HEVC format with AAC audio and PNG thumbnails

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Encode with HEVC](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC/index.ts)| python | java |

## Content aware encoding with HEVC

Example of using the standard encoder with Content Aware encoding to automatically generate the best quality HEVC (H.265) adaptive bitrate streaming set based on an analysis of the source files contents

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Content aware encoding with HEVC](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC_ContentAware/index.ts)| python | java |

## Content aware encoding constrained with HEVC

Demonstrates how to control the output settings of the Content Aware encoding preset to make the outputs more deterministic to your encoding needs and costs. This will still auto generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents, but constrain the output to your desired ranges.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Content aware encoding constrained with HEVC](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC_ContentAware_Constrained/index.ts)| python | java |

## Bulk encoding from a remote Azure storage account using SAS URLs

This samples shows how you can point to a remote Azure Storage account using a SAS URL and submit batches of encoding jobs to your account, monitor progress, and continue.  You can modify the file extension types to scan for (e.g - .mp4, .mov) and control the batch size submitted.  You can also modify the Transform used in the batch operation. This sample demonstrates the use of SAS URL's as ingest sources to a Job input. Make sure to configure the REMOTESTORAGEACCOUNTSAS environment variable in the .env file for this sample to work.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Bulk encoding from a remote Azure storage account using SAS URLs](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Bulk_Remote_Storage_Account_SAS/index.ts)| python | java |

## Copy live archive to MP4 file format for export or use with Video Indexer

This sample demonstrates how to use the archived output from a live event and extract only the top highest bitrate video track to be packaged into an MP4 file for export to social media platforms, or for use with Video Indexer.  The key concept in this sample is the use of an input definition on the Job InputAsset to specify a VideoTrackDescriptor. The SelectVideoTrackByAttribute allows you to select a single track from the live archive by using the bitrate attribute, and filtering by the "Top" video bitrate track in the live archive.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Copy live archive to MP4 file format for export or use with Video Indexer](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Live_Archive_To_MP4/) | python | java |

## Encode a multi-channel audio source file

This sample demonstrates how to create an encoding Transform that uses channel mappings and audio track selection from the input source to output two new AAC audio tracks. The standard encoder is limited to outputting 1 Stereo track, followed by a 5.1 surround sound audio track in AAC format.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Encode a multi-channel audio source file](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_MultiChannel_Audio/) | python | java |

## Stitch and edit two assets together

This sample demonstrates how to stitch and edit together two or more assets into a single MP4 file using the JobInputSequence as part of a job submission.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Stitch and edit two assets together](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Stitch_Two_Assets/) | python | java |

## [Analytics](#tab/analytics/)

## Basic Audio Analytics with per-job language override

This sample illustrates how to create a audio analyzer transform using the basic mode.  It also shows how you can override the preset language on a per-job basis to avoid creating a transform for every language.  It also shows how to upload a media file to an input asset, submit a job with the transform and download the results for verification.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Basic Audio Analytics with per-job language override](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/AudioAnalytics/index.ts)| python | java |

## [Player](#tab/player/)

## Shaka player with Timed Metadata for live event interactivity

This sample shows how to use the Google Shaka player with Low latency HLS streams to receive timed metadata events and display interactive information overlayed on the video element. This can be used to build interactive ads, quiz shows, polling, and other solutions that require events to be triggered in your web page or application during a live stream.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Shaka player with Timed Metadata for live event interactivity](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Player/examples/shaka)| python | java |

---
