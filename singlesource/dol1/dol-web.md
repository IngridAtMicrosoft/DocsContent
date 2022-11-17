---
title: Building a Web Site
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Building a Web Site

[!INCLUDE [<get-help>](includes/get-help.md)]

Next we will build a web site where Microsoft employees can view the video.

First we need to create a Web App:

1. Go to the [Azure Portal](https://portal.azure.com/) and sign in with your Microsoft credentials
1. Select the hamburger (three horizontal lines) icon in the top left corner of the page, then pick the first option, "Create a resource"
1. Select `Web App` from the list of popular Azure services
1. Select the same subscription and resource group as you used when creating the Media Services account
1. Pick a name for the site, for example `{your-alias}-web`
1. Leave the Publish option set to `Code`
1. Set the runtime stack to `.NET 6 (LTS)`
1. Set the operating system to `Windows` (`Linux` should also work)
1. Select a region, for example `West US 2`
1. Set the pricing plan to `Free F1` and create a new plan if necessary
1. Select `Review + Create`

Once the web site is created, we can enable authentication:

1. Select the `Authentication` option for the web app
1. Click `Add identity provider`
1. Select `Microsoft`
1. Click `Add` accepting all the default options

We now need to create a web application:

1. Start another instance of Visual Studio
1. Select `Create a new project`
1. Search for the `ASP.NET Core Empty` template and select it
1. Pick a project name and press `Next`
1. Set the framework to `.NET 6.0 (Long Term Support)` and press `Create`
1. From the menu, select `Tools` -> `NuGet Package Manager` -> `Package Manager Console`
1. In the Package Manager window, enter these commands:
```powershell
NuGet\Install-Package Microsoft.IdentityModel.JsonWebTokens
```
1. Replace the contents of `Program.cs` with the following code:
```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddRazorPages();
var app = builder.Build();

app.UseRouting();
app.MapRazorPages();
app.Run();
```
1. Right click on the web application project in the Solution Explorer window and select `Add` -> `New Folder`
1. Name the folder `Pages`
1. Right click on the `Pages` folder and select `Add` -> `Razor Page`, then select `Razor Page - Empty`, then press `Add`
1. Name the page `Index.cshtml` and press `Add`
1. Replace the contents of `Index.cshtml` with the following code:
```csharp
@page
@using System.Security.Claims
@using System.Security.Cryptography;
@using System.Text;
@using Microsoft.IdentityModel.JsonWebTokens
@using Microsoft.IdentityModel.Tokens

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>Azure Media Demo</title>
  <link href="//amp.azure.net/libs/amp/latest/skins/amp-default/azuremediaplayer.min.css" rel="stylesheet">
  <script src="//amp.azure.net/libs/amp/latest/azuremediaplayer.min.js"></script>
</head>

@{
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

    var token = CreateToken(password: "apple fish pen");
    var source = "https://mymedia-usw22.streaming.media.azure.net/00000000-0000-0000-0000-000000000000/input.ism/manifest";
}

<body>
  <h1>Azure Media Demo</h1>
  <video id="azuremediaplayer" class="azuremediaplayer amp-default-skin" autoplay controls width="1280" height="720" data-setup='{}'>
    <source src="@source" type="application/vnd.ms-sstr+xml" data-setup='{"protectionInfo": [{"type": "AES", "authenticationToken": "Bearer=@token"}]}' />
  </video>
</body>

</html>
```
1. Update the `token` line to use the password you created in the previous section
1. Update the `source` property to use the streaming URL printed by the encoding application

Publish the web site:
1. Right click on the web application project in the Solution Explorer window and select `Publish`
1. Select `Azure` and press `Next`
1. Select `Azure App Service (Windows)` and press `Next`
1. Sign in if necessary, then select the web application you created
1. Press `Finish` then `Close`
1. Press the `Publish` button
1. When the publish process is complete, click `Open site`
1. Log in to the site and grant the site permission to read your Azure Active Directory account name
1. Play your video!

If you want to, share your web site address in the meeting Teams chat.

*Continue to [Cleanup](dol-cleanup.md) -->*