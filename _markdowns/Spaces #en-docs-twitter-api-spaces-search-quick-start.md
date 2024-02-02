::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
search Spaces endpoint with a set of specified fields using Postman.

If you would like to see sample code in different programming languages,
please visit our [Twitter API v2 sample code GitHub
repository](https://github.com/twitterdev/Twitter-API-v2-sample-code) .\
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
To complete this guide, you will need to have a set of [keys and
tokens](/en/docs/authentication) to authenticate your request. You can
generate these keys and tokens by following these steps:

-   [Sign up for a developer account](/en/apply-for-access) and receive
    approval.
-   Create a [Project](/en/docs/projects) and an associated [developer
    App](/en/docs/apps) in the developer portal.
-   Navigate to your App\'s "Keys and tokens" page to generate the
    required credentials. Make sure to save all credentials in a secure
    location.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Step one: Start with a tool or library**\

There are several different tools, code examples, and libraries that you
can use to make a request to this endpoint, but we are going to use the
Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please
click on the following button:
:::
:::

::: b03-button-v3
[](https://t.co/twitter-api-postman){.chirp-btn .twtr-spacing--mb-500
.chirp-btn--primary .chirp-btn--icon .chirp-btn--icon-end
.twtr-scribe-clicks}

::: chirp-btn__icon
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/m1_vnext/carat.svg){.chirp-btn__icon--img}
:::

Add Twitter API v2 to Postman
:::

::: c01-rich-text-editor
::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the Spaces folder and find the \"Search Spaces\" request.\

**Step two: Authenticate your request**

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so, this endpoint requires you to
authenticate your request with either [OAuth 2.0
App-Only](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/application-only.html)
or [OAuth 2.0 Authorization Code with
PKCE](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/authorization-code.html)
authentication methods.

For simplicity\'s sake, we will utilize OAuth 2.0 App-Only with this
request, but you will need to use one of the other authentication
methods if you\'d like to request private
[metrics](https://aem.twitter.biz/content/developer-twitter/en/docs/twitter-api/metrics.html)
or Spaces from a private user.

To utilize OAuth 2.0 App-Only, you must add your keys and tokens,
specifically the [App Access
Token](https://aem.twitter.biz/content/developer-twitter/en/docs/authentication/oauth-2-0/bearer-tokens.html)
(also known as the App-only Bearer Token) to Postman. You can do this by
selecting the environment named "Twitter API v2" in the top-right corner
of Postman and adding your keys and tokens to the \"initial value\" and
\"current value\" fields (by clicking the eye icon next to the
environment dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.\

**Step three: create a search query**

This endpoint accepts text as a search query. Unlike other search
endpoints, it does not accept operators, grouping, and logical
operators. For this exercise, we will use "hello" as a simple query.

In Postman, navigate to the \"Params\" tab and enter this user ID into
the \"Value\" column of the id parameter.

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
ID of the Spaces and its state, which are the only Space object fields
returned by default in your response.

If you would like to receive additional fields, you will have to specify
them in your request with the space.fields or expansions parameters.

For this exercise, we will requested three additional sets of fields
from different objects:

-   The additional title field in the primary Spaces object.
-   The full user object of the specified creator ID
-   The additional user.created_at field in the associated user object.

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
https://api.twitter.com/2/spaces/search?query=hello&space.fields=creator_id&expansions=creator_id&user.fields=created_at
]{.code-inline}
:::
:::

::: c01-rich-text-editor
::: is-table-default
**Step five: Make your request and review your response**

Once you have everything set up, hit the "Send" button and you will
receive the following response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
   "data": [
    {
        "creator_id": "2244994945",
        "id": "1zqKVXPQhvZJB",
        "title": "Hello world 👋",
        "state": "Running"
   },
   "includes": {
       "users": [
           {
               "created_at": "2013-12-14T04:35:55.000Z",
               "name": "Twitter Dev",
               "id": "2244994945",
               "username": "TwitterDev"
           }
       ]
   }
]
}

    
```
:::
:::
:::

::: ct01-columns
:::
:::
