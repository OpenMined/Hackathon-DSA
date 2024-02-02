::: is-table-default
This guide will walk you through some steps that you could follow to
make your first request. This is a great resource to help you once
you've signed up for a Twitter account.

If you are interested in using code samples, more technical guides, or a
graphical tool like Postman, please consider using the following guides
to make your first request:

This guide assumes that you have collected your [API key and
secret](/en/docs/authentication/oauth-1-0a/api-key-and-secret) , [user
Access Token and
Secret](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
, [App Access Token](/en/docs/authentication/oauth-2-0/bearer-tokens) ,
and have stored them in a secure location. You can learn how to do this
by following the steps in the [getting access to the Twitter
API](/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
guide.\

### Step 1. Identify which endpoint you would like to use

The Twitter API allows you to perform a variety of different actions
using code that you might be able to perform on the Twitter website or
mobile application.

We have a complete list of the endpoints that are available via the API
listed within our [API Reference Index](/en/docs/api-reference-index) ,
but we recommend sticking to one of the following for simplicity's sake:

-   [Manage Tweets \> Post a
    Tweet](/en/docs/twitter-api/tweets/manage-tweets)
-   [Search Tweets](/en/docs/twitter-api/tweets/search)
-   [User lookup](/en/docs/twitter-api/users/lookup)\

### Step 2. Choose a tool to make your request

While some requests can be straightforward, others can be tricky to
build. That's why the amazing community of developers have developed
tools to abstract away some of the complexity.

The following are some recommended tools and details on how to use them:

#### Postman

Postman is a visual tool that you can use to make requests to REST
endpoints. We've created some great materials around Postman to help you
get started with and explore the different endpoints available via the
Twitter API.

We recommend you read through our [\"Getting started with Postman\"
tutorial](/en/docs/tutorials/postman-getting-started) to learn how to
add your keys and tokens and make your first request.

We've also produced a quick start guide for each of our Twitter API v2
endpoints, most of which use Postman. You can find these guides in each
respective endpoint section, but here is a link to a few:

-   Quick start: Post a Tweet
-   Quick start: Search for Tweets
-   Quick start: Lookup a user\

Please note that you can't make requests to streaming endpoints using
Postman. Please visit the [filtered
stream](/en/docs/twitter-api/tweets/filtered-stream/quick-start) or [1%
ampled
stream](/en/docs/twitter-api/tweets/volume-streams/quick-start/sampled-stream)
quick start guide to learn how to work with those endpoints.

If you prefer a more simple graphical tool, you should also consider
using [Insomnia](https://insomnia.rest) .\

#### Sample code

If you are interested in using some simple code to make your request,
we've put together sample code in multiple different languages for each
of our Twitter API v2 endpoints.

You can find the code samples via our Github repo,
[Twitter-API-v2-sample-code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
, which also contains a README file that you can use to learn how to set
up your credentials to properly work with the requests.

For example, here is a cURL example for the user lookup endpoint. All
you have to do to use this request is replace the \$ACCESS_TOKEN and
\$USERNAME with your [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) and Twitter
handle. Then, copy and paste this code into your command line tool and
press 'Return' or 'Enter'.
:::
