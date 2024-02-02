::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This page contains information on several tools and key concepts that
you should be aware of as you integrate the mutes endpoints into your
system. We've broken the page into a couple of different sections:

### Helpful tools {#helpful}

Before we dive into some key concepts that will help you integrate this
endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each
Postman request includes every path and body parameter to help you
quickly understand what is available to you. To learn more about our
Postman collections, please visit our [\"Using
Postman\"](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman)
page.

#### Code samples

Interested in getting set up with this endpoint with some code in your
preferred coding language? We've got a handful of different code samples
available that you can use as a starting point on our [Github
page](https://github.com/twitterdev/Twitter-API-v2-sample-code) .

#### Third-party libraries

Take advantage of one of our communities' [third-party
libraries](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
to help you get started. You can find a library that works with the v2
endpoints by looking for the proper version tag.

### Key concepts

#### Authentication

All Twitter API v2 endpoints require you to authenticate your requests
with a set of credentials, also known as keys and tokens. You can use
OAuth 1.0a User Context to authenticate your requests to this endpoint.

[OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, which means that you must use a set of API Keys and user Access Tokens
to make a successful request. The access tokens must be associated with
the user that you are making the request on behalf of. If you would like
to generate a set of Access Tokens for another user, they must authorize
your App using the [3-legged OAuth
flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
.

Please note that OAuth 1.0a can be difficult to use. If you are not
familiar with this authentication method, we recommend that you use a
[library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
, use a tool like Postman.
:::
:::

::: c01-rich-text-editor
::: is-table-default
To retrieve a set of authentication credentials that will work with the
Twitter API v2 endpoints, you must [sign up for a developer
account](https://developer.twitter.com/en/portal/petition/essential/basic-info)
, set up a [Project](/en/docs/projects) within that account, and created
a [developer App](/en/docs/apps) within that Project. You can then find
your keys and tokens within your developer App.\

#### []{#limits} Rate limits

Every day, many thousands of developers make requests to the Twitter
API. To help manage the sheer volume of these requests, [rate
limits](/content/developer-twitter/en/docs/twitter-api/rate-limits) are
placed on each endpoint that limits the number of requests you can make
on behalf of your app or on behalf of an authenticated user.

These endpoints are rate limited at the user level, meaning that the
authenticated user that you are making the request on behalf of can only
call the endpoint a certain number of times across any developer App.

The chart below shows the rate limits for each endpoint.

  ------------------------------------------------------ ----------------- ----------------------------
  **Endpoint**                                           **HTTP method**   **Rate limit**
  [ /2/users/:id/pinned_lists ]{.code-inline}            POST              50 requests per 15 minutes
  [ /2/users/:id/pinned_lists/:list_id ]{.code-inline}   DELETE            50 requests per 15 minutes
  [ /2/users/:id/pinned_lists ]{.code-inline}            GET               15 requests per 15 minutes
  ------------------------------------------------------ ----------------- ----------------------------

#### Fields and expansions {#fields}

The Twitter API v2 GET endpoint allows users to select exactly which
data they want to return from the API using a set of tools called
` fields ` and ` expansions ` . The ` expansions ` parameter allows you
to expand objects referenced in the payload. For example, looking up
pinned Lists allows you to pull the following
[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions)
:

The ` fields ` parameter allows you to select exactly which
[fields](https://developer.twitter.com/en/docs/twitter-api/fields)
within the different data objects you would like to receive. This
endpoint delivers user objects primarily. By default, the List object
returns the ` id ` , and ` name ` fields. To receive additional fields
such as ` list.created_at ` or ` list.description ` , you will have to
specifically request those using a fields parameter.

We've added a guide on using [fields and
expansions](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
together to our [Twitter API v2 data
dictionary](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction)
.

The chart below shows the field and expansions available for the lookup
endpoint:

+-----------------------+-----------------------+-----------------------+
| **Endpoint**          | **Fields**            | **Expansions**        |
+-----------------------+-----------------------+-----------------------+
| [                     | ` list.fields `       | ` owner_id `          |
| /2/u                  |                       |                       |
| sers/:id/pinned_lists | ` user.fields `       |                       |
| ]{.code-inline}       |                       |                       |
+-----------------------+-----------------------+-----------------------+
:::
:::
:::
:::
:::
:::
:::
:::
