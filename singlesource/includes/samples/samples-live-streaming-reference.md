---
title: Media Services v3 Live Streaming samples
description: description: This article contains a list of all the samples available for Media Services Live Streaming in Node.JS, Python, and Java.
author: IngridAtMicrosoft
ms.service: azure-monitor
ms.topic: overview
ms.date: 01/26/2023
ms.author: inhenkel
---

# Media Services v3 Live Streaming samples

This article contains a list of all the samples available for Media Services Live Streaming in Node.JS, Python, and Java.

## Live stream with standard passthrough

Standard passthrough live streaming example.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Standard_Passthrough_Live_Event/index.ts)| python | java |

## Live stream with standard passthrough with Event Hub

Demonstrates how to use Event Hubs to subscribe to events on the live streaming channel. Events include encoder connections, disconnections, heartbeat, latency, discontinuity, and drift issues.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Standard_Passthrough_Live_Event_with_EventHub/index.ts)| python | java |

## Live stream with basic passthrough

Shows how to set up the basic passthrough live event if you only need to broadcast a low-cost UGC channel.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/Basic_Passthrough_Live_Event/index.ts)| python | java |

## Low Latency (LL-HLS) live streaming with 720p standard encoding

Enable low latency live streaming with Apple's LL-HLS protocol and encode with the new 3-layer 720P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live//720P_Low_Latency_Encoding_Live_Event/index.ts)|python | java |

## Live stream with 720p standard encoding

Use live encoding in the cloud with the 720P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/720P_Encoding_Live_Event/index.ts)| python | java |

## Live stream with 1080p encoding

Use live encoding in the cloud with the 1080P HD adaptive bitrate encoding preset.

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/720P_Encoding_Live_Event/index.ts)| python | java |

## FFmpeg command line samples for RTMP and Smooth

Example command lines for using FFmpeg locally to stream over RTMP or Smooth streaming. Demonstrates various scenarios including audio only, multi-audio, and screen recording

| Node.JS | Python | Java |
| ------- | ------ | ---- |
|[Node.JS](https://github.com/Azure-Samples/media-services-v3-node-tutorials/blob/main/Live/FFmpeg/ffmpeg_commands.md)| python | java |
