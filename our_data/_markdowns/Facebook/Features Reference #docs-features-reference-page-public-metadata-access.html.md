Page Public Metadata Access - Graph API - Documentation - Meta for Developers

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
Page Public Metadata Access
===========================

*Requires App Review.*  The **Page Public Metadata Access** allows your app access to the Pages Search API and to read public data for Pages for which you lack the pages\_read\_engagement permission and the pages\_read\_user\_content permission. The allowed usage for this feature is to analyze engagement with public Pages by viewing Like and follower counts, or aggregate public-facing **About** Page information from multiple, disparate pages. You may also use this permission to request analytics insights to improve your app and for marketing or advertising purposes, through the use of aggregated and de-identified or anonymized information (provided such data cannot be re-identified). Allowed Usage
-------------

* Analyze engagement with public Pages by viewing Like and follower counts.
* Aggregate public-facing "about" Page information from multiple, disparate pages.
Common Endpoints
----------------

/pageAdditional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. Learn More
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. Learn More Here
* If your app also needs to read the Page Feed edge, or Comments on a Page's Posts, request the Page Public Content Access feature instead.
* This feature is superseded by the Page Public Content Access (PPCA) feature. If your App Review submission includes PPCA, or your app has already been approved for PPCA, you cannot request this permission.
* If your app also needs to create, update, or delete data on a Page, request the `pages_read_engagement` permission instead.