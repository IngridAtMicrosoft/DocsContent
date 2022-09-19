---
title: Authentication or access control v2
author: IngridAtMicrosoft
ms.author: inhenkel
ms.service: media-services
ms.date: 9/19/2022
---

<!--
<properties
  articleid="apollo-mediaservices-authentication-access-control"
  cloudenvironments="public,fairfax,usnat,ussec"
  description="Apollo migrated file - Authentication or access control"
  ms.author="akucer,jiayali,inhenkel"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Authentication or access control"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="3962655e-b25d-3a69-1175-b540ce09c9da" />
-->

# Authentication or access control v2

## Resolve issues with authentication or access control in the Azure Media Services API

This article discusses Azure Media Services API access, authentication options, role assignments, and more.

### Common issues and solutions

**Gain access to Media Services API**

To gain access to Media Services resources and the Media Services API, you must first be authenticated. Media Services supports [Azure Active Directory (Azure AD)-based](/azure/active-directory/fundamentals/active-directory-whatis) authentication.

**Authenticate a person or service**

Two common authentication options are:

* **Service principal authentication**: Used to authenticate a service, for example, web apps, function apps, logic apps, API, and microservices. Applications that commonly use this authentication method are apps that run daemon services, middle-tier services, or scheduled jobs.
* **User authentication**: Used to authenticate a person who's using the app to interact with Media Services resources. The interactive app should first prompt the user for their credentials. An example is a management console app used by authorized users to monitor encoding jobs or live streaming.

**Role assignment**

The Media Services API requires that the user or app making the REST API requests have access to the Media Services account resource and use a Contributor or Owner role. To learn how to assign a role, see [Steps to assign an Azure role](/azure/role-based-access-control/role-assignments-steps).

The API can be accessed with the Reader role but only Get or List  operations will be available. For more information, see [Role-based access control for Media Services accounts](/azure/media-services/latest/security-rbac-concept).

**Managed identities**

Instead of creating a service principal, consider using managed identities for Azure resources to access the Media Services API through Azure Resource Manager.

To learn more about managed identities for Azure resources, see [What is managed identities for Azure resources](/azure/active-directory/managed-identities-azure-resources/overview).

### Resources

Media Services v3 (latest)
* [Develop with Media Services v3 APIs](/azure/media-services/latest/media-services-apis-overview)

Media Services v2 (legacy)
* [Access the Azure Media Services API with Azure AD authentication](/azure/media-services/previous/media-services-use-aad-auth-to-access-ams-api)

### Relevant results from the web
<azureKB>
	<client>portal</client>
</azureKB>
