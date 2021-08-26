---
title: How-to template 
description: This article is a template for creating How-tos.  It contains a list of SEO rules and guidance for writing.
author: IngridAtMicrosoft
ms.author: inhenkel
ms.topic: how-to
ms.date: 08/26/2021
ms.service: media-services
---

# How-To template

<!--
This How-to template has been created to make how-to content SEO compliant.

## SEO Rules

- At least 2 but no more than 5 H2 level headings.  If you have more than that, then you are teaching too much. Consider breaking the content down into two or more how-tos.
- Titles should be no longer than 70 characters and should not break into a second line.
- The title in the metadata should match the title in the document.
- If possible, the title in the TOC should match the title of the document. Otherwise remove articles from the title and see if that works.
- Descriptions should be long and contain as many keywords as possible.
- How-tos are task-based documents.  Introductions and interstitial paragraphs should be kept short.

## Content rules

- Screenshots should only be used when what needs to be done can't be adequately explained by text.
- Screenshot alt-text should describe what is in the image.  Make an effort at describing what you see.
- Diagrams should **NOT** be used in How-Tos they are for explaining architectures/sequences (see UML standards) and are more appropriate for conceptual articles.

## Visual syntax

- When describing a UI element, including screen names and wizard names, bold the name of the element. Avoid describing what the UI is because that sometimes changes.  For example:
    
    Correct:<br/>
    Select **Submit**.

    Incorrect:<br/>
    Select the **Submit** button.

- When describing a file name, italicize the name. For example:
    
    Select the *example.html* file.

- When describing a code element, use ` before and after the code element.  For example:
    
    The `ThingThatDoesStuff` object does things with stuff.

## Step descriptions

- Use Markdown "1." for every step and let markdown determine what number it is.
- Do **NOT** refer to a previous step to describe the current step.
- When describing an interaction, on the same step, describe the result of the action. For example:
    Select **Submit**.  The **Thank you** screen will appear.

## Instruction headings

If the How-to need to have groupings of steps and the groupings are less than five, describe the grouping with an H2 heading.  Use the directive form of the verb. Avoid using H3 headings if you can.  

Example:

## Configure the service

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **Thingy Wizard** will open.
1. Select **Not In My Back Yard**.

### Configure the back yard

1. Clean up the `LeafObject` array.
1. Delete the *oldtires.exe* file.

Use Monikers where appropriate

-->

## Same file different versions

This How-To template uses monikers.  That way, telling someone how to do something can be in one place for all versions.  If the same method applies to several versions, you designate the section with an operator preding the version such as >, <, >=, <=.

:::moniker range="windows-server-2008"

## How-to for Windows Server 2008

## H2.1.2008 for first part (See the comments in this template.)

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

## H2.2.2008 for the second part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.

## H2.3.2008 for the third part

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

### H2.4.2008 for the fourth part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.
1. Use this code block. If the code block can be included directly from a related sample or API use that method instead.

    ```python
    var codeblock
    ```

1. Save the file

## H2.5.2008 for the fifth part

If you are writing more than 5 parts then consider breaking the instruction into a couple of pages.  Think encapsulation.
:::moniker-end

:::moniker range="windows-server-2012"

## How-to for Windows Server 2012

## H2.1.2012 for first part (See the comments in this template.)

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

## H2.2.2012 for the second part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.

## H2.3.2012 for the third part

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

### H2.4.2012 for the fourth part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.
1. Do this code block. If the code block can be included directly from a related sample or API use that method instead.

    ```python
    var codeblock
    ```

1. Save the file

## H2.5.2012 for the fifth part

If you are writing more than 5 parts then consider breaking the instruction into a couple of pages.  Think encapsulation.
:::moniker-end

:::moniker range="windows-server-2016"

## How-to for Windows Server 2016

## H2.1.2016 for first part (See the comments in this template.)

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

## H2.2.2016 for the second part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.

## H2.3.2016 for the third part

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

### H2.4.2016 for the fourth part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.
1. Do this code block. If the code block can be included directly from a related sample or API use that method instead.

    ```python
    var codeblock
    ```

1. Save the file

## H2.5.2016 for the fifth part

If you are writing more than 5 parts then consider breaking the instruction into a couple of pages.  Think encapsulation.
:::moniker-end

:::moniker range="windows-server-2019"

## How-to for Windows Server 2019

## H2.1.2019 for first part (See the comments in this template.)

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

## H2.2.2019 for the second part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.

## H2.3.2019 for the third part

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

### H2.4.2019 for the fourth part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.
1. Do this code block. If the code block can be included directly from a related sample or API use that method instead.

    ```python
    var codeblock
    ```

1. Save the file

## H2.5.2019 for the fifth part

If you are writing more than 5 parts then consider breaking the instruction into a couple of pages.  Think encapsulation.
:::moniker-end

:::moniker range="windows-server-2022"

## How-to for Windows Server 2022

## H2.1.2022 for first part (See the comments in this template.)

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

## H2.2 for the second part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.

## H2.3.2022 for the third part

This is an interstitial paragraph. It gives a short explanation of what you will be doing next.  If it isn't necessary, omit it.

1. Do this. The **wizard** will open.
1. Select **UI element**.

### H2.4.2022 for the fourth part

1. Clean up the `CodeObject` array.
1. Delete the *filename.exe* file.
1. Do this code block. If the code block can be included directly from a related sample or API use that method instead.

    ```python
    var codeblock
    ```

1. Save the file

## H2.5.2022 for the fifth part

If you are writing more than 5 parts then consider breaking the instruction into a couple of pages.  Think encapsulation.
:::moniker-end
