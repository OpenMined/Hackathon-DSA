::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
This is the standard v1.1 data dictionary. We also have data
dictionaries for [premium
v1.1](/en/docs/twitter-api/premium/data-dictionary) ,
[enterprise](/en/docs/twitter-api/enterprise/data-dictionary) , and
[Twitter API v2](/en/docs/twitter-api/data-dictionary) .

If you are migrating from a standard v1.1 endpoint to a v2 endpoint,
we\'ve put together a [data format migration
guide](/en/docs/twitter-api/migrate/data-formats) that you can use to
map standard v1.1 fields to v2 fields. This guide will also let you know
which fields and expansions parameters you will need to include in your
request to return specific v2 fields.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
[ Standard ]{.subscription-tag .subscription-tag--standard}

All Twitter APIs that return Tweets provide that data encoded using
JavaScript Object Notation (JSON). JSON is based on key-value pairs,
with named attributes and associated values. These attributes, and their
state are used to describe objects.\

At Twitter we serve many objects as JSON, including *Tweets and* *Users*
. These objects all encapsulate core attributes that describe the
object. Each Tweet has an author, a message, a unique ID, a timestamp of
when it was posted, and sometimes geo metadata shared by the user. Each
User has a Twitter name, an ID, a number of followers, and most often an
account bio.

With each Tweet we also generate \"entity\" objects, which are arrays of
common Tweet contents such as hashtags, mentions, media, and links. If
there are links, the JSON payload can also provide metadata such as the
fully unwound URL and the webpage's title and description.

So, in addition to the text content itself, a Tweet can have over 150
attributes associated with it. Let's start with an example Tweet:
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
The following JSON illustrates the structure for these objects and some
of their attributes:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "created_at": "Thu Apr 06 15:24:15 +0000 2017",
  "id_str": "850006245121695744",
  "text": "1\/ Today we\u2019re sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",
  "user": {
    "id": 2244994945,
    "name": "Twitter Dev",
    "screen_name": "TwitterDev",
    "location": "Internet",
    "url": "https:\/\/dev.twitter.com\/",
    "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
  },
  "place": {   
  },
  "entities": {
    "hashtags": [      
    ],
    "urls": [
      {
        "url": "https:\/\/t.co\/XweGngmxlP",
        "unwound": {
          "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
          "title": "Building the Future of the Twitter API Platform"
        }
      }
    ],
    "user_mentions": [     
    ]
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
:::
:::
