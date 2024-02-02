
POST media/upload (APPEND) | Docs | Twitter Developer Platform 

POST media/upload (APPEND)

post-media-upload-append
POST media/upload (APPEND)
==========================

Overview¶
---------

The `APPEND` command is used to upload a chunk
(consecutive byte range) of the media file. For example, a 3 MB file
could be split into 3 chunks of size 1 MB, and uploaded using 3
`APPEND` command requests. After the entire file is uploaded,
the next step is to call the FINALIZE
command.

There are a number of advantages of uploading a media file in small
chunks:

* Improved reliability and success rates under low bandwidth network
conditions
* Uploads can be paused and resumed
* File chunks can be retried individually
* Ability to tune chunk sizes to match changing network conditions e.g
on cellular clients

Request¶
--------

Requests should be `multipart/form-data` POST format.

**Note:** The domain for this endpoint is
**upload.twitter.com**

Response¶
---------

A successful response returns HTTP 2xx.

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
| command | required | Must be set to `APPEND` (case sensitive). |  |  |
| media\_id | required | The `media_id` returned from the `INIT`
command. |  |  |
| media | required | The raw binary file content being uploaded. It must be <= 5 MB,
and cannot be used with `media_data`. |  |  |
| media\_data | required | The base64-encoded chunk of media file. It must be <= 5 MB and
cannot be used with `media`. Use raw binary (media parameter)
when possible. |  |  |
| segment\_index | required | An ordered index of file chunk. It must be between 0-999 inclusive.
The first segment has index 0, second segment has index 1, and so
on. |  |  |

Example Request¶
----------------

`POST https://upload.twitter.com/1.1/media/upload.json?command=APPEND&media_id=123&segment_index=2&media_data=123`

Example Result¶
---------------

```
// Successful response returns HTTP 2XX code without any content body.
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