Graph API Reference v18.0: Event Live Videos












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
		- Live Videos
		- /event/photos
		- /event/picture
		- Roles
		- Ticket Tiers
		- Graph API Reference /event/videos
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
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
	+ Whats App Message Template
On This PageEvent Live VideosReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingGraph API Versionv18.0Event Live Videos
=================

Reading
-------

SELF\_EXPLANATORY


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{event-id}/live\_videos HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{event-id}/live\_videos',
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
 "/{event-id}/live\_videos",
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
 "/{event-id}/live\_videos",
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
 initWithGraphPath:@"/{event-id}/live\_videos"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

This endpoint doesn't have any parameters.### Fields

Reading from this edge will return a JSON formatted result:


```
{
 "`data`": [],
 "`paging`": {}
}



```
#### `data`

A list of Null nodes.#### `paging`

For more details about pagination, see the Graph API guide.### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |

Creating
--------

You can make a POST request to `live_videos` edge from the following paths: * `/{event_id}/live_videos`

When posting to this edge, a LiveVideo will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `content_tags`list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.

```
 Example:
 ~~~~
 /search?type=adinterest&q=couscous
 ~~~~
```

 |
| `description`UTF-8 string | The description of the live video.
Supports Emoji |
| `enable_backup_ingest`boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set
 |
| `encoding_settings`string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query).
 |
| `event_params`Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.
Example:
{
 start\_time: 1641013200,
 cover: 'https://your.url/image.jpg',
}
 |
| `fisheye_video_cropped`boolean | Whether the single fisheye video is cropped or not
 |
| `front_z_rotation`float | The front z rotation in degrees on the single fisheye video
 |
| `is_spherical`boolean | Flag that denotes the broadcast is a 360 live broadcast.
 |
| `original_fov`int64 | Original field of view of the camera
 |
| `privacy`Privacy Parameter | Privacy for this live video.
 |
| `projection`enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR.
 |
| `published`boolean | Set this to false to preview the stream before going live.

```
 Deprecated. Prefer setting the status instead.
```

 |
| `schedule_custom_profile_image`image | Custom image that will appear in the scheduled live story and lobby.
 |
| `spatial_audio_format`enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo.
 |
| `status`enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.)
 |
| `stereoscopic_mode`enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video.
 |
| `stop_on_delete_stream`boolean | Set this to true if stream should be stopped when
 deleteStream RTMP command received.
 |
| `title`UTF-8 string | The title of the live video. Maximum 254 characters.
Supports Emoji |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `stream_url`: string, `secure_stream_url`: string, `stream_secondary_urls`: List [string], `secure_stream_secondary_urls`: List [string], `dash_ingest_url`: string, `dash_ingest_secondary_urls`: List [string], `event_id`: numeric string, }### Error Codes



| Error | Description |
| --- | --- |
| 6000 | There was a problem uploading your video file. Please try again with another file. |

Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.On This PageEvent Live VideosReadingExampleParametersFieldsError CodesCreatingParametersReturn TypeError CodesUpdatingFollow Us* 
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