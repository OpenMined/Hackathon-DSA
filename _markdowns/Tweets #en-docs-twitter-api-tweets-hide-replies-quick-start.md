::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the hide
replies endpoint using
[Postman](/en/docs/tools-and-libraries/using-postman) .

If you would like to see some code snippets in different languages,
please visit the [hide replies API Reference
page](/en/docs/twitter-api/tweets/hide-replies/api-reference/put-tweets-id-hidden#requests)
.
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
<div>

There are several different tools, code examples, and libraries that you
can use to make a request to this endpoint, but we are going to use the
Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please
click on the following button:

</div>
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
<div>

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

#### Step three: Find a Tweet ID to hide

The hide replies endpoint can hide or unhide replies on behalf of an
authorized user. Because we are using the Access Tokens related to your
user profile in this example, you will be able to hide replies from
users who participate in a conversation started by you. Similarly, if
you were using Access Tokens that belong to another user that authorized
your app, you would be able to moderate replies to any conversations
started by that account.

Ask a friend to reply to a Tweet (let them know you\'re testing hide
replies) or reply to any of your Tweets from a test account. Click on
that reply, then copy the numeric part of its URL. That will be the
Tweet ID we will hide.

In this case, we will be looking at the following Tweet, which has the
ID ` 1232720193182412800 ` :

` https://twitter.com/TwitterDev/status/1232720193182412800 `

####  Step four: Hide the Tweet

In Postman, open the Hide replies folder and select Hide a reply. In the
Params tab, paste the Tweet ID next to the id field (you won\'t need to
replace :id in the URL). Click \"Send\" and you will see a successful
response.

</div>
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {"hidden":true}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Hidden Tweets are moved to a separate tab in the Twitter app. To unhide
a tweet in Postman, open the Hide replies folder and select Unhide a
reply. In the Params tab, paste the same Tweet ID used in the previous
step next into the [ id ]{.code-inline} field. Click \"Send\" and you
will see a successful response.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {"hidden":false}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
The [ hidden ]{.code-inline} field represents the hidden status of the
Tweet. A [ hidden ]{.code-inline} status of [ true ]{.code-inline} means
the Tweet is hidden. Similarly, [ false ]{.code-inline} means the Tweet
is not hidden.
:::
:::
:::
