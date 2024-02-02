



GET statuses/lookup | Docs | Twitter Developer Platform 





































































































GET statuses/lookup



get-statuses-lookup

GET statuses/lookup
===================




Returns fully-hydrated Tweet
objects for up to 100 Tweets per request, as specified by
comma-separated values passed to the `id` parameter.


This method is especially useful to get the details (hydrate) a
collection of Tweet IDs.


GET
statuses / show / :id is used to retrieve a single Tweet object.


There are a few things to note when using this method.


* You must be following a protected user to be able to see their most
recent Tweets. If you don't follow a protected user their status will be
removed.
* The order of Tweet IDs may not match the order of Tweets in the
returned array.
* If a requested Tweet is unknown or deleted, then that Tweet will not
be returned in the results list, unless the `map` parameter
is set to `true`, in which case it will be returned with a
value of `null`.
* If none of your lookup criteria matches valid Tweet IDs an empty
array will be returned for `map=false`.
* You are strongly encouraged to use a POST for larger requests.


Resource URL¶
-------------


`https://api.twitter.com/1.1/statuses/lookup.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 300 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | A comma separated list of Tweet IDs, up to 100 are allowed in a
single request. |  | *20* *1050118621198921728* |
| include\_entities | optional | The *entities* node that may appear within embedded statuses
will not be included when set to *false*. |  | *false* |
| trim\_user | optional | When set to either *true* , *t* or *1* , each
Tweet returned in a timeline will include a user object including only
the status authors numerical ID. Omit this parameter to receive the
complete user object. |  | *true* |
| map | optional | When using the *map* parameter, Tweets that do not exist or
cannot be viewed by the current user will still have their key
represented but with an explicitly *null* value paired with
it |  | *true* |
| include\_ext\_alt\_text | optional | If alt text has been added to any attached media entities, this
parameter will return an *ext\_alt\_text* value in the top-level
key for the media entity. If no value has been set, this will be
returned as `null` |  | *true* |
| include\_card\_uri | optional | When set to either *true* , *t* or *1* , each
Tweet returned will include a *card\_uri* attribute when there is
an ads card attached to the Tweet and when that card was attached using
the *card\_uri* value. |  | *true* |
| include\_ext\_edit\_control | optional | Must be set to true in order to return edited Tweet metadata as
part of the Tweet object.
`include_ext_edit_control=true` Note that historical
Tweets may not contain edited Tweet metadata. |  | *true* |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/statuses/lookup.json?id=20,1050118621198921728`


Example Response¶
-----------------



```
[
  {
    "created_at": "Tue Mar 21 20:50:14 +0000 2006",
    "id": 20,
    "id_str": "20",
    "text": "just setting up my twttr",
    "truncated": false,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": []
    },
    "source": "<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 12,
      "id_str": "12",
      "name": "jack",
      "screen_name": "jack",
      "location": "",
      "description": "",
      "url": null,
      "entities": {
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 4183755,
      "friends_count": 3894,
      "listed_count": 28137,
      "created_at": "Tue Mar 21 20:50:14 +0000 2006",
      "favourites_count": 23361,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": null,
      "verified": true,
      "statuses_count": 25783,
      "lang": "null",
      "contributors_enabled": null,
      "is_translator": null,
      "is_translation_enabled": null,
      "profile_background_color": "null",
      "profile_background_image_url": "null",
      "profile_background_image_url_https": "null",
      "profile_background_tile": null,
      "profile_image_url": "null",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
      "profile_banner_url": "null",
      "profile_link_color": "null",
      "profile_sidebar_border_color": "null",
      "profile_sidebar_fill_color": "null",
      "profile_text_color": "null",
      "profile_use_background_image": null,
      "has_extended_profile": null,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "null"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 111160,
    "favorite_count": 98090,
    "favorited": false,
    "retweeted": false,
    "lang": "en"
  },
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
  ]
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















