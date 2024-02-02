::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick overview will help you make your first request to List
members endpoints using
[Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman)
.

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code)
GitHub repository.
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
To load the Twitter API v2 Postman collection into your workspace,
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
#### Authenticate your request

To make a successful request to **lookup** endpoints, you can use either
[OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [App
only](https://developer.twitter.com/en/docs/authentication/oauth-2-0) ,
or [OAuth 2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) . However,
with **manage** endpoints, you can only authenticate with OAuth 1.0a
User Context or OAuth 2.0 Authorization Code with PKCE.

Regardless, when using Postman, the default authentication keys and
tokens will automatically populate in your requests as long as you\'ve
set up your environment properly.

You can do this by selecting the environment named "Twitter API v2" (in
the top-right corner of Postman), and adding your keys and tokens to the
\"initial value\" and \"current value\" fields (by clicking the eye icon
next to the environment dropdown). These keys include the following:

-   API Key (also known as Consumer Key)
-   API Secret Key (also known as Consumer Secret)
-   OAuth 1.0a user Access Token
-   OAuth 1.0a user Access Token Secret
-   App only Access Token
-   OAuth 2.0 Client Key (only available if you\'ve set up OAuth 2.0
    User Authentication settings in your App\'s settings)
-   OAuth 2.0 Client Secret (only available if you\'ve set up OAuth 2.0
    User Authentication settings in your App\'s settings)
:::
:::

::: d09-content-module
::: {.d09 .d09-content-module__container}
[ ]{.d09__title--underline .twtr-color-bg--blue-dark}

Choose any of the following endpoints for a more in-depth guide once,
you have completed the prerequisites:
:::
:::
:::
