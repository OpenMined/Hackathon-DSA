Graph API Reference v18.0: Group Message












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
		- Attachments
		- Dynamic Posts
		- Insights
		- Reactions
		- Sharedposts
		- Sponsor Tags
		- To
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
On This PageGroup MessageReadingNew Page ExperienceFeature PermissionsExampleParametersFieldsEdgesError CodesCreatingGraph API Versionv18.0Group Message
=============

Reading
-------

GroupMessage


### New Page Experience

This endpoint is supported for New Page Experience.### Feature Permissions



| Name | Description |
| --- | --- |
| Groups API | This feature permission may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{group-message-id} HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
try {
 // Returns a `Facebook\FacebookResponse` object
 $response = $fb->get(
 '/{group-message-id}',
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
 "/{group-message-id}",
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
 "/{group-message-id}",
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
 initWithGraphPath:@"/{group-message-id}"
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



| Field | Description |
| --- | --- |
| `id`token with structure: Post ID | id
 |
| `actions`list | actions
 |
| `admin_creator`BusinessUser|User|Application | admin\_creator
 |
| `allowed_advertising_objectives`list<string> | allowed\_advertising\_objectives
 |
| `application`Application | application
 |
| `backdated_time`datetime | backdated\_time
 |
| `call_to_action`struct with keys: type, value | call\_to\_action
 |
| `can_reply_privately`bool | can\_reply\_privately
 |
| `caption`string | caption
 |
| `child_attachments`list | child\_attachments
 |
| `comments_mirroring_domain`string | comments\_mirroring\_domain
 |
| `coordinates`struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | coordinates
 |
| `created_time`datetime | created\_time
Default |
| `description`string | description
 |
| `event`Event | event
 |
| `expanded_height`unsigned int32 | expanded\_height
 |
| `expanded_width`unsigned int32 | expanded\_width
 |
| `feed_targeting`struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | feed\_targeting
 |
| `from`User|Page | from
 |
| `full_picture`string | full\_picture
 |
| `height`unsigned int32 | height
 |
| `icon`string | icon
 |
| `is_app_share`bool | is\_app\_share
 |
| `is_eligible_for_promotion`bool | is\_eligible\_for\_promotion
 |
| `is_expired`bool | is\_expired
 |
| `is_hidden`bool | is\_hidden
 |
| `is_inline_created`bool | is\_inline\_created
 |
| `is_popular`bool | is\_popular
 |
| `is_published`bool | is\_published
 |
| `is_spherical`bool | is\_spherical
 |
| `link`uri | link
 |
| `message`string | message
Default |
| `message_tags`list | message\_tags
 |
| `multi_share_end_card`bool | multi\_share\_end\_card
 |
| `multi_share_optimized`bool | multi\_share\_optimized
 |
| `name`string | name
 |
| `object_id`string | object\_id
 |
| `parent_id`token with structure: Post ID | parent\_id
 |
| `permalink_url`uri | permalink\_url
 |
| `place`Place | place
 |
| `privacy`Privacy | privacy
 |
| `promotable_id`token with structure: Post ID | promotable\_id
 |
| `properties`list | properties
 |
| `scheduled_publish_time`float | scheduled\_publish\_time
 |
| `shares`struct with keys: count | shares
 |
| `source`string | source
 |
| `status_type`string | status\_type
 |
| `story`string | story
Default |
| `story_tags`list | story\_tags
 |
| `subscribed`bool | subscribed
 |
| `target`Profile | target
 |
| `targeting`struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | targeting
 |
| `timeline_visibility`string | timeline\_visibility
 |
| `type`string | type
 |
| `updated_time`datetime | updated\_time
 |
| `via`User|Page | via
 |
| `width`unsigned int32 | width
 |

### Edges



| Edge | Description |
| --- | --- |
| `attachments` | attachments
 |
| `comments` | comments
 |
| `dynamic_posts` | dynamic\_posts
 |
| `insights` | insights
 |
| `reactions` | reactions
 |
| `sharedposts` | sharedposts
 |
| `sponsor_tags` | sponsor\_tags
 |
| `to` | to
 |

### Error Codes



| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.On This PageGroup MessageReadingNew Page ExperienceFeature PermissionsExampleParametersFieldsEdgesError CodesCreatingFollow Us* 
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