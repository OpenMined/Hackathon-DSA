::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
Tweets lookup endpoints with a set of specified fields using Postman.

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository.
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
to the \"Tweet Lookup \> Multiple Tweets\" request.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do this with this endpoint, you must
authenticate your request with either [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only) , [OAuth
2.0 Authorization Code with
PKCE](/en/docs/authentication/oauth-2-0/authorization-code) , or [OAuth
1.0a User Context](/en/docs/authentication/oauth-1-0a) authentication
methods.

For simplicity\'s sake, we are going to utilize OAuth 2.0 App-Only with
this request, but if you\'d like to request private
[metrics](/en/docs/twitter-api/metrics) or Tweets, you will need to use
one of the other authentication methods.

To utilize OAuth 2.0 App-Only, you must add your keys and tokens (and
specifically the [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) , also known as
the App-only Bearer Token) to Postman by selecting the environment named
"Twitter API v2" (in the top-right corner of Postman), and adding your
keys and tokens to the \"initial value\" and \"current value\" fields
(by clicking the eye icon next to the environment dropdown).

If you\'ve done this correctly, these variables will automatically be
pulled into the request\'s authorization tab.\

#### Step three: Identify and specify which Tweets you would like to retrieve

You must specify a Tweet or a set of Tweets that you would like to
receive within the request. You can find the Tweet ID by navigating to
twitter.com and clicking on a Tweet and then looking in the URL. For
example, the following URL\'s Tweet ID is ` 1228393702244134912 ` .

` https://twitter.com/TwitterDev/status/1228393702244134912 `

In Postman, navigate to the \"Params\" tab and enter this ID, or a
string of Tweet IDs separated by a comma, into the \"Value\" column of
the ` ids ` parameter.

  --------- ---------------------------------------------------------------------------
  **Key**   **Value**
  ` ids `   ` 1228393702244134912, ` ` 1227640996038684673, ` ` 1199786642791452673 `
  --------- ---------------------------------------------------------------------------

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default
[Tweet](/content/developer-twitter/en/docs/twitter-api/object-reference/tweet)
object fields in your response: [ id ]{.code-inline} , [ text
]{.code-inline} , and [ edit_history_tweet_ids ]{.code-inline} .

If you would like to receive additional fields beyond [ id
]{.code-inline} , [ text ]{.code-inline} , and [ edit_history_tweet_ids
]{.code-inline} , you will have to specify those fields in your request
with the [field](/content/developer-twitter/en/docs/twitter-api/fields)
and/or
[expansion](/content/developer-twitter/en/docs/twitter-api/expansions)
parameters.

For this exercise, we will request a three additional different sets of
fields from different objects:

1.  The additional [ tweet.created_at ]{.code-inline} field in the
    primary user objects.\
2.  The associated authors' user object's default fields for the
    returned Tweets: [ id ]{.code-inline} , [ name ]{.code-inline} , and
    [ username ]{.code-inline}
3.  The additional [ user.created_at ]{.code-inline} field in the
    associated user objects.\

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:\

  ------------------ ---------------- -------------------------------------------------------------------------------
  **Key**            **Value**        **Returned fields**
  ` tweet.fields `   ` created_at `   ` tweets.created_at `
  ` expansions `     ` author_id `    ` includes.users.id ` , ` includes.users.name ` , ` includes.users.username `
  ` user.fields `    ` created_at `   ` includes.users.created_at `
  ------------------ ---------------- -------------------------------------------------------------------------------

You should now see the following URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://api.twitter.com/2/tweets?ids=1228393702244134912,1227640996038684673,1199786642791452673&tweet.fields=created_at&expansions=author_id&user.fields=created_at
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, hit the \"Send\" button and you will
receive the following response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "data": [
    {
      "author_id": "2244994945",
      "created_at": "2020-02-14T19:00:55.000Z",
      "id": "1228393702244134912",
      "edit_history_tweet_ids": ["1228393702244134912"],
      "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}"
    },
    {
      "author_id": "2244994945",
      "created_at": "2020-02-12T17:09:56.000Z",
      "id": "1227640996038684673",
      "edit_history_tweet_ids": ["1227640996038684673"],
      "text": "Doctors: Googling stuff online does not make you a doctor\n\nDevelopers: https://t.co/mrju5ypPkb"
    },
    {
      "author_id": "2244994945",
      "created_at": "2019-11-27T20:26:41.000Z",
      "id": "1199786642791452673",
      "edit_history_tweet_ids": ["1199786642791452673"],
      "text": "C#"
    }
  ],
  "includes": {
    "users": [
      {
        "created_at": "2013-12-14T04:35:55.000Z",
        "id": "2244994945",
        "name": "Twitter Dev",
        "username": "TwitterDev"
      }
    ]
  }
}

    
```
:::
:::
:::
:::
