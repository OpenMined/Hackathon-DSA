::: is-table-default
If you have been working with the v1.1
[statuses/filter](/en/docs/twitter-api/v1/tweets/filter-realtime/api-reference/post-statuses-filter)
endpoint, this guide can help you understand the similarities and
differences between the standard and Twitter API v2 filtered stream
endpoints.

-   **Similarities**
    -   Request parameters and operators
    -   Support for Tweet edit history and metadata
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirement
    -   Authentication method
    -   Rule volume and persistent stream
    -   Response data format
    -   Request parameters
    -   Availability of recovery and redundancy features
    -    Query operators

### Similarities

#### Request parameters and operators

The standard v1.1 statuses/filter endpoint features a few parameters
that can be passed along with the request to filter the stream. With v2
filtered stream, you instead use a set of
[operators](/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule)
that can be connected together using boolean logic to filter for desired
Tweets. The available operators include some that are direct
replacements for the existing standard v1.1 parameters.

The following standard v1.1 request parameters have equivalent operators
in Twitter API v2:\

+-----------------------------------+-----------------------------------+
| **Standard**                      | **Twitter API v2**                |
+===================================+===================================+
| [ follow ]{.code-inline} - A      | Many operators that can help you  |
| comma-separated list of user IDs, | find Tweets related to specific   |
| indicating the users whose Tweets | users:                            |
| should be delivered on the        |                                   |
| stream.                           |                                   |
+-----------------------------------+-----------------------------------+
| [ track ]{.code-inline} - A       | Many operators that can help you  |
| comma-separated list of phrases   | find Tweets related to specific   |
| which will be used to determine   | keywords:                         |
| what Tweets will be delivered on  |                                   |
| the stream.                       | -   [ keyword ]{.code-inline}     |
|                                   | -   [ \"exact phrase match\"      |
|                                   |     ]{.code-inline}               |
|                                   | -   [ \# ]{.code-inline}          |
|                                   | -   etc.\                         |
+-----------------------------------+-----------------------------------+

**Support for Tweet edit history and metadata**\

Both versions provide metadata that describes any edit history. Check
out the [filtered stream API
References](/en/docs/twitter-api/tweets/filtered-stream/api-reference)
and the [Tweet edits fundamentals
page](/en/docs/twitter-api/tweet-edits) for more details.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://stream.twitter.com/1.1/statuses/filter.json
        ]{.code-inline}
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets/search/stream ]{.code-inline}
    -   [ https://api.twitter.com/2/tweets/search/stream/rule
        ]{.code-inline}

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/en/docs/apps) that is associated to a
[Project](/en/docs/project) when authenticating your requests. All
Twitter API v1.1 endpoints can use credentials from standalone Apps or
Apps associated with a Project.

#### Authentication method

The standard endpoint supports [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) , whereas the Twitter API
v2 filtered stream endpoints supports [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0) (also referred to as
Application-only authentication). To make requests to the Twitter API v2
version you must use a App Access Token to authenticate your requests.

If you no longer have the App Access Token that was presented to you
when you created your Project and app in the developer portal, you can
generate a new one by navigating to your app\'s "Keys and tokens" page
on the developer portal. If you'd like to generate an App Access Token
programmatically, see this [OAuth 2.0 App-Only
guide](/en/docs/authentication/oauth-2-0/application-only) .

#### Rule volume and persistent stream

The standard v1.1 endpoint supports a single rule to filter the
streaming connection. To change the rule, you have to disconnect the
stream and submit a new request with the revised filtering rules
submitted as parameters.

The Twitter API v2 filtered stream endpoint allows you to apply multiple
rules to a single stream and add and remove rules to your stream while
maintaining the stream connection.

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by
default, and then have the option to use parameters to identify which
fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet [ id ]{.code-inline}
and [ text ]{.code-inline} fields by default. To request any additional
fields or objects, you wil need to use the
[fields](/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields)
and
[expansions](/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions)
parameters. Any Tweet fields that you request from these endpoints will
return in the primary Tweet object. Any expanded user, media, poll, or
place objects and fields will return in an [ includes ]{.code-inline}
object within your response. You can then match any expanded objects
back to the Tweet object by matching the IDs located in both the Tweet
and the expanded object.

We encourage you to read more about these new parameters in their
respective guides, or by reading our guide on [how to use fields and
expansions](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
.

We have also put together a [data format migration
guide](/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2)
which can help you map standard v1.1 fields to the newer v2 fields. This
guide will also provide you the specific expansion and field parameter
that you will need to pass with your v2 request to return specific
fields.\

In addition to the changes in how you request certain fields, Twitter
API v2 is also introducing new JSON designs for the objects returned by
the APIs, including
[Tweet](/en/docs/twitter-api/data-dictionary/object-model/tweet) and
[user](/en/docs/twitter-api/data-dictionary/object-model/user) objects.

-   At the JSON root level, the standard endpoints return Tweet objects
    in a [ statuses ]{.code-inline} array, while Twitter API v2 returns
    a [ data ]{.code-inline} array.
-   Instead of referring to Retweeted and Quoted \"statuses\", Twitter
    API v2 JSON refers to Retweeted and Quoted Tweets. Many legacy and
    deprecated fields, such as [ contributors ]{.code-inline} and [
    user.translator_type ]{.code-inline} are being removed.
-   Instead of using both [ favorites ]{.code-inline} (in Tweet object)
    and [ favourites ]{.code-inline} (in user object), Twitter API v2
    uses the term [ like ]{.code-inline} .
-   Twitter is adopting the convention that JSON values with no value
    (for example, [ null ]{.code-inline} ) are not written to the
    payload. Tweet and user attributes are only included if they have a
    non-null values.\

We also introduced a new set of fields to the [Tweet
object](/en/docs/twitter-api/data-dictionary/object-model/tweet)
including the following:

-   A [ [conversation_id](/en/docs/twitter-api/conversation-id)
    ]{.code-inline} field
-   Two new [annotations](/en/docs/twitter-api/annotations) fields,
    including [ context ]{.code-inline} and [ entities ]{.code-inline}
-   Several new [metrics](/en/docs/twitter-api/metrics) fields
-   A new [ reply_setting ]{.code-inline} field, which shows you who can
    reply to a given Tweet

#### Request parameters

There are also a set of standard filtered stream request parameters
**not** supported in Twitter API v2: \

+-----------------------------------+-----------------------------------+
| Standard v1.1 parameter           | Details                           |
+===================================+===================================+
| [ locations ]{.code-inline} - A   | We have not released              |
| comma-separated list of           | location-based operators for      |
| longitude,latitude pairs          | Twitter API v2 yet.               |
| specifying a set of bounding      |                                   |
| boxes to filter Tweets by.        |                                   |
+-----------------------------------+-----------------------------------+
| [ Delimited ]{.code-inline}       | With the v1.1 endpoint, setting   |
|                                   | this to the string length         |
|                                   | indicates that statuses should be |
|                                   | delimited in the stream, so that  |
|                                   | clients know how many bytes to    |
|                                   | read before the end of the status |
|                                   | message.                          |
|                                   |                                   |
|                                   | This functionality is not         |
|                                   | available with Twitter API v2.    |
+-----------------------------------+-----------------------------------+
| [ Stall_warnings ]{.code-inline}  | With the v1.1 endpoint, setting   |
|                                   | this parameter to true will cause |
|                                   | periodic messages to be delivered |
|                                   | if the client is in danger of     |
|                                   | being disconnected.               |
|                                   |                                   |
|                                   | With Twitter API v2, stall        |
|                                   | warnings are sent by default with |
|                                   | the new line sent every so often. |
+-----------------------------------+-----------------------------------+

####  Availability of recovery and redundancy features

The Twitter API v2 version of filtered stream introduces recovery and
redundancy features that can help you maximize streaming up-time as well
as recover any Tweets that might have been missed due to a disconnection
that lasted five minutes or less.

Redundant connections allows you to connect to a given stream up to two
times, which can help ensure that you maintain a connection to the
stream at all times, even if one of your connections fails.

The [ backfill_minutes ]{.code-inline} parameter can be used to recover
up to five minutes of missed data.

Both of these features are only available via [Academic Research
access](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
. You can learn more about this functionality via our [recovery and
redundancy
features](/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features)
integration guide.

#### New query operators

Twitter API v2 introduces new operators in support of two new features:

-   **[Conversation IDs](/en/docs/twitter-api/conversation-id)** - As
    conversations unfold on Twitter, a conservation ID will be available
    to mark Tweets that are part of the conversation. All Tweets in the
    conversation will have their conversation_id set to the Tweet ID
    that started it.
-   **[Twitter Annotations](/en/docs/twitter-api/annotations)** provide
    contextual information about Tweets, and include entity and context
    annotations. Entities are comprised of people, places, products and
    organizations. Contexts are domains, or topics, that surfaced
    entities are a part of. For example, people mentioned in a Tweet may
    have a context that indicates whether they are an athlete, actor, or
    politician.
    -   [ context: ]{.code-inline} - matches on Tweets that have been
        annotated with a context of interest.
    -   [ entity: ]{.code-inline} - matches on Tweets that have been
        annotated with an entity of interest.
:::
