<!-- 1. Topic sentence(s) --------------------------------------------------------------------------------

    Goal: state what's in this unit and how it aligns to the 'describe' learning objective.

    Pattern:
        One paragraph of 2-3 sentences:
            Sentence 1: State that this unit addresses ("how it works").
            Sentence 2: State that this unit targets this learning objective: "Describe how (features) of (product) work to (solve problem)."
            Sentence 3-4 (optional): Give the rationale ("helps you decide if it will meet your needs").
        Table-of-contents as a bulleted list (do not simply list every heading you'll have on the page, group them into about 3 high-level areas).

    Heading: none

    Example: "Here, we'll discuss how Logic Apps works behind the scenes. You'll learn about all the pieces of Logic apps and see how they fit together into an app. This knowledge will help you decide whether Logic Apps will work for you without any customization. In cases where you do need to create custom components, you'll be able to determine how difficult it will be.
        * Connectors, triggers, actions
        * Control actions
        * Logic Apps Designer"
-->

Here, we'll discuss how Azure Media Services works behind the scenes. You'll learn about the parts of Azure Media Services and see how they fit together to create a streaming media application. You can use only some of these parts or all of them depending on your needs. This knowledge will help you decide whether Azure Media Services will work for you.

* Some definitions
* Packaging and delivery
* Content protection
* Basic video on demand for encoding and streaming workflow
* Live streaming workflow
* Security

## Some definitions

- **Asset** - an Azure Storage block blob container. It contains all the files related to one piece of media such as MP4 files as well as manifests, captions, and other data. It can be used to store files for video on demand, encoding inputs and outputs, live streaming outputs, etc.
- **Input asset** - an Azure Storage blob container that holds the original (mezzanine) files that are to be encoded.
- **Output asset** - an Azure Storage blob container that contains all of the files produced by the encoder as well as files needed for streaming the videos.
- **Transform** - the "recipe" that applies tells Azure Media Services which encoders to use while encoding the mezzanine file.
- **Job** - the actual encoding job where the transform is applied to the mezzanine file.
- **Streaming endpoint** - A streaming endpoint is a dynamic packaging and origin service that delivers live and on-demand content directly to a client player app, using one of the common streaming media protocols (HLS or DASH). It also provides dynamic encryption for digital rights management.
- **Streaming locator** - an entity in Azure Media Services that builds streaming URLs for assets.
- **Streaming URL** - a URL that tells the browser what to play and how to play it.
- **Streaming policy** - defines the streaming protocols and encryption options for streaming locators.
- **Content key** - provides secure access to an asset.
- **Content key policy** - used to configure how a content key is delivered to media players.
- **Digtal Rights Management (DRM)** - a way of protecting content from being played unless certain criteria are met such as allowing playback during a period of time or only by certain devices. DRM technologies include Apple FairPlay, Google Widevine, and Microsoft's PlayReady.
- **DRM license** - a document that communicates the restrictions placed on the content by digital rights management.

## Packaging and delivery

Most browsers and mobile devices on the market today support and understand the HTTP Live Streaming (HLS) or DASH streaming protocols. For example, iOS requires streams to be delivered in HLS format and Android devices support HLS as well as MPEG DASH on certain models or through the use of the application level player, Exoplayer. Azure Media Services provides built-in origin server and packaging capabilities to deliver content in HLS and MPEG DASH streaming protocol formats.

A *streaming endpoint* acts as the "origin" server sending formatted HLS and DASH content to client players that support adaptive bitrate streaming using those popular formats.

Here are some of the advantages of dynamic packaging:

- You can store all your files in standard MP4 file format.
- You do not need to store multiple copies of static packaged HLS and DASH formats which reduces the amount of video content stored and lowering your overall costs of storage.
- You can instantly take advantage of new protocol updates and changes to the specifications as they evolve over time without need of re-packaging the static content in your catalog.
- You can deliver content with or without encryption and DRM using the same MP4 files in storage.
- You can dynamically filter or alter the manifests with simple asset-level or global filters to remove specific tracks, resolutions, languages, or provide shorter highlight clips from the same MP4 files without re-encoding or re-rendering the content.

## Content protection

You can deliver your live and on-demand content encrypted dynamically with Advanced Encryption Standard (AES-128) or any of the three major digital rights management (DRM) systems: Microsoft PlayReady, Google Widevine, and Apple FairPlay. FairPlay Streaming is an Apple technology that is only available for video transferred over HTTP Live Streaming (HLS) on iOS devices, in Apple TV, and in Safari on macOS.

Media Services also provides a service for delivering AES keys and DRM (PlayReady, Widevine, and FairPlay) licenses to authorized clients. If content is encrypted with an AES clear key and is sent over HTTPS, it is not in clear until it reaches the client.

When a stream is requested by a player, Media Services uses the specified key to dynamically encrypt your content by using AES clear key or DRM encryption. To decrypt the stream, the player requests the key from Media Services key delivery service or the key delivery service you specified. To decide if the user is authorized to get the key, the service evaluates the content key policy that you specified for the key.

:::image type="content" source="../media/content-protection.svg" alt-text="azure media services content protection":::

For detailed information about Azure Media Services content protection see [Content protection with dynamic encryption and key delivery](/azure/media-services/latest/drm-content-protection-concept), [Streaming policies](/azure/media-services/latest/stream-streaming-policy-concept), and [Content key policies](/azure/media-services/latest/drm-content-key-policy-concept).

## Basic video on demand for encoding and streaming workflow

Before you can begin streaming with Azure Media Services, videos need to be encoded. The steps are:

1. Videos are uploaded and
1. Housed in an input asset.
1. One or more encoding presets are chosen for the transform.
1. A transform is created.
1. A job is created and started.
1. The job creates an output asset that houses the encoded files along with the files needed for streaming.
1. A streaming policy is selected while creating a streaming locator an asset.
1. Streaming URLs are created which are then used by the player as the source value.

:::image type="content" source="../media/vod-process.svg" alt-text="azure media services vod application workflow" lightbox="../media/vod-process.svg" :::

## Live streaming workflow

There are two ways to set up live streaming, as pass-through events or a live encoding event.

### Pass-through events

When you create a pass-through event, the on-premises encoder generates a *multiple-bitrate video stream* and sends it as the contribution feed to a live event. The live event sends the incoming video stream to the streaming endpoint.

1. An Azure Media Services Live event is set up to receive a broadcast from an on-premises encoder.
1. An on-premises encoder is set up to send a broadcast to the live event as a *multiple-bitrate video stream*.
1. The live event and broadcasting is started.
    1. If live transcription is used, a transcript of the video is dynamically generated and saved to an output asset.
1. The live event is streamed with the streaming endpoint using the HLS, DASH or Smooth Streaming protocols.
    1. If DRM is used, the video is encrypted. When the player requests a video, Azure Media Services key delivery service checks whether the player is allowed to decrypt and play the content.

When the live event is over, you can choose to archive the output files for use with a VOD application.

:::image type="content" source="../media/pass-through.svg" alt-text="Azure Media Services pass-through event" lightbox="../media/pass-through.svg":::

### Live encoding events

When you can also use Azure Media Services to encode the live events for you. In this case, the on-premises encoder would be set up to generate a *single bitrate video stream*.

1. An Azure Media Services Live event is set up to receive a broadcast from an on-premises encoder as a *single bitrate video stream*.
1. An on-premises encoder is set up to send a broadcast to the live event.
1. The live event and broadcasting is started.
    1. The live encoder encodes the incoming single bitrate stream to multiple bitrate streams.
    1. If live transcription is used, a transcript of the video is dynamically generated and saved to an output asset.
1. The live event is streamed with the streaming endpoint using the HLS, DASH or Smooth Streaming protocols.
    1. If DRM is used, the video is encrypted. When the player requests a video, Azure Media Services key delivery service checks whether the player is allowed to decrypt and play the content.

:::image type="content" source="../media/live-encoding.svg" alt-text="azure media services live encoding":::

## Security

Discussing securing the Azure resources in your application architecture is beyond the scope of this introduction. However, security is mentioned here so you can be azzured that there are methods for securing your accounts, keys, and network. For detailed information about securing Azure Media Services resources, see [Azure security baseline for Azure Media Services](/security/benchmark/azure/baselines/media-services-security-baseline).