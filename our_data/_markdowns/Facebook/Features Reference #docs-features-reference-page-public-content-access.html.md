Page Public Content Access - Graph API - Documentation - Meta for Developers

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
Page Public Content Access
==========================

 The **Page Public Content Access** feature allows an app access to the Pages Search API and to read public data for Pages for which you lack the **pages\_read\_engagement** permission and the **pages\_read\_user\_content** permission. Readable data includes business metadata, public comments and posts. The allowed usage for this feature is to analyze and/or display posts and engagement on Pages. Allowed Usage
-------------

* Analyze and/or display posts and engagement on Pages.
Common Endpoints
----------------

/page/feed  
/page-post  
/page-post/commentsAdditional Details
------------------

* This permission or feature requires successful completion of the App Review process before your app can access live data. Learn More
* This permission or feature is only available with business verification. You may also need to sign additional contracts before your app can access data. Learn More Here
* While you are testing your app and before you submit it for review, your app can only access content on a Page for which the following is true: The person who holds the admin role for the Page also holds an admin, developer, or tester role on the app. If you want the app to be able to access public content on other Pages, you must submit this feature for review. Once you set your app to live mode, it will not be able to see any Page public content without this feature.