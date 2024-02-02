::: is-table-default
There are two authentication methods available with the Engagement API:
[OAuth
1.0a](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth1.0a)
and [OAuth 2.0 Bearer
Token](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth2.0)
.

**OAuth 2.0 Bearer Token** (also referred to as "application-only")
allows you to access publicly available engagement metrics. This
authentication method can be used to get total counts for Favorites (aka
Likes), Retweets, Quote Tweets, Replies, and video views for any
publicly available Tweets when making requests to the [/totals
endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#Totals)
.

**OAuth 1.0a** (also referred to as "user context") allows you to make
requests on behalf of a user and access private engagement metrics that
belong to the user in question.

This authentication method is required for:

-   All requests sent to the [/28hr
    endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#api-28hr)
    and [/historical
    endpoint](https://developer.twitter.com/en/docs/twitter-api/enterprise/engagement-api/api-reference/post-insights-engagement#Historical)
-   Accessing any of the following private metrics: Impressions,
    Engagements, Media Views, Media Engagements, URL Clicks, Hashtag
    Clicks, Detail Expands, Permalink Clicks, App Install Attempts, App
    Opens, Email Tweet, User Follows, and User Profile Clicks

When sending a request with OAuth 1.0a, you need to include the Access
Tokens (Access Token and Secret) of the user who owns the Tweet or
protected resource of interest. If you do not provide the correct user
Access Tokens when requesting protected user data, the Engagement API
will return a ` 403 Forbidden ` error.

The Engagement API will not allow you to fetch engagement data for
[protected
Tweets](https://help.twitter.com/en/safety-and-security/public-and-protected-tweets)
, even if you are authenticating on behalf of the user who owns these
Tweets. Attempting to do so will return a ` 400 Bad Request ` error,
with the message ` "Tweet ID(s) are unavailable" ` .

If you are sending a request on behalf of your own Twitter account (in
other words, the account that owns the developer App), you can generate
the required Access Tokens directly from within the [developer
portal](https://developer.twitter.com/en/portal/projects-and-apps) ,
under the "Keys and tokens" tab for the developer App.

If you are making a request on behalf of any other user, you will need
to use the 3-legged OAuth flow to obtain the required Access Tokens. The
following documentation contains more information on how to do this:
[OAuth 1.0a: how to obtain a user's access
tokens](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/oauth1-0a-and-user-access-tokens)
.

For additional examples, including how to authenticate using OAuth 1.0a,
check out [TwitterDev's sample Python code for the Engagement
API](https://github.com/twitterdev/enterprise-scripts-python/tree/master/Engagement-API)
.
:::
