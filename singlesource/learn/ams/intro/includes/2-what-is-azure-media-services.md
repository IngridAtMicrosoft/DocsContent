Let's start with a few definitions and a quick tour of the core features of Azure Media Services.  This overview should help you determine whether the Azure Media Services platform is a good fit for delivering streaming media.

## What is media streaming?

Video and audio content can be quite large. Think of how large a file for an entire, full length movie would have to be. It would take forever to download it before the viewer could enjoy it. Streaming is a way of delivering digital media to an end user in small chunks so that it can be played sooner. Additionally, streaming is a way to protect copyrighted content from being distributed without your consent, or distributed *with* your consent.

Live streaming, such as when a sporting event is being broadcast over the Internet, is another example of streaming.  You may want to create a subscription service where your customers are giving privileged access to extra live content that non-subscribers don't have access to.

## What is encoding?

The term *encoding* in Media Services applies to the process of converting files containing digital video and/or audio from one standard format to another, with the purpose of:

- reducing the size of the files, and/or
- producing a format that's compatible with a broad range of devices and apps.

This process is also referred to as video compression, or transcoding.

Videos are typically delivered to devices and apps by progressive download or through adaptive bitrate streaming.

## What is video on demand (VOD)?

Video on Demand is when you have a set of videos that you want to deliver to your viewers now and in the future.

## What is live streaming?

Live streaming is when you are using an on-premises encoder, such as OBS Studio or Wirecast to broadcast an event that is happening in real time. With Azure Media Services, you will create a live event and the broadcast or contribution feed to it.

You may or may not want to keep that video for your viewers to see after the event is over. In that case, the video would be archived to storage and delivered via VOD.

## What is content protection?

Also known as Digital Rights Management (DRM), is a way of restricting access to your content through encryption, streaming policies, and content keys. A streaming policy specifies encryption options for your stream.  A content key and a content key policy are used to provide secure access to your content. You would set the requirements (restrictions) on the content key policy that must be met in order for keys to be delivered to clients.

When a stream is requested by a player, the service evaluates the content key policy to decide if the user is authorized to get the key, the service evaluates the content key policy that you specified for the key.

## Azure Media Services definition

Azure Media Services is a cloud-based platform that enables you to build applications to deliver high-quality video streaming, ensuring secured distribution to large audiences on today's most popular mobile devices and browsers.

The rest of this module will describe how Azure Media Services works, and when to use it.