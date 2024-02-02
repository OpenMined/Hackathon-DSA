Handle Errors - Graph API











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
On This PageHandling ErrorsError ResponsesError CodesAuthentication Error SubcodesRate Limiting Error CodesHandling Errors
===============


Requests made to our APIs can result in several different error responses. The following document describes the recovery tactics and provides a list of error values with a map to the most common recovery tactic to use.


Error Responses
---------------


The following represents a common error response resulting from a failed API request:



```
{
 "error": {
 "message": "Message describing the error", 
 "type": "OAuthException", 
 "code": 190,
 "error\_subcode": 460,
 "error\_user\_title": "A title",
 "error\_user\_msg": "A message",
 "fbtrace\_id": "EJplcsCHuLu"
 }
}
```
* `message`: A human-readable description of the error.
* `code`: An error code. Common values are listed below, along with common recovery tactics.
* `error_subcode`: Additional information about the error. Common values are listed below.
* `error_user_msg`: The message to display to the user. The language of the message is based on the locale of the API request.
* `error_user_title`: The title of the dialog, if shown. The language of the message is based on the locale of the API request.
* `fbtrace_id`: Internal support identifier. When reporting a bug related to a Graph API call, include the `fbtrace_id` to help us find log data for debugging. However, this ID will expire shortly. To help the support team reproduce your issue, please attach a saved graph explorer session.


### Error Codes




| 
Code or Type
 | 
Name
 | 
What To Do
 |
| --- | --- | --- |
| OAuthException |  | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. Get a new access token.
If a subcode is present, see the subcode. |
| 102 | API Session | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. Get a new access token.
If a subcode is present, see the subcode. |
| 1 | API Unknown | Possibly a temporary issue due to downtime. Wait and retry the operation. If it occurs again, check that you are requesting an existing API. |
| 2 | API Service | Temporary issue due to downtime. Wait and retry the operation. |
| 3 | API Method | Capability or permissions issue. Make sure your app has the necessary capability or permissions to make this call. |
| 4 | API Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 17 | API User Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 10 | API Permission Denied | Permission is either not granted or has been removed. Handle the missing permissions. |
| 190 | Access token has expired | Get a new access token. |
| 200-299 | API Permission (Multiple values depending on permission) | Permission is either not granted or has been removed. Handle the missing permissions. |
| 341 | Application limit reached | Temporary issue due to downtime or throttling. Wait and retry the operation, or examine your API request volume. |
| 368 | Temporarily blocked for policies violations | Wait and retry the operation. |
| 506 | Duplicate Post | Duplicate posts cannot be published consecutively. Change the content of the post and try again. |
| 1609005 | Error Posting Link | There was a problem scraping data from the provided link. Check the URL and try again. |

### Authentication Error Subcodes




| 
Code
 | 
Name
 | 
What To Do
 |
| --- | --- | --- |
| 458 | App Not Installed | The User has not logged into your app. Reauthenticate the User. |
| 459 | User Checkpointed | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 460 | Password Changed | On iOS 6 and above, if the person logged in using the OS-integrated flow, direct them to Facebook OS settings on the device to update their password. Otherwise, they must log in to the app again. |
| 463 | Expired | Login status or access token has expired, been revoked, or is otherwise invalid. Handle expired access tokens. |
| 464 | Unconfirmed User | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 467 | Invalid Access Token | Access token has expired, been revoked, or is otherwise invalid. Handle expired access tokens. |
| 492 | Invalid Session | User associated with the Page access token does not have an appropriate role on the Page. |

### Rate Limiting Error Codes


Visit the Graph API Rate Limits guide for more information about Rate Limiting Error Codes.


On This PageHandling ErrorsError ResponsesError CodesAuthentication Error SubcodesRate Limiting Error CodesFollow Us* 
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