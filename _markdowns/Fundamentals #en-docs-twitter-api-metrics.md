::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The metrics field allows developers to access public and private
engagement metrics for Tweet and media objects. Public metrics are
accessible by anyone with a developer account while private metrics are
accessible from owned/authorized accounts (definition below). By
metrics, we mean the total count of impressions, Retweets, Quote Tweets,
likes, replies, video views, video view quartiles, URL and profile link
clicks for each Tweet specified in the request. There is also the option
to view a breakdown of metrics earned in an organic or promoted context,
if the Tweet was promoted as an [Ad](https://ads.twitter.com/) .

Public metrics can be requested with [App only
Token](/en/docs/authentication/oauth-2-0) authentication. Non-public
metrics can be requested for owned/authorized Tweets only. This means
developers are required to authenticate using [OAuth
2.0](/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth
1.0a](/en/docs/authentication/oauth-1-0a) user context authorization.

**Non-public, organic, and promoted metrics are only available for
Tweets that have been created within the last 30 days.\
**

### Terminology

-   **Authorized account** : Twitter account that has authorized your
    [Twitter developer app](/en/docs/apps/overview) by granting it
    access to that account (any [app permission
    level](/en/docs/apps/app-permissions) will permit access to Tweet
    metrics). This can be achieved using the [Authorization Code Flow
    with
    PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token)
    or [3-legged
    OAuth](/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
    process.
-   **Owned account** : Twitter account linked to your [Twitter
    developer app](/en/docs/apps/overview) .
-   **Public metrics** : Metrics' totals that are available for anyone
    to access on [Twitter](https://twitter.com/home) , such as number of
    likes and number of Retweets.
-   **Non-public metrics** : Metrics' totals that are not available for
    anyone to view on [Twitter](https://twitter.com/home) , such as
    number of impressions and video view quartiles. Requires [OAuth
    2.0](/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth
    1.0a](/en/docs/authentication/oauth-1-0a) user
    context authentication.
-   **Organic metrics** : Grouping of public and non-public metrics
    attributed to an organic context (posted and viewed in a regular
    manner). Requires [OAuth
    2.0](/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth
    1.0a](/en/docs/authentication/oauth-1-0a) user
    context authentication.
-   **Promoted metrics** : Grouping of public and non-public metrics
    attributed to a promoted context (posted or viewed as part of an Ads
    campaign). Requires [OAuth
    2.0](/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth
    1.0a](/en/docs/authentication/oauth-1-0a) user
    context authentication and that the Tweet was promoted in an Ad.
    Promoted metrics are not included in these counts when a Twitter
    user is using their own Ads account to promote another Twitter
    user\'s Tweets. Promoted metrics are included in these counts when:
    -   a Twitter user promotes their own Tweets
    -   in an Ads account for a specific handle, the admin for that
        account may add another Twitter user as an account user so this
        second account user can promote Tweets for the handle

## 

## Available Metrics

+-----------------------+-----------------------+-----------------------+
| **Metric**            | **API                 | **Description**       |
|                       | Representations**     |                       |
+-----------------------+-----------------------+-----------------------+
| Impressions           | ` data.non_public_m   | A count of how many   |
|                       | etrics.impression_cou | times the Tweet has   |
|                       | nt data.organic_metri | been viewed (not      |
|                       | cs.impression_count ` | unique by user). A    |
|                       |                       | view is counted if    |
|                       | data.promoted_met     | any part of the Tweet |
|                       | rics.impression_count | is visible on the     |
|                       |                       | screen.               |
|                       |                       |                       |
|                       |                       | This is a private, or |
|                       |                       | non-public, metric    |
|                       |                       | and always requires   |
|                       |                       | OAuth 1.0a User       |
|                       |                       | Context               |
|                       |                       | authentication.       |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | `                     |
|                       |                       |  non_public_metrics ` |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | impressions from both |
|                       |                       | organic and paid      |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the count of          |
|                       |                       | impressions from      |
|                       |                       | organic contexts.     |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the count of          |
|                       |                       | impressions from      |
|                       |                       | promoted contexts.    |
+-----------------------+-----------------------+-----------------------+
| Retweets              | ` data.pu             | A count of how many   |
|                       | blic_metrics.retweet_ | times the Tweet has   |
|                       | count data.organic_me | been Retweeted.       |
|                       | trics.retweet_count ` | Please note: This     |
|                       |                       | does not include      |
|                       | data.promoted_        | Quote Tweets          |
|                       | metrics.retweet_count | ("Retweets with       |
|                       |                       | comment"). To get the |
|                       |                       | \"Retweets and        |
|                       |                       | comments\" total as   |
|                       |                       | displayed on the      |
|                       |                       | Twitter clients,      |
|                       |                       | simply add            |
|                       |                       | ` retweet_count ` and |
|                       |                       | ` quote_count ` .     |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` public_metrics `    |
|                       |                       | field, this will      |
|                       |                       | return the total      |
|                       |                       | count of Retweets     |
|                       |                       | from both organic and |
|                       |                       | paid contexts, in     |
|                       |                       | order to maintain     |
|                       |                       | consistency with the  |
|                       |                       | counts shown publicly |
|                       |                       | on Twitter.           |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | Retweets from organic |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | Retweets from paid    |
|                       |                       | contexts.             |
+-----------------------+-----------------------+-----------------------+
| Quote Tweets          | ` data.public_        | A count of how many   |
|                       | metrics.quote_count ` | times the Tweet has   |
|                       |                       | been Retweeted with a |
|                       |                       | new comment           |
|                       |                       | (message). Please     |
|                       |                       | note: This does not   |
|                       |                       | include Retweets. To  |
|                       |                       | get the "Retweets and |
|                       |                       | comments" total as    |
|                       |                       | displayed on the      |
|                       |                       | Twitter clients,      |
|                       |                       | simply add            |
|                       |                       | ` retweet_count ` and |
|                       |                       | ` quote_count ` .     |
|                       |                       |                       |
|                       |                       | This will return the  |
|                       |                       | total count of Quote  |
|                       |                       | Tweets. There are no  |
|                       |                       | Quote Tweets from a   |
|                       |                       | paid context so all   |
|                       |                       | Quote Tweets are      |
|                       |                       | organic.              |
+-----------------------+-----------------------+-----------------------+
| Likes                 | ` d                   | A count of how many   |
|                       | ata.public_metrics.li | times the Tweet has   |
|                       | ke_count data.organic | been liked.           |
|                       | _metrics.like_count ` |                       |
|                       |                       | Using the             |
|                       | data.promot           | ` public_metrics `    |
|                       | ed_metrics.like_count | field, this will      |
|                       |                       | return the total      |
|                       |                       | count of likes from   |
|                       |                       | both organic and paid |
|                       |                       | contexts, in order to |
|                       |                       | maintain consistency  |
|                       |                       | with the counts shown |
|                       |                       | publicly on Twitter.  |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | Retweets from organic |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | Retweets from paid    |
|                       |                       | contexts.             |
+-----------------------+-----------------------+-----------------------+
| Replies               | ` dat                 | A count of how many   |
|                       | a.public_metrics.repl | times the Tweet has   |
|                       | y_count data.organic_ | been replied to.      |
|                       | metrics.reply_count ` |                       |
|                       |                       | Using the             |
|                       | data.promote          | ` public_metrics `    |
|                       | d_metrics.reply_count | field, this will      |
|                       |                       | return the total      |
|                       |                       | count of replies from |
|                       |                       | both organic and paid |
|                       |                       | contexts, in order to |
|                       |                       | maintain consistency  |
|                       |                       | with the counts shown |
|                       |                       | publicly on Twitter.  |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | replies from organic  |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | replies from paid     |
|                       |                       | contexts.             |
+-----------------------+-----------------------+-----------------------+
| URL Link Clicks       | ` data.non_public     | A count of the number |
|                       | _metrics.url_link_cli | of times a user       |
|                       | cks data.organic_metr | clicks on a URL link  |
|                       | ics.url_link_clicks ` | or URL preview card   |
|                       |                       | in a Tweet.           |
|                       | data.promoted_me      |                       |
|                       | trics.url_link_clicks | This is a private, or |
|                       |                       | non-public, metric    |
|                       |                       | and always requires   |
|                       |                       | OAuth 1.0a User       |
|                       |                       | Context               |
|                       |                       | authentication.       |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | `                     |
|                       |                       |  non_public_metrics ` |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | URL link clicks from  |
|                       |                       | both organic and paid |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the count of URL link |
|                       |                       | clicks from organic   |
|                       |                       | contexts.             |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the count of URL link |
|                       |                       | clicks from paid      |
|                       |                       | contexts.             |
+-----------------------+-----------------------+-----------------------+
| User Profile Clicks   | ` da                  | A count of the number |
|                       | ta.non_public_metrics | of times a user       |
|                       | .user_profile_clicks  | clicks the following  |
|                       | data.organic_metrics. | portions of a Tweet:  |
|                       | user_profile_clicks ` | display name, user    |
|                       |                       | name, profile         |
|                       | data.promoted_metric  | picture.              |
|                       | s.user_profile_clicks |                       |
|                       |                       | This is a private, or |
|                       |                       | non-public, metric    |
|                       |                       | and always requires   |
|                       |                       | OAuth 1.0a User       |
|                       |                       | Context               |
|                       |                       | authentication.       |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | `                     |
|                       |                       |  non_public_metrics ` |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | user profile clicks   |
|                       |                       | from both organic and |
|                       |                       | paid contexts.        |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the count of user     |
|                       |                       | profile clicks from   |
|                       |                       | organic contexts.     |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the count of user     |
|                       |                       | profile clicks from   |
|                       |                       | paid contexts.        |
+-----------------------+-----------------------+-----------------------+
| Video views           | `                     | A count of how many   |
|                       | includes.media.public | times the video       |
|                       | _metrics.view_count i | included in the Tweet |
|                       | ncludes.media.organic | has been viewed.      |
|                       | _metrics.view_count ` |                       |
|                       |                       | This is the number of |
|                       | includes.media.promot | video views           |
|                       | ed_metrics.view_count | aggregated across all |
|                       |                       | Tweets in which the   |
|                       |                       | given video has been  |
|                       |                       | posted. That means    |
|                       |                       | that the metric       |
|                       |                       | includes the combined |
|                       |                       | views from any        |
|                       |                       | instance where the    |
|                       |                       | video has been        |
|                       |                       | Retweeted or reposted |
|                       |                       | in separate Tweets.   |
|                       |                       |                       |
|                       |                       | Use expansion for     |
|                       |                       | media objects,        |
|                       |                       | ` expansions=at       |
|                       |                       | tachment.media_keys ` |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` public_metrics `    |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | video views from both |
|                       |                       | organic and paid      |
|                       |                       | contexts, in order to |
|                       |                       | maintain consistency  |
|                       |                       | with the counts shown |
|                       |                       | publicly on Twitter.  |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` organic_metrics `   |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | video views from      |
|                       |                       | organic contexts.     |
|                       |                       |                       |
|                       |                       | Using the             |
|                       |                       | ` promoted_metrics `  |
|                       |                       | field, this returns   |
|                       |                       | the total count of    |
|                       |                       | video views from paid |
|                       |                       | contexts.             |
+-----------------------+-----------------------+-----------------------+
| Video view quartiles  | ` includes.media.non_ | The number of users   |
|                       | public_metrics.playba | who played through to |
|                       | ck_0_count includes.m | each quartile in a    |
|                       | edia.non_public_metri | video. This reflects  |
|                       | cs.playback_25_count  | the number of         |
|                       | includes.media.non_pu | quartile views across |
|                       | blic_metrics.playback | all Tweets in which   |
|                       | _50_count includes.me | the given video has   |
|                       | dia.non_public_metric | been posted.          |
|                       | s.playback_75_count ` |                       |
|                       |                       | This is a private, or |
|                       | includes.m            | non-public, metric    |
|                       | edia.non_public_metri | and always requires   |
|                       | cs.playback_100_count | OAuth 1.0a User       |
|                       |                       | Context               |
|                       | \                     | authentication.       |
|                       |                       |                       |
|                       | ` include             | Use expansion for     |
|                       | s.media.organic_metri | media objects,        |
|                       | cs.playback_0_count i | ` expansions=at       |
|                       | ncludes.media.organic | tachment.media_keys ` |
|                       | _metrics.playback_25_ | .                     |
|                       | count includes.media. |                       |
|                       | organic_metrics.playb | Using the             |
|                       | ack_50_count includes | `                     |
|                       | .media.organic_metric |  non_public_metrics ` |
|                       | s.playback_75_count ` | field, this returns   |
|                       |                       | the total count of    |
|                       | include               | video view quartiles  |
|                       | s.media.organic_metri | from both organic and |
|                       | cs.playback_100_count | paid contexts.        |
|                       |                       |                       |
|                       | \                     | Using the             |
|                       |                       | ` organic_metrics `   |
|                       | `                     | field, this returns   |
|                       |  includes.media.promo | the total count of    |
|                       | ted_metrics.playback_ | video view quartiles  |
|                       | 0_count includes.medi | from organic          |
|                       | a.promoted_metrics.pl | contexts.             |
|                       | ayback_25_count inclu |                       |
|                       | des.media.promoted_me | Using the             |
|                       | trics.playback_50_cou | ` promoted_metrics `  |
|                       | nt includes.media.pro | field, this returns   |
|                       | moted_metrics.playbac | the total count of    |
|                       | k_75_count includes.m | video view quartiles  |
|                       | edia.promoted_metrics | from paid contexts.   |
|                       | .playback_100_count ` |                       |
+-----------------------+-----------------------+-----------------------+

## Requesting metrics

### Public metrics

In the following request, we are requesting public metrics on the Tweet
and on the attached video with the following fields and expansion. Be
sure to replace ` $BEARER_TOKEN ` with your own generated bearer token.

-    tweet.fields=public_metrics
-    expansions=attachments.media_keys&media.fields=public_metrics
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets?ids=1204084171334832128&tweet.fields=public_metrics&expansions=attachments.media_keys&media.fields=public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'
    
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
            "id": "1204084171334832128",
            "text": "Tired of reading? We’ve got you covered. Learn about the capabilities of the Account Activity API in this video walkthrough with @tonyv00 from our DevRel team. 🍿 ⬇️ https://t.co/LdHy4aLu0i",
            "public_metrics": {
                "retweet_count": 9,
                "reply_count": 2,
                "like_count": 49,
                "quote_count": 1
            },
            "attachments": {
                "media_keys": [
                    "13_1204080851740315648"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "media_key": "13_1204080851740315648",
                "public_metrics": {
                    "view_count": 1808
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
In the following request, we are requesting non-public metrics with more
details or organic metrics, meaning which of these metrics
were generated in an organic context, on the Tweet and attached video
with the following fields and expansion. Since these fields are private
(not available to view on Twitter.com),Requires [OAuth
2.0](/en/docs/authentication/oauth-2-0/authorization-code) or [OAuth
1.0a](/en/docs/authentication/oauth-1-0a) user
context authentication. is required for the request. Check out our
[guide](/en/docs/authentication/oauth-1-0a/creating-a-signature) that
explains how to generate the OAuth 1.0a signature sampled below.

-   ` tweet.fields=non_public_metrics,organic_metrics `
-   ` expansions=attachments.media_keys&media.fields=non_public_metrics,organic_metrics `

**Sample Request**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets/1204084171334832128?tweet.fields=non_public_metrics,organic_metrics&media.fields=non_public_metrics,organic_metrics&expansions=attachments.media_keys'
--header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY", oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP", oauth_token="ACCESS_TOKEN", oauth_version="1.0"'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "data": {
    "attachments": {
      "media_keys": [
        "13_1204080851740315648"
      ]
    },
    "id": "1263145271946551300",
    "non_public_metrics": {
      "impression_count": 956,
      "url_link_clicks": 9,
       "user_profile_clicks": 34
    },
    "organic_metrics": {
      "impression_count": 956,
      "like_count": 49,
      "reply_count": 2,
      "retweet_count": 9,
      "url_link_clicks": 9,
       "user_profile_clicks": 34
    },
    "text": "test"
  },
  "includes": {
    "media": [
      {
        "media_key": "13_1204080851740315648",
        "non_public_metrics": {
          "playback_0_count": 0,
          "playback_100_count": 1,
          "playback_25_count": 2,
          "playback_50_count": 1,
          "playback_75_count": 1
        },
        "organic_metrics": {
          "playback_0_count": 0,
          "playback_100_count": 1,
          "playback_25_count": 2,
          "playback_50_count": 1,
          "playback_75_count": 1,
          "view_count": 1
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
:::
