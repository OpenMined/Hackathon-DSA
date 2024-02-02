Upgrade - Graph API










DocsToolsSupportLog InGraph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
	+ Upgrade
	+ Versions
	+ Out-Of-Cycle Changes
* Features Reference
* Permissions Reference
* Reference
On This PageUpgrade to the Latest Graph API VersionLearn How a Change Affects Your AppRead the ResultsLimitationsImplement a New VersionLearn MoreUpgrade to the Latest Graph API Version
=======================================


This guide describes how to prepare your app to test different versions of the Graph API and to upgrade to the latest version.


The API Upgrade Tool shows the API calls from your app that may be affected by changes in newer versions of the API. You will be able to quickly see which changes you need to make to upgrade from your current version to a newer version.


Learn How a Change Affects Your App
-----------------------------------


The API Upgrade Tool displays a customized list of changes that impact an app when upgrading to a specified target version. This allows you to view all relevant changes between the source and target versions.


Step 1. In the Upgrade tool, select your app from the dropdown menu or type in the name of the app.


The dropdown menu only lists up to ten apps. To view more apps than those listed, use the search bar in the dropdown menu.


Step 2. Use the dropdown menus to the right to select the version you would like to **Upgrade from** and the version you would like to **Upgrade to**.


### Read the Results


The tool displays the number of changes that need to be made to update your app to the selected version. If your app makes API calls that will not be affected by a newer version no data will be returned.


Methods are color coded by the version affecting the call. Hover over the bar chart to see how many changes are in each version. The dates associated with each version are when the changes will be enforced for all apps.


The table shows the type of change (deprecation, new feature or change), which methods are affected, the number of calls made in the last 7 days, and the percentage of API calls affected by that specific change.


### Limitations


* You must be an admin or developer of the app to view the app in the tool.
* No data will be returned if your app has not made any, or too few, API calls from the **Update from** version.
* Call volumes may appear incorrect. API call logging is sampled and aggregated over the previous week. It is compared with the call volume to estimate how many of your calls could be affected by a given version change.


**Note:** Not all changes may affect each API call. Use your best judgment on whether a particular change needs to be handled by your app. Be sure to test your API calls in the newer version to ensure it works properly.


Implement a New Version
-----------------------


In the App Dashboard **Settings > Advanced**, scroll to the **Upgrade API Version** section.


#### Upgrading Developers and Admins


This upgrades all developers and admins of an app to the next available version. This allows you to test changes with a small subset of real users before releasing the new version to the public.


#### Upgrading All Calls


This upgrades all calls made by an app to the next available version. Upgrading early is useful since it preserves the option of going back to the original version in case of unforeseen bugs or issues.


Learn More
----------


* Graph API Changelog – Learn about the latest version changes.
* Versioning – Learn all about Graph API versioning, requests to different versions, and more.
* Test Apps – Learn how to create test apps to test changes to your app before public release.
* Test Users – Learn how to create test users to test changes to your app before public release.


On This PageUpgrade to the Latest Graph API VersionLearn How a Change Affects Your AppRead the ResultsLimitationsImplement a New VersionLearn MoreFollow Us* 
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