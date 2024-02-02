::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This page contains information on several tools and key concepts that
you should be aware of as you integrate the Retweet endpoints into your
system. We've broken the page into a couple of different sections:

### []{#helpful} Helpful tools

Before we dive into some key concepts that will help you integrate this
endpoint, we recommend that you become familiar with:

#### Postman

Postman is a great tool that you can use to test out an endpoint. Each
Postman request includes every path and body parameter to help you
quickly understand what is available to you. To learn more about our
Postman collections, please visit our [\"Using
Postman\"](/en/docs/tools-and-libraries/using-postman) page.

#### Code samples

Interested in getting set up with this endpoint with some code in your
preferred coding language? We've got a handful of different code samples
available that you can use as a starting point on our [Github
page](https://github.com/twitterdev/Twitter-API-v2-sample-code) .

#### Third-party libraries

Take advantage of one of our communities' [third-party
libraries](/en/docs/twitter-api/tools-and-libraries) to help you get
started. You can find a library that works with the v2 endpoints by
looking for the proper version tag.\

### Key concepts

#### []{#authentication} Authentication

All Twitter API v2 endpoints require for you to authenticate your
requests with a set of credentials, also known as keys and tokens.

You can use either OAuth 1.0a User Context or OAuth 2.0 Bearer Token to
authenticate your requests to the Retweets lookup endpoint.

The manage Retweets endpoints require the use of OAuth 1.0a User
Context, which means that you must use a set of API keys and user access
tokens to make a successful request. The access tokens must be
associated with the user that you are making the request on behalf of.
If you would like to generate a set of access tokens for another user,
they must authorize or authenticate your App using the 3-legged OAuth
flow.

Please note that OAuth 1.0a can be tricky to use. If you are not
familiar with this authentication method, we recommend that you use a
[library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
to properly authenticate your requests.
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note**

If you are requesting the following fields, OAuth 1.0a User Context is
required:

-   [ tweet.fields.non_public_metrics ]{.code-inline}
-    [ tweet.fields.promoted_metrics ]{.code-inline}
-    [ tweet.fields.organic_metrics ]{.code-inline}
-    [ media.fields.non_public_metrics ]{.code-inline}
-    [ media.fields.promoted_metrics ]{.code-inline}
-   [ media.fields.organic_metrics ]{.code-inline}
:::
:::
:::
:::
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
limits](https://developer-staging.twitter.com/en/docs/twitter-api/rate-limits)
are placed on each endpoint that limits the number of requests that you
can make on behalf of your app or on behalf of an authenticated user.

The manage Retweets endpoints are limited to 50 requests per 15 min (per
user). Additionally, for the POST endpoint, you are limited to 300
requests per 3-hour window (per user, per app).

With the Retweets lookup endpoint, you are limited to 75 requests per
15-min window.

#### []{#fields} Fields and expansions

The Twitter API v2 allows users to select exactly which data they want
to return from the API using a set of tools called fields and
expansions. The [ expansion ]{.code-inline} parameter allows you to
expand objects referenced in the payload. For example, this endpoint
allows you to pull the following
[expansions](/en/docs/twitter-api/expansions) :

-   [ attachments.poll_ids ]{.code-inline}
-   [ attachments.media_keys ]{.code-inline}
-   [ author_id, entities.mentions.username ]{.code-inline}
-   [ geo.place_id ]{.code-inline}
-   [ in_reply_to_user_id, ]{.code-inline}
-   [ referenced_tweets.id, ]{.code-inline}
-   [ referenced_tweets.id.author_id ]{.code-inline}

\
The [ fields ]{.code-inline} parameter allows you to select exactly
which [fields](/en/docs/twitter-api/fields) within the different data
objects you would like to receive. These endpoints delivers Tweet
objects primarily. By default, the Tweet object returns the [ id
]{.code-inline} and [ text ]{.code-inline} fields. To receive additional
fields such as [ tweet.created_at ]{.code-inline} or [ tweet.entities
]{.code-inline} , you will have to specifically request those using a [
fields ]{.code-inline} parameter. Some important fields that you may
want to consider using in your integration are our poll data, metrics,
Tweet annotations, and conversation ID fields.

We've added a guide on how to [use fields and
expansions](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
together to our [Twitter API v2 data
dictionary](/en/docs/twitter-api/data-dictionary/introduction) .

#### []{#pageination} Pagination 

This endpoint utilizes pagination so that responses are returned
quickly. In cases where there are more results than what can be sent in
a single response (up to 100 users) you will need to paginate. Use the
` max_results ` parameter to identify how many results will return per
page, and the ` pagination_token ` parameter to return the next page of
results. You can learn more by reviewing our [pagination
guide](https://developer.twitter.com/en/docs/twitter-api/pagination) .
:::
:::
:::
