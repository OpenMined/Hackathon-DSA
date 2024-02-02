
PowerTrack API | Docs | Twitter Developer Platform 

PowerTrack API

powertrack-stream
PowerTrack API
==============

Jump to on this pageMethods
Authentication
GET
/track/:stream

Methods¶
--------

| Method | Description |
| --- | --- |
| GET /track/:stream | Connect to the data stream |

Authentication¶
---------------

All requests to the PowerTrack API must use HTTP Basic
Authentication, constructed from a valid email address and password
combination used to log into your account at console.gnip.com.
Credentials must be passed as the Authorization header for each request.
Make sure your client is adding the "Authentication: Basic" HTTP header
(with encoded credentials over HTTPS) to all API requests.

GET
/track/:stream¶
-------------------

Establishes a persistent connection to the PowerTrack data stream,
through which the social data will be delivered.

**IMPORTANT:** After you establish the connection see here for
details on consuming streaming data.

|  |  |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-AliveThis should be specified in the header of the
request. |
| **URL** | Found on the stream's API Help page of your console dashboard, and
resembles the following structure:
```
https://gnip-stream.twitter.com/stream/powertrack/accounts/{gnip_account_name}/publishers/twitter/{stream_label}.json
```
 |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send
an Accept-Encoding header in the connection request. The header should
look like the following:Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the
response. |
| **Rate Limit** | 60 requests per minute. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a
value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet objects will include Tweet edit metadata describing the
Tweet's edit history. See the "Edit
Tweets" fundamentals page for more details. |

#### Responses

The following responses may be returned by the API for these
requests. Most error codes are returned with a string with additional
details in the body. For non-200 responses, clients should attempt to
reconnect.

| Status | Text | Description |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be
sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to
console.gnip.com with your credentials to ensure you are using them
correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include
the headers to accept gzip encoding from the stream, but can occur in
other circumstances as well. Will contain a JSON message
similar to "This connection requires compression. To enable compression,
send an 'Accept-Encoding: gzip' header in your request and be ready to
uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff
pattern. If no notice about this issue has been posted on the Twitter API Status Page, contact
support or emergency if unable to connect after 10 minutes. |

**Example curl Request**

The following example request is accomplished using cURL on the
command line. However, note that these requests may also be sent with
the programming language of your choice.

```
curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/powertrack/accounts/:account_name/publishers/twitter/:stream_label.json"
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