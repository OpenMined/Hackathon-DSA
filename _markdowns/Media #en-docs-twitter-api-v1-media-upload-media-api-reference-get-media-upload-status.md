



GET media/upload (STATUS) | Docs | Twitter Developer Platform 





































































































GET media/upload (STATUS)



get-media-upload-status

GET media/upload (STATUS)
=========================




Overview¶
---------


The `STATUS` command is used to periodically poll for
updates of media processing operation. After the `STATUS`
command response returns `succeeded`, you can move on to the
next step which is usually create Tweet with media\_id.


Request¶
--------


It should be a HTTP GET request with url params.


**Note:** The domain for this endpoint is
**upload.twitter.com**


Response¶
---------


The response body contains `processing_info` field which
provides information about current state of media processing operation.
It contains a `state` field which has transition flow:
“pending” -> “in\_progress” -> [“failed” | “succeeded”]. You can
not use the media\_id to create Tweet or other entities before the state
field is set to “succeeded”.


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
| command | required | Must be set to `STATUS` (case sensitive). |  |  |
| media\_id | required | The `media_id` returned from the `INIT`
command. |  |  |


Example request¶
----------------


`GET https://upload.twitter.com/1.1/media/upload.json?command=STATUS&media_id=710511363345354753`


Example Result¶
---------------



```
// Example of an in_progress response:

{
  "media_id":710511363345354753,
  "media_id_string":"710511363345354753",
  "expires_after_secs":3595,
  "processing_info":{
    "state":"in_progress", // state transition flow is pending -> in_progress -> [failed|succeeded]
    "check_after_secs":10, // check for the update after 10 seconds
    "progress_percent":8 // Optional [0-100] int value. Please don't use it as a replacement of "state" field.
  }
}

// Example of a failed response:

{
  "media_id":710511363345354753,
  "media_id_string":"710511363345354753",
  "processing_info":{
    "state":"failed",
    "progress_percent":12,
    "error":{
      "code":1,
      "name":"InvalidMedia",
      "message":"Unsupported video format"
    }
  }
}

// Example of a succeeded response:

{
  "media_id":710511363345354753,
  "media_id_string":"710511363345354753",
  "expires_after_secs":3593,
  "video":{
    "video_type":"video/mp4"
  },
  "processing_info":{
    "state":"succeeded",
    "progress_percent":100,
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















