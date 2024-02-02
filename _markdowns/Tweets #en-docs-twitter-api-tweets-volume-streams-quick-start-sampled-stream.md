::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to a
sampled stream endpoint using a cURL request. cURL is a command-line
tool that allows you to make requests with minimal configuration.

If you would like to see sample code in different languages, please
visit our [Twitter API v2 sample
code](https://github.com/twitterdev/Twitter-API-v2-sample-code) GitHub
repository. The examples there are based on the 1% sampled stream and
are easily updated for the 10% sampled stream. See the repository README
for more details. \

Note: The steps below are also based on making requests to the 1%
sampled stream. If you have Enterprise access and are working with the
10% sampled stream, see the Using the 10% sampled stream section below.
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
In this quick start, we are going to use a simple cURL request to
connect a real-time stream to Twitter that will deliver 1% of all
publicly available Tweets. The sampled stream endpoint is a very simple
one. All you will have to do is replace or add a couple of elements of
the below request and submit it to your command line tool.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X GET "https://api.twitter.com/2/tweets/sample/stream" \
-H "Authorization: Bearer $APP_ACCESS_TOKEN" 
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Since sampled stream requires [OAuth 2.0
App-Only](/en/docs/authentication/oauth-2-0/application-only)
authentication, you will need to replace [ \$APP_ACCESS_TOKEN
]{.code-inline} with the App Access Token that you generated in the
prerequisites.\

#### Step three: Identify and specify which fields you would like to retrieve

If you connect to the stream after step two, you will receive the
default [Tweet
object](/content/developer-twitter/en/docs/twitter-api/object-reference/tweet)
fields in your response: [ id ]{.code-inline} , [ text ]{.code-inline} ,
and [ edit_history_tweet_ids ]{.code-inline} .

If you would like to receive additional fields beyond these default
fields, you will have to specify those fields in your request with the
[field](/content/developer-twitter/en/docs/twitter-api/fields) and/or
[expansion](/content/developer-twitter/en/docs/twitter-api/expansions)
parameters.\

For this exercise, we will request a three different sets of fields from
different objects:

1.  The additional [ tweet.created_at ]{.code-inline} field in the
    primary Tweet objects.
2.  The associated authors' user object's default fields for the
    returned Tweets: [ id ]{.code-inline} , [ name ]{.code-inline} , [
    username ]{.code-inline}
3.  The additional [ user.created_at ]{.code-inline} field in the
    associated user objects.\

To request these fields, you will need to pass the following in your
request:\

  ------------------ ---------------- -------------------------------------------------------------------------------
  **Key**            **Value**        **Returned fields**
  ` tweet.fields `   ` created_at `   ` tweets.created_at `
  ` expansions `     ` author_id `    ` includes.users.id ` , ` includes.users.name ` , ` includes.users.username `
  ` user.fields `    ` created_at `   ` includes.users.created_at `
  ------------------ ---------------- -------------------------------------------------------------------------------

\
Once you\'ve added these, the URL in your cURL request should look like
the following:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://api.twitter.com/2/tweets/sample/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have everything set up, you can submit your request to Twitter
using a command line tool. If done successfully, you will receive a live
stream of Tweets with payloads similar to the following:
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

::: c01-rich-text-editor
::: is-table-default
If you would like to close your connection, you can press Control-C in
your command line tool on either Mac or Windows systems to break the
connection, or you can also close the window.

#### Using the 10% sampled stream

If you have Enterprise access and are working with the 10% sampled
stream, note the following differences:\

-   The request URL changes from [
    api.twitter.com/2/tweets/sample/stream ]{.code-inline} to [
    api.twitter.com/2/tweets/sample10/stream ]{.code-inline} .

-   The 10% sample stream is split into 2 partitions, each requiring a
    connection request. Use the [ partition ]{.code-inline} request
    parameter to indicate which partition you are connecting to:

    -   /2/tweets/sample10/stream&partition=1

    -   /2/tweets/sample10/stream&partition=2
:::
:::
:::
