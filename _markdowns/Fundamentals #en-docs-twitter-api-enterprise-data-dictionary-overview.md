::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: c01-rich-text-editor
::: is-table-default
[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}

Tweets are the basic atomic building block of all things Twitter. All
Twitter APIs that return Tweets provide that data encoded using
JavaScript Object Notation (JSON). JSON is based on key-value pairs,
with named attributes and associated values. Tweet objects retrieved
from the API include a Twitter User\'s \"status update\" but Retweets,
replies, and quote Tweets are all also Tweet objects.  If a Tweet is
related to another Tweet, as a Retweet, reply or quote Tweet, each will
be identified or embedded into the Tweet object.  Even the simplest
Tweet in the native Twitter data format, will have nested JSON objects
to represent the other attributes of a Tweet, such as the author,
mentioned users, tagged place location, hashtags, cashtag symbols, media
or URL links.  When working with Twitter data, this is an important
concept to understand. The format of the Tweet data you will receive
from the Twitter API depends on the type of Tweet received, the Twitter
API you are using, and the format settings.

Enterprise endpoints that return Tweet objects have been updated to
provide the metadata needed to understand the Tweet\'s edit history.
Learn more about these metadata on the [\"Edit Tweets\"
fundamentals](/en/docs/twitter-api/edit-tweets) page.

> What did the developer write in their Valentine's card? while(true) {
> I = Love(You);
>
> }
>
> --- Twitter Dev (@TwitterDev) [February 14,
> 2020](https://twitter.com/TwitterDev/status/1228393702244134912?ref_src=twsrc%5Etfw)

In native Twitter format, the JSON payload will include of 'root-level'
attributes, and nested JSON objects (which are represented here with the
` {} ` notation):
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "created_at": "Fri Feb 14 19:00:55 +0000 2020",
    "id_str": "1228393702244134912",
    "text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}",
    "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": []
    },
    "user": {
        "entities": {
            "url": {}
        }
    },
    "place": {}
}
    
```
:::
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
Please note: It is highly recommended to use the [Enriched
Native](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)
format for enterprise data APIs.

-   The Enriched Native format includes all new metadata since 2017,
    such as [poll
    metadata](/en/docs/twitter-api/enterprise/enrichments/overview/poll-metadata.html)
    , and additional metrics such as reply_count and quote_count.

-   Activity Streams format has not been updated with new metadata or
    enrichments since the [character
    update](https://blog.twitter.com/official/en_us/topics/product/2017/Giving-you-more-characters-to-express-yourself.html)
    in 2017.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Enterprise data APIs deliver data in two different formats.  The
enterprise format closest to the standard v1.1 native format is Native
Enriched.  The legacy enterprise data format is Activity Streams,
orignially implimented and used by Gnip as a normalized format across
Twitter and other social media data providers at the time. While this
format is still available, Twitter has only invested new features and
developments on the native enriched format since 2017.\

The enriched native format is exactly how it sounds, it includes native
Twitter objects as well as additional enrichments avialable for
enterprise data products such as URL unwinding metadata, profile geo,
poll metadata and additional engagement metrics.
:::
:::

::: c01-rich-text-editor
::: is-table-default
### Object comparison per data format []{#enterprise-data-objects}

Whatever your Twitter use case, understanding what these JSON-encoded
Tweet objects and attributes *represent* is critical to successfully
finding your data signals of interest. To help in that effort, there are
a set of pages dedicated to each object in each data format *.*

Reflecting the JSON hierarchy above, here are links to each of these
objects:

  Native Enriched                                                                                                              Activity Streams
  ---------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------
  [Link](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet) Tweet object                           [Link](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/tweet) Activity object
  [Link](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/user) User object                             [Link](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/user) Actor object
  [Link](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/entities) Entities object                     [Link](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/entities) Twitter entities object
  [Link](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities) Extended entities object   [Link](extended-entities) Twitter extended entitites object
  [Link](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo) Geo object                               [Link](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/geo) Location object
  n/a                                                                                                                          [Link](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html) Gnip object

## Parsing best-practices []{#parsing-best-practices}

-   Twitter JSON is encoded using UTF-8 characters.
-   Parsers should tolerate variance in the ordering of fields with
    ease. It should be assumed that Tweet JSON is served as an unordered
    hash of data.
-   Parsers should tolerate the addition of \'new\' fields.
-   JSON parsers must be tolerant of 'missing' fields, since not all
    fields appear in all contexts.
-   It is generally safe to consider a nulled field, an empty set, and
    the absence of a field as the same thing

```{=html}
<!-- -->
```
-   Review the enterprise [enriched native data
    dictionary](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/tweet.html)
:::
:::
:::
