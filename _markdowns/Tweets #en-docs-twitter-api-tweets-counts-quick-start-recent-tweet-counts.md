::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
recent Tweet counts endpoint using Postman, a graphical tool that allows
you to send HTTP requests.

If you would like to see sample code in different programming languages,
please visit our [Twitter API v2 sample
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
to the Tweet counts \> Recent Tweet counts request.

####  Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that
you have permission. To do so with this endpoint, you must authenticate
your request with the [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only)
authentication methods.

You must add your keys and tokens, specifically the [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) (also known as
the App-only Bearer Token) to Postman. You can do this by selecting the
environment named "Twitter API v2" in the top-right corner of Postman
and adding your keys and tokens to the \"initial value\" and \"current
value\" fields (by clicking the eye icon next to the environment
dropdown).

This variable will automatically be pulled into the request\'s
authorization tab if you\'ve done this correctly.\

#### Step three: Create a query

Each recent Tweet counts request requires a single
[query](/en/docs/twitter-api/tweets/counts/integrate/build-a-query) .
For this example, we are going to use a query that matches on Tweets
posted by the \@XDevelopers account. For this query we use the [ from:
]{.code-inline} operator and set it to [ XDevelopers ]{.code-inline}
(case insensitive):

` from:XDevelopers `

In Postman, navigate to the \"Params\" tab and enter this ID, or a
string of Tweet IDs separated by a comma, into the \"Value\" column of
the ` ids ` parameter.

  ----------- ------------------------------------ -----------------------------------------------------
  **Key**     **Value**                            **Description**
  ` query `   [ from:XDevelopers ]{.code-inline}   Query to submit to the recent Tweet counts endpoint
  ----------- ------------------------------------ -----------------------------------------------------

#### Step four (optional): Specify the granularity of the request

If you click the 'Send' button after step three, you will get the
default recent Tweet counts: by hour for the last seven days. If you
want to get recent Tweet counts by day, you will have to add the [
granularity ]{.code-inline} parameter with a value of [ day
]{.code-inline} .

In Postman, navigate to the \"Params\" tab and day into the \"Value\"
column of the [ granularity ]{.code-inline} parameter.

  ------------------------------- ----------------------- ---------------------------------------------------------------------------------------
  **Key**                         **Value**               **Description**
  [ granularity ]{.code-inline}   [ day ]{.code-inline}   The granularity for the Tweet counts results. Possible values are day, hour or minute
  ------------------------------- ----------------------- ---------------------------------------------------------------------------------------

\
You should now see the following URL next to the \"Send\" button: \

</div>
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/tweets/counts/recent?query=from%3AXDevelopers&granularity=day
    
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
           "end": "2021-06-16T00:00:00.000Z",
           "start": "2021-06-15T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-17T00:00:00.000Z",
           "start": "2021-06-16T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-06-18T00:00:00.000Z",
           "start": "2021-06-17T00:00:00.000Z",
           "tweet_count": 2
       },
       {
           "end": "2021-06-19T00:00:00.000Z",
           "start": "2021-06-18T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-20T00:00:00.000Z",
           "start": "2021-06-19T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-21T00:00:00.000Z",
           "start": "2021-06-20T00:00:00.000Z",
           "tweet_count": 0
       },
       {
           "end": "2021-06-22T00:00:00.000Z",
           "start": "2021-06-21T00:00:00.000Z",
           "tweet_count": 1
       },
       {
           "end": "2021-06-23T00:00:00.000Z",
           "start": "2021-06-22T00:00:00.000Z",
           "tweet_count": 2
       }
   ],
   "meta": {
       "total_tweet_count": 6
   }
}
    
```
:::
:::
:::
:::
