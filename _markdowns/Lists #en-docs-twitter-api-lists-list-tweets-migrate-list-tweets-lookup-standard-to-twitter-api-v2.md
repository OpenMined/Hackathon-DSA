::: is-table-default
If you have been working with the standard v1.1 [GET
lists/statuses](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/get-lists-statuses)
endpoint, the goal of this guide is to help you understand the
similarities and differences between the standard v1.1 and Twitter API
v2 endpoints.

-   **Similarities**
    -   Authentication methods
    -   Rate limits
-   **Differences**
    -    Endpoint URLs
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
Tweets lookup endpoints, you can continue using the same authentication
method if you migrate to the Twitter API v2 version.

Depending on your authentication library/package of choice, App only
authentication is probably the easiest way to get started and can be set
with a simple request header. To learn how to generate an App only
Access Token, see [this App only
guide](https://developer.twitter.com/en/docs/basics/authentication/overview/application-only)
.

**Rate limits**

+-----------------------------------+-----------------------------------+
| **Standard v1.1**                 | **Twitter API v2**                |
+-----------------------------------+-----------------------------------+
| [ /1.1/lists/statuses.json        | [ /2/lists/:id/tweets             |
| ]{.code-inline}                   | ]{.code-inline}                   |
|                                   |                                   |
| 900 requests per 15-minute window | 900 requests per 15-minute window |
| with OAuth 1.0a User Context      | with OAuth 1.0a User Context      |
|                                   |                                   |
| 900 requests per 15-minute window | 900 requests per 15-minute window |
| with App only                     | with OAuth 2.0 Authorization Code |
|                                   | with PKCE                         |
|                                   |                                   |
|                                   | 900 requests per 15-minute window |
|                                   | with App only                     |
+-----------------------------------+-----------------------------------+

#### 

### Differences

#### Endpoint URLs

-   Standard v1.1 endpoints:
    -   [ GET https://api.twitter.com/1.1/lists/statuses.json\
        ]{.code-inline} (Lookup Tweets from a specified List)
-   Twitter API v2 endpoint:
    -   [ GET https://api.twitter.com/2/lists/:id/tweets\
        ]{.code-inline} (Lookup Tweets from a specified List)

#### 

#### App and Project requirements

The Twitter API v2 endpoints require that you use credentials from a
[developer App](https://developer.twitter.com/en/docs/apps) that is
associated with a
[Project](https://developer.twitter.com/en/docs/projects) when
authenticating your requests. All Twitter API v1.1 endpoints can use
credentials from standalone Apps or Apps associated with a project.

#### 

Data objects per request limits

The standard v1.1 [ /lists/statuses ]{.code-inline} endpoint allows you
to return up to 5000 Tweets per request. The new v2 endpoints allow you
to return up to 100 Tweets per request. By default, 100 user objects
will be returned, to change the number of results you will need to pass
a query parameter [ max_results= ]{.code-inline} with a number between
1-100; you can then pass the [ next_token ]{.code-inline} returned in
the response payload to the [ pagination_token ]{.code-inline} query
parameter in your next request.

**Response data format**

One of the biggest differences between standard v1.1 and Twitter API v2
endpoint versions is how you select which fields return in your payload.

For the standard endpoints, you receive many of the response fields by
default and then have the option to use parameters to identify which
additional fields or sets of fields should return in the payload.

The Twitter API v2 version only delivers the Tweet [ id ]{.code-inline}
and [ text ]{.code-inline} fields by default. To request any additional
fields or objects, you will need to use the
[fields](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/fields)
and
[expansions](https://developer.twitter.com/en/docs/twitter-api/fields/content/developer-twitter/en/docs/twitter-api/expansions)
parameters. Any Tweet fields that you request from this endpoint will
return in the primary Tweet object. Any expanded object fields will
return an [ includes ]{.code-inline} object within your response. You
can then match any expanded objects back to the primary Tweet object by
matching the IDs from the primary object and in expanded objects.

Here are examples of possible Tweet fields and expansions:

-   [ attachments ]{.code-inline}

-   [ author_id ]{.code-inline}

-   [ context_annotations ]{.code-inline}

-   [ created_at ]{.code-inline}

-   [ geo ]{.code-inline}

-   [ lang ]{.code-inline}

  --------------------------------------- -----------------------------
  **Endpoint**                            **Expansion**
  [ /2/lists/:id/tweets ]{.code-inline}   [ author_id ]{.code-inline}
  --------------------------------------- -----------------------------

We encourage you to read more about these new parameters in their
respective guides, or by reading our guide on [how to use fields and
expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
.

We have also put together a [data format migration
guide](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2)
that can help you map standard v1.1 fields to the newer v2 fields. This
guide will also provide you the specific expansion and field parameter
that you will need to pass with your v2 request to return specific
fields.

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

-   [ ]{.code-inline} Twitter is adopting the convention that JSON
    values with no value (for example, [ null ]{.code-inline} ) are not
    written to the payload. Tweet and user attributes are only included
    if they have non-null values.\

#### Request parameters

The following standard v1.1 request parameters have equivalents in
Twitter API v2:

+-----------------------------------+-----------------------------------+
| Standard v1.1                     | Twitter API v2                    |
+-----------------------------------+-----------------------------------+
| [ list_id ]{.code-inline}         | [ id ]{.code-inline}              |
+-----------------------------------+-----------------------------------+
| [ slug ]{.code-inline}            | No equivalent                     |
+-----------------------------------+-----------------------------------+
| [ owner_screen_name               | No equivalent                     |
| ]{.code-inline}                   |                                   |
+-----------------------------------+-----------------------------------+
| [ owner_id ]{.code-inline}        | Requested with [ expansions       |
|                                   | ]{.code-inline} parameter with    |
| \                                 | value of [ author_id              |
|                                   | ]{.code-inline}                   |
+-----------------------------------+-----------------------------------+
| [ since_id ]{.code-inline}        | No equivalent                     |
+-----------------------------------+-----------------------------------+
| [ max_id ]{.code-inline}          | No equivalent                     |
+-----------------------------------+-----------------------------------+
| [ include_entities                | Requested with [ tweet.fields     |
| ]{.code-inline}                   | ]{.code-inline} parameter with    |
|                                   | value of [ entities               |
|                                   | ]{.code-inline}                   |
+-----------------------------------+-----------------------------------+
| [ include_rts ]{.code-inline}     | No equivalent                     |
+-----------------------------------+-----------------------------------+
| [ count ]{.code-inline}           | [ max_results ]{.code-inline}     |
+-----------------------------------+-----------------------------------+
:::
