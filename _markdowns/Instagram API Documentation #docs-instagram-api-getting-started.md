Getting Started - Instagram Platform











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
On This PageGetting StartedBefore You Start1. Configure Facebook Login2. Implement Facebook Login3. Get a User Access Token4. Get the User's Pages5. Get the Page's Instagram Business Account6. Get the Instagram Business Account's Media ObjectsNext StepsGetting Started
===============


This document explains how to successfully call the Instagram Graph API with your app and get an Instagram Business or Creator Account's media objects. It assumes you are familiar with the Graph API and Facebook Login, and know how to perform REST API calls. If you do not have an app yet, you can use the Graph API Explorer instead and skip steps 1 and 2.


Before You Start
----------------


You will need access to the following:


* An Instagram Business Account or Instagram Creator Account
* A Facebook Page connected to that account
* A Facebook Developer account that can perform Tasks on that Page
* A registered Facebook App with **Basic** settings configured


1. Configure Facebook Login
---------------------------


Add the Facebook Login product to your app in the App Dashboard.


You can leave all settings on their defaults. If you are implementing Facebook Login manually (which we don't recommend), enter your `redirect_uri` in the **Valid OAuth redirect URIs** field. If you will be using one of our SDKs, you can leave it blank.


2. Implement Facebook Login
---------------------------


Follow our Facebook Login documentation for your platform and implement Facebook Login into your app. Set up your implementation to request these permissions:


* `instagram_basic`
* `pages_show_list`


3. Get a User Access Token
--------------------------


Once you've implemented Facebook Login, make sure you are signed into your Facebook Developer account, then access your app and trigger the Facebook Login modal. Remember, your Facebook Developer account must be able to perform Tasks on the Facebook Page connected to the Instagram account you want to query.


Once you have triggered the modal, click **OK** to grant your app the `instagram_basic` and `pages_show_list` permissions.


The API should return a User access token. Capture the token so your app can use it in the next few queries. If you are using the Graph API Explorer, it will be captured automatically and displayed in the **Access Token** field for reference:


4. Get the User's Pages
-----------------------


Query the `GET /me/accounts` endpoint (this translates to `GET /{user-id}/accounts`, which perform a `GET` on the Facebook User node, based on your access token).



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/me/accounts?access\_token={access-token}"
```
This should return a collection of Facebook Pages that the current Facebook User can perform the `MANAGE`, `CREATE_CONTENT`, `MODERATE`, or `ADVERTISE` tasks on:



```
{
 "data": [
 {
 "access\_token": "EAAJjmJ...",
 "category": "App Page",
 "category\_list": [
 {
 "id": "2301",
 "name": "App Page"
 }
 ],
 "name": "Metricsaurus",
 "id": "134895793791914", // capture the Page ID
 "tasks": [
 "ANALYZE",
 "ADVERTISE",
 "MODERATE",
 "CREATE\_CONTENT",
 "MANAGE"
 ]
 }
 ]
}
```
Capture the ID of the Facebook Page that's connected to the Instagram account that you want to query. Keep in mind that your app users may be able to perform tasks on multiple pages, so you eventually will have to introduce logic that can determine the correct Page ID to capture (or devise a UI where your app users can identify the correct Page for you).


5. Get the Page's Instagram Business Account
--------------------------------------------


Use the Page ID you captured to query the `GET /{page-id}?fields=instagram_business_account` endpoint:



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/134895793791914?fields=instagram\_business\_account&access\_token={access-token}"
```
This should return the IG User — an Instagram Business or Creator Account — that's connected to the Facebook Page.



```
{
 "instagram\_business\_account": {
 "id": "17841405822304914" // Connected IG User ID
 },
 "id": "134895793791914" // Facebook Page ID
}
```
Capture the IG User ID.


6. Get the Instagram Business Account's Media Objects
-----------------------------------------------------


Use the IG User ID you captured to query the `GET /{ig-user-id}/media` endpoint:



```
curl -i -X GET \
 "https://graph.facebook.com/v18.0/17841405822304914/media?access\_token={access-token}"
```
This should return the IDs of all the IG Media objects on the IG User:



```
{
 "data": [
 {
 "id": "17918195224117851"
 },
 {
 "id": "17895695668004550"
 },
 {
 "id": "17899305451014820"
 },
 {
 "id": "17896450804038745"
 },
 {
 "id": "17881042411086627"
 },
 {
 "id": "17869102915168123"
 }
 ],
 "paging": {
 "cursors": {
 "before": "QVFIUkdGRXA2eHNNTUs4T1ZAXNGFxQTAtd3U4QjBLd1B2NXRMM1NkcnhqRFdBcEUzSDVJZATFoLWtXMWZAGU2VrRTk2RHVtTVlDckI2NjN0UERFa2JrUk4yMW13",
 "after": "QVFIUmlwbnFsM3N2cV9lZAFdCa0hDeV9qMVliT0VuMmJyNENxZA180c0t6VjFQVEJaTE9XV085aU92OUFLNFB6Szd2amo5aV9rTlVBcnNlWmEtMzYxcE1HSFR3"
 }
 }
}
```
If you are able to perform this final query successfully, you should be able to perform queries using any of the Instagram Graph API endpoints — just refer to our various guides and references to learn what each endpoint can do and what permissions they require.


Next Steps
----------


* Develop your app further so it can successfully use any other endpoints it needs, and keep track of the permissions each endpoint requires
	+ If you plan to implement Instagram Messaging from Messenger Platform you will need additional permissions
* Complete the App Review process and request approval for all of the permissions your app will need so your app users can grant them while your app is in Live Mode
* Switch your app to Live Mode and market it to potential users


Once your app is in Live Mode, any Facebook User who you've made your app available to can access an Instagram Business or Creator Account's data, as long as they have a Facebook User account that can perform Tasks on the Page connected to that Instagram Business or Creator Account.


On This PageGetting StartedBefore You Start1. Configure Facebook Login2. Implement Facebook Login3. Get a User Access Token4. Get the User's Pages5. Get the Page's Instagram Business Account6. Get the Instagram Business Account's Media ObjectsNext StepsFollow Us* 
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