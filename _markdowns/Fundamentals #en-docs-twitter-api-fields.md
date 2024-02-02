::: main-content__wrapper
::: c01-rich-text-editor
<div>

The Twitter API v2 endpoints are equipped with a set of parameters
called *fields,* which allows you to select just the data that you want
from each of the objects in your endpoint response.

By default, the Tweet object only returns the [ id ]{.code-inline} and
the [ text ]{.code-inline} fields, and for Tweets created since
September 29, 2022, the [ edit_history_tweet_ids ]{.code-inline} field.
If you need the Tweet's created date or public metrics, you will need to
use the [ tweet.fields ]{.code-inline} parameters to request them. This
provides a higher degree of customization by enabling you to only
request the fields you require depending on your use case. For example,
you would include this query string in your request

[ ?tweet.fields=created_at,public_metrics ]{.code-inline}

Each object has its own parameter which is used to specifically request
the fields that are associated with that object. Here are the different
fields parameters that are currently available: \

When using an endpoint that primarily returns a particular object,
simply use the matching field parameter and specify the field(s) desired
in a comma-separated list as the value to that parameter to retrieve
those fields in the response.

### Example

If you are using the [GET
/tweets/search/recent](/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent)
endpoint, you will primarily receive [Tweet
objects](/en/docs/twitter-api/data-dictionary/object-model/tweet) in
that response. Without specifying any fields parameters, you will just
receive the default values, ` id ` and ` text ` . If you are interested
in receiving the public metrics of the Tweets that are returned in the
response, you will want to include the ` tweet.fields ` parameter in
your request, with ` public_metrics ` set as the value.

This request would look like the following. If you would like to use
this request, make sure to replace [ \$BEARER_TOKEN ]{.code-inline} with
your [Bearer Token](/en/docs/authentication/oauth-2-0/bearer-tokens) and
send it using your command line tool.\

</div>
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
If you send this request in your terminal, then each of the Tweets that
return will include the following fields:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
   "data": {
       "id": "1263150595717730305",
       "public_metrics": {
           "retweet_count": 12,
           "reply_count": 14,
           "like_count": 49,
           "quote_count": 7
       },
       "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER"
   }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If you would like to retrieve a set of fields from a secondary object
that is associated with the primary object returned by an endpoint, you
will need to include an additional
` `[`expansions`](/en/docs/twitter-api/expansions.html)` ` parameter.

For example, if you were using the same GET search/tweets/recent
endpoint as earlier, and you wanted to retrieve the author\'s profile
description, you will have to pass the [ expansions=author_id
]{.code-inline} and [ user.fields=description ]{.code-inline} with your
request. Here is an example of what this might look like. If you would
like to try this request, make sure to replace the [ \$BEARER_TOKEN
]{.code-inline} with your [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) before pasting
it into your command line tool.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics&expansions=author_id&user.fields=description' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
If you specify this in the request, then each of the Tweets that deliver
will have the following fields, and the related [user
object\'s](/en/docs/twitter-api/data-dictionary/object-model/user)
default and specified fields will return within [ includes
]{.code-inline} . The user object can be mapped back to the
corresponding Tweet(s) by matching the [ tweet.author_id ]{.code-inline}
and [ users.id ]{.code-inline} fields.\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "data": [
    {
      "id": "1263150595717730305",
      "author_id": "2244994945",
      "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER",
      "public_metrics": {
        "retweet_count": 12,
        "reply_count": 13,
        "like_count": 51,
        "quote_count": 7
      }
    }
  ],
  "includes": {
    "users": [
      {
        "id": "2244994945",
        "username": "TwitterDev",
        "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "name": "Twitter Dev"
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
Bear in mind that you cannot request specific subfields (for example,
` public_metrics.retweet_count ` ). All subfields will be returned when
the top-level field ( ` public_metrics ` ) is specified. We have listed
all possible fields that you can request in each endpoints\' API
reference page\'s parameters table.

A full list of fields are listed in the [object
model](/en/docs/twitter-api/data-dictionary/object-model.html) . To
expand and request fields on an object that is not that endpoint's
primary resource, use the
[expansions](/en/docs/twitter-api/expansions.html) parameter with
fields.
:::
:::
:::
