::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Retweeting is one of the core features people use to engage in the
public conversation on Twitter. With the Retweets lookup endpoints, you
can see a list of accounts that Retweeted a given Tweet. In addition,
the new manage Retweets endpoints allow you to Retweet a Tweet or undo a
Retweet.
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: c01-rich-text-editor
::: is-table-default
With the Retweets lookup endpoint, you can retrieve a list of accounts
that have Retweeted a Tweet. For this endpoint, pagination tokens will
be provided for paging through large sets of results in batches of up to
100 users.

You can authenticate these endpoints with either [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
, or [OAuth 2.0 Authorization Code with
PKCE](https://aem-staging.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/authorization-code.html)
.

### Manage Retweets

The manage Retweets endpoints enable you to Retweet or undo a Retweet of
a specified Tweet on behalf of an authenticated account. For this
endpoint group, there are two methods available POST and DELETE. The
POST method allows you to Retweet a Tweet, and the DELETE method will
enable you to undo a Retweet of a given Tweet.

Since you are making requests on behalf of a user, you must authenticate
these endpoints with either [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , and
utilize the user Access Tokens associated with the user you are making
the request on behalf of. You can generate this user Access Token using
the [3-legged OAuth
flow](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
(OAuth 1.0a) or using the [Authorization Code with PKCE grant
flow](/en/docs/authentication/oauth-2-0/user-access-token) (OAuth 2.0).
You can Retweet a Tweet from your account or an account of an
authenticated user. With both endpoints, there is a user rate limit of
50 requests per 15 minutes per endpoint.
:::
:::
:::
