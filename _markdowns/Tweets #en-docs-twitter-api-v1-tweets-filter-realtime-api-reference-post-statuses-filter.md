



POST statuses/filter | Docs | Twitter Developer Platform 





































































































POST statuses/filter



post-statuses-filter

POST statuses/filter
====================




Returns public Tweets that match one or more filter predicates.
Multiple parameters may be specified which allows most clients to use a
single connection to the Streaming API. Both GET and POST requests are
supported, but GET requests with too many parameters may cause the
request to be rejected for excessive URL length. Use a POST request to
avoid long URLs.


The track, follow, and locations fields should be considered to be
combined with an OR operator. `track=foo&follow=1234`
returns Tweets matching "foo" OR created by user 1234.


The default access level allows up to 400 track keywords, 5,000
follow userids and 25 0.1-360 degree location boxes. If you need access
to more rules and filtering tools, please apply for enterprise access.


Resource URL¶
-------------


`https://stream.twitter.com/1.1/statuses/filter.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Supports Edit Tweets feature? | No |


Parameters¶
-----------




|  |  |  |
| --- | --- | --- |
| Name | Required | Description |
| follow | optional | A comma separated list of user IDs, indicating the users to return
statuses for in the stream. See follow
for more information. |
| track | optional | Keywords to track. Phrases of keywords are specified by a
comma-separated list. See track
for more information. |
| locations | optional | Specifies a set of bounding boxes to track. See locations
for more information. |
| delimited | optional | Specifies whether messages should be length-delimited. See delimited
for more information. |
| stall\_warnings | optional | Specifies whether stall warnings should be delivered. See stall\_warnings
for more information. |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as
part of the Tweet object. |


Example Request¶
----------------


`GET https://stream.twitter.com/1.1/statuses/filter.json?track=twitter`



















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















