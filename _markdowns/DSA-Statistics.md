
















API Reference  |  YouTube Data API  |  Google for Developers

















* YouTube
* Data API






















* English
* Deutsch
* Español
* Español – América Latina
* Français
* Indonesia
* Italiano
* Polski
* Português – Brasil
* Tiếng Việt
* Türkçe
* Русский
* עברית
* العربيّة
* فارسی
* हिंदी
* বাংলা
* ภาษาไทย
* 中文 – 简体
* 中文 – 繁體
* 日本語
* 한국어




Sign in










Home


Guides


Reference


Samples


Support





















* YouTube
* Data API







* Home
* Guides
* Reference
* Samples
* Support




* Overview
* Activities

	+ Overview
	+ list
	+ insert
* Captions

	+ Overview
	+ list
	+ insert
	+ update
	+ download
	+ delete
* ChannelBanners

	+ Overview
	+ insert
* Channels

	+ Overview
	+ list
	+ update
* ChannelSections

	+ Overview
	+ list
	+ insert
	+ update
	+ delete
* Comments

	+ Overview
	+ list
	+ insert
	+ update
	+ markAsSpam
	+ setModerationStatus
	+ delete
* CommentThreads

	+ Overview
	+ list
	+ insert
* i18nLanguages

	+ Overview
	+ list
* i18nRegions

	+ Overview
	+ list
* Members

	+ Overview
	+ list
* MembershipsLevels

	+ Overview
	+ list
* PlaylistItems

	+ Overview
	+ list
	+ insert
	+ update
	+ delete
* Playlists

	+ Overview
	+ list
	+ insert
	+ update
	+ delete
* Search

	+ Overview
	+ list
* Subscriptions

	+ Overview
	+ list
	+ insert
	+ delete
* Thumbnails

	+ Overview
	+ set
* VideoAbuseReportReasons

	+ Overview
	+ list
* VideoCategories

	+ Overview
	+ list
* Videos

	+ Overview
	+ list
	+ insert
	+ update
	+ rate
	+ getRating
	+ reportAbuse
	+ delete
* Watermarks

	+ Overview
	+ set
	+ unset
* GuideCategories

	+ Overview
	+ list
* Standard Query Parameters
* YouTube Data API Errors

	+ Overview
	+ Global Domain Errors


















* Home
* Products
* YouTube
* Data API
* Reference





API Reference
=============




 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
 







The YouTube Data API lets you incorporate functions normally executed on the YouTube website into your own website or application. The lists below identify the different types of resources that you can retrieve using the API. The API also supports methods to insert, update, or delete many of these resources.


This reference guide explains how to use the API to perform all of these operations. The guide is organized by resource type. A resource represents a type of item that comprises part of the YouTube experience, such as a video, a playlist, or a subscription. For each resource type, the guide lists one or more data representations, and resources are represented as JSON objects. The guide also lists one or more supported methods (`LIST`, `POST`, `DELETE`, etc.) for each resource type and explains how to use those methods in your application.


Calling the API
---------------


The following requirements apply to YouTube Data API requests:


1. Every request must either specify an API key (with the `key` parameter) or provide an OAuth 2.0 token. Your API key is available in the Developer Console's **API Access** pane for your project.
2. You **must** send an authorization token for every insert, update, and delete request. You must also send an authorization token for any request that retrieves the authenticated user's private data.


In addition, some API methods for retrieving resources may support parameters that require authorization or may contain additional metadata when requests are authorized. For example, a request to retrieve a user's uploaded videos may also contain private videos if the request is authorized by that specific user.
3. The API supports the OAuth 2.0 authentication protocol. You can provide an OAuth 2.0 token in either of the following ways:



	* Use the `access_token` query parameter like this: `?access_token=``oauth2-token`
	* Use the HTTP `Authorization` header like this: `Authorization: Bearer` `oauth2-token`Complete instructions for implementing OAuth 2.0 authentication in your application can be found in the authentication guide.




Resource types
--------------



### Activities


An `**activity**` resource contains information about an action that a particular channel, or user, has taken on YouTube. The actions reported in activity feeds include rating a video, sharing a video, marking a video as a favorite, uploading a video, and so forth. Each `activity` resource identifies the type of action, the channel associated with the action, and the resource(s) associated with the action, such as the video that was rated or uploaded.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /activities` | Returns a list of channel activity events that match the request criteria. For example, you can retrieve events associated with a particular channel or with the user's own channel. |
| `insert` | `POST /activities` | **Note:** This method has been deprecated and is no longer
 supported. |




### Captions


A `**caption**` resource represents a YouTube caption track. A caption track is associated with exactly one YouTube video.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `delete` | `DELETE /captions` | Deletes the specified caption track. |
| `download` | `GET /captions/id` | Downloads a caption track. The caption track is returned in its original format unless the request specifies a value for the `tfmt` parameter and in its original language unless the request specifies a value for the `tlang` parameter. |
| `insert` | `POST /captions` | Uploads a caption track. |
| `list` | `GET /captions` | Returns a list of caption tracks that are associated with a specified video. Note that the API response does not contain the actual captions and that the `captions.download` method provides the ability to retrieve a caption track. |
| `update` | `PUT /captions` | Updates a caption track. When updating a caption track, you can change the track's draft status, upload a new caption file for the track, or both. |




### ChannelBanners


A `channelBanner` resource contains the URL that you would use to set a newly uploaded image as the banner image for a channel.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `insert` | `POST /channelBanners/insert` | Uploads a channel banner image to YouTube. This method represents the first two steps in a three-step process to update the banner image for a channel:1. Call the `channelBanners.insert` method to upload the binary image data to YouTube. The image must have a 16:9 aspect ratio and be at least 2048x1152 pixels. We recommend uploading a 2560px by 1440px image.
2. Extract the `url` property's value from the response that the API returns for step 1.
3. Call the `channels.update` method to update the channel's branding settings. Set the `brandingSettings.image.bannerExternalUrl` property's value to the URL obtained in step 2.
 |




### ChannelSections


A `**channelSection**` resource contains information about a set of videos that a channel has chosen to feature. For example, a section could feature a channel's latest uploads, most popular uploads, or videos from one or more playlists.  
  
Note that a channel's sections are only visible if the channel displays content in a browse view (rather than a feed view). To enable a channel to display content in a browse view, set the `brandingSettings.channel.showBrowseView` property to `true` for the specified channel.  
  
A channel can create a maximum of 10 shelves.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `delete` | `DELETE /channelSections` | Deletes a channel section. |
| `insert` | `POST /channelSections` | Adds a channel section to the authenticated user's channel. A channel can create a maximum of 10 shelves. |
| `list` | `GET /channelSections` | Returns a list of `channelSection` resources that match the API request criteria. |
| `update` | `PUT /channelSections` | Updates a channel section. |




### Channels


A `**channel**` resource contains information about a YouTube channel.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /channels` | Returns a collection of zero or more `**channel**` resources that match the request criteria. |
| `update` | `PUT /channels` | Updates a channel's metadata. Note that this method currently only supports updates to the `channel` resource's `brandingSettings` and `invideoPromotion` objects and their child properties. |




### CommentThreads


A `**commentThread**` resource contains information about a YouTube comment thread, which comprises a top-level comment and replies, if any exist, to that comment. A `commentThread` resource can represent comments about either a video or a channel.  
  
Both the top-level comment and the replies are actually `comment` resources nested inside the `commentThread` resource. The `commentThread` resource does not necessarily contain all replies to a comment, and you need to use the `comments.list` method if you want to retrieve all replies for a particular comment. Also note that some comments do not have replies.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /commentThreads` | Returns a list of comment threads that match the API request parameters. |
| `insert` | `POST /commentThreads` | Creates a new top-level comment. To add a reply to an existing comment, use the `comments.insert` method instead. |




### Comments


A `**comment**` resource contains information about a single YouTube comment. A `comment` resource can represent a comment about either a video or a channel. In addition, the comment could be a top-level comment or a reply to a top-level comment.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /comments` | Returns a list of comments that match the API request parameters. |
| `setModerationStatus` | `POST /comments/setModerationStatus` | Sets the moderation status of one or more comments. The API request must be authorized by the owner of the channel or video associated with the comments. |
| `insert` | `POST /comments` | Creates a reply to an existing comment. **Note:** To create a top-level comment, use the `commentThreads.insert` method. |
| `markAsSpam` | `POST /comments/markAsSpam` | **Note:** This method has been deprecated and is no longer
 supported. |
| `delete` | `DELETE /comments` | Deletes a comment. |
| `update` | `PUT /comments` | Modifies a comment. |




### GuideCategories


A `**guideCategory**` resource identifies a category that YouTube algorithmically assigns based on a channel's content or other indicators, such as the channel's popularity. The list is similar to video categories, with the difference being that a video's uploader can assign a video category but only YouTube can assign a channel category.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /guideCategories` | Returns a list of categories that can be associated with YouTube channels. |




### I18nLanguages


An `**i18nLanguage**` resource identifies an application language that the YouTube website supports. The application language can also be referred to as a UI language. For the YouTube website, an application language could be automatically selected based on Google Account settings, browser language, or IP location. A user could also manually select the desired UI language from the YouTube site footer.  
  
Each `i18nLanguage` resource identifies a language code and a name. The language code can be used as the value of the `hl` parameter when calling API methods like `videoCategories.list` and `guideCategories.list`.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /i18nLanguages` | Returns a list of application languages that the YouTube website supports. |




### I18nRegions


An `**i18nRegion**` resource identifies a geographic area that a YouTube user can select as the preferred content region. The content region can also be referred to as a content locale. For the YouTube website, a content region could be automatically selected based on heuristics like the YouTube domain or the user's IP location. A user could also manually select the desired content region from the YouTube site footer.  
  
Each `i18nRegion` resource identifies a region code and a name. The region code can be used as the value of the `regionCode` parameter when calling API methods like `search.list`, `videos.list`, `activities.list`, and `videoCategories.list`.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /i18nRegions` | Returns a list of content regions that the YouTube website supports. |




### Members


A `**member**` resource represents a channel member for a YouTube
 channel. A member provides recurring monetary support to a creator and receives special
 benefits. For example, members are able to chat when the creator turns on members-only mode for
 a chat.


For more information about this resource, see its
 resource representation and list of
 properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /members` | Lists members (formerly known as "sponsors") for a channel. The API request must be
 authorized by the channel owner. |




### MembershipsLevels


A `**membershipsLevel**` resource identifies a pricing level for the
 creator that authorized the API request.


For more information about this resource, see its
 resource representation and list of
 properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /membershipsLevels` | Returns a collection of zero or more `**membershipsLevel**`
 resources owned by the channel that authorized the API request. Levels are returned in
 implicit display order. |




### PlaylistItems


A `**playlistItem**` resource identifies another resource, such as a
 video, that is included in a playlist. In addition, the `playlistItem`  resource
 contains details about the included resource that pertain specifically to how that resource
 is used in that playlist.  
  

 YouTube also uses a playlist to identify a channel's list of uploaded videos, with each
 `playlistItem` in that list representing one uploaded video. You can retrieve the
 playlist ID for that list from the `channel resource`
 for a given channel. You can then use the
 `playlistItems.list` method to the
 list.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `delete` | `DELETE /playlistItems` | Deletes a playlist item. |
| `insert` | `POST /playlistItems` | Adds a resource to a playlist. |
| `list` | `GET /playlistItems` | Returns a collection of playlist items that match the API request parameters. You can retrieve all of the playlist items in a specified playlist or retrieve one or more playlist items by their unique IDs. |
| `update` | `PUT /playlistItems` | Modifies a playlist item. For example, you could update the item's position in the playlist. |




### Playlists


A `**playlist**` resource represents a YouTube playlist. A playlist is a collection of videos that can be viewed sequentially and shared with other users. A playlist can contain up to 200 videos, and YouTube does not limit the number of playlists that each user creates. By default, playlists are publicly visible to other users, but playlists can be public or private.  
  
 YouTube also uses playlists to identify special collections of videos for a channel, such as: 

* uploaded videos
* positively rated (liked) videos
* watch history
* watch later

 To be more specific, these lists are associated with a channel, which is a collection of a person, group, or company's videos, playlists, and other YouTube information. You can retrieve the playlist IDs for each of these lists from the `channel resource` for a given channel.  
  
 You can then use the `playlistItems.list` method to retrieve any of those lists. You can also add or remove items from those lists by calling the `playlistItems.insert` and `playlistItems.delete` methods.
 For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `delete` | `DELETE /playlists` | Deletes a playlist. |
| `list` | `GET /playlists` | Returns a collection of playlists that match the API request parameters. For example, you can retrieve all playlists that the authenticated user owns, or you can retrieve one or more playlists by their unique IDs. |
| `insert` | `POST /playlists` | Creates a playlist. |
| `update` | `PUT /playlists` | Modifies a playlist. For example, you could change a playlist's title, description, or privacy status. |




### Search


A search result contains information about a YouTube video, channel, or playlist that matches the search parameters specified in an API request. While a search result points to a uniquely identifiable resource, like a video, it does not have its own persistent data.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /search` | Returns a collection of search results that match the query parameters specified in the API request. By default, a search result set identifies matching `video`, `channel`, and `playlist` resources, but you can also configure queries to only retrieve a specific type of resource. |




### Subscriptions


A `**subscription**` resource contains information about a YouTube user subscription. A subscription notifies a user when new videos are added to a channel or when another user takes one of several actions on YouTube, such as uploading a video, rating a video, or commenting on a video.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `delete` | `DELETE /subscriptions` | Deletes a subscription. |
| `insert` | `POST /subscriptions` | Adds a subscription for the authenticated user's channel. |
| `list` | `GET /subscriptions` | Returns subscription resources that match the API request criteria. |




### Thumbnails


A `**thumbnail**` resource identifies different thumbnail image sizes associated with a resource. Please note the following characteristics of thumbnail images:

* A resource's `snippet.thumbnails` property is an object that identifies the thumbnail images available for that resource.
* A `thumbnail` resource contains a series of objects. The name of each object (`default`, `medium`, `high`, etc.) refers to the thumbnail image size.
* Different types of resources may support different thumbnail image sizes.
* Different types of resources may define different sizes for thumbnail images with the same name. For example, the `default` thumbnail image for a `video` resource is typically 120px by 90px, and the `default` thumbnail image for a `channel` resource is typically 88px by 88px.
* Resources of the same type may still have different thumbnail image sizes for certain images depending on the resolution of the original image or content uploaded to YouTube. For example, an HD video may support higher resolution thumbnails than non-HD videos.
* Each object that contains information about a thumbnail image size has a `width` property and a `height` property. However, the width and height properties may not be returned for that image.
* If an uploaded thumbnail image does not match the required dimensions, the image is resized to match the correct size without changing its aspect ratio. The image is not cropped, but may include black bars so that the size is correct.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `set` | `POST /thumbnails/set` | Uploads a custom video thumbnail to YouTube and sets it for a video. |




### VideoAbuseReportReasons


A `**videoAbuseReportReason**` resource contains information about a reason that a video would be flagged for containing abusive content. When your application calls the `videos.reportAbuse` method to report an abusive video, the request uses the information from a `videoAbuseReportReason` resource to identify the reason that the video is being reported.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /videoAbuseReportReasons` | Retrieve a list of reasons that can be used to report abusive videos. |




### VideoCategories


A `**videoCategory**` resource identifies a category that has been or could be associated with uploaded videos.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `list` | `GET /videoCategories` | Returns a list of categories that can be associated with YouTube videos. |




### Videos


A `**video**` resource represents a YouTube video.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `insert` | `POST /videos` | Uploads a video to YouTube and optionally sets the video's metadata. |
| `list` | `GET /videos` | Returns a list of videos that match the API request parameters. |
| `delete` | `DELETE /videos` | Deletes a YouTube video. |
| `update` | `PUT /videos` | Updates a video's metadata. |
| `rate` | `POST /videos/rate` | Add a like or dislike rating to a video or remove a rating from a video. |
| `getRating` | `GET /videos/getRating` | Retrieves the ratings that the authorized user gave to a list of specified videos. |
| `reportAbuse` | `POST /videos/reportAbuse` | Report a video for containing abusive content. |




### Watermarks


A `**watermark**` resource identifies an image that displays during playbacks of a specified channel's videos. You can also specify a target channel to which the image will link as well as timing details that determine when the watermark appears during video playbacks and the length of time it is visible.


For more information about this resource, see its resource representation and list of properties.




| Method | HTTP request | Description |
| --- | --- | --- |
| URIs relative to `https://www.googleapis.com/youtube/v3` |
| `set` | `POST /watermarks/set` | Uploads a watermark image to YouTube and sets it for a channel. |
| `unset` | `POST /watermarks/unset` | Deletes a channel's watermark image. |











Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.


Last updated 2023-09-13 UTC.







 [{
 "type": "thumb-down",
 "id": "missingTheInformationINeed",
 "label":"Missing the information I need"
 },{
 "type": "thumb-down",
 "id": "tooComplicatedTooManySteps",
 "label":"Too complicated / too many steps"
 },{
 "type": "thumb-down",
 "id": "outOfDate",
 "label":"Out of date"
 },{
 "type": "thumb-down",
 "id": "samplesCodeIssue",
 "label":"Samples / code issue"
 },{
 "type": "thumb-down",
 "id": "otherDown",
 "label":"Other"
 }]
 

 [{
 "type": "thumb-up",
 "id": "easyToUnderstand",
 "label":"Easy to understand"
 },{
 "type": "thumb-up",
 "id": "solvedMyProblem",
 "label":"Solved my problem"
 },{
 "type": "thumb-up",
 "id": "otherUp",
 "label":"Other"
 }]
 





* Blog
The latest news on the YouTube blog
* GitHub
Find API code samples and other YouTube open-source projects.
* Issue Tracker
Something wrong? Send us a bug report!
* Stack Overflow
Ask a question under the youtube-api tag
* Videos
Check out the YouTube Developer Relations team's YouTube channel






* ### Tools


	+ Google APIs Explorer
	+ YouTube Player Demo
	+ Configure a Subscribe Button
* ### Issue Tracker


	+ File a bug
	+ Request a feature
	+ See open issues
* ### Product Info


	+ Terms of Service
	+ Branding Guidelines
	+ Monetization Guidelines
	+ APIs subject to Deprecation Policy








* Android
* Chrome
* Firebase
* Google Cloud Platform
* All products




* Terms
* Privacy
* Sign up for the Google for Developers newsletter
Subscribe



* English
* Deutsch
* Español
* Español – América Latina
* Français
* Indonesia
* Italiano
* Polski
* Português – Brasil
* Tiếng Việt
* Türkçe
* Русский
* עברית
* العربيّة
* فارسی
* हिंदी
* বাংলা
* ภาษาไทย
* 中文 – 简体
* 中文 – 繁體
* 日本語
* 한국어





















