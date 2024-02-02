::: is-table-default
Use this migration guide to understand the similarities and differences
between [PowerTrack
API](/en/docs/twitter-api/enterprise/powertrack-api/overview.html) and
Twitter API v2 [filtered
stream](/en/docs/twitter-api/tweets/filtered-stream/introduction.html) ,
and to help migrate a current PowerTrack API integration to v2 filtered
stream.

-   **Similarities**
    -   Streaming delivery method
    -   Integration process
    -   Persistent stream connection with separate rules management
        endpoints
    -   Rule syntax
    -   Rule operators (with exceptions)
    -   Rule matching logic
    -   Support for Tweet edit history and metadata
-   **Differences**
    -   Rule length
    -   Rule volume
    -   Endpoint URLs
    -   App and Project requirement for access
    -   Authentication method
    -   Request parameters
    -   Usage tracking
    -   Multiple streams, redundant conections, backfill and Replay
        recovery
    -   Request parameters and response format
    -   Response JSON data structure

### 

### Similarities

#### Streaming delivery method

Both PowerTrack and Twitter API v2 filtered stream use streaming data
delivery, which require the client to establish an open connection to an
endpoint and keeping a very long lived HTTP request, and parsing the
response incrementally from the server in real time.  Both PowerTrack
and Twitter API v2 filtered stream filter publicly available Tweets
matching rules that exist on the stream in real time, and use keep-alive
signals as new line characters ( [ \\r\\n ]{.code-inline} ) to signal
the connection is still active. Both PowerTrack and Twitter API v2
filtered stream endpoint connections deliver data in real time and
should be read by the connecting client quickly.

#### Integration process

Integrating with filtered stream is similar to integrating with
PowerTrack, using the general process below:

1.  Establish a streaming connection.
2.  Asynchronously send separate requests to add and delete rules from
    the stream.
3.  Reconnect to the stream automatically when connection is
    disconnected.

#### Persistent stream connection with separate rules management endpoints

Similar to the PowerTrack API and Rules API, the new Twitter API v2
filtered stream endpoints allows you to apply multiple rules to a single
stream and add and remove rules to your stream while maintaining the
stream connection.

#### 

#### Rule syntax, operators, and matching rules logic

The Twitter API v2 filtered stream uses a subset of the same rule
operators currently used for PowerTrack rules. These operators are used
to create boolean based rule syntax used for filtering desired matching
Tweets from the live stream.  Both PowerTrack and filtered stream use
the same rule syntax for building rules and matching logic is the same.
While the majority of the operators are available for both PowerTrack
and filter stream, there are a few notable differences and net new
operators listed below.  For more details and example uses for each
operator see current [PowerTrack
operators](/en/docs/twitter-api/enterprise/powertrack-api/guides/operators.html)
and current Twitter API v2 [filtered stream
operators](/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule.html)
.

Please note that many operators (noted as \'advanced operators\') are
reserved for those users who have been approved for [Academic Research
access or Enterprise
access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

[Operators available with both PowerTrack and Twitter API v2 Filter
stream:]{.underline}

+-----------------------------------+-----------------------------------+
| **Standalone operators**          | **Conjunction required operators  |
|                                   | (must be used with at least one   |
|                                   | standalone operator within a      |
|                                   | rule)**                           |
+===================================+===================================+
| keyword (example: [ coffee        | [ has:links ]{.code-inline}       |
| ]{.code-inline} )                 |                                   |
|                                   | [ lang: ]{.code-inline}           |
| emoji (example: 🐶 or [           |                                   |
| \\uD83D\\uDC36 ]{.code-inline} )  | [ has:mentions ]{.code-inline}    |
|                                   |                                   |
| \"exact phrase match\" (example:  | [ has:media ]{.code-inline}       |
| [ \"happy birthday\"              |                                   |
| ]{.code-inline} )                 | [ has:images ]{.code-inline}      |
|                                   |                                   |
| [ from: ]{.code-inline}           | [ has:videos ]{.code-inline}      |
|                                   |                                   |
| [ to: ]{.code-inline}             | [ is:retweet ]{.code-inline}      |
|                                   |                                   |
| [ @ ]{.code-inline}               | [ is:quote ]{.code-inline}        |
|                                   |                                   |
| [ retweets_of: ]{.code-inline}    | [ is:verified ]{.code-inline}     |
|                                   |                                   |
| [ \# ]{.code-inline}              | [ has:hashtags ]{.code-inline}    |
|                                   |                                   |
| [ url: ]{.code-inline}            | [ has:geo ]{.code-inline}         |
|                                   |                                   |
|                                   | [ sample: ]{.code-inline}         |
|                                   |                                   |
|                                   | [ -is:nullcast ]{.code-inline}    |
+-----------------------------------+-----------------------------------+

+-----------------------------------------------------------------------+
| **Net new operators available with Twitter API v2 filtered stream**   |
+-----------------------------------------------------------------------+
| [ conversation_id: ]{.code-inline} - matches on Tweets that exist in  |
| any reply threads from the specified Tweet conversation root.Net new  |
| operators available with Twitter API v2 filtered stream:              |
|                                                                       |
| [ context: ]{.code-inline} - matches on Tweets that have been         |
| annotated with a context of interest.                                 |
|                                                                       |
| [ entity: ]{.code-inline} - matches on Tweets that have been          |
| annotated with an entity of interest.                                 |
+-----------------------------------------------------------------------+

+-----------------------------------------------------------------------+
| **Operators currently only available on PowerTrack API**              |
+-----------------------------------------------------------------------+
| [ url_title: ]{.code-inline}                                          |
|                                                                       |
| [ url_description: ]{.code-inline}                                    |
|                                                                       |
| [ followers_count: ]{.code-inline}                                    |
|                                                                       |
| [ statuses_count: ]{.code-inline}                                     |
|                                                                       |
| [ friends_count: ]{.code-inline}                                      |
|                                                                       |
| [ listed_count: ]{.code-inline}                                       |
|                                                                       |
| \"proximity match\"\~3                                                |
|                                                                       |
| [ contains: ]{.code-inline}                                           |
|                                                                       |
| [ has:symbols ]{.code-inline}                                         |
|                                                                       |
| [ url_contains: ]{.code-inline}                                       |
|                                                                       |
| [ in_reply_to_status_id: ]{.code-inline}                              |
|                                                                       |
| [ retweets_of_status_id: ]{.code-inline}                              |
|                                                                       |
| [ source: ]{.code-inline}                                             |
|                                                                       |
| [ bio: ]{.code-inline}                                                |
|                                                                       |
| [ bio_name: ]{.code-inline}                                           |
|                                                                       |
| [ bio_location: ]{.code-inline}                                       |
|                                                                       |
| [ place: ]{.code-inline}                                              |
|                                                                       |
| [ place_country: ]{.code-inline}                                      |
|                                                                       |
| [ point_radius: ]{.code-inline}                                       |
|                                                                       |
| [ bounding_box: ]{.code-inline}                                       |
|                                                                       |
| [ is:reply ]{.code-inline}                                            |
|                                                                       |
| (Available without conjunction)                                       |
|                                                                       |
| [ has:links ]{.code-inline}                                           |
|                                                                       |
| [ lang: ]{.code-inline}                                               |
|                                                                       |
| [ has:mentions ]{.code-inline}                                        |
|                                                                       |
| [ has:media ]{.code-inline}                                           |
|                                                                       |
| [ has:images ]{.code-inline}                                          |
|                                                                       |
| [ has:videos ]{.code-inline}                                          |
|                                                                       |
| [ is:retweet ]{.code-inline}                                          |
|                                                                       |
| [ is:quote ]{.code-inline}                                            |
|                                                                       |
| [ is:verified ]{.code-inline}                                         |
|                                                                       |
| [ is:reply ]{.code-inline}                                            |
|                                                                       |
| [ has:hashtags ]{.code-inline}                                        |
|                                                                       |
| [ has:geo ]{.code-inline}                                             |
|                                                                       |
| [ sample: ]{.code-inline}                                             |
+-----------------------------------------------------------------------+

**Support for Tweet edit history and metadata**\

Both versions provide metadata that describes any edit history. Check
out the [filtered stream API
References](/en/docs/twitter-api/tweets/filtered-stream/api-reference)
and the [Edit Tweets fundamentals
page](/en/docs/twitter-api/edit-tweets) for more details.

### Differences

#### Rule length 

Rule length is measured the same way (by character count) for both
PowerTrack and filtered stream rules, however the maximum length for
PowerTrack rules is 2048 characters and the maximum rule length for
rules on Twitter API v2 filtered stream varies by [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

Essential and Elevated access - 512 characters\

<div>

Academic Research access - 1024 characters Enterprise access - 2048
characters

</div>

#### Rule volume

The PowerTrack maximum rule volume per stream is defined within the
enterprise account contract.  Twitter API v2 filtered stream rule volume
varies by [access
level](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

Essential access - 5 rules Elevated access - 25 rules Academic research
access - 1000 rules Enterprise access - 2500+ rules

#### Endpoint URLs

-   PowerTrack endpoints:
    -   [
        https://gnip-stream.twitter.com/stream/powertrack/accounts/{account_name}/publishers/twitter/{stream_label}.json
        ]{.code-inline}
    -   [
        https://gnip-api.twitter.com/rules/powertrack/accounts/{account_name}/publishers/twitter/{stream_label}.json
        ]{.code-inline}
    -   [
        https://gnip-api.twitter.com/rules/powertrack/accounts/{account_name}/publishers/twitter/{stream_label}/validation.json
        ]{.code-inline}
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets/search/stream ]{.code-inline}
    -   [ https://api.twitter.com/2/tweets/search/stream/rule
        ]{.code-inline}

####  App and Project requirements for v2 access

PowerTrack access is granted through a contracted annual subscription
for data, and set up through console.gnip.com by your account manager at
Twitter.  PowerTrack does not require a Twitter developer App to
access.  In order to use the Twitter API v2 filter stream, you must have
[signed up for a Twitter developer
account](https://developer.twitter.com/en/portal/petition/essential/basic-info)
, and a Twitter [developer App](/en/portal/projects-and-apps.html)
associated with a Project. The developer App and Project setup for
Twitter API v2 access is all done through the [developer
portal](https://developer.twitter.com/en/portal/projects-and-apps) .

#### Authentication method

The PowerTrack API endpoints use Basic Authentication set up in
console.gnip.com. The Twitter API v2 filtered stream endpoints require a
Twitter developer App and an [OAuth 2.0 App Access
Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0)
(also referred to as Application-only or Bearer Authentication). To make
requests to the Twitter API v2 version you must use your specific
developer App\'s Access Token to authenticate your requests.

In the process of setting up your developer account, developer App and
Project, an App Access Token is created and shared within the dev portal
user interface, however, you can generate a new one by navigating to
your app\'s "Keys and tokens" page on the [developer
portal](https://developer.twitter.com/en/portal/projects-and-apps) . If
you'd like to generate/destroy the App Access Tokens programmatically,
see this [OAuth 2.0 App-Only
guide](/en/docs/authentication/oauth-2-0/application-only.html) .

#### Usage tracking

PowerTrack usage can be retrieved programatically using the Usage API,
or can be seen in console.gnip.com on the [usage
tab](/en/docs/twitter-api/enterprise/console/usage.html) .  Tweet
consumption across all PowerTrack streams is deduplicated each day and
volume consumption is defined within the enterprise contract.

Twitter API v2 filtered stream usage can be tracked within the developer
portal at the Project level.  Tweet consumption is [set at the Project
level](/en/docs/projects/overview.html) and is shared across several
different Twitter API v2 endpoints, including filtered stream, recent
search, user Tweet timeline and user mention timeline.  Currently with
Basic Access, the monthly Tweet consumption limit is 500,000 Tweets per
month total, and Tweets are not deduplicated across products or time.

#### 

#### Multiple streams, redundant conections, backfill and Replay API for recovery

There are several recovery and redunancy features available via
PowerTrack, some of which are not yet available for Twitter API v2
filtered stream.  For PowerTrack, all [recovery and redundancy
features](/en/docs/twitter-api/enterprise/powertrack-api/guides/powertrack_recovery_and_redundancy_features.html)
are configured within the enterprise contract. PowerTrack API currently
has the flexibility to offer multiple PowerTrack streams (commonly
\"dev\" and \"production\") with unique rulesets.  Currently, the
Twitter API v2 filtered stream is only available with a single stream.

PowerTrack allows you to connect to have multiple connections to a
single stream, generally used for redundant connections to different
data centers or clients. If you have [Academic Research
access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
, you will have access redundant connections, enabling you to make up to
two connections to a single stream.

If a PowerTrack stream is disconnected breifly, a reconnection can be
made using the [ backfillMinutes ]{.code-inline} parameter to reduce the
chance of data loss within five minutes of the disconection. While we
have added this functionality to the Twitter API v2 version, it is
currently only available with Academic Research access, and has been
renamed to [ backfill_minutes ]{.code-inline} .

If a PowerTrack stream is disconnected for longer than a 5 minute
period, the separate [Replay
API](/en/docs/twitter-api/enterprise/powertrack-api/api-reference/replay-stream.html)
can be used to recover data for up to a 2 hour period in the recent 5
day past.  Currently, the Twitter API v2 filtered stream does not have a
replay feature.

#### Request parameters and response format

One of the biggest differences between PowerTrack API and Twitter API v2
filtered stream is the parameter functionality.

Using the Twitter API v2 filtered stream, there are several parameters
used on the connection request to identify which fields or expanded
objects to return in the Tweet payload.  This is common for all v2
endpoints. By default, only the Tweet [ id ]{.code-inline} and [ text
]{.code-inline} are returned for matching Tweets but additional
parameters, fields and expansions described below, can be added in order
to recieve more detailed data per matching Tweet.

[
https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at,public_metrics,author_id,entities&expansions=attachments.poll_ids
]{.code-inline}

You can learn more about how to use fields and expansions by visiting
our
[guide](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
, and by reading through our broader [data
dictionary](/en/docs/twitter-api/data-dictionary/introduction) .

+-----------------------------------+-----------------------------------+
| **Connection to PowerTrack**      | **Example request to Twitter API  |
|                                   | v2 filtered stream**              |
+-----------------------------------+-----------------------------------+
|     curl --compressed -v -ue      |     curl "https://api.twitter     |
| xample@customer.com "https://gnip | .com/2/tweets/search/stream?tweet |
| -stream.twitter.com/stream/powert | .fields=attachments,author_id,con |
| rack/accounts/:account_name/publi | text_annotations,conversation_id, |
| shers/twitter/:stream_label.json" | created_at,entities,geo,id,in_rep |
|                                   | ly_to_user_id,lang,possibly_sensi |
|                                   | tive,public_metrics,referenced_tw |
|                                   | eets,reply_settings,source,text,w |
|                                   | ithheld&user.fields=created_at,de |
|                                   | scription,entities,id,location,na |
|                                   | me,pinned_tweet_id,profile_image_ |
|                                   | url,protected,public_metrics,url, |
|                                   | username,verified,withheld&expans |
|                                   | ions=author_id,referenced_tweets. |
|                                   | id,referenced_tweets.id.author_id |
|                                   | ,entities.mentions.username,attac |
|                                   | hments.poll_ids,attachments.media |
|                                   | _keys,in_reply_to_user_id,geo.pla |
|                                   | ce_id&place.fields=contained_with |
|                                   | in,country,country_code,full_name |
|                                   | ,geo,id,name,place_type&poll.fiel |
|                                   | ds=duration_minutes,end_datetime, |
|                                   | id,options,voting_status" -H "Aut |
|                                   | horization: Bearer $ACCESS_TOKEN" |
+-----------------------------------+-----------------------------------+

The PowerTrack API data format is set within console.gnip.com at the
stream settings level, which can be set to either the Twitter [native
enriched
format](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)
or [Activity streams
format](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/activity.html)
.

PowerTrack API only uses one optional parameter on connection, to
reconnect using backfill ( [ backfillMinutes=5 ]{.code-inline} ). This
optional parameter is also available to filtered stream, but is called
backfill_minutes, and is only available via Academic Research access.\

    https://gnip-stream.twitter.com/stream/powertrack/accounts/{account_name}/publishers/twitter/{stream_label}.json?backfillMinutes=5

#### Response structure and data format

As described above, the request parameters set at the connection request
for Twitter API v2 filtered stream determine the response data
returned.  There are several different response possibilites using
different fields and expansions which can range from the most simple
default response with only the Tweet id and text, to an extremely
detailed and expanded data payload.

The data format for PowerTrack is set within console.gnip.com at the
stream settings level, which can be set to either the Twitter Native
Enriched format or Activity Streams format.

The following table references Tweet response examples in each different
format:

If you would like to know more about how the enterprise data formats map
to the Twitter API v2 format, please visit our following guides:
:::
