
POST statuses/update | Docs | Twitter Developer Platform 

POST statuses/update

post-statuses-update
POST statuses/update
====================

Updates the authenticating user's current status, also known as
Tweeting.

For each update attempt, the update text is compared with the
authenticating user's recent Tweets. Any attempt that would result in
duplication will be blocked, resulting in a 403 error. A user cannot
submit the same status twice in a row.

While not rate limited by the API, a user is limited in the number of
Tweets they can create at a time. If the number of updates posted by the
user reaches the current allowed limit this method will return an HTTP
403 error.

**About Geo**

* Any geo-tagging parameters in the update will be ignored if
`geo_enabled` for the user is false (this is the default
setting for all users, unless the user has enabled geolocation in their
settings)
* The number of digits after the decimal separator passed to
`lat` (up to 8) is tracked so that when the `lat`
is returned in a status object it will have the same number of digits
after the decimal separator.
* Use a decimal point as the separator (and not a decimal comma) for
the latitude and the longitude - usage of a decimal comma will cause the
geo-tagged portion of the status update to be dropped.
* For JSON, the response mostly uses conventions described in GeoJSON. However, the `geo`
object coordinates that Twitter renders are **reversed**
from the GeoJSON specification. GeoJSON specifies a longitude then a
latitude, whereas Twitter represents it as a latitude then a longitude:
`"geo": { "type":"Point", "coordinates":[37.78217, -122.40062] }`
* The `coordinates` object is replacing the
`geo` object (no deprecation date has been set for the
`geo` object yet) -- the difference is that the coordinates
object, in JSON, is now rendered correctly in GeoJSON.
* If a `place_id` is passed into the status update, then
that place will be attached to the status. If no `place_id`
was explicitly provided, but `latitude` and
`longitude` are, the API attempts to implicitly provide a
place by calling geo/reverse\_geocode.
* Users have the ability to remove all geotags from all their Tweets
en masse via the user settings page. Currently there is no method to
remove geotags from individual Tweets.

Resource URL¶
-------------

`https://api.twitter.com/1.1/statuses/update.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 3-hour window | 300\* per user; 300\* per app |

*Please note* - The 300 per 3 hours is a combined limit with
the POST
statuses/retweet/:id endpoint. You can only post 300 Tweets or
Retweets during a 3 hour period.

Parameters¶
-----------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of the status update. URL encode as necessary. t.co link wrapping will affect character
counts. |  |  |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to.
**Note:** This parameter will be ignored unless the author
of the Tweet this parameter references is mentioned within the status
text. Therefore, you must include `@username` , where
`username` is the author of the referenced Tweet, within the
update. |  |  |
| auto\_populate\_reply\_metadata | optional | If set to `true` and used with
`in_reply_to_status_id`, leading `@mentions` will
be looked up from the original Tweet, and added to the new Tweet from
there. This wil append `@mentions` into the metadata of an
extended Tweet as a reply chain grows, until the limit on
`@mentions` is reached. In cases where the original Tweet has
been deleted, the reply will fail. | `false` | `true` |
| exclude\_reply\_user\_ids | optional | When used with `auto_populate_reply_metadata`, a
comma-separated list of user ids which will be removed from the
server-generated `@mentions` prefix on an extended Tweet.
Note that the leading `@mention` cannot be removed as it
would break the `in-reply-to-status-id` semantics. Attempting
to remove it will be silently ignored. |  | `786491,54931584` |
| attachment\_url | optional | In order for a URL to not be counted in the status body of an
extended Tweet, provide a URL as a Tweet attachment. This URL must be a
Tweet permalink, or Direct Message deep link. Arbitrary, non-Twitter
URLs must remain in the status text. URLs passed to the
`attachment_url` parameter not matching either a Tweet
permalink or Direct Message deep link will fail at Tweet creation and
cause an exception. |  | `https://twitter.com/andypiper/status/903615884664725505` |
| media\_ids | optional | A comma-delimited list of `media_ids` to associate with
the Tweet. You may include up to 4 photos or 1 animated GIF or 1 video
in a Tweet. See Uploading
Media for further details on uploading media. |  | `471592142565957632` |
| possibly\_sensitive | optional | If you upload Tweet media that might be considered sensitive content
such as nudity, or medical procedures, you must set this value to
`true`. If this parameter is included in your request, it
will override the user’s preferences. Including any value other than
`true`, `1`, or `t` will be interpreted
as `false`. See Media setting and
best practices for more context. | If left unspecified, the value applied to the newly
created Tweet is derived from the user's preferences.
 | `true` |
| lat | optional | The latitude of the location this Tweet refers to. This parameter
will be ignored unless it is inside the range -90.0 to +90.0 (North is
positive) inclusive. It will also be ignored if there is no
corresponding `long` parameter. |  | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges
for longitude are -180.0 to +180.0 (East is positive) inclusive. This
parameter will be ignored if outside that range, if it is not a number,
if `geo_enabled` is turned off, or if there no corresponding
`lat` parameter. |  | `-122.400612831116` |
| place\_id | optional | A place in the
world. |  | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has
been sent from. |  | `true` |
| trim\_user | optional | When set to either `true` , `t` or
`1` , the response will include a user object including only
the author's ID. Omit this parameter to receive the complete user
object. | `false` | `true` |
| card\_uri | optional | Associate an ads card with the Tweet using the `card_uri`
value from any ads card response. |  | `card://853503245793641682` |

Example Request¶
----------------

To obtain the generated oauth\_nonce, oauth\_token, and oauth\_signature
you can use a REST tool such as Insomnia or Postman.

```
curl -XPOST 
  --url 'https://api.twitter.com/1.1/statuses/update.json?status=hello' 
  --header 'authorization: OAuth
  oauth_consumer_key="oauth_customer_key",
  oauth_nonce="generated_oauth_nonce",
  oauth_signature="generated_oauth_signature",
  oauth_signature_method="HMAC-SHA1",
  oauth_timestamp="generated_timestamp",
  oauth_token="oauth_token",
  oauth_version="1.0"'
```
You many want to change the status from 'hello' to something
different.

You can use also use any other OAuth helper library you'd like such
as twurl.

```
$ twurl -d 'status=Test tweet using the POST statuses/update endpoint' /1.1/statuses/update.json
```
Example Response¶
-----------------

After you post successfully you should get back something that looks
like this:

```
{
  "created_at": "Wed Oct 10 20:19:24 +0000 2018",
  "id": 1050118621198921700,
  "id_str": "1050118621198921728",
  "text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin t… https://t.co/MkGjXf9aXm",
  "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
  "truncated": true,
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
    "url": "https://developer.twitter.com",
    "description": "The Real Twitter API. Tweets about API changes, service issues and our Developer Platform. Don't get an answer? It's on my website.",
    "translator_type": "null",
    "derived": {
      "locations": [
        {
          "country": "United States",
          "country_code": "US",
          "locality": "San Francisco",
          "region": "California",
          "sub_region": "San Francisco County",
          "full_name": "San Francisco, California, United States",
          "geo": {
            "coordinates": [
              -122.41942,
              37.77493
            ],
            "type": "point"
          }
        }
      ]
    },
    "protected": false,
    "verified": true,
    "followers_count": 6172196,
    "friends_count": 12,
    "listed_count": 13003,
    "favourites_count": 31,
    "statuses_count": 3650,
    "created_at": "Wed May 23 06:01:13 +0000 2007",
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": false,
    "lang": "en",
    "contributors_enabled": false,
    "is_translator": null,
    "profile_background_color": "null",
    "profile_background_image_url": "null",
    "profile_background_image_url_https": "null",
    "profile_background_tile": null,
    "profile_link_color": "null",
    "profile_sidebar_border_color": "null",
    "profile_sidebar_fill_color": "null",
    "profile_text_color": "null",
    "profile_use_background_image": null,
    "profile_image_url": "null",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/6253282/1497491515",
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "extended_tweet": {
    "full_text": "To make room for more expression, we will now count all emojis as equal—including those with gender‍‍‍ ‍‍and skin tone modifiers 👍🏻👍🏽👍🏿. This is now reflected in Twitter-Text, our Open Source library. nnUsing Twitter-Text? See the forum post for detail: https://t.co/Nx1XZmRCXA",
    "display_text_range": [
      0,
      277
    ],
    "entities": {
      "hashtags": [],
      "urls": [
        {
          "url": "https://t.co/Nx1XZmRCXA",
          "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
          "display_url": "twittercommunity.com/t/new-update-t…",
          "unwound": {
            "url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
            "status": 200,
            "title": "New update to the Twitter-Text library: Emoji character count",
            "description": "Over the years, we have made several updates to the way that people can communicate on Twitter. One of the more notable changes made last year was to increase the number of characters per Tweet from 140 to 280 characters. Today, we continue to expand people’s ability to express themselves by announcing a change to the way that we count emojis. Due to the differences in the way written text and emojis are encoded, many emojis (including emojis where you can apply gender and skin tone) have count..."
          },
          "indices": [
            254,
            277
          ]
        }
      ],
      "user_mentions": [],
      "symbols": []
    }
  },
  "quote_count": 0,
  "reply_count": 0,
  "retweet_count": 0,
  "favorite_count": 0,
  "entities": {
    "hashtags": [],
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
    ],
    "user_mentions": [],
    "symbols": []
  },
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "filter_level": "low",
  "lang": "en"
}
```

Developer policy and terms

Follow @XDevelopers

Subscribe to developer news

#### 
 X platform

* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app

#### 
 X Corp.

* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors

#### 
 Help

* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us

#### 
 Developer resources

* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms

#### 
 Business resources

* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy

 © 2024 X Corp.

Cookies

Privacy

Terms and conditions

**Did someone say … cookies?**  

 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.

* Accept all cookies
* Refuse non-essential cookies