::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
In order to use v2 endpoints, you will need the following things:

Please note the importance of using keys and tokens from an App within a
Project. If you are using keys and tokens from an App outside of a
Project, you will not be able to make a request to v2 endpoints.

Once you have a developer account, you can set up all of the above in
the [developer portal](/en/portal) .
:::
:::

::: c01-rich-text-editor
::: is-table-default
With the new Twitter API, you'll use two different authentication
patterns, [OAuth 1.0a User Context](/en/docs/authentication/oauth-1-0a)
and [OAuth 2.0 Bearer Token](/en/docs/authentication/oauth-2-0) , to
access different endpoints. Each serves a different purpose when making
requests to the endpoints:

-   OAuth 1.0a User Context is required when making a request on behalf
    of a Twitter user
-   OAuth 2.0 Bearer token is required to make requests on behalf of
    your developer App

### Tools and Code

To help you get started and familiarize yourself with the new endpoints
and capabilities we have a few options to jump start your work:

First, we have a Twitter [Postman
collection](https://t.co/twitter-api-postman) that allows you to use the
Postman client to make requests of and connect to the individual
endpoints. This is a low friction way to test authentication and
experiment with the endpoints. It's important to note the Postman client
is best for RESTful endpoints, but you can copy requests to streaming
endpoints from the tool and paste them into your command line tool.

If you want to dig deeper, we've also provided a list of both Twitter
supported and third party libraries in Ruby, Python, Node, Java, and
many more. For additional context, take a look at our [tools and
libraries
page](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
.

### Migrating to updated endpoints

As you start to explore the new Twitter v2 endpoints, we've built a
series of detailed migration guides to help you compare and contrast
each updated endpoints\' capabilities compared to older versions:
:::
:::

::: c01-rich-text-editor
:::

::: c01-rich-text-editor
::: is-table-default
Those of you who have used the platform for some time will notice that
many of the new endpoints are aligned with existing [standard
v1.1](/en/docs/twitter-api/v1) , and
[enterprise](/en/docs/twitter-api/enterprise) endpoints. Indeed, we
intend for these to replace all three versions in the future.

We've put together a table to help you understand how the [Twitter API
endpoints map](/en/docs/twitter-api/migrate/twitter-api-endpoint-map) to
previous versions.

If you'd like to see what's coming next, please visit our [product
roadmap](https://trello.com/b/myf7rKwV/twitter-developer-platform-roadmap)
.

We also have a [changelog](/en/updates/changelog) that you can check out
to understand what we have already released.

### What should we build next?

As we build out additional capabilities of the Twitter API v2 we want to
continue to hear from you. We welcome and encourage
[feedback](https://twitterdevfeedback.uservoice.com/) from you.

Take a look at the ideas that have already been submitted, show your
support for those that correlate with your needs and provide feedback as
well!
:::
:::
:::
