::: is-table-default
If you have been working with the standard v1.1 [v1.1 GET
statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id)
, [v1.1 GET
statuses/retweets/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)
, the goal of this guide is to help you understand the similarities and
differences between the standard v1.1 and Twitter API v2 Retweets lookup
endpoints.

-   **Similarities**
    -   Authentiation
    -   Users per request limits
-   **Differences**
    -    Endpoint URLs \
    -    Request limitations
    -    App and Project requirements \
    -   Response data format
    -   Request parameters

### Similarities

####   **Authentication**  

Both the standard v1.1 and Twitter API v2 Retweets lookup endpoints (
[v1.1 GET
statuses/retweets/:id](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweets-id)
and [v1.1 GET
statuses/retweeters/:ids](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-statuses-retweeters-ids)
) use [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
or OAuth 2.0 Bearer Token.

**Users per request limits**

For both v1.1 and v2 GET endpoints the max number of users that will be
returned by the Retweets lookup endpoint is 100 users per page. For the
v2 Retweets lookup endpoint, you can use pagination tokens to page
through large results.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/statuses/retweets/:id.json\
        ]{.code-inline} (Returns a collection of the 100 most recent
        Retweets of the Tweet specified by the ` id ` parameter)
    -   ` https://api.twitter.com/1.1/statuses/retweeters/ids.json `\
        (Returns a collection of up to 100 user IDs belonging to users
        who have Retweeted the Tweet specified by the ` id ` parameter)
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/tweets/:id/retweeted_by\
        ]{.code-inline} (Returns a list of accounts who have Retweeted a
        given Tweet)

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](/content/developer-twitter/en/docs/apps) that is
associated with a [Project](/content/developer-twitter/en/docs/projects)
when authenticating your requests. All Twitter API v1.1 endpoints can
use credentials from standalone Apps or Apps associated with a project.

#### Response data format

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by
default, and then have the option to use parameters to identify which
fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the user [ id ]{.code-inline} ,
[ name ]{.code-inline} , and [ username ]{.code-inline} fields by
default. To request any additional fields or objects, you wil need to
use the
[fields](/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields)
and
[expansions](/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions)
parameters. Any user fields that you request from this endpoint will
return in the primary user object. Any expanded Tweet object and fields
will return in an [ includes ]{.code-inline} object within your
response. You can then match any expanded objects back to the user
object by matching the IDs located in both the user and the expanded
Tweet object.

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

The following standard v1.1 request parameters accepted two request
query parameters ( [ user_id ]{.code-inline} or [ screen_name
]{.code-inline} ). The Twitter API v2 only accepts the numerical user
ID, and it must be passed as part of the endpoint path.
:::
