Query Videos
============

Request
=======

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/video/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.data.basic (**required**) |

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Content-Type | string | Indicate the original media type of the resource. | "application/json" | Yes |
| Authorization | string | The client access token which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | Yes |

Query Parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields. Choose from the Video Object's fields. | Complete list:<br><br>id,video\_description,create\_time, region\_code,share\_count,view\_count,like\_count,comment\_count, music\_id,hashtag\_names, username,effect\_ids,playlist\_id,voice\_to\_text | Yes |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| query | Query object<br><br>(See the definition below) | A JSON object that contains three types of children: `and`, `or`, and `not`, each of which is a list of conditions. An valid query must contain at least one non-empty `and`, `or` or `not` condition lists | {<br>      "and":[<br>        {<br>          "operation":"IN",<br>          "field_name":"region_code",<br>          "field_values":[<br>            "JP",<br>            "US"<br>          ]<br>        },<br>        {<br>          "operation":"EQ",<br>          "field_name":"keyword",<br>          "field_values":[<br>            "animal"<br>          ]<br>        }<br>      ],<br>      "not":[<br>        {<br>          "operation":"LT",<br>          "field_name":"create_date",<br>          "field_values":[<br>            "20230101"<br>          ]<br>        }<br>      ]<br>    } | Yes |
| start\_date | string | The lower bound of video creation time in UTC | "20210102" | Yes |
| end\_date | string | The upper bound of video creation time in UTC<br><br>The end\_date must be no more than 30 days after the start\_date | "20210123" | Yes |
| max\_count | int64 | The number of videos in response. Default is 20, max is 100.<br><br>It is possible that the API returns less videos than the max count due to reasons such as videos deleted/marked as private by users etc. | 20  | No  |
| cursor | int64 | Retrieve video results starting from the specified index | 100 | No  |
| search\_id | string | The unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "7201388525814961198" | No  |
| is\_random | bool | The flag that indicates whether to return results in a random order.<br><br>If set to true, then the API returns 1 - 100 videos in random order that matches the query.<br><br>If set to false or not set with any value, then the API returns results in the decreasing order of video IDs. | true | No  |

##### Query

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Required** |
| and | list<Condition> | The `and` conditions specify that all the conditions in the list must be met | No  |
| or  | list<Condition> | The `or` conditions specify that at least one of the conditions in the list must be met | No  |
| not | list<Condition> | The `not` conditions specify that none of the conditions in the list must be met | No  |

##### Condition

|     |     |     |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| field\_name | string | The name of the field this condition is restricting<br><br>One of: \["create\_date", "username", "region\_code", "video\_id", "hashtag\_name", "keyword", "music\_id", "effect\_id", "video\_length"\] |
| operation | string | One of: "EQ", "IN", "GT", "GTE", "LT", "LTE" |
| field\_values | list<string> | A list of restriction values |

##### Condition fields

|     |     |     |
| --- | --- | --- |
| **Field Name** | **Description** | **Example** |
| create\_date | The video creation date in UTC, presented in the format YYYYMMDD | 20220910 |
| username | The username of the video creator | "cookie\_love\_122" |
| region\_code | The abbreviated name of the country where the video was created | 'FR', 'TH', 'MM', 'BD', 'IT', 'NP', 'IQ', 'BR', 'US', 'KW', 'VN', 'AR', 'KZ', 'GB', 'UA', 'TR', 'ID', 'PK', 'NG', 'KH', 'PH', 'EG', 'QA', 'MY', 'ES', 'JO', 'MA', 'SA', 'TW', 'AF', 'EC', 'MX', 'BW', 'JP', 'LT', 'TN', 'RO', 'LY', 'IL', 'DZ', 'CG', 'GH', 'DE', 'BJ', 'SN', 'SK', 'BY', 'NL', 'LA', 'BE', 'DO', 'TZ', 'LK', 'NI', 'LB', 'IE', 'RS', 'HU', 'PT', 'GP', 'CM', 'HN', 'FI', 'GA', 'BN', 'SG', 'BO', 'GM', 'BG', 'SD', 'TT', 'OM', 'FO', 'MZ', 'ML', 'UG', 'RE', 'PY', 'GT', 'CI', 'SR', 'AO', 'AZ', 'LR', 'CD', 'HR', 'SV', 'MV', 'GY', 'BH', 'TG', 'SL', 'MK', 'KE', 'MT', 'MG', 'MR', 'PA', 'IS', 'LU', 'HT', 'TM', 'ZM', 'CR', 'NO', 'AL', 'ET', 'GW', 'AU', 'KR', 'UY', 'JM', 'DK', 'AE', 'MD', 'SE', 'MU', 'SO', 'CO', 'AT', 'GR', 'UZ', 'CL', 'GE', 'PL', 'CA', 'CZ', 'ZA', 'AI', 'VE', 'KG', 'PE', 'CH', 'LV', 'PR', 'NZ', 'TL', 'BT', 'MN', 'FJ', 'SZ', 'VU', 'BF', 'TJ', 'BA', 'AM', 'TD', 'SI', 'CY', 'MW', 'EE', 'XK', 'ME', 'KY', 'YE', 'LS', 'ZW', 'MC', 'GN', 'BS', 'PF', 'NA', 'VI', 'BB', 'BZ', 'CW', 'PS', 'FM', 'PG', 'BI', 'AD', 'TV', 'GL', 'KM', 'AW', 'TC', 'CV', 'MO', 'VC', 'NE', 'WS', 'MP', 'DJ', 'RW', 'AG', 'GI', 'GQ', 'AS', 'AX', 'TO', 'KN', 'LC', 'NC', 'LI', 'SS', 'IR', 'SY', 'IM', 'SC', 'VG', 'SB', 'DM', 'KI', 'UM', 'SX', 'GD', 'MH', 'BQ', 'YT', 'ST', 'CF', 'BM', 'SM', 'PW', 'GU', 'HK', 'IN', 'CK', 'AQ', 'WF', 'JE', 'MQ', 'CN', 'GF', 'MS', 'GG', 'TK', 'FK', 'PM', 'NU', 'MF', 'ER', 'NF', 'VA', 'IO', 'SH', 'BL', 'CU', 'NR', 'TP', 'BV', 'EH', 'PN', 'TF', 'RU' |
| video\_id | The unique identifier of the video | 6978662169214864645 |
| hashtag\_name | The hashtag associated with the video | "arianagrande", "celebrity" |
| keyword | The keyword in the video description | "tiktok" |
| music\_id | The music ID of the video. | 8978345345214861235 |
| effect\_id | The effect ID of the video. | 3957392342148643476 |
| video\_length | The duration of the video<br><br>SHORT: <15s<br><br>MID: 15 ~60s<br><br>LONG: 1~5min<br><br>EXTRA\_LONG: >5min | "SHORT", "MID", "LONG", "EXTRA\_LONG" |

Example
-------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description,create_time' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
        "query": {
            "and": [
                {
                    "operation": "IN",
                    "field_name": "region_code",
                    "field_values": ["JP", "US"]
                },
                {
                    "operation":"EQ",
                    "field_name":"hashtag_name",
                    "field_values":["animal"]
                }
            ],
            "not": [
              {
                    "operation": "EQ",
                    "field_name": "video_length",
                    "field_values": ["SHORT"]
               }
            ]
        },
        "max_count": 100,
        "cursor": 0,
        "start_date": "20230101",
        "end_date": "20230115"
    }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryVideoResponseData | {<br><br>"videos": \[...\],<br><br>"cursor": 100,<br><br>"has\_more": true,<br><br>"search\_id": ""<br><br>} |
| error | ErrorStruct | Error object |

Data Structures
---------------

### QueryVideoResponseData

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| videos | list<Video Object> | A list of video objects that match the query |
| cursor | int64 | Returns video results from the given index. |
| has\_more | bool | Whether there are more videos or not. |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. |

##### Video Object

|     |     |     |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| "id" | int64 | Unique identifier for the TikTok video. Also called "item\_id" or "video\_id" |
| "create\_time" | int64 | UTC Unix epoch (in seconds) of when the TikTok video was posted. (Inherited field from TNS research API) |
| "username" | string | The video's author's username |
| "region\_code" | string | A two digit code for the country the video was posted in |
| "video\_description" | string | The description of the video, also known as the title |
| "music\_id" | int64 | The music\_id used in the video |
| "like\_count" | int64 | The number of likes the video has received. |
| "comment\_count" | int64 | The number of comments the video has received. |
| "share\_count" | int64 | The number of shares the video has received. |
| "view\_count" | int64 | The number of video views the video has received. |
| "effect\_ids" | list<string> | The list of effect ids applied on the video |
| "hashtag\_names" | list<string> | The list of hashtag names that the video participates in |
| "playlist\_id" | int64 | The ID of playlist that the video belongs to |
| "voice\_to\_text" | string | Voice to text and subtitles (for videos that have voice to text features on, show the texts already generated) |

Example
-------

    {
        "data": {
            "videos": [
                {
                    "hashtag_names": [
                        "avengers",
                        "pov"
                    ],
                    "region_code": "CA",
                    "create_time": 1633823999,
                    "effect_ids": [
                        "0"
                    ],
                    "video_id": 702874395068494965,
                    "music_id": 703847506349838790,
                    "video_description": "lol #pov #avengers",
                    "view_count": 1050,
                    "comment_count": 2
                },
                ...
            ],
            "cursor": 100,
            "search_id": "7201388525814961198",
            "has_more": true
        },
        "error": {
            "code": "ok",
            "message": "",
            "log_id": "20230113024658F0D7C5D6CA3A9B79C5B9"
        }
    }