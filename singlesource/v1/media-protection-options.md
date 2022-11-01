---
title: Media Protection Options
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Media Protection Options

Access to media streams can be restricted by setting a media protection option for a media stream output.
Each media stream output with media protection enabled is encrypted with a different content keys. Viewers
can access the content key required to view an output by presenting a valid token to the content key server.

Tokens used to request content keys are encrypted with a token signing key, stored in Azure Key Vault. The token
signing key is accessed a Managed Identity of the media account.

## Creating a token validation certificate

Each media protection option requires a token signing certificate, stored in an Azure Key Vault.

Creating a certificate for token validation:

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-create-certificate>](../includes/csharp-content-protection-create-certificate.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-create-certificate](../includes/http-content-protection-create-certificate.md)]

---

## Creating a media protection option

To create a token protection option, specify the enabled content protection methods (currently only clear key is supported),
the token protection certificate, and the managed identity that should be used to access the token protection certificate.

The managed identity must be associated with the media account and must be granted the `Sign` permission for the Key Vault
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

[!INCLUDE [<csharp-media-stream-with-media-protection-options>](../includes/media-stream-with-media-protection-options.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-media-stream-with-media-protection-options](../includes/http-media-stream-with-media-protection-options.md)]

---

## Media protection tokens

To playback media using media protection option, the player must request the content key using a token.

Tokens must have an audience of `urn:microsoft:azure:mediaservices` and a `urn:microsoft:azure:mediaservices:contentkeyidentifier`
claim containing the content key of the output. Tokens must be signed using the token signing certificate.

#### [C#](#tab/csharp)

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
---

## Media playback using tokens

Tokens may be embedded in HTML pages by a web server. The following example shows how a ASP.NET Core Razor
page can render a player with a content key token.

```csharp

@page
@using System.Security.Claims
@using Microsoft.IdentityModel.JsonWebTokens
@using Microsoft.IdentityModel.Tokens

@{
    var signingCertificate = GetSigningCertificate();

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

Media streams can be updated to add or remove outputs. The enabled property of outputs may also be updated.

#### [C#](#tab/csharp)

[!INCLUDE [<csharp-content-protection-option-update>](../includes/csharp-content-protection-option-update.md)]

#### [HTTP](#tab/http)

[!INCLUDE [<http-content-protection-option-update](../includes/http-content-protection-option-update.md)]

---

### Listing media protection options

Media protection options may be listed using the service API.

> [!NOTE]
> The API does not provide support for filtering or sorting lists of media protection options. If your application requires
a large number of media protection options, consider using a database to store media protection options metadata.

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

A media account may have up to one thousand media protection options. There is no charge for creating a media protection
option. Requests to access keys using a media protection option are billed.