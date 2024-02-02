Resumable Upload API - Graph API










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
On This PageResumable Upload APIUpload StepsStep 1: Create a SessionStep 2: Initiate UploadInterruptionsRequest SyntaxResponseSample RequestSample ResponseResumable Upload API
====================


The Resumable Upload API allows you to upload large files to the Graph API and resume interrupted upload sessions without having to start over. Once uploaded, you can use an uploaded file's handle with other Graph API endpoints that support them.


Note that the Resumable Upload API is not the only way to upload files. Many nodes have an edge that supports uploading, but most do not have a way to handle large files or a way to resume an interrupted upload session.


References for endpoints that support uploaded file handles will indicate if the endpoints support handles returned by the Resumable Upload API.


Upload Steps
------------


Uploading a file is a two step process:


1. Use the Application Uploads endpoint to describe your file and create an upload session.
2. Use the returned upload session ID to initiate the upload process.


If successful, a file handle will be returned which you can then use with other endpoints that support file handles returned by the Resumable Upload API.


### Step 1: Create a Session


Send a `POST` request that describes your file to the Application Uploads endpoint (`{app-id}/uploads`) . Upon success an upload session ID will be returned that you can use in the next step to initiate the upload.


#### Request Syntax



```
POST https://graph.facebook.com/{api-version}/{app-id}/uploads
 &file\_length={file-length}
 &file\_type={file-type}
 &access\_token={access-token}
```
Parameters Placeholders:


* `{api-version}` — The Graph API version.
* `{app-id}` — The application ID. The uploaded file that will be associated with this app. The app user must have an administrator or developer role on this app.
* `file-length` — The file's size, in bytes.
* `file-type` — The file's MIME type. Valid values are: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, and `video/mp4`
* `{access-token}` — The app user's User Access Token.


Refer to the Application Uploads endpoint reference for a complete list of available query parameters and supported file types.


#### Response



```
{
 "id": "{id}"
}
```
Response property values:


* `{id}` — Upload session ID.


#### Sample Request



```
curl -X POST \
 "https://graph.facebook.com/v18.0/584544743160774/uploads?file\_length=109981&file\_type=image/png&access\_token=EAAIT..."
```
#### Sample Response



```
{
 "id": "upload:MTphd..."
}
```
### Step 2: Initiate Upload


Initiate the upload session by sending a `POST` request to Graph API host address and append your upload session `{id}` along with the required headers indicated below. Upon success, a file handle, `{h}`, is returned that you can then use with any Graph API endpoints that support file handles returned by the Resumable Upload API.


If the upload session is taking longer than expected or has been interrupted, follow the steps described in the Interruptions section.


#### Request Syntax



```
POST https://graph.facebook.com/{api-version}/{upload-session-id}
 --header 'Authorization: OAuth {access-token}' 
 --header 'file\_offset: 0'
 --data-binary @{file-name}
```
**Placeholder Values**


* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in step 1.
* `{access-token}` — App user's User Access Token. The app user must have a role on the app that was targeted in step 1.
* `{file-name}` — Name of the file to upload.


You must include the access token in the header or your request will fail.


#### Response



```
{
 "h": "{h}"
}
```
Response property values:


* `{h}` — The uploaded file's file handle


#### Sample Request



```
curl -X POST \
 "https://graph.facebook.com/v18.0/upload:MTphd..." \
 --header "Authorization: OAuth EAAIT..." \
 --header "file\_offset: 0" \
 --data-binary @cats\_are\_jerks.png
```
#### Sample Response



```
{
 "h": "2:c2FtcGxl..."
}
```
Interruptions
-------------


If you have initiated an upload session but it is taking longer than expected or has been interrupted, send a `GET` request to Graph API host address and append your upload session ID. The API returns a `file_offset` value that you can use to resume the upload process from the point of interruption.


### Request Syntax



```
GET https://graph.facebook.com/{api-version}/{upload-session-id}
 ?access\_token={access-token}
```
Placeholder values:


* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in Step 1: Create a Session.
* `{access-token}` — App user's User Access Token.


### Response



```
{
 "id": "{id}",
 "file\_offset": {file-offset}
}
```
Response property values:


* `{id}` — The upload session ID that was queried.
* `{file-offset}` — An integer that indicates the number of bytes that have been successfully uploaded.


Capture the `file_offset` value and repeat Step 2: Initiate Upload, assigning the value to the corresponding `file_offset` header. This will resume the upload process from the point of interruption.


### Sample Request



```
curl -X GET \
 "https://graph.facebook.com/v18.0/upload:MTphd...&access\_token=EAAIT..." \
```
### Sample Response



```
{
 "id": "upload:MTphd",
 "file\_offset": 5238
}
```
On This PageResumable Upload APIUpload StepsStep 1: Create a SessionStep 2: Initiate UploadInterruptionsRequest SyntaxResponseSample RequestSample ResponseFollow Us* 
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