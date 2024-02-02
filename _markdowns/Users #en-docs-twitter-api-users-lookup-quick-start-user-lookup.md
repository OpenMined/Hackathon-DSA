::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the GET /users/by endpoint.\

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so, this endpoint requires you to
authenticate your request with either [App
only](/en/docs/authentication/oauth-2-0/application-only) , [OAuth 2.0
Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , or [OAuth
1.0a User Context](/en/docs/authentication/oauth-1-0a) authentication
methods.

For simplicity\'s sake, we will utilize App only with this request, but
you will need to use one of the other authentication methods if you\'d
like to request private [metrics](/en/docs/twitter-api/metrics) or
users.

To utilize App only, you must add your keys and tokens, specifically the
[App Access Token](/en/docs/authentication/oauth-2-0/bearer-tokens)
(also known as the App only Bearer Token) to Postman. You can do this by
selecting the environment named "Twitter API v2" in the top-right corner
of Postman and adding your keys and tokens to the \"initial value\" and
\"current value\" fields (by clicking the eye icon next to the
environment dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.\

#### Step three: Identify and specify which user(s) you would like to retrieve

You must specify a user or a set of users that you would like to receive
within the request. Depending on which user endpoint you use, you can
pass either a user ID or a username. In this situation, we are going to
use the [GET /users/by
endpoint](/en/docs/twitter-api/users/lookup/api-reference/get-users-by)
which allows you to pass multiple usernames in a single request (rather
than the
[single-ID](/en/docs/twitter-api/users/lookup/api-reference/get-users-id)
, [multi-ID](/en/docs/twitter-api/users/lookup/api-reference/get-users)
, and
[single-username](/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username)
endpoints) and pass a set of usernames using the usernames query
parameter.

Usernames are simply the account handle that you can find within an
account\'s profile URL. For example, the following account's username is
[ twitterdev ]{.code-inline} .

` https://twitter.com/TwitterDev `

In Postman, navigate to the \"Params\" tab and enter this username, or a
string of usernames separated by a comma, into the \"Value\" column of
the [ username ]{.code-inline} parameter, making sure to not include any
spaces between usernames and commas.

  -------------- ------------------------------------------------
  **Key**        **Value**
  ` username `   [ twitterdev,twitterapi,adsapi ]{.code-inline}
  -------------- ------------------------------------------------

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default [user
object](/en/docs/twitter-api/data-dictionary/object-model/user) fields
in your response: [ id ]{.code-inline} , [ name ]{.code-inline} , and [
username ]{.code-inline} .

If you would like to receive additional fields beyond [ id
]{.code-inline} , [ name ]{.code-inline} , and [ username
]{.code-inline} , you will have to specify those fields in your request
with the [[ field
]{.code-inline}](/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields)
and/or [[ expansion
]{.code-inline}](/en/docs/twitter-api/data-dictionary/introduction/expansions)
parameters.

For this exercise, we will request a three additional sets of fields
from different objects:

1.  The additional [ user.created_at ]{.code-inline} field in the
    primary user objects.
2.  The associated pinned Tweets' object's default fields for the
    returned users: [ id ]{.code-inline} and [ text ]{.code-inline} .
3.  The additional [ tweet.created_at ]{.code-inline} field in the
    associated Tweet objects.\

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

  ------------------ ---------------- -----------------------------------------------------------
  **Key**            **Value**        **Returned fields**
  ` user.fields `    ` created_at `   ` user.created_at `
  ` expansions `     ` author_id `    [ tweet.id ]{.code-inline} , [ tweet.text ]{.code-inline}
  ` tweet.fields `   ` created_at `   ` includes.users.created_at `
  ------------------ ---------------- -----------------------------------------------------------

You should now see the following URL next to the \"Send\" button:
:::
