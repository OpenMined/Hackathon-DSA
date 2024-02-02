::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
manage Bookmarks endpoints using
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
to the "Bookmarks" folder, and select "Create a Bookmark".

#### Step two: Authenticate your request

To make a successful request to this endpoint, you will need to use
[OAuth 2.0 Authorization Code Flow with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
. You can generate an access token within Postman.

If you go to the tab entitled "Authorization" and select "OAuth 2.0".

In this tab, be sure to follow these steps:

1.  Name your token

2.  Select the Grant Type as Authorization Code (with PKCE)

3.  Update the parameters:

    **Callback URL** -
    [https://www.example.com](https://www.example.com/)

    This should be matching the callback URL you set in your auth
    settings page in the Developer Portal.

    **Auth URL** - <https://twitter.com/i/oauth2/authorize>

    **Access Token URL** - <https://api.twitter.com/2/oauth2/token>

    **Client ID** - Cut and paste OAuth 2.0 client ID from the Developer
    Portal

    **Client Secret** - Cut and paste OAuth 2.0 client ID from the
    Developer Portal. You will need this only if you are using an App
    type that is a confidential client.

4.  Update the scopes with the following values: tweet.read users.read
    bookmark.write

5.  Populate the field state with "State"

6.  Click where it says "Generate Token"

7.  Press the save icon to save the folder changes.

You may get a message that you are not logged into Twitter. If you get
this error, you will need to log in to the Twitter account inside of
Postman you are trying to post on behalf of.

#### Step three: Specify a user

With this endpoint, you must specify the user ID whose followers you
would like to receive in the response. For example, the user ID for
\@TwitterDev is ` 2244994945 ` .

In Postman, navigate to the "Params" tab and enter the ID of yourself or
an authenticated user as the value for the id parameter.

#### Step four: Specify Specify a Tweet you want to Bookmark

You will want to navigate to the "Body" tab and make sure the Tweet ID
is set to the one you are looking to save to your Bookmarks. The JSON
payload should look similar to the one below.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {"tweet_id": "1460323737035677698"}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: {.t05-inline-code-snippet .t05-inline-code-snippet--full-height}
``` {.line-numbers .t05__pre--wrap-text}
 {
   "data": {
       "bookmarked": true
   }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
To delete a Tweet, select the "Remove a Bookmark" request also found in
the "Bookmarks" folder of the Twitter API v2 collection loaded in
Postman. You will first want to specify the user ID of the user you are
making a request on behalf of as the value for the " ` id ` " column.
This endpoint also requires the ID of the Tweet you wish to delete.
Then, in the "Params" tab, enter the ID of the Tweet you wish to delete
as the value for the " ` tweet_id ` " column.

When you have a successful delete request, you will receive a response
similar to the following example:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
   "data": {
       "bookmarked": false
   }
}
    
```
:::
:::
:::
:::
