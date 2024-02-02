::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the Spaces folder and find the \"Lookup Spaces created by one or more
users\" request.\

**Step two: Authenticate your request**

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so, this endpoint requires you to
authenticate your request with either [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) or [OAuth
2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code)
authentication methods.

For simplicity\'s sake, we will utilize OAuth 2.0 App-Only with this
request, but you will need to use one of the other authentication
methods if you\'d like to request private
[metrics](/en/docs/twitter-api/metrics) or Spaces from a private user.

To utilize OAuth 2.0 App-Only, you must add your keys and tokens,
specifically the [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as
the App-only Bearer Token) to Postman. You can do this by selecting the
environment named "Twitter API v2" in the top-right corner of Postman
and adding your keys and tokens to the \"initial value\" and \"current
value\" fields (by clicking the eye icon next to the environment
dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.\

**Step three: Identify and specify which user from which you would like
to retrieve Tweets**

You must specify a user you would like to retrieve live or upcoming
Spaces for within the request. In this example, we will be passing a
single user ID.

User IDs are simply the numerical value that represents an account
handle that you can find within an account\'s profile URL. For example,
the following account's username is TwitterDev.

[ https://twitter.com/TwitterDev ]{.code-inline}

To convert this username to the user ID, you will have to use the user
lookup endpoint with the username and find the numerical user ID in the
payload. In the case of \@TwitterDev, the user ID is 2244994945.

In Postman, navigate to the \"Params\" tab and enter this user ID into
the \"Value\" column of the [ id ]{.code-inline} parameter.

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive an
id, which is the only [Space
object](/en/docs/twitter-api/data-dictionary/object-model/space) field
returned by default in your response.

If you would like to receive additional fields, you will have to specify
them in your request with the [ space.fields ]{.code-inline} or [
expansions ]{.code-inline} parameters.

For this exercise, we will requested three additional sets of fields
from different objects:

-   The additional [ title ]{.code-inline} field in the primary Spaces
    object.
-   The full [user
    object](/en/docs/twitter-api/data-dictionary/object-model/user) of
    the specified creator ID
-   The additional [ user.created_at ]{.code-inline} field in the
    associated user object.

In Postman, navigate to the "Params" tab and add the following key:value
pair to the "Query Params" table:

  -------------------------------- ------------------------------ -----------------------------------------------------------------------------------
  **Key**                          **Value**                      **Returned fields**
  [ space.fields ]{.code-inline}   [ title ]{.code-inline}        [ creator_id ]{.code-inline}
  [ expansions ]{.code-inline}     [ creator_id ]{.code-inline}   [ includes.users.id, includes.users.name, includes.users.username ]{.code-inline}
  [ user.fields ]{.code-inline}    [ created_at ]{.code-inline}   [ includes.users.created_at ]{.code-inline}
  -------------------------------- ------------------------------ -----------------------------------------------------------------------------------

You should now see the following URL next to the "Send" button:

[
https://api.twitter.com/2/spaces/by/creator_ids?user_ids=2244994945&space.fields=creator_id&expansions=creator_id&user.fields=created_at
]{.code-inline}
:::
