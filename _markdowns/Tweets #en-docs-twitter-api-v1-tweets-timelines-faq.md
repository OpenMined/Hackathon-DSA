



FAQ | Docs | Twitter Developer Platform 





































































































FAQ








**Please note:**  




We launched a new version of the standard v1.1 statuses/user\_timeline and statuses/mentions\_timeline endpoints as part of Twitter API v2: Early Access. If you are currently using either of these endpoints, you can use our migration materials to start working with the newer endpoint.









Frequently Asked Questions
--------------------------


This FAQ addresses questions about the new request limit (100,000 / 24-hours) enforced on the /statuses/mentions\_timeline and /statuses/user\_timeline endpoints.


**Why are you making this change?**


As noted in the blog post, we’re making these changes so we can appropriately review how developers are using these endpoints, and so that access to our APIs is fair and consistent for developers who have built solutions to serve other businesses. Adjusting these rate limits also contributes to our goal of helping people feel safe and protecting their privacy while maintaining open access to our developer platform.


**What API endpoints are impacted by the announcement?**


We are announcing that we are limiting access to two of the most commonly used Twitter standard API endpoints – statuses/user\_timeline and statuses/mentions\_timeline. This change will ensure that we appropriately review how existing apps are using these endpoints, while also making sure that all companies using our APIs to build products for business purposes are doing so fairly and consistently.


**What are the new rate limits?**


On June 19, 2019, we will begin limiting access to the /statuses/mentions\_timeline and /statuses/user\_timeline endpoints to 100,000 requests per day as a default. This is a total request limit that applies across both user-auth and app-auth requests. These limits will be on a per-application and per-endpoint basis, meaning that a single developer app can make up to 100,000 calls to each of the two endpoints during any single 24-hour period. The existing default user-auth and app-auth rate limits will not change.


**Are we changing the existing user-auth and app-auth rate limits?**


No, existing default user-auth and app-auth rate limits are not currently changing. To be clear, as of June 19, rate limits for statuses/mentions\_timeline and statuses/user\_timeline will be as follows:


* **/statuses/mentions\_timeline:**
	+ 75 requests/15-min window (user-auth)
	+ 100,000 requests/24-hour window (application level)
* **/statuses/user\_timeline:**
	+ 900 requests/15-min window (user-auth)
	+ 1500 requests/15-min window (app-auth)
	+ 100,000 requests/24-hour window (application level)


**Is the 24-hour period based on clock time (e.g., 0:00 UTC) or a rolling clock?**


The 24-hour period is based on a rolling clock, beginning at the time of the first request and monitored for the next 24 hours.


**How do I determine if I am impacted by this change?**


We have proactively contacted developers who will be impacted via their registered developer email addresses. If you did not receive an email, you’ll need to check if your Twitter developer app is making more than 100,000 requests to either /statuses/mentions\_timeline or /statuses/user\_timeline endpoints in a 24-hour period. Please see question 8 (option 2) below for details on what to do if you believe your app will be impacted.


**How do I check whether I am hitting the endpoint(s) near the request limit?**


We do not have an endpoint that provides this information, so you will have to review your logs to track your usage. If you would like to check your usage from the current rate limit window, you can use the application/rate\_limit\_status endpoint.


**What can I do if I am impacted by this change?**


Please review the two options outlined below and proceed with the one that best describes your application:


**I. My application serves other businesses:**


1. Please complete the enterprise API application via this form with detailed information about your application that makes use of these endpoints.
2. A Twitter representative will be in touch to discuss available options for continued access. Part of this process will include a review of your application, your use case, and a consultation of the best API solutions available to serve your needs.


**II. My application does not serve other businesses:**


1. Make sure that you are logged into your Twitter Developer account.
2. Follow this link to the API Policy Support Page, where you might see the option: "I would like to apply for elevated user & mentions timeline limits."
	* *Important note:* If you do not see this option, please double check the Twitter account you're currently logged in with. If you still do not see this option, your application does not qualify for a review at this time because your usage is well below impacted thresholds. Rest assured, if you start making requests at a volume near the rate limit, the proper form option will become available. Based on this, we request that you don’t post to the forums if you don’t see this option unless you actually hit the rate limit.
3. Complete the form with as much detail as you can about your current use of one (or both) of the mentions and user timeline endpoints. Our team may need to reach out for further clarification if your submission is incomplete or unclear, which may delay a decision about your application. Please provide as much detail as possible.
4. We will review your submission and notify you of our decision when our review is complete.


**Will developers ever be required to migrate off of the user and mentions timeline endpoints?**


We are taking a phased approach at changes to our platform, so that we can collect feedback from developers and minimize impact. We want to make sure we understand how and why developers are using them to help inform any changes we might make in the future.


**If an app makes a request to mentions or user timeline and it fails (e.g., 401 Unauthorized), will it count against the 100,000 limit?**


No. If the request fails, then it will not count against the 100,000 limit.


**How will the API behave if my app exceeds the 100,000 request limit in a 24-hour period?**


The API will return a 429 error response if your app exceeds the 100,000 request limit in a 24-hour period:


HTTP/1.1 429 Too Many Requests


{"errors":[{"message":"Rate limit exceeded","code":88}]}


The 429 error response will continue to be returned until the current 24-hour period ends. 



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















