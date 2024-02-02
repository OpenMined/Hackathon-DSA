::: is-table-default
The recent search endpoint allows you to programmatically access
filtered public Tweets posted over the last week, and is available to
all developers who have a developer account and are using keys and
tokens from an [App](/en/docs/apps) within a
[Project](/en/docs/projects) .

You can authenticate your requests with [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) , [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) , or
[OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) . However,
if you would like to receive private metrics, or a breakdown of organic
and promoted metrics within your Tweet results, you will have to
use OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE,
and pass user Access Tokens that are associated with the user that
published the given content.

This endpoint can deliver up to 100 Tweets per request in
reverse-chronological order, and
[pagination](/en/docs/twitter-api/tweets/search/integrate/paginate)
tokens are provided for paging through large sets of matching Tweets.

When using a Project with regular access, you can use the basic set of
[operators](/en/docs/twitter-api/tweets/search/integrate/build-a-rule)
and can make queries up to 512 characters long. When using a Project
with Enterprise access, you have access to additional operators.
Projects with Enterprise Access can make queries up to 4096 characters
long.

Learn more about [access
levels](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
.

### Full-archive search

The v2 full-archive search endpoint is only available to Projects with
[Enteprise](/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-level)
access. The endpoint allows you to programmatically access public Tweets
from the complete archive dating back to the first Tweet in March 2006,
based on your search query.

You can authenticate your requests to this endpoint using [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) , and the
[App Access Token](/en/docs/authentication/oauth-2-0/bearer-tokens) must
come from an App that is within a Project that has Enterprise access.
Since you cannot make a request on behalf of other users (OAuth 1.0a
User Context or OAuth 2.0 Authorization Code with PKCE) with this
endpoint, you will not be able to pull private
[metrics](/en/docs/twitter-api/metrics) .

This endpoint can deliver up to 500 Tweets per request in
reverse-chronological order, and
[pagination](/en/docs/twitter-api/tweets/search/integrate/paginate)
tokens are provided for paging through large sets of matching Tweets.

**Note:** If requesting
[annotations](/en/docs/twitter-api/annotations/overview.html) through
the [ tweet.fields ]{.code-inline} parameter, the [ max_results
]{.code-inline} parameter is currently limited to a max value of 100.
This may change in the future, but please be mindful of this limitation.

Since this endpoint is only available to those that have been approved
for Enterprise access, you have access to the full set of search
[operators](/en/docs/twitter-api/tweets/search/integrate/build-a-rule)
and can make queries up to 1024 characters long.
:::
