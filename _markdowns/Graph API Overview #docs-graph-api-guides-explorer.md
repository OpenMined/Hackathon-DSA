Graph Explorer Guide - Graph API











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
On This PageGraph API Explorer GuideCommon UsesRequirementsComponentsAccess TokenMeta AppUser or PagePermissionsQuery string FieldNode Field ViewerResponse WindowGet CodeCopy Debug InformationSave SessionSample QueryGraph API Explorer Guide
========================




|  |  |
| --- | --- |
| The Graph API Explorer tool allows you to construct and perform Graph API queries and see their responses for any apps on which you have an admin, developer, or tester role. | Open the Graph API Explorer tool |

Common Uses
-----------


* Quickly generate access tokens
* Get code samples for your queries
* Generate debug information to include in support requests
* Test API queries with your production app's settings including permissions, features, and settings for your use cases
* Test API queries with your test or development app using permission and features on test users or test data


Requirements
------------


* A Facebook Developer Account
* An app for which you have a role, such as an admin, developer, or tester role

Components
----------


### Access Token


When you get an access token, it is displayed in the upper right of the tool. This is the token that is included in your Graph API query. You can copy this token and use it in your app to test your code.


Click the information icon to see information about the current token, including the app that it's tied to, and any permissions that have been granted by the User who is using the app (which is you).


You can generate a new access token if the token has expired or if you add new permissions.


### Meta App


The Meta App dropdown menu in the upper right displays all the apps on which you have an admin, developer, or tester role. Use the dropdown to select the app settings that you wish to test.


### User or Page


The User or Page dropdown menu allows you to get and exchange App, User, and Page access tokens for the currently selected app. You can also use it to uninstall your app from your User node, which destroys the current access token.


### Permissions


Whenever you request a User access token, only one permission is given by default, `public_profile`. The Permission dropdown menu allows you to select User Data Permissions, such as `email` and `user_photos`, Events, Groups, and Pages Permissions, such as `manage_pages` and `ads_management`, and Other permissions, such as `instagram_basic` and `publish_video` permissions. This allows the current app User (which is you) to grant the app specific permissions. Only grant permissions that your app actually needs.


If your app is in development, you can grant your app any permission and your queries respect them for data owned by people with a role on your app. If your app is live, however, granting a permission that your app has not been approved for by the App Review process causes your query to fail whenever you submit it.


### Query string Field


When you first enter the tool a default query appears. You can edit the query by typing in a new one, or by searching for and selecting fields in the field viewer after executing the query. You can also use the dropdown menus to switch between operation methods, and target different versions of the Graph API.


If you click the star icon at the end of the query field, the query is saved as a favorite. You can view your favorite queries by clicking the book icon.


### Node Field Viewer


When you submit a `GET` query on a node, the field viewer located in the left side of the window displays the name of the node and the fields returned by the Graph API. You can modify your query by searching for and selecting new fields, clicking the plus icon, and choosing from available fields, or unchecking unnecessary fields. These actions dynamically update your query in the query string field.


### Response Window


The response, located below the query string, shows the results returned from your last submitted query.


### Get Code


If you are happy with your query, click the Get Code button located in the botton center below the response, to generate sample code based on the query. Typically you won't be able to copy and paste the sample code directly in your code base, but it gives you a useful starting point.


### Copy Debug Information


If your query keeps failing and you can't figure out why, and you decide to contact Developer Support, click this button, located at the bottom center, to copy your query and response details to your clipboard. You can submit this information with your support request to help us figure out what's going on.


### Save Session


Click the Save Session button, located at the bottom center, to save the state of your query, with the access token removed. Include the link to this session if you decide to contact Developer Support.


Sample Query
------------


Try executing the default query that appears when you first load the Graph API Explorer. If you haven't already, open the Graph API Explorer in a new window, select the app you want to test from the application dropdown menu, and get a User access token.

The default query appears in the query string field:



```
GET https://developers.facebook.com/v18.0/me?fields=id,name
```
The default query is requesting the `id` and `name` fields on the `/me` node, which is a special node that maps to either the `/User` or `/Page` node identified by the token. Since your are using a User access token, this maps to your User node.


The `id` and `name` fields are publicly available and can be returned if the User has granted your app the `default` or `public_profile` permissions. These permissions are pre-approved for all apps (you can confirm this by clicking the information icon in the **Access Token Field**), so you don't have to grant your app any additional permissions for the query to work. Click **Get Access Token** and confirm that you want to grant your app access to your publicly available User information.


Submit your query, and you should see your app-scoped User ID and name appear in the response window.


On This PageGraph API Explorer GuideCommon UsesRequirementsComponentsAccess TokenMeta AppUser or PagePermissionsQuery string FieldNode Field ViewerResponse WindowGet CodeCopy Debug InformationSave SessionSample QueryFollow Us* 
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