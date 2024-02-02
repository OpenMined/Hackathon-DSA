::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
This quick start guide will help you make your first request to the
filtered stream endpoint group using a cURL request. cURL is a command
line tool which allows you to make requests with minimal configuration.

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
### Steps to build a filtered stream request using cURL

#### Step one: Create a rule

Rules are made up of one or many different
[operators](/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule)
that are combined using boolean logic and parentheses to help define
which Tweets will deliver to your stream. In this guide, we will filter
the stream to find Tweets that contain both the keyword "cat" and
images. Here is our rule:

[ cat has:images ]{.code-inline}

####  Step two: Add a tag to your rule

You can add multiple concurrent rules to your stream. When you open your
streaming connection, Tweets that match any of these rules will flow
through the same streaming connection. To ensure that you know which
Tweet matches which rule, you can pass a tag along with your rule
creation request. Each Tweet that matches that rule will then include a
tag field within the Tweet payload noting which rule it matched. For
this rule, we are going to assign the following tag:

[ cats with images ]{.code-inline}

####  Step three: Add your rule to the stream

This endpoint requires you to pass an application/JSON body along with
this request that contains your rule and its tag. You will also notice
that we have included the rule value and tag within an [ add
]{.code-inline} object since we are trying to add this rule to the
stream. This JSON body will look like this:

    {
      "add": [
        {"value": "cat has:images", "tag": "cats with images"}
      ]
    }

\
Now that you have fully set up this JSON body, you can add that to a
cURL request, which will look like the following. This request isn\'t
ready yet, so please hold off on submitting it until a later step.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X POST 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Content-type: application/json" \
-H "Authorization: Bearer $APP_ACCESS_TOKEN" -d \
'{
  "add": [
    {"value": "cat has:images", "tag": "cats with images"}
  ]
}'

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Since the filtered stream rules endpoints require [OAuth 2.0 App-Only
authentication](/en/docs/authentication/oauth-2-0/application-only) ,
you will need to replace [ \$APP_ACCESS_TOKEN ]{.code-inline} in the
cURL command from step three with the [App Access
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) that you
generated in the prerequisites.\

#### Step five: Add your rule to the stream

Next step is to execute your cURL request, which will add the rule to
your stream. Copy and paste the cURL command into your command line
interface and press \"return\".

If your cURL request was successful, you'll receive a response
containing data about your value, tag, and id (serves as a unique
identifier for your rule). This response will look similar to this:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [{
        "value": "cat has:images",
        "tag": "cats with images",
        "id": "1273026480692322304"
    }],
    "meta": {
        "sent": "2020-06-16T22:55:39.356Z",
        "summary": {
            "created": 1,
            "not_created": 0,
            "valid": 1,
            "invalid": 0
        }
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You can validate that your rule was added successfully by sending the
following GET request to the rules endpoint, once again making sure to
replace [ \$APP_ACCESS_TOKEN ]{.code-inline} with your token. This
request will return a full list of all the rules that have been added to
your stream.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X GET 'https://api.twitter.com/2/tweets/search/stream/rules' \
-H "Authorization: Bearer $APP_ACCESS_TOKEN" 

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If your cURL request was successful, you should receive the following:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [{
        "id": "1273028376882589696",
        "value": "cat has:images",
        "tag": "cats with images"
    }],
    "meta": {
        "sent": "2020-06-16T23:14:06.498Z"
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If you connect to the stream after step five, you will receive the
default [Tweet
object](/en/docs/twitter-api/data-dictionary/object-model/tweet) fields
in your response: [ id ]{.code-inline} , [ text ]{.code-inline} , and [
edit_history_tweet_ids ]{.code-inline} . If you would like to receive
additional fields beyond these, you will have to specify those fields in
your request with the [[ field
]{.code-inline}](/content/developer-twitter/en/docs/twitter-api/fields)
and/or [[ expansion
]{.code-inline}](/content/developer-twitter/en/docs/twitter-api/expansions)
parameters.

For this exercise, we will request a three different sets of fields from
different objects:

1.  The additional [ tweet.created_at ]{.code-inline} field in the
    primary Tweet objects.\
2.  The associated authors' [user
    object's](/en/docs/twitter-api/data-dictionary/object-model/user)
    default fields for the returned Tweets: [ id ]{.code-inline} , [
    name ]{.code-inline} , and [ username ]{.code-inline}
3.  The additional [ user.created_at ]{.code-inline} field in the
    associated user objects.\

To request these fields, you will need to pass the following in your
request:

  ----------------------- ----------------------- -----------------------------------------------------------------
  Key                     Value                   Returned fields

  [ tweet.fields          [ created_at            [ tweets.created_at ]{.code-inline}
  ]{.code-inline}         ]{.code-inline}         

  [ expansions            [ author_id             [ includes.users.id, includes.users.name, includes.users.username
  ]{.code-inline}         ]{.code-inline}         ]{.code-inline}

  [ user.fields           [ created_at            [ includes.users.created_at ]{.code-inline}\
  ]{.code-inline}         ]{.code-inline}         
  ----------------------- ----------------------- -----------------------------------------------------------------

Now that you know this, you can piece together your request URL to
connect to the stream, which will look like this:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Now that your rule is in place and you've specified which fields you
want returned, you're ready to connect to the stream, which will deliver
Tweet objects that match the rule you've submitted. This is what the
cURL command looks like once you've added the URL from step six into
your request:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl -X GET -H "Authorization: Bearer $APP_ACCESS_TOKEN" "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at"
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
Once again, this request must be authenticated using OAuth 2.0 App-Only,
so make sure to replace \$APP_ACCESS_TOKEN with your credentials before
copying and pasting it into your command line tool.

Once you are connected to the filtered stream you will start to receive
Tweets that match your rules in the following JSON format:\
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
      "created_at": "2022-09-14T19:00:55.000Z",
      "id": "1228393702244134912",
      "edit_history_tweet_ids": ["1228393702244134912"],
      "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}"
    },
    {
      "author_id": "2244994945",
      "created_at": "2022-09-12T17:09:56.000Z",
      "id": "1227640996038684673",
       "edit_history_tweet_ids": ["1227640996038684673"],
      "text": "Doctors: Googling stuff online does not make you a doctor\n\nDevelopers: https://t.co/mrju5ypPkb"
    },
    {
      "author_id": "2244994945",
      "created_at": "2022-09-27T20:26:41.000Z",
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
\
If you would like to close your connection, you can press Control-C in
your command line tool on either Mac or Windows systems to break the
connection, or you can also close the window.
:::
:::
:::
