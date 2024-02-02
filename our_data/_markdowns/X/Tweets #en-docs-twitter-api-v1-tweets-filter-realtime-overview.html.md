
Overview | Docs | Twitter Developer Platform 

Overview

**Please note:**  

We recently released filtered stream, a set of Twitter API v2 endpoints that has similar functionality to this one. The new version is now ready for production and serves adequate access for the majority of developers on our platform.

This endpoint is now deprecated and has NOT been updated to include Tweet edit metadata. Learn more about these metadata on the "Edit Tweets" fundamentals page.   

We have deprecated the delivery of compliance messages through this endpoint. Apps created after April 29, 2022 cannot access this endpoint. This endpoint will stop delivering compliance messages beginning October 31, 2022. Learn more about this change and see our migration resources.

Developers in need of higher levels of access can explore our enterprise PowerTrack API. You can see an overview of our filtered stream offerings on our filtered stream overview page, and see what's new with v2 by visiting themigration guide.  

Overview
--------

Standard

Returns public statuses that match one or more filter predicates. Multiple parameters may be specified which allows most clients to use a single connection to the Streaming API. Both GET and POST requests are supported, but GET requests with too many parameters may cause the request to be rejected for excessive URL length. Use a POST request to avoid long URLs.

The track, follow, and locations fields should be considered to be combined with an OR operator. track=foo&follow=1234 returns Tweets matching “foo” OR created by user 1234.

The default access level allows up to 400 track keywords, 5,000 follow userids and 25 0.1-360 degree location boxes. If you need more access to the Streaming API, please use the enterprise streaming API, PowerTrack.  

Streaming message types
-----------------------

### Standard 'Track' stream messages

In addition to standard Tweet payloads, the following kinds of messages may be delivered on a stream. Note that this list may not be comprehensive—additional objects may be introduced into streams in the future. Ensure that your parser is tolerant of unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status with another status nested inside it. If you are matching Tweet fields using regular expressions, it is possible that you will match fields in the nested Tweet instead of the wrapper. As a rule of thumb it is better to use a JSON parser to extract information from message payloads.

#### Maintenance Messages

#### Blank lines

On slow streams, some messages may be blank lines (\r\n or similar) which serve as “keep-alive” signals to prevent clients and other network infrastructure from assuming the stream has stalled and closing the connection.

#### Limit notices (limit)

These messages indicate that a filtered stream has matched more Tweets than its current rate limit allows to be delivered. Limit notices contain a total count of the number of undelivered Tweets since the connection was opened, making them useful for tracking counts of track terms, for example. Note that the counts do not specify which filter predicates undelivered messages matched.

{  
"limit":{  
"track":1234  
}  
}

#### Disconnect messages (disconnect)

Streams may be shut down for a variety of reasons. The streaming API will attempt to deliver a message indicating why a stream was closed. Note that if the disconnect was due to network issues or a client reading too slowly, it is possible that this message will not be received.

{  
"disconnect":{  
"code": 4,  
"stream\_name":"",  
"reason":""  
}  
}

The following table lists possible status codes and their meanings. Additional codes may be used without warning.

| Code | Name | Description |
| --- | --- | --- |
| 1 | Shutdown | The feed was shutdown (possibly a machine restart) |
| 2 | Duplicate stream | The same endpoint was connected too many times. |
| 4 | Stall | The client was reading too slowly and was disconnected by the server. |
| 5 | Normal | The client appeared to have initiated a disconnect. |
| 7 | Admin logout | The same credentials were used to connect a new stream and the oldest was disconnected. |
| 9 | Max message limit | The stream connected with a negative count parameter and was disconnected after all backfill was delivered. |
| 10 | Stream exception | An internal issue disconnected the stream. |
| 11 | Broker stall | An internal issue disconnected the stream. |
| 12 | Shed load | The host the stream was connected to became overloaded and streams were disconnected to balance load. Reconnect as usual. |

#### Stall warnings (warning)

When connected to a stream using the stall\_warnings parameter, you may receive status notices indicating the current health of the connection. See the stall\_warnings documentation for more information.

{  
"warning":{  
"code":"FALLING\_BEHIND",  
"message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",  
"percent\_full": 60  
}  
}

### Compliance Messages

#### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code must honor these messages by clearing the referenced Tweet from memory and any storage or archive, even in the rare case where a deletion message arrives earlier in the stream that the Tweet it references.

{  
"delete":{  
"status":{  
"id":1234,  
"id\_str":"1234",  
"user\_id":3,  
"user\_id\_str":"3"  
}  
}  
}

#### Location deletion notices (scrub\_geo)

These messages indicate that geolocated data must be stripped from a range of Tweets. Clients must honor these messages by deleting geocoded data from Tweets which fall before the given status ID and belong to the specified user. These messages may also arrive before a Tweet which falls into the specified range, although this is rare.

{  
"scrub\_geo":{  
"user\_id":14090452,  
"user\_id\_str":"14090452",  
"up\_to\_status\_id":23260136625,  
"up\_to\_status\_id\_str":"23260136625"  
}  
}

#### Withheld content notices (status\_withheld, user\_withheld)

These messages indicate that either the indicated Tweet or indicated user has had their content withheld.

#### status\_withheld¶

These events contain an id field indicating the status ID, a user\_id indicating the user, and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical Tweet that has been withheld in Germany and Argentina.

{  
"status\_withheld":{  
"id":1234567890,  
"user\_id":123456,  
"withheld\_in\_countries":["DE", "AR"]  
}  
}

#### user\_withheld¶

These events contain an id field indicating the user ID and a collection of withheld\_in\_countries uppercase two-letter country codes. This example illustrates a hypothetical user who has been withheld in Germany and Argentina.

{  
"user\_withheld":{  
"id":123456,  
"withheld\_in\_countries":["DE","AR"]  
}  
}

#### User update

Everytime a user updates their profile we broadcast a user\_update event to indicate that an update has been made to the user profile. The source and target objects are identical in content.

{  
"created\_at": "Tue Aug 06 02:23:21 +0000 2013",  
"source": {  
...  
},  
"target": {  
...  
},  
"event": "user\_update"  
}

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