::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
:::
:::

::: c01-rich-text-editor
::: is-table-default
When using enterprise data products, you will notice that much of the
data dictionary is similar to the native format of Tweet data, with some
additional enriched metadata.  The base level of the native enriched
format uses much of the same object names as the [Twitter API v1.1 data
format](/en/docs/twitter-api/v1/data-dictionary/overview/intro-to-tweet-json.html)
.  The Tweet object has a long list of 'root-level' attributes,
including fundamental attributes such as ` id ` , ` created_at ` , and
` text ` . Tweet objects will also have nested objects to include the
` user ` , ` entities ` , and ` extended_entities ` . Tweet objects will
also have other [nested Tweet objects](nested-tweet-objects) such as [
retweeted_status ]{.code-inline} , [ quoted_status ]{.code-inline} and [
extended_tweet ]{.code-inline} .  The native enriched format will
additionally have a [ matching_rules ]{.code-inline} object.

### []{#tweet-dictionary} Tweet Data Dictionary

Below you will find the data dictionary for these 'root-level'
attributes, as well as links to child object data dictionaries.

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| created_at            | String                | UTC time when this    |
|                       |                       | Tweet was created.    |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "cre              |
|                       |                       | ated_at": "Wed Oct 10 |
|                       |                       |  20:19:24 +0000 2018" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| id                    | Int64                 | The integer           |
|                       |                       | representation of the |
|                       |                       | unique identifier for |
|                       |                       | this Tweet. This      |
|                       |                       | number is greater     |
|                       |                       | than 53 bits and some |
|                       |                       | programming languages |
|                       |                       | may have              |
|                       |                       | difficulty/silent     |
|                       |                       | defects in            |
|                       |                       | interpreting it.      |
|                       |                       | Using a signed 64 bit |
|                       |                       | integer for storing   |
|                       |                       | this identifier is    |
|                       |                       | safe. Use             |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}**           |
|                       |                       | [` id_str `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} to fetch    |
|                       |                       | the identifier to be  |
|                       |                       | safe. See [Twitter    |
|                       |                       | IDs                   |
|                       |                       | ](https://developer.t |
|                       |                       | witter.com/en/docs/tw |
|                       |                       | itter-ids){.reference |
|                       |                       | .external} for more   |
|                       |                       | information. Example: |
+-----------------------+-----------------------+-----------------------+
| id_str                | String                | The string            |
|                       |                       | representation of the |
|                       |                       | unique identifier for |
|                       |                       | this Tweet.           |
|                       |                       | Implementations       |
|                       |                       | should use this       |
|                       |                       | rather than the large |
|                       |                       | integer in            |
|                       |                       | ` `{.docutils         |
|                       |                       | .litera               |
|                       |                       | l}**[` id `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} . Example:  |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "id_str":         |
|                       |                       | "1050118621198921728" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| text                  | String                | The actual UTF-8 text |
|                       |                       | of the status update. |
|                       |                       | See                   |
|                       |                       | [t                    |
|                       |                       | witter-text](https:// |
|                       |                       | github.com/twitter/tw |
|                       |                       | itter-text/blob/maste |
|                       |                       | r/rb/lib/twitter-text |
|                       |                       | /regex.rb){.reference |
|                       |                       | .external} for        |
|                       |                       | details on what       |
|                       |                       | characters are        |
|                       |                       | currently considered  |
|                       |                       | valid. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |    "text":"To make ro |
|                       |                       | om for more expressio |
|                       |                       | n, we will now count  |
|                       |                       | all emojis as equal—i |
|                       |                       | ncluding those with g |
|                       |                       | ender‍‍‍ ‍‍and skin t… htt |
|                       |                       | ps://t.co/MkGjXf9aXm" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| source                | String                | Utility used to post  |
|                       |                       | the Tweet, as an      |
|                       |                       | HTML-formatted        |
|                       |                       | string. Tweets from   |
|                       |                       | the Twitter website   |
|                       |                       | have a source value   |
|                       |                       | of ` `{.docutils      |
|                       |                       | .literal              |
|                       |                       | }**[` web `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} .           |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "source"          |
|                       |                       | :"Twitter Web Client" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| truncated             | Boolean               | Indicates whether the |
|                       |                       | value of the          |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}             |
|                       |                       | **[` text `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} parameter   |
|                       |                       | was truncated, for    |
|                       |                       | example, as a result  |
|                       |                       | of a retweet          |
|                       |                       | exceeding the         |
|                       |                       | original Tweet text   |
|                       |                       | length limit of 140   |
|                       |                       | characters. Truncated |
|                       |                       | text will end in      |
|                       |                       | ellipsis, like this   |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }**[` ... `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} Since       |
|                       |                       | Twitter now rejects   |
|                       |                       | long Tweets vs        |
|                       |                       | truncating them, the  |
|                       |                       | large majority of     |
|                       |                       | Tweets will have this |
|                       |                       | set to ` `{.docutils  |
|                       |                       | .literal}*            |
|                       |                       | *[` false `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} . Note that |
|                       |                       | while native retweets |
|                       |                       | may have their        |
|                       |                       | toplevel              |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}             |
|                       |                       | **[` text `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} property    |
|                       |                       | shortened, the        |
|                       |                       | original text will be |
|                       |                       | available under the   |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}**[` retweet |
|                       |                       | ed_status `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} object and  |
|                       |                       | the ` `{.docutils     |
|                       |                       | .literal}**[`         |
|                       |                       | truncated `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} parameter   |
|                       |                       | will be set to the    |
|                       |                       | value of the original |
|                       |                       | status (in most       |
|                       |                       | cases, ` `{.docutils  |
|                       |                       | .literal}*            |
|                       |                       | *[` false `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} ). Example: |
+-----------------------+-----------------------+-----------------------+
| in_reply_to_status_id | Int64                 | *Nullable.* If the    |
|                       |                       | represented Tweet is  |
|                       |                       | a reply, this field   |
|                       |                       | will contain the      |
|                       |                       | integer               |
|                       |                       | representation of the |
|                       |                       | original Tweet's ID.  |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "                 |
|                       |                       | in_reply_to_status_id |
|                       |                       | ":1051222721923756032 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| in_r                  | String                | *Nullable.* If the    |
| eply_to_status_id_str |                       | represented Tweet is  |
|                       |                       | a reply, this field   |
|                       |                       | will contain the      |
|                       |                       | string representation |
|                       |                       | of the original       |
|                       |                       | Tweet's ID. Example:  |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "in_rep           |
|                       |                       | ly_to_status_id_str": |
|                       |                       | "1051222721923756032" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| in_reply_to_user_id   | Int64                 | *Nullable.* If the    |
|                       |                       | represented Tweet is  |
|                       |                       | a reply, this field   |
|                       |                       | will contain the      |
|                       |                       | integer               |
|                       |                       | representation of the |
|                       |                       | original Tweet's      |
|                       |                       | author ID. This will  |
|                       |                       | not necessarily       |
|                       |                       | always be the user    |
|                       |                       | directly mentioned in |
|                       |                       | the Tweet. Example:   |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "in_repl          |
|                       |                       | y_to_user_id":6253282 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| in                    | String                | *Nullable.* If the    |
| _reply_to_user_id_str |                       | represented Tweet is  |
|                       |                       | a reply, this field   |
|                       |                       | will contain the      |
|                       |                       | string representation |
|                       |                       | of the original       |
|                       |                       | Tweet's author ID.    |
|                       |                       | This will not         |
|                       |                       | necessarily always be |
|                       |                       | the user directly     |
|                       |                       | mentioned in the      |
|                       |                       | Tweet. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "in_reply_to_u    |
|                       |                       | ser_id_str":"6253282" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| in                    | String                | *Nullable.* If the    |
| _reply_to_screen_name |                       | represented Tweet is  |
|                       |                       | a reply, this field   |
|                       |                       | will contain the      |
|                       |                       | screen name of the    |
|                       |                       | original Tweet's      |
|                       |                       | author. Example:      |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "in_reply_to_scre |
|                       |                       | en_name":"twitterapi" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| user                  | [User                 | The user who posted   |
|                       | object](/en/          | this Tweet. See User  |
|                       | docs/twitter-api/ente | data dictionary for   |
|                       | rprise/data-dictionar | complete list of      |
|                       | y/native-enriched-obj | attributes.           |
|                       | ects/user){.reference |                       |
|                       | .external}            | Example highlighting  |
|                       |                       | select attributes:    |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |      { "user": {      |
|                       |                       |                       |
|                       |                       |        "id": 6253282, |
|                       |                       |                       |
|                       |                       |  "id_str": "6253282", |
|                       |                       |         "             |
|                       |                       | name": "Twitter API", |
|                       |                       |         "screen       |
|                       |                       | _name": "TwitterAPI", |
|                       |                       |         "location":   |
|                       |                       |  "San Francisco, CA", |
|                       |                       |                       |
|                       |                       |    "url": "https://de |
|                       |                       | veloper.twitter.com", |
|                       |                       |         "d            |
|                       |                       | escription": "The Rea |
|                       |                       | l Twitter API. Tweets |
|                       |                       |  about API changes, s |
|                       |                       | ervice issues and our |
|                       |                       |  Developer Platform.  |
|                       |                       | Don't get an answer?  |
|                       |                       | It's on my website.", |
|                       |                       |                       |
|                       |                       |     "verified": true, |
|                       |                       |         "follo        |
|                       |                       | wers_count": 6129794, |
|                       |                       |                       |
|                       |                       |  "friends_count": 12, |
|                       |                       |         "             |
|                       |                       | listed_count": 12899, |
|                       |                       |         "f            |
|                       |                       | avourites_count": 31, |
|                       |                       |         "s            |
|                       |                       | tatuses_count": 3658, |
|                       |                       |         "crea         |
|                       |                       | ted_at": "Wed May 23  |
|                       |                       | 06:01:13 +0000 2007", |
|                       |                       |                       |
|                       |                       |   "utc_offset": null, |
|                       |                       |                       |
|                       |                       |    "time_zone": null, |
|                       |                       |                       |
|                       |                       | "geo_enabled": false, |
|                       |                       |         "lang": "en", |
|                       |                       |         "contribu     |
|                       |                       | tors_enabled": false, |
|                       |                       |         "i            |
|                       |                       | s_translator": false, |
|                       |                       |                       |
|                       |                       |        "profile_backg |
|                       |                       | round_color": "null", |
|                       |                       |                       |
|                       |                       |    "profile_backgroun |
|                       |                       | d_image_url": "null", |
|                       |                       |         "pr           |
|                       |                       | ofile_background_imag |
|                       |                       | e_url_https": "null", |
|                       |                       |         "profile_ba   |
|                       |                       | ckground_tile": null, |
|                       |                       |         "profile      |
|                       |                       | _link_color": "null", |
|                       |                       |                       |
|                       |                       |    "profile_sidebar_b |
|                       |                       | order_color": "null", |
|                       |                       |                       |
|                       |                       |      "profile_sidebar |
|                       |                       | _fill_color": "null", |
|                       |                       |         "profile      |
|                       |                       | _text_color": "null", |
|                       |                       |                       |
|                       |                       |      "profile_use_bac |
|                       |                       | kground_image": null, |
|                       |                       |         "profil       |
|                       |                       | e_image_url": "null", |
|                       |                       |                       |
|                       |                       | "profile_image_url_ht |
|                       |                       | tps": "https://pbs.tw |
|                       |                       | img.com/profile_image |
|                       |                       | s/942858479592554497/ |
|                       |                       | BbazLO9L_normal.jpg", |
|                       |                       |                       |
|                       |                       |    "profile_banner_ur |
|                       |                       | l": "https://pbs.twim |
|                       |                       | g.com/profile_banners |
|                       |                       | /6253282/1497491515", |
|                       |                       |         "def          |
|                       |                       | ault_profile": false, |
|                       |                       |         "default_p    |
|                       |                       | rofile_image": false, |
|                       |                       |                       |
|                       |                       |    "following": null, |
|                       |                       |         "follow       |
|                       |                       | _request_sent": null, |
|                       |                       |                       |
|                       |                       | "notifications": null |
|                       |                       |       }               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| coordinates           | [Coordinates](/en/d   | *Nullable.*           |
|                       | ocs/twitter-api/enter | Represents the        |
|                       | prise/data-dictionary | geographic location   |
|                       | /native-enriched-obje | of this Tweet as      |
|                       | cts/geo#coordinates-d | reported by the user  |
|                       | ictionary){.reference | or client             |
|                       | .external}            | application. The      |
|                       |                       | inner coordinates     |
|                       |                       | array is formatted as |
|                       |                       | [ge                   |
|                       |                       | oJSON](http://www.geo |
|                       |                       | json.org/){.reference |
|                       |                       | .external} (longitude |
|                       |                       | first, then           |
|                       |                       | latitude). Example:   |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "coordinates":    |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |        "coordinates": |
|                       |                       |         [             |
|                       |                       |                       |
|                       |                       |         -75.14310264, |
|                       |                       |                       |
|                       |                       |           40.05701649 |
|                       |                       |         ],            |
|                       |                       |                       |
|                       |                       |        "type":"Point" |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| place                 | [Places]              | *Nullable* When       |
|                       | (/en/docs/twitter-api | present, indicates    |
|                       | /enterprise/data-dict | that the tweet is     |
|                       | ionary/native-enriche | associated (but not   |
|                       | d-objects/geo#place-d | necessarily           |
|                       | ictionary){.reference | originating from) a   |
|                       | .external}            | Place  Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "place":          |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |      "attributes":{}, |
|                       |                       |                       |
|                       |                       |       "bounding_box": |
|                       |                       |       {               |
|                       |                       |                       |
|                       |                       |        "coordinates": |
|                       |                       |          [[           |
|                       |                       |                [-     |
|                       |                       | 77.119759,38.791645], |
|                       |                       |                [-     |
|                       |                       | 76.909393,38.791645], |
|                       |                       |                [-     |
|                       |                       | 76.909393,38.995548], |
|                       |                       |                [      |
|                       |                       | -77.119759,38.995548] |
|                       |                       |          ]],          |
|                       |                       |                       |
|                       |                       |      "type":"Polygon" |
|                       |                       |       },              |
|                       |                       |        "coun          |
|                       |                       | try":"United States", |
|                       |                       |                       |
|                       |                       |  "country_code":"US", |
|                       |                       |        "full_na       |
|                       |                       | me":"Washington, DC", |
|                       |                       |        "id            |
|                       |                       | ":"01fbe706f872cb32", |
|                       |                       |                       |
|                       |                       |  "name":"Washington", |
|                       |                       |                       |
|                       |                       |  "place_type":"city", |
|                       |                       |        "url":"http    |
|                       |                       | ://api.twitter.com/1/ |
|                       |                       | geo/id/0172cb32.json" |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| quoted_status_id      | Int64                 | This field only       |
|                       |                       | surfaces when the     |
|                       |                       | Tweet is a quote      |
|                       |                       | Tweet. This field     |
|                       |                       | contains the integer  |
|                       |                       | value Tweet ID of the |
|                       |                       | quoted Tweet.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "quoted_status_id |
|                       |                       | ":1050119905717055488 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| quoted_status_id_str  | String                | This field only       |
|                       |                       | surfaces when the     |
|                       |                       | Tweet is a quote      |
|                       |                       | Tweet. This is the    |
|                       |                       | string representation |
|                       |                       | Tweet ID of the       |
|                       |                       | quoted Tweet.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "q                |
|                       |                       | uoted_status_id_str": |
|                       |                       | "1050119905717055488" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| is_quote_status       | Boolean               | Indicates whether     |
|                       |                       | this is a Quoted      |
|                       |                       | Tweet. Example:       |
+-----------------------+-----------------------+-----------------------+
| quoted_status         | Tweet                 | This field only       |
|                       |                       | surfaces when the     |
|                       |                       | Tweet is a quote      |
|                       |                       | Tweet. This attribute |
|                       |                       | contains the Tweet    |
|                       |                       | object of the         |
|                       |                       | original Tweet that   |
|                       |                       | was quoted.           |
+-----------------------+-----------------------+-----------------------+
| retweeted_status      | Tweet                 | Users can amplify the |
|                       |                       | broadcast of Tweets   |
|                       |                       | authored by other     |
|                       |                       | users by Retweeting . |
|                       |                       | Retweets can be       |
|                       |                       | distinguished from    |
|                       |                       | typical Tweets by the |
|                       |                       | existence of a        |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}**[` retweet |
|                       |                       | ed_status `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} attribute.  |
|                       |                       | This attribute        |
|                       |                       | contains a            |
|                       |                       | representation of the |
|                       |                       | *original* Tweet that |
|                       |                       | was retweeted. Note   |
|                       |                       | that retweets of      |
|                       |                       | retweets do not show  |
|                       |                       | representations of    |
|                       |                       | the intermediary      |
|                       |                       | retweet, but only the |
|                       |                       | original Tweet.       |
|                       |                       | (Users can also       |
|                       |                       | unretweet a retweet   |
|                       |                       | they created by       |
|                       |                       | deleting their        |
|                       |                       | retweet.)             |
+-----------------------+-----------------------+-----------------------+
| quote_count           | Integer               | *Nullable.* Indicates |
|                       |                       | approximately how     |
|                       |                       | many times this Tweet |
|                       |                       | has been quoted by    |
|                       |                       | Twitter users.        |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       |     "quote_count":33  |
|                       |                       |                       |
|                       |                       | Note: This object is  |
|                       |                       | only available with   |
|                       |                       | the Premium and       |
|                       |                       | Enterprise tier       |
|                       |                       | products.             |
+-----------------------+-----------------------+-----------------------+
| reply_count           | Int                   | Number of times this  |
|                       |                       | Tweet has been        |
|                       |                       | replied to. Example:  |
|                       |                       |                       |
|                       |                       |     "reply_count":30  |
|                       |                       |                       |
|                       |                       | Note: This object is  |
|                       |                       | only available with   |
|                       |                       | the Premium and       |
|                       |                       | Enterprise tier       |
|                       |                       | products.             |
+-----------------------+-----------------------+-----------------------+
| retweet_count         | Int                   | Number of times this  |
|                       |                       | Tweet has been        |
|                       |                       | retweeted. Example:   |
+-----------------------+-----------------------+-----------------------+
| favorite_count        | Integer               | *Nullable.* Indicates |
|                       |                       | approximately how     |
|                       |                       | many times this Tweet |
|                       |                       | has been liked by     |
|                       |                       | Twitter users.        |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| entities              | [Entities](/en/docs   | Entities which have   |
|                       | /twitter-api/enterpri | been parsed out of    |
|                       | se/data-dictionary/na | the text of the       |
|                       | tive-enriched-objects | Tweet. Additionally   |
|                       | /entities){.reference | see [Entities in      |
|                       | .external}            | Twitter               |
|                       |                       | Obj                   |
|                       |                       | ects](/en/docs/twitte |
|                       |                       | r-api/v1/data-diction |
|                       |                       | ary/object-model/enti |
|                       |                       | ties.html){.reference |
|                       |                       | .external} . Example: |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "entities":       |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |        "hashtags":[], |
|                       |                       |         "urls":[],    |
|                       |                       |                       |
|                       |                       |   "user_mentions":[], |
|                       |                       |         "media":[],   |
|                       |                       |         "symbols":[]  |
|                       |                       |         "polls":[]    |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| extended_entities     | [Extended             | When between one and  |
|                       | Entities](/en/docs    | four native photos or |
|                       | /twitter-api/enterpri | one video or one      |
|                       | se/data-dictionary/na | animated GIF are in   |
|                       | tive-enriched-objects | Tweet, contains an    |
|                       | /entities){.reference | array \'media\'       |
|                       | .external}            | metadata. This is     |
|                       |                       | also available in     |
|                       |                       | Quote Tweets.         |
|                       |                       | Additionally see      |
|                       |                       | [Entities in Twitter  |
|                       |                       | Objects](/en          |
|                       |                       | /docs/twitter-api/v1/ |
|                       |                       | data-dictionary/objec |
|                       |                       | t-model/extended-enti |
|                       |                       | ties.html){.reference |
|                       |                       | .external} . Example: |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "entities":       |
|                       |                       |     {                 |
|                       |                       |         "media":[]    |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| favorited             | Boolean               | *Nullable.* Indicates |
|                       |                       | whether this Tweet    |
|                       |                       | has been liked by the |
|                       |                       | authenticating user.  |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| retweeted             | Boolean               | Indicates whether     |
|                       |                       | this Tweet has been   |
|                       |                       | Retweeted by the      |
|                       |                       | authenticating user.  |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| possibly_sensitive    | Boolean               | *Nullable.* This      |
|                       |                       | field indicates       |
|                       |                       | content may be        |
|                       |                       | recognized as         |
|                       |                       | sensitive. The Tweet  |
|                       |                       | author can select     |
|                       |                       | within their own      |
|                       |                       | account preferences   |
|                       |                       | and choose "Mark      |
|                       |                       | media you tweet as    |
|                       |                       | having material that  |
|                       |                       | may be sensitive" so  |
|                       |                       | each Tweet created    |
|                       |                       | after has this flag   |
|                       |                       | set.                  |
|                       |                       |                       |
|                       |                       | This may also be      |
|                       |                       | judged and labeled by |
|                       |                       | an internal Twitter   |
|                       |                       | support agent.        |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "poss             |
|                       |                       | ibly_sensitive":false |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| filter_level          | String                | Indicates the maximum |
|                       |                       | value of the          |
|                       |                       | filter_level          |
|                       |                       | parameter which may   |
|                       |                       | be used and still     |
|                       |                       | stream this Tweet. So |
|                       |                       | a value of            |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}**           |
|                       |                       | [` medium `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} will be     |
|                       |                       | streamed on           |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}             |
|                       |                       | **[` none `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} ,           |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }**[` low `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} , and       |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}**           |
|                       |                       | [` medium `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} streams.    |
|                       |                       |                       |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| lang                  | String                | *Nullable.* When      |
|                       |                       | present, indicates a  |
|                       |                       | [BCP                  |
|                       |                       | 47](ht                |
|                       |                       | tp://tools.ietf.org/h |
|                       |                       | tml/bcp47){.reference |
|                       |                       | .external} language   |
|                       |                       | identifier            |
|                       |                       | corresponding to the  |
|                       |                       | machine-detected      |
|                       |                       | language of the Tweet |
|                       |                       | text, or              |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }**[` und `{.docutils |
|                       |                       | .literal}]            |
|                       |                       | {.pre}**` `{.docutils |
|                       |                       | .literal} if no       |
|                       |                       | language could be     |
|                       |                       | detected.             |
|                       |                       |                       |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| edit_history          | Object                | Unique identifiers    |
|                       |                       | indicating all        |
|                       |                       | versions of a Tweet.  |
|                       |                       | For Tweets with no    |
|                       |                       | edits, there will be  |
|                       |                       | one ID. For Tweets    |
|                       |                       | with an edit history, |
|                       |                       | there will be         |
|                       |                       | multiple IDs,         |
|                       |                       | arranged in ascending |
|                       |                       | order reflecting the  |
|                       |                       | order of edits, with  |
|                       |                       | the most recent       |
|                       |                       | version in the last   |
|                       |                       | position of the       |
|                       |                       | array.                |
|                       |                       |                       |
|                       |                       | The Tweet IDs can be  |
|                       |                       | used to hydrate and   |
|                       |                       | view previous         |
|                       |                       | versions of a Tweet.  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     edit_history": {  |
|                       |                       |         "initial_tw   |
|                       |                       | eet_id": "1283764123" |
|                       |                       |         "edi          |
|                       |                       | t_tweet_ids": ["12837 |
|                       |                       | 64123", "1394263866"] |
|                       |                       |       }               |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| edit_controls         | Object                | When present,         |
|                       |                       | indicates how long a  |
|                       |                       | Tweet is still        |
|                       |                       | editable for and the  |
|                       |                       | number of remaining   |
|                       |                       | edits. Tweets are     |
|                       |                       | only editable for the |
|                       |                       | first 30 minutes      |
|                       |                       | after creation and    |
|                       |                       | can be edited up to   |
|                       |                       | five times.           |
|                       |                       |                       |
|                       |                       | The Tweet IDs can be  |
|                       |                       | used to hydrate and   |
|                       |                       | view previous         |
|                       |                       | versions of a Tweet.  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |  "edit_controls": {   |
|                       |                       |          "ed          |
|                       |                       | itable_until_ms": 123 |
|                       |                       |          "e           |
|                       |                       | dits_remaining": 3    |
|                       |                       |       }               |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| editable              | Boolean               | When present,         |
|                       |                       | indicates if a Tweet  |
|                       |                       | was eligible for edit |
|                       |                       | when published. This  |
|                       |                       | field is not dynamic  |
|                       |                       | and won\'t toggle     |
|                       |                       | from True to False    |
|                       |                       | when a Tweet reaches  |
|                       |                       | its editable time     |
|                       |                       | limit, or maximum     |
|                       |                       | number of edits. The  |
|                       |                       | following Tweet       |
|                       |                       | features will cause   |
|                       |                       | this field to be      |
|                       |                       | false:                |
|                       |                       |                       |
|                       |                       | -   Tweets is         |
|                       |                       |     promoted          |
|                       |                       | -   Tweet has a poll  |
|                       |                       | -   Tweet is a        |
|                       |                       |     non-self-thread   |
|                       |                       |     reply             |
|                       |                       | -   Tweet is a        |
|                       |                       |     retweet (note     |
|                       |                       |     that Quote Tweets |
|                       |                       |     are eligible for  |
|                       |                       |     edit)             |
|                       |                       | -   Tweet is nullcast |
|                       |                       | -   Community Tweet   |
|                       |                       | -   Superfollow Tweet |
|                       |                       | -   Collaborative     |
|                       |                       |     Tweet             |
+-----------------------+-----------------------+-----------------------+
| matching_rules        | Array of Rule Objects | Present in *filtered* |
|                       |                       | products such as      |
|                       |                       | Twitter Search and    |
|                       |                       | PowerTrack. Provides  |
|                       |                       | the *id* and *tag*    |
|                       |                       | associated with the   |
|                       |                       | rule that matched the |
|                       |                       | Tweet. More on        |
|                       |                       | matching rules        |
|                       |                       | [here](/en/docs/t     |
|                       |                       | witter-api/enterprise |
|                       |                       | /enrichments/overview |
|                       |                       | /matching-rules.html) |
|                       |                       | . With PowerTrack,    |
|                       |                       | more than one rule    |
|                       |                       | can match a Tweet.    |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "                 |
|                       |                       | matching_rules": " [{ |
|                       |                       |             "tag":    |
|                       |                       |  "twitterapi emojis", |
|                       |                       |             "id":     |
|                       |                       |  1050118621198921728, |
|                       |                       |                       |
|                       |                       |            "id_str":  |
|                       |                       | "1050118621198921728" |
|                       |                       |         }]"           |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+

### Additional Tweet attributes

Twitter APIs that provide Tweets (e.g. the GET statuses/lookup endpoint)
may include these additional Tweet attributes:

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| current_user_retweet  | Object                | *Perspectival* Only   |
|                       |                       | surfaces on methods   |
|                       |                       | supporting            |
|                       |                       | t                     |
|                       |                       | he include_my_retweet |
|                       |                       | parameter, when set   |
|                       |                       | to true. Details the  |
|                       |                       | Tweet ID of the       |
|                       |                       | user's own retweet    |
|                       |                       | (if existent) of this |
|                       |                       | Tweet. Example:       |
|                       |                       |                       |
|                       |                       |     "cur              |
|                       |                       | rent_user_retweet": { |
|                       |                       |       "id": 6253282,  |
|                       |                       |                       |
|                       |                       |   "id_str": "6253282" |
|                       |                       |     }                 |
+-----------------------+-----------------------+-----------------------+
| scopes                | Object                | A set of key-value    |
|                       |                       | pairs indicating the  |
|                       |                       | intended contextual   |
|                       |                       | delivery of the       |
|                       |                       | containing Tweet.     |
|                       |                       | Currently used by     |
|                       |                       | Twitter's Promoted    |
|                       |                       | Products. Example:    |
|                       |                       |                       |
|                       |                       |     "scopes           |
|                       |                       | ":{"followers":false} |
+-----------------------+-----------------------+-----------------------+
| withheld_copyright    | Boolean               | When present and set  |
|                       |                       | to "true", it         |
|                       |                       | indicates that this   |
|                       |                       | piece of content has  |
|                       |                       | been withheld due to  |
|                       |                       | a [DMCA               |
|                       |                       | complaint]            |
|                       |                       | (http://en.wikipedia. |
|                       |                       | org/wiki/Digital_Mill |
|                       |                       | ennium_Copyright_Act) |
|                       |                       | . Example:            |
|                       |                       |                       |
|                       |                       |     "with             |
|                       |                       | held_copyright": true |
+-----------------------+-----------------------+-----------------------+
| withheld_in_countries | Array of String       | When present,         |
|                       |                       | indicates a list of   |
|                       |                       | uppercase [two-letter |
|                       |                       | country               |
|                       |                       | codes](http:/         |
|                       |                       | /en.wikipedia.org/wik |
|                       |                       | i/ISO_3166-1_alpha-2) |
|                       |                       | this content is       |
|                       |                       | withheld from.        |
|                       |                       | Twitter supports the  |
|                       |                       | following non-country |
|                       |                       | values for this       |
|                       |                       | field:                |
|                       |                       |                       |
|                       |                       | "XX" - Content is     |
|                       |                       | withheld in all       |
|                       |                       | countries "XY" -      |
|                       |                       | Content is withheld   |
|                       |                       | due to a DMCA         |
|                       |                       | request.              |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       |     "                 |
|                       |                       | withheld_in_countries |
|                       |                       | ": ["GR", "HK", "MY"] |
+-----------------------+-----------------------+-----------------------+
| withheld_scope        | String                | When present,         |
|                       |                       | indicates whether the |
|                       |                       | content being         |
|                       |                       | withheld is the       |
|                       |                       | "status" or a "user." |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       |     "with             |
|                       |                       | held_scope": "status" |
+-----------------------+-----------------------+-----------------------+

### Deprecated Attributes

  ----------------------- ----------------------- -------------------------------------
  Field                   Type                    Description

  geo                     Object                  **Deprecated.** *Nullable.* Use the
                                                  ` `{.docutils
                                                  .literal}[` coordinates `{.docutils
                                                  .literal}]{.pre}` `{.docutils
                                                  .literal} field instead. This
                                                  deprecated attribute has its
                                                  coordinates formatted as *\[lat,
                                                  long\]* , while all other Tweet geo
                                                  is formatted as *\[long, lat\]* .
  ----------------------- ----------------------- -------------------------------------

##  []{#nested-tweet-objects} Nested Tweet objects

In several cases, a Tweet object will included other nested objects.  If
you are working with nested objects, then that JSON payload will contain
multiple Tweet objects, and each Tweet object may contain its own
objects. The root-level object will contain information on the type of
action taken, i.e. whether it is a Retweet or a Quote Tweet, and may
also contain an object that describes the \'original\' Tweet being
shared. Extended Tweets will include a nested extended object that
extends beyond 140 characters, which was used to prevent breaking
changes when the update was made in 2017. Each nested object dictionary
is described below.
:::
:::

::: c01-rich-text-editor
::: is-table-default
#### []{#retweet} Retweets

Retweets always contain two Tweet objects. The \'original\' Tweet being
Retweeted is provided in a \"retweeted_status\" object. The root-level
object encapsulates the Retweet itself, including a User object for the
account taking the Retweet action and the time of the Retweet.
Retweeting is an action to share a Tweet with your followers, and no
other new content can be added. Also, a (new) location cannot be
provided with a Retweet. While the \'original\' Tweet may have
geo-tagged, the Retweet \"geo\" and \"place\" objects will always be
null.

Even before the introduction of Extended Tweets, the root-level
\"entities\" object was in some cases truncated and incomplete due to
the \"RT \@username \" string being appended to Tweet message being
Retweeted.  Note that if a Retweet gets Retweeted, the
\"retweet_status\" will still point to the original Tweet, meaning the
intermediate Retweet is not included. Similar behavior is seen when
using twitter.com to \'display\' a Retweet. If you copy the unique Tweet
ID assigned to the Retweet \'action\', the original Tweet is displayed.

Below is an example structure for a Retweet. Again, when parsing
Retweets, it is key to parse the \"retweeted_status\" object for
complete (original) Tweet message and entity metadata.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "tweet": {
        "text": "RT @author original message",
        "user": {
            "screen_name": "Retweeter"
        },
        "retweeted_status": {
            "text": "original message",
            "user": {
                "screen_name": "OriginalTweeter"
            },
            "place": {},
            "entities": {},
            "extended_entities": {}
        }
    },
    "entities": {},
    "extended_entities": {}
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
#### []{#quotetweet} Quote Tweets

Quote Tweets are much like Retweets except that they include a new Tweet
message. These new messages can contain their own set of hashtags,
links, and other \"entities\" metadata. Quote Tweets can also include
location information shared by the user posting the Quote Tweet, along
with media such as GIFs, videos, and photos.

Quote Tweets will contain at least two Tweet objects, and in some cases,
three. The Tweet being Quoted, which itself can be a Quoted Tweet, is
provided in a \"quoted_status\" object. The root-level object
encapsulates the Quote Tweet itself, including a User object for the
account taking the sharing action and the time of the Quote Tweet.

Note that Quote Tweets can now have photos, GIFs, or videos, added to
them using the \'post Tweet\' user-interface. When links to externally
hosted media are included in the Quote Tweet message, the root-level
\"entities.urls\" will describe those. Media attached to Quote Tweets
will appear in the root-level \"extended_entities\" metadata.

When Quote Tweets were first launched, a shortened link (t.co URL) was
appended to the \'original\' Tweet message and provided in the
root-level \"text\" field. In addition, metadata for that t.co URL was
included in the root-level \'entities.urls\' array. In May 2018, we
changed this so that the shortened t.co URL to the quoted Tweet *will
not be included* in the root-level \"text\" field. Second, the metadata
for the quoted Tweet *will not be included* in the \"entities.urls\"
metadata. Instead, URL metadata for the quoted Tweet will be in a new
\"quoted_status_permalink\" object on the root-level (or top-level), so
at the same level of the \"quoted_status\" object.

Below is an example structure for a Quote Tweet using this original
formatting.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "created_at": "Tue Feb 14 19:30:06 +0000 2017",
    "id_str": "831586333415976960",
    "text": "Definitely quotable! https:\/\/t.co\/J1LKrbHpWR",
    "user": {
        "screen_name": "happycamper"
    },
    "quoted_status_id_str": "831569219296882688",
    "quoted_status": {
        "created_at": "Tue Feb 14 18:22:06 +0000 2017",
        "id_str": "831569219296882688",
        "text": "This is a test of the tweeting system \ud83d\ude0e to update #supportdocs @twitterboulder here: https:\/\/t.co\/NRq9UrSzm0",
        "user": {
            "screen_name": "furiouscamper",
        },
        "place": {
            "id": "9a974dfc8efb32a0",
        },
        "entities": {
            "hashtags": [{
                "text": "supportdocs",
            }],
            "urls": [{
            }],
            "user_mentions": [{   }],
            "symbols": []
        },
    },
    "is_quote_status": true,
    "entities": {},
    "matching_rules": [{}]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "created_at": "Fri Jan 04 18:47:16 +0000 2019",
    "id_str": "1081260794069671936",
    "text": "Quote test https://t.co/CE4m1qs3NJ",
    "user": {
        "screen_name": "furiouscamper"
    },
    "place": null,
    "quoted_status_id_str": "1079578364904648705",
    "quoted_status": {
        "created_at": "Mon Dec 31 03:21:54 +0000 2018",
        "id_str": "1079578364904648705",
        "text": "AHHHHH",
        "user": {
            "screen_name": "infinite_scream"
        },
        "place": null,
        "is_quote_status": false,
        "quote_count": 1,
        "reply_count": 0,
        "retweet_count": 3,
        "favorite_count": 6,
        "entities": {
            "hashtags": [],
            "urls": [],
            "user_mentions": [],
            "symbols": []
        }
    },
    "quoted_status_permalink": {
        "url": "https://t.co/CE4m1qs3NJ",
        "expanded": "https://twitter.com/infinite_scream/status/1079578364904648705",
        "display": "twitter.com/infinite_screa…"
    },
    "is_quote_status": true,
    "quote_count": 0,
    "reply_count": 0,
    "retweet_count": 0,
    "favorite_count": 1,
    "entities": {}
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
### []{#extendedtweet} Extended Tweets

JSON that describes *Extended Tweets* was introduced when 280-character
Tweets were launched in November 2017. Tweet JSON was extended to
encapsulate these longer messages, while not breaking the thousands of
apps parsing these fundamental Twitter objects. To provide full backward
compatibility, the original 140-character \'text\' field, and the entity
objects parsed from that, were retained. In the case of Tweets longer
than 140 characters, this root-level \'text\' field would become
truncated and thus incomplete. Since the root-level \'entities\' objects
contain arrays of key metadata parsed from the \'text\' message, such as
included hashtags and links, these collections would be incomplete. For
example, if a Tweet message was 200 characters long, with a hashtag
included at the end, the legacy root-level
\'entities.hashtags\' array would not include it.

A new \'extended_tweet\' field was introduced to hold the longer Tweet
messages and complete entity metadata. The \"extended_tweet\" object
provides the \"full_text\" field that contains the complete, untruncated
Tweet message when longer than 140 characters. The \"extended_tweet\"
object also contains an \"entities\" object with complete arrays of
hashtags, links, mentions, etc.

Extended Tweets are identified with a root-level \"truncated\" boolean.
When true (\"truncated\": true), the \"extended_tweet\" fields should be
parsed instead of the root-level fields.

Note in the JSON example below that the root-level \"text\" field is
truncated and the root-level \"entities.hashtags\" array is empty even
though the Tweet message includes three hashtags. Since this is an
Extended Tweet, the \"truncated\" field is set to true, and the
\"extended_tweet\" object provides complete \"full_text\" and
\"entities\" Tweet metadata.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "created_at": "Thu May 10 17:41:57 +0000 2018",
    "id_str": "994633657141813248",
    "text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"tru… https://t.co/U7Se4NM7Eu",
    "display_text_range": [0, 140],
    "truncated": true,
    "user": {
        "id_str": "944480690",
        "screen_name": "FloodSocial"
    },
    "extended_tweet": {
        "full_text": "Just another Extended Tweet with more than 140 characters, generated as a documentation example, showing that [\"truncated\": true] and the presence of an \"extended_tweet\" object with complete text and \"entities\" #documentation #parsingJSON #GeoTagged https://t.co/e9yhQTJSIA",
        "display_text_range": [0, 249],
        "entities": {
            "hashtags": [{
                "text": "documentation",
                "indices": [211, 225]
            }, {
                "text": "parsingJSON",
                "indices": [226, 238]
            }, {
                "text": "GeoTagged",
                "indices": [239, 249]
            }]
        }

    },
    "entities": {
        "hashtags": []
    }
}
    
```
:::
:::
:::
:::
