---
title: Welcome to Single Source 
description: This is a repository for a single source prototype.
author: IngridAtMicrosoft
ms.topic: article
ms.date: 07/04/2020
ms.author: inhenkel
ms.reviewer: inhenkel
ms.lastreviewed: 08/25/2021
ms.service: windows-server
---

# Single source introduction

This repo is dedicated to using single source documentation principles with GitHub. The pages here are for modeling and experimenting with content reuse.

Our organization doesn't use a component content management system. GitHub is used not just for publishing but for content development.  The general idea is "Docs as Code". That means that documentation is treated the same way code is treated.  With that in mind, content should be considered an object the same way an object is understood in Object Oriented Programming (OOP).

## Structure, but no awareness

In OOP, objects are encapsulated.  They have properties and methods.  The goal here is to define content objects so that they are reusable and extendable.  Darwin Typing Information Architecture (DITA) has already defined content objects within its schema.  The challenge applying that schema to flat file management where there is no awareness of content such as exists within a component content management system.  Even at the most basic level, there is no unique identifier for pieces of content to be used with tracking changes.  Everything is done with manually with JSON, YML or Markdown.

## Decoupling content development from publishing

Is the answer to the challenge to decouple the content development process from the publishing process? More here later.

## Tools

Writers within the DevRel org are expected to use Visual Studio Code to develop content.  Extensions have been integrated into the tool to facilitate the established workflow.