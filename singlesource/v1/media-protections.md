---
title: Media Protections
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Protections

Media stream outputs can protected using media protections. Each media stream output with
media protection option is encrypted with a content key. Authorized viewers can use tokens
to access the content key for a media stream output.

Tokens used in request media content key requests are signed with a token signing certificate, stored in
Azure Key Vault. The token signing certificate is accessed a managed identity associated with the media stream account.

## Creating a token signing certificate

Each media protection option requires a token signing certificate, stored in an Azure Key Vault.

Creating a token signing certificate:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-create-certificate>](../includes/csharp-content-protection-create-certificate.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-create-certificate](../includes/http-content-protection-create-certificate.md)]

---

## Creating a media protection option

To create a token protection option, specify the enabled content protection methods (currently only clear key is supported),
the token protection certificate, and the managed identity that should be used to access the token protection certificate.

The managed identity must be associated with the media stream account and must be granted the `Sign` permission for the Key Vault
certificate.

The token signing certificate may either be specified as a Key Vault certificate URI with a version identifier or a URI without
version information. When version information is not provided, Media Services will accept tokens signed with any matching, valid,
and enabled certificate.

#### [C#](#tab/csharp)

[!INCLUDE [<notes-for-csharp-setup>](../includes/notes-for-csharp-setup.md)]
[!INCLUDE [<csharp-arm-client-setup>](../includes/csharp-arm-client-setup.md)]

Creating a media protection option:

[!INCLUDE [<csharp-content-protection-option-create>](../includes/csharp-content-protection-option-create.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-create](../includes/http-content-protection-option-create.md)]

---

## Using a media protection option in a media stream

Each output of a media stream may have a media protection option. When a media protection option is set
for a media stream output, a content key will be generated for the output and the output properties
will contain the ID of the content key.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-media-stream-with-media-protection-options>](../includes/csharp-media-stream-with-media-protections.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-with-media-protection-options](../includes/http-media-stream-with-media-protections.md)]

---

## Media protection tokens

To playback media using media protection option, the player must request the content key using a token.

Tokens must have an audience of `urn:microsoft:azure:mediaservices` and a `urn:microsoft:azure:mediaservices:contentkeyidentifier`
claim containing the content key of the output. Tokens must be signed using the token signing certificate.

```csharp
var signingCertificate = GetSigningCertificate(); // read the token signing certificate from Key Vault

var token = new JsonWebTokenHandler().CreateToken(new SecurityTokenDescriptor
{
    Claims = new Dictionary<string, object>
    {
        {
            "urn:microsoft:azure:mediaservices:contentkeyidentifier",
            "47f91083-74b4-455a-8d9b-86efbc86e0b0"
        }
    },
    Expires = DateTime.UtcNow.AddHours(4),
    Audience = "urn:microsoft:azure:mediaservices",
    SigningCredentials = new X509SigningCredentials(signingCertificate),
});
```

## Media playback using tokens

Tokens may be embedded in HTML pages by a web server. The following example shows how a ASP.NET Core Razor
page can render a player with a content key token.

```csharp

@page
@using System.Security.Claims
@using Microsoft.IdentityModel.JsonWebTokens
@using Microsoft.IdentityModel.Tokens

@{
    var signingCertificate = GetSigningCertificate(); // read the token signing certificate from Key Vault

    var token = new JsonWebTokenHandler().CreateToken(new SecurityTokenDescriptor
    {
        Claims = new Dictionary<string, object>
        {
            {
                "urn:microsoft:azure:mediaservices:contentkeyidentifier",
                "47f91083-74b4-455a-8d9b-86efbc86e0b0"
            }
        },
        Expires = DateTime.UtcNow.AddHours(4),
        Audience = "urn:microsoft:azure:mediaservices",
        SigningCredentials = new X509SigningCredentials(signingCertificate),
    });
}

<HeadContent>
  <link href="//amp.azure.net/libs/amp/latest/skins/amp-default/azuremediaplayer.min.css" rel="stylesheet">
  <script src="//amp.azure.net/libs/amp/latest/azuremediaplayer.min.js"></script>
</HeadContent>

<video class="azuremediaplayer" autoplay controls>
  <source src="//stream.azure.media.net/2ddc6abd-2d3d-4b30-a696-754bb90d3a8a"
    type="application/vnd.ms-sstr+xml"
    data-setup='{"protectionInfo": [{"type": "AES", "authenticationToken": "Bearer=@token"}]}' />
</video>

```

## Media protection options operations

### Updating a media protection option

Media protection options may be updated to change the token signing key.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-option-update>](../includes/csharp-content-protection-option-update.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-update](../includes/http-content-protection-option-update.md)]

---

### Listing media protections

Media protection options may be listed using the service API.

> [!NOTE]
> The API does not provide support for filtering or sorting lists of media protections. If your application requires
a large number of media protections, consider using a database to store media protections metadata.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-option-list>](../includes/csharp-content-protection-option-list.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-list](../includes/http-content-protection-option-list.md)]

---

### Deleting a media protection option

A media protection option may be deleted if it is not used by any media stream output. If any media stream output
is using a media protection option, requests to delete the media protection option will fail.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-option-delete>](../includes/csharp-content-protection-option-delete.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-delete](../includes/http-content-protection-option-delete.md)]

---

## Media protection options limits and billing

A media stream account may have up to one thousand media protections. There is no charge for creating a media protection
option. Requests to access keys using a media protection option are billed.