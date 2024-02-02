Overview - Instagram Platform












DocsToolsSupportLog InInstagram Platform* Instagram Graph API
	+ Overview
	+ Getting Started
	+ Guides
	+ Reference
	+ Changelog
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
On This PageOverviewBase URLApp UsersAuthenticationAuthorizationInstagram MessagingCollaboratorsPagesTasksReferring to tasksApp ReviewPrivate AppsBusiness VerificationRate LimitingWebhooksInstagram MessagingOverview
========


The Instagram Graph API is a collection of Facebook Graph API endpoints that allow apps to access data in Instagram Professional accounts (both Business and Creator accounts). If you are unfamiliar with the Facebook Graph API, please read our Graph API documentation before proceeding.


Base URL
--------


All endpoints can be accessed via the `graph.facebook.com` host.


App Users
---------


Instagram Professional accounts are accessed indirectly through Facebook accounts so your app users must have a Facebook account and use it when signing into your app. In addition, the Facebook account must be able to perform admin-equivalent Tasks on a Facebook Page that has been connected to the Instagram account they are trying to access.


These requirements apply to all app users, even those who have a Role on your app or a Role on a Business that has claimed your app.


Authentication
--------------


App user authentication is handled through access tokens. Instagram Professional accounts are accessed indirectly through Facebook accounts, so all API requests must include your app users's Facebook User access token. You can get tokens from app users by implementing Facebook Login. Note that Facebook Login does not support Instagram credentials so app users must sign in using a Facebook account.


Authorization
-------------


Endpoint authorization is handled through permissions and features. Before your app can use an endpoint to access an app user's Instagram data, you must first request all permissions required by those endpoints from the app user. The app user must then grant those permissions to your app. Once granted, you can query the endpoints to access the user's data.


Note that a permission only allows access to data created by the user who granted the permission. There are a few endpoints that allow apps to access data not created by the app user, but the accessible data is limited and public.


You can request permissions from app users by implementing Facebook Login. App users who have a role on your app can grant any requested permissions. App users who do not have a role on your app can only grant permissions and features that have been approved through the App Review process.


The API uses the following permissions and features:


* `instagram_basic`
* `instagram_content_publish`
* `instagram_manage_comments`
* `instagram_manage_insights`
* `instagram_shopping_tag_products`
* `pages_show_list`
* `pages_read_engagement`
* Instagram Public Content Access


Refer to our endpoint reference to determine which permission and features your app will need to request from app users.


### Instagram Messaging


If you plan to implement Instagram Messaging from Messenger Platform, you will need to include the `instagram_manage_messages` permission.

 
 Learn more about Instagram Messaging.

Collaborators
-------------


The Instagram Collab feature allows Instagram app users to co-author content (i.e. publish media) with other accounts (collaborators).


With a few exceptions, data on or about co-authored media can only be accessed through the API by the user who published the media; collaborators are unable to access this data via the API. The only exceptions are when searching for top performing media or recently published media that has been tagged with a specific hashtag. See Hashtag Search.


Pages
-----


Instagram Professional accounts must be connected to a Facebook Page before their data can be accessed through the API. Once connected, any Facebook User who is able to perform Tasks on that Page can grant your app an access token, which can then be used in API requests.


Our Add or change the Facebook Page connected to your Instagram professional account help article explains how to connect to a Facebook Page to an Instagram Professional account.


Tasks
-----


In order for an app user to grant your app permissions, the app user must be able to perform tasks on the Facebook Page connected to the Instagram account they are attempting to access. App users may grant your app permissions based on tasks they are able to perform as follows:




| Permission | `MANAGE` | `CREATE_CONTENT` | `MODERATE` | `ADVERTISE` | `ANALYZE` |
| --- | --- | --- | --- | --- | --- |
| instagram\_basic | ✔ | ✔ | ✔ | ✔ | ✔ |
| instagram\_content\_publish | ✔ | ✔ |  |  |  |
| instagram\_manage\_comments | ✔ | ✔ | ✔ |  |  |
| instagram\_manage\_insights | ✔ | ✔ | ✔ | ✔ | ✔ |

You can determine which tasks an app user is able to perform on a Page by querying the `GET /me/accounts` endpoint with the app user's User access token. The endpoint will return a list of Pages that the app user is able to perform tasks on, and indicate which tasks the user can perform on each of them.


Refer to the reference documentation to see which permissions each endpoint requires. The API does not support Business Manager System Users, or app users who have the Live Contributor role.


### Referring to tasks


If you need to inform your app users about tasks (and which ones are required to use your app properly), here's how tasks are referred to in our various UIs.


#### Classic Pages


Classic Pages refer to tasks as **roles**. App users with an Admin role on a Page can grant your app any permission. App users with other roles can grant permissions as follows:




| Role | Grantable Permissions |
| --- | --- |
| Editor | instagram\_basic
instagram\_content\_publish |
| Moderator | instagram\_basic
instagram\_manage\_comments
instagram\_manage\_insights |
| Advertiser | instagram\_basic
instagram\_manage\_insights |
| Analyst | instagram\_basic
instagram\_manage\_insights |

#### New Experience Pages


New Experience Pages refer to tasks as either Facebook Access or Task Access. App users with Facebook Access on a Page can grant your app any permission. App users with Task Access can grant permissions as follows:




| Task Access | Grantable Permissions |
| --- | --- |
| Ads | instagram\_basic |
| Content | instagram\_basic
instagram\_content\_publish |
| Insights | instagram\_basic
instagram\_manage\_insights |
| Messages & Community Activity | instagram\_basic
instagram\_manage\_comments |

To determine if a Page is using the new experience, request its `has_transitioned_to_new_page_experience` field. This value return `true` if the Page uses the new experience.


App Review
----------


Your app must complete App Review before it can be used by app users who do not have a Role on your app or a Role on a Business that has claimed your app. If your app will only be used by app users who have a Role on your app or Business, you do not need to complete App Review.


Your App Review submission does not need to include any Facebook test user credentials if you have implemented Facebook Login and your app is publicly available. However, if our reviewers need to sign into a non-Facebook account in order to trigger your implementation of Facebook Login, you must include the non-Facebook account credentials in your submission.


### Private Apps


If our reviewers are unable to test your app because it is behind a private intranet, has no user interface, or has not implemented Facebook Login, you may only request approval for these Permissions:


* instagram\_basic
* instagram\_manage\_comments


Business Verification
---------------------


You must complete Business Verification if your app will be used by app users who do not have a Role on the app itself, or a Role in a Business that has claimed the app.


Rate Limiting
-------------


All endpoints are subject to Instagram Business Use Case rate limiting except for Business Discovery and Hashtag Search endpoints, which are subject to Platform Rate limiting.


Webhooks
--------


You can use Webhooks to have notifications sent to you whenever someone comments on your app users' media objects or when any of their stories expire. Refer to our Webhooks documentation to learn how to use Webhooks, then set up a webhook for the `Instagram` topic and subscribe to its `comments` and `story_insights` fields.


Instagram Messaging
-------------------


Several Instagram Graph API endpoints are used in conjunction with the Messenger Platform endpoints to allow your app users to interact with direct messages sent to their Instagram Professional accounts. Refer to the Messenger Platform's Instagram Messaging documentation to learn how to access messages in Instagram Business accounts.


On This PageOverviewBase URLApp UsersAuthenticationAuthorizationInstagram MessagingCollaboratorsPagesTasksReferring to tasksApp ReviewPrivate AppsBusiness VerificationRate LimitingWebhooksInstagram MessagingFollow Us* 
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