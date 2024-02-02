::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Signing up for a developer account is quick and easy! Just click on the
button below, answer a few questions, and you can start exploring and
building on the Twitter API v2 using [Basic
access](https://developer.twitter.com/en/portal/products/basic) .

Next you will create a Project and an associated developer App during
the onboarding process, which will provide you a set of credentials that
you will use to authenticate all requests to the API.
:::
:::

::: b03-button-v3
[](https://developer.twitter.com/en/portal/products/basic){.chirp-btn
.twtr-spacing--mb-500 .chirp-btn--primary .chirp-btn--icon
.chirp-btn--icon-end .twtr-scribe-clicks}

::: chirp-btn__icon
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/icons/chevron_right.svg){.chirp-btn__icon--img}
:::

Sign up
:::

::: c01-rich-text-editor
::: is-table-default
Once you have access and have created a Project and App, you will be
able to find or generate the following credentials within your developer
App:

-   **[API Key and
    Secret](/en/docs/authentication/oauth-1-0a/api-key-and-secret) :**
    Essentially the username and password for your App. You will use
    these to authenticate requests that require [OAuth 1.0a User
    Context](/en/docs/authentication/oauth-1-0a) , or to generate other
    tokens such as user Access Tokens or App Access Token.

-   **[Access Token and
    Secret](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
    :** In general, Access Tokens represent the user that you are making
    the request on behalf of. The ones that you can generate via the
    developer portal represent the user that owns the App. You will use
    these to authenticate requests that require [OAuth 1.0a User
    Context](/en/docs/authentication/oauth-1-0a) . If you would like to
    make requests on behalf of another user, you will need to use the
    3-legged OAuth flow for them to authorize you.

-   **[Client ID and Client
    Secret](/content/en/docs/authentication/oauth-2-0/user-access-token)
    :** These credentials are used to obtain a user Access Token with
    OAuth 2.0 authentication. Similar to OAuth 1.0a, the user Access
    Tokens are used to authenticate requests that provide private user
    account information or perform actions on behalf of another account
    but, with fine-grained scope for greater control over what access
    the client application has on the user.

-   **[App only Access
    Token](/en/docs/authentication/oauth-2-0/bearer-tokens) :** You will
    use this token when making requests to endpoints that responds with
    information publicly available on Twitter.

Since these keys and tokens do not expire unless regenerated, we suggest
that you save them in a secure location, such as a password manager,
once you\'ve received your credentials.
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note: Your keys and tokens will only display once in the
[developer portal](/en/docs/developer-portal) , so it is important that
you store these credentials in your password management system as soon
as you generate them.**

If you misplace or forget the keys and tokens, you will need to
regenerate them, which creates new credentials and invalidates the old
ones. This means that you will have to update any integrations that you
may have set up with your prior credentials.

Learn more about our [authentication best
practices](/en/docs/authentication/guides/authentication-best-practices)
.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
What's next? Let's make your first request to the API!

We have guides, tutorials, tools, and code to help you get started. The
following page will be a great place to start, but note that we've also
put together an important resources page to help you navigate the
broader documentation.
:::
:::

::: c01-rich-text-editor
:::
:::
