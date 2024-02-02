::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
recent search endpoint with a set of specified fields using Postman.

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
<div>

\
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the Search Tweets \> Recent search request.

####  Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do this with this endpoint, you must
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
authorization tab if you\'ve done this correctly.\

#### Step three: Create a search query

Each recent search query requires a single [search
query](/en/docs/twitter-api/tweets/search/integrate/build-a-rule) . For
this example, we are going to use a query that matches on Tweets posted
by the \@XDevelopers account. For this query we use the [ from
]{.code-inline} operator and set it to [ XDevelopers ]{.code-inline}
(case insensitive):

` from:XDevelopers `

In Postman, navigate to the \"Params\" tab and enter this ID, or a
string of Tweet IDs separated by a comma, into the \"Value\" column of
the ` ids ` parameter.

  ----------- ------------------------------------ ------------------------------------------------------
  **Key**     **Value**                            **Description**
  ` query `   [ from:XDevelopers ]{.code-inline}   Search query to submit to the recent search endpoint
  ----------- ------------------------------------ ------------------------------------------------------

#### Step four: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default [Tweet
object](/en/docs/twitter-api/data-dictionary/object-model/tweet) fields
in your response: [ id ]{.code-inline} , [ text ]{.code-inline} , and [
edit_history_tweet_ids ]{.code-inline} . If you would like to receive
additional fields beyond [ id ]{.code-inline} , [ text ]{.code-inline} ,
and [ edit_history_tweet_ids ]{.code-inline} , you will have to specify
those fields in your request with the
[field](/content/developer-twitter/en/docs/twitter-api/fields) and/or
[expansion](/content/developer-twitter/en/docs/twitter-api/expansions)
parameters.

For this exercise, we will request a four different sets of fields from
different objects:

1.  The default Tweet object fields.
2.  The additional [ tweet.created_at ]{.code-inline} field in the
    primary user objects.
3.  The associated authors' user object's default fields for the
    returned Tweets.
4.  The additional [ user.description ]{.code-inline} field in the
    associated user objects.

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

  ------------------ ----------------- -------------------------------------------------------------------------------
  **Key**            **Value**         **Returned fields**
  ` tweet.fields `   ` created_at `    ` tweets.created_at `
  ` expansions `     ` author_id `     ` includes.users.id ` , ` includes.users.name ` , ` includes.users.username `
  ` user.fields `    ` description `   ` includes.users.description `
  ------------------ ----------------- -------------------------------------------------------------------------------

You should now see the following URL next to the \"Send\" button:

</div>
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/tweets/search/recent?query=from:XDevelopers&tweet.fields=created_at&expansions=author_id&user.fields=created_at

    
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
           "created_at": "2020-06-11T16:05:06.000Z",
           "id": "1271111223220809728",
           "text": "Tune in tonight and watch as @jessicagarson takes us through running your favorite Python package in R. 🍿\n\nLearn how to use two powerful programming languages for data science together, and see a live example that uses the recent search endpoint from Twitter’s Developer Labs. https://t.co/v178oUZNuj"
       },
       {
           "author_id": "2244994945",
           "created_at": "2020-06-10T19:25:24.000Z",
           "id": "1270799243071062016",
           "text": "As we work towards building the new Twitter API, we’ve extended the deprecation timeline for several Labs v1 endpoints. Learn more 📖 https://t.co/rRWaJYJgKk"
       },
       {
           "author_id": "2244994945",
           "created_at": "2020-06-09T18:08:47.000Z",
           "id": "1270417572001976322",
           "text": "Annotations help you learn more about a Tweet — they can even help you find topics of interest. 🔬\n\nIn this tutorial, @suhemparack shows us how find Tweets related to COVID-19 using annotations + the filtered stream endpoint.\n\nLearn how you can, too. ⤵️\nhttps://t.co/qwVOgw0zSV"
       }
   ],
   "includes": {
       "users": [
           {
               "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",
               "id": "2244994945",
               "name": "X Developers",
               "username": "XDevelopers"
           }
       ]
   },
   "meta": {
       "newest_id": "1271111223220809728",
       "oldest_id": "1270417572001976322",
       "result_count": 3
   }
}
    
```
:::
:::
:::
:::
