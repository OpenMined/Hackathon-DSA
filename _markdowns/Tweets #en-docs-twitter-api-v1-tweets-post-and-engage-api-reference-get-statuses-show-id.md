<div>

::: c01-rich-text-editor
Returns a single
[Tweet](/en/docs/tweets/data-dictionary/overview/tweet-object) ,
specified by the id parameter. The Tweet\'s author will also be embedded
within the Tweet.

See [GET statuses /
lookup](/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup)
for getting Tweets in bulk (up to 100 per call). See also [Embedded
Timelines](/web/embedded-timelines) , [Embedded
Tweets](/web/embedded-tweets) , and [GET
statuses/oembed](/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed)
for tools to render Tweets according to [Display
Requirements](https://about.twitter.com/company/display-requirements) .

**About Geo**

If there is no geotag for a status, then there will be an empty
` <geo></geo> ` or ` "geo" : {} ` . This can only be populated if the
user has used the Geotagging API to send a statuses/update.

The JSON response mostly uses conventions laid out in GeoJSON. The
coordinates that Twitter renders are *reversed* from the GeoJSON
specification (GeoJSON specifies a longitude then a latitude, whereas
Twitter represents it as a latitude then a longitude), eg:
` "geo": { "type":"Point", "coordinates":[37.78029, -122.39697] } `

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/show.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   900
  Requests / 15-min window (app auth)    900
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| Name        | Required    | Description | Default     | Example     |
|             |             |             | Value       |             |
+-------------+-------------+-------------+-------------+-------------+
| id          | required    | The         |             | *123*       |
|             |             | numerical   |             |             |
|             |             | ID of the   |             |             |
|             |             | desired     |             |             |
|             |             | Tweet.      |             |             |
+-------------+-------------+-------------+-------------+-------------+
| trim_user   | optional    | When set to |             | *true*      |
|             |             | either      |             |             |
|             |             | *true* ,    |             |             |
|             |             | *t* or *1*  |             |             |
|             |             | , each      |             |             |
|             |             | Tweet       |             |             |
|             |             | returned in |             |             |
|             |             | a timeline  |             |             |
|             |             | will        |             |             |
|             |             | include a   |             |             |
|             |             | user object |             |             |
|             |             | including   |             |             |
|             |             | only the    |             |             |
|             |             | status      |             |             |
|             |             | authors     |             |             |
|             |             | numerical   |             |             |
|             |             | ID. Omit    |             |             |
|             |             | this        |             |             |
|             |             | parameter   |             |             |
|             |             | to receive  |             |             |
|             |             | the         |             |             |
|             |             | complete    |             |             |
|             |             | user        |             |             |
|             |             | object.     |             |             |
+-------------+-------------+-------------+-------------+-------------+
| include     | optional    | When set to |             | *true*      |
| _my_retweet |             | either      |             |             |
|             |             | *true* ,    |             |             |
|             |             | *t* or *1*  |             |             |
|             |             | , any       |             |             |
|             |             | Tweets      |             |             |
|             |             | returned    |             |             |
|             |             | that have   |             |             |
|             |             | been        |             |             |
|             |             | retweeted   |             |             |
|             |             | by the      |             |             |
|             |             | aut         |             |             |
|             |             | henticating |             |             |
|             |             | user will   |             |             |
|             |             | include an  |             |             |
|             |             | additional  |             |             |
|             |             | *current_us |             |             |
|             |             | er_retweet* |             |             |
|             |             | node,       |             |             |
|             |             | containing  |             |             |
|             |             | the ID of   |             |             |
|             |             | the source  |             |             |
|             |             | status for  |             |             |
|             |             | the         |             |             |
|             |             | retweet.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| inclu       | optional    | The         |             | *false*     |
| de_entities |             | *entities*  |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | *false* .   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| include_e   | optional    | If alt text |             | *true*      |
| xt_alt_text |             | has been    |             |             |
|             |             | added to    |             |             |
|             |             | any         |             |             |
|             |             | attached    |             |             |
|             |             | media       |             |             |
|             |             | entities,   |             |             |
|             |             | this        |             |             |
|             |             | parameter   |             |             |
|             |             | will return |             |             |
|             |             | an          |             |             |
|             |             | *ex         |             |             |
|             |             | t_alt_text* |             |             |
|             |             | value in    |             |             |
|             |             | the         |             |             |
|             |             | top-level   |             |             |
|             |             | key for the |             |             |
|             |             | media       |             |             |
|             |             | entity. If  |             |             |
|             |             | no value    |             |             |
|             |             | has been    |             |             |
|             |             | set, this   |             |             |
|             |             | will be     |             |             |
|             |             | returned as |             |             |
|             |             | ` null `    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| inclu       | optional    | When set to |             | *true*      |
| de_card_uri |             | either      |             |             |
|             |             | *true* ,    |             |             |
|             |             | *t* or *1*  |             |             |
|             |             | , the       |             |             |
|             |             | retrieved   |             |             |
|             |             | Tweet will  |             |             |
|             |             | include a   |             |             |
|             |             | *card_uri*  |             |             |
|             |             | attribute   |             |             |
|             |             | when there  |             |             |
|             |             | is an ads   |             |             |
|             |             | card        |             |             |
|             |             | attached to |             |             |
|             |             | the Tweet   |             |             |
|             |             | and when    |             |             |
|             |             | that card   |             |             |
|             |             | was         |             |             |
|             |             | attached    |             |             |
|             |             | using the   |             |             |
|             |             | *card_uri*  |             |             |
|             |             | value.      |             |             |
+-------------+-------------+-------------+-------------+-------------+
| in          | optional    | Must be set |             | *true*      |
| clude_ext_e |             | to true in  |             |             |
| dit_control |             | order to    |             |             |
|             |             | return      |             |             |
|             |             | edited      |             |             |
|             |             | Tweet       |             |             |
|             |             | metadata as |             |             |
|             |             | part of the |             |             |
|             |             | Tweet       |             |             |
|             |             | object.     |             |             |
|             |             |             |             |             |
|             |             | ` include_e |             |             |
|             |             | xt_edit_con |             |             |
|             |             | trol=true ` |             |             |
|             |             |             |             |             |
|             |             | Note that   |             |             |
|             |             | historical  |             |             |
|             |             | Tweets may  |             |             |
|             |             | not contain |             |             |
|             |             | edited      |             |             |
|             |             | Tweet       |             |             |
|             |             | metadata.   |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/statuses/show.json?id=210462857140252672 `

## Example Response [¶](#example-response){.headerlink}

    {
      "created_at": "Wed Oct 10 20:19:24 +0000 2018",
      "id": 1050118621198921728,
      "id_str": "1050118621198921728",
      "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ and skin t… https://t.co/MkGjXf9aXm",
      "truncated": true,
      "entities": {
        "hashtags": [],
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https://t.co/MkGjXf9aXm",
            "expanded_url": "https://twitter.com/i/web/status/1050118621198921728",
            "display_url": "twitter.com/i/web/status/1…",
            "indices": [
              117,
              140
            ]
          }
        ]
      },
      "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
      "in_reply_to_status_id": null,
      "in_reply_to_status_id_str": null,
      "in_reply_to_user_id": null,
      "in_reply_to_user_id_str": null,
      "in_reply_to_screen_name": null,
      "user": {
        "id": 6253282,
        "id_str": "6253282",
        "name": "Twitter API",
        "screen_name": "TwitterAPI",
        "location": "San Francisco, CA",
        "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
        "url": "https://t.co/8IkCzCDr19",
        "entities": {
          "url": {
            "urls": [
              {
                "url": "https://t.co/8IkCzCDr19",
                "expanded_url": "https://developer.twitter.com",
                "display_url": "developer.twitter.com",
                "indices": [
                  0,
                  23
                ]
              }
            ]
          },
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 6128663,
        "friends_count": 12,
        "listed_count": 12900,
        "created_at": "Wed May 23 06:01:13 +0000 2007",
        "favourites_count": 32,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": null,
        "verified": true,
        "statuses_count": 3659,
        "lang": "null",
        "contributors_enabled": null,
        "is_translator": null,
        "is_translation_enabled": null,
        "profile_background_color": "null",
        "profile_background_image_url": "null",
        "profile_background_image_url_https": "null",
        "profile_background_tile": nulll,
        "profile_image_url": "null",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
        "profile_link_color": "null",
        "profile_sidebar_border_color": "null",
        "profile_sidebar_fill_color": "null",
        "profile_text_color": "null",
        "profile_use_background_image": null,
        "has_extended_profile": null,
        "default_profile": false,
        "default_profile_image": false,
        "following": nul,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "null"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 161,
      "favorite_count": 296,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    }

This request could also be obtained with:
` GET https://api.twitter.com/1.1/statuses/show/210462857140252672.json `
:::

</div>
