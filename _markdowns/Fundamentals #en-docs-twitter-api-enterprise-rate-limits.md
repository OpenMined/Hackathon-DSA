



Rate limits: Enterprise | Docs | Twitter Developer Platform 





































































































Rate limits: Enterprise



Overview
--------


Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 


The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 






### 
Enterprise rate limits per window




| Product | Endpoint | Rate limit |
| --- | --- | --- |
| PowerTrack API | Streaming endpoint | 60 requests per minute |
| Rules endpoint | 60 requests per minute aggregated across all /rules endpoints |
| Replay endpoint | 5 requests per 5 minutes |
| Historical PowerTrack API |  | 60 Jobs can be created per (UTC) day. |
|  | 30 Jobs can be created per hour. |
|  | 2 Jobs can be estimating concurrently. |
|  | 2 Jobs can be running concurrently. |
| Decahose API |  | 10 requests per minute |
| Streaming likes API |  | 10 requests per minute |
| Firehose API |  | 10 requests per minute |
| Account Activity API | POST account\_activity/webhooks | 15 requests per 15 minutes |
| GET account\_activity/webhooks | 15 requests per 15 minutes |
| PUT account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| POST account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/subscriptions/count | 15 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all | 500 requests per 15 minutes |
| GET account\_activity/webhooks/:webhook\_id/subscriptions/all/list | 50 requests per 15 minutes |
| DELETE account\_activity/webhooks/:webhook\_id | 15 requests per 15 minutes |
| DELETE /account\_activity/webhooks/:webhook\_id/subscriptions/:user\_id/all.json | 500 requests per 15 minutes |
| Replay | 5 requests per 15 minutes |
| Search API |  | Per minute rate limit will vary by contract |
|  | 20 requests per second aggregated across either the 30 day data and counts endpoints, or across the full-archive data and counts endpoints |
| Engagement API |  | Per minute rate limit will vary by contract |
| Compliance Firehose API |  | 10 requests per minute |
| Usage API |  | 2 requests per minute |



















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















