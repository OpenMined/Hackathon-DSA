
GET compliance/firehose | Docs | Twitter Developer Platform 

GET compliance/firehose

compliance-firehose
GET compliance/firehose
=======================

Jump to on this pageMethods
Authentication
GET
/compliance/:stream
Response
Codes
Other Recommendations
& Best Practices

Methods¶
--------

| Method | Description |
| --- | --- |
| GET /compliance/:stream | Connect to the Data Stream |

Authentication¶
---------------

All requests to the Compliance Firehose API must use HTTP Basic
Authentication, constructed from a valid email address and password
combination used to log into your account at console.gnip.com.
Credentials must be passed as the Authorization header for each
request.

GET
/compliance/:stream¶
------------------------

Establishes a persistent connection to the Compliance firehose data
stream, through which the compliance events will be delivered.

|  |  |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive |
| **URL** | Found on the stream's API Help page of your dashboard, and resembles
the following structure: 
```
https://gnip-stream.twitter.com/stream/compliance/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1
```
**Note:** The "partition" parameter is required. You
will need to connect to all 8 partitions, each containing 12.5% of the
total volume, to consume the full stream. |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send
an Accept-Encoding header in the connection request. The header should
look like the following:Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the
response. |
| **Rate Limit** | 10 requests per 60 seconds. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a
value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet edits trigger a "tweet\_edit" Compliance event. See the Compliance
Data Objects documentation for more details. |

**Example Curl Request**

The following example request is accomplished using cURL on the
command line:

```
curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/compliance/accounts/:account_name/publishers/twitter/:stream_label.json?partition=1"
```
*Note:* the above request is only connecting to
`partition=1` of the Compliance firehose - you'll need to
connect to all 8 partitions to consume the entirety of this stream.

Response
Codes¶
---------------

The following responses may be returned by the API for these
requests. Most error codes are returned with a string with additional
details in the body. For non-200 responses, clients should attempt to
reconnect.

| Status | Text | Definition |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be
sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to
console.gnip.com with your credentials to ensure you are using them
correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include
the headers to accept gzip encoding from the stream, but can occur in
other circumstances as well. Will contain a JSON message similar to
"This connection requires compression. To enable compression, send an
'Accept-Encoding: gzip' header in your request and be ready to
uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff
pattern. If no notice about this issue has been posted on the Twitter API Status Page, contact
support. |

Other Recommendations
& Best Practices¶
---------------------------------------

* **Build Data Storage Schemas That Store Numeric Tweet ID
and User ID**: User messages require action to be taken on all
Tweets from that User. Therefore, since all compliance messages are
delivered only by numeric ID, it is important to design storage schemas
that maintain the relationship between Tweet and User based on numeric
IDs. Data consumers will need to monitor compliance events by both Tweet
ID and User ID and be able to update the local data store
appropriately.
* **Build Schemas That Address All Compliance
Statuses**: Depending on how compliance activities will be
addressed in various applications, it may be required to add other
metadata to the data store. For instance, data consumers may decide to
add metadata to an existing database to facilitate restricting the
display of content in countries affected by a status\_withheld
message.
* **Handling Retweet Deletes**: Retweets are a special
kind of Tweet where the original message is nested in an object within
the Retweet. In this case, there are two Tweet IDs referenced in a
Retweet -- the ID for the Retweet, and the ID for the original message
(included in the nested object). When an original message is deleted, a
Tweet delete message is issued for the original ID. Subsequent delete
messages are NOT issued for all of the Retweets. The deletion of the
original ID should be sufficient to delete all subsequent
Retweets.

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