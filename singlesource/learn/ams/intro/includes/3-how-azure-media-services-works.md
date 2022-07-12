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
TODO: add your topic sentences(s)
TODO: add your bulleted list of key things covered
* TODO
* TODO
* TODO

<!-- 2. Chunked content-------------------------------------------------------------------------------------

    Goal:
        Cover the components of (product) and how they work.
        Repeat this pattern multiple times as needed.

    Pattern:
        Break the content into 'chunks' where each chunk has three things:
            1. An H2 or H3 heading describing the goal of the chunk.
            2. 1-3 paragraphs of text, with a strong lead sentence in the first paragraph.
            3. Visual like an image, table, list, code sample, or blockquote.

    [Learning-unit structural guidance](https://review.docs.microsoft.com/learn-docs/docs/id-guidance-structure-learning-content?branch=main)
-->

<!-- Pattern for simple topic -->
## H2 heading
Strong lead sentence; remainder of paragraph.
Paragraph (optional)
Visual (image, table, list, code sample, blockquote)
Paragraph (optional)
Paragraph (optional)

<!-- Pattern for complex topic -->
## H2 heading
Strong lead sentence; remainder of paragraph.
Visual (image, table, list, code sample, blockquote)
### H3 heading
Strong lead sentence; remainder of paragraph.
Paragraph (optional)
Visual (image, table, list, code sample, blockquote)
Paragraph (optional)
### H3 heading
Strong lead sentence; remainder of paragraph.
Paragraph (optional)
Visual (image, table, list, code sample, blockquote)
Paragraph (optional)

The below diagram shows the workflow for encoding files with Azure Media Services.

:::image type="content" source="../media/v3-encoding.svg" alt-text="encoding workflow for media services encoding":::

:::image type="content" source="../media/media-services-dynamic-packaging.svg" alt-text="Diagram of media services packaging origin and delivery":::


## What is packaging, origin and delivery?

Most browsers and mobile devices on the market today support and understand the HTTP Live Streaming (HLS) or DASH streaming protocols. For example, iOS requires streams to be delivered in HLS format and Android devices support HLS as well as MPEG DASH on certain models or through the use of the application level player, Exoplayer. Azure Media Services provides built-in origin server and packaging capabilities to deliver content in HLS and MPEG DASH streaming protocol formats.

A *streaming endpoint* acts as the "origin" server sending formatted HLS and DASH content to client players that support adaptive bitrate streaming using those popular formats.

Here are some of the advantages of dynamic packaging:

- You can store all your files in standard MP4 file format.
- You do not need to store multiple copies of static packaged HLS and DASH formats which reduces the amount of video content stored and lowering your overall costs of storage.
- You can instantly take advantage of new protocol updates and changes to the specifications as they evolve over time without need of re-packaging the static content in your catalog.
- You can deliver content with or without encryption and DRM using the same MP4 files in storage.
- You can dynamically filter or alter the manifests with simple asset-level or global filters to remove specific tracks, resolutions, languages, or provide shorter highlight clips from the same MP4 files without re-encoding or re-rendering the content.

Azure Media Services offers two types of streaming video-on-demand (VOD) and live streaming.

## What is live streaming?

You can create a *pass-through* live event where you rely on your on-premises encoder to generate a multiple bitrate video stream and send that as the contribution feed to the live event. The live event then sends the incoming video streams to the dynamic packager (streaming endpoint) without any further transcoding. The pass-through live event is optimized for long-running live events or 24x365 linear live streaming.

You may or may not want to keep that video for your viewers to see after the event is over. In that case, the video would be archived to storage and delivered via VOD.
