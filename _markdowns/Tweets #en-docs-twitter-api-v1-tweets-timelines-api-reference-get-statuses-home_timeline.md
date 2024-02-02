<div>

::: c01-rich-text-editor
Returns a collection of the most recent
[Tweets](/en/docs/tweets/data-dictionary/overview/tweet-object) and
Retweets posted by the authenticating user and the users they follow.
The home timeline is central to how most users interact with the Twitter
service.

Up to 800 Tweets are obtainable on the home timeline. It is more
volatile for users that follow many users or follow users who Tweet
frequently.

See [Working with
Timelines](/en/docs/tweets/timelines/guides/working-with-timelines) for
instructions on traversing timelines efficiently.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/home_timeline.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  Supports Edit Tweets feature?          Yes
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| Name        | Required    | Description | Default     | Example     |
|             |             |             | Value       |             |
+-------------+-------------+-------------+-------------+-------------+
| count       | optional    | Specifies   |             | *5*         |
|             |             | the number  |             |             |
|             |             | of records  |             |             |
|             |             | to          |             |             |
|             |             | retrieve.   |             |             |
|             |             | Must be     |             |             |
|             |             | less than   |             |             |
|             |             | or equal to |             |             |
|             |             | 200.        |             |             |
|             |             | Defaults to |             |             |
|             |             | 20. The     |             |             |
|             |             | value of    |             |             |
|             |             | count is    |             |             |
|             |             | best        |             |             |
|             |             | thought of  |             |             |
|             |             | as a limit  |             |             |
|             |             | to the      |             |             |
|             |             | number of   |             |             |
|             |             | tweets to   |             |             |
|             |             | return      |             |             |
|             |             | because     |             |             |
|             |             | suspended   |             |             |
|             |             | or deleted  |             |             |
|             |             | content is  |             |             |
|             |             | removed     |             |             |
|             |             | after the   |             |             |
|             |             | count has   |             |             |
|             |             | been        |             |             |
|             |             | applied.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| since_id    | optional    | Returns     |             | *12345*     |
|             |             | results     |             |             |
|             |             | with an ID  |             |             |
|             |             | greater     |             |             |
|             |             | than (that  |             |             |
|             |             | is, more    |             |             |
|             |             | recent      |             |             |
|             |             | than) the   |             |             |
|             |             | specified   |             |             |
|             |             | ID. There   |             |             |
|             |             | are limits  |             |             |
|             |             | to the      |             |             |
|             |             | number of   |             |             |
|             |             | Tweets      |             |             |
|             |             | which can   |             |             |
|             |             | be accessed |             |             |
|             |             | through the |             |             |
|             |             | API. If the |             |             |
|             |             | limit of    |             |             |
|             |             | Tweets has  |             |             |
|             |             | occured     |             |             |
|             |             | since the   |             |             |
|             |             | since_id,   |             |             |
|             |             | the         |             |             |
|             |             | since_id    |             |             |
|             |             | will be     |             |             |
|             |             | forced to   |             |             |
|             |             | the oldest  |             |             |
|             |             | ID          |             |             |
|             |             | available.  |             |             |
+-------------+-------------+-------------+-------------+-------------+
| max_id      | optional    | Returns     |             | *54321*     |
|             |             | results     |             |             |
|             |             | with an ID  |             |             |
|             |             | less than   |             |             |
|             |             | (that is,   |             |             |
|             |             | older than) |             |             |
|             |             | or equal to |             |             |
|             |             | the         |             |             |
|             |             | specified   |             |             |
|             |             | ID.         |             |             |
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
| excl        | optional    | This        |             | *true*      |
| ude_replies |             | parameter   |             |             |
|             |             | will        |             |             |
|             |             | prevent     |             |             |
|             |             | replies     |             |             |
|             |             | from        |             |             |
|             |             | appearing   |             |             |
|             |             | in the      |             |             |
|             |             | returned    |             |             |
|             |             | timeline.   |             |             |
|             |             | Using       |             |             |
|             |             | *exclu      |             |             |
|             |             | de_replies* |             |             |
|             |             | with the    |             |             |
|             |             | *count*     |             |             |
|             |             | parameter   |             |             |
|             |             | will mean   |             |             |
|             |             | you will    |             |             |
|             |             | receive     |             |             |
|             |             | up-to count |             |             |
|             |             | Tweets ---  |             |             |
|             |             | this is     |             |             |
|             |             | because the |             |             |
|             |             | *count*     |             |             |
|             |             | parameter   |             |             |
|             |             | retrieves   |             |             |
|             |             | that many   |             |             |
|             |             | Tweets      |             |             |
|             |             | before      |             |             |
|             |             | filtering   |             |             |
|             |             | out         |             |             |
|             |             | retweets    |             |             |
|             |             | and         |             |             |
|             |             | replies.    |             |             |
+-------------+-------------+-------------+-------------+-------------+
| inclu       | optional    | The         |             | *false*     |
| de_entities |             | *entities*  |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | *false* .   |             |             |
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
|             |             |             |             |             |
|             |             | To learn    |             |             |
|             |             | more about  |             |             |
|             |             | how edited  |             |             |
|             |             | Tweets are  |             |             |
|             |             | supported,  |             |             |
|             |             | see the     |             |             |
|             |             | [Edit       |             |             |
|             |             | Tweets      |             |             |
|             |             | fu          |             |             |
|             |             | ndamentals] |             |             |
|             |             | (https://de |             |             |
|             |             | veloper.twi |             |             |
|             |             | tter.com/en |             |             |
|             |             | /docs/twitt |             |             |
|             |             | er-api/v1/e |             |             |
|             |             | dit-tweets) |             |             |
|             |             | page.       |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/statuses/home_timeline.json `

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
:::

</div>
