---
title: Azure Media Player playback issues v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-player-playback-issues"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Azure Media Player playback issues"
  isofficial="True"
  ms.author="inhenkel,jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Azure Media Player playback issues"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="6272b6a0-6c9c-32d1-0849-981b96a666ee" />
-->

# Azure Media Player playback issues v2

## Resolve Azure Media Player play-back issues

Azure Media Player play-back issues may be cosed DRM issues, improper encoding, or other issues. Use the following guidance to help resolve play-back issues in Azure Media Player and to learn how to possibly improve playback.

### Troubleshooting

1. Compare your error code with the known list of [Azure Media Player error codes](/azure/media-services/azure-media-player/azure-media-player-error-codes).
2. To rule out DRM related issues, remove all content protection (AES) or DRM encryption from the stream.
3. Test your (non-DRM) content using the [Azure Media Services test player](https://ampdemo.azureedge.net/azuremediaplayer.html).
4. Test your (non-DRM) on target devices (iOS or Android) to confirm playback.
5. Confirm the content is encoded correctly, with codecs and bitrates for the target devices in the manufacturer guidance.
6. Confirm you are using the needed [player heuristics profile](/azure/media-services/azure-media-player/demos) for your scenario.
7. Review the [known issues list](/azure/media-services/azure-media-player/azure-media-player-known-issues) for Azure Media Player.

### Error codes and catching errors

When playback cannot start or has stopped, the error function returns a code and an optional message.

To catch errors, add the 'error' event listener to the player:

```
var myPlayer = amp('vid1');
myPlayer.addEventListener('error', function() {
    var errorDetails = myPlayer.error();
    var code = errorDetails.code;
    var message = errorDetails.message;
}
```

For player error codes and meanings see [Azure Media Player error codes](/azure/media-services/azure-media-player/azure-media-player-error-codes).

### Improving playback

If there is bad playback, use [adaptive bitrate streaming](/azure/media-services/latest/encode-autogen-bitrate-ladder). This automatically selects the best bitrate for network connections.

### Frequently Asked Questions

|Question|Answer
|---|---
|What browsers and OS are supported for Media Player?|See the [browser and OS compatibility matrix](/azure/media-services/azure-media-player/azure-media-player-playback-technology#compatibility-matrix) for Azure Media Player.
|Does my browser support Media Source Extensions?|For streaming playback for work (DASH, HLS) your browser should support Media Source Extension. See the [Can I Use](https://caniuse.com/#feat=mediasource) website.
|Does my browser support Encrypted Media Extensions?|For DRM content to playback, check the support matrix for EME on the browser and confirm the needed DRM is configured for targeting that browser. See the [Can I Use](https://caniuse.com/#feat=eme) website.
|Does my browser or target device support HEVC/H.265 video playback?|See the [Can I Use](https://caniuse.com/#feat=hevc) website. For device support of HEVC, engage the device manufacturer to determine the hardware release that includes support.
|Does my browser support H.264/AVC video playback?|See the [Can I Use](https://caniuse.com/#feat=mpeg4) website.
|Why will my video not play on an Android model?|Successful playback on Android devices requires device capabilities, graphics support, codec rendering, OS support and more. The Android open source platform allows phone manufacturers to change the base Android OS. This caused fragmentation in Android compatibility for video and audio playback. Some devices are not supported because of a lack in features. Some Android devices do not have support for popular codecs (HEVC, AAC, H.264).


### HEVC support

**Apple iOS and HEVC**

For iOS devices, HEVC playback was in iOS 11.0 or higher. iPhone X, iPhone 8/Plus, iPhone 7/6s/6/Plus. Not all phone models can play back 4K and might be limited to specific resolutions and frame rate requirements. For example, iPhone 6/Plus can play HEVC video only up to 1080p at 240fps.
iPhone XS/XR/X, iPhone 8/Plus, iPhone 7/6s/Plus with Apples A9, A10 chipset (or later) support up to 4K 2160p playback at common frame rates.

For supported Apple devices for HEVC, search HEVC in the [Apple support system](https://support.apple.com/kb/index?page=search&q=HEVC&product=&doctype=SPECIFICATIONS&currentPage=1&includeArchived=false&locale=en_US).

**Android and HEVC**

Android supports HEVC in Android 5.0+ on certain OEM hardware:

- Chromecast Ultra supports HEVC
- Android mobile has support for HEVC, but typically only up to Main Level 3 on mobile devices (limited support). See [video formats and codecs supported by Android mobile.](https://developer.android.com/guide/topics/media/media-formats#video-codecs).
- Android TV support for HEVC up to Main Level 4.1. See [video formats and codecs supported by Android TV](https://developer.android.com/guide/topics/media/media-formats#video-codecs) for details.


### Resources

* [Azure Media Player Error Codes](/azure/media-services/azure-media-player/azure-media-player-error-codes)
* [Azure Media Player overview](/azure/media-services/azure-media-player/azure-media-player-overview)
* [Azure Media Player documentation](/azure/media-services/azure-media-player/azure-media-player-overview)
* [Azure Media Player sample streams](https://github.com/Azure-Samples/azure-media-player-samples)
* [Azure Media Player changelog](https://amp.azure.net/libs/amp/latest/docs/changelog.html)

### Relevant results from the web
<azureKB>
	<client>portal</client>
</azureKB>
