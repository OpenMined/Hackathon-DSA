::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to
the authenticated user lookup endpoint using Postman.

Please visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository if you want to see sample code in different languages.
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
to the "Authenticated User Lookup" folder, and select "Lookup an
Authenticated User".

#### 

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

Step three: Determine which user fields you want to retrieve \

If you click the \"Send\" button after step three, you will receive the
default [user
object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
fields in your response: [ id ]{.code-inline} , [ name ]{.code-inline} ,
and [ username ]{.code-inline} .

If you would like to receive additional fields beyond [ id
]{.code-inline} , [ name ]{.code-inline} , and [ username
]{.code-inline} , you will have to specify those fields in your request
with the [[ field
]{.code-inline}](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields)
and/or [[ expansion
]{.code-inline}](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions)
parameters.

For this exercise, we will request three additional sets of fields from
different objects:

1.  The additional [ user.created_at ]{.code-inline} field in the
    primary user objects.

2.  The associated pinned Tweets' object's default fields for the
    returned users: [ id ]{.code-inline} and [ text ]{.code-inline} .

3.  The additional [ tweet.created_at ]{.code-inline} field in the
    associated Tweet objects.\

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

+-----------------------+-----------------------+-----------------------+
| **Key**               | **Value**             | **Returned fields**   |
+-----------------------+-----------------------+-----------------------+
| [ user.fields         | [ created_at          | [ user.created_at     |
| ]{.code-inline}       | ]{.code-inline}       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [ expansions          | [ pinned_tweet_id     | [                     |
| ]{.code-inline}       | ]{.code-inline}       | includes.tweets.id,\  |
|                       |                       | includes.tweets.text  |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| [ tweet.fields        | [ created_at,         | [                     |
| ]{.code-inline}       | author_id             | includ                |
|                       | ]{.code-inline}       | es.tweets.created_at, |
|                       |                       | incl                  |
|                       |                       | udes_tweets.author_id |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+

You should now see a similar URL next to the "Send" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/users/me?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at
    
```
:::
:::
:::
:::
