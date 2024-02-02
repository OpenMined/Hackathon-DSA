::: is-table-default
Liking Tweets is one of the core features people use to engage in the
public conversation on  Twitter. With endpoints in our Likes lookup
endpoint group, you can see a list of accounts that have liked a given
Tweet, or which Tweets a given account has liked. You could use these
endpoints to understand what kind of content a specified account or
group of accounts likes.

### Likes lookup

With endpoints in the Likes lookup group, you can retrieve a list of
accounts that have liked a Tweet, or a list of Tweets that an account
has liked. These endpoints include:

-   Tweets liked by a user - GET /2/users/:id/liked_tweets
-   Users who have liked a Tweet - GET /2/tweets/:id/liking_users

You can authenticate these endpoints with either [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
or [OAuth 2.0 Bearer
Token](https://developer.twitter.com/en/docs/authentication/oauth-2-0) .
For the liked Tweets endpoints, pagination tokens will be provided for
paging through large sets of results.

The liking users endpoint limits you to a total of 100 liking accounts
per tweet for all time.  Additionally, the liked Tweets endpoint is also
subject to the monthly [Tweet cap](/en/docs/twitter-api/tweet-caps)
applied at the Project level.\

### Manage Likes

The manage Likes endpoints enable you to like or unlike a specified
Tweet on behalf of an authenticated account. For this endpoint group,
there are two methods available POST and DELETE. The POST method allows
you to like a Tweet, and the DELETE method will enable you to unlike a
Tweet.

Since you are making requests on behalf of a user, you must authenticate
these endpoints with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) and use the Access Tokens
associated with the user, which can be generated using the [3-legged
OAuth
flow](/content/developer-twitter/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
. You can like a Tweet from your account or an account of an
authenticated user. With both endpoints, there is a user rate limit of
50 requests per 15 minutes per endpoint.\

To access these endpoint, you must have an approved [developer
account](/en/docs/developer-portal/overview) . When authenticating, you
must use keys and tokens from a [developer App](/en/docs/apps) that is
located within a [Project](/en/docs/projects) .

Learn more about getting access to the Twitter API v2 endpoints in our
[getting started](/en/docs/twitter-api/getting-started) page.
:::
