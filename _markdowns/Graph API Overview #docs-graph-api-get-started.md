Get Started - Graph API











DocsToolsSupportLog InGraph API* Overview
* Get Started
	+ Graph Explorer Guide
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
On This PageGet StartedBefore You StartYour First RequestStep 1: Open the Graph API Explorer toolStep 2. Generate an Access TokenStep 3. Submit the RequestYour Second RequestStep 1. Let's Add a FieldStep 2. Add a PermissionLet's Look at an EdgeGet the Code for your RequestLearn MoreGet Started
===========


This guide explains how to get started with receiving data from the Facebook Social Graph.


Before You Start
----------------


You will need:


* Register as a Meta Developer
* A Meta App – This app will be for testing so there is no need to involve your app code when creating this Meta App.
* The Graph API Explorer tool open in a separate browser window
* A brief understanding of the structure of the Meta's social graph from our Graph API Overview guide

Your First Request
------------------


### Step 1: Open the Graph API Explorer tool


Open the Graph API Explorer in a new browser window. This allows you to execute the examples as you read this tutorial.

The explorer loads with a default query with the `GET` method, the lastest version of the Graph API, the `/me` node and the `id` and `name` fields in the Query String Field, and your Facebook App.


### Step 2. Generate an Access Token


Click the **Generate Access Token** button. A **Log in With Facebook** window will pop up. This popup is your app asking for your permission to get your name and profile picture from Facebook.




|  |  |
| --- | --- |
| This flow is our Facebook Login product that allows a person to log into an app using their Facebook credentials. Facebook Login allows an app to ask a person to access the person's Facebook data, and for the person to accept or decline access. Your name and profile picture are public, to allow people to find you on Facebook, so no additional requirements are needed to run this request.
Click **Continue as...**
A User Access Token is created. This token contains information such as the app making the request, the person using the app to make a request, if the access token is still valid (it expires in about an hour), the expiration time, and the scope of data the app can request. In this request the scope is `public_profile` which includes your name and profile picture. |  |



|  |  |
| --- | --- |
|  | Click the information circle icon next to the acces token to view the token's information. |

### Step 3. Submit the Request


Click the **Submit** button in the upper right corner.


#### What You Should See


In the Response Window, you will see a JSON response with your Facebook User ID and your name.


If you remove `?fields=id,name` from the query string field and click **Submit**, you will see the same result since `name` and `id` are the User node fields returned by default.


Your Second Request
-------------------


### Step 1. Let's Add a Field


Let's make the First Request a little more complex by adding another field, `email`. There are two ways to add fields:


* Click the search dropdown menu in the Node Field Viewer to the left of the response window
* Start typing in the query string field.


Let's add the `email` field and click **Submit**.


#### What You Should See


While the call did not fail, only the `name` and `id` fields were returned along with a debug message. Click the (Show) link to debug the request.


Almost all nodes and fields need a specific permission to access them. The debug message is telling you that you need to give your app permission to access the email address that you have associated with your Facebook account.


### Step 2. Add a Permission




|  |  |
| --- | --- |
| In the right side panel, under **Permissions**, click the **Add a Permission** dropdown menu. Click **User Data Permissions** and select **email**.
Generate A New User Access Token
Because you are changing the scope of the access token, you need to create a new one. Click **Generate Access Token**. Just like your first request, you must give your app permission to access your email in the Facebook Login dialog.
Once the new token has been created, click **Submit**. Now all fields in your request will be returned. |  |

Try getting your Facebook posts.


See the steps.

#### Links in the Response


Notice that `id` values returned in the response window are links. These links can represent nodes, such as User, Page, or Post. If you click on a link, the ID will replace the contents of the query string field. Now you can run requests on that node. Because this node is connected to the parent node, a Post of a User, you may not need to add permissions. You can click on a Post ID now since we will be using it in the next example.


Notice: Some IDs are a combination of the parent ID and a new ID string. For example, a User's Post will have a Post ID that looks something like this: `1028223264288_102224043055529` where `1028223264288` is the User ID.


Let's Look at an Edge
---------------------


The User node does not have many edges that can return data. Access to User objects can only be given by the User who owns the object. In most cases, a User owns an object if they created it.


For example, if you publish a post you can see information about the post such as when it was created, text, photos, and links shared in the post, and the number of reactions the post received. If you comment on your post, you will be able to get that comment, but if another person publishes a comment on your post, you will not be able to see the comment or who published it.


Try getting the number of reactions for one of your posts. You will want to take a look at the


Object Reactions reference.See the steps.

Get the Code for your Request
-----------------------------


The explorer tool lets you test requests and once you have a successful response, you can get the code to insert into your app code. At the bottom of the response window, click **Get Code**. The explorer offers Android, iOS, JavaScript, PHP, and cURL code. The code is pre-selected so you can just copy and paste.


We recommend that you implement the Facebook SDK for your app. This SDK will include Facebook Login which allows your app to ask for permissions and get access tokens.


Learn More
----------


You can use the Graph API Explorer to test any request for Users, Pages, Groups, and more. Visit the reference for each node or edge to determine the permission and access token type required.




|  |  |
| --- | --- |
| * Access Token
* Facebook Login
* Facebook SDKs
 | * Graph API References
* Graph API Explorer Guide
* Login Security
* Permissions Reference
 |

On This PageGet StartedBefore You StartYour First RequestStep 1: Open the Graph API Explorer toolStep 2. Generate an Access TokenStep 3. Submit the RequestYour Second RequestStep 1. Let's Add a FieldStep 2. Add a PermissionLet's Look at an EdgeGet the Code for your RequestLearn MoreFollow Us* 
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