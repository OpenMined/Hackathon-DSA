



POST
statuses/update\_with\_media (deprecated) | Docs | Twitter Developer Platform 





































































































POST
statuses/update\_with\_media (deprecated)



post-statuses-update\_with\_media

POST
statuses/update\_with\_media (deprecated)
==============================================




**This endpoint has been DEPRECATED should no longer be used.
This endpoint does not support multiple images, animated GIFs, or
video.** Replacement method: follow the Uploading media guide to
upload one or more media entities, and then use POST
statuses/update to attach them to a Tweet.


Updates the authenticated user's current status and attaches media
for upload. This creates a Tweet with a (single) picture attached.


Unlike POST
statuses/update, this method expects raw multipart data. The POST
request's `content-type` should be set to
`multipart/form-data` with the `media[]`
parameter.


The Tweet text will be rewritten to include the media URL(s), which
will reduce the number of characters allowed in the Tweet text. If the
URL(s) cannot be appended without text truncation, the Tweet will be
rejected and this method will return an HTTP 403 error.


Users are limited to a specific daily media upload limit. Requests to
this endpoint will return the following headers with information
regarding the user's current media upload limits:


* `x-mediaratelimit-limit` - Indicates the total pieces of
media the current user may upload before the time indicated in
`x-mediaratelimit-reset`.
* `x-mediaratelimit-remaining` - The remaining pieces of
media the current user may upload before the time indicated in
`x-mediaratelimit-reset`.
* `x-mediaratelimit-reset` - A UTC-based timestamp (in
seconds) indicating when `x-mediaratelimit-remaining` will
reset to the value in `x-mediaratelimit-limit` and the user
can resume uploading media.


If the user is over the daily media limit, this method will return an
HTTP 403 error. In addition to media upload limits, the user is also
limited in the number of statuses they can publish daily. If the user
tries to exceed the number of updates allowed, this method will also
return an HTTP 403 error, similar to POST
statuses/update.


There is a 30 second timeout for this endpoint, so network latency
may prevent media being posted successfully.


OAuth is handled differently for POST messages. See Uploading Media for more
details on this.


Resource URL¶
-------------


`https://api.twitter.com/1.1/statuses/update_with_media.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |


Parameters¶
-----------




| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| status | required | The text of your status update. URL encode as necessary. t.co link wrapping may affect character
counts if the post contains URLs. You must additionally account for the
`characters_reserved_per_media` per uploaded media,
additionally accounting for space characters in between finalized URLs.
**Note** : Request the
`GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` characters\_reserved\_per\_media`and`max\_media\_per\_upload`
values. |  | onfiguration>`\_\_ endpoint to get the |
| media[] | required | Up to `max_media_per_upload` files may be specified in
the request, each named `media[]` . Supported image formats
are PNG, JPG and GIF, including animated GIFs of up to 3MB . This data
must be either the raw image bytes or encoded as base64.
**Note** : Request the
`GET help / configuration &lt;/en/docs/developer-utilities/configuration/api-reference/get-help-c current` max\_media\_per\_upload`and`photo\_size\_limit`
values. | onfiguration>`\_\_ endpoint to get the |  |
| possibly\_sensitive | optional | Set to `true` for content which may not be suitable for
every audience. |  |  |
| in\_reply\_to\_status\_id | optional | The ID of an existing status that the update is in reply to.
**Note** : This parameter will be ignored unless the author
of the Tweet this parameter references is mentioned within the status
text. Therefore, you must include `@username` , where
`username` is the author of the referenced Tweet, within the
update. |  |  |
| lat | optional | The latitude of the location this Tweet refers to. This parameter
will be ignored unless it is inside the range -90.0 to +90.0 (North is
positive) inclusive. It will also be ignored if there isn't a
corresponding `long` parameter. |  | `37.7821120598956` |
| long | optional | The longitude of the location this Tweet refers to. The valid ranges
for longitude is -180.0 to +180.0 (East is positive) inclusive. This
parameter will be ignored if outside that range, not a number,
`geo_enabled` is turned off, or if there not a corresponding
`lat` parameter. |  | `-122.400612831116` |
| place\_id | optional | A place in the world identified by a Twitter place ID. Place IDs can
be retrieved from geo/reverse\_geocode. |  | `df51dec6f4ee2b2c` |
| display\_coordinates | optional | Whether or not to put a pin on the exact coordinates a Tweet has
been sent from. |  | `true` |
| enable\_dmcommands | optional | When set to `true`, enables shortcode commands for
sending Direct Messages as part of the status text to send a Direct
Message to a user. When set to `false`, it turns off this
behavior and includes any leading characters in the status text. | `true` | `true` |
| fail\_dmcommands | optional | When set to `true`, causes any status text that starts
with shortcode commands to return an API error. When set to
`false`, allows shortcode commands to be sent in the status
text and acted on by the API. | `false` | `false` |


### Example Request¶


**Note:** The example request here demonstrates the
multipart request format.



```
POST /1.1/statuses/update_with_media.json HTTP/1.1
Host: api.twitter.com
User-Agent: Go http package
Content-Length: 15532
Authorization: OAuth oauth_consumer_key="...", oauth_nonce="...", oauth_signature="...", oauth_signature_method="HMAC-SHA1", oauth_timestamp="1347058301", oauth_token="...", oauth_version="1.0"
Content-Type: multipart/form-data;boundary=cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Accept-Encoding: gzip

--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340
Content-Disposition: form-data; name="status" Hello 2012-09-07 15:51:41.375247 -0700 PDT!
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340

Content-Type: application/octet-stream
Content-Disposition: form-data; name="media[]"; filename="media.png" ...
--cce6735153bf14e47e999e68bb183e70a1fa7fc89722fc1efdf03a917340-- 
```


```
{
  "contributors": null,
  "coordinates": null,
  "created_at": "Fri Sep 07 22:46:18 +0000 2012",
  "entities": {
    "hashtags": [],
    "media": [
      {
        "display_url": "pic.twitter.com/lX5LVZO",
        "expanded_url": "https://twitter.com/fakekurrik/status/244204973972410368/photo/1",
        "id": 244204973989187584,
        "id_str": "244204973989187584",
        "indices": [
          44,
          63
        ],
        "media_url": "http://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "media_url_https": "https://pbs.twimg.com/media/A2OXIUcCUAAXj9k.png",
        "sizes": {
          "large": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "medium": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "small": {
            "h": 175,
            "resize": "fit",
            "w": 333
          },
          "thumb": {
            "h": 150,
            "resize": "crop",
            "w": 150
          }
        },
        "type": "photo",
        "url": "http://t.co/lX5LVZO"
      }
    ],
    "urls": [],
    "user_mentions": []
  },
  "favorited": false,
  "geo": null,
  "id": 244204973972410368,
  "id_str": "244204973972410368",
  "in_reply_to_screen_name": null,
  "in_reply_to_status_id": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id": null,
  "in_reply_to_user_id_str": null,
  "place": null,
  "possibly_sensitive": false,
  "retweet_count": 0,
  "retweeted": false,
  "source": "Fakekurrik's Test Application",
  "text": "Hello 2012-09-07 15:48:27.889593 -0700 PDT! http://t.co/lX5LVZO",
  "truncated": false,
  "user": {
    "contributors_enabled": false,
    "created_at": "Fri Sep 09 16:13:20 +0000 2011",
    "default_profile": false,
    "default_profile_image": false,
    "description": "I am just a testing account, following me probably won't gain you very much",
    "entities": {
      "description": {
        "urls": []
      },
      "url": {
        "urls": [
          {
            "display_url": null,
            "expanded_url": null,
            "indices": [
              0,
              24
            ],
            "url": "http://blog.roomanna.com"
          }
        ]
      }
    },
    "favourites_count": 1,
    "follow_request_sent": false,
    "followers_count": 2,
    "following": false,
    "friends_count": 5,
    "geo_enabled": true,
    "id": 370773112,
    "id_str": "370773112",
    "is_translator": false,
    "lang": "en",
    "listed_count": 0,
    "location": "Trapped in factory",
    "name": "fakekurrik",
    "notifications": false,
    "profile_background_color": "C0DEED",
    "profile_background_image_url": "http://a0.twimg.com/profile_background_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile_background_image_url_https": "https://si0.twimg.com/profile_background_images/616512781/iarz5lvj7lg7zpg3zv8j.jpeg",
    "profile_background_tile": true,
    "profile_image_url": "http://a0.twimg.com/profile_images/2440719659/x47xdzkguqxr1w1gg5un_normal.png",
    "profile_image_url_https": "https://si0.twimg.com/profile_images/2440719659/x47xdzkguqxr1w1gg5un_normal.png",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "C0DEED",
    "profile_sidebar_fill_color": "FFFFFF",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "protected": true,
    "screen_name": "fakekurrik",
    "show_all_inline_media": false,
    "statuses_count": 546,
    "time_zone": "Pacific Time (US & Canada)",
    "url": "http://blog.roomanna.com",
    "utc_offset": -28800,
    "verified": false
  }
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















