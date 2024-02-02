Overview

**Please note**

We have released a new compliance tool to Twitter API v2 called [batch compliance](https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance). This new tool allows you to upload large datasets of Tweet or user IDs to retrieve their compliance status in order to determine what data requires action in order to bring your datasets into compliance.

In addtion, both the batch compliance and the compliance firehose have been updated to support Tweet edits. For the compliance firehose, a new 'tweet\_edit' event was added. See the [Compliance Data Objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects) documentation for more details. Learn more about how Edit Tweet metadata works on the [Edit Tweets fundamentals](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) page.

Overview
--------

Enterprise

One of Twitter’s core values is to defend and respect the user’s voice. This includes respecting their expectations and intent when they delete, modify, or edit the content they choose to share on Twitter. We believe that this is critically important to the long term health of one of the largest public, real-time information platforms in the world. Twitter puts controls in the hands of its users, giving individuals the ability to control their own Twitter experience. We believe that business consumers that receive Twitter data have a responsibility to honor the expectations and intent of end users.

For more information on the types of compliance events that are possible on the Twitter platform, reference our article, [Honoring User Intent on Twitter](https://developer.twitter.com/content/developer-twitter/en/docs/tweets/compliance/guides/honoring-user-intent).  

Any developer or company consuming Twitter data via an API holds an obligation to use all reasonable efforts to honor changes to user content. This obligation extends to user events such as deletions, modifications, and changes to sharing options (e.g., content becoming protected or withheld). This also includes when users edit their Tweets. Please reference the specific language in the [Developer Policy](https://developer.twitter.com/en/developer-terms/policy.html) and/or your Twitter Data Agreement to understand how this obligation affects your use of Twitter data.  

Twitter offers the following solutions that deliver information about these user compliance events and whether a specific Tweet or User is publicly available or not. A brief overview of the solutions and their general integration patterns is detailed below:

#### GET statuses/lookup and GET users/lookup

* Format: REST API’s See: [GET statuses/lookup](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup.html) and [GET users/lookup](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup.html).
* These endpoints always return the latest version of any Tweet edits. All Tweet objects describing Tweets created after the edit feature was introduced will include Tweet edit metadata. This is true even for Tweets that were not edited. 
* For all Tweets, requests for Tweets more than 30 minutes after they were created will represent the final state of all Tweets.   
    
* Deliver availability information for specific Tweets or Users as defined by the caller as part of the API request.
* May be used for ad-hoc spot-checking on the current availability state of a specific group of Tweets / Users.
* Ideal for customers who need a way to check the current state of a specific Tweet or User at a given moment in time.
* These API’s provide a helpful mechanism that may be used by customers who need to check the availability of a piece of Content, for instance when:
    1. Displaying Tweets
    2. Engaging with a Tweet(s) or User(s) in a 1:1 way
    3. Distributing Twitter Content to a 3rd party through an allowed file download
    4. Storing Tweets for extended periods of time

#### Compliance Firehose (enterprise only)

* Format: Streaming API See: [Compliance Firehose](https://developer.twitter.com/en/docs/tweets/compliance/api-reference.html).
* Delivers realtime stream of [Compliance activities](https://developer.twitter.com/en/docs/tweets/compliance/guides/compliance-data-objects) on Twitter. These activities include when Tweets are edited. 
* May be used to maintain compliance state across a set of stored data as new compliance events happen on the platform.
* Ideal for customers consuming and storing large quantities of Twitter data for extended periods of time.

Compliance Best Practices

Recommendations & Best Practices
--------------------------------

* **Build Data Storage Schemas That Store Numeric Tweet ID and User ID**: User messages require action to be taken on all Tweets from that User. Therefore, since all compliance messages are delivered only by numeric ID, it is important to design storage schemas that maintain the relationship between Tweet and User based on numeric IDs. Data consumers will need to monitor compliance events by both Tweet ID and User ID and be able to update the local data store appropriately.
    
* **Build Schemas That Address All Compliance Statuses**: Depending on how compliance activities will be addressed in various applications, it may be required to add other metadata to the data store. For instance, data consumers may decide to add metadata to an existing database to facilitate restricting the display of content in countries affected by a status\_withheld message.
    
* **Handling Retweet Deletes**: Retweets are a special kind of Tweet where the original message is nested in an object within the Retweet. In this case, there are two Tweet IDs referenced in a Retweet – the ID for the Retweet, and the ID for the original message (included in the nested object). When an original message is deleted, a Tweet delete message is issued for the original ID. Tweet deletion events typically trigger delete events for all Retweets. However, in some cases not all are sent and client systems should be tolerant of incomplete Retweet deletions. The deletion of the original ID should be sufficient to delete all subsequent Retweets. It is a best practice to reference the original Tweet ID when storing Retweets, and deleting all referenced Retweets when receiving Tweet delete events.

Compliance Data Objects

Possible types of compliance events will include Tweet (or “status”) events and User events, for which there are multiple types described below.    

Please note:

* Read more about User statuses [here](https://support.twitter.com/articles/14016) and our developer policy around deleted Tweets [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy).
* The Compliance Firehose has been updated to provide 'tweet\_edit' events. 
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by status\_deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.  
  

| Original Message Type | Object | Permanent (Yes/No) | Recommended Action |
| --- | --- | --- | --- |
| delete | Status | Yes | Delete associated Tweet. |
| status\_withheld | Status | Yes | Suppress associated Tweet in specific countries listed in the status\_withheld message. |
| drop | Status | No  | Remove the Tweet from public view. |
| undrop | Status | No  | Status may be displayed again and treated as public. |
| tweet\_edit | Status | Yes | Honor and, where relevant, display the new edit. |
| user\_delete | User | No  | Suppress or delete all Tweets by associated user. |
| user\_undelete | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| user\_protect | User | No  | Suppress or delete all Tweets by associated user. |
| user\_unprotect | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| user\_suspend | User | No  | Suppress or delete all Tweets by associated user. |
| user\_unsuspend | User | No  | All Tweets by associated user may be displayed again and treated as public. |
| scrub\_geo | User | Yes | Delete all geodata provided by Twitter for all Tweets by the user prior to the specified Tweet in the scrub\_geomessage. Note that subsequent Tweets by a user may contain geodata that may be used. |
| user\_withheld | User | Yes | Suppress Tweets by associated user in specific countries listed in the user\_withheld message. |
| delete | Favorite | Yes | Delete associated like/favorite. |

Payload examples
----------------

See the payload examples below for each compliance event described in the table above.

**Tweet edit**

      `{"tweet_edit":    {      "id": "1557445923210514432"      "initial_tweet_id": "1557433858676740098",      "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"],      "timestamp_ms": "1660155761384"    }  }`
    

#### Tweet delete

      `{   "delete": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220608",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Tweet withheld

      `{   "status_withheld": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220608",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "withheld_in_countries": [       "XY"     ],     "timestamp_ms": "1432228155593"   } }`
    

#### Drop

      `{   "drop": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220600",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Undrop

      `{   "undrop": {     "status": {       "id": 601430178305220600,       "id_str": "601430178305220600",       "user_id": 3198576760,       "user_id_str": "3198576760"     },     "timestamp_ms": "1432228155593"   } }`
    

#### Scrub geo

      `{   "scrub_geo": {     "user_id": 519761961,     "up_to_status_id": 411552403083628540,     "up_to_status_id_str": "411552403083628544",     "user_id_str": "519761961",     "timestamp_ms": "1432228180345"   } }`
    

#### User delete

      `{   "user_delete": {     "id": 771136850,     "timestamp_ms": "1432228153548"   } }`
    

#### User undelete

      `{   "user_undelete": {     "id": 796250066,     "timestamp_ms": "1432228149062"   } }`
    

#### User withheld

      `{   "user_withheld": {     "user": {       "id": 1375036644,       "id_str": "1375036644"     },     "withheld_in_countries": [       "XY"     ],     "timestampMs": "2014-08-27T23:49:41.839+00:00"   } }`
    

#### User protect

      `{   "user_protect": {     "id": 3182003550,     "timestamp_ms": "1432228177137"   } }`
    

#### User unprotect

      `{   "user_unprotect": {     "id": 2911076065,     "timestamp_ms": "1432228180113"   } }`
    

#### User suspend

      `{   "user_suspend": {     "id": 3120539094,     "timestamp_ms": "1432228194217"   } }`
    

#### User unsuspend

      `{   "user_unsuspend": {     "id": 3293130873,     "timestamp_ms": "1432228193828"   } }`

Integrating Compliance Firehose

The Compliance Firehose is a realtime streaming API that delivers compliance events that occur on the Twitter platform. For an understanding of compliance events and how they are generated on Twitter, please reference our article, [Honoring User Intent on Twitter](https://developer.twitter.com/en/docs/basics/honoring-user-intent-on-twitter.html).

It is important to note that Tweet and User events are delivered independently and that each should be processed independently (i.e. a Tweet delete doesn’t imply a User event, and vice versa.) Several User events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.

User\_deletes are followed by status\_deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their tweets 30 days later do not occur.

User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

It is never suitable to display compliance events directly to users of your software or to otherwise incorporate them into your products or customer experiences. They are intended solely for maintaining compliance and honoring the actions of Twitter users.

Integrating with the Compliance Firehose
----------------------------------------

To integrate the Compliance Firehose into your system, you will need to build an integration that can do the following:

1. Establish a streaming connection to each streaming API partition of the Compliance Firehose
2. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes
3. Reconnect to the stream partitions automatically when disconnected for any reason
4. Process compliance events that are relevant to Tweet and User data you have stored in accordance with the guidance presented above

Honoring user intent on Twitter

We believe that respecting the privacy and intent of Twitter users is critically important to the long term health of one of the largest public, real-time information platforms in the world. Twitter puts privacy controls in the hands of its users, giving individuals the ability to control their own Twitter experience. As business consumers of Twitter data, we have a collective responsibility to honor the privacy and actions of end users in order to maintain this environment of trust and respect.  

There are a variety of things that can happen to Tweets and User accounts that impact how they are displayed on the platform. The actions that affect privacy and intent are defined at both the Status (Tweet) and User levels. These actions include:

### User

| Action | Description |
| --- | --- |
| Protect Account | A Twitter user can protect or unprotect their account at any time. Protected accounts require manual user approval of every person who is allowed to view their account's Tweets.   <br>For more information, see [About Public and Protected Tweets](https://support.twitter.com/articles/14016-about-public-and-protected-tweets). |
| Delete Account | A Twitter user can decide to delete their account and all associated status messages at any time. Twitter retains the account information for 30 days after deletion in case the user decides to undelete and effectively reactivate their account. |
| Scrub Geo | A Twitter user can remove all location data from past Tweets at any time. This known as “scrub geo”. |
| Suspend Account | Twitter retains the right to suspend accounts that are in violation of the Twitter Rules or if an account is suspected to have been hacked or compromised. Account suspensions can only be reversed (unsuspend) by Twitter. |
| Withhold Account | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld account can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Status

| Action | Description |
| --- | --- |
| Delete Status | A Twitter user can delete a status at any point in time. Deleted statuses cannot be reversed and are permanently deleted. |
| Withhold Status | Twitter retains the right to reactively withhold access to certain content in a specific country from time to time. A withheld status can only be made unwithheld by Twitter.   <br>For more information, see [Country Withheld Content](https://support.twitter.com/articles/20169222-country-withheld-content). |

### Keeping Track of User and Status Changes

The state of a User or Status can change at any time due to one of the actions above, and this impacts how consumers of Twitter data are expected to treat the availability and privacy of all associated content. When these actions happen, a corresponding compliance message is sent that indicates that the state of a Status or User has changed.

GET compliance/firehose

compliance-firehose

GET compliance/firehose
=======================

Jump to on this page

[Methods](#Methods)

[Authentication](#Authentication)

[GET /compliance/:stream](#Connect)

[Response Codes](#ResponseCodes)

[Other Recommendations & Best Practices](#OtherRecommendations)

Methods [¶](#methods- "Permalink to this headline")
---------------------------------------------------

| Method | Description |
| --- | --- |
| [GET /compliance/:stream](#Connect) | Connect to the Data Stream |

Authentication [¶](#authentication- "Permalink to this headline")
-----------------------------------------------------------------

All requests to the Compliance Firehose API must use HTTP Basic Authentication, constructed from a valid email address and password combination used to log into your account at console.gnip.com. Credentials must be passed as the Authorization header for each request.

GET /compliance/:stream [¶](#get-compliance-stream- "Permalink to this headline")
---------------------------------------------------------------------------------

Establishes a persistent connection to the Compliance firehose data stream, through which the compliance events will be delivered.

|     |     |
| --- | --- |
| **Request Method** | HTTP GET |
| **Connection Type** | Keep-Alive |
| **URL** | Found on the stream's API Help page of your dashboard, and resembles the following structure:  <br>  <br><br>[https://gnip-stream.twitter.com/stream/compliance/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1](https://gnip-stream.twitter.com/stream/compliance/accounts/:account_name/publishers/twitter/:stream_label.json?partition=1)<br><br>**Note:** The "partition" parameter is required. You will need to connect to all 8 partitions, each containing 12.5% of the total volume, to consume the full stream. |
| **Compression** | Gzip. To connect to the stream using Gzip compression, simply send an Accept-Encoding header in the connection request. The header should look like the following:  <br>  <br>Accept-Encoding: gzip |
| **Character Encoding** | UTF-8 |
| **Response Format** | JSON. The header of your request should specify JSON format for the response. |
| **Rate Limit** | 10 requests per 60 seconds. |
| **Read Timeout** | Set a read timeout on your client, and ensure that it is set to a value beyond 30 seconds. |
| **Support for Tweet edits** | All Tweet edits trigger a "tweet\_edit" Compliance event. See the [Compliance Data Objects](https://developer.twitter.com/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects) documentation for more details. |

**Example Curl Request**

The following example request is accomplished using cURL on the command line:

curl --compressed -v -uexample@customer.com "https://gnip-stream.twitter.com/stream/compliance/accounts/:account\_name/publishers/twitter/:stream\_label.json?partition=1"

_Note:_ the above request is only connecting to `partition=1` of the Compliance firehose - you'll need to connect to all 8 partitions to consume the entirety of this stream.

Response Codes [¶](#response-codes- "Permalink to this headline")
-----------------------------------------------------------------

The following responses may be returned by the API for these requests. Most error codes are returned with a string with additional details in the body. For non-200 responses, clients should attempt to reconnect.

| Status | Text | Definition |
| --- | --- | --- |
| 200 | Success | The connection was successfully opened, and new activities will be sent through as they arrive. |
| 401 | Unauthorized | HTTP authentication failed due to invalid credentials. Log in to console.gnip.com with your credentials to ensure you are using them correctly with your request. |
| 406 | Not Acceptable | Generally, this occurs where your client fails to properly include the headers to accept gzip encoding from the stream, but can occur in other circumstances as well. Will contain a JSON message similar to "This connection requires compression. To enable compression, send an 'Accept-Encoding: gzip' header in your request and be ready to uncompress the stream as it is read on the client end." |
| 429 | Rate Limited | Your app has exceeded the limit on connection requests. |
| 503 | Service Unavailable | Twitter server issue. Reconnect using an exponential backoff pattern. If no notice about this issue has been posted on the [Twitter API Status Page](https://api.twitterstat.us/), contact support. |

Other Recommendations & Best Practices [¶](#other-recommendations-best-practices- "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

* **Build Data Storage Schemas That Store Numeric Tweet ID and User ID**: User messages require action to be taken on all Tweets from that User. Therefore, since all compliance messages are delivered only by numeric ID, it is important to design storage schemas that maintain the relationship between Tweet and User based on numeric IDs. Data consumers will need to monitor compliance events by both Tweet ID and User ID and be able to update the local data store appropriately.
    
* **Build Schemas That Address All Compliance Statuses**: Depending on how compliance activities will be addressed in various applications, it may be required to add other metadata to the data store. For instance, data consumers may decide to add metadata to an existing database to facilitate restricting the display of content in countries affected by a status\_withheld message.
    
* **Handling Retweet Deletes**: Retweets are a special kind of Tweet where the original message is nested in an object within the Retweet. In this case, there are two Tweet IDs referenced in a Retweet -- the ID for the Retweet, and the ID for the original message (included in the nested object). When an original message is deleted, a Tweet delete message is issued for the original ID. Subsequent delete messages are NOT issued for all of the Retweets. The deletion of the original ID should be sufficient to delete all subsequent Retweets.