<properties
  articleid="apollo-mediaservices-player-closed-captions"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Azure Media Player closed captions and subtitle support"
  ms.author="jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Azure Media Player closed captions and subtitle support"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="c9174122-cb68-f0bd-1ca1-fe91f7b6342d" />
# Azure Media Player closed captions and subtitles

## Learn about Azure Media Player closed captions and subtitles


Azure Media Player currently supports captions for only On Demand events with WebVTT format and live events using CEA-708 pass-through. IMSC1/TTML format is  not supported. Captions and subtitles allow the player to cater to and empower a broader audience, including people with hearing disabilities or those who want to read along in a different language. Captions also increase video engagement, improve comprehension, and make it possible to view the video in sound sensitive environments, like a workplace.

### Sample WebVTT subtitles in Azure Media Player

Review [this sample of using WebVTT](https://amp.azure.net/libs/amp/latest/samples/dynamic_webvtt.html) subtitles with Azure Media Player. 

### Live captions with 608/708 pass-through

Review [this sample showing live captions with 608/708 passthrough](https://amp.azure.net/libs/amp/latest/samples/dynamic_live_captions.html).

Your upstream live encoder must be capable of pre-inserting CEA-708 and 608 captions into the video stream. If captions are detected in the video stream, they will be preserved. 

### Resources

* [Subtitle and Captions in Azure Media Player](http://amp.azure.net/libs/amp/latest/docs/index.html#captions-and-subtitles)<br> 
* [CEA-708 and 608 captions settings in Player](http://amp.azure.net/libs/amp/latest/docs/index.html#amp.player.cea708captionssettings)<br>
* [Azure Media Player overview](https://docs.microsoft.com/azure/media-services/azure-media-player/azure-media-player-overview)<br>
* [Azure Media Player documentation](http://amp.azure.net/libs/amp/latest/docs/index.html)<br>
* [Azure Media Player sample streams](https://amp.azure.net/libs/amp/latest/docs/samples.html)<br>
* [Azure Media Player changelog](http://amp.azure.net/libs/amp/latest/docs/changelog.html)

### Relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>
