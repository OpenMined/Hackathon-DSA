::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
manage Tweets endpoints using
[Postman](https://developer.twitter.com/en/docs/tools-and-libraries/using-postman)
.\

Please visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository if you want to see sample code in different languages.
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
to the "Manage Tweets" folder, and select "Create a Tweet".\

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission to do so. To do this with the manage Tweets
endpoints, you must authenticate your request using either [OAuth 1.0a
User Context](/en/docs/authentication/oauth-1-0a) or [OAuth 2.0
Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) .

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens (and specifically your API Key, API
Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access
Token Secret) to Postman. You can do this by selecting the environment
named "Twitter API v2" (in the top-right corner of Postman), and adding
your keys and tokens to the \"initial value\" and \"current value\"
fields (by clicking the eye icon next to the environment dropdown).

If you\'ve done this correctly, these variables will automatically be
pulled into the request\'s authorization tab.

#### Step three: Specify the text of the Tweet

When creating a new Tweet with this endpoint, text or media for the
Tweet are the required body parameters.

In Postman, navigate to the "Body" tab and enter the text of the Tweet
as the value for the ` text ` parameter. Additionally, if you wish to
add parameters for items such as polls, replying to a Tweet ID, or
adding reply settings you can also do so here. You can learn more about
what's available in our [API reference
guide](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/api-reference)
. \

  ---------- -------------- --------------------
  **Key**    **Value**      **Parameter type**
  ` text `   Hello world!   body
  ---------- -------------- --------------------

####  Step four: Identify and specify which fields you would like to retrieve

Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "data": {
    "id": "1445880548472328192",
    "text": "Hello world!"
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If the returned response object contains an ` id ` and the ` text ` of
your Tweet, you have successfully created a Tweet.\

####  Step five: Delete your Tweet  

To delete a Tweet, select the "Delete a Tweet" request also found in the
"Manage Tweets" folder of the Twitter API v2 collection loaded in
Postman. This endpoint requires the ID of the Tweet you wish to delete.
Then, in the "Params" tab, enter the ID of the Tweet you wish to delete
as the value for the ` id ` column.

On successful delete request, you will receive a response similar to the
following example:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "data": {
       "deleted" : true
   }
}

    
```
:::
:::
:::
:::
