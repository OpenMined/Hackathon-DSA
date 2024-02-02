::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the List
lookup endpoint using Postman.

Please visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository if you want to see sample code in different languages.

**Note:** For this example, we will make a request to the *List lookup
by ID* endpoint, but you can apply the learnings from this quick start
to other lookup requests as well.
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
There are several different tools, code examples, and libraries that you
can use to make a request to this endpoint, but we will use the Postman
tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment,
please click on the following button:
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
to the "List" folder, select another folder "List lookup", and then
choose \"List by ID\".\

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do this with this endpoint, you must
authenticate your request with either [App
only](/en/docs/authentication/oauth-2-0/application-only) , [OAuth 2.0
Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , or [OAuth
1.0a User Context](/en/docs/authentication/oauth-1-0a) authentication
methods.

For simplicity\'s sake, we are going to utilize App only with this
request, but if you\'d like to request private
[metrics](/en/docs/twitter-api/metrics) or Lists, you will need to use
one of the other authentication methods.

To utilize App only, you must add your keys and tokens (specifically the
[App only Access Token](/en/docs/authentication/oauth-2-0/bearer-tokens)
) to Postman by selecting the environment named "Twitter API v2" (in the
top-right corner of Postman), and adding your keys and tokens to the
\"initial value\" and \"current value\" fields (by clicking the eye icon
next to the environment dropdown).

If you\'ve done this correctly, these variables will automatically be
pulled into the request\'s authorization tab.\

#### Step three: Identify and specify which List you would like to retrieve

You must specify a List that you would like to receive within the
request. You can find the List ID by navigating to twitter.com and
clicking on a List and then looking in the URL. For example, the
following URL\'s List ID is [ 84839422 ]{.code-inline} .

[ https://twitter.com/i/lists/84839422 ]{.code-inline}

The target ID can be any valid List ID. In Postman, navigate to the
\"Params\" tab, and enter your ID into the \"Value\" column of the [ id
]{.code-inline} path variable. Be sure not to include any spaces before
or after any ID.

  ---------------------- ------------------------------------------
  **Key**                **Value**
  [ id ]{.code-inline}   [ 84839422 ]{.code-inline} (The List ID)
  ---------------------- ------------------------------------------

\
Step four: Identify and specify which fields you would like to retrieve
\

If you click the \"Send\" button after step three, you will receive the
default [List
object](/en/docs/twitter-api/data-dictionary/object-model/lists) fields
in your response: [ id ]{.code-inline} , [ name ]{.code-inline} .

If you would like to receive additional fields, you will have to specify
those fields in your request with [ list.fields ]{.code-inline} and/or
[[ expansion
]{.code-inline}](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions)
parameters.

For this exercise, we will request three additional sets of fields from
different objects:

-   The additional [ created_at ]{.code-inline} field in the primary
    Lists object.

-   The full [user
    object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
    using the [ expansion ]{.code-inline} parameter

-   The additional user. [ created_at ]{.code-inline} field in the
    associated user object.

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

+-----------------------+-----------------------+-----------------------+
| **Key**               | **Value**             | **Returned fields**   |
+-----------------------+-----------------------+-----------------------+
| [ list.fields         | [ created_at          | [ created_at          |
| ]{.code-inline}       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [ expansions          | [ owner_id            | ::: code-inline       |
| ]{.code-inline}       | ]{.code-inline}       | includes.users.id,    |
|                       |                       | includes.users.name,  |
|                       |                       |                       |
|                       |                       | in                    |
|                       |                       | cludes.users.username |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| [ user.fields         | [ created_at          | [                     |
| ]{.code-inline}       | ]{.code-inline}       | incl                  |
|                       |                       | udes.users.created_at |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+

You should now see a similar URL next to the "Send" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/lists/84839422?list.fields=owner_id&expansions=owner_id&user.fields=created_at
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Step five: Make your request and review your response \

Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "id": "84839422",
    "name": "Official Twitter Accounts",
    "owner_id": "783214"
  },
  "includes": {
    "users": [
      {
        "name": "Twitter",
        "created_at": "2007-02-20T14:35:54.000Z",
        "username": "Twitter",
        "id": "783214"
      }
    ]
  }
}
    
```
:::
:::
:::
:::
