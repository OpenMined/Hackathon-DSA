Graph API Reference: User Videos












DocsToolsSupportLog InGraph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
	+ Ads Archive
	+ Album
	+ App Link Host
	+ Application
	+ Branded Content Search
	+ CPASAdvertiser Partnership Recommendation
	+ Canvas
	+ Canvas Button
	+ Canvas Carousel
	+ Canvas Footer
	+ Canvas Header
	+ Canvas Photo
	+ Canvas Product List
	+ Canvas Product Set
	+ Canvas Text
	+ Canvas Video
	+ Collaborative Ads Directory
	+ Comment
	+ Commerce Merchant Settings
	+ Conversation
	+ Debug Token
	+ Event
	+ Games IAPProduct
	+ Group
	+ Group Doc
	+ Group Message
	+ Image Copyright
	+ Instagram Oembed
	+ Link
	+ Live Video
	+ Live Video Input Stream
	+ Mailing Address
	+ Media Fingerprint
	+ Message
	+ Milestone
	+ Object Comments
	+ Object Likes
	+ Object Private Replies
	+ Object Reactions
	+ Object Sharedposts
	+ Oembed Page
	+ Oembed Post
	+ Oembed Video
	+ Offline Conversion Data Set Upload
	+ Page
	+ Page Call To Action
	+ Page Post
	+ Page Upcoming Change
	+ Page/insights
	+ Payment
	+ Photo
	+ Place
	+ Place Tag
	+ Place Topic
	+ Post
	+ Profile
	+ Request
	+ Test User
	+ Thread
	+ URL
	+ User
		- Accounts
		- Ad Studies
		- Albums
		- Apprequestformerrecipients
		- Apprequests
		- Assigned Business Asset Groups
		- Assigned Pages
		- Assigned Product Catalogs
		- Business Users
		- Businesses
		- /user/checkins
		- Custom Labels
		- /user/family
		- Feed
		- /user/friends
		- Ids For Apps
		- Ids For Business
		- Ids For Pages
		- Likes
		- Live Videos
		- Music
		- Notifications
		- User Outbox
		- /user/payment\_transactions
		- Permissions
		- Photos
		- Picture
		- User Posts
		- /user/questions
		- Rich Media Documents
		- /user/scores
		- /user/subscribedto
		- /user/subscribers
		- Videos
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
	+ Whats App Message Template
On This PageUser VideosReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingGraph API Versionv18.0User Videos
===========

Reading
-------

GET GraphUserVideosEdge


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{user-id}/videos HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{user-id}/videos',
 '{access-token}'
 );
} catch(Facebook\Exceptions\FacebookResponseException $e) {
 echo 'Graph returned an error: ' . $e->getMessage();
 exit;
} catch(Facebook\Exceptions\FacebookSDKException $e) {
 echo 'Facebook SDK returned an error: ' . $e->getMessage();
 exit;
}
$graphNode = $response->getGraphNode();
/\* handle the result \*/
```

```
/\* make the API call \*/
FB.api(
 "/{user-id}/videos",
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{user-id}/videos",
 null,
 HttpMethod.GET,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{user-id}/videos"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters



| Parameter | Description |
| --- | --- |
| `type`enum {TAGGED, UPLOADED} | Default value: `"TAGGED"`Allows you to query which type of videos to return
 |

### Fields

Reading from this edge will return a JSON formatted result:


```
{
 "`data`": [],
 "`paging`": {}
}



```
#### `data`

A list of Video nodes.#### `paging`

For more details about pagination, see the Graph API guide.### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

Creating
--------

You can make a POST request to `videos` edge from the following paths: * `/{user_id}/videos`

When posting to this edge, a Video will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `audio_story_wave_animation_handle`string | Everstore handle of wave animation used to burn audio story video
 |
| `content_category`enum {BEAUTY\_FASHION, BUSINESS, CARS\_TRUCKS, COMEDY, CUTE\_ANIMALS, ENTERTAINMENT, FAMILY, FOOD\_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO\_GAMING, OTHER} | Content category of this video.
 |
| `description`UTF-8 string | 
```
 The text describing a post that may be shown in a story about it.
 It may include rich text information, such as entities and emojis.
```

Supports Emoji |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post.
 |
| `embeddable`boolean | Whether the video is embeddable.
 |
| `end_offset`int64 | end\_offset
 |
| `file_size`int64 | The size of the entire video file in bytes.
 |
| `file_url`string | Accessible URL of a video file. Cannot be used with `upload_phase`.
 |
| `fisheye_video_cropped`boolean | Whether the single fisheye video is cropped or not
 |
| `fov`int64 | 360 video only: Vertical field of view
 |
| `front_z_rotation`float | The front z rotation in degrees on the single fisheye video
 |
| `guide`list<list<int64>> | 360 video only: Guide keyframes data. An array of keyframes, each of which is an array of 3 or 4 elements in the following order: [video timestamp (seconds), pitch (degrees, -90 ~ 90), yaw (degrees, -180 ~ 180), field of view (degrees, 40 ~ 90, optional)], ordered by video timestamp in strictly ascending order.
 |
| `guide_enabled`boolean | 360 video only: Whether Guide is active.
 |
| `initial_heading`int64 | 360 video only: Horizontal camera perspective to display when the video begins.
 |
| `initial_pitch`int64 | 360 video only: Vertical camera perspective to display when the video begins.
 |
| `is_voice_clip`boolean | is\_voice\_clip, used to indicate that if a video is used as audio record
 |
| `no_story`boolean | Default value: `false`If set to `true`, this will suppress feed and timeline story.
 |
| `original_fov`int64 | Original field of view of the source camera
 |
| `original_projection_type`enum {equirectangular, cubemap, half\_equirectangular} | 360 video only: The original projection type of the 360 video being uploaded.
 |
| `posting_to_redspace`enum {enabled, disabled} | Whether the post should appear in RedSpace.
 |
| `privacy`Privacy Parameter | Determines the privacy settings of the video. If not supplied, this defaults to the privacy level granted to the app in the Login Dialog. This field cannot be used to set a more open privacy setting than the one granted.
 |
| `prompt_id`string | The prompt id in prompts or purple rain that generated this post
 |
| `prompt_tracking_string`string | The prompt tracking string associated with this video post
 |
| `react_mode_metadata`JSON-encoded string | This metadata is required for clip reacts feature
 |
| `referenced_sticker_id`numeric string or integer | Sticker id of the sticker in the post
 |
| `replace_video_id`numeric string or integer | The video id your uploaded video about to replace
 |
| `slideshow_spec`JSON object | Specification of a list of images that are used to generate video.
 |
| `images_urls`list<URL> | A 3-7 element array of the URLs of the images. Required.
Required |
| `duration_ms`integer | The duration in milliseconds of each image. Default value is 1000.
 |
| `transition_ms`integer | The duration in milliseconds of the crossfade transition between images.
 Default value is 1000.
 |
| `reordering_opt_in`boolean | Default value: `false` |
| `music_variations_opt_in`boolean | Default value: `false` |
| `source`string | The video, encoded as form data. This field is required.
 |
| `spherical`boolean | Default value: `false`Set if the video was recorded in 360 format.
 |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the video post
 |
| `start_offset`int64 | Start byte position of the file chunk.
 |
| `swap_mode`enum {replace} | Type of replacing video request
 |
| `title`UTF-8 string | The title of the video
Supports Emoji |
| `transcode_setting_properties`string | Properties used in computing transcode settings for the video
 |
| `unpublished_content_type`enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Type of unpublished content, such as scheduled, draft or ads\_post.
 |
| `upload_phase`enum {start, transfer, finish, cancel} | Type of chunked upload request.
 |
| `upload_session_id`numeric string or integer | ID of the chunked upload session.
 |
| `video_file_chunk`string | The video file chunk, encoded as form data. This field is required during `transfer` upload phase.
 |
| `video_id_original`string | video\_id\_original
 |

### Return Type

 Struct {`id`: numeric string, `upload_session_id`: numeric string, `video_id`: numeric string, `start_offset`: numeric string, `end_offset`: numeric string, `success`: bool, `skip_upload`: bool, `upload_domain`: string, `region_hint`: string, `xpv_asset_id`: numeric string, `is_xpv_single_prod`: bool, `transcode_bit_rate_bps`: numeric string, `transcode_dimension`: numeric string, `should_expand_to_transcode_dimension`: bool, `action_id`: string, `gop_size_seconds`: numeric string, `target_video_codec`: string, `target_hdr`: string, `maximum_frame_rate`: numeric string, }### Error Codes



| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 6000 | There was a problem uploading your video file. Please try again with another file. |
| 6001 | There was a problem uploading your video. Please try again. |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
| 194 | Missing at least one required parameter |
| 210 | User not visible |

Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.On This PageUser VideosReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingFollow Us* 
#### Products

* Artificial Intelligence
* AR/VR
* Business Tools
* Gaming
* Open Source
* Publishing
* Social Integrations
* Social Presence
#### Programs

* ThreatExchange
#### Support

* Developer Support
* Bugs
* Platform Status
* Report a Platform Data Incident
* Facebook for Developers Community Group
* Sitemap
#### News

* Blog
* Success Stories
* Videos
* Meta for Developers Page
#### Terms and Policies

* Platform Initiatives Hub
* Platform Terms
* Developer Policies
* European Commission Commitments
Follow Us* 
 © 2024 Meta * About
* Create Ad
* Careers
* Privacy Policy
* Cookies
* Terms
English (US)Bahasa IndonesiaDeutschEspañolEspañol (España)Français (France)ItalianoPortuguês (Brasil)Tiếng ViệtРусскийالعربيةภาษาไทย한국어中文(香港)中文(台灣)中文(简体)日本語English (US)




































Allow the use of cookies from Facebook on this browser?We use cookies and similar technologies to help:Provide and improve content on Meta ProductsProvide a safer experience by using information we receive from cookies on and off FacebookProvide and improve Meta Products for people who have an accountFor advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you, we use tools from other companies on Facebook. These companies also use cookies.You can allow the use of all cookies, just essential cookies or you can choose more options below. You can learn more about cookies and how we use them, and review or change your choice at any time in our Cookie Policy.Essential cookiesThese cookies are required to use Meta Products. They’re necessary for these sites to work as intended.Optional cookies

Cookies from other companiesWe use tools from other companies for advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you. These companies also use cookies.More informationIf you allow these cookies:

* We’ll be able to better personalize ads for you off of Meta Products, and measure their performance
* Features on our products will not be affected
* Other companies will receive information about you by using cookies

If you don’t allow these cookies:

* We won’t use cookies from other companies to help personalize ads for you off of Meta Products, or to measure their performance
* Some features on our products may not work

Other ways you can control your information

Manage your ad experience in Accounts CenterIf you have a Facebook account, you can manage how different data is used to personalize ads with these tools.

Ad settings

To show you better ads, we use data that advertisers and other partners provide us about your activity off Meta Company Products, including websites and apps. You can control whether we use this data to show you ads in your ad settings.

The Meta Audience Network is a way for advertisers to show you ads in apps and websites off the Meta Company Products. One of the ways Audience Network shows relevant ads is by using your ad preferences to determine which ads you may be interested in seeing. You can control this in your ad settings.

Ad preferences

In Ad preferences, you can choose whether we show you ads and make choices about the information used to show you ads.

Off-Facebook activity

You can review your off-Facebook activity, which is a summary of activity that businesses and organizations share with us about your interactions with them, such as visiting their apps or websites. They use our Business Tools, such as Facebook Login or Meta Pixel, to share this information with us. This helps us do things such as give you a more personalized experience on Meta Products. Learn more about off-Facebook activity, how we use it, and how you can manage it.

More information about online advertisingYou can opt out of seeing online interest-based ads from Meta and other participating companies through the Digital Advertising Alliance in the US, the Digital Advertising Alliance of Canada in Canada or the European Interactive Digital Advertising Alliance in Europe, or through your mobile device settings, if you are using Android, iOS 13 or an earlier version of iOS. Please note that ad blockers and tools that restrict our cookie use may interfere with these controls.

The advertising companies we work with generally use cookies and similar technologies as part of their services. To learn more about how advertisers generally use cookies and the choices they offer, you can review the following resources:

* Digital Advertising Alliance
* Digital Advertising Alliance of Canada
* European Interactive Digital Advertising Alliance
Controlling cookies with browser settingsYour browser or device may offer settings that allow you to choose whether browser cookies are set and to delete them. These controls vary by browser, and manufacturers may change both the settings they make available and how they work at any time. As of 5 October 2020, you may find additional information about the controls offered by popular browsers at the links below. Certain parts of Meta Products may not work properly if you have disabled browser cookies. Please be aware that these controls are distinct from the controls that Facebook offers.

* Google Chrome
* Internet Explorer
* Firefox
* Safari
* Safari Mobile
* Opera
Only allow essential cookiesAllow essential and optional cookies