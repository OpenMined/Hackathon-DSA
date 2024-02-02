::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
manage follows endpoints using
[Postman](/en/docs/tutorials/postman-getting-started) .

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
to the "Follows" folder, and select "Follow a user ID".\

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

#### Step three: Specify who is going to follow whom

Manage follows endpoints take two IDs: one for the source user (the user
who wishes to follow or unfollow another user) and the target user (the
user that will be followed or unfollowed). The source user's ID must
correspond to the user ID of the authenticating user. In this case, you
can specify the ID belonging to your own user. You can find your ID in
two ways:

1.  Using the [user lookup by
    username](/en/docs/twitter-api/users/lookup/api-reference) endpoint,
    you can pass a username and receive the [ id ]{.code-inline} field.
2.  Looking at your Access Token, you will find that the numeric part is
    your user ID.\

The target ID can be any valid user ID. For example the user ID for
\@TwitterDev is 2244994945.

In Postman, navigate to the \"Params\" tab, and enter your ID into the
\"Value\" column of the [ id ]{.code-inline} path variable. Navigate to
the "Body" tab and and 2244994945 (the user ID for \@TwitterDev) as the
value for the [ target_user_id ]{.code-inline} parameter. Making sure to
not include any spaces before or after any ID.

  ---------------------------------- ------------------------------
  **Key**                            **Value**
  [ ` id ` ]{.code-inline}           (your user ID)
  [ target_user_id ]{.code-inline}   [ 2244994945 ]{.code-inline}
  ---------------------------------- ------------------------------

\
If you click the \"Send\" button, you will receive a response object
containing the status of the relationship:

-   If you receive a [ \"following\": true ]{.code-inline} , then the [
    id ]{.code-inline} is successfully following the [ target_user_id
    ]{.code-inline} .
-   If you receive a [ \"pending\": true ]{.code-inline} , then the [
    target_user_id ]{.code-inline} is protected and must accept your
    follow request.

####  Step four: Make your request and review your response

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
        "following": true,
        "pending_follow": false
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Similarly, if you were trying to unfollow a user, you would use the
\"Unfollow a user ID\" request within the same Postman collection.
However, both the [ source_user_id ]{.code-inline} and [ target_user_id
]{.code-inline} parameters should be passed as path variables using the
unfollow endpoint.
:::
:::
:::
