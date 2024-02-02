::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
blocks lookup endpoint using
[Postman](/en/docs/tools-and-libraries/using-postman) .

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository.\
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
to the "Blocks" folder, and select "Blocks Lookup".\

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

#### Step three: Specify a user

With this endpoint, you must specify your user ID or the user ID of an
authenticated user to see who you have blocked.

In Postman, navigate to the \"Params\" tab and enter this username into
the \"Value\" column of the [ id ]{.code-inline} path variable (at the
bottom of the section), making sure to not include any spaces before or
after usernames.\

  ------------------------------- ---------------------
  **Key**                         **Value**
  [ ` id ` ]{.code-inline}        (your user ID)
  [ max_results ]{.code-inline}   [ 5 ]{.code-inline}
  ------------------------------- ---------------------

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default [user
object](/en/docs/twitter-api/data-dictionary/object-model/user) fields
in your response: [ id ]{.code-inline} , [ name ]{.code-inline} , and [
username ]{.code-inline} .

If you would like to receive additional fields beyond id, name, and
username, you will have to specify those fields in your request with the
[[ fields
]{.code-inline}](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields)
and/or [[ expansions
]{.code-inline}](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions)
parameters.

For this exercise, we will request three additional sets of fields from
different objects:

1.  The additional [ user.created_at ]{.code-inline} field in the
    primary user objects.
2.  The associated pinned Tweets' object's default fields for the
    returned users: [ id ]{.code-inline} and [ text ]{.code-inline} .
3.  The additional [ tweet.created_at ]{.code-inline} field in the
    associated Tweet objects.

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

  -------------------------------- ----------------------------------- ----------------------------------------------
  **Key**                          **Value**                           **Returned fields**
  [ user.fields ]{.code-inline}    [ created_at ]{.code-inline}        [ user.created_at ]{.code-inline}
  [ expansions ]{.code-inline}     [ pinned_tweet_id ]{.code-inline}   [ tweet.id, tweet.text ]{.code-inline}
  [ tweet.fields ]{.code-inline}   [ created_at ]{.code-inline}        [ includes.tweets.created_at ]{.code-inline}
  -------------------------------- ----------------------------------- ----------------------------------------------

You should now see a similar URL with your own user ID instead of
TwitterDev's URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/users/2244994945/blocking?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
#### Step five: Make your request and review your response

Once you have everything set up, hit the \"Send\" button and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": [
    {
      "created_at": "2008-12-04T18:51:57.000Z",
      "id": "17874544",
      "username": "TwitterSupport",
      "name": "Twitter Support"
    },
    {
      "created_at": "2007-02-20T14:35:54.000Z",
      "id": "783214",
      "username": "Twitter",
      "name": "Twitter"
    },
    {
      "pinned_tweet_id": "1389270063807598594",
      "created_at": "2018-11-21T14:24:58.000Z",
      "id": "1065249714214457345",
      "username": "TwitterSpaces",
      "name": "Spaces"
    },
    {
      "pinned_tweet_id": "1293595870563381249",
      "created_at": "2007-05-23T06:01:13.000Z",
      "id": "6253282",
      "username": "TwitterAPI",
      "name": "Twitter API"
    }
  ],
  "includes": {
    "tweets": [
      {
        "created_at": "2021-05-03T17:26:09.000Z",
        "id": "1389270063807598594",
        "text": "now, everyone with 600 or more followers can host a Space.\n\nbased on what we've learned, these accounts are likely to have a good experience hosting because of their existing audience. before bringing the ability to create a Space to everyone, we’re focused on a few things. 🧵"
      },
      {
        "created_at": "2020-08-12T17:11:04.000Z",
        "id": "1293595870563381249",
        "text": "Twitter API v2: Early Access released\n\nToday we announced Early Access to the first endpoints of the new Twitter API!\n\n#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"
      }
    ]
  }

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You may notice that there is a [ meta ]{.code-inline} object located at
the bottom of the response. If you received a [ next_token
]{.code-inline} , this signals that there is another page of results
that we can retrieve. To pull the next page of results, you will pull
the value of the [ next_token ]{.code-inline} field and add it to the
request as the value to an additional [ pagination_token ]{.code-inline}
parameter.\

  ------------------------------------ ------------------------------------
  **Key**                              **Value**
  [ pagination_token ]{.code-inline}   [ 1D3PU6DRII9HEZZZ ]{.code-inline}
  ------------------------------------ ------------------------------------

If you send the request after adding this additional parameter, the next
five results will be delivered with the subsequent payload since we
specified [ max_results ]{.code-inline} as [ 5 ]{.code-inline} in step
three. You can continue to repeat this process until all results have
been returned, but you can also use the [ max_results ]{.code-inline}
parameter to request up to 1000 users per request, so you don't have to
paginate through results quite as much.
:::
:::
:::
