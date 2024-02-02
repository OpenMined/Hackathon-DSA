Permissions Reference - Graph API - Documentation - Meta for Developers

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
Permissions Reference for Meta Technologies APIs
================================================

Permissions are a form of granular, user-granted Graph API authorization. Before your app can use an endpoint to access an app user's data, the app user must grant your app all permissions required by that endpoint.

Starting on or after October 27, 2023, if your app requests permission to use an endpoint to access an app user’s data, you may need to complete data handling questions. See this blog post and FAQs for more information.

Beginning September 5, some developers may also be required to answer data handling questions during their annual Data Use Checkup.

You may also use any permission granted to your app to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified).

### Requirements

* App Review
 is required for **all permissions** except for `email` and `public_profile` if your app needs access to data that you do not own or manage
* Business Verification
 is required for all apps making requests for 
 Advanced Access
* Only select permissions that your app needs to function as intended. Selecting unneeded permissions is a common reason for rejection during app review
### Ways to ask for a permission

When users log onto your app, they receive a request to grant the permissions your app has requested. Users can grant or deny the requested permissions or any subset of them.

* Facebook Login
* Facebook Login for Business
* Business Login for Instagram
* Meta Business Manager
If your app does not use a permission for 90 days, usually due to user inactivity, the app user must regrant your app that permission.

### Remove a permission

You can use the app dashboard to remove a permission your app no longer uses or to remove a permission that has been deprecated.

A
-

 Permission | Description || `ads_management` |  The **ads\_management** permission allows your app to both read and manage the Ads account it owns, or has been granted access to, by the Ad account owner. ***Allowed Usage**** Programmatically create campaigns, manage ads, and fetch metrics.
* Build ad management tools that provide innovative solutions and differentiated value for advertisers.
 |
| `ads_read` |  The **ads\_read** permission allows your app to access the Ads Insights API to pull Ads report information for Ad accounts you own or have been granted access to by the owner or owners of other ad accounts through this permission. This permissions also grants your app access to the Server-Side API to allow advertisers to send web events from their servers directly to Facebook. ***Allowed Usage**** Provide API access to your ad performance data for use in custom dashboards and data analytics.
* Send web events from your server directly to Facebook.
 |
| `attribution_read` |  The **attribution\_read** permission grants your app access to the Attribution API to pull attribution report data for lines of business you own or have been granted access to by the owner or owners of other lines of business. ***Allowed Usage**** Provides the ability for your app to access ads performance data from Attribution for use in custom dashboards and data analytics.
 |
B
-

 Permission | Description || `business_management` |  The **business\_management** permission allows your app to read and write with the Business Manager API. ***Allowed Usage**** Manage business assets such as an ad account.
* Claim ad accounts.
 |
C
-

 Permission | Description || `catalog_management` |  The **catalog\_management** permission allows your app to create, read, update and delete business-owned product catalogs that the user is an admin of. ***Allowed Usage**** Build commerce-related solutions like ecommerce platforms, travel platforms and dynamic ads.
* Build inventory type management solutions like product inventory, hotel inventory or car inventory.
 |
E
-

 Permission | Description || `email` |  The **email** permission allows your app to read a person's primary email address. ***Allowed Usage**** Communicating with people and letting them log into your app with the email address associated with their Facebook profile.
 |
G
-

 Permission | Description || `gaming_user_locale` |  The **gaming\_user\_locale** permission allows your app to get a user's preferred language while the user plays a game on Facebook (for example, Instant Games or Cloud Gaming). ***Allowed Usage**** Display a game interface in the user's preferred language.
 |
| `groups_access_member_info` | *Deprecated for v19.0. Will be removed for all version April 22, 2024.*
 The **groups\_access\_member\_info** permission allows your app to read publicly available group member information like name and ID if the post author has granted your app access. ***Allowed Usage**** Allow apps to get content posted in their group with user details.
* Help admins get aggregated insights about activity happening in their group.
 |
I
-

 Permission | Description || `instagram_basic` |  The **instagram\_basic** permission allows your app to read an Instagram account profile's info and media. ***Allowed Usage**** Get basic metadata of an Instagram Business account profile, for example username and ID.
 |
| `instagram_content_publish` |  The **instagram\_content\_publish** permission allows your app to create organic feed photo and video posts on behalf of a business user. ***Allowed Usage**** Managing organic content creation process for Instagram (for example, post photos and videos to main feed) on behalf of a business.
 |
| `instagram_graph_user_media` |  The **instagram\_graph\_user\_media** permission allows your app to read the Media node, which represents an image, video, or album and the node’s edges. ***Allowed Usage**** Creating physical or digital books from the app user's photos, including exporting photos for printing.
* Displaying the app users photos to other app users within the app, for example with social or dating apps.
* Editing or creating new photos or videos based on the app user's existing photos and videos, (e.g. for photo or video Editing Apps).
* Displaying the app user's photos and videos in an external device such as a TV or digital photo frame.
 |
| `instagram_graph_user_profile` |  The **instagram\_graph\_user\_profile** permission allows your app to read the app user's profile. ***Allowed Usage**** Read fields in an Instagram user profile, for example user ID and account type.
 |
| `instagram_manage_comments` |  The **instagram\_manage\_comments** permission allows your app to create, delete and hide comments on behalf of the Instagram account linked to a Page. Your app can also read and respond to public media and comments that a business has been photo tagged or @mentioned in. ***Allowed Usage**** Read, update and delete comments of Instagram Business accounts.
* Read media objects, such as stories, of Instagram Business accounts.
 |
| `instagram_manage_insights` |  The **instagram\_manage\_insights** permission allows your app to get access to insights for the Instagram account linked to a Facebook Page. Your app can also discover and read the profile info and media of other business profiles. ***Allowed Usage**** Get metadata of an Instagram Business account.
* Get data insights of an Instagram Business account.
* Get story insights of an Instagram Business account.
 |
| `instagram_manage_messages` |  The **instagram\_manage\_messages** permission allows business users to read and respond to Instagram Direct messages. ***Allowed Usage**** Business that want to retrieve threads and messages from its Direct inbox.
* Business that want to manage messages with their customer.
* Business that want to use third-party customer relationship management (CRM) tools to manage its IG Direct inbox.
 |
| `instagram_shopping_tag_products` |  The **instagram\_shopping\_tag\_products** permission allows an app to tag Instagram media with product tags and appeal product rejections. ***Allowed Usage**** Check eligibility for product tagging
* Get catalogs and products
* Tag media with product tags
* Manage existing product tags
* Appeal product rejections
 |
L
-

 Permission | Description || `leads_retrieval` |  The **leads\_retrieval** permission allows your app to retrieve and read all information captured by a lead ads form associated with an ad created in Ads Manager or the Marketing API. ***Allowed Usage**** Reach out to the people who followed up your lead ad form requesting more information. For example, an auto dealer reaching out to a potential customer (lead) that responded to their ad with quotes for a car.
* For advertiser authorized CRM platforms to pull the lead data on behalf of the advertisers. These advertisers can then use the lead information to reach out to the user.
 |
M
-

 Permission | Description || `manage_fundraisers` |  The **manage\_fundraisers** permission allows an app to create, update, and read a fundraiser and its donations on behalf of a user. ***Allowed Usage**** Help fundraiser creators to expand their reach on Facebook.
* Sync the amount raised displayed on the fundraiser's website and the linked Facebook fundraiser.
 |
P
-

 Permission | Description || `pages_events` |  The **page\_events** permissions allows your app permission to log events on behalf of Facebook Pages administered by people using your app and to send those events to Facebook for ads targeting, optimization and reporting. ***Allowed Usage**** Send businesses related activities (for example purchase, add-to-cart, lead) on behalf of Pages owned by the people who use your app.
 |
| `pages_manage_ads` |  The **pages\_manage\_ads** permission allows your app to manage ads associated with the Page. ***Allowed Usage**** Create ads for your Page.
* Manage ads for your Page.
 |
| `pages_manage_cta` |  The **pages\_manage\_cta** permission allows your app to carry out POST and DELETE functions on endpoints used to manage call-to-action buttons on a Facebook Page. ***Allowed Usage**** Provide API access to manage call-to-action buttons on Pages that you manage.
 |
| `pages_manage_instant_articles` |  The **pages\_manage\_instant\_articles** permission allows your app to manage Instant Articles on behalf of Facebook Pages administered by people using your app. ***Allowed Usage**** Create and update Instant Articles for Pages owned by the people who use your app.
 |
| `pages_manage_engagement` |  The **pages\_manage\_engagement** permission allows your app to create, edit and delete comments posted on the Page. ***Allowed Usage**** Publish a comment on a Page post.
* Update your comment on a Page post.
* Delete a comment on a Page post.
* Like a Page post or remove your Like from a Page post.
 |
| `pages_manage_metadata` |  The **pages\_manage\_metadata** permission allows your app to subscribe and receive webhooks about activity on the Page, and to update settings on the Page. ***Allowed Usage**** Subscribe to receive webhooks of your Page.
* Update settings of your Page.
 |
| `pages_manage_posts` |  The **pages\_manage\_posts** permission allows your app to create, edit and delete your Page posts. ***Allowed Usage**** Publish a post, photo, or video to your Page.
* Update a post, photo, or video on your Page.
* Delete a post, photo, or video on your Page.
 |
| `pages_messaging` |  The **pages\_messaging** permission allows your app to manage and access Page conversations in Messenger. ***Allowed Usage**** Create interactive experiences initiated by a user.
* Confirm customer interactions such as purchases, orders and bookings.
* Send customer support messages.
 |
| `pages_read_engagement` |  The **pages\_read\_engagement** permission allows your app to read content (posts, photos, videos, events) posted by the Page, read followers data (including name, PSID), and profile picture, and read metadata and other insights about the Page. ***Allowed Usage**** Get content posted by your Page.
* Get names, PSIDs, and profile pictures of your Page followers.
* Get metadata about your Page.
 |
| `pages_read_user_content` |  The **pages\_read\_user\_content** permission allows your app to read user generated content on the Page, such as posts, comments, and ratings by users or other Pages, and to delete user comments on Page posts. ***Allowed Usage**** Get user generated content on your Page.
* Get posts that your Page is tagged in.
* Delete comments posted by users on your Page.
 |
| `pages_show_list` |  The **pages\_show\_list** permission allows your app to access the list of Pages a person manages. ***Allowed Usage**** Show a person the list of Pages they manage.
* Verify that a person manages a Page.
 |
| `pages_user_gender` |  The **pages\_user\_gender** permission allows your app to access a user's gender through the Page your app is connected to. ***Allowed Usage**** Personalize experiences or recommendations based on gender.
* Use gendered language such as correct pronouns and titles.
 |
| `pages_user_locale` |  The **pages\_user\_locale** permission allows your app to access a user's locale through the Page your app is connected to. ***Allowed Usage**** Personalize experiences based on the locale of a person by surfacing locale specific content.
* Send responses in the preferred language of the person.
* Display numbers, times, and dates correctly for the locale of the person.
 |
| `pages_user_timezone` |  The **pages\_user\_timezone** permission grants your app access to a user's time zone through the Page your app is connected to. ***Allowed Usage**** Prevent messages from being sent at an inconvenient time.
* Send time sensitive content or recurring news at a specific time.
* Provide tailored content based on time.
* Send time appropriate greetings.
 |
| `private_computation_access` |  The **private\_computation\_access** permission allows an app to access the Meta Private Computation products. ***Allowed Usage**** Monitor private attribution datasets for a business.
* Monitor instances for private attribution datasets for a business.
* Create and manage instances for private attribution datasets for a business.
 |
| `public_profile` |  The **public\_profile** permission allows an app to read the Default Public Profile Fields on the User node. This permission is automatically granted to all apps. ***Allowed Usage**** Authenticate app users and provide them with a personalized in-app experience.
 |
| `publish_to_groups` | *Deprecated for v19.0. Will be removed for all version April 22, 2024.*
 The **publish\_to\_groups** permission allows your app to post content into a Group on behalf of a person if they've granted your app access. ***Allowed Usage**** Allow people to publish content from your app to their Facebook group.
* Help people manage the content published to their group.
 |
| `publish_video` |  The **publish\_video** permission allows your app to publish live videos to an app user's timeline, group, event or Page. ***Allowed Usage**** Grants an app permission to live-video stream to an app user's timeline, group, event or Page.
 |
R
-

 Permission | Description || `read_insights` |  The **read\_insights** permission allows your app to read the Insights data for Pages, apps and web domains the person owns. ***Allowed Usage**** Integrate Facebook's app, page or domain insights into your own analytics tools.
 |
U
-

 Permission | Description || `user_age_range` |  The **user\_age\_range** permission allows your app to access a person's age range as listed in their Facebook profile. ***Allowed Usage**** Your app is legally required to be age-gated.
* Your app contains content that is not suitable for the general Facebook user base, for example dating, violent or mature content.
 |
| `user_birthday` |  The **user\_birthday** permission allows your app to read a person's birthday as listed in their Facebook profile. ***Allowed Usage**** Provide age-relevant content to people when their age range is not sufficient.
 |
| `user_friends` |  The **user\_friends** permission allows your app to get a list of a person's friends using that app. ***Allowed Usage**** Provide Facebook-related content to personalize a person's experience.
 |
| `user_gender` |  The **user\_gender** permission allows your app to read a person's gender as listed in their Facebook profile. ***Allowed Usage**** To render pronouns.
* Personalize a person's experience based on gender, for example dating, shopping and fashion apps.
 |
| `user_hometown` |  The **user\_hometown** permission allows your app to read a person's hometown location from their Facebook profile. ***Allowed Usage**** Provide a personalized experience based on where a person lived or grew up.
 |
| `user_likes` |  The **user\_likes** permission allows your app to read a list of all Facebook Pages that a user has liked. ***Allowed Usage**** Provide a personalized experience by correlating or surfacing content related to the person’s likes. This includes curating content at scale to customize apps with large amounts of content and to enable people to share their likes with others, such as in the case of dating and music apps.
* Allow parental access controls and monitoring apps to analyze user likes for potential safety and wellbeing issues for people under 18 years old, as used solely by parents and guardians for under 18 year old dependents and limited to youth social media analysis as presented in the app’s user interface.
 |
| `user_link` |  The **user\_link** permission allows your app to access the Facebook profile URL of the person using your app. ***Allowed Usage**** Provide a way for someone who uses your app to visit another person's Facebook profile.
 |
| `user_location` |  The **user\_location** permission allows your app to read the city name as listed in the location field of a person's Facebook profile. ***Allowed Usage**** Provide a personalized experience based on the city name as listed in the location field of a person's Facebook profile.
 |
| `user_messenger_contact` |  The **user\_messenger\_contact** permission allows a business to contact a person via Messenger upon their approval or initiation of a chat thread with the business's Page. ***Allowed Usage**** For a Page to send a person an initial message, post-purchase updates and account updates.
 |
| `user_photos` |  The **user\_photos** permission allows your app to read the photos a person has uploaded to Facebook. ***Allowed Usage**** Create physical or digital books or albums of a person's photos, which includes permitting people to export photos for printing.
* Provide people with the ability to display their photos with other app users, for example in dating or social apps.
* Provide people with the ability to edit or create new photo content based on existing photos.
 |
| `user_posts` |  The **user\_posts** permission allows your app to access the posts that a user has made on their timeline. ***Allowed Usage**** Enable people to create physical or digital books or albums of their timelines, and to share memories from their timeline on Facebook or on other social apps.
* Allow parental access controls and monitoring apps to analyze a post's content to detect potential risk to safety or wellbeing for people under 18 years old, as used solely by parents and guardians for under 18 year old dependents and limited to youth social media analysis as presented in the app’s user interface.
 |
| `user_videos` |  The **user\_videos** permission allows your app to read a list of videos uploaded by a person. ***Allowed Usage**** Display a person's videos on a TV via a set-top box or in a digital photo frame.
* Provide people with the ability to edit or create new video content using existing videos.
* Provide people with the ability to display their video with owners within their app, for example in dating or social apps.
 |
W
-

 Permission | Description || `whatsapp_business_management` |  The **whatsapp\_business\_management** permission allows your app to read and/or manage WhatsApp business assets you own or have been granted access to by other businesses through this permission. These business assets include WhatsApp business accounts, phone numbers, message templates, QR codes and their associated messages, and webhook subscriptions. ***Allowed Usage**** Manage WhatsApp business assets.
* Display WhatsApp Business Account analytics in your customer portal.
 |
| `whatsapp_business_messaging` |  The **whatsapp\_business\_messaging** permission allows an app to send WhatsApp messages to a specific phone number, upload and retrieve media from messages, manage and get WhatsApp business profile information, and to register those phone numbers with Meta. ***Allowed Usage**** Send WhatsApp messages to a specific phone number
* Upload and retrieve media from messages
* Manage and get WhatsApp business profile information
* Register a phone number with Meta
 |
Permission Dependencies
-----------------------

To use certain permissions when your app goes live, your app must also be approved for additional permissions. These dependent permissions must have been approved either during the same app review submission or a in previous submission.

 Permission | Dependent on || `ads_management` | `pages_read_engagement`
`pages_show_list` |
| `instagram_basic` | `pages_read_engagement`
`pages_show_list` |
| `leads_retrieval` | `pages_manage_ads`
`pages_read_engagement`
`pages_show_list` |
| `pages_manage_ads` | `pages_show_list` |
| `pages_manage_engagement` | `pages_read_user_content`
`pages_show_list` |
| `pages_manage_metadata` | `pages_show_list` |
| `pages_manage_posts` | `pages_read_engagement`
`pages_show_list` |
| `pages_messaging` | `pages_manage_metadata`
`pages_show_list` |
| `pages_read_engagement` | `pages_show_list` |
| `pages_read_user_content` | `pages_show_list` |
Learn More
----------

* Access Tokens
* Maintaining Data Access
* Secure Requests
* Terms and Policies