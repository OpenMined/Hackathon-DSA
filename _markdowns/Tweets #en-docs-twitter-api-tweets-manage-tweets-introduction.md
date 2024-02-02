::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Creating and deleting Tweets using the Twitter API is essential for
engaging with the public conversation. The new manage Tweets endpoints
allow you to do just that and much more.

We have two available methods for manage Tweets, POST and DELETE. The
POST method lets you post polls, quote Tweets, Tweet with reply
settings, Tweet with geo, Tweet with media and tag users, and Tweet to
Super Followers, in addition to other features. Likewise, the DELETE
method allows you to delete a specific Tweet. For the POST method, you
can pass in [the
parameters](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference)
you are looking for to enable you to further customize your request.

The \'delete Tweet\' method has been updated to support edited Tweets.
When any Tweet in a chain of Tweet edits is deleted, all Tweets in that
edit chain are also deleted. To learn more about Edit Tweet metadata,
check out the [Edit Tweets
fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/edit-tweets)
page.

There is a user rate limit of 200 requests per 15 minutes for the POST
method. The DELETE method has a rate limit of 50 requests per 15
minutes. Additionally, there is a limit of 300 requests per 3 hours,
including Tweets created with either manage Tweets or manage Retweets.

Since you are making requests on behalf of a user with the manage Tweets
endpoints, you must authenticate with either [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) ,
and use a user Access Tokens associated with a user that has authorized
your App. To generate this user Access Token with OAuth 1.0a, you can
use the [3-legged OAuth
flow](/en/docs/authentication/oauth-2-0/bearer-tokens) . To generate a
user Access Token with OAuth 2.0, you can use the [Authorization Code
with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) .
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: ct01-columns
:::
:::
:::
:::
:::
:::
:::
