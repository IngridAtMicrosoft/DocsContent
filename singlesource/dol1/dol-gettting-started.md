---
title: Getting started
description: This is a repository for a single source prototype.
author: jonpayne
ms.topic: article
ms.date: 12/01/2022
ms.author: jopayn
ms.reviewer: jopayn
ms.lastreviewed: 12/01/2022
ms.service: media-services
---

# Overview

This hands-on lab shows how to use Media Services for encoding, streaming, and content protection. By the end of the lab, you
will have a web site for a video you created, with content protection.

Feel free to adapt this lab to things that you want to learn. If you want to follow along using Java instead of C#, that's fine.

[!INCLUDE [<get-help>](includes/get-help.md)]

# Setup

For this lab, you will need Visual Studio (any recent version should be fine). You can download it from the [Visual Studio web site](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise).

When installing Visual Studio, ensure the `Azure Development` option is checked. While Visual Studio is being installed, continue to the next step.

# Creating a Media Services account

You will also need a Media Services account to complete this lab. To create an account:

1. Go to the [Azure Portal](https://portal.azure.com/) and sign in with your Microsoft credentials
1. Select the hamburger (three horizontal lines) icon in the top left corner, then pick the first option, "Create a resource"
1. In the search box, enter `Media Services` and then select Media Services from the options
1. Select `Create` on the first page, then on the second page
   - Select a subscription (ping Jon Payne if your not sure what subscription to use)
   - Click the `Create new` text for the Resource Group and pick a name, for example "{your-alias}rg"
   - Enter a Media Services account name, for example "{your-alias}media"
   - Pick a Location, for example `West US 2`
   - Click the `Create a new storage account` text and pick a name, for example "{your-alias}store" (the other options are fine)
   - Do not check the `Enable classic API` option
   - Click `Create a new user-assigned managed identity` option and pick a name, for example "{your-alias}id"
   - Finally tick the "I have all the rights..." option, then press `Review + Create`

Make a note of the resource group name and account name. You will also need the subscription ID which is shown once the account has been created.

While the Media Services account is being created, continue to the next step.

# Create a video

Using your cell phone or webcam, record a 30 second video and copy it to your PC (on iPhones, click share, then `Copy iCloudLink`, then email the link to yourself).

*Continue to [Connecting to Media Services using .NET](dol-connecting.md) -->*