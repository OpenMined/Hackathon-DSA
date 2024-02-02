::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
Likes lookup endpoint using
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
to the \"Likes\" folder and select \"Liking users."\

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so, this endpoint requires you to
authenticate your request with either [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) , [OAuth
2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , or [OAuth
1.0a User Context](/en/docs/authentication/oauth-1-0a) authentication
methods.

For simplicity\'s sake, we will utilize OAuth 2.0 App-Only with this
request, but you will need to use one of the other authentication
methods if you\'d like to request private
[metrics](/en/docs/twitter-api/metrics) or Tweets.

To utilize OAuth 2.0 App-Only, you must add your keys and tokens,
specifically the [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as
the App-only Bearer Token) to Postman. You can do this by selecting the
environment named "Twitter API v2" in the top-right corner of Postman
and adding your keys and tokens to the \"initial value\" and \"current
value\" fields (by clicking the eye icon next to the environment
dropdown).

These variables will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.

#### Step three: Specify a Tweet

With this endpoint, you must specify the Tweet ID that you want to get
liking users for. You can find the ID of a Tweet by navigating to that
Tweet on Twitter and pulling the numerical code at the end of the URL.
For example, the following URL\'s Tweet ID is 1354143047324299264.

[ https://twitter.com/TwitterDev/status/1354143047324299264
]{.code-inline}

In Postman, navigate to the \"Params\" tab and enter this username into
the \"Value\" column of the [ tweet_id ]{.code-inline} path variable (at
the bottom of the section), making sure to not include any spaces before
or after usernames.

  -------------------------- --------------------------------------------------
  **Key**                    **Value**
  [ ` id ` ]{.code-inline}   The Tweet ID you want to get the liking users of
  -------------------------- --------------------------------------------------

####  Step four: Identify and specify which fields you would like to retrieve

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

  -------------------------------- ----------------------------------- ----------------------------------------
  **Key**                          **Value**                           **Returned fields**
  [ user.fields ]{.code-inline}    [ created_at ]{.code-inline}        [ user.created_at ]{.code-inline}
  [ expansions ]{.code-inline}     [ pinned_tweet_id ]{.code-inline}   [ tweet.id, tweet.text ]{.code-inline}
  [ tweet.fields ]{.code-inline}   [ created_at ]{.code-inline}        [ tweet.created_at ]{.code-inline}
  -------------------------------- ----------------------------------- ----------------------------------------

You should now see the following URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/tweets/1354143047324299264/liking_users?user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=created_at
    
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
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You might also want to make a request to get a user's liked Tweets as
well. With the Likes lookup endpoint, you can get information about a
user's liked Tweets. To do this navigate to the \"Likes\" folder and
select \"Liked Tweets".

With this endpoint, you must specify the User ID that you want to get
liking users for. You can use the [user
lookup](/content/developer-twitter/en/docs/twitter-api/users/lookup/introduction)
endpoint to get this information.

In Postman, navigate to the \"Params\" tab and enter this username into
the \"Value\" column of the [ id ]{.code-inline} path variable (at the
bottom of the section), making sure to not include any spaces before or
after usernames.

  ------------------------------- -------------------------------------------------
  **Key**                         **Value**
  [ id ]{.code-inline}            The user ID you want to get the liked Tweets of
  [ max_results ]{.code-inline}   [ 5 ]{.code-inline}
  ------------------------------- -------------------------------------------------

You can now see a similar URL with your ID instead of TwitterDev's next
to the \"Send\" button:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/users/2244994945/liked_tweets?max_results=5

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
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
      "id": "1362449997430542337",
      "text": "Honored to be the first developer to be featured in @TwitterDev's love fest 🥰♥️😍 https://t.co/g8TsPoZsij"
    },
    {
      "id": "1365416026435854338",
      "text": "We're so happy for our Official Partner @Brandwatch and their big news. https://t.co/3DwWBNSq0o https://t.co/bDUGbgPkKO"
    },
    {
      "id": "1296487407475462144",
      "text": "Check out this feature on @TwitterDev to learn more about how we're mining social media data to make sense of this evolving #publichealth crisis https://t.co/sIFLXRSvEX."
    },
    {
      "id": "1294346980072624128",
      "text": "I awake from five years of slumber https://t.co/OEPVyAFcfB"
    },
    {
      "id": "1283153843367206912",
      "text": "@wongmjane Wish we could tell you more, but I’m only a teapot 👀"
    }
  ],
  "meta": {
        "next_token": "7140dibdnow9c7btw4539n0vybdnx19ylpayqf16fjt4l",
          "result_count": 5
  }
}
    
```
:::
:::
:::
:::
