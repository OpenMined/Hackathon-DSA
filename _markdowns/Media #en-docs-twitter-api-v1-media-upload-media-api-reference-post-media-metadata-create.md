



POST media/metadata/create | Docs | Twitter Developer Platform 





































































































POST media/metadata/create



post-media-metadata-create

POST media/metadata/create
==========================




Overview¶
---------


This endpoint can be used to provide additional information about the
uploaded `media_id`. This feature is currently only supported
for images and GIFs.


The request flow should be:


1. Upload media using either the simple
upload endpoint or the (preferred) chunked
upload endpoint.
2. Call this endpoint to attach additional metadata such as image alt
text.
3. Create Tweet with `media_id(s)` attached.


Request¶
--------


Requests should be HTTP POST with a JSON content body, and
Content-Type `application/json; charset=UTF-8` or
`text/plain; charset=UTF-8`.


**Note:** The domain for this endpoint is
**upload.twitter.com**


Response¶
---------


A successful response returns HTTP 2xx.


Resource URL¶
-------------


`https://upload.twitter.com/1.1/media/metadata/create.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Example Request¶
----------------


`POST https://upload.twitter.com/1.1/media/metadata/create.json`



```
{
  "media_id":"692797692624265216",
  // image alt text metadata
  "alt_text": {
    "text":"dancing cat" // Must be <= 1000 chars
  }
}
```


















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















