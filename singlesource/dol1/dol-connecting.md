---
title: Connecting
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Connecting

## Connecting to Media Services using .NET

Next we will encode the video file using .NET code, so we can see a typical customer work flow.

First we need to create a new project in Visual Studio:
1. Start Visual Studio
1. Select `Create a new project`
1. Select the `Console App` item with the `C#` tag (it should be the first item), then press `Next`
1. Pick a name for your project, for example `MediaServicesLab`, and press `Next`
1. Set the framework to `.NET 6.0` or `.NET 7.0` (either is fine) then press `Create`
1. When the project is ready, you can click the hollow green play button in the toolbar to run the project

Now we need to connect to Media Services:
1. From the menu, select `Tools` -> `NuGet Package Manager` -> `Package Manager Console`
1. In the Package Manager window, enter these commands:
```powershell
NuGet\Install-Package Azure.Identity
NuGet\Install-Package Azure.ResourceManager.Media
NuGet\Install-Package Azure.Storage.Blobs
NuGet\Install-Package System.Linq.Async
```
1. Replace all the code in the `Program.cs` file with the following text:
```csharp
using Azure;
using Azure.Identity;
using Azure.ResourceManager;
using Azure.ResourceManager.Media;
using Azure.ResourceManager.Media.Models;
using Azure.Storage.Blobs;
using System.Security.Cryptography;
using System.Text;

var runIndex = DateTime.UtcNow.Ticks.ToString();

var mediaServicesAccountIdentifier = MediaServicesAccountResource.CreateResourceIdentifier(
    subscriptionId: "--update this text--", // this should be in the format 00000000-0000-0000-0000-000000000000
    resourceGroupName: "--update this text--",
    accountName: "--update this text--");

var videoPath = @"C:\Media\video1.mp4"; // set this to the path to your video

var credential = new DefaultAzureCredential(
    new DefaultAzureCredentialOptions
    {
        ExcludeManagedIdentityCredential = true,
        ExcludeInteractiveBrowserCredential = false
    });

var armClient = new ArmClient(credential);

MediaServicesAccountResource mediaServices =
    await armClient.GetMediaServicesAccountResource(mediaServicesAccountIdentifier).GetAsync();

Console.WriteLine($"Using Media Services account with ID {mediaServices.Data.MediaServicesAccountId}");

//var transform = await CreateTransformAsync(mediaServices);
//var outputAsset = await EncodeFileAsync(mediaServices, transform, videoPath, runIndex);
//var streamingEndpoint = await StartStreamingEndpointAsync(mediaServices);
//var streamingLocator = await CreateStreamingLocatorAsync(mediaServices, outputAsset, runIndex);

//var streamingUri = $"https://{streamingEndpoint.Data.HostName}/{streamingLocator.Data.StreamingLocatorId}/input.ism/manifest";

//Console.WriteLine($"Steaming URL: {streamingUri}");
//Console.WriteLine();
//Console.WriteLine($"Watch your video at: https://aka.ms/azuremediaplayer?url={Uri.EscapeDataString(streamingUri)}");
```
1. Update the `subscriptionId`, `resourceGroupName`, and `accountName` to the values you used when creating your Media Services account
1. Update `videoPath` to the location of your video file
1. Click the hollow green play button in the toolbar to run the project

If everything works, the code should run and print the ID of the Media Services account. You may be asked to sign in each time your run this code -- to avoid this, select `File` -> `Account Settings` then sign in to your account using Visual Studio.

This code is:
- Getting a token to connect to Azure Resource Manager
- Generating a request Azure Resource Manager to get details about your account
- Printing some account details

*Continue to [Encoding and Streaming](dol-encoding-and-streaming.md) -->*