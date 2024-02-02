Features Reference
==================

Features are authorization mechanisms that allow apps to access specific types of data through our various APIs. In this way they are similar to Permissions, however Features cannot be granted to an app by an app user. Instead, Features are active or inactive depending on the app user's relationship to the app and the app's mode when it is being used.

For apps in Development Mode, all Features except for Page Public Content Access and Page Public Metadata Access are active for any app user who has a Role on the app or a Role in a Business that has claimed the app.

For apps in Live Mode, only Features approved through App Review are active for app users. This also applies to app users who have a Role on the app or Business.

For Business app types (which have access levels instead of modes), Features are active for any app users who have a Role on the app or in a Business that has claimed the app, unless access has been removed. In order for a Feature to be active for app users without a Role on the app or Business, it must first be approved through App Review.

Access to any Feature that is granted by default or through App Review can be used to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Unlike Permissions, Features do not expire, their approval will not be revoked, if they are unused.

| Feature | Description |
| --- | --- |
| [Ad Targeting Data Access](https://developers.facebook.com/docs/features-reference/ad-targeting-data-access) | The **Ad Targeting Data Access** feature allows access to ad targeting data within the Facebook Open Research and Transparency tool for election, political, and social issue ads that are run on Facebook from Meta and Instagram from Meta.  <br>  <br><br>**Allowed Usage**<br><br>* To conduct research about Meta's role in society |
| [Business Asset User Profile Access](https://developers.facebook.com/docs/features-reference/business-asset-user-profile-access) | The **Business Asset User Profile Access** feature allows your app to read the [User Fields](https://developers.facebook.com/docs/graph-api/reference/user#fields) for users engaging with your business assets such as id, ids\_for\_business, name, and picture.  <br>  <br><br>**Allowed Usage**<br><br>You can use this feature if your app uses one or more of the User Fields in its business app experience. |
| [Ads Management Standard Access](https://developers.facebook.com/docs/features-reference/ads-management-standard-access) | The **Ads Management Standard Access** feature allows your app to access the Marketing API.  <br>  <br><br>**Allowed Usage**<br><br>* Enable an unlimited number of ad accounts and lower rate limiting.<br>    <br>* To read ads reports for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_read** permission.<br>    <br>* To read and manage ads for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_management** permission.<br>    <br>* To pull ads reports from a set of clients, and to read and manage ads from another set of clients, request **Ads Management Standard Access**, along with both **ads\_read** and **ads\_management** permissions. |
| [Business Asset User Profile Access](https://developers.facebook.com/docs/features-reference/business-asset-user-profile-access) | The **Business Asset User Profile Access** feature allows your app to read the [User Fields](https://developers.facebook.com/docs/graph-api/reference/user#fields) for users engaging with your business assets such as id, ids\_for\_business, name, and picture.  <br>  <br><br>**Allowed Usage**<br><br>You can use this feature if your app uses one or more of the User Fields in its business app experience. |
| [Groups API](https://developers.facebook.com/docs/features-reference/groups-api) | The **Groups API** feature allows your app to access content in a Facebook Group.  <br>  <br><br>**Allowed Usage**<br><br>* Help people manage the posts and content published to their Group.<br>    <br>* Help people get information about content posted to their Group.<br>    <br>* Let people publish content from your app to their Facebook Group.<br>    <br>* Help people get aggregated insights about activity happening in their Group. |
| [Human Agent](https://developers.facebook.com/docs/features-reference/human-agent) | The **Human Agent** feature allows your app to have a human agent respond to user messages using the **human\_agent** tag within 7 days of a user's message.  <br>  <br><br>**Allowed Usage**<br><br>* Provide human agent support in cases where a user’s issue cannot be resolved in the standard messaging window. |
| [Instagram Public Content Access](https://developers.facebook.com/docs/features-reference/instagram-public-content-access) | The **Instagram Public Content Access** feature allows your app to access Instagram Graph API's Hashtag Search endpoints.  <br>  <br><br>**Allowed Usage**<br><br>* Discover content associated with its current campaign.<br>    <br>* Provide customer support.<br>    <br>* Identify entrants to its contests, competitions, or sweepstakes.<br>    <br>* Understand public sentiment around brand.<br>    <br>* Understand and manage their audience, develop their content strategy and obtain digital rights. |
| [Live Video API](https://developers.facebook.com/docs/features-reference/live-video-api) | The **Live Video API** feature allows an app to manage live videos to Pages, Groups and User timelines when combined with the correct matching permission.  <br>  <br><br>**Allowed Usage**<br><br>* App users can publish live video content from your app to Facebook. |
| [oEmbed Read](https://developers.facebook.com/docs/features-reference/oembed_read) | The **oEmbed Read** feature allows your app to get embed HTML and basic metadata for public Facebook and Instagram pages, posts, and videos.  <br>  <br><br>**Allowed Usage**<br><br>* Provide front-end views of Facebook and Instagram pages, posts, and videos. |
| [Page Mentioning](https://developers.facebook.com/docs/features-reference/page-mentioning) | The **Page Mentioning** feature allows your app mention any Facebook Page when publishing posts on the Pages managed by your app.  <br>  <br><br>**Allowed Usage**<br><br>* Allow people to use your app to publish Page posts that mention other Pages.<br>    <br>* Mention Pages relevant to the content in your page post. |
| [Page Public Content Access](https://developers.facebook.com/docs/features-reference/page-public-content-access) | The **Page Public Content Access** feature allows your app access to the Pages Search API and to read public data for Pages for which you lack the [pages\_read\_engagement permission](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) and the [pages\_read\_user\_content permission](https://developers.facebook.com/docs/permissions/reference/pages_read_user_content). Readable data includes business metadata, public comments and posts.  <br>  <br><br>**Allowed Usage**<br><br>* Analyze and/or display posts and engagement on Pages. |
| [Page Public Metadata Access](https://developers.facebook.com/docs/features-reference/page-public-metadata-access) | The **Page Public Metadata Access** feature allows your app access to the Pages Search API and to read public data for Pages for which you lack the [public Page fields](https://developers.facebook.com/docs/graph-api/reference/page#public-page-data) and the [Pages Search API](https://developers.facebook.com/docs/pages/searching).  <br>  <br><br>**Allowed Usage**<br><br>* Analyze engagement with public Pages by viewing Like and follower counts.<br>    <br>* Aggregate public-facing "about" Page information from multiple, disparate pages. |
| [Threat Exchange](https://developers.facebook.com/docs/features-reference/threat-exchange) | The **ThreatExchange** feature allows your app to share threat data among a select group of vetted industry partners.  <br>  <br><br>**Allowed Usage**<br><br>* Share threat data with a specific group of partners to achieve their security goals. |

Deprecated Features
-------------------

| Feature | Deprecation Date |
| --- | --- |
| All Mutual Friends API | October 24th, 2018 |
| Profile Expression Kit | September 30th, 2018 |
| Optimized Sharing to Messenger | August 1st, 2018 |
| Taggable Friends | April 4th, 2018 |

Learn More
----------

Learn more about developing with Meta with the following guides:

|     |     |     |
| --- | --- | --- |
| * [Access Levels](https://developers.facebook.com/docs/graph-api/overview/access-levels/#development-mode-and-live-mode)<br>* [App Review](https://developers.facebook.com/docs/app-review)<br>* [App Roles](https://developers.facebook.com/docs/development/build-and-test/app-roles) | * [App Types](https://developers.facebook.com/docs/development/create-an-app#app-type)<br>* [Business Roles](https://www.facebook.com/business/help/442345745885606?id=180505742745347)<br>* [Development Mode](https://developers.facebook.com/docs/development/build-and-test/app-modes) | * [Live Mode](https://developers.facebook.com/docs/development/build-and-test/app-modes)<br>* [Permissions Reference](https://developers.facebook.com/docs/permissions/reference) |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Ad Targeting Data Access
========================

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Ad Targeting Data Access** feature allows access to ad targeting data within the Facebook Open Research and Transparency tool for election, political, and social issue ads that are run on Facebook from Meta and Instagram from Meta. The allowed usage of this functionality is to conduct research about Meta's role in society. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* To conduct research about Meta's role in society
    

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature requires that you complete [business verification](https://developers.facebook.com/docs/development/release/business-verification) in addition to App Review.
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Ads Management Standard Access
==============================

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Ads Management Standard Access** feature allows your app to access the Marketing API. The allowed usage for this feature is to enable an unlimited number of ad accounts and lower rate limiting. At a minimum, ads\_read or ads\_management permission is required to use Ads Management Standard Access. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Enable an unlimited number of ad accounts and lower rate limiting.
    
* To read ads reports for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_read** permission.
    
* To read and manage ads for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_management** permission.
    
* To pull ads reports from a set of clients, and to read and manage ads from another set of clients, request **Ads Management Standard Access**, along with both **ads\_read** and **ads\_management** permissions.
    

Common Endpoints
----------------

[/adaccount](https://developers.facebook.com/docs/graph-api/reference/adaccount)  
[/adaccount/adcreatives/](https://developers.facebook.com/docs/graph-api/reference/adaccount/adcreatives/)  
[/adaccount/ads](https://developers.facebook.com/docs/graph-api/reference/adaccount/ads)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Business Asset User Profile Access
==================================

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Business Asset User Profile Access** feature allows your app to read the User Fields for users engaging with your business assets such as id, ids\_for\_business, name, and picture. The allowed usage for this feature is to read one or more of the User Fields in a business app experience. You may also use this feature to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Common Endpoints
----------------

[/User](https://developers.facebook.com/docs/graph-api/reference/user#fields)

Allowed Usage
-------------

You can use this feature if your app uses one or more of the User Fields in its business app experience.

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Groups API
==========

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Groups API** feature allows your app to access content in a Facebook Group. The allowed usage for this feature is to help people manage the posts and content published to their group or to get information about content posted to their Group. It can also be used to let people publish content from your app to their Facebook Group. This feature is often used with the **publish\_to\_group** and **groups\_access\_member\_info** permissions. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Help people manage the posts and content published to their Group.
    
* Help people get information about content posted to their Group.
    
* Let people publish content from your app to their Facebook Group.
    
* Help people get aggregated insights about activity happening in their Group.
    

Common Endpoints
----------------

[/group](https://developers.facebook.com/docs/graph-api/reference/group)

Additional Details
------------------

* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    
* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Human Agent
===========

The **Human Agent** feature allows your app to have a human agent respond to user messages using the **human\_agent** tag within 7 days of a user's message. The allowed usage for this feature is to provide human agent support in cases where a user’s issue cannot be resolved in the standard messaging window. Examples include when the business is closed for the weekend, or if the issue requires more than 24 hours to resolve.

Allowed Usage
-------------

* Provide human agent support in cases where a user’s issue cannot be resolved in the standard messaging window.
    

Common Endpoints
----------------

[/page/messages](https://developers.facebook.com/docs/graph-api/reference/page/messages)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Instagram Public Content Access
===============================

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The Instagram Public Content Access feature allows your app to access Instagram Graph API's Hashtag Search endpoints. The allowed usages for this feature is to discover content associated with your hashtag campaigns, understand public sentiment around your brand or identify contest, competition and sweepstakes entrants. It can also be used to provide customer support and better understand and manage your audience. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Discover content associated with its current campaign.
    
* Provide customer support.
    
* Identify entrants to its contests, competitions, or sweepstakes.
    
* Understand public sentiment around brand.
    
* Understand and manage their audience, develop their content strategy and obtain digital rights.
    

Common Endpoints
----------------

* [/ig-hashtag-search](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag-search)
    
* [/ig-hashtag](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag)
    
* [/ig-hashtag/recent-media](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/recent-media)
    
* [/ig-hashtag/top-media](https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag/top-media)
    

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Live Video API
==============

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Live Video API** feature allows an app to manage live videos to Pages, Groups and User timelines when combined with the correct matching permission.

Allowed Usage
-------------

* App users can publish live video content from your app to Facebook.
    

Common Endpoints
----------------

[/group/live\_videos](https://developers.facebook.com/docs/graph-api/reference/group/live_videos)  
[/live-video](https://developers.facebook.com/docs/graph-api/reference/live-video)  
[/page/live\_videos](https://developers.facebook.com/docs/graph-api/reference/page/live_videos)  
[/user/live\_videos](https://developers.facebook.com/docs/graph-api/reference/user/live_videos)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

oEmbed Read
===========

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **oEmbed Read** feature allows your app to get embed HTML and basic metadata for public Facebook and Instagram pages, posts, and videos. The allowed usage for this feature is to provide front-end views of Facebook and Instagram pages, posts, and videos. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Provide front-end views of Facebook and Instagram pages, posts, and videos.
    

Common Endpoints
----------------

* [/oembed\_page](https://developers.facebook.com/docs/graph-api/reference/oembed-page/)
    
* [/oembed\_post](https://developers.facebook.com/docs/graph-api/reference/oembed-post/)
    
* [/oembed\_video](https://developers.facebook.com/docs/graph-api/reference/oembed-video/)
    
* [/instagram\_oembed](https://developers.facebook.com/docs/graph-api/reference/instagram-oembed/)
    

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    

* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Page Mentioning
===============

The **Page Mentioning** feature allows your app mention any Facebook Page when publishing posts on the Pages managed by your app. To use Page Mentioning, your app needs to have been granted the **manage\_pages** and **publish\_pages** permissions. The allowed usage for this feature is to to let people use your app to publish Page posts that mention other Pages or to mention Pages relevant to the content in your page post. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Allow people to use your app to publish Page posts that mention other Pages.
    
* Mention Pages relevant to the content in your page post.
    

Common Endpoints
----------------

[/page/feed](https://developers.facebook.com/docs/graph-api/reference/page/feed)  
[/page-post](https://developers.facebook.com/docs/graph-api/reference/page-post)  
[/page-post/comments](https://developers.facebook.com/docs/graph-api/reference/object/comments)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    
* To use Page Mentioning, your app needs to have been granted the [`pages_read_engagement`](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) and [`pages_manage_posts`](https://developers.facebook.com/docs/permissions/reference/pages_manage_posts) permissions.
    
* If your app has its own user authentication system, please include a working username and password in your review instructions so our team can easily reproduce your page mentioning functionality.
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Page Public Content Access
==========================

The **Page Public Content Access** feature allows an app access to the Pages Search API and to read public data for Pages for which you lack the **pages\_read\_engagement** permission and the **pages\_read\_user\_content** permission. Readable data includes business metadata, public comments and posts. The allowed usage for this feature is to analyze and/or display posts and engagement on Pages.

Allowed Usage
-------------

* Analyze and/or display posts and engagement on Pages.
    

Common Endpoints
----------------

[/page/feed](https://developers.facebook.com/docs/graph-api/reference/page/feed)  
[/page-post](https://developers.facebook.com/docs/graph-api/reference/page-post)  
[/page-post/comments](https://developers.facebook.com/docs/graph-api/reference/object/comments)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    
* While you are testing your app and before you submit it for review, your app can only access content on a Page for which the following is true: The person who holds the admin role for the Page also holds an admin, developer, or tester role on the app. If you want the app to be able to access public content on other Pages, you must submit this feature for review. Once you set your app to live mode, it will not be able to see any Page public content without this feature.
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Page Public Metadata Access
===========================

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **Page Public Metadata Access** allows your app access to the [Pages Search API](https://developers.facebook.com/docs/pages/searching) and to read public data for Pages for which you lack the [pages\_read\_engagement permission](https://developers.facebook.com/docs/permissions/reference/pages_read_engagement) and the [pages\_read\_user\_content permission](https://developers.facebook.com/docs/permissions/reference/pages_read_user_content). The allowed usage for this feature is to analyze engagement with public Pages by viewing Like and follower counts, or aggregate public-facing **About** Page information from multiple, disparate pages. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Analyze engagement with public Pages by viewing Like and follower counts.
    
* Aggregate public-facing "about" Page information from multiple, disparate pages.
    

Common Endpoints
----------------

[/page](https://developers.facebook.com/docs/graph-api/reference/page)

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    
* If your app also needs to read the [Page Feed](https://developers.facebook.com/docs/graph-api/reference/page/feed) edge, or [Comments](https://developers.facebook.com/docs/graph-api/reference/comment) on a Page's [Posts](https://developers.facebook.com/docs/graph-api/reference/post), request the [Page Public Content Access](#page-public-content-access) feature instead.
    
* This feature is superseded by the Page Public Content Access (PPCA) feature. If your App Review submission includes PPCA, or your app has already been approved for PPCA, you cannot request this permission.
    
* If your app also needs to create, update, or delete data on a Page, request the [`pages_read_engagement`](https://developers.facebook.com/docs/permission/reference/pages_read_engagement) permission instead.
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

Threat Exchange
===============

_Requires [App Review](https://developers.facebook.com/docs/app-review)._

The **ThreatExchange** feature allows your app to share threat data among a select group of vetted industry partners. The allowed usage for this feature is to share threat data with a specific group of partners to achieve their security goals. You may also use this feature to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

Allowed Usage
-------------

* Share threat data with a specific group of partners to achieve their security goals.
    

Additional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. [Learn More](https://developers.facebook.com/docs/app-review)
    
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. [Learn More Here](https://developers.facebook.com/docs/development/release/business-verification)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)