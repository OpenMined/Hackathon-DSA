
POST media/subtitles/create | Docs | Twitter Developer Platform 

POST media/subtitles/create

post-media-subtitles-create
POST media/subtitles/create
===========================

Overview
========

Use this endpoint to associate uploaded subtitles to an uploaded
video. You can associate subtitles to video before or after
Tweeting.

Request flow for associating subtitle to video before the video is
Tweeted : 1. Upload video using the chunked upload endpoint and get the
video media\_id. 2. Upload subtitle using the chunked upload endpoint
with media category set to “Subtitles” and get the subtitle media\_id. 3.
Call this endpoint to associate the subtitle to the video. 4. Create
Tweet with the video media\_id.

Request flow for associating subtitle to video after the video is
Tweeted : 1. Upload video using the chunked upload endpoint and get the
video media\_id. 2. Create Tweet with the video media\_id. 3. Upload
subtitle using the chunked upload endpoint with media category set to
SUBTITLES and get the subtitle media\_id. 4. Call this endpoint to
associate the subtitle to the video.

Request
=======

Requests should be HTTP POST with a JSON content body, and
Content-Type `application/json; charset=UTF-8`

**Note:** The domain for this endpoint is
**upload.twitter.com**

Response
========

This endpoint returns the following HTTP responses:

|  |  |  |
| --- | --- | --- |
| Status | Text | Description |
| 200 | OK | The request to create the subtitle was successful. |
| 400 | Bad Request | Generally, this response occurs due to the presence of invalid JSON
in the request, or where the request failed to send any JSON payload. In
this case this error could indicate an invalid subtitle file. |
| 403 | Unauthorized | HTTP authentication failed due to invalid credentials. Check your
OAuth keys and tokens. |
| 404 | Not Found | The resource was not found at the URL to which the request was sent,
likely because an incorrect media\_id |
| 500 | Internal Server Error | There was an error on Twitter's side. Retry your request using an
exponential backoff pattern. |
| 503 | Service Unavailable | There was an error on Twitter's side. Retry your request using an
exponential backoff pattern. |

Resource URL
============

`https://upload.twitter.com/1.1/media/subtitles/create.json`

Resource Information
====================

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Example Request
===============

```
POST https://upload.twitter.com/1.1/media/subtitles/create.json
    {
      "media_id":"692797692624265216",
      "media_category":"TweetVideo",
      "subtitle_info": {
        "subtitles": [
          "media_id":"105195515189863968",
          "language_code":"EN", //The language code should be a BCP47 code (e.g. 'en", "sp"),
          "display_name":"English"
        ]
      }
    }
```
Example Result
==============

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