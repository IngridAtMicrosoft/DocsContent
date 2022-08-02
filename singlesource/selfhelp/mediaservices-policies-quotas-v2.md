<properties
  articleid="apollo-mediaservices-policies-quotas"
  cloudenvironments="blackforest,fairfax,mooncake,public,usnat,ussec"
  description="Apollo migrated file - Manage access policies quotas"
  ms.author="jiayali"
  ownershipid="StorageMediaEdge_Media"
  pagetitle="Manage access policies quotas"
  problemids=""
  productpesids="14885"
  resourcerequired="False"
  resourcetags=""
  selfhelptype="apollo"
  supporttopicids="5d0175e0-fdc9-ecdd-07a2-9962b8c06ec1" />
# Manage access policies quotas

## Manage access policies quotas in Media Services


You should try to design a limited set of policies in your Media Services account and reuse them when possible.

In Media Services v3, Streaming Policies have a default (soft) limit of 100. Try to reuse them for your Streaming Locators whenever the same encryption options and protocols are needed.  

In Media Services v2 (legacy), there is a default limit of 1,000,000 policies for different policies (for example, for Locator policy or ContentKeyAuthorizationPolicy). Use the same policy ID if you are always using the same days/access permissions, for example, policies for locators that are intended to remain in place for a long time (non-upload policies).

### Resources

* [Azure Media Services v3 quotas and limitations](https://docs.microsoft.com/azure/media-services/latest/limits-quotas-constraints-reference) <br>
* [Media Services v2 (legacy) quotas and limitations](https://docs.microsoft.com/azure/media-services/previous/media-services-quotas-and-limitations)

 ### Here are some relevant results from the web
<azureKB>
    <client>portal</client>
</azureKB>