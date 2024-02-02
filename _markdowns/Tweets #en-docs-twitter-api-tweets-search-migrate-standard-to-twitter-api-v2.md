::: is-table-default
If you have been working with the v1.1
[search/tweets](/en/docs/twitter-api/v1/tweets/search/overview) , the
goal of this guide is to help you understand the similarities and
differences between the standard and Twitter API v2 search Tweets
endpoint.

-   **Similarities**
    -   OAuth 1.0a User Context and OAuth 2.0 App-Only
    -   Support for Tweet edit history and metadata.
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirements
    -   Response data format
    -   Request parameters
    -    New query operators \
    -   AND / OR operator precedence

### Similarities

#### OAuth 1.0a User Context and OAuth 2.0 App-Only authentication

The v1.1 search/tweets and the Twitter API v2 recent search endpoint
support both [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) and [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0) .

Therefore, if you were previously using the standard v1.1 search
endpoint you can continue using the same authentication method if you
migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App-Only
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate an App Access
Token see this [OAuth 2.0 App-Only
guide](/en/docs/basics/authentication/overview/application-only) .

If you would like to take advantage of the ability to pull private or
advertising metrics with the Twitter API v2 endpoint, you will need to
use OAuth 1.0a User Context, and pass the user access tokens related to
the user who posted the Tweet for which you would like to pull metrics.

\
**Support for Tweet edit history and metadata**

Both versions provide metadata that describes any edit history. Check
out the [search API
References](/en/docs/twitter-api/tweets/search/api-reference) and the
[Tweet edits fundamentals page](/en/docs/twitter-api/tweet-edits) for
more details.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/search/tweets ]{.code-inline}
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets/search/recent\
        ]{.code-inline}

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/en/docs/apps) that is associated to a
[Project](/en/docs/projects) when authenticating your requests. All
Twitter API v1.1 endpoints can use credentials from standalone Apps or
Apps associated with a Project.

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by
default, and then have the option to use parameters to identify which
fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet [ id ]{.code-inline}
and [ text ]{.code-inline} fields by default. To request any additional
fields or objects, you will need to use the
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
    payload. Tweet and user attributes are only included if they have
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

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  Standard search v1.1                             Search Tweets v2
  ------------------------------------------------ -----------------------------------
  q                                                query
                                                   start_time (YYYY-MM-DDTHH:mm:ssZ)
  until (YYYY-MM-DD)                               end_time (YYYY-MM-DDTHH:mm:ssZ)
  since_id                                         since_id
  max_id                                           until_id
  count                                            max_results
  Response provides search_metadata.next_results   next_token

\
There are also a set of standard search Tweets request parameters
**not** supported in Twitter API v2: \

  **Standard v1.1 parameter**          **Details**
  ------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------
  [ geocode ]{.code-inline}            Search Tweets at the Basic Access level does not support geo operators.
  [ locale ]{.code-inline}             With standard search, this was used to specify the language of the query but never fully implemented.
  [ lang ]{.code-inline}               Search Tweets endpoints provide a [ lang ]{.code-inline} query operator for matching on languages of interest.
  [ include_entities ]{.code-inline}   Tweet entities are always included.
  [ result_type ]{.code-inline}        Search Tweets endpoints deliver all matching Tweets, regardless of engagement level.
  [ extended ]{.code-inline}           Twitter API v2 is built from the ground up to support Tweets with up to 280 characters. With v2, there is no concept of \'extended\' Tweets.

\
Here is an example request that shows the difference between a Standard
request and a Search Tweets request:

  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------
  **Standard v1.1**                                                                  **Twitter API v2**
  [ https://api.twitter.com/1.1/search/tweets.json?q=snow&count=50 ]{.code-inline}   [ https://api.twitter.com/2/tweets/search/recent?query=snow&max_results=50 ]{.code-inline}
  ---------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------

\
These requests will both return the 50 most recent Tweets that contain
the keyword [ snow. ]{.code-inline} The v2 request will return the
default [ id ]{.code-inline} and [ text ]{.code-inline} fields of the
matching Tweets. Here is an example of specifying additional Tweet and
user fields to include in the JSON payload:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Twitter API v2**
  [ https://api.twitter.com/2/tweets/search/recent?query=snow&max_results=50&tweet.fields=id,created_at,author_id,text,source,entities,attachments&user.fields=id,name,username,description ]{.code-inline}
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### ** New query operators** 

Search Tweets introduces new operators in support of two new Twitter API
v2 features:

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
    -   [ context: ]{.code-inline} matches on Tweets that have been
        annotated with a context of interest.
    -   [ entity: ]{.code-inline} matches on Tweets that have been
        annotated with an entity of interest.

#### AND / OR operator precedence

The basic building block for building search queries is the use of OR
and AND logical groupings. The standard search API applies ORs before
ANDs, while Search Tweets endpoints (as well as the premium and
enterprise versions) applies ANDs before ORs. This difference is
critical when translating queries between the two.

For example, with standard search, if you wanted to match Tweets with
the keyword 'storm' that mention the word 'colorado' or the #COwx
hashtag, you could do that with the following search query:

[ storm #COwx OR colorado ]{.code-inline}

With the Search Tweets operator precedence, ANDs are applied before ORs.
So the above query is equivalent to:

[ (storm #COwx) OR colorado ]{.code-inline}

However, the above rule would match on any Tweets that mentions
'Colorado', regardless if the Tweet mentions 'storm' or the #COwx
hashtag. In addition it would also  match Tweets that mentioned both the
keyword 'storm' and the #COwx hashtag.

To make the query behave as originally intended, the OR clauses need to
be grouped together. The translation of the original standard query to
Search Tweets would be:

[ storm (#COwx OR colorado) ]{.code-inline}

These two rules have very different matching behavior. For the month of
October 2019, the original rule matches over 1,175,000 Tweets while the
correctly translated rule matches around 5,600 Tweets. Be sure to mind
your ANDs and ORs, and use parentheses where needed.
:::
