
LinkedIn API Rate Limiting - LinkedIn | Microsoft Learn

Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.

Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge

Table of contents 

Exit focus mode

Read in English

Save

Table of contents
Read in English

Save
Edit

Print

Twitter
LinkedIn
Facebook
Email

Table of contents

Rate Limiting
=============

* Article
* 09/06/2023
* 4 contributors

Feedback

In this article
---------------

To prevent abuse and ensure service stability, all API requests are rate limited. Rate limits specify the maximum number of API calls that can be made in a 24 hour period. These limits reset at midnight UTC every day.

There are two kinds of limits that affect your application:

* **Application** — The total number of calls that your application can make in a day.
* **Member** — The total number of calls that a single member per application can make in a day.

Note

The term `Member` refers to a LinkedIn user whose token is used to initiate API calls from the developer application. For example, a partner is responsible for managing multiple members. This member-level designation indicates the permissible number of API calls the partner can initiate from their application on behalf of a member token.

Rate limited requests will receive a 429 response. In rare cases, LinkedIn may also return a 429 response as part of infrastructure protection. API service will return to normal automatically.

Your application's daily rate limit varies based on which API endpoint you are using. Standard rate limits are not published in documentation. You can look up the rate limit of any endpoint your app has access to through the Developer Portal. Select your app from the list and navigate to its Analytics tab. This page will only show usage and rate limits for endpoints you have made at least 1 request to today(UTC). If you want to look up a rate limit for an endpoint not listed in your app's Analytics page, make 1 test call to that endpoint and refresh the Analytics page.

---

Feedback
--------

Was this page helpful?

Yes

No

Provide product feedback

Feedback
--------

Submit and view feedback for

This product
This page

View all page feedback

---

Additional resources
--------------------

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024

Additional resources
--------------------

### In this article

California Consumer Privacy Act (CCPA) Opt-Out Icon

Your Privacy Choices

Theme

* Light
* Dark
* High contrast

* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2024