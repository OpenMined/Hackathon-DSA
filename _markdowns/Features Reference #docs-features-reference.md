
Features Reference - Graph API - Documentation - Meta for Developers











Graph API* Overview
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
Features Reference
==================


Features are authorization mechanisms that allow apps to access specific types of data through our various APIs. In this way they are similar to Permissions, however Features cannot be granted to an app by an app user. Instead, Features are active or inactive depending on the app user's relationship to the app and the app's mode when it is being used.


For apps in Development Mode, all Features except for Page Public Content Access and Page Public Metadata Access are active for any app user who has a Role on the app or a Role in a Business that has claimed the app.


For apps in Live Mode, only Features approved through App Review are active for app users. This also applies to app users who have a Role on the app or Business.


For Business app types (which have access levels instead of modes), Features are active for any app users who have a Role on the app or in a Business that has claimed the app, unless access has been removed. In order for a Feature to be active for app users without a Role on the app or Business, it must first be approved through App Review.


Access to any Feature that is granted by default or through App Review can be used to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).


Unlike Permissions, Features do not expire, their approval will not be revoked, if they are unused.




 Feature | Description || Ad Targeting Data Access |  The **Ad Targeting Data Access** feature allows access to ad targeting data within the Facebook Open Research and Transparency tool for election, political, and social issue ads that are run on Facebook from Meta and Instagram from Meta. **Allowed Usage*** To conduct research about Meta's role in society
 |
| Business Asset User Profile Access |  The **Business Asset User Profile Access** feature allows your app to read the User Fields for users engaging with your business assets such as id, ids\_for\_business, name, and picture. **Allowed Usage**
 You can use this feature if your app uses one or more of the User Fields in its business app experience.  |
| Ads Management Standard Access |  The **Ads Management Standard Access** feature allows your app to access the Marketing API. **Allowed Usage*** Enable an unlimited number of ad accounts and lower rate limiting.
* To read ads reports for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_read** permission.
* To read and manage ads for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_management** permission.
* To pull ads reports from a set of clients, and to read and manage ads from another set of clients, request **Ads Management Standard Access**, along with both **ads\_read** and **ads\_management** permissions.
 |
| Business Asset User Profile Access |  The **Business Asset User Profile Access** feature allows your app to read the User Fields for users engaging with your business assets such as id, ids\_for\_business, name, and picture. **Allowed Usage**
 You can use this feature if your app uses one or more of the User Fields in its business app experience.  |
| Groups API |  The **Groups API** feature allows your app to access content in a Facebook Group.**Allowed Usage*** Help people manage the posts and content published to their Group.
* Help people get information about content posted to their Group.
* Let people publish content from your app to their Facebook Group.
* Help people get aggregated insights about activity happening in their Group.
 |
| Human Agent |  The **Human Agent** feature allows your app to have a human agent respond to user messages using the **human\_agent** tag within 7 days of a user's message. **Allowed Usage*** Provide human agent support in cases where a user’s issue cannot be resolved in the standard messaging window.
 |
| Instagram Public Content Access |  The **Instagram Public Content Access** feature allows your app to access Instagram Graph API's Hashtag Search endpoints. **Allowed Usage*** Discover content associated with its current campaign.
* Provide customer support.
* Identify entrants to its contests, competitions, or sweepstakes.
* Understand public sentiment around brand.
* Understand and manage their audience, develop their content strategy and obtain digital rights.
 |
| Live Video API |  The **Live Video API** feature allows an app to manage live videos to Pages, Groups and User timelines when combined with the correct matching permission. **Allowed Usage*** App users can publish live video content from your app to Facebook.
 |
| oEmbed Read |  The **oEmbed Read** feature allows your app to get embed HTML and basic metadata for public Facebook and Instagram pages, posts, and videos. **Allowed Usage*** Provide front-end views of Facebook and Instagram pages, posts, and videos.
 |
| Page Mentioning |  The **Page Mentioning** feature allows your app mention any Facebook Page when publishing posts on the Pages managed by your app. **Allowed Usage*** Allow people to use your app to publish Page posts that mention other Pages.
* Mention Pages relevant to the content in your page post.
 |
| Page Public Content Access |  The **Page Public Content Access** feature allows your app access to the Pages Search API and to read public data for Pages for which you lack the pages\_read\_engagement permission and the pages\_read\_user\_content permission. Readable data includes business metadata, public comments and posts.**Allowed Usage*** Analyze and/or display posts and engagement on Pages.
 |
| Page Public Metadata Access |  The **Page Public Metadata Access** feature allows your app access to the Pages Search API and to read public data for Pages for which you lack the public Page fields and the Pages Search API. **Allowed Usage*** Analyze engagement with public Pages by viewing Like and follower counts.
* Aggregate public-facing "about" Page information from multiple, disparate pages.
 |
| Threat Exchange |  The **ThreatExchange** feature allows your app to share threat data among a select group of vetted industry partners. **Allowed Usage*** Share threat data with a specific group of partners to achieve their security goals.
 |

Deprecated Features
-------------------




 Feature | Deprecation Date || All Mutual Friends API | October 24th, 2018 |
| Profile Expression Kit | September 30th, 2018 |
| Optimized Sharing to Messenger | August 1st, 2018 |
| Taggable Friends | April 4th, 2018 |

Learn More
----------


Learn more about developing with Meta with the following guides:




|  |  |  |
| --- | --- | --- |
| * Access Levels
* App Review
* App Roles
 | * App Types
* Business Roles
* Development Mode
 | * Live Mode
* Permissions Reference
 |


































 
