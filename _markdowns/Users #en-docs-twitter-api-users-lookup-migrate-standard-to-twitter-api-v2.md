::: is-table-default
If you have been working with the standard v1.1 GET users/show and GET
users/lookup, the goal of this guide is to help you understand the
similarities and differences between the standard and Twitter API v2
users lookup endpoints.

-   **Similarities**
    -   OAuth 1.0a User Context
    -   Users per request limits
-   **Differences**
    -   Endpoint URLs
    -   App and Project requirements
    -   Response data format
    -   Request parameters

### Similarities

#### OAuth 1.0a User Context authentication method

The standard endpoint supports [OAuth 1.0a User
Context](/content/developer-twitter/en/docs/authentication/oauth-1-0a) ,
while the new Twitter API v2 users lookup endpoints supports both OAuth
1.0a User Context and [OAuth 2.0 Bearer
Token](/content/developer-twitter/en/docs/authentication/oauth-2-0) .
Therefore, if you were previously using one of the standard v1.1 users
lookup endpoints, you can continue using the same authentication method
if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, Bearer Token
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate a Bearer Token,
see [this OAuth 2.0 Bearer Token
guide](/content/developer-twitter/en/docs/basics/authentication/overview/application-only)
.

#### Users per request limits

The standard v1.1 GET users/lookup endpoint allows you to specify 100
users per request. This also goes for the GET /users and GET /users/by
endpoints. To specify a full 100 users, you will need to pass the [ ids
]{.code-inline} (GET /users) parameter or the [ username ]{.code-inline}
(GET /users/by) parameter as a query parameter, and include the list of
user IDs/usernames in a comma-separated list.\

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ https://api.twitter.com/1.1/users/show ]{.code-inline}
        (single-ID or username lookup)
    -   [ https://api.twitter.com/1.1/users/lookup ]{.code-inline}
        (multi-ID or username lookup)
-   Twitter API v2 endpoint:
    -   [ https://api.twitter.com/2/users ]{.code-inline} (multi-ID
        lookup)
    -   [ https://api.twitter.com/2/users/:id ]{.code-inline} (single-ID
        lookup)
    -   [ https://api.twitter.com/2/users/by ]{.code-inline}
        (multi-username lookup)
    -   [ https://api.twitter.com/2/users/by/username/:username
        ]{.code-inline} (single-username lookup)

The Twitter API v2 endpoints require that you use credentials from a
[developer
App](https://aem-staging.twitter.biz/content/developer-twitter/en/docs/apps.html)
that is associated to a
[Project](https://aem-staging.twitter.biz/content/developer-twitter/en/docs/projects.html)
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

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

  ------------------------------- ----------------------------
  **Standard**                    **Twitter API v2**
  [ user_id ]{.code-inline}       [ ids ]{.code-inline}
  [ screen_name ]{.code-inline}   [ username ]{.code-inline}
  ------------------------------- ----------------------------

\
There are also a set of standard users lookup request parameters **not**
supported in Twitter API v2: \

  Standard                             Comment
  ------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [ include_entities ]{.code-inline}   This parameter is used to remove the entities node from the Tweet payload.  It has been replaced with the additive [ fields ]{.code-inline} and [ expansions ]{.code-inline} functionality.
:::
