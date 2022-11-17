---
title: Encoding and Streaming
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Creating a Transform

To prepare a media file for streaming, we have a Transform resource that tells Media Services how the source video should be transformed into a streaming video. For this example we will use a Transform with the built-in Content Aware Encoding preset. This transform will convert our single bitrate input file into a multi bitrate output that can stream on a wide variety of devices and network conditions.

Add the following code to the end of the file:
```csharp
static async Task<MediaTransformResource> CreateTransformAsync(
    MediaServicesAccountResource mediaServices)
{
    Console.WriteLine("Creating transform");

    var transformName = "content-aware-transform";

    if (await mediaServices.GetMediaTransforms().ExistsAsync(transformName))
    {
        return await mediaServices.GetMediaTransforms().GetAsync(transformName);
    }

    return (await mediaServices.GetMediaTransforms().CreateOrUpdateAsync(
        WaitUntil.Completed,
        "content-aware-transform",
        new MediaTransformData
        {
            Outputs = { new MediaTransformOutput(new BuiltInStandardEncoderPreset(EncoderNamedPreset.ContentAwareEncoding)) }
        })).Value;
}
```

Then uncomment the line that creates the transform, by changing this line:
```csharp
//var transform = await CreateTransformAsync(mediaServices);
```

To be:
```csharp
var transform = await CreateTransformAsync(mediaServices);
```

If you run the project now, the transform will be created.

# Running an encoding Job

Next we need to upload our video and run a Job using the Transform we created. To do this, add the following code:

```csharp
static async Task<MediaAssetResource> EncodeFileAsync(
    MediaServicesAccountResource mediaServices,
    MediaTransformResource transform,
    string videoPath,
    string runIndex)
{
    Console.WriteLine("Creating input asset");
    var inputAsset = (await mediaServices.GetMediaAssets().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"input-asset-{runIndex}",
        new MediaAssetData())).Value;

    var inputAssetSas = await inputAsset.GetStorageContainerUrisAsync(
        new MediaAssetStorageContainerSasContent
        {
            ExpireOn = DateTime.UtcNow.AddHours(1),
            Permissions = MediaAssetContainerPermission.ReadWriteDelete
        }).FirstOrDefaultAsync();

    Console.WriteLine("Uploading input asset media");
    var inputAssetContainer = new BlobContainerClient(inputAssetSas);
    var inputAssetBlob = inputAssetContainer.GetBlobClient("input.mp4");
    await inputAssetBlob.UploadAsync(videoPath);

    Console.WriteLine("Creating output asset");
    var outputAsset = (await mediaServices.GetMediaAssets().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"output-asset-{runIndex}",
        new MediaAssetData())).Value;

    Console.WriteLine("Starting encoding job");
    var job = (await transform.GetMediaJobs().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"job-{runIndex}",
        new MediaJobData
        {
            Input = new MediaJobInputAsset(inputAsset.Data.Name),
            Outputs = { new MediaJobOutputAsset(outputAsset.Data.Name) }
        })).Value;

    while (
        job.Data.State == MediaJobState.Processing ||
        job.Data.State == MediaJobState.Queued ||
        job.Data.State == MediaJobState.Scheduled)
    {
        Console.WriteLine($"Waiting for job to complete... {job.Data.State} {job.Data.Outputs.First().Progress}% complete");
        await Task.Delay(TimeSpan.FromSeconds(10));

        job = await transform.GetMediaJobAsync(job.Data.Name);
    }

    Console.WriteLine($"Final job state {job.Data.State}");

    return outputAsset;
}
```

This code:
- Creates an Asset to contain the input file
- Requests credentials for uploading data to the input Asset
- Uploads the video to the input Asset
- Creates an Asset to store the encoding video
- Starts an encoding Job
- Waits for the Job to complete

Uncomment the line containing `await EncodeFileAsync` line and run the project again. The source file should be encoded.

# Starting the Streaming Endpoint

Before streaming the Asset, we must start a Streaming Endpoint.

Add the following code to the end of the project:

```csharp
static async Task<StreamingEndpointResource> StartStreamingEndpointAsync(
    MediaServicesAccountResource mediaServices)
{
    StreamingEndpointResource defaultStreamingEndpoint =
    await mediaServices.GetStreamingEndpointAsync("default");

    if (defaultStreamingEndpoint.Data.ResourceState != StreamingEndpointResourceState.Running)
    {
        Console.WriteLine("Starting default streaming endpoint");
        await defaultStreamingEndpoint.StartAsync(WaitUntil.Completed);
    }

    return defaultStreamingEndpoint;
}
```

Uncomment the line containing `await StartStreamingEndpointAsync` line and run the project again. The Streaming Endpoint should be started.

# Creating a Streaming Locator

Finally, we need to create a Streaming Locator to tell the Streaming Endpoint how the Asset should be streamed.

Add the following code to the end of the file:

```csharp
static async Task<StreamingLocatorResource> CreateStreamingLocatorAsync(
    MediaServicesAccountResource mediaServices,
    MediaAssetResource outputAsset,
    string runIndex)
{
    Console.WriteLine("Creating streaming locator");
    return (await mediaServices.GetStreamingLocators().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"locator-{runIndex}",
        new StreamingLocatorData
        {
            AssetName = outputAsset.Data.Name,
            StreamingPolicyName = "Predefined_ClearStreamingOnly"
        })).Value;
}
```

Uncomment all the remaining lines and run the project again.

# Watching the video

If everything worked, the application should print out a URL that allows you to watch the video.

This is a lot of work to watch one video, but there are some good points:
- It is trivial to enable a CDN for the Streaming Endpoint, allowing us to stream to global audiences of almost any size
- We can add content protection to the video to restrict who can watch the video
- The video should play back on almost any device under a wide range of network conditions

*Continue to [Content Protection](dol-content-protection.md) -->*