
Here, we'll discuss how Azure Media Services works behind the scenes. You'll learn about the parts of Azure Media Services and see how they fit together into a video steaming platform app. This knowledge will help you decide whether Azure Media Services will work for you.

- Media Services accounts and storage
- Assets
- Streaming endpoints
- Streaming locators
- Encoding transforms
- Jobs
- Content protection and Digital Rights Management(DRM)
- Live streaming
- Media Analysis

## Media Services accounts and storage

A Media Services account is an Azure resource that allows you to work with the Media Services product. It is associated with an Azure Storage account which is used to store and deliver media.

## Assets

For Media Services, an Asset is a core concept. It is where you input media (for example, through upload or live ingest), output media (from a job output), and publish media (for streaming). An Asset is mapped to a blob container in the Azure Storage account and the files in the Asset are stored as block blobs in that container. Assets contain information about digital files stored in Azure Storage (including video, audio, images, thumbnail collections, text tracks, and closed caption files).

## Streaming endpoints

A Streaming Endpoint represents a dynamic (just-in-time) packaging and origin service that can deliver your live and on-demand content directly to a client player application. It uses one of the common streaming media protocols (HLS or DASH). In addition, the Streaming Endpoint provides dynamic (just-in-time) encryption to industry-leading digital rights management systems (DRMs).

In the media streaming industry, this service is commonly referred to as a Packager or Origin. Other common terms in the industry for this capability include JITP (just-in-time-packager) or JITE (just-in-time-encryption).

## Streaming locators

To make videos in an asset available to clients for playback, you have to create a streaming locator and then build streaming URLs. These URLs are used by the media player to locate and stream the content. The process of creating a streaming locator is called *publishing*.

## Encoding preset

An encoding preset is a set of configuration settings for an encoding job or other transformation done on media. Presets are offered by Media Services as a convenience to customers who don't want to define custom presets.

## Encoding transforms

A transform is like a recipe for encoding media from one format to another (or several others). When you create a transform, you specify which encoding presets you want to use.

## Jobs

A Job is the actual request to Media Services to apply the Transform to a given input video or audio content. The Job specifies information like the location of the input video and the location for the output. You can specify the location of your input video using: HTTPS URLs, SAS URLs, or Assets.

## Content protection and Digital Rights Management(DRM)

You can deliver your live and on-demand content encrypted dynamically with Advanced Encryption Standard (AES-128) or/and any of the three major DRM systems: Microsoft PlayReady, Google Widevine, and Apple FairPlay. Media Services also provides a service for delivering AES keys and DRM (PlayReady, Widevine, and Apple FairPlay Streaming) licenses to authorized clients.

## Live events

Live events are responsible for ingesting and processing the live video feeds. When you create a live event, a primary and secondary input endpoint is created that you can use to send a live signal from a remote encoder.

## Media analysis

Media services offers media analyzer presets that are similar to encoding presets.