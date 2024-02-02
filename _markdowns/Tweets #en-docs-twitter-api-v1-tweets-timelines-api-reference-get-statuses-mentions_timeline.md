<div>

::: c01-rich-text-editor
**Important notice:** On June 19, 2019, we began enforcing a limit of
100,000 requests per day to the /statuses/mentions_timeline endpoint.
This is in addition to existing user-level rate limits (75 requests /
15-minutes). This limit is enforced on a per-application basis, meaning
that a single developer app can make up to 100,000 calls during any
single 24-hour period.

Returns the 20 most recent mentions (Tweets containing a users\'s
\@screen_name) for the authenticating user.

The timeline returned is the equivalent of the one seen when you view
[your mentions](http://twitter.com/mentions) on twitter.com.

This method can only return up to 800 tweets.

See [Working with
Timelines](/en/docs/tweets/timelines/guides/working-with-timelines) for
instructions on traversing timelines.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/statuses/mentions_timeline.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  Requests / 24-hour window              100,000
  Supports Edit Tweets feature?          Yes
  -------------------------------------- -------------------------

*Note:* the 24-hour request limit is based on a rolling clock, beginning
at the time of the first request and monitored for the next 24 hours.

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| Name        | Required    | Description | Default     | Example     |
|             |             |             | Value       |             |
+-------------+-------------+-------------+-------------+-------------+
| count       | optional    | Specifies   |             |             |
|             |             | the number  |             |             |
|             |             | of Tweets   |             |             |
|             |             | to try and  |             |             |
|             |             | retrieve,   |             |             |
|             |             | up to a     |             |             |
|             |             | maximum of  |             |             |
|             |             | 200. The    |             |             |
|             |             | value of    |             |             |
|             |             | *count* is  |             |             |
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
|             |             | applied. We |             |             |
|             |             | include     |             |             |
|             |             | retweets in |             |             |
|             |             | the count,  |             |             |
|             |             | even if     |             |             |
|             |             | *i          |             |             |
|             |             | nclude_rts* |             |             |
|             |             | is not      |             |             |
|             |             | supplied.   |             |             |
|             |             | It is       |             |             |
|             |             | recommended |             |             |
|             |             | you always  |             |             |
|             |             | send        |             |             |
|             |             | *inc        |             |             |
|             |             | lude_rts=1* |             |             |
|             |             | when using  |             |             |
|             |             | this API    |             |             |
|             |             | method.     |             |             |
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
|             |             | tweet       |             |             |
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

` GET https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=2&since_id=14927799 `

## Example Response [¶](#example-response){.headerlink}

    [
      {
        "coordinates": null,
        "favorited": false,
        "truncated": false,
        "created_at": "Mon Sep 03 13:24:14 +0000 2012",
        "id_str": "242613977966850048",
        "entities": {
          "urls": [

          ],
          "hashtags": [

          ],
          "user_mentions": [
            {
              "name": "Jason Costa",
              "id_str": "14927800",
              "id": 14927800,
              "indices": [
                0,
                11
              ],
              "screen_name": "jasoncosta"
            },
            {
              "name": "Matt Harris",
              "id_str": "777925",
              "id": 777925,
              "indices": [
                12,
                26
              ],
              "screen_name": "themattharris"
            },
            {
              "name": "ThinkWall",
              "id_str": "117426578",
              "id": 117426578,
              "indices": [
                109,
                119
              ],
              "screen_name": "thinkwall"
            }
          ]
        },
        "in_reply_to_user_id_str": "14927800",
        "contributors": null,
        "text": "@jasoncosta @themattharris Hey! Going to be in Frisco in October. Was hoping to have a meeting to talk about @thinkwall if you're around?",
        "retweet_count": 0,
        "in_reply_to_status_id_str": null,
        "id": 242613977966850048,
        "geo": null,
        "retweeted": false,
        "in_reply_to_user_id": 14927800,
        "place": null,
        "user": {
          "profile_sidebar_fill_color": "EEEEEE",
          "profile_sidebar_border_color": "000000",
          "profile_background_tile": false,
          "name": "Andrew Spode Miller",
          "profile_image_url": "http://a0.twimg.com/profile_images/1227466231/spode-balloon-medium_normal.jpg",
          "created_at": "Mon Sep 22 13:12:01 +0000 2008",
          "location": "London via Gravesend",
          "follow_request_sent": false,
          "profile_link_color": "F31B52",
          "is_translator": false,
          "id_str": "16402947",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "http://www.linkedin.com/in/spode",
                  "indices": [
                    0,
                    32
                  ]
                }
              ]
            },
            "description": {
              "urls": [

              ]
            }
          },
          "default_profile": false,
          "contributors_enabled": false,
          "favourites_count": 16,
          "url": "http://www.linkedin.com/in/spode",
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1227466231/spode-balloon-medium_normal.jpg",
          "utc_offset": 0,
          "id": 16402947,
          "profile_use_background_image": false,
          "listed_count": 129,
          "profile_text_color": "262626",
          "lang": "en",
          "followers_count": 2013,
          "protected": false,
          "notifications": null,
          "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/16420220/twitter-background-final.png",
          "profile_background_color": "FFFFFF",
          "verified": false,
          "geo_enabled": true,
          "time_zone": "London",
          "description": "Co-Founder/Dev (PHP/jQuery) @justFDI. Run @thinkbikes and @thinkwall for events. Ex tech journo, helps run @uktjpr. Passion for Linux and customises everything.",
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/profile_background_images/16420220/twitter-background-final.png",
          "statuses_count": 11550,
          "friends_count": 770,
          "following": null,
          "show_all_inline_media": true,
          "screen_name": "spode"
        },
        "in_reply_to_screen_name": "jasoncosta",
        "source": "JournoTwit",
        "in_reply_to_status_id": null
      },
      {
        "coordinates": {
          "coordinates": [
            121.0132101,
            14.5191613
          ],
          "type": "Point"
        },
        "favorited": false,
        "truncated": false,
        "created_at": "Mon Sep 03 08:08:02 +0000 2012",
        "id_str": "242534402280783873",
        "entities": {
          "urls": [

          ],
          "hashtags": [
            {
              "text": "twitter",
              "indices": [
                49,
                57
              ]
            }
          ],
          "user_mentions": [
            {
              "name": "Jason Costa",
              "id_str": "14927800",
              "id": 14927800,
              "indices": [
                14,
                25
              ],
              "screen_name": "jasoncosta"
            }
          ]
        },
        "in_reply_to_user_id_str": null,
        "contributors": null,
        "text": "Got the shirt @jasoncosta thanks man! Loving the #twitter bird on the shirt :-)",
        "retweet_count": 0,
        "in_reply_to_status_id_str": null,
        "id": 242534402280783873,
        "geo": {
          "coordinates": [
            14.5191613,
            121.0132101
          ],
          "type": "Point"
        },
        "retweeted": false,
        "in_reply_to_user_id": null,
        "place": null,
        "user": {
          "profile_sidebar_fill_color": "EFEFEF",
          "profile_sidebar_border_color": "EEEEEE",
          "profile_background_tile": true,
          "name": "Mikey",
          "profile_image_url": "http://a0.twimg.com/profile_images/1305509670/chatMikeTwitter_normal.png",
          "created_at": "Fri Jun 20 15:57:08 +0000 2008",
          "location": "Singapore",
          "follow_request_sent": false,
          "profile_link_color": "009999",
          "is_translator": false,
          "id_str": "15181205",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "http://about.me/michaelangelo",
                  "indices": [
                    0,
                    29
                  ]
                }
              ]
            },
            "description": {
              "urls": [

              ]
            }
          },
          "default_profile": false,
          "contributors_enabled": false,
          "favourites_count": 11,
          "url": "http://about.me/michaelangelo",
          "profile_image_url_https": "https://si0.twimg.com/profile_images/1305509670/chatMikeTwitter_normal.png",
          "utc_offset": 28800,
          "id": 15181205,
          "profile_use_background_image": true,
          "listed_count": 61,
          "profile_text_color": "333333",
          "lang": "en",
          "followers_count": 577,
          "protected": false,
          "notifications": null,
          "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme14/bg.gif",
          "profile_background_color": "131516",
          "verified": false,
          "geo_enabled": true,
          "time_zone": "Hong Kong",
          "description": "Android Applications Developer,  Studying Martial Arts, Plays MTG, Food and movie junkie",
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/images/themes/theme14/bg.gif",
          "statuses_count": 11327,
          "friends_count": 138,
          "following": null,
          "show_all_inline_media": true,
          "screen_name": "mikedroid"
        },
        "in_reply_to_screen_name": null,
        "source": "Twitter for Android",
        "in_reply_to_status_id": null
      }
    ]
:::

</div>
