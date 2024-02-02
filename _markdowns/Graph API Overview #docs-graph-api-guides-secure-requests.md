Secure Requests - Graph API










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
On This PageSecure Graph API CallsMeta CrawlerLogin SecurityServer Allow ListSocial Plugin Confirmation StepsEncryptionVerify Graph API Calls with appsecret\_proofGenerate the ProofAdd the ProofRequire the ProofSecure Graph API Calls
======================


Almost every Graph API call requires an access token. Malicious developers can steal access tokens and use them to send spam from your app. Meta has automated systems to detect this, but you can help us secure your app. This document covers some of the ways you can improve security in your app.


Meta Crawler
------------


A number of platform services such as Social Plugins and Open Graph require our systems to be able to reach your web pages. We recognize that there are situations where you might not want these pages on the public web, during testing or for other security reasons.


We've provided information on IP allow lists and User Agent strings for Meta's crawlers in our Meta Crawler guide.


Login Security
--------------


There are a large number of settings you can change to improve the security of your app. Please see our Login Security documentation for a checklist of things you can do.


It's also worth looking at our access token documentation which covers various architectures and the security trade-offs that you should consider.


Server Allow List
-----------------


We also enable you to restrict some of your API calls to come from a list of servers that you have allowed to make calls. Learn more in our login security documentation.


Social Plugin Confirmation Steps
--------------------------------


In order to protect users from unintentionally liking content around the web, our systems will occasionally require them to confirm that they intended to interact with one of our Social Plugins via a "confirm" dialog. This is expected behavior and once the system has verified your site as a good actor, the step will be removed automatically.


Encryption
----------


When connecting to our servers your client must use TLS and be able to verify a certificate signed using `sha256WithRSAEncryption`.


Graph API supports TLS 1.2 and 1.3 and non-static RSA cipher suites. We are currently deprecating support for older TLS versions and static RSA cipher suites. Version 16.0 no longer supports TLS versions older than 1.1 or static RSA cipher suites. This change will apply to all API versions on May 3, 2023.


Verify Graph API Calls with `appsecret_proof`
---------------------------------------------


Access tokens are portable. It's possible to take an access token generated on a client by Meta's SDK, send it to a server and then make calls from that server on behalf of the client. An access token can also be stolen by malicious software on a person's computer or a man in the middle attack. Then that access token can be used from an entirely different system that's not the client and not your server, generating spam or stealing data.


Calls from a server can be better secured by adding a parameter called `appsecret_proof`. The app secret proof is a sha256 hash of your access token, using your app secret as the key. The app secret can be found in your app dashboard in **Settings > Basic**.


If you're using the official PHP SDK, the `appsecret_proof` parameter is automatically added.


### Generate the Proof


The following code example is what the call looks like in PHP:



```
$appsecret\_proof= hash\_hmac('sha256', $access\_token, $app\_secret); 
```
### Add the Proof


You add the result as an `appsecret_proof` parameter to each call you make:



```
curl \
 -F 'access\_token=<access\_token>' \
 -F 'appsecret\_proof=<app secret proof>' \
 -F 'batch=[{"method":"GET", "relative\_url":"me"},{"method":"GET", "relative\_url":"me/friends?limit=50"}]' \
 https://graph.facebook.com
```
### Require the Proof


In the **Settings > Advanced** section of your app dashboard in the **Security** section, you enable **Require App Secret**. When this is enabled, we will only allow API calls that include the `appsecret_proof`.


On This PageSecure Graph API CallsMeta CrawlerLogin SecurityServer Allow ListSocial Plugin Confirmation StepsEncryptionVerify Graph API Calls with appsecret\_proofGenerate the ProofAdd the ProofRequire the ProofFollow Us* 
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