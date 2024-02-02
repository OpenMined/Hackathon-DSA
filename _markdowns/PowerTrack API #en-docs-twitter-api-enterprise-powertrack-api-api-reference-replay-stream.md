



Replay API | Docs | Twitter Developer Platform 





































































































Replay API



replay-stream

Replay API
==========


Jump to on this pageMethods

Authentication

GET /replay


Methods¶
--------




| Method | Description |
| --- | --- |
| GET /replay/:stream\_type | Connect to the replay stream. For realtime PowerTrack, the Stream
Type is 'powertrack'. For Volume Streams, Stream Types include
'sample10' (i.e. decahose), 'firehose', 'mentions', and
'compliance'. |




---


Authentication¶
---------------


All requests to the Replay API must use HTTP Basic Authentication,
constructed from a valid email address and password combination used to
log into your account at console.gnip.com. Credentials must be passed as
the Authorization header for each request.




---


GET /replay¶
------------


Establishes a connection to the Replay data stream. Tweet data will
be delivered for the time period specified, and user profile objects
will reflect the referenced users at the time when the Replay API is
running.


**Please see HERE
for details on consuming streaming data after the connection is
established.**




|  |  |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-AliveThis should be specified in the header of the
request. |
| **URL** | Found on the stream's API Help page of your dashboard, the URL is
built with Stream Type, Account Name and Stream Label tokens. For
realtime PowerTrack, the Stream Type is 'powertrack'. For Volume
Streams, Stream Types include 'sample10' (i.e. decahose), 'firehose',
'mentions', and 'compliance'.   Replay URLs have the following
pattern:
```
https://gnip-stream.gnip.com/replay/{STREAM_TYPE}/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json

```
 For example, the Replay URL for realtime PowerTrack has the
following pattern:
```
https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json

```
 For example, the Replay URL for Decahose has the following
pattern:
```
https://gnip-stream.gnip.com/replay/sample10/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json

```
 |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send
an Accept-Encoding header in the connection request. The header should
look like the following:Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the
response. |
| **Rate Limit** | 5 requests per 5 minutes. |
| **fromDate** | The oldest (starting) UTC timestamp from which the activities will
be provided, must be in 'YYYYMMDDHHMM' format. Timestamp is in minute
granularity and is inclusive (i.e. 12:00 includes the 00 minute). Valid
times must be within the last 5 days, UTC time, and no more recent than
31 minutes before the current point in time. It's recommended that the
fromDate and toDate should be within ~2 hours. |
| **toDate** | The latest (ending) UTC timestamp to which the activities will be
provided, must be in 'YYYYMMDDHHMM' format. Timestamp is in minute
granularity and is exclusive (i.e. 12:30 does not include the 30th
minute of the hour). Valid times must be within the last 5 days, UTC
time, and no more recent than 30 minutes before the current point in
time. It's recommended that the fromDate and toDate should be within ~2
hours. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a
value beyond 30 seconds. |
| **Support for Tweet edits** | Since all Replay requests are for Tweets posted at least 30 minutes
ago, all Tweets returned by Replay will reflect their final edit state.
All Tweet objects will include metadata that describes its edit history.
See the "Edit
Tweets" fundamentals page for more details. |


  

#### Responses


The following responses may be returned by the API for these
requests. Most error codes are returned with a string with additional
details in the body. For non-200 responses, clients should attempt to
reconnect.




| Status | Text | Description |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be
sent through until the end of the requested time period is reached, and
a "Replay Request Completed" message is sent. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to
console.gnip.com with your credentials to ensure you are using them
correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client either fails to properly
include the headers to accept gzip encoding from the stream, or
specifies an unacceptable fromDate or toDate. Will contain a
JSON message indicating the issue -- e.g. "This connection requires
compression. To enable compression, send an 'Accept-Encoding: gzip'
header in your request and be ready to uncompress the stream as it is
read on the client end." or "Invalid date for query parameter 'toDate'.
Can't ask for tweets from within the past 30 minutes." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff
pattern. If no notice about this issue has been posted on the Twitter API Status Page, contact
support. |


  

#### "Request Completed" Message


Once a request has been completed, a "Replay Request Completed"
message will be delivered through the stream prior to disconnecting
inside a "info" JSON message. If your stream is disconnected prior to
receiving this message, the request was not completed, and you will need
to re-run the missing portion of the request.


A premature disconnection may occur especially where your client is
not consuming activities quickly enough. In this scenario, the
connection may send the "Completed" message, but the connection may
close prior to your client receiving it due to the slow rate of
consumption. In this scenario, your client should re-request the
end-portion of the data to ensure completeness, based on the timestamps
of the last Tweets received.


The "info" JSON message has the following structure:



```

{
  "info": {
    "message": "Replay Request Completed",
    "sent": "2016-05-27T22:15:50+00:00",
    "activity_count": 8874
  }
}

```

If any errors are associated with a completed Replay request, the
"info" message will indicate that errors occurred and also list the
minutes that were effected in the "minutes\_failed" field. Here is an
example:



```

{
  "info": {
    "message": "Replay Request Completed with Errors",
    "sent": "2016-05-27T16:00:02+00:00",
    "activity_count": 56333,
    "minutes_failed": [
      "2013-02-20T00:05:00+00:00",
      "2013-02-20T00:06:00+00:00"
    ]
  }
}
```

Users (or their client applications) should monitor for complete
success of the Replay stream, and submit new Replay requests for any
minutes that failed.


#### "Request Failed to Complete"
Message


If a Replay request fails to complete, the "info" message will
indicate the failure and also list the time range was was not processed.
Here is an example:



```

{
  "info": {
    "message": "Replay Request Failed to Complete",
    "sent": "2016-06-27T16:37:13+00:00",
    "unprocessed_range": {
      "fromDate": "2016-06-26T00:00:00+00:00",
      "toDate": "2016-06-26T00:01:00+00:00"
    },
    "activity_count": 1822
  }
}

```

If this message is received another Replay request should be made
based on the "fromDate" and "toDate" included in the "unprocessed\_range"
attribute.


#### Example curl Request


The following example request is accomplished using cURL on the
command line, and requests the first hour of data from June 1, 2016.



```

curl --compressed -v -uexample@customer.com "https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}json?fromDate=201606010000&toDate=201606010100"

```

  



---


### Sample
streams Replay Examples (Stream Types include 'sample10' (i.e.
decahose), 'firehose', 'mentions')¶


Decahose, firehose, mentions note- All partitions from volume streams
are delievered in a single Replay connection.



```

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/sample10/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json?fromDate=201712312330&toDate=201801010130"

```

### Compliance Replay Examples¶


Compliance note- All partitions from Compliance Firehose are
delievered in a single Replay connection.



```

curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/compliance/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json?fromDate=201712312330&toDate=201801010130"

```

### PowerTrack Replay Examples¶


Connection to Replay to complete data during the 2018 New Year's eve
disconnection:



```

    curl --compressed -v -uexample@customer.com 
"https://gnip-stream.gnip.com/replay/powertrack/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json?fromDate=201712312330&toDate=201801010130"

```

Important Note: When using PowerTrack Replay, you must first add or
manage the rules currently on the replay stream. PowerTrack rules are
not automatically added to a Replay stream from a normal PowerTrack
stream. Rules can be managed through the Rules API for a Replay stream.
Please see the PowerTrack
Rules API for specific details on managing rules.


Rules management on the PowerTrack replay:



```

curl -v -X POST -uexample@customer.com 
"https://gnip-api.twitter.com/rules/powertrack-replay/accounts/{ACCOUNT_NAME}/publishers/twitter/{STREAM_LABEL}.json" 
-d '{"rules":[{"value":"rule1","tag":"tag1"},{"value":"rule2"}]}'

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















