Ads Management Standard Access - Graph API - Documentation - Meta for Developers

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
Ads Management Standard Access
==============================

*Requires App Review.*  The **Ads Management Standard Access** feature allows your app to access the Marketing API. The allowed usage for this feature is to enable an unlimited number of ad accounts and lower rate limiting. At a minimum, ads\_read or ads\_management permission is required to use Ads Management Standard Access. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified). Allowed Usage
-------------

* Enable an unlimited number of ad accounts and lower rate limiting.
* To read ads reports for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_read** permission.
* To read and manage ads for ad accounts you own or have been granted access to by the ad account owner, request **Ads Management Standard Access**, along with the **ads\_management** permission.
* To pull ads reports from a set of clients, and to read and manage ads from another set of clients, request **Ads Management Standard Access**, along with both **ads\_read** and **ads\_management** permissions.
Common Endpoints
----------------

/adaccount  
/adaccount/adcreatives/  
/adaccount/adsAdditional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. Learn More
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. Learn More Here