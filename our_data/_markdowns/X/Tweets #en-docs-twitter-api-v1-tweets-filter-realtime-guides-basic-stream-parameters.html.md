
Standard stream parameters | Docs | Twitter Developer Platform 

Standard stream parameters

**Please note:**  

We launched a new version of the POST statuses/filter endpoint as part of Twitter API v2: Early Access. If you are currently using this endpoint, you can use our migration materials to start working with the newer version.

To see all of Twitter's filtered stream endpoint offerings, please visit ouroverview.

Standard streaming API request parameters
-----------------------------------------

Standard

1. delimited
2. stall\_warnings
3. filter\_level
4. language
5. follow
6. track
7. locations
8. count
9. with (deprecated)
10. replies (deprecated)
11. stringify\_friend\_id (deprecated)

Use the following request parameters to define what data is returned by the Streaming API endpoints:

### delimited

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this to the string length indicates that statuses should be delimited in the stream, so that clients know how many bytes to read before the end of the status message. Statuses are represented by a length, in bytes, a newline, and the status text that is exactly length bytes. Note that “keep-alive” newlines may be inserted before each length.

As an example, consider this response to a request to https://stream.twitter.com/1.1/statuses/filter.json?delimited=length&track=twitterapi:

The 1953 indicates how many bytes to read off of the stream to get the rest of the Tweet (including rn). The next length delimiter will occur exactly after 1953 bytes.

### stall\_warnings

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to the string true will cause periodic messages to be delivered if the client is in danger of being disconnected. These messages are only sent when the client is falling behind, and will occur at a maximum rate of about once every 5 minutes. This parameter is most appropriate for clients with high-bandwidth connections.

Such warning messages will look like:

```
{
  "warning":{
    "code":"FALLING_BEHIND",
    "message":"Your connection is falling behind and messages are being queued for delivery to you. Your queue is now over 60% full. You will be disconnected when the queue is full.",
    "percent_full": 60
  }
}
```

### filter\_level

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to one of none, low, or medium will set the minimum value of the filter\_level Tweet attribute required to be included in the stream. The default value is none, which includes all available Tweets.

When displaying a stream of Tweets to end users (dashboards or live feeds at a presentation or conference, for example) it is suggested that you set this value to medium.

### language

This parameter may be used on all streaming endpoints, unless explicitly noted.

Setting this parameter to a comma-separated list of BCP 47 language identifiers corresponding to any of the languages listed on Twitter’s advanced search page will only return Tweets that have been detected as being written in the specified languages. For example, connecting with language=en will only stream Tweets detected to be in the English language.

### follow

A comma-separated list of user IDs, indicating the users whose Tweets should be delivered on the stream. Following protected users is not supported. For each user specified, the stream will contain:

* Tweets created by the user.
* Tweets which are retweeted by the user.
* Replies to any Tweet created by the user.
* Retweets of any Tweet created by the user.
* Manual replies, created without pressing a reply button (e.g. “@twitterapi I agree”).

The stream will not contain:

* Tweets mentioning the user (e.g. “Hello @twitterapi!”).
* Manual Retweets created without pressing a Retweet button (e.g. “RT @twitterapi The API is great”).
* Tweets by protected users.

### track

A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. A phrase may be one or more terms separated by spaces, and a phrase will match if all of the terms in the phrase are present in the Tweet, regardless of order and ignoring case. By this model, you can think of commas as logical ORs, while spaces are equivalent to logical ANDs (e.g. ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter).

The text of the Tweet and some entity fields are considered for matches. Specifically, the text attribute of the Tweet, expanded\_url and display\_url for links and media, text for hashtags, and screen\_name for user mentions are checked for matches.

Each phrase must be between 1 and 60 bytes, inclusive.

Exact matching of phrases (equivalent to quoted phrases in most search engines) is not supported.

Punctuation and special characters will be considered part of the term they are adjacent to. In this sense, “hello.” is a different track term than “hello”. However, matches will ignore punctuation present in the Tweet. So “hello” will match both “hello world” and “my brother says hello.” Note that punctuation is not considered to be part of a #hashtag or @mention, so a track term containing punctuation will not match either #hashtags or @mentions.

UTF-8 characters will match exactly, even in cases where an “equivalent” ASCII character exists. For example, “touché” will not match a Tweet containing “touche”.

Non-space separated languages, such as CJK are currently unsupported.

URLs are considered words for the purposes of matches which means that the entire domain and path must be included in the track query for a Tweet containing an URL to match. Note that display\_url does not contain a protocol, so this is not required to perform a match.

Twitter currently canonicalizes the domain “www.example.com” to “example.com” before the match is performed, so omit the “www” from URL track terms.

Finally, to address a common use case where you may want to track all mentions of a particular domain name (i.e., regardless of subdomain or path), you should use “example com” as the track parameter for “example.com” (notice the lack of period between “example” and “com” in the track parameter). This will be over-inclusive, so make sure to do additional pattern-matching in your code. See the table below for more examples related to this issue.

Track examples:

|  |  |  |
| --- | --- | --- |
| Parameter value | Will match... | Will not match... |
| Twitter | TWITTERtwitter “Twitter” twitter. #twitter @twitter http://twitter.com | TwitterTracker#newtwitter |
| Twitter’s | I like Twitter’s new design | Someday I’d like to visit @Twitter’s office |
| twitter api,twitter streaming | The Twitter API is awesomeThe twitter streaming service is fast Twitter has a streaming API | I’m new to Twitter |
| example.com | Someday I will visit example.com | There is no example.com/foobarbaz |
| example.com/foobarbaz | example.com/foobarbazwww.example.com/foobarbaz | example.com |
| www.example.com/foobarbaz |  | www.example.com/foobarbaz |
| example com | example.comwww.example.com foo.example.com foo.example.com/bar I hope my startup isn’t merely another example of a dot com boom! |  |

### locations

A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets by. Only geolocated Tweets falling within the requested bounding boxes will be included—unlike the Search API, the user’s location field is not used to filter Tweets.

Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the bounding box coming first. For example:

|  |  |
| --- | --- |
| Parameter value | Tracks Tweets from... |
| -122.75,36.8,-121.75,37.8 | San Francisco |
| -74,40,-73,41 | New York City |
| -122.75,36.8,-121.75,37.8,-74,40,-73,41 | San FranciscoOR New York City |

Bounding boxes do not act as filters for other filter parameters. For example track=twitter&locations=-122.75,36.8,-121.75,37.8 would match any Tweets containing the term Twitter (even non-geo Tweets) OR coming from the San Francisco area.

The streaming API uses the following heuristic to determine whether a given Tweet falls within a bounding box:

* If the coordinates field is populated, the values there will be tested against the bounding box. Note that this field uses geoJSON order (longitude, latitude).
* If coordinates is empty but place is populated, the region defined in place is checked for intersection against the locations bounding box. Any overlap will match.
* If none of the rules listed above match, the Tweet does not match the location query. Note that the geo field is deprecated, and ignored by the streaming API.

If you would like to exclude place matches or only include places which fall completely within the bounding box, your code will have to perform an additional filtering step after reading the filtered stream.

Note that native Retweets are not matched by this parameter. While the original Tweet may have a location, the Retweet will not.

### count

This parameter requires elevated access to use.

When reconnecting to a streaming endpoint, elevated access clients may include the count parameter to attempt to backfill missed messages which occurred during the disconnect period. The supplied value may be an integer from 1 to 150000 or from -1 to -150000. If a positive number is specified, the stream will transition to live values once the backfill has been delivered to the client. If a negative number is specified, the stream will disconnect once the backfill has been delivered to the client, which may be useful for debugging.

Note that use of this parameter should be carefully considered, as high values increase the chance of a subsequent disconnect. To demonstrate this, consider the case where a client connects without backfill. Upon establishing a connection, Twitter will allocate a fixed-size queue, and begin adding messages to be streamed to the client. If the client reads too slowly, the queue will fill up. Once full, Twitter will disconnect the client:

When a client connects with backfill, that number of messages are immediately added to the queue. The client must read messages faster than the current rate of Tweets being added to the queue, as the available buffer before a disconnect occurs can be much smaller than when connecting without backfill.

### with (deprecated)

Available on User Streams and Site Streams (deprecated)

The with parameter controls the types of messages delivered to User and Site Streams clients.

* The default for Site Streams is with=user, which only streams messages from the user associated with the stream.
* The default for User Streams is with=followings which adds messages from accounts the user follows, equivalent to the user’s home timeline.

Despite the difference in defaults, Site and User each accept both user and followings parameter values.

### replies (deprecated)

Available on User Streams and Site Streams (deprectated)  

By default @replies are only sent if the current user follows both the sender and receiver of the reply. For example, consider the case where Alice follows Bob, but Alice doesn’t follow Carol. By default, if Bob @replies Carol, Alice does not see the Tweet. This mimics twitter.com and api.twitter.com behavior. To have such Tweets returned in a streaming connection, specify replies=all when connecting.

### stringify\_friend\_ids (deprecated)

Available on  User Streams and Site Streams (deprecated)  

By default, user and site streams send the Friends List preamble as an array of integers (equivalent to stringify\_friend\_ids=false). However, as the number of Twitter users grows, user ids are quickly approaching the 32-bit integer threshold, which when passed, will require your code to handle 64-bit integers. Some languages or libraries (including JSON decoders) expect that integers provided in JSON are 32-bit and will therefore have erroneous and potentially unpredictable behavior. If natively interpreting integers as 64-bit poses a challenge for you, we offer the stringify\_friend\_ids=true parameter to have the friends list preamble be an array of strings (instead of integers). If you use this parameter, note that it will suppress the friends array and return the friends\_str array in its place. See the Friends List message type entry for an example payload.

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