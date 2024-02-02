



POST media/upload (INIT) | Docs | Twitter Developer Platform 





































































































POST media/upload (INIT)



post-media-upload-init

POST media/upload (INIT)
========================




Overview¶
---------


The `INIT` command request is used to initiate a file
upload session. It returns a `media_id` which should be used
to execute all subsequent requests. The next step after a successful
return from INIT command is the APPEND
command.


See the Uploading
media guide for constraints and requirements on media files.


Request¶
--------


Requests should be either `multipart/form-data` or
`application/x-www-form-urlencoded` POST formats.


**Note:** The domain for this endpoint is
**upload.twitter.com**


Response¶
---------


The response provides a media identifier in the `media_id`
(64-bit integer) and `media_id_string` (string) fields. Use
the `media_id_string` provided in the API response from
JavaScript and other languages that cannot accurately represent a long
integer.


The entire file must be uploaded before
`expires_after_secs` seconds.


The `additional_owners` field enables media to be uploaded
media as user A and then used to create Tweets as user B.


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




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| command | required | Must be set to `INIT` (case sensitive). |  |  |
| total\_bytes | required | The size of the media being uploaded in bytes. |  |  |
| media\_type | required | The MIME type of the media being uploaded. |  | `video/mp4` |
| media\_category | sometimes | A string enum value which identifies a media usecase. This
identifier is used to enforce usecase specific constraints (e.g. file
size, video duration) and enable advanced features. |  |  |
| additional\_owners | optional | A comma-separated list of user IDs to set as additional owners
allowed to use the returned `media_id` in Tweets or Cards. Up
to 100 additional owners may be specified. |  |  |


Example Request¶
----------------


`POST https://upload.twitter.com/1.1/media/upload.json?command=INIT&total_bytes=10240&media_type=image/jpeg`


Example Result¶
---------------



```
{
  "media_id": 710511363345354753,
  "media_id_string": "710511363345354753",
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















