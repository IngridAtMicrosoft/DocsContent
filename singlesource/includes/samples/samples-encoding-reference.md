---
title: Media Services v3 Encoding samples
description: This article is a listing of all of the Media Services Encoding code samples for Node.JS, Python, and Java.
author: IngridAtMicrosoft
ms.service: azure-monitor
ms.topic: overview
ms.date: 01/26/2023
ms.author: inhenkel
---

# Media Services v3 Encoding samples

This article is a listing of all of the Media Services Encoding code samples for Node.JS, Python, and Java.

## Create transform, use job preset overrides (v2-to-v3 API migration)

If you need a workflow where you desire to submit custom preset jobs to a single queue, you can use this base sample that shows how to create a (mostly) empty Transform, and then you can use the preset override property on the Job to submit custom presets to the same transform. This allows you to treat the v3 AMS API a lot more like the legacy v2 API Job queue if you desire.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/CreateTransform_Job_PresetOverride/index.ts)| python | java |

## Copy Audio and Video to MP4 without re-encoding

Uses the built in preset that rapidly copies the source video and audio into a new MP4 file that is ready to be streamed as on-demand through AMS.  This is an extremely useful preset for pre-encoded content or externally encoded content to be quickly readied for streaming in AMS.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_BuiltIn_CopyCodec/) | python | java |

## Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy

Same as above sample, but adds an additional fast encoded proxy resolution. Very useful when creating a CMS or preview of an Asset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main//VideoEncoding/Encoding_BuiltIn_CopyCodecWithProxy/) | python | java |

## Copy Audio and Video to MP4 without re-encoding and create a low bitrate proxy and VTT sprite thumbnail

Same as above samples, with the addition of a VTT sprite thumbnail for use in building a web page, CMS, or custom asset management application

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main//VideoEncoding/Encoding_Custom_CopyCodec_Sprite%2BProxy/) | python | java |

## Encode with H264

Shows how to use the standard encoder to encode a source file into H264 format with AAC audio and PNG thumbnails

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264/index.ts)| python | java |

## Encode with H264 with Event Hubs/Event Grid

Shows how to use the standard encoder and receive and process Event Grid events from Media Services through an Event Hubs. First set up an Event Grid subscription that pushes events into an Event Hubs using the Azure portal or CLI to use this sample.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/tree/main/VideoEncoding/Encoding_H264_with_EventHub/index.ts)| python | java |

## Create a thumbnail sprite (VTT) in JPG format

Shows how to generate a VTT Sprite Thumbnail in JPG format and how to set the columns and number of images. This also shows a speed encoding mode in H264 for a 720P layer.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Sprite_Thumbnail/index.ts)| python | java |

## Content aware encoding with H264

Example of using the standard encoder with Content Aware encoding to automatically generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_ContentAware/index.ts)| python | java |

## Content aware encoding constrained with H264

Demonstrates how to control the output settings of the Content Aware encoding preset to make the outputs more deterministic to your encoding needs and costs. This will still auto generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents, but constrain the output to your desired ranges.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_ContentAware_Constrained/index.ts)| python | java |

## Use an overlay image

Shows how to upload an image file and overlay on top of video with output to MP4 container

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_OverlayImage/index.ts)| python | java |

## Rotate a video

Shows how to use the rotation filter to rotate a video by 90 degrees.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_Rotate90degrees/index.ts)| python | java |

## Output to MPEG transport stream format

Shows how to use the standard encoder to encode a source file and output to MPEG Transport Stream format using H264 format with AAC audio and PNG thumbnail.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_H264_To_TransportStream/index.ts)| python | java |

## Encode with HEVC

Shows how to use the standard encoder to encode a source file into HEVC format with AAC audio and PNG thumbnails

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC/index.ts)| python | java |

## Content aware encoding with HEVC

Example of using the standard encoder with Content Aware encoding to automatically generate the best quality HEVC (H.265) adaptive bitrate streaming set based on an analysis of the source files contents

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC_ContentAware/index.ts)| python | java |

## Content aware encoding constrained with HEVC

Demonstrates how to control the output settings of the Content Aware encoding preset to make the outputs more deterministic to your encoding needs and costs. This will still auto generate the best quality adaptive bitrate streaming set based on an analysis of the source files contents, but constrain the output to your desired ranges.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_HEVC_ContentAware_Constrained/index.ts)| python | java |

## Bulk encoding from a remote Azure storage account using SAS URLs

This samples shows how you can point to a remote Azure Storage account using a SAS URL and submit batches of encoding jobs to your account, monitor progress, and continue.  You can modify the file extension types to scan for (e.g - .mp4, .mov) and control the batch size submitted.  You can also modify the Transform used in the batch operation. This sample demonstrates the use of SAS URL's as ingest sources to a Job input. Make sure to configure the REMOTESTORAGEACCOUNTSAS environment variable in the .env file for this sample to work.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Bulk_Remote_Storage_Account_SAS/index.ts)| python | java |

## Copy live archive to MP4 file format for export or use with Video Indexer

This sample demonstrates how to use the archived output from a live event and extract only the top highest bitrate video track to be packaged into an MP4 file for export to social media platforms, or for use with Video Indexer.  The key concept in this sample is the use of an input definition on the Job InputAsset to specify a VideoTrackDescriptor. The SelectVideoTrackByAttribute allows you to select a single track from the live archive by using the bitrate attribute, and filtering by the "Top" video bitrate track in the live archive.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Live_Archive_To_MP4/) | python | java |

## Encode a multi-channel audio source file

This sample demonstrates how to create an encoding Transform that uses channel mappings and audio track selection from the input source to output two new AAC audio tracks. The standard encoder is limited to outputting 1 Stereo track, followed by a 5.1 surround sound audio track in AAC format.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_MultiChannel_Audio/) | python | java |

## Stitch and edit two assets together

This sample demonstrates how to stitch and edit together two or more assets into a single MP4 file using the JobInputSequence as part of a job submission.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
| [Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/VideoEncoding/Encoding_Stitch_Two_Assets/) | python | java |
