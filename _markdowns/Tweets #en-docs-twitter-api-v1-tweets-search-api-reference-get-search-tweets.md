<div>

::: c01-rich-text-editor
Returns a collection of relevant
[Tweets](/en/docs/tweets/data-dictionary/overview/tweet-object) matching
a specified query.

Please note that Twitter\'s search service and, by extension, the Search
API is not meant to be an exhaustive source of Tweets. Not all Tweets
will be indexed or made available via the search interface.

To learn how to use [Twitter Search](https://twitter.com/search)
effectively, please see the [Standard search
operators](/en/docs/tweets/search/guides/standard-operators) page for a
list of available filter operators. Also, see the [Working with
Timelines](/en/docs/tweets/timelines/guides/working-with-timelines) page
to learn best practices for navigating results by ` since_id ` and
` max_id ` .

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/search/tweets.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   180
  Requests / 15-min window (app auth)    450
  Supports Edit Tweets feature?          Yes
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

+-------------+-------------+-------------+-------------+-------------+
| q           | required    | A UTF-8,    |             | `           |
|             |             | URL-encoded |             |  @noradio ` |
|             |             | search      |             |             |
|             |             | query of    |             |             |
|             |             | 500         |             |             |
|             |             | characters  |             |             |
|             |             | maximum,    |             |             |
|             |             | including   |             |             |
|             |             | operators.  |             |             |
|             |             | Queries may |             |             |
|             |             | a           |             |             |
|             |             | dditionally |             |             |
|             |             | be limited  |             |             |
|             |             | by          |             |             |
|             |             | complexity. |             |             |
+-------------+-------------+-------------+-------------+-------------+
| in          | optional    | Must be set |             | ` true `    |
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
| geocode     | optional    | Returns     |             | ` 37.78     |
|             |             | tweets by   |             | 1157 -122.3 |
|             |             | users       |             | 98720 1mi ` |
|             |             | located     |             |             |
|             |             | within a    |             |             |
|             |             | given       |             |             |
|             |             | radius of   |             |             |
|             |             | the given   |             |             |
|             |             | latitude    |             |             |
|             |             | /longitude. |             |             |
|             |             | The         |             |             |
|             |             | location is |             |             |
|             |             | pre         |             |             |
|             |             | ferentially |             |             |
|             |             | taking from |             |             |
|             |             | the         |             |             |
|             |             | Geotagging  |             |             |
|             |             | API, but    |             |             |
|             |             | will fall   |             |             |
|             |             | back to     |             |             |
|             |             | their       |             |             |
|             |             | Twitter     |             |             |
|             |             | profile.    |             |             |
|             |             | The         |             |             |
|             |             | parameter   |             |             |
|             |             | value is    |             |             |
|             |             | specified   |             |             |
|             |             | by \"       |             |             |
|             |             | ` latit     |             |             |
|             |             | ude,longitu |             |             |
|             |             | de,radius ` |             |             |
|             |             | \", where   |             |             |
|             |             | radius      |             |             |
|             |             | units must  |             |             |
|             |             | be          |             |             |
|             |             | specified   |             |             |
|             |             | as either   |             |             |
|             |             | \" ` mi `   |             |             |
|             |             | \" (miles)  |             |             |
|             |             | or \"       |             |             |
|             |             | ` km ` \"   |             |             |
|             |             | (k          |             |             |
|             |             | ilometers). |             |             |
|             |             | Note that   |             |             |
|             |             | you cannot  |             |             |
|             |             | use the     |             |             |
|             |             | near        |             |             |
|             |             | operator    |             |             |
|             |             | via the API |             |             |
|             |             | to geocode  |             |             |
|             |             | arbitrary   |             |             |
|             |             | locations;  |             |             |
|             |             | however you |             |             |
|             |             | can use     |             |             |
|             |             | this        |             |             |
|             |             | ` geocode ` |             |             |
|             |             | parameter   |             |             |
|             |             | to search   |             |             |
|             |             | near        |             |             |
|             |             | geocodes    |             |             |
|             |             | directly. A |             |             |
|             |             | maximum of  |             |             |
|             |             | 1,000       |             |             |
|             |             | distinct    |             |             |
|             |             | \"su        |             |             |
|             |             | b-regions\" |             |             |
|             |             | will be     |             |             |
|             |             | considered  |             |             |
|             |             | when using  |             |             |
|             |             | the radius  |             |             |
|             |             | modifier.   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| lang        | optional    | Restricts   |             | ` eu `      |
|             |             | tweets to   |             |             |
|             |             | the given   |             |             |
|             |             | language,   |             |             |
|             |             | given by an |             |             |
|             |             | [ISO        |             |             |
|             |             | 639-1       |             |             |
|             |             | ](http://en |             |             |
|             |             | .wikipedia. |             |             |
|             |             | org/wiki/Li |             |             |
|             |             | st_of_ISO_6 |             |             |
|             |             | 39-1_codes) |             |             |
|             |             | code.       |             |             |
|             |             | Language    |             |             |
|             |             | detection   |             |             |
|             |             | is          |             |             |
|             |             | b           |             |             |
|             |             | est-effort. |             |             |
+-------------+-------------+-------------+-------------+-------------+
| locale      | optional    | Specify the |             | ` ja `      |
|             |             | language of |             |             |
|             |             | the query   |             |             |
|             |             | you are     |             |             |
|             |             | sending     |             |             |
|             |             | (only       |             |             |
|             |             | ` ja ` is   |             |             |
|             |             | currently   |             |             |
|             |             | effective). |             |             |
|             |             | This is     |             |             |
|             |             | intended    |             |             |
|             |             | for         |             |             |
|             |             | langua      |             |             |
|             |             | ge-specific |             |             |
|             |             | consumers   |             |             |
|             |             | and the     |             |             |
|             |             | default     |             |             |
|             |             | should work |             |             |
|             |             | in the      |             |             |
|             |             | majority of |             |             |
|             |             | cases.      |             |             |
+-------------+-------------+-------------+-------------+-------------+
| result_type | optional    | Optional.   |             | ` mixed `   |
|             |             | Specifies   |             | ` recent `  |
|             |             | what type   |             | ` popular ` |
|             |             | of search   |             |             |
|             |             | results you |             |             |
|             |             | would       |             |             |
|             |             | prefer to   |             |             |
|             |             | receive.    |             |             |
|             |             | The current |             |             |
|             |             | default is  |             |             |
|             |             | \"mixed.\"  |             |             |
|             |             | Valid       |             |             |
|             |             | values      |             |             |
|             |             | include:    |             |             |
|             |             |             |             |             |
|             |             | \*          |             |             |
|             |             | ` mixed ` : |             |             |
|             |             | Include     |             |             |
|             |             | both        |             |             |
|             |             | popular and |             |             |
|             |             | real time   |             |             |
|             |             | results in  |             |             |
|             |             | the         |             |             |
|             |             | response.   |             |             |
|             |             |             |             |             |
|             |             | \*          |             |             |
|             |             | ` recent `  |             |             |
|             |             | : return    |             |             |
|             |             | only the    |             |             |
|             |             | most recent |             |             |
|             |             | results in  |             |             |
|             |             | the         |             |             |
|             |             | response    |             |             |
|             |             |             |             |             |
|             |             | \*          |             |             |
|             |             | ` popular ` |             |             |
|             |             | : return    |             |             |
|             |             | only the    |             |             |
|             |             | most        |             |             |
|             |             | popular     |             |             |
|             |             | results in  |             |             |
|             |             | the         |             |             |
|             |             | response.   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| count       | optional    | The number  |             | ` 100 `     |
|             |             | of tweets   |             |             |
|             |             | to return   |             |             |
|             |             | per page,   |             |             |
|             |             | up to a     |             |             |
|             |             | maximum of  |             |             |
|             |             | 100.        |             |             |
|             |             | Defaults to |             |             |
|             |             | 15. This    |             |             |
|             |             | was         |             |             |
|             |             | formerly    |             |             |
|             |             | the \"rpp\" |             |             |
|             |             | parameter   |             |             |
|             |             | in the old  |             |             |
|             |             | Search API. |             |             |
+-------------+-------------+-------------+-------------+-------------+
| until       | optional    | Returns     |             | ` 2         |
|             |             | tweets      |             | 015-07-19 ` |
|             |             | created     |             |             |
|             |             | before the  |             |             |
|             |             | given date. |             |             |
|             |             | Date should |             |             |
|             |             | be          |             |             |
|             |             | formatted   |             |             |
|             |             | as          |             |             |
|             |             | YYYY-MM-DD. |             |             |
|             |             | Keep in     |             |             |
|             |             | mind that   |             |             |
|             |             | the search  |             |             |
|             |             | index has a |             |             |
|             |             | 7-day       |             |             |
|             |             | limit. In   |             |             |
|             |             | other       |             |             |
|             |             | words, no   |             |             |
|             |             | tweets will |             |             |
|             |             | be found    |             |             |
|             |             | for a date  |             |             |
|             |             | older than  |             |             |
|             |             | one week.   |             |             |
+-------------+-------------+-------------+-------------+-------------+
| since_id    | optional    | Returns     |             | ` 12345 `   |
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
| max_id      | optional    | Returns     |             | ` 54321 `   |
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
| inclu       | optional    | The         |             | ` false `   |
| de_entities |             | `           |             |             |
|             |             |  entities ` |             |             |
|             |             | node will   |             |             |
|             |             | not be      |             |             |
|             |             | included    |             |             |
|             |             | when set to |             |             |
|             |             | ` false ` . |             |             |
+-------------+-------------+-------------+-------------+-------------+

## Example Requests [¶](#example-requests){.headerlink}

    $ curl --request GET 
     --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' 
     --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
     oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
     oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
     oauth_token="access-token-for-authed-user", oauth_version="1.0"'

    $ twurl /1.1/search/tweets.json?q=nasa&result_type=popular

## Example Response [¶](#example-response){.headerlink}

    {
        "statuses": [
            {
                "created_at": "Sun Feb 25 18:11:01 +0000 2018",
                "id": 967824267948773377,
                "id_str": "967824267948773377",
                "text": "From pilot to astronaut, Robert H. Lawrence was the first African-American to be selected as an astronaut by any na… https://t.co/FjPEWnh804",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/FjPEWnh804",
                            "expanded_url": "https://twitter.com/i/web/status/967824267948773377",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
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
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 988,
                "favorite_count": 3875,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Sun Feb 25 19:31:07 +0000 2018",
                "id": 967844427480911872,
                "id_str": "967844427480911872",
                "text": "A magnetic power struggle of galactic proportions - new research highlights the role of the Sun's magnetic landscap… https://t.co/29dZgga54m",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/29dZgga54m",
                            "expanded_url": "https://twitter.com/i/web/status/967844427480911872",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
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
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 2654,
                "favorite_count": 7962,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Mon Feb 26 19:21:43 +0000 2018",
                "id": 968204446625869827,
                "id_str": "968204446625869827",
                "text": "Someone's got to be first. In space, the first explorers beyond Mars were Pioneers 10 and 11, twin robots who chart… https://t.co/SUX30Y45mr",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/SUX30Y45mr",
                            "expanded_url": "https://twitter.com/i/web/status/968204446625869827",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://www.sprinklr.com"' rel='"nofollow"'>Sprinklr</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 11348282,
                    "id_str": "11348282",
                    "name": "NASA",
                    "screen_name": "NASA",
                    "location": "",
                    "description": "Explore the universe and discover our home planet with @NASA. We usually post in EST (UTC-5)",
                    "url": "https://t.co/TcEE6NS8nD",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/TcEE6NS8nD",
                                    "expanded_url": "http://www.nasa.gov",
                                    "display_url": "nasa.gov",
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
                    "followers_count": 28605561,
                    "friends_count": 270,
                    "listed_count": 90405,
                    "created_at": "Wed Dec 19 20:20:32 +0000 2007",
                    "favourites_count": 2960,
                    "utc_offset": -18000,
                    "time_zone": "Eastern Time (US & Canada)",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 50713,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/590922434682880000/3byPYvqe.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/188302352/nasalogo_twitter_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/11348282/1518798395",
                    "profile_link_color": "205BA7",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "F3F2F2",
                    "profile_text_color": "000000",
                    "profile_use_background_image": true,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "regular"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 729,
                "favorite_count": 2777,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            },
            {
                "created_at": "Mon Feb 26 06:42:50 +0000 2018",
                "id": 968013469743288321,
                "id_str": "968013469743288321",
                "text": "宇宙ステーションでも、日本と9時間の時差で月曜日が始まりました。n今週は6人から3人にクルーのサイズダウンがありますが、しっかりと任されているタスクをこなしたいと思います。nn写真は、NASAの実験施設「ディスティニー」のグローブ… https://t.co/2CYoPV6Aqx",
                "truncated": true,
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/2CYoPV6Aqx",
                            "expanded_url": "https://twitter.com/i/web/status/968013469743288321",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                117,
                                140
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "ja"
                },
                "source": "<a href='"http://twitter.com"' rel='"nofollow"'>Twitter Web Client</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 842625693733203968,
                    "id_str": "842625693733203968",
                    "name": "金井 宣茂",
                    "screen_name": "Astro_Kanai",
                    "location": "",
                    "description": "宇宙飛行士。2017年12月19日から国際宇宙ステーションに長期滞在中。 応援いただいているフォロワーのみなさまと一緒に、宇宙滞在を楽しみたいと思います！",
                    "url": "https://t.co/rWU6cxY9iL",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "https://t.co/rWU6cxY9iL",
                                    "expanded_url": "https://ameblo.jp/astro-kanai/",
                                    "display_url": "ameblo.jp/astro-kanai/",
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
                    "followers_count": 51512,
                    "friends_count": 59,
                    "listed_count": 655,
                    "created_at": "Fri Mar 17 06:36:35 +0000 2017",
                    "favourites_count": 7075,
                    "utc_offset": 32400,
                    "time_zone": "Tokyo",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 1035,
                    "lang": "ja",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "000000",
                    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/879071738625232901/u0nlrr4Y_normal.jpg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/842625693733203968/1492509582",
                    "profile_link_color": "E81C4F",
                    "profile_sidebar_border_color": "000000",
                    "profile_sidebar_fill_color": "000000",
                    "profile_text_color": "000000",
                    "profile_use_background_image": false,
                    "has_extended_profile": true,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "none"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 226,
                "favorite_count": 1356,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "ja"
            },
            {
                "created_at": "Mon Feb 26 01:07:05 +0000 2018",
                "id": 967928974960545793,
                "id_str": "967928974960545793",
                "text": "Congratulations to #Olympics athletes who won gold! Neutron stars like the one at the heart of the Crab Nebula may… https://t.co/vz4SnPupe2",
                "truncated": true,
                "entities": {
                    "hashtags": [
                        {
                            "text": "Olympics",
                            "indices": [
                                19,
                                28
                            ]
                        }
                    ],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": [
                        {
                            "url": "https://t.co/vz4SnPupe2",
                            "expanded_url": "https://twitter.com/i/web/status/967928974960545793",
                            "display_url": "twitter.com/i/web/status/9…",
                            "indices": [
                                116,
                                139
                            ]
                        }
                    ]
                },
                "metadata": {
                    "result_type": "popular",
                    "iso_language_code": "en"
                },
                "source": "<a href='"https://studio.twitter.com"' rel='"nofollow"'>Media Studio</a>",
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "in_reply_to_screen_name": null,
                "user": {
                    "id": 19802879,
                    "id_str": "19802879",
                    "name": "NASA JPL",
                    "screen_name": "NASAJPL",
                    "location": "Pasadena, Calif.",
                    "description": "NASA Jet Propulsion Laboratory manages many of NASA's robotic missions exploring Earth, the solar system and our universe. Tweets from JPL's News Office.",
                    "url": "http://t.co/gcM9d1YLUB",
                    "entities": {
                        "url": {
                            "urls": [
                                {
                                    "url": "http://t.co/gcM9d1YLUB",
                                    "expanded_url": "http://www.jpl.nasa.gov",
                                    "display_url": "jpl.nasa.gov",
                                    "indices": [
                                        0,
                                        22
                                    ]
                                }
                            ]
                        },
                        "description": {
                            "urls": []
                        }
                    },
                    "protected": false,
                    "followers_count": 2566921,
                    "friends_count": 379,
                    "listed_count": 15065,
                    "created_at": "Sat Jan 31 03:19:43 +0000 2009",
                    "favourites_count": 1281,
                    "utc_offset": -32400,
                    "time_zone": "Alaska",
                    "geo_enabled": false,
                    "verified": true,
                    "statuses_count": 6328,
                    "lang": "en",
                    "contributors_enabled": false,
                    "is_translator": false,
                    "is_translation_enabled": false,
                    "profile_background_color": "0B090B",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/8479565/twitter_jpl_bkg.009.jpg",
                    "profile_background_tile": false,
                    "profile_image_url": "http://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/2305452633/lg0hov3l8g4msxbdwv48_normal.jpeg",
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/19802879/1398298134",
                    "profile_link_color": "0D1787",
                    "profile_sidebar_border_color": "100F0E",
                    "profile_sidebar_fill_color": "74A6CD",
                    "profile_text_color": "0C0C0D",
                    "profile_use_background_image": true,
                    "has_extended_profile": false,
                    "default_profile": false,
                    "default_profile_image": false,
                    "following": null,
                    "follow_request_sent": null,
                    "notifications": null,
                    "translator_type": "none"
                },
                "geo": null,
                "coordinates": null,
                "place": null,
                "contributors": null,
                "is_quote_status": false,
                "retweet_count": 325,
                "favorite_count": 1280,
                "favorited": false,
                "retweeted": false,
                "possibly_sensitive": false,
                "lang": "en"
            }
        ],
        "search_metadata": {
            "completed_in": 0.057,
            "max_id": 0,
            "max_id_str": "0",
            "next_results": "?max_id=967574182522482687&q=nasa&include_entities=1&result_type=popular",
            "query": "nasa",
            "count": 3,
            "since_id": 0,
            "since_id_str": "0"
        }
    }

Please note that \"count\" was previously \"results_per_page\".
:::

</div>
