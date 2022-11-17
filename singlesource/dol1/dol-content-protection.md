---
title: Content Protection
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Content Protection

[!INCLUDE [<get-help>](includes/get-help.md)]

## Content Protection configuration

Next, we will configure Media Services to encrypt the media content and to only provide the decryption key to users with a valid token.

Only give viewers access to the content key that can decrypt media if they have a valid JWT token. Tokens provided by viewers must have:
- An issuer claim with the value `urn:microsoft:azure:mediaservices`
- An audience claim with the value `urn:microsoft:azure:mediaservices`
- The token must not be expired
- The token must be signed using the `HS256` algorithm using a token signing key that we will provide to Media Services

To configure this, first add this method at the end of the file:

```csharp
static async Task<ContentKeyPolicyResource> CreateContentKeyPolicyAsync(
    MediaServicesAccountResource mediaServices,
    string password,
    string runIndex)
{
    Console.WriteLine("Creating content key policy");

    var configuration = new ContentKeyPolicyClearKeyConfiguration();

    var restriction = new ContentKeyPolicyTokenRestriction(
        issuer: "urn:microsoft:azure:mediaservices",
        audience: "urn:microsoft:azure:mediaservices",
        primaryVerificationKey: new ContentKeyPolicySymmetricTokenKey(DeriveKey(password)),
        restrictionTokenType: ContentKeyPolicyRestrictionTokenType.Jwt);

    return (await mediaServices.GetContentKeyPolicies().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"ckp-{runIndex}",
        new ContentKeyPolicyData
        {
            Options =
            {
                new ContentKeyPolicyOption(configuration, restriction) { Name = "option1" }
            }
        })).Value;
}

static string CreateToken(string password)
{
    var tokenKey = new SymmetricSecurityKey(DeriveKey(password));

    return new JsonWebTokenHandler().CreateToken(new SecurityTokenDescriptor
    {
        Expires = DateTime.UtcNow.AddHours(4),
        Issuer = "urn:microsoft:azure:mediaservices",
        Audience = "urn:microsoft:azure:mediaservices",
        SigningCredentials = new SigningCredentials(tokenKey, SecurityAlgorithms.HmacSha256),
    });
}

static byte[] DeriveKey(string password)
{
    return SHA256.HashData(Encoding.UTF8.GetBytes(password)).Take(16).ToArray();
}
```

The `CreateStreamingLocatorAsync` method should be updated to set the Content Key Policy:

```csharp
static async Task<StreamingLocatorResource> CreateStreamingLocatorAsync(
    MediaServicesAccountResource mediaServices,
    MediaAssetResource outputAsset,
    ContentKeyPolicyResource contentKeyPolicy,
    string runIndex)
{
    Console.WriteLine("Creating streaming locator");

    return (await mediaServices.GetStreamingLocators().CreateOrUpdateAsync(
        WaitUntil.Completed,
        $"locator-{runIndex}",
        new StreamingLocatorData
        {
            AssetName = outputAsset.Data.Name,
            StreamingPolicyName = "Predefined_ClearKey",
            DefaultContentKeyPolicyName = contentKeyPolicy.Data.Name
        })).Value;
}
```

To simplify key management, this example derives a key from a string. Add this variable after the line where `videoPath` is set.
```csharp
var password = "apple fish pen"; // update this to any value you like
```

Finally, replace the line containing `await CreateStreamingLocatorAsync` with the following lines:
```csharp
var contentKeyPolicy = await CreateContentKeyPolicyAsync(mediaServices, password, runIndex);
var streamingLocator = await CreateStreamingLocatorAsync(mediaServices, outputAsset, contentKeyPolicy, runIndex);

Console.WriteLine($"Playback token: {CreateToken(password)}");
```

## Watching the video

Run the application and try playing the video using the player link provided. The video should fail to play as the player does not have a token.

In the player, tick `Advanced Options`, then tick the `AES` box, and paste in the example token printed by the application. The video should now play.

This demonstrates that only users who can obtain valid tokens are able to watch the content. The encrypted media data can is accessible to anyone and can be cached by a CDN, enabling media to be distributed to very large audiences, but to decrypt and view the media, viewers must have a valid token to access the content key.

*Continue to [Building a web site](dol-web.md) -->*