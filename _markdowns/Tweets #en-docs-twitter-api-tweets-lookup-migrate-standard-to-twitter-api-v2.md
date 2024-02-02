::: is-table-default
If you have been working with the standard v1.1 GET statuses/show and
GET statuses/lookup, the goal of this guide is to help you understand
the similarities and differences between the standard and Twitter API v2
Tweets lookup endpoints..

You may also be interested in our [visual data format migration
tool](/en/docs/twitter-api/migrate/data-formats/visual-data-format-migration-tool)
to help you quickly see the differences between the [Twitter API v1.1
data
format](/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json)
and the [Twitter API v2
format](/en/docs/twitter-api/data-dictionary/introduction) .

-   **Similarities**
    -   OAuth 1.0a User Context
    -   Tweets per request limits
    -   Support for Tweet edit history and metadata
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirements
    -   Response data format
    -   Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports [OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a) ,
while the new Twitter API v2 Tweet lookup endpoint supports both OAuth
1.0a User Context and [OAuth 2.0
App-Only](/content/developer-twitter/en/docs/authentication/oauth-2-0) .
Therefore, if you were previously using one of the standard v1.1 Tweet
lookup endpoints, you can continue using the same authentication method
if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App-Only
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate an App Access
Token, see [this OAuth 2.0 App-only
guide](/en/docs/basics/authentication/overview/application-only) .\

#### Tweets per request limits

The v1.1 [GET
statuses/lookup](/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-lookup)
endpoint allows you to specify 100 Tweets per request. This also goes
for the GET /tweets endpoint. To specify a full 100 Tweets, you will
need to pass the ids parameter as a query parameter rather than a path
parameter and include the list of [Tweet
IDs](/content/developer-twitter/en/docs/twitter-ids) in a
comma-separated list.\

**Support for Tweet edit history and metadata**\

Both versions provide metadata that describes any edit history. Check
out the [Tweet lookup API
References](/en/docs/twitter-api/tweets/lookup/api-reference) and the
[Edit Tweets fundamentals page](/en/docs/twitter-api/edit-tweets) for
more details.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/statuses/show ]{.code-inline}
    -   [ https://api.twitter.com/1.1/statuses/lookup ]{.code-inline}
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets ]{.code-inline}
    -   [ https://api.twitter.com/2/tweets/:id ]{.code-inline}

#### 

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

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  ---------------------- -----------------------
  **Standard**           **Twitter API v2**
  [ id ]{.code-inline}   [ ids ]{.code-inline}
  ---------------------- -----------------------

There are also a set of standard v1.1 Tweet lookup request parameters
**not** supported in Twitter API v2:

+-----------------------------------+-----------------------------------+
| Standard                          | Comment                           |
+===================================+===================================+
| [ tweet_mode ]{.code-inline}      | This parameter enables developers |
|                                   | to request a series of different  |
|                                   | extended fields that had been     |
|                                   | introduced in the years since     |
|                                   | statuses/show and statuses/lookup |
|                                   | were introduced. It has been      |
|                                   | replaced with the fields and      |
|                                   | expansions functionality.         |
+-----------------------------------+-----------------------------------+
| [ trim_user ]{.code-inline}       | This parameter is used to reduce  |
|                                   | the number of fields that deliver |
|                                   | in the user object that comes     |
|                                   | alongside each Tweet. It has been |
|                                   | replaced with the additive fields |
|                                   | and expansions functionality.\    |
|                                   | To request user information       |
|                                   | alongside your requested Tweet,   |
|                                   | you will need to use a            |
|                                   | combination of the [ author_id    |
|                                   | ]{.code-inline} expansion and the |
|                                   | [ user.fields ]{.code-inline}     |
|                                   | parameter with a set of specified |
|                                   | [user                             |
|                                   | fields](/en/docs/twitter-api/d    |
|                                   | ata-dictionary/object-model/user) |
|                                   | .                                 |
+-----------------------------------+-----------------------------------+
| [ include_my_retweet              | This parameter includes the ID of |
| ]{.code-inline}                   | the source Tweet for those        |
|                                   | specified Tweets that were        |
|                                   | Retweeted by the authenticating   |
|                                   | user.                             |
+-----------------------------------+-----------------------------------+
| [ include_entities                | This parameter is used to remove  |
| ]{.code-inline}                   | the entities node from the Tweet  |
|                                   | payload. It has been replaced     |
|                                   | with the additive fields and      |
|                                   | expansions functionality.         |
+-----------------------------------+-----------------------------------+
| [ include_ext_alt_text            | This parameter adds an additional |
| ]{.code-inline}                   | [ ext_alt_text ]{.code-inline}    |
|                                   | field in the media entity if that |
|                                   | media has alt text attached to    |
|                                   | it.\                              |
+-----------------------------------+-----------------------------------+
| [ include_card_uri                | This parameters adds a [ card_uri |
| ]{.code-inline}                   | ]{.code-inline} attribute when    |
|                                   | there is an ads card attached.\   |
+-----------------------------------+-----------------------------------+
| [ map ]{.code-inline}             | This parameter would return the   |
|                                   | Tweet ID and nullified fields for |
|                                   | unavailable Tweets.               |
|                                   |                                   |
|                                   | In v2, we return the Tweet ID and |
|                                   | a detailed error message for      |
|                                   | unavailable Tweets.               |
+-----------------------------------+-----------------------------------+
:::
