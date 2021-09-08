---
title: Welcome to Single Source 
description: This is a repository for a single source prototype.
author: IngridAtMicrosoft
ms.topic: article
ms.date: 09/08/2021
ms.author: inhenkel
ms.reviewer: inhenkel
ms.lastreviewed: 09/08/2021
ms.service: media-services
---

# Single source introduction

This repo is dedicated to using single source documentation principles with GitHub. The pages here are for modeling and experimenting with content reuse.

Our organization doesn't use a component content management system. GitHub is used not just for publishing but for content development.  The general idea is "Docs as Code". That means that documentation is treated the same way code is treated.  With that in mind, content should be considered an object the same way an object is understood in Object Oriented Programming (OOP).

## Structure, but no awareness

The goal here is to define content objects so that they are reusable and extendable.  Darwin Typing Information Architecture (DITA) has already defined content objects within its schema.  The schema is then used to make certain that the content follows the schema as it is being written. Additionally, each topic has a unique identifier that is used to identify the topic for inclusion into a larger document. It has properties such as audience as well as variables that are used for things such as product names. Component content management systems also are aware of where topics have been used so that the writer can understand the context of the content itself.

In the DevRel model, we use Markdown which is more or less without a schema except for what is checked by a linter.  We make content modular by using includes that use the file name and relative path to identify the content to be aggregated into a larger document.  However, this cannot be considered a unique identifier because the file may be moved and its path changed.  There is no database in our publishing system that gives content an identifier that persists with the file. The only awareness we have of files that have been moved or deleted is the table of contents and when a file is linked to or included by other documents.  In that case, the links break and we get warnings in our pull requests.

We don't have a component content management system that can tell us what content is currently available for reuse. Therefore, the same content gets written over and over again within the same repo and across repos.  Add external contributors who also have no awareness of what is currently available, and there is further duplication. So the problem of scaling could be addressed by making the system more aware of what is available for reuse. Creating a content management system on top of the GitHub system would be expensive and negate the whole point of scaling resources to create content.

Therefore, this repo attempts to make efficient use of the current limitations by:

- Making the content itself modular.
- Providing templates.
- Creating an architecture that facilitates modularity.
- Extending the linter so that the content follows a DITA-like schema.
- Extending the linter so that search engine optimization techniques are included such as limiting the title lengths.

## Decoupling content development from publishing

Another possibility would be to separate content development from content publishing. SharePoint has awareness.  The biggest problem is round-tripping. More on this later.

## Windows Server content

This repo uses Windows Server content as sample content because the content is badly in need of an overhaul so experiments with it will be happening here.
