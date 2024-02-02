::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Media refers to any image, GIF, or video attached to a Tweet. The media
object is not a primary object on any endpoint, but can be found and
expanded in the Tweet object.

The object is available for expansion with
` ?expansions=attachments.media_keys ` to get the condensed object with
only default fields. Use the expansion with the field parameter:
` media.fields ` when requesting additional fields to complete the
object.

+-----------------+-----------------+-----------------+-----------------+
| Field value     | Type            | Description     | How it can be   |
|                 |                 |                 | used            |
+-----------------+-----------------+-----------------+-----------------+
| media_key       | string          | Unique          | Can be used to  |
| (default)       |                 | identifier of   | p               |
|                 |                 | the expanded    | rogrammatically |
|                 |                 | media content.  | retrieve media  |
|                 |                 |                 |                 |
|                 |                 | ` "media_ke     |                 |
|                 |                 | y": "13_1263145 |                 |
|                 |                 | 212760805376" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| type (default)  | string          | Type of content | Classify the    |
|                 |                 | (animated_gif,  | media as a      |
|                 |                 | photo, video).  | photo, GIF, or  |
|                 |                 |                 | video           |
|                 |                 | ` "t            |                 |
|                 |                 | ype": "video" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| url             | string          | A direct URL to | Returns a Media |
|                 |                 | the media file  | object with a   |
|                 |                 | on Twitter.     | URL field for   |
|                 |                 |                 | photos          |
+-----------------+-----------------+-----------------+-----------------+
| duration_ms     | integer         | Available when  |                 |
|                 |                 | type is video.  |                 |
|                 |                 | Duration in     |                 |
|                 |                 | milliseconds of |                 |
|                 |                 | the video.      |                 |
|                 |                 |                 |                 |
|                 |                 | ` "durati       |                 |
|                 |                 | on_ms": 46947 ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| height          | integer         | Height of this  |                 |
|                 |                 | content in      |                 |
|                 |                 | pixels.         |                 |
|                 |                 |                 |                 |
|                 |                 | ` "             |                 |
|                 |                 | height": 1080 ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| non             | object          | Non-public      | Determine video |
| _public_metrics |                 | engagement      | engagement: how |
|                 |                 | metrics for the | many users      |
|                 |                 | media content   | played through  |
|                 |                 | at the time of  | to each quarter |
|                 |                 | the request.    | of the video.   |
|                 |                 |                 |                 |
|                 |                 | Requires user   |                 |
|                 |                 | context         |                 |
|                 |                 | authentication. |                 |
|                 |                 |                 |                 |
|                 |                 | ` "non_p        |                 |
|                 |                 | ublic_metrics": |                 |
|                 |                 |  { "playback_0_ |                 |
|                 |                 | count": 1561, " |                 |
|                 |                 | playback_100_co |                 |
|                 |                 | unt": 116, "pla |                 |
|                 |                 | yback_25_count" |                 |
|                 |                 | : 559, "playbac |                 |
|                 |                 | k_50_count": 30 |                 |
|                 |                 | 5, "playback_75 |                 |
|                 |                 | _count": 183, ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| organic_metrics | object          | Engagement      | Determine       |
|                 |                 | metrics for the | organic media   |
|                 | \               | media content,  | engagement.     |
|                 |                 | tracked in an   |                 |
|                 |                 | organic         |                 |
|                 |                 | context, at the |                 |
|                 |                 | time of the     |                 |
|                 |                 | request.        |                 |
|                 |                 |                 |                 |
|                 |                 | Requires user   |                 |
|                 |                 | context         |                 |
|                 |                 | authentication. |                 |
|                 |                 |                 |                 |
|                 |                 | ` "organ        |                 |
|                 |                 | ic_metrics": {  |                 |
|                 |                 | "playback_0_cou |                 |
|                 |                 | nt": 1561, "pla |                 |
|                 |                 | yback_100_count |                 |
|                 |                 | ": 116, "playba |                 |
|                 |                 | ck_25_count": 5 |                 |
|                 |                 | 59, "playback_5 |                 |
|                 |                 | 0_count": 305,  |                 |
|                 |                 | "playback_75_co |                 |
|                 |                 | unt": 183, "vie |                 |
|                 |                 | w_count": 629 ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| pr              | string          | URL to the      |                 |
| eview_image_url |                 | static          |                 |
|                 |                 | placeholder     |                 |
|                 |                 | preview of this |                 |
|                 |                 | content.        |                 |
|                 |                 |                 |                 |
|                 |                 | ` "preview_ima  |                 |
|                 |                 | ge_url": "https |                 |
|                 |                 | ://pbs.twimg.co |                 |
|                 |                 | m/media/EYeX7ak |                 |
|                 |                 | WsAIP1_1.jpg" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \               |                 |
+-----------------+-----------------+-----------------+-----------------+
| p               | object          | Engagement      | Determine media |
| romoted_metrics |                 | metrics for the | engagement when |
|                 |                 | media content,  | the Tweet was   |
|                 |                 | tracked in a    | promoted.       |
|                 |                 | promoted        |                 |
|                 |                 | context, at the |                 |
|                 |                 | time of the     |                 |
|                 |                 | request.        |                 |
|                 |                 |                 |                 |
|                 |                 | Requires user   |                 |
|                 |                 | context         |                 |
|                 |                 | authentication. |                 |
|                 |                 |                 |                 |
|                 |                 | ` "pr           |                 |
|                 |                 | omoted_metrics" |                 |
|                 |                 | : { "playback_0 |                 |
|                 |                 | _count": 259, " |                 |
|                 |                 | playback_100_co |                 |
|                 |                 | unt": 15, "play |                 |
|                 |                 | back_25_count": |                 |
|                 |                 |  113, "playback |                 |
|                 |                 | _50_count": 57, |                 |
|                 |                 |  "playback_75_c |                 |
|                 |                 | ount": 25, "vie |                 |
|                 |                 | w_count": 124 ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| public_metrics  | object          | Public          | Determine total |
|                 |                 | engagement      | number of views |
|                 |                 | metrics for the | for the video   |
|                 |                 | media content   | attached to the |
|                 |                 | at the time of  | Tweet.          |
|                 |                 | the request.    |                 |
|                 |                 |                 |                 |
|                 |                 | ` "public_metri |                 |
|                 |                 | cs": { "view_co |                 |
|                 |                 | unt": 6865141 ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| width           | integer         | Width of this   |                 |
|                 |                 | content in      |                 |
|                 |                 | pixels.         |                 |
|                 |                 |                 |                 |
|                 |                 | `               |                 |
|                 |                 | "width": 1920 ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| alt_text        | string          | A description   | Can be used to  |
|                 |                 | of an image to  | provide a       |
|                 |                 | enable and      | written         |
|                 |                 | support         | description of  |
|                 |                 | accessibility.  | an image in     |
|                 |                 | Can be up to    | case a user is  |
|                 |                 | 1000 characters | visually        |
|                 |                 | long. Alt text  | impaired.       |
|                 |                 | can only be     |                 |
|                 |                 | added to images |                 |
|                 |                 | at the moment.  |                 |
|                 |                 |                 |                 |
|                 |                 | [               |                 |
|                 |                 | \"alt_          |                 |
|                 |                 | text\": "Rugged |                 |
|                 |                 | hills along the |                 |
|                 |                 | Na Pali coast   |                 |
|                 |                 | on the island   |                 |
|                 |                 | of Kauai"       |                 |
|                 |                 | ]{.code-inline} |                 |
+-----------------+-----------------+-----------------+-----------------+
| variants        | array           | Each media      |                 |
|                 |                 | object may have |                 |
|                 |                 | multiple        |                 |
|                 |                 | display or      |                 |
|                 |                 | playback        |                 |
|                 |                 | variants, with  |                 |
|                 |                 | different       |                 |
|                 |                 | resolutions or  |                 |
|                 |                 | formats         |                 |
|                 |                 |                 |                 |
|                 |                 | `               |                 |
|                 |                 | "variants": [ ` |                 |
|                 |                 |                 |                 |
|                 |                 | ` { "bit_rat    |                 |
|                 |                 | e": 632000, "co |                 |
|                 |                 | ntent_type":"vi |                 |
|                 |                 | deo/mp4", "url" |                 |
|                 |                 | : "https://vide |                 |
|                 |                 | o.twimg.com/ext |                 |
|                 |                 | _tw_video/15273 |                 |
|                 |                 | 22141724532740/ |                 |
|                 |                 | pu/vid/320x568/ |                 |
|                 |                 | lnBaR2hCqE-R_90 |                 |
|                 |                 | a.mp4?tag=12" ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
|                 |                 |                 |                 |
|                 |                 | ` ] `           |                 |
+-----------------+-----------------+-----------------+-----------------+

### 

### Retrieving a media object

#### Sample Request

In the following request, we are requesting fields for the media object
attached to the Tweet on the [Tweet
lookup](/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint.
Since media is a child object of a Tweet, the ` attachment.media_keys `
expansion is required. Be sure to replace ` $BEARER_TOKEN ` with your
own generated [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/tweets?ids=1263145271946551300&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text' --header 'Authorization: Bearer $BEARER_TOKEN'
    
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
            "text": "Testing, testing...\n\nA new way to have a convo with exactly who you want. We’re starting with a small % globally, so keep your 👀 out to see it in action. https://t.co/pV53mvjAVT",
            "id": "1263145271946551300",
            "attachments": {
                "media_keys": [
                    "13_1263145212760805376"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "duration_ms": 46947,
                "type": "video",
                "height": 1080,
                "media_key": "13_1263145212760805376",
                "public_metrics": {
                    "view_count": 6909260
                },
                "preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg",
                "width": 1920
            }
        ]
    }
}
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
