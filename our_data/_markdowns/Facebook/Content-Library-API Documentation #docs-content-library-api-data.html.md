Data dictionary - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Data dictionary
===============

This data dictionary describes the data names displayed in the Meta Content Library web UI (the Name column) if
applicable, and the corresponding API fields returned in Meta Content Library API search responses (the API
field column). In the API field column, some fields have nested fields indicated by a dot notation. These are referred to as *expanded fields*. See Field expansion for information about how to include some or all of a parent field's expanded fields in your queries.

Facebook Page
-------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Facebook Page. | Content Library API |
| Name | name | The name of the Facebook Page. | Content Library
Content Library API |
| About | about | The short paragraph in the About section of the Facebook Page. | Content Library
Content Library API |
| Website | website | The external URL from the Facebook Page’s About section. | Content Library API |
| Description | description | The long paragraph in the About section of the Facebook Page. | Content Library
Content Library API |
| Verification status | verification\_status | The verification status of the Facebook Page. A Facebook Page with a verified badge
 indicates that Facebook has confirmed that it is the authentic presence for that person or brand. 
 Learn more. | Content Library
Content Library API |
| Page categories | page\_categories | The list of up to three categories of the Facebook Page, selected by the Page
manager. | Content Library
Content Library API |
| Location city | location.city | The self-reported, publicly accessible city location associated with the Facebook
Page. | Content Library API |
| Location country | location.country | The self-reported, publicly accessible country location associated with the Facebook
Page. | Content Library API |
| Location country code | location.country\_code | The self-reported, publicly accessible country code location associated with the Facebook
Page. | Content Library API |
| Location name | location.name | The self-reported, publicly accessible location name associated with the Facebook
Page. | Content Library API |
| Location region | location.region | The self-reported, publicly accessible region location associated with the Facebook
Page. | Content Library API |
| Location zip | location.zip | The self-reported, publicly accessible location zip associated with the Facebook
Page. | Content Library API |
| Location street | location.street | The self-reported, publicly accessible street location associated with the Facebook
Page. | Content Library API |
| Location state | location.state | The self-reported, publicly accessible state location associated with the Facebook
Page. | Content Library API |
| Page name change date | page\_transparency.page\_name\_changes.data.date | The date the Facebook Page’s name changed. | Content Library API |
| Page name old | page\_transparency.page\_name\_changes.data.old\_name | The old name of the Facebook Page prior to the name change. | Content Library API |
| Page name new | page\_transparency.page\_name\_changes.data.new\_name | The new name of the Facebook Page, following the name change. | Content Library API |
| Page merged date | page\_transparency.page\_merges.data.date | The date another Facebook Page merged with this Page. | Content Library API |
| Page merged | page\_transparency.page\_merges.data.page\_merged | The name of the Facebook Page that merged with this Page. | Content Library API |
| Creation date | creation\_date | The date the Facebook Page was created. | Content Library
Content Library API |
| Page manager countries | page\_transparency.admin\_countries.data.country | The predicted primary country locations of people who manage this Facebook
Page. | Content Library
Content Library API |
| Count of Page managers by countries | page\_transparency.admin\_countries.data.count | The number of people who manage this Facebook Page predicted to be from the associated
country. | Content Library
Content Library API |
| Page owner | page\_transparency.confirmed\_page\_owner | The confirmed owner associated with the Facebook Page. | Content Library API |
| Has active ads | page\_transparency.has\_active\_ads | Whether the Facebook Page has active ads or not. | Content Library API |
| Has run political ads | page\_transparency.has\_run\_political\_ads | Whether the Facebook Page has run political ads or not. | Content Library API |
| Followers | follower\_count | The number of followers of the Facebook Page. | Content Library
Content Library API |
| Page likes | like\_count | The number of likes of the Facebook Page. | Content Library API |
Facebook group
--------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Facebook group. | Content Library API |
| Name | name | The name of the Facebook group. | Content Library
Content Library API |
| Description | description | The description of the Facebook group. | Content Library
Content Library API |
| Creation date | creation\_date | The date the Facebook group was created. | Content Library
Content Library API |
| Group original name | group\_transparency.original\_name | The original name of the Facebook group. | Content Library API |
| Group name change date | group\_transparency.name\_changes.data.date | The date the name of the Facebook group changed. | Content Library
Content Library API |
| Group name new | group\_transparency.name\_changes.data.new\_name | The new name of the Facebook group. | Content Library API |
| Group admin and moderator Page IDs | group\_transparency.admin\_and\_moderator\_page\_ids | The list of Meta Content Library IDs of Facebook Pages that are admins or moderators of the Facebook group. | Content Library API |
| Group owner type | group\_owners.data.type | The type of the group owner associated with the Facebook group.This field will display if
the group owner is a professional profile or Page. Only the Meta Content Library Page ID will be
shared. | Content Library API |
| Group owner ID | group\_owners.data.id | The Meta Content Library ID of the Facebook group owners.This field will display if the group owner
is a professional profile or Page. Only the Meta Content Library Page ID will be shared. | Content Library API |
| Picture URL | picture\_url | The photo URL of the Facebook group. | Content Library API |
| Group members | member\_count | The number of members of the Facebook group. | Content Library
Content Library API |
Facebook event
--------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Facebook event. | Content Library API |
| Name | name | The name of the Facebook event. | Content Library
Content Library API |
| Description | description | The description of the Facebook event. | Content Library
Content Library API |
| Creation time | creation\_time | The time the Facebook event was created. | Content Library API |
| Event start time | event\_start\_time | The start time of the Facebook event. Not available if the event is the parent of recurring event instances. Learn more. | Content Library
Content Library API |
| Event end time | event\_end\_time | The end time of the Facebook event. Not available if the event is the parent of recurring event instances. Learn more. | Content Library API |
| Going responses | going\_count | The number of Going responses on a Facebook event. Not available if the event is the parent of recurring event instances. Learn more. | Content Library
Content Library API |
| Not going responses | not\_going\_count | The number of Not Going responses on a Facebook event. Not available if the event is the parent of recurring event instances. Learn more. | Content Library API |
| Interested responses | interested\_count | The number of Interested responses on a Facebook event. Not available if the event is the parent of recurring event instances. Learn more. | Content Library
Content Library API |
| Event type | event\_type | The type of Facebook event. Event types include single instance, recurring or instance of
recurring. | Content Library API |
| Recurring event IDs | recurring\_event\_ids | The list of Meta Content Library IDs of the recurring instances of the Facebook event, if the event
is recurring. Only available if the event is the parent of recurring event instances. Learn more. | Content Library API |
| Parent event ID | parent\_event\_id | The Meta Content Library ID of the parent event of the Facebook event, if the event is
recurring. Only available if the event is an instance of a recurring event. Learn more. | Content Library API |
| Event owners type | event\_owners.data.type | The type of the event owner associated with the Facebook event. | Content Library API |
| Event owners ID | event\_owners.data.id | The Meta Content Library ID of the event owner associated with the Facebook event. This field will
display if the event owner is a group, professional profile or Page. For events owned by
professional profiles or Pages, only the Meta Content Library Page ID will be shared. | Content Library API |
| Place name | place.name | The self-reported, publicly accessible name of the place where the Facebook event is
located. | Content Library API |
| Place location city | place.location.city | The self-reported, publicly accessible city where the Facebook event is
located. | Content Library API |
| Place location country | place.location.country | The self-reported, publicly accessible country where the Facebook event is
located. | Content Library API |
| Place location country code | place.location.country\_code | The self-reported, publicly accessible country code of the Facebook event’s
location. | Content Library API |
| Place location name | place.location.name | The self-reported, publicly accessible name of the Facebook event’s
location. | Content Library API |
| Place location region | place.location.region | The self-reported, publicly accessible region where the Facebook event is
located. | Content Library API |
| Place location state | place.location.state | The self-reported, publicly accessible state where the Facebook event is
located. | Content Library API |
| Place location street | place.location.street | The self-reported, publicly accessible street where the Facebook event is
located. | Content Library API |
| Place location zip | place.location.zip | The self-reported, publicly accessible zip of the Facebook event’s
location. | Content Library API |
Facebook post
-------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Facebook post. | Content Library API |
| Text | text | The text of the Facebook post. Tags are excluded. | Content Library
Content Library API |
| Creation time | creation\_time | The time the Facebook post was created. | Content Library
Content Library API |
| Modified time | modified\_time | The time the Facebook post was most recently modified. | Content Library API |
| Language | lang | The content language of the Facebook post. Returns ISO 639-1 language code in 2-letter
lowercase format. | Content Library (Filter only)
Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library
Content Library API |
| Love reactions | statistics.love\_count | The number of love reactions on the post or reel. | Content Library
Content Library API |
| Wow reactions | statistics.wow\_count | The number of wow reactions on the post or reel. | Content Library
Content Library API |
| Haha reactions | statistics.haha\_count | The number of haha reactions on the post or reel. | Content Library
Content Library API |
| Sad reactions | statistics.sad\_count | The number of sad reactions on the post or reel. | Content Library
Content Library API |
| Angry reactions | statistics.angry\_count | The number of angry reactions on the post or reel. | Content Library
Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library
Content Library API |
| Reactions | statistics.reaction\_count | The total number of reactions on the post. Reactions include: Like, Love, Care, Haha,
Wow, Sad or Angry. | Content Library
Content Library API |
| Shares | statistics.share\_count | The number of times the post was shared. | Content Library
Content Library API |
| Care reactions | statistics.care\_count | The number of care reactions on the post. | Content Library
Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Facebook posts or reels made before January 1, 2017 are not available. View counts are not available for Facebook posts created in the last 5-7 days due to the refresh cycle. | Content Library
Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 7 days for all Facebook posts. | Content Library
Content Library API |
| Post owner type | post\_owner.data.type | The type of post owner associated with the Facebook post. Post owner types include:
Pages, groups and events. | Content Library
Content Library API |
| Post owner ID | post\_owner.data.id | The Meta Content Library ID of the owner associated with the Facebook post. | Content Library API |
| Post owner name | post\_owner.data.name | The name of the post owner associated with the Facebook post. | Content Library
Content Library API |
| Media type | media\_type | The media type included in the Facebook Post. Media types include photos, videos and
reels, and miscellaneous (including links, reshares, and text-only posts). | Content Library |
| Branded content Page ID | branded\_content\_page\_id | The Meta Content Library ID of the Page associated with the Facebook post. Included if the post has
 branded content. Learn more. | Content Library API |
| Link attachment fields description | link\_attachment\_fields.description | The description of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields link | link\_attachment\_fields.link | The URL of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields name | link\_attachment\_fields.name | The name of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields caption | link\_attachment\_fields.caption | The caption of the link attachment included in the Facebook post. | Content Library API |
| Shared post ID | shared\_post\_id | The Meta Content Library ID of the reshared post included in the Facebook post. | Content Library API |
Facebook post third-party cleanroom only
----------------------------------------

The following data dictionary entries are only available when using the Content Library API in an approved third-party cleanroom that supports the specific functionality.

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Multimedia type | multimedia.type | The type (photo or video) of the multimedia content. | Content Library API |
| Multimedia ID | multimedia.id | Anonymized ID of the photo or video content. | Content Library API |
| Multimedia URL | multimedia.url | URL within a storage location to which the multimedia content has been downloaded by the third-party cleanroom if the cleanroom system is unable to provide the multimedia directly in the search results. | Content Library API |
Instagram account
-----------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Instagram account. | Content Library API |
| Account type | account\_type | The type of public Instagram account. Creator, business, and personal accounts are valid types. Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. | Content Library API |
| Is verified | is\_verified | Whether the Instagram account has a verified badge. A verified badge in this context refers to accounts confirmed as authentic and not to those with a paid Meta Verified subscription. Learn more. | Content Library
Content Library API |
| Followers | follower\_count | The number of followers of the Instagram account. | Content Library
Content Library API |
| Following | following\_count | The number of accounts the Instagram account is following. | Content Library API |
| Website | website | The external website URL of the Instagram account. | Content Library API |
| Name | name | The name of the Instagram account. | Content Library
Content Library API |
| Biography | biography | The description of the Instagram account. | Content Library
Content Library API |
| Creation date | creation\_date | The date the Instagram account was created. | Content Library API |
Instagram post
--------------

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Meta Content Library ID | id | The Meta Content Library ID associated with the Instagram post. | Content Library API |
| Text | text | The text of the Instagram post. Tags are excluded. | Content Library
Content Library API |
| Creation time | creation\_time | The time the Instagram post was created. | Content Library
Content Library API |
| Modified time | modified\_time | The time the Instagram post was most recently modified. | Content Library API |
| Language | lang | The content language of the Instagram post. Returns ISO 639-1 language code in 2-letter lowercase format. | Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library
Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library
Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Instagram posts or reels made before October 1, 2022 are not available. View counts are not available for Instagram posts created in the last 3-5 days due to the refresh cycle. | Content Library
Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 3 days for all Instagram posts and reels. | Content Library
Content Library API |
| Post owner account type | post\_owner.type | The account type of the post owner associated with the Instagram post. Post owner types include business, creator, and personal. For personal accounts, only those with privacy set to public and with either a verified badge or 50,000 or more followers are included. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. | Content Library API |
| Post owner ID | post\_owner.id | The Meta Content Library ID of the owner associated with the Instagram post. | Content Library API |
| Is branded content | is\_branded\_content | Whether the Instagram post has branded content or not. Learn more. | Content Library API |
| Media type | media\_type | The media type included in the Instagram post. Media types include albums, photos, and videos and reels. | Content Library
Content Library API |
| Hashtags | hashtags | The list of hashtags included in the Instagram post. | Content Library
Content Library API |
Instagram post third-party cleanroom only
-----------------------------------------

The following data dictionary entries are only available when using the Content Library API in an approved third-party cleanroom that supports the specific functionality.

 Name
  | 
 API field
  | 
 Description
  | 
 Products
  || Multimedia type | multimedia.type | The type (photo or video) of the multimedia content. | Content Library API |
| Multimedia ID | multimedia.id | Meta Content Library ID associated with the photo or video content. | Content Library API |
| Multimedia URL | multimedia.url | URL within a storage location to which the multimedia content has been downloaded by the third-party cleanroom if the cleanroom system is unable to provide the multimedia directly in the search results. | Content Library API |
Learn more
----------

* Field expansion