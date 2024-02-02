::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
manage Likes endpoints using
[Postman](/en/docs/tools-and-libraries/using-postman) .

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
GitHub repository.\
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
can use to make a request to this endpoint, but we are going to use the
Postman tool here to simplify the process.

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
to the "Likes" folder, and select "Like a Tweet".

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so with this endpoint, you must authenticate
your request using either [OAuth 1.0a User
Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0 Authorization
Code with PKCE](/en/docs/authentication/oauth-2-0/authorization-code) .

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens -- specifically your API Key, API
Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access
Token Secret -- to Postman. You can do this by selecting the environment
named "Twitter API v2" in the top-right corner of Postman and adding
your keys and tokens to the \"initial value\" and \"current value\"
fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.\

#### Step three: Specify which Tweet you are going to like

Manage Likes endpoints require two IDs: one for the user (the user who
wishes to like a Tweet), and the other representing the  Tweet ID that
the user is trying to like or unlike.

The user's ID must correspond to the authenticating user's ID, meaning
that you must pass the [Access
Tokens](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
associated with the user ID when authenticating your request.  In this
case, you can specify the ID belonging to your own user. You can find
your ID in two ways:

1.  Using the [user lookup by
    username](/en/docs/twitter-api/users/lookup/api-reference) endpoint,
    you can pass a username and receive the [ id ]{.code-inline} field.
2.  Looking at your Access Token, you will find that the numeric part is
    your user ID.\

You also must specify a Tweet that you want to like. You can find the
Tweet ID by navigating to twitter.com and clicking on a Tweet and then
looking in the URL. For example, the following URL\'s Tweet ID
is 1228393702244134912.

[ https://twitter.com/TwitterDev/status/1228393702244134912\
]{.code-inline}

In Postman, navigate to the \"Params\" tab, and enter your ID into the
\"Value\" column of the [ id ]{.code-inline} path variable. Navigate to
the "Body" tab and ID of the Tweet you wish to like as the value for the
[ tweet_id ]{.code-inline} parameter. Be sure not to include any spaces
before or after any ID.

  ---------------------------- ----------------------------------------
  **Key**                      **Value**
  [ ` id ` ]{.code-inline}     (your user ID)
  [ tweet_id ]{.code-inline}   (the ID of the Tweet you want to like)
  ---------------------------- ----------------------------------------

\
If you click the \"Send\" button, you will receive a response object
containing the status of the relationship:

-   If you receive a [ \"liked\": true ]{.code-inline} , then the [ id
    ]{.code-inline} is successfully liking the [ tweet_id
    ]{.code-inline} .\

#### Step four: Make your request and review your response

Once you have everything set up, hit the \"Send\" button and you will
receive the following response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "liked": true
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
\
If you wish to unlike the same Tweet you can use the request entitled
"Unlike a Tweet", which is also found in the "Likes" folder of the
Twitter API v2 collection in Postman. The [ id ]{.code-inline} and [
tweet_id ]{.code-inline} should be used in the same way as the previous
example.  To unlike a Tweet, you will not have to add this as a JSON
body so you will want to make sure that you add in the requisite query
params for [ id ]{.code-inline} and [ tweet_id ]{.code-inline} .
:::
:::
:::
