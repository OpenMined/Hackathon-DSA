::: is-table-default
If you have been working with the standard v1.1 [GET
lists/members](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-members)
and [GET
lists/memberships](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-memberships)
endpoints, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 List member endpoints.

-   **Similarities**
-   **Differences**
    -    Endpoint URLs
    -   Rate limits
    -   App and Project requirements
    -   Data objects per request limits
    -   Response data formats
    -   Request parameters

### Similarities

####   **Authentication**  

Both endpoint versions support both [OAuth 1.0a User
Context](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-1-0a)
and [App
only](https://developer.twitter.com/content/developer-twitter/en/docs/authentication/oauth-2-0)
. Therefore, if you were previously using one of the standard v1.1 List
members endpoints, you can continue using the same authentication method
if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate an App only
Access Token, see [this App only
guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)
.

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ GET https://api.twitter.com/1.1/lists/members.json\
        ]{.code-inline} (Lookup members of a specified List)
    -   [ GET https://api.twitter.com/1.1/lists/memberships.json\
        ]{.code-inline} (Lookup Lists a user is a member of)
-   Twitter API v2 endpoint:
    -   [ GET https://api.twitter.com/2/lists/:id/members\
        ]{.code-inline} (Lookup members of a specified List)\
    -   [ GET https://api.twitter.com/2/users/:id/list_memberships\
        ]{.code-inline} (Lookup Lists a user is a member of)

#### 

**Rate limits**

+-----------------------------------+-----------------------------------+
| **Standard v1.1**                 | **Twitter API v2**                |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/members.json         | [ /2/lists/:id/members            |
| ]{.code-inline}                   | ]{.code-inline}                   |
|                                   |                                   |
| 900 requests per 15-minute window | 900 requests per 15-minute window |
| with OAuth 1.0a User Context      | with OAuth 1.0a User Context      |
|                                   |                                   |
| 15 requests per 15-minute window  | 900 requests per 15-minute window |
| with App only                     | with OAuth 2.0 Authorization Code |
|                                   | with PKCE                         |
|                                   |                                   |
|                                   | 900 requests per 15-minute window |
|                                   | with App only                     |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/memberships.json     | [ /2/users/:id/list_memberships   |
| ]{.code-inline}                   | ]{.code-inline}                   |
|                                   |                                   |
| 15 requests per 15-minute window  | 15 requests per 15-minute window  |
| with OAuth 1.0a User Context      | with OAuth 1.0a User Context      |
|                                   |                                   |
| 15 requests per 15-minute window  | 15 requests per 15-minute window  |
| with App only                     | with OAuth 2.0 Authorization Code |
|                                   | with PKCE                         |
|                                   |                                   |
|                                   | 15 requests per 15-minute window  |
|                                   | with App only                     |
+-----------------------------------+-----------------------------------+

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer.twitter.com/en/docs/apps) that is
associated with a
[Project](https://developer.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps associated with a project.

#### 

Data objects per request limits

The standard v1.1 [ /1.1/lists/members ]{.code-inline} endpoint allows
you to return up to 5000 users per request. The new v2 endpoints allow
you to return up to 100 users per request. By default, 100 user objects
will be returned, to change the number of results you will need to pass
a query parameter [ max_results= ]{.code-inline} with a number between
1-100; you can then pass the [ next_token ]{.code-inline} returned in
the response payload to the [ pagination_token ]{.code-inline} query
parameter in your next request.

Additionally, the endpoint [ /1.1/lists/memberships ]{.code-inline} ,
allow you to return up to 1000 Lists per request. With the v2
replacement, the endpoint allows up to 100 Lists per request. By default
100 Lists objects are returned, use the query parameters [ max_results=
]{.code-inline} and [ pagination_token ]{.code-inline} in the same
fashion as [ /1.1/lists/members ]{.code-inline} to change the number of
results.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by
default and then have the option to use parameters to identify which
additional fields or sets of fields should return in the payload.

The Twitter API v2 version [ /users/:id/list_memberships ]{.code-inline}
will deliver the List [ id ]{.code-inline} and [ name ]{.code-inline}
fields by default. To request any additional fields or objects, you will
need to use the
[fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields)
and
[expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions)
parameters. Any List fields that you request from this endpoint will
return in the primary List object. Any expanded object and fields will
return an [ includes ]{.code-inline} object within your response. You
can then match any expanded objects back to the primary List object by
matching the IDs located in both the primary and the expanded object.

Here are examples of possible List fields and expansions:

-   [ created_at ]{.code-inline}

-   [ follower_count ]{.code-inline}

-   [ member_count ]{.code-inline}

-   [ owner_id ]{.code-inline}

-   [ description ]{.code-inline}

-   [ private ]{.code-inline}

  ------------------------------------------------- -----------------------------------
  **Endpoint**                                      **Expansion**
  [ /2/lists/:id/members ]{.code-inline}            [ pinned_tweet_id ]{.code-inline}
  [ /2/users/:id/list_memberships ]{.code-inline}   [ owner_id ]{.code-inline}
  ------------------------------------------------- -----------------------------------

We encourage you to read more about these new parameters in their
respective guides, or by reading our guide on [how to use fields and
expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
.

We have also put together a [data format migration
guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2)
that can help you map standard v1.1 fields to the newer v2 fields. This
guide will also provide you with the specific expansion and field
parameter that you will need to pass with your v2 request to return
specific fields.

In addition to the changes in how you request certain fields, Twitter
API v2 is also introducing new JSON designs for the objects returned by
the APIs, including
[Tweet](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)
and
[user](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
objects.

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
    non-null values.

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

**List members lookup**

  ------------------------------------- ------------------------------------
  **Standard v1.1**                     **Twitter API v2**
  [ list_id ]{.code-inline}             [ id ]{.code-inline}
  [ slug ]{.code-inline}                No equivalent
  [ owner_screen_name ]{.code-inline}   No equivalent
  [ owner_id ]{.code-inline}            No equivalent
  [ count ]{.code-inline}               [ max_results ]{.code-inline}
  [ cursor ]{.code-inline}              [ pagination_token ]{.code-inline}
  [ include_entities ]{.code-inline}    No equivalent
  [ skip_status ]{.code-inline}         No equivalent
  ------------------------------------- ------------------------------------

**List membership lookup**

  ------------------------------- ------------------------------------
  **Standard v1.1**               **Twitter API v2**
  [ user_id ]{.code-inline}       [ id ]{.code-inline}
  [ screen_name ]{.code-inline}   No equivalent
  [ count ]{.code-inline}         [ max_results ]{.code-inline}
  [ cursor ]{.code-inline}        [ pagination_token ]{.code-inline}
  ------------------------------- ------------------------------------
:::
