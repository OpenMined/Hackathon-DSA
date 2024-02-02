::: is-table-default
If you have been working with the standard v1.1 [GET
favorites/list](/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list)
endpoint, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 Likes lookup endpoints.

With v2, we've also introduced a new liked users endpoint which allows
you to get information about a Tweet's liking users.

-   **Similarities**
    -   Authentiation
    -   Rate limits
-   **Differences**
    -    Endpoint URLs \
    -    Request limitations
    -    App and Project requirements \
    -   Response data format
    -   Request parameters

### Similarities

####   **Authentication**  

Both the standard v1.1 and Twitter API v2 Likes lookup endpoints use
[OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Bearer
Token](/content/developer-twitter/en/docs/basics/authentication/overview/application-only)
. Therefore, if you were previously using the [GET favorites/list
endpoints](/content/developer-twitter/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/get-favorites-list)
standard v1.1 endpoints, you can continue using the same authentication
method if you migrate to the Twitter API v2 version if you wish.

Depending on your authentication library/package of choice, Bearer Token
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate a Bearer Token,
see [this OAuth 2.0 Bearer Token
guide](/content/developer-twitter/en/docs/basics/authentication/overview/application-only)
.\

**Rate limits**

The standard v1.1 GET favorites/list endpoint has a 75 requests per 15
minutes per user rate limit. The corresponding liked Tweets endpoint in
v2 also has this same rate limit. However, this v2 endpoint also has an
additional rate limit of 75 requests per 15 minutes per App.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ GET https://api.twitter.com/1.1/favorites/list.json\
        ]{.code-inline} (list of Tweets which are by the specified user)
    -   There is no v1.1 equivalent to the v2 liking users endpoint
-   Twitter API v2 endpoint:
    -   [ GET https://api.twitter.com/2/users/:id/liked_tweets\
        ]{.code-inline} (list of Tweets which are liked by the specified
        user ID)
    -   [ GET https://api.twitter.com/2/tweets/:id/liking_users
        ]{.code-inline}\
        (list of users who liked the specified Tweet ID)

#### Request limitations

The v2 liked Tweets endpoint allows you to request 5 to 100 Tweets per
request, but you can request all likes of a Tweet using pagination
tokens. The v1.1 GET favorites/list endpoint also allows you to pull all
likes of Tweets, but you can pull from 20 to 200 Tweets per request.

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

The following standard v1.1 request parameters accepted two request
query parameters ( [ user_id ]{.code-inline} or [ screen_name
]{.code-inline} ). The Twitter API v2 only accepts the numerical user
ID, and it must be passed as part of the endpoint path.
:::
