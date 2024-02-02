::: is-table-default
This page contains information on several tools and key concepts that
you should be aware of as you integrate the Tweets lookup endpoints into
your system. We've broken the page into a couple of different sections:

### []{#helpful} Helpful tools

Before we dive into some key concepts that will help you integrate this
endpoint, we recommend that you become familiar with the following:

Postman

Postman is a great tool that you can use to test out an endpoint. Each
Postman request includes every path and body parameter to help you
quickly understand what is available to you. To learn more about our
Postman collections, please visit our [getting started with Postman
guide](/en/docs/tools-and-libraries/using-postman) .

Code samples

Interested in getting set up with this endpoint with some code in your
preferred coding language? We've got a handful of different code samples
available that you can use as a starting point on our [Github
page.](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[ Third-party libraries
](https://github.com/twitterdev/Twitter-API-v2-sample-code)

Take advantage of one of our communities' [third-party
libraries](/en/docs/twitter-api/tools-and-libraries) to help you get
started. You can find a library that works with the v2 endpoints by
looking for the proper version tag.\

### Key concepts

#### []{#authentication} Authentication

All Twitter API v2 endpoints require you to authenticate your requests
with a set of credentials, also known as keys and tokens. You can use
either OAuth 1.0a User Context, OAuth 2.0 App-Only, or OAuth 2.0
Authorization Code with PKCE to authenticate your requests to these
endpoints.

[OAuth 1.0a User Context](/en/docs/authentication/oauth-1-0a) requires
you to utilize your API Keys, user Access Tokens, and a handful of other
parameters to [create an authorization
header](/en/docs/authentication/oauth-1-0a/authorizing-a-request) ,
which you will then pass with your request. The Access Tokens must be
associated with the user that you are making the request on behalf of.
If you would like to generate a set of Access Tokens for another user,
they must authorize your App using the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens) .

Please note that OAuth 1.0a can be difficult to use. If you are not
familiar with this authentication method, we recommend that you use a
[library](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
, use a tool like Postman, or use OAuth 2.0 to authenticate your
requests. If you would like to request a Tweet or private metrics from
these endpoints, you will need to use a either OAuth 1.0a User Context
or OAuth 2.0 Authorization Code with PKCE, which will ensure that you
have the proper permissions from the user that owns that content.\

[OAuth 2.0 App-Only](/en/docs/authentication/oauth-2-0) just requires
that you pass an [OAuth 2.0 App Access
Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)
with your request. You can either generate an App Access Token from
directly within a developer App, or generate one using the [POST
oauth2/token](/en/docs/authentication/api-reference/token) endpoint.

[OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
allows for greater control over an application's scope, and
authorization flows across multiple devices. OAuth 2.0 allows you to
pick specific fine-grained scopes which give you specific permissions on
behalf of a user.

To enable OAuth 2.0 in your App, you must enable it in your's App's
authentication settings found in the App settings section of the
developer portal.
:::
