



POST media/upload | Docs | Twitter Developer Platform 





































































































POST media/upload



post-media-upload

POST media/upload
=================




Overview¶
---------


Use this endpoint to upload images to Twitter.


This endpoint returns a `media_id` by default and can
optionally return a `media_key` when a
`media_category` is specified. These values are used by
Twitter endpoints that accept images.


For example, a `media_id` value can be used to create a
Tweet with an attached photo using the POST
statuses/update endpoint.


All Ads API endpoints require a
`media_key`. For example, a `media_key` value can
be used to create a Draft Tweet with a photo using the POST
accounts/:account\_id/draft\_tweets endpoint.


Usage¶
------


This is a simple image upload endpoint with a limited set of
features. The preferred alternative is the chunked upload endpoint which
supports both images and videos, provides better reliability, allows
resumption of file uploads, and other important features. In the future,
new features will only be supported for the chunked upload endpoint.


* See the Uploading
media guide for constraints and requirements on media files.
* See the Uploading Media
tutorial for step-by-step instructions on uploading an image.
* Use the media
metadata endpoint to provide image alt text information.
* Ensure the POST is a `multipart/form-data` request.
Either upload the raw binary (`media` parameter) of the file,
or its base64-encoded contents (`media_data` parameter). Use
raw binary when possible, because base64 encoding results in larger file
sizes
* The response provides a media identifier in the
`media_id` (64-bit integer) and `media_id_string`
(string) fields. Use the `media_id_string` provided in the
API response from JavaScript and other languages that cannot accurately
represent a long integer.
* The returned `media_id` and `media_key` are
only valid for `expires_after_secs` seconds. Any attempt to
use either after this time period in other endpoints will result in an
HTTP 4xx Bad Request.
* The `additional_owners` field enables media to be
uploaded as user A and then used to create Tweets as user B.
* Please note that to upload videos or GIFs (`tweet_video`,
`amplify_video`, and `tweet_gif`), you need to use
the chunked
upload end-point.


Request¶
--------


Requests should be either `multipart/form-data` or
`application/x-www-form-urlencoded` POST formats.


**Note:** The domain for this endpoint is
**upload.twitter.com**


Resource URL¶
-------------


`https://upload.twitter.com/1.1/media/upload.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| media | required | The raw binary file content being uploaded. Cannot be used with
`media_data`. |  |  |
| media\_category | optional | The category that represents how the media will be used. This field
is required when using the media with the Ads APIPossible values:
`amplify_video`, `tweet_gif`,
`tweet_image`, and `tweet_video` |  |  |
| media\_data | required | The base64-encoded file content being uploaded. Cannot be used with
`media`. |  |  |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners
allowed to use the returned `media_id` in Tweets or Cards. Up
to 100 additional owners may be specified. |  |  |


Example Request¶
----------------


`POST https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image`


Example Response¶
-----------------



```
{
  "media_id": 710511363345354753,
  "media_id_string": "710511363345354753",
  "media_key": "3_710511363345354753",
  "size": 11065,
  "expires_after_secs": 86400,
  "image": {
    "image_type": "image/jpeg",
    "w": 800,
    "h": 320
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















