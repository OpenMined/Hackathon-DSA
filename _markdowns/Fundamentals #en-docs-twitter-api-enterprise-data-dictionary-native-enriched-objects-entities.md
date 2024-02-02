::: is-table-default
Entities provide metadata and additional contextual information about
content posted on Twitter. The ` entities ` section provides arrays of
common things included in Tweets: hashtags, user mentions, links, stock
tickers (symbols), Twitter polls, and attached media. These arrays are
convenient for developers when ingesting Tweets, since Twitter has
essentially pre-processed, or pre-parsed, the text body. Instead of
needing to explicitly search and find these entities in the Tweet body,
your parser can go straight to this JSON section and there they are.

Beyond providing parsing conveniences, the ` entities ` section also
provides useful 'value-add' metadata. For example, if you are using the
[Enhanced URLs
enrichment](/en/docs/twitter-api/enterprise/enrichments/overview/expanded-and-enhanced-urls)
, URL metadata include fully-expanded URLs, as well as associated
website titles and descriptions. Another example is when there are user
mentions, the entities metadata include the numeric user ID, which are
useful when making requests to many Twitter APIs.

Every Tweet JSON payload includes an ` entities ` section, with the
minimum set of ` hashtags ` , ` urls ` , ` user_mentions ` , and
` symbols ` attributes, even if none of those entities are part of the
Tweet message. For example, if you examine the JSON for a Tweet with a
body of "Hello World!" and no attached media, the Tweet's JSON will
include the following content with entity arrays containing zero items:

    "entities": {
        "hashtags": [
        ],
        "urls": [
        ],
        "user_mentions": [
        ],
        "symbols": [
        ]
      }

Notes:

-   media and polls entities will only appear when that type of content
    is part of the Tweet.
-   if you are working with native media (photos, videos, or GIFs), the
    [Extended Entities
    object](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/extended-entities)
    is the way to go.

## Entities object []{#entitiesobject} []{.tall}

The ` entities ` and ` extended_entities ` sections are both made up of
arrays of entity *objects* . Below you will find descriptions for each
of these entity objects, including data dictionaries that describe the
object attribute names, types, and short description. We'll also
indicate which PowerTrack Operators match these attributes, and include
some sample JSON payloads.

A collection of common entities found in Tweets, including hashtags,
links, and user mentions. This ` entities ` object does include a
` media ` attribute, but its implementation in the ` entiites ` section
is only completely accurate for Tweets with a single photo. For all
Tweets with more than one photo, a video, or animated GIF, the reader is
directed to the ` extended_entities ` section.

### Entities data dictionary

The entities object is a holder of arrays of other entity sub-objects.
After illustrating the ` entities ` structure, data dictionaries for
these sub-objects, and the Operators that match them, will be provided.

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| hashtags              | Array of [Hashtag     | Represents hashtags   |
|                       | Objects](             | which have been       |
|                       | #hashtags){.reference | parsed out of the     |
|                       | .external}            | Tweet text. Example:  |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |       "hashtags": [   |
|                       |                       |         {             |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |             32,       |
|                       |                       |             38        |
|                       |                       |           ],          |
|                       |                       |                       |
|                       |                       |      "text": "nodejs" |
|                       |                       |         }             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| media                 | Array of [Media       | Represents media      |
|                       | Object                | elements uploaded     |
|                       | s](#media){.reference | with the Tweet.       |
|                       | .external}            | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |       "media": [      |
|                       |                       |         {             |
|                       |                       |           "d          |
|                       |                       | isplay_url": "pic.twi |
|                       |                       | tter.com/5J1WJSRCy9", |
|                       |                       |                       |
|                       |                       |  "expanded_url": "htt |
|                       |                       | ps://twitter.com/nola |
|                       |                       | n_test/status/9300778 |
|                       |                       | 47535812610/photo/1", |
|                       |                       |           "id":       |
|                       |                       | 9.300778475358126e17, |
|                       |                       |           "id_str":   |
|                       |                       | "930077847535812610", |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |               13,     |
|                       |                       |               36      |
|                       |                       |           ],          |
|                       |                       |                       |
|                       |                       |  "media_url": "http:/ |
|                       |                       | /pbs.twimg.com/media/ |
|                       |                       | DOhM30VVwAEpIHq.jpg", |
|                       |                       |           "medi       |
|                       |                       | a_url_https": "https: |
|                       |                       | //pbs.twimg.com/media |
|                       |                       | /DOhM30VVwAEpIHq.jpg" |
|                       |                       |           "sizes": {  |
|                       |                       |                       |
|                       |                       |            "thumb": { |
|                       |                       |                       |
|                       |                       |             "h": 150, |
|                       |                       |                       |
|                       |                       |     "resize": "crop", |
|                       |                       |                       |
|                       |                       |              "w": 150 |
|                       |                       |               },      |
|                       |                       |                       |
|                       |                       |            "large": { |
|                       |                       |                       |
|                       |                       |            "h": 1366, |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |                       |
|                       |                       |             "w": 2048 |
|                       |                       |               },      |
|                       |                       |                       |
|                       |                       |           "medium": { |
|                       |                       |                       |
|                       |                       |             "h": 800, |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |                       |
|                       |                       |             "w": 1200 |
|                       |                       |               },      |
|                       |                       |                       |
|                       |                       |            "small": { |
|                       |                       |                       |
|                       |                       |             "h": 454, |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |                       |
|                       |                       |              "w": 680 |
|                       |                       |               }       |
|                       |                       |           },          |
|                       |                       |           "           |
|                       |                       | type": "photo",       |
|                       |                       |                       |
|                       |                       |          "url": "http |
|                       |                       | s://t.co/5J1WJSRCy9", |
|                       |                       |         }             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| urls                  | Array of [URL         | Represents URLs       |
|                       | Objec                 | included in the text  |
|                       | ts](#urls){.reference | of a Tweet.           |
|                       | .external}            |                       |
|                       |                       | Example (without      |
|                       |                       | Enhanced URLs         |
|                       |                       | enrichment enabled):  |
|                       |                       |                       |
|                       |                       | ::: {.code .javascri  |
|                       |                       | pt .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |       "urls": [       |
|                       |                       |         {             |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |             32,       |
|                       |                       |             52        |
|                       |                       |           ],          |
|                       |                       |           "url": "h   |
|                       |                       | ttp://t.co/IOwBrTZR", |
|                       |                       |           "di         |
|                       |                       | splay_url": "youtube. |
|                       |                       | com/watch?v=oHg5SJ…", |
|                       |                       |                       |
|                       |                       |    "expanded_url": "h |
|                       |                       | ttp://www.youtube.com |
|                       |                       | /watch?v=oHg5SJYRHA0" |
|                       |                       |         }             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | Example (with         |
|                       |                       | Enhanced URLs         |
|                       |                       | enrichment enabled):  |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {"urls": [        |
|                       |                       |           {           |
|                       |                       |                       |
|                       |                       |          "url": "http |
|                       |                       | s://t.co/D0n7a53c2l", |
|                       |                       |                       |
|                       |                       |   "expanded_url": "ht |
|                       |                       | tp://bit.ly/18gECvy", |
|                       |                       |                       |
|                       |                       |           "display_ur |
|                       |                       | l": "bit.ly/18gECvy", |
|                       |                       |                       |
|                       |                       |          "unwound": { |
|                       |                       |                       |
|                       |                       |           "url": "htt |
|                       |                       | ps://www.youtube.com/ |
|                       |                       | watch?v=oHg5SJYRHA0", |
|                       |                       |                       |
|                       |                       |        "status": 200, |
|                       |                       |               "       |
|                       |                       | title": "RickRoll'D", |
|                       |                       |                       |
|                       |                       |   "description": "htt |
|                       |                       | p://www.facebook.com/ |
|                       |                       | rickroll548 As long a |
|                       |                       | s trolls are still tr |
|                       |                       | olling, the Rick will |
|                       |                       |  never stop rolling." |
|                       |                       |             },        |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |               62,     |
|                       |                       |               85      |
|                       |                       |             ]         |
|                       |                       |           }           |
|                       |                       |         ]             |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| user_mentions         | Array of [User        | Represents other      |
|                       | Mention               | Twitter users         |
|                       | Objects](             | mentioned in the text |
|                       | #mentions){.reference | of the Tweet.         |
|                       | .external}            | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |    "user_mentions": [ |
|                       |                       |         {             |
|                       |                       |           "           |
|                       |                       | name": "Twitter API", |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |             4,        |
|                       |                       |             15        |
|                       |                       |           ],          |
|                       |                       |           "screen     |
|                       |                       | _name": "twitterapi", |
|                       |                       |                       |
|                       |                       |        "id": 6253282, |
|                       |                       |                       |
|                       |                       |   "id_str": "6253282" |
|                       |                       |         }             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| symbols               | Array of [Symbol      | Represents symbols,   |
|                       | Objects]              | i.e. \$cashtags,      |
|                       | (#symbols){.reference | included in the text  |
|                       | .external}            | of the Tweet.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |       "symbols": [    |
|                       |                       |         {             |
|                       |                       |                       |
|                       |                       |          "indices": [ |
|                       |                       |             12,       |
|                       |                       |             17        |
|                       |                       |           ],          |
|                       |                       |                       |
|                       |                       |        "text": "twtr" |
|                       |                       |         }             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| polls                 | Array of [Poll        | Represents Twitter    |
|                       | Object                | Polls included in the |
|                       | s](#polls){.reference | Tweet. Example:       |
|                       | .external}            |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {"polls": [       |
|                       |                       |           {           |
|                       |                       |                       |
|                       |                       |          "options": [ |
|                       |                       |               {       |
|                       |                       |                       |
|                       |                       |        "position": 1, |
|                       |                       |                       |
|                       |                       |       "text": "I read |
|                       |                       |  documentation once." |
|                       |                       |               },      |
|                       |                       |               {       |
|                       |                       |                       |
|                       |                       |        "position": 2, |
|                       |                       |                       |
|                       |                       |      "text": "I read  |
|                       |                       | documentation twice." |
|                       |                       |               },      |
|                       |                       |               {       |
|                       |                       |                       |
|                       |                       |        "position": 3, |
|                       |                       |                       |
|                       |                       |             "text": " |
|                       |                       | I read documentation  |
|                       |                       | over and over again." |
|                       |                       |               }       |
|                       |                       |             ],        |
|                       |                       |             "end_da   |
|                       |                       | tetime": "Thu May 25  |
|                       |                       | 22:20:27 +0000 2017", |
|                       |                       |             "         |
|                       |                       | duration_minutes": 60 |
|                       |                       |           }           |
|                       |                       |         ]             |
|                       |                       |       }               |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

### []{#hashtags} Hashtag object []{.tall}

The ` entities ` section will contain a ` hashtags ` array containing an
object for every hashtag included in the Tweet body, and include an
empty array if no hashtags are present.

The PowerTrack ` # ` Operator is used to match on the ` text `
attribute. The ` has:hashtags ` Operator will match if there is at least
one item in the array.

<div>

  --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Field     Type           Description
  indices   Array of Int   An array of integers indicating the offsets within the Tweet text where the hashtag begins and ends. The first integer represents the location of the \# character in the Tweet text string. The second integer represents the location of the first character after the hashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the '#' character). Example:
  text      String         Name of the hashtag, minus the leading '#' character. Example:
  --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

### []{#media} Media object []{.tall}

The ` entities ` section will contain a ` media ` array containing a
single media object if any media object has been 'attached' to the
Tweet. If no native media has been attached, there will be no ` media `
array in the ` entities ` . For the following reasons the
` extended_entities ` section should be used to process Tweet native
media:\
+ Media ` type ` will always indicate 'photo' even in cases of a video
and GIF being attached to Tweet.\
+ Even though up to four photos can be attached, only the first one will
be listed in the ` entities ` section.

The ` has:media ` Operator will match if this array is populated.

<div>

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| display_url           | String                | URL of the media to   |
|                       |                       | display to clients.   |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |   "display_url":"pic. |
|                       |                       | twitter.com/rJC5Pxsu" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| expanded_url          | String                | An expanded version   |
|                       |                       | of display_url. Links |
|                       |                       | to the media display  |
|                       |                       | page. Example:        |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "expanded_url":   |
|                       |                       |  "http://twitter.com/ |
|                       |                       | yunorno/status/114080 |
|                       |                       | 493036773378/photo/1" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| id                    | Int64                 | ID of the media       |
|                       |                       | expressed as a 64-bit |
|                       |                       | integer. Example:     |
+-----------------------+-----------------------+-----------------------+
| id_str                | String                | ID of the media       |
|                       |                       | expressed as a        |
|                       |                       | string. Example:      |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "id_str"          |
|                       |                       | :"114080493040967680" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| indices               | Array of Int          | An array of integers  |
|                       |                       | indicating the        |
|                       |                       | offsets within the    |
|                       |                       | Tweet text where the  |
|                       |                       | URL begins and ends.  |
|                       |                       | The first integer     |
|                       |                       | represents the        |
|                       |                       | location of the first |
|                       |                       | character of the URL  |
|                       |                       | in the Tweet text.    |
|                       |                       | The second integer    |
|                       |                       | represents the        |
|                       |                       | location of the first |
|                       |                       | non-URL character     |
|                       |                       | occurring after the   |
|                       |                       | URL (or the end of    |
|                       |                       | the string if the URL |
|                       |                       | is the last part of   |
|                       |                       | the Tweet text).      |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| media_url             | String                | An                    |
|                       |                       | [http://]{.reference  |
|                       |                       | .external} URL        |
|                       |                       | pointing directly to  |
|                       |                       | the uploaded media    |
|                       |                       | file. Example:        |
|                       |                       |                       |
|                       |                       | ::: {.code .javascri  |
|                       |                       | pt .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |    "media_url":"http: |
|                       |                       | //pbs.twimg.com/media |
|                       |                       | /DOhM30VVwAEpIHq.jpg" |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | For media in direct   |
|                       |                       | messages,             |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[`           |
|                       |                       | media_url `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} is the same |
|                       |                       | https URL as          |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[` media_    |
|                       |                       | url_https `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} and must be |
|                       |                       | accessed by signing a |
|                       |                       | request with the      |
|                       |                       | user's access token   |
|                       |                       | using OAuth 1.0A.     |
|                       |                       |                       |
|                       |                       | It is not possible to |
|                       |                       | access images via an  |
|                       |                       | authenticated         |
|                       |                       | twitter.com session.  |
|                       |                       | Please visit [this    |
|                       |                       | page](/en/do          |
|                       |                       | cs/direct-messages/me |
|                       |                       | ssage-attachments/gui |
|                       |                       | des/retrieving-media) |
|                       |                       | to learn how to       |
|                       |                       | account for these     |
|                       |                       | recent change.        |
|                       |                       |                       |
|                       |                       | You cannot directly   |
|                       |                       | embed these images in |
|                       |                       | a web page.           |
|                       |                       |                       |
|                       |                       | See [Photo Media URL  |
|                       |                       | forma                 |
|                       |                       | tting](#photo_format) |
|                       |                       | for how to format a   |
|                       |                       | photo\'s URL, such as |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[` media_    |
|                       |                       | url_https `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} , based on  |
|                       |                       | the available         |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }[` sizes `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} .           |
+-----------------------+-----------------------+-----------------------+
| media_url_https       | String                | An                    |
|                       |                       | [https://]{.reference |
|                       |                       | .external} URL        |
|                       |                       | pointing directly to  |
|                       |                       | the uploaded media    |
|                       |                       | file, for embedding   |
|                       |                       | on https pages.       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {.code .javascri  |
|                       |                       | pt .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "media_url_https" |
|                       |                       | :"https://p.twimg.com |
|                       |                       | /AZVLmp-CIAAbkyy.jpg" |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | For media in direct   |
|                       |                       | messages,             |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[` media_    |
|                       |                       | url_https `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} must be     |
|                       |                       | accessed by signing a |
|                       |                       | request with the      |
|                       |                       | user's access token   |
|                       |                       | using OAuth 1.0A.     |
|                       |                       |                       |
|                       |                       | It is not possible to |
|                       |                       | access images via an  |
|                       |                       | authenticated         |
|                       |                       | twitter.com session.  |
|                       |                       | Please visit [this    |
|                       |                       | page](/en/do          |
|                       |                       | cs/direct-messages/me |
|                       |                       | ssage-attachments/gui |
|                       |                       | des/retrieving-media) |
|                       |                       | to learn how to       |
|                       |                       | account for these     |
|                       |                       | recent change.        |
|                       |                       |                       |
|                       |                       | You cannot directly   |
|                       |                       | embed these images in |
|                       |                       | a web page.           |
|                       |                       |                       |
|                       |                       | See [Photo Media URL  |
|                       |                       | forma                 |
|                       |                       | tting](#photo_format) |
|                       |                       | for how to format a   |
|                       |                       | photo\'s URL, such as |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[` media_    |
|                       |                       | url_https `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} , based on  |
|                       |                       | the available         |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }[` sizes `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} .           |
+-----------------------+-----------------------+-----------------------+
| sizes                 | [Size                 | An object showing     |
|                       | Obje                  | available sizes for   |
|                       | ct](#size){.reference | the media file.       |
|                       | .external}            | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |       "sizes": {      |
|                       |                       |         "thumb": {    |
|                       |                       |           "h": 150,   |
|                       |                       |                       |
|                       |                       |     "resize": "crop", |
|                       |                       |           "w": 150    |
|                       |                       |         },            |
|                       |                       |         "large": {    |
|                       |                       |           "h": 1366,  |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |           "w": 2048   |
|                       |                       |         },            |
|                       |                       |         "medium": {   |
|                       |                       |           "h": 800,   |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |           "w": 1200   |
|                       |                       |         },            |
|                       |                       |         "small": {    |
|                       |                       |           "h": 454,   |
|                       |                       |                       |
|                       |                       |      "resize": "fit", |
|                       |                       |           "w": 680    |
|                       |                       |         }             |
|                       |                       |       }               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | See [Photo Media URL  |
|                       |                       | forma                 |
|                       |                       | tting](#photo_format) |
|                       |                       | for how to format a   |
|                       |                       | photo\'s URL, such as |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal}[` media_    |
|                       |                       | url_https `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} , based on  |
|                       |                       | the available         |
|                       |                       | ` `{.docutils         |
|                       |                       | .literal              |
|                       |                       | }[` sizes `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} .           |
+-----------------------+-----------------------+-----------------------+
| source_status_id      | Int64                 | Nullable. For Tweets  |
|                       |                       | containing media that |
|                       |                       | was originally        |
|                       |                       | associated with a     |
|                       |                       | different tweet, this |
|                       |                       | ID points to the      |
|                       |                       | original Tweet.       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "source_status_id |
|                       |                       | ": 205282515685081088 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| source_status_id_str  | Int64                 | Nullable. For Tweets  |
|                       |                       | containing media that |
|                       |                       | was originally        |
|                       |                       | associated with a     |
|                       |                       | different tweet, this |
|                       |                       | string-based ID       |
|                       |                       | points to the         |
|                       |                       | original Tweet.       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "s                |
|                       |                       | ource_status_id_str": |
|                       |                       |  "205282515685081088" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| type                  | String                | Type of uploaded      |
|                       |                       | media. Possible types |
|                       |                       | include photo, video, |
|                       |                       | and animated_gif.     |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| url                   | String                | Wrapped URL for the   |
|                       |                       | media link. This      |
|                       |                       | corresponds with the  |
|                       |                       | URL embedded directly |
|                       |                       | into the raw Tweet    |
|                       |                       | text, and the values  |
|                       |                       | for the ` `{.docutils |
|                       |                       | .literal}[            |
|                       |                       | ` indices `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} parameter.  |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "url":"           |
|                       |                       | http://t.co/rJC5Pxsu" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

</div>

### 

### []{#media-size} Media size objects

All Tweets with native media (photos, video, and GIFs) will include a
set of 'thumb', 'small', 'medium', and 'large' sizes with height and
width pixel sizes.  For photos and preview image media URLs, [Photo
Media URL formatting](#photo_format) specifies how to construct
different URLs for loading different sized photo media.

#### Sizes object 

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| thumb                 | [Size Object](#size)  | Information for a     |
|                       |                       | thumbnail-sized       |
|                       |                       | version of the media. |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "                 |
|                       |                       | thumb":{"h":150, "res |
|                       |                       | ize":"crop", "w":150} |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | Thumbnail-sized photo |
|                       |                       | media will be limited |
|                       |                       | to *fill* a 150x150   |
|                       |                       | boundary and cropped. |
+-----------------------+-----------------------+-----------------------+
| large                 | [Size Object](#size)  | Information for a     |
|                       |                       | large-sized version   |
|                       |                       | of the media.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       | "large":{"h":454, "re |
|                       |                       | size":"fit", "w":680} |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | Small-sized photo     |
|                       |                       | media will be limited |
|                       |                       | to *fit* within a     |
|                       |                       | 680x680 boundary.     |
+-----------------------+-----------------------+-----------------------+
| medium                | [Size Object](#size)  | Information for a     |
|                       |                       | medium-sized version  |
|                       |                       | of the media.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "m                |
|                       |                       | edium":{"h":800, "res |
|                       |                       | ize":"fit", "w":1200} |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | Medium-sized photo    |
|                       |                       | media will be limited |
|                       |                       | to *fit* within a     |
|                       |                       | 1200x1200 boundary. \ |
+-----------------------+-----------------------+-----------------------+
| small                 | [Size Object](#size)  | Information for a     |
|                       |                       | small-sized version   |
|                       |                       | of the media.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "s                |
|                       |                       | mall":{"h":1366, "res |
|                       |                       | ize":"fit", "w":2048} |
|                       |                       | :::                   |
|                       |                       | :::                   |
|                       |                       |                       |
|                       |                       | Large-sized photo     |
|                       |                       | media will be limited |
|                       |                       | to *fit* within a     |
|                       |                       | 2048x2048 boundary.\  |
+-----------------------+-----------------------+-----------------------+

#### []{#size} Size object 

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| w                     | Int                   | Width in pixels of    |
|                       |                       | this size. Example:   |
|                       |                       |                       |
|                       |                       | \"w\":150             |
+-----------------------+-----------------------+-----------------------+
| h                     | Int                   | Height in pixels of   |
|                       |                       | this size. Example:   |
|                       |                       |                       |
|                       |                       | \"h\":150             |
+-----------------------+-----------------------+-----------------------+
| resize                | String                | Resizing method used  |
|                       |                       | to obtain this size.  |
|                       |                       | A value of *fit*      |
|                       |                       | means that the media  |
|                       |                       | was resized to fit    |
|                       |                       | one dimension,        |
|                       |                       | keeping its native    |
|                       |                       | aspect ratio. A value |
|                       |                       | of *crop* means that  |
|                       |                       | the media was cropped |
|                       |                       | in order to fit a     |
|                       |                       | specific resolution.  |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | \"resize\":\"crop\"   |
+-----------------------+-----------------------+-----------------------+

### []{#photo_format} Photo Media URL Formatting

Photo media on Twitter can be loaded in different sizes.  It is best to
load the smallest size image that is larger enough to fit into a
particular image viewport.  To load different sizes, the [Size
Object](#size) and [media_url](#media) (or [media_url_https](#media) )
need to be combined in a particular format.  We\'ll use the [media
entity](#entitiesobject) example object already provided for our example
in constructing a photo media URL.

The ` media_url ` or ` media_url_https ` on their own can be loaded,
which will result in the medium variant being loaded by default.  It is
preferable, however, to provide a fully formatted photo media URL when
possible.\

There are three parts of a photo media URL:

+-----------------------------------+-----------------------------------+
| Base URL                          | The base URL is the media URL     |
|                                   | without the file extension.       |
|                                   |                                   |
|                                   | For example:\                     |
|                                   |                                   |
|                                   | [ \"media_url_https\":            |
|                                   | \"https://pbs.twimg               |
|                                   | .com/media/DOhM30VVwAEpIHq.jpg\", |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | The base URL is then:\            |
|                                   |                                   |
|                                   | *https://pbs                      |
|                                   | .twimg.com/media/DOhM30VVwAEpIHq* |
+-----------------------------------+-----------------------------------+
| Format                            | The format is the type of photo   |
|                                   | the image is formatted as.        |
|                                   |  Possible formats are *jpg* or    |
|                                   | *png* , which is provided as the  |
|                                   | extension of the media URL.       |
|                                   |                                   |
|                                   | For example:\                     |
|                                   |                                   |
|                                   | [ \"media_url_https\":            |
|                                   | \"https://pbs.twimg               |
|                                   | .com/media/DOhM30VVwAEpIHq.jpg\", |
|                                   | ]{.code-inline}                   |
|                                   |                                   |
|                                   | The format is then: *jpg*         |
+-----------------------------------+-----------------------------------+
| Name                              | The name is the field name of the |
|                                   | size to load.                     |
|                                   |                                   |
|                                   | For example:                      |
|                                   |                                   |
|                                   | [ ]{.payload}                     |
|                                   |                                   |
|                                   | ::: code-inline                   |
|                                   | { \"sizes\": { \"thumb\": {       |
|                                   | \"h\": 150, \"resize\": \"crop\", |
|                                   | \"w\": 150 }, \"large\": { \"h\": |
|                                   | 1366, \"resize\": \"fit\", \"w\": |
|                                   | 2048 }, \"medium\": { \"h\": 800, |
|                                   | \"resize\": \"fit\", \"w\": 1200  |
|                                   | }, \"small\": { \"h\": 454,       |
|                                   | \"resize\": \"fit\", \"w\": 680 } |
|                                   | }                                 |
|                                   |                                   |
|                                   | }                                 |
|                                   | :::                               |
|                                   |                                   |
|                                   | The name when loading the         |
|                                   | large-sized photo would be:       |
|                                   | *large*                           |
+-----------------------------------+-----------------------------------+

We take these three parts (base URL, format and name) and combine them
into the photo media URL to load.  There are 2 formats for loading
images this way, *legacy* and *modern* .  All image loads should stop
using the *legacy* format and use the *modern* format.  Using the
*modern* format will result in better CDN hit rate for the caller, thus
improving load latencies by being less likely to have to generate and
load the media from the Data Center.

+-----------------------------------+-----------------------------------+
| Legacy format                     | The legacy format is deprecated.  |
|                                   |  Photo media loads should all     |
|                                   | move to the modern format.        |
|                                   |                                   |
|                                   | *\                                |
|                                   | <base_url\>.\<format\>:\<name\>*\ |
|                                   |                                   |
|                                   | For example:\                     |
|                                   |                                   |
|                                   | *https://pbs.twimg.com            |
|                                   | /media/DOhM30VVwAEpIHq.jpg:large\ |
|                                   | *                                 |
+-----------------------------------+-----------------------------------+
| Modern format                     | The modern format for loading     |
|                                   | photos was established at Twitter |
|                                   | in 2015 and has been defacto      |
|                                   | since 2017.  All photo media      |
|                                   | loads should move to this format. |
|                                   |                                   |
|                                   | *\<base_url\>?                    |
|                                   | format=\<format\>&name=\<name\>*\ |
|                                   |                                   |
|                                   | For example:\                     |
|                                   |                                   |
|                                   | *                                 |
|                                   | https://pbs.twimg.com/media/DOhM3 |
|                                   | 0VVwAEpIHq?format=jpg&name=large\ |
|                                   | *                                 |
|                                   |                                   |
|                                   | Note: the items in the query      |
|                                   | string for the photo media URL    |
|                                   | are in alphabetical order.  If    |
|                                   | media loading were to add any     |
|                                   | additional query items,           |
|                                   | alphabetical ordering would       |
|                                   | continue to be necessary.  For    |
|                                   | example, if there was the         |
|                                   | hypothetical new query item       |
|                                   | called *preferred_format* , it    |
|                                   | would go after *format* and       |
|                                   | *name* in the query string.       |
+-----------------------------------+-----------------------------------+

### []{#urls} URL object

The ` entities ` section will contain a ` urls ` array containing an
object for every link included in the Tweet body, and include an empty
array if no links are present.

The ` has:links ` Operator will match if there is at least one item in
the array. The ` url: ` Operator is used to match on the
` expanded_url ` attribute. If you are using the [Expanded URL
enrichment](http://support.gnip.com/enrichments/expanded_urls.html) ,
the ` url: ` Operator is used to match on the ` unwound.url ` (fully
unwound URL) attribute. If you are using the [Exhanced URL
enrichment](http://support.gnip.com/enrichments/enhanced_urls.html) ,
the ` url_title: ` and ` url_decription: ` Operators are used to match
on the ` unwound.title ` and ` unwound.description ` attributes.

<div>

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| display_url           | String                | URL pasted/typed into |
|                       |                       | Tweet. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "display_         |
|                       |                       | url":"bit.ly/2so49n2" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| expanded_url          | String                | Expanded version of   |
|                       |                       | \`\` display_url\`\`  |
|                       |                       | . Example:            |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "expanded_url":"h |
|                       |                       | ttp://bit.ly/2so49n2" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| indices               | Array of Int          | An array of integers  |
|                       |                       | representing offsets  |
|                       |                       | within the Tweet text |
|                       |                       | where the URL begins  |
|                       |                       | and ends. The first   |
|                       |                       | integer represents    |
|                       |                       | the location of the   |
|                       |                       | first character of    |
|                       |                       | the URL in the Tweet  |
|                       |                       | text. The second      |
|                       |                       | integer represents    |
|                       |                       | the location of the   |
|                       |                       | first non-URL         |
|                       |                       | character after the   |
|                       |                       | end of the URL.       |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| url                   | String                | Wrapped URL,          |
|                       |                       | corresponding to the  |
|                       |                       | value embedded        |
|                       |                       | directly into the raw |
|                       |                       | Tweet text, and the   |
|                       |                       | values for the        |
|                       |                       | indices parameter.    |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "url":"htt        |
|                       |                       | ps://t.co/yzocNFvJuL" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

</div>

If you are using the Expanded and/or Enhanced URL enrichments, the
following metadata is available under the ` unwound ` attribute:

<div>

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| url                   | String                | The fully unwound     |
|                       |                       | version of the link   |
|                       |                       | included in the       |
|                       |                       | Tweet. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "url":"https:/    |
|                       |                       | /blog.twitter.com/en_ |
|                       |                       | us/topics/insights/20 |
|                       |                       | 16/using-twitter-as-a |
|                       |                       | -go-to-communication- |
|                       |                       | channel-during-severe |
|                       |                       | -weather-events.html" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| status                | Int                   | Final HTTP status of  |
|                       |                       | the unwinding         |
|                       |                       | process, a \'200\'    |
|                       |                       | indicating success.   |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| title                 | String                | HTML title for the    |
|                       |                       | link. Example:        |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "title":"Using Tw |
|                       |                       | itter as a ‘go-to’ co |
|                       |                       | mmunication channel d |
|                       |                       | uring severe weather" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| description           | String                | HTML description for  |
|                       |                       | the link. Example:    |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "d                |
|                       |                       | escription":"Using Tw |
|                       |                       | itter as a ‘go-to’ co |
|                       |                       | mmunication channel d |
|                       |                       | uring severe weather" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

</div>

### []{#mentions} User mention object []{.tall}

The ` entities ` section will contain a ` user_mentions ` array
containing an object for every user mention included in the Tweet body,
and include an empty array if no user mention is present.

The PowerTrack ` @ ` Operator is used to match on the ` screen_name `
attribute. The ` has:mentions ` Operator will match if there is at least
one item in the array.

<div>

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| id                    | Int64                 | ID of the mentioned   |
|                       |                       | user, as an integer.  |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| id_str                | String                | If of the mentioned   |
|                       |                       | user, as a string.    |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| indices               | Array of Int          | An array of integers  |
|                       |                       | representing the      |
|                       |                       | offsets within the    |
|                       |                       | Tweet text where the  |
|                       |                       | user reference begins |
|                       |                       | and ends. The first   |
|                       |                       | integer represents    |
|                       |                       | the location of the   |
|                       |                       | '@' character of the  |
|                       |                       | user mention. The     |
|                       |                       | second integer        |
|                       |                       | represents the        |
|                       |                       | location of the first |
|                       |                       | non-screenname        |
|                       |                       | character following   |
|                       |                       | the user mention.     |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| name                  | String                | Display name of the   |
|                       |                       | referenced user.      |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| screen_name           | String                | Screen name of the    |
|                       |                       | referenced user.      |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "scre             |
|                       |                       | en_name":"twitterapi" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

</div>

### []{#symbols} Symbol object []{.tall}

The ` entities ` section will contain a ` symbols ` array containing an
object for every \$cashtag included in the Tweet body, and include an
empty array if no symbol is present.

The PowerTrack ` $ ` Operator is used to match on the ` text `
attribute. The ` has:symbols ` Operator will match if there is at least
one item in the array.

<div>

  --------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Field     Type           Description
  indices   Array of Int   An array of integers indicating the offsets within the Tweet text where the symbol/cashtag begins and ends. The first integer represents the location of the \$ character in the Tweet text string. The second integer represents the location of the first character after the cashtag. Therefore the difference between the two numbers will be the length of the hashtag name plus one (for the '\$' character). Example:
  text      String         Name of the cashhtag, minus the leading '\$' character. Example:
  --------- -------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>

### []{#polls} Poll object

The ` entities ` section will contain a ` polls ` array containing a
single ` poll ` object if the Tweet contains a poll. If no poll is
included, there will be no ` polls ` array in the ` entities ` section.

Note that these Poll metadata are only available with the following
Enterprise APIs:

<div>

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| options               | Array of Option       | An array of options,  |
|                       | Object                | each having a poll    |
|                       |                       | position, and the     |
|                       |                       | text for that         |
|                       |                       | position. Example:    |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {"options": [     |
|                       |                       |               {       |
|                       |                       |                       |
|                       |                       |        "position": 1, |
|                       |                       |                       |
|                       |                       |       "text": "I read |
|                       |                       |  documentation once." |
|                       |                       |               }       |
|                       |                       |           ]           |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| end_datetime          | String                | Time stamp (UTC) of   |
|                       |                       | when poll ends.       |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "end_d            |
|                       |                       | atetime": "Thu May 25 |
|                       |                       |  22:20:27 +0000 2017" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| duration_minutes      | String                | Duration of poll in   |
|                       |                       | minutes. Example:     |
+-----------------------+-----------------------+-----------------------+

</div>

## Retweet and Quote Tweet details

From the Twitter API perspective, Retweet and Quote Tweets are special
kinds of Tweets that contain the original Tweet as an embedded object.
So Retweets and Quote Tweet objects are parents of a child \'original\'
Tweet (and thus double the size). Retweets have a top-level
\"retweeted_status\" object, and Quoted Tweets have a \"quoted_status\"
object. For consistency, these top-level Retweet and Quote Tweet objects
also have a text property and associated entities. However, the entities
at the top level can differ from the entities provided by the embedded
\'original\' entities. In case of Retweets, new text is prepended to the
original Tweet body. For Quoted Tweets, new text is appended to the
Tweet body.

In general, the best practice is to retrieve the text, entities,
original author and date from the original Tweet
in retweeted_status whenever this exists. An exception is getting
Twitter entities that are part of the additive Quote. See below for more
details and tips.

### Retweets 

An important detail with Retweets is that no additional Twitter
*entities* can be added to the Tweet. Users can not add hashtags, URLs
or other details when they Retweet. However, the Retweet (top-level)
text attribute is composed of the original Tweet text with "RT
\@username: " prepended.

In some cases, especially with accounts with long user names, the
combination of these new characters and the original Tweet body can
easily exceed the original Tweet text length limit of 140 characters. In
order to preserve support for 140 character based display and storage,
the top-level body truncates the end of the Tweet body and adds an
ellipsis ("..."). Consequently, some top-level entities positioned at
the end of the original Tweet might be incorrect or missing, for
instance in the case of a truncated hashtag or URL entry.

This Tweet,  https://twitter.com/FloodSocial/status/907974220298125312,
has the following Tweet text:

Just another test Tweet that needs to be exactly 140 characters with
trailing URL and hashtag
[http://wapo.st/2w8iwPQ](https://t.co/R5iMzxWelp)
[#Testing](https://twitter.com/hashtag/Testing?src=hash)\

In the above example, both the URL and hashtag were affected. Since the
hashtag was completely truncated and the URL partially truncated, these
are missing from the the top-level entities. You will also notice the
additional user_mentions top-level entity coming from the "RT
\@floodsocial: " prefix on the text field.

However, the Tweet text and entities in retweeted_status perfectly
reflect the original Tweet with no truncation or incorrect entities,
hence our recommendation to rely on the nested *retweeted_status* object
for Retweets.

### Quote Tweets

Quote Tweets were introduced in 2016, and differ from Retweets in that
when you \"quote\" a Tweet you are adding new content \"on top\" of a
shared Tweet. This new content can include nearly anything an original
Tweet can have, including new text, hashtags, mentions, and URLs.

Quote Tweets can contain native media (photos, videos, and GIFs), and
will appear under the entities object.

Since Twitter entities can be added, the Quote entities are likely
different from the original entities.

In this example, a new URL and hashtag were positioned at the end of the
Quote Tweet.

This Tweet, https://twitter.com/FloodSocial/status/907983973225160704,
has the following Tweet text:

strange and equally tragic when islands flood\... trans-atlantic testing
of quote tweets \| [\@thisuser](https://twitter.com/andypiper)
[\@thatuser](https://twitter.com/johnd)
[http://bit.ly/2vMMDuu](https://t.co/fzFgMhWlPO)
[#testing](https://twitter.com/hashtag/testing?src=hash)\

In this case, the top-level entities do not reflect the Quote details.

However, the Tweet text and entities in extended_tweet perfectly reflect
the Quote Tweet with no truncation or incorrect entities, hence our
recommendation to rely on the nested *extended_tweet* object for Quote
Tweets.

## []{#entities-user} Entities for user object

Entities for User Objects describe URLs that appear in the user defined
profile URL and description fields. They do not
describe hashtags or user_mentions. Unlike Tweet entities, user entities
can apply to multiple fields within its parent object --- to
disambiguate, you will find a parent nodes
called url and description that indicate which field contains the
entitized URL.

In this example, the user url field contains a t.co link that is fully
expanded within the entities/url/urls\[0\] node of the response. The
user does not have a wrapped URL in their description.

### JSON example
:::
