::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note** :

Twitter needs to enable access to the Account Activity API for your
developer App before you can start using the API. To this end, make sure
to share the App ID that you intend to use for authentication purposes
with your account manager or technical support team.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The [Account Activity
API](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/overview)
consists of a set of endpoints that allow you to create and manage user
subscriptions to receive real-time account activities for all of your
subscribed accounts through a single connection.

There are two authentication methods available with the Account Activity
API ( [OAuth
1.0a](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth1.0a)
and [OAuth 2.0 Bearer
Token](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/authentication-method-overview#oauth2.0)
). The authentication method that you should use will depend on which
endpoint you are using.
:::
:::

::: c01-rich-text-editor
:::

::: c01-rich-text-editor
::: is-table-default
For those endpoints that require OAuth 1.0a user context authentication,
you will need to provide the following credentials to authenticate the
request:

-   Consumer Keys (API Key and Secret)
-    Access Tokens (Access Token and Secret)

In the case of the following three endpoints, you perform write actions
within the context of your application (no Twitter users are involved).
Therefore, the Access Tokens you need to provide are the ones belonging
to your developer App. These can be generated directly from within the
[developer
portal](https://developer.twitter.com/en/portal/projects-and-apps) ,
under the "Keys and tokens" tab for your App.

On the other hand, in the case of the following three endpoints, you are
making a request that allows your application to access protected data
on behalf of a Twitter user (for example, Direct Messages). You must
therefore provide the Access Tokens that belong to the subscribing user
in question. The required Access tokens can be obtained using the
3-legged OAuth flow (see [OAuth 1.0a: how to obtain a user's Access
Tokens](/en/docs/tutorials/authenticating-with-twitter-api-for-enterprise/oauth1-0a-and-user-access-tokens)
). These endpoints have been marked with an asterisk in the above table
(\*).
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note** :

Make sure that your developer App is enabled for \"Read, Write, and
Direct Messages.\" You can change this setting in the [Projects & Apps
section](https://developer.twitter.com/en/portal/projects-and-apps) of
your developer account, under "App permissions" for the selected
developer App. You will need to regenerate your App credentials after
changing the permissions settings.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
A list of all endpoints available with the Account Activity API,
including associated description and example cURL requests with
authentication implementation examples, can be found in [the API
reference
documentation](https://developer.twitter.com/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise)
.

For additional information, check out TwitterDev's [sample web app and
helper
scripts](https://github.com/twitterdev/account-activity-dashboard-enterprise)
to get started with the Enterprise Account Activity API.
:::
:::

::: c01-rich-text-editor
### Next steps
:::
:::
