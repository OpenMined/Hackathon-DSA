::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
By default, the Twitter API v2 data objects include a small number of
default fields when making a request without the use of the
[fields](/en/docs/twitter-api/fields.html) or
[expansions](/en/docs/twitter-api/expansions.html) parameters. This
guide will show you how to use the ` fields ` and ` expansions ` query
parameters in your request to receive additional objects and fields in
your response.

In this guide, we will be requesting several fields in the following
Tweet screenshot.\
:::
:::

::: ct01-columns
:::

::: c01-rich-text-editor
::: is-table-default
As you can see in the screenshot, there are several visible pieces of
information related to the Tweet, including the Tweet author, Tweet
metrics, created timestamp, video, and video view count. There are also
several pieces of data that are not visible within the screenshot, but
are still available to request.

When making a request to the API, the default response is simple,
containing only the default Tweet fields ( [ id ]{.code-inline} and [
text ]{.code-inline} ). You will also only receive the primary object
that returns with the given endpoint that you are using, and not any of
the associated data objects that might relate to the primary object.

This simplicity, along with the fields and expansions parameters, enable
you to request only those fields you require, depending on your use
case.\

### Requesting additional fields and objects.

First off, we will be requesting a [Tweet
object](/en/docs/twitter-api/data-dictionary/object-model/tweet) using a
Tweet ID and the [GET /tweets
endpoint](/en/docs/twitter-api/tweets/lookup/introduction.html) . \

Request:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y"
        }
    ]
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The following step-by-step guide will show you how to retrieve the
additional data we can see in the screenshot. \

1.  Identify the additional fields that you would like to request by
    using our [object
    model](/en/docs/twitter-api/data-dictionary/object-model.html) , or
    by reviewing the list of fields in the endpoints' API reference
    pages. In this case, we will be requesting the following additional
    fields:

    [ attachments ]{.code-inline} , [ author_id ]{.code-inline} , [
    created_at ]{.code-inline} , [ public_metrics ]{.code-inline} , and
    [ source ]{.code-inline}

2.  Build the ` tweet.fields ` query parameter with the above fields as
    its value using a comma-separated list:\
    ` ?tweet.fields=attachments,author_id,created_at,public_metrics,source `

3.  Add the query parameter to the GET /tweets request that you made
    earlier.

Request:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "author_id": "783214",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "source": "Sprinklr",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            },
            "created_at": "2020-05-12T19:44:51.000Z"
        }
    ]
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
4. Next, we are going to request fields related to the video that was
included in the Tweet. To do so, we will use the ` expansions `
parameter with ` attachments.media_keys ` as the value, and add this to
the request.

[ ?expansions=attachments.media_keys ]{.code-inline}

Request:\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Response, with the media object represented in the includes object:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "created_at": "2020-05-12T19:44:51.000Z",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            },
            "author_id": "783214",
            "source": "Sprinklr"
        }
    ],
    "includes": {
        "media": [
            {
                "media_key": "13_1260294804770041858",
                "type": "video"
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
5. And finally, we are going to request the view count and duration of
the video. These aren't default fields so we have to specifically
request them. Use the ` media.fields ` parameter with the
comma-separated values, ` public_metrics ` and ` duration_ms ` in your
request.

[ ?media.fields=public_metrics,duration_ms ]{.code-inline}

Request:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys&media.fields=duration_ms,public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Response, which now includes all the data that can be seen in the Tweet
screenshot:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "author_id": "783214",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "created_at": "2020-05-12T19:44:51.000Z",
            "source": "Sprinklr",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "duration_ms": 36503,
                "media_key": "13_1260294804770041858",
                "public_metrics": {
                    "view_count": 1534703
                },
                "type": "video"
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
In total, we included the following parameters in this example:

-   [ ids=1260294888811347969 ]{.code-inline}
-   [
    tweet.fields=attachments,author_id,created_at,public_metrics,source
    ]{.code-inline}
-   [ expansions=attachments.media_keys ]{.code-inline}
-   [ media.fields=public_metrics,duration_ms ]{.code-inline}\

When tied together, here is what the full query string looks like:

[
?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys&media.fields=public_metrics,duration_ms
]{.code-inline}
:::
:::
:::
