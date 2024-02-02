::: is-table-default
If you have been working with the standard v1.1 [GET
blocks/ids](/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-ids)
and [GET
blocks/list](/content/developer-twitter/en/docs/twitter-api/v1/accounts-and-users/mute-block-report-users/api-reference/get-blocks-list)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 blocks lookup endpoints.

-   **Similarities**
-   **Differences**
    -    Endpoint URLs \
    -   Users per request limits
    -   App and Project requirements
    -   Response data formats
    -   Request parameters

### Similarities

####   **Authentication**  

Both the standard v1.1 and Twitter API v2 blocks lookup endpoints use
[OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a) .
Therefore, if you were previously using one of the standard v1.1 blocks
lookup endpoints, you can continue using the same authentication method
if you migrate to the Twitter API v2 version.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ GET https://api.twitter.com/1.1/blocks/ids.json\
        ]{.code-inline} (list of user IDs who are blocked by the
        specified user)
    -   [ GET https://api.twitter.com/1.1/blocks/lists.json\
        ]{.code-inline} (list of users who are blocked by the specified
        user)
-   Twitter API v2 endpoint:
    -   [ GET https://api.twitter.com/2/users/:id/blocking\
        ]{.code-inline} (list of users who are blocked by the specified
        user ID)\

#### Users per request limits

The standard v1.1 endpoints allow you to return up to 5000 users per
request. The new v2 endpoints allow you to return up to 1000 users per
request. To return a full 1000 users, you will need to pass [
max_results=1000 ]{.code-inline} as a query parameter; you can then pass
the [ next_token ]{.code-inline} returned in the response payload to the
[ pagination_token ]{.code-inline} query parameter in your next
request.\

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
