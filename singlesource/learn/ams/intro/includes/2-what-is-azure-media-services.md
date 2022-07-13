Let's start with talking about video streaming in general, and then look at some of the Azure Media Services scenarios. This overview should help you determine whether the Azure Media Services platform is a good fit for delivering streaming media.

## What is media streaming?

Video and audio content can be quite large. Think of how large a file for an entire, full length movie would have to be. It would take forever to download it before the viewer could enjoy it. Streaming is a way of delivering digital media to an end user in small chunks so that it can be played sooner. Additionally, streaming is a way to protect copyrighted content from being distributed without your consent, or distributed *with* your consent.

*Encoding* is the process of converting files containing digital video and/or audio from one standard format to another, with the purpose of:

- reducing the size of the files, and/or
- producing a format that's compatible with a broad range of devices and apps.

This process is also referred to as video compression, or transcoding. Videos are typically delivered to devices and apps by progressive download or through adaptive bitrate streaming.

**Live streaming** is when an event, such as a sporting event is captured by a on-premises encoder and streamed over the Internet.  Video on demand (VOD) applications, can be used for delivering a library of videos to customer when they need it. You may want to create a subscription service where your customers are given privileged access to extra live content that non-subscribers don't have access to. Live streaming is when you are using an on-premises encoder, such as OBS Studio or Wirecast to broadcast an event that is happening in real time. With Azure Media Services, you will create a live event and the broadcast or contribution feed to it. You may or may not want to keep that video for your viewers to see after the event is over. In that case, the video would be archived to storage and delivered via video on demand (VOD).

**Video on demand (VOD)** is when you have a set of videos that you want to deliver to your viewers now and in the future.

**Digital Rights Management (DRM)**, is a way of restricting access to your content through encryption, streaming policies, and content keys. A streaming policy specifies encryption options for your stream.  A content key and a content key policy are used to provide secure access to your content. You would set the requirements (restrictions) on the content key policy that must be met in order for keys to be delivered to clients.

When a stream is requested by a player, the service evaluates the content key policy to decide if the user is authorized to get the key, the service evaluates the content key policy that you specified for the key.

## Azure Media Services definition

Azure Media Services is a cloud-based platform that enables you to build applications to deliver high-quality video streaming, ensuring secured distribution to large audiences on today's most popular mobile devices and browsers.

Media Services lets you build a variety of media workflows in the cloud. Some examples of what you can do with Media Services include:

- Deliver videos in various formats so they can be played on a wide variety of browsers and devices. For both on-demand and live streaming delivery to various clients (mobile devices, TV, PC, and so on), the video and audio content needs to be encoded and packaged appropriately. To see how to deliver and stream such content, see Quickstart: Encode and stream files.
- Stream live sporting events to a large audience, like soccer, baseball, college and high school sports, and more.
- Broadcast public meetings and events, like town halls, city council meetings, and legislative bodies.
- Create a subscription video service and stream DRM protected content when a customer (for example, a movie studio) needs to restrict the access and use of proprietary copyrighted work.
- Deliver offline content for playback on airplanes, trains, and automobiles. A customer might need to download content onto their phone or tablet for playback when they anticipate to be disconnected from the network.
- Enable Azure CDN to achieve large scaling to better handle instantaneous high loads (for example, the start of a product launch event).

The rest of this module will describe how Azure Media Services works, and when to use it.
