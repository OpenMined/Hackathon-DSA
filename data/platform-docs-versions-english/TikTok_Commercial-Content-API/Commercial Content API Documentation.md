Getting Started
===============

This guide will show you how to use the Commercial Content API. Learn how to use the Commercial Content API to query ad data and fetch public advertiser data in the following use case example.

View your client registration
=============================

Once your application is approved, a research client will be generated for your project. You can view your approved research projects [here](https://developers.tiktok.com/research/). Select a project from the list to see the research client details.

The provided **Client key** and **Client secret** are required to connect to the Commercial Content API endpoints. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).

**Note:** The client secret is a credential used to authenticate your connection to TikTok's APIs. Do not share this with anyone!

Obtain a client access token
============================

Once you have obtained the client key and secret for your project, [generate a client access token](https://developers.tiktok.com/doc/client-access-token-management). Add this access token in the authorization header of the http requests to connect to the Commercial Content API endpoints.

Query TikTok public content data
================================

The cURL command below shows an example of how you can query the TikTok ads created in Italy between January 2, 2021 to January 9, 2021 with the keyword "coffee".

    curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group' \
     -H 'authorization: bearer clt.example12345Example12345Example' \
     -d '{ 
             "filters": {
                "ad_published_date_range": {
                     "min": "20221001",
                     "max": "20230510"
                 },
                "country": "IT"
             }, 
            "search_term": "coffee",
            "max_count": 20
        }'
    

Pagination
----------

If the total number of ads that match the search criteria is larger than the maximum number of ads that can be returned in a single request, the response data will be returned with different requests.

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Field** | **Type** | **Description** | **Example** | **Required?** |
| max\_count | number | The maximum count of TikTok videos in the response. The default value is 10 and the maximum value is 50. | 12  | FALSE |
| search\_id | string | The ID of a previous search to provide sequential calls for paging. | "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD" | FALSE |

### First page

When you send the first request, you do not need to set the `search_id` in the request body. In the http response, `has_more` and `search_id` are returned, which are used in the subsequent requests.

    Try out this request:
    
    curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "filters": {
                  "ad_published_date_range": {
                     "min": "20221001",
                     "max": "20230510"
                  },
                  "country": "IT"
               }, 
              "search_term": "coffee",
              "max_count": 20
           }'
    

The following example data is returned from the response.

    {
        "data": {
            "has_more": true,
            "search_id": "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD",
            "ads": [
                ...
            ]
        },
        "error": {
            ...
        }
     }
    

### Next page

With the cURL command below, you can get the next page of query results.

    curl -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad,ad_group' \
      -H 'authorization: bearer clt.example12345Example12345Example' \
      -d '{ 
              "filters": {
                  "ad_published_date_range": {
                     "min": "20221001",
                     "max": "20230510"
                  },
                  "country": "IT"
               }, 
              "search_term": "coffee",
              "max_count": 20,
              "search_id": "eyJsYXN0X3NvcnQiOls3NDA3OCwiMzUwNDIwOTgzOD"
           }'
    

The following example data is returned from the response.

    {
        "data": {
            "has_more": true,
            "search_id": "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI",
            "ads": [
                ...
            ]
        },
        "error": {
            ...
        } 
    }

Query Ads
=========

Use POST /v2/research/adlib/ad/query to query ads.

|     |     |
| --- | --- |
| **HTTP URL** | https://open.tiktokapis.com/v2/research/adlib/ad/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

Request
=======

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | The original media type of the resource. | application/json | true |

Query parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* ad.id<br>* ad.first\_shown\_date<br>* ad.last\_shown\_date<br>* ad.status<br>* ad.status\_statement<br>* ad.videos<br>* ad.image\_urls<br>* ad.reach<br>* advertiser.business\_id<br>* advertiser.business\_name<br>* advertiser.paid\_for\_by | ad.id, ad.first\_shown\_date, ad.last\_shown\_date | true |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | The filters that will be applied to the query. | See the "Request example" section below | true |
| search\_term | string | The terms to search for in the query. The limit of the string is 50 characters or less.<br><br>If you provide "search\_term", the "advertiser\_business\_ids" filter will be ignored | mobile games | false |
| search\_type | string | The search type (which is case insensitive):<br><br>* "exact\_phrase": Returns results that contain an exact match for the search term. The default search type.<br>* "fuzzy\_phrase": Returns results that contain any or all of the words in the search term in any order. | fuzzy\_phrase | false |
| max\_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20  | false |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria.<br><br>If you want to start a new search with an updated`search_term` or `filters` value in the request, remove the `search_id` to avoid getting unexpected results. | 20230501124205358FF99E4D6D1294A2A7 | false |

Data structures
---------------

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_published\_date\_range | DateRange | The date range during which the ads were published.<br><br>The "min" value should represent a date after October 1, 2022. | {<br><br>"min": 20230102,<br><br>"max": 20230109<br><br>} | true |
| country\_code | string | The country where the ads were targeted. The default value is ALL.<br><br>[Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR  | false |
| advertiser\_business\_ids | list<i64> | The advertiser's business ID of the ads.<br><br>If you provide "search\_term", this filter will be ignored. | \[294854736284058, 495736284058473\] | false |
| unique\_users\_seen\_size\_range | SizeRange | The range of the number of users who've seen the content of this ad. | {<br><br>"min": "10K",<br><br>"max": "20K"<br><br>} | false |

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range and this needs to be after October 1, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

### SizeRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The minimum size in thousands (K), millions (M), or billions (B).<br><br>The number before "K", "M", and "B" must be an integer less than 1000. | Valid: 0K, 120K, 2M, 1B<br><br>Invalid: 2000K, 1.1M, 1B2M | false |
| max | string | The maximum size in thousands (K), millions (M), or billions (B)<br><br>The number before "K", "M", and "B" must be an integer less than 1000.<br><br>The value must be greater than 0. | Valid: 120K, 2M, 1B<br><br>Invalid: 0K, 2000K, 1.1M, 1B2M | false |

Request example
---------------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
       "filters":{
           "advertiser_business_ids": [3847236290405, 319282903829],
           "ad_published_date_range": {
                "min": "20210102",
                "max": "20210109"
           },
           "country_code": "FR",
           "unique_users_seen_size_range": {
               "min": "10K",
               "max": "1M"
           },
       },
       "search_term": "mobile games"
    }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryAdData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

Response example
----------------

    {
       "data": {
          "ads": [
             {
                "ad": {
                   "first_shown_date": 20210101,
                   "id": 1923845247192304,
                   "image_urls": [
                      "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf"
                   ],
                   "last_shown_date": 20210101,
                   "status": "active",
                   "videos": [
                      {"url": "https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4"},
                      {"url": "https://asdfcdn.com/..../1kmeidhfb38u21nd82hsk389fd/?mime_type=video_mp4"}
                   ],
                   "reach": {
                      "unique_user_seen": "11K"
                    }
                },
                "advertiser": {
                    "buisness_id": 3847236290405,
                    "business_name": "Awe Food Co.",
                    "paid_by": "Awe Co."
                }
             }
          ],
          "has_more": "true",
          "search_id": "2837438294054038"
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202304280326050102231031430C7E754E",
          "message": ""
       }
    }
    

Data structures
---------------

### QueryAdData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| ads | list<AdDto> | The list of ads that match all the criteria. |     |
| has\_more | bool | The flag that indicates if there are more items to be returned. | true |
| search\_id | string | A unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | 2837438294054038 |

### AdDto

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| ad  | Ad  | The metadata of this ad. |     |
| advertiser | Advertiser | The metadata of the advertiser. |     |

### Ad

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The ad ID. | 1923845247192304 |
| first\_shown\_date | string | The first day when this ad was shown. | 20210101 |
| last\_shown\_date | string | The last day when this ad was shown. | 20210101 |
| status | string | The audit status of this ad: active or inactive. | active |
| videos | list<AdVideo> | The list of videos. |     |
| image\_urls | list<string> | The image URL list of this ad. | \[<br><br>"https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\\u0026x-signature=asdf"<br><br>\] |
| reach | Reach | The number of users who have seen this ad. | {<br><br>"unique\_users\_seen": "11K"<br><br>} |

### AdVideo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| url | string | The video url of this ad | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime\_type=video\_mp4 |

### Reach

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| unique\_users\_seen | string | The number of users who have seen this ad. | "11K" |

### Advertiser

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| business\_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business\_name | string | The advertiser's business name. | Awe Food Co. |
| paid\_by | string | The advertiser's funding source. | Awe Co. |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. |     |
| log\_id | string | The unique ID associated with every request for debugging purporse. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |

Query Advertisers
=================

Use POST /v2/research/adlib/advertiser/query to query advertisers.

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/adlib/advertiser/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

Request
=======

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

Query parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* business\_name<br>* business\_id<br>* country\_code | business\_name,business\_id,country\_code | true |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| search\_term | string | The terms to search for in the query. The limit of the string is 50 characters or less. | awesome | true |
| max\_count | i64 | The maximum number of results returned at once. The default value is 10 and the maximum value is 50. | 20  | false |

Request example
---------------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/advertiser/query/?fields=business_id,business_name' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "search_term": "awesome",
       "max_count": 25
    }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryAdvertiserData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

Response example
----------------

    {
       "data": {
          "advertisers": [
             {
                "business_id": 1755645247067185,
                "business_name": "Awesome Food Co.",
                "country_code": "US",        
             },
             {
                "business_id": 183746395837294,
                "business_name": "Awesome Drink Co.",
                "country_code": "CA",        
             }
          ]
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

Data structures
---------------

### QueryAdvertiserData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| advertisers | list<Advertiser> | The list of advertisers that match all the criteria. |     |

### Advertiser

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| business\_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business\_name | string | The advertiser's business name. | Awesome Food Co. |
| country\_code | string | The advertiser's country in the format of a two-letter code defined in ISO 3166-1. | US  |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. |     |
| log\_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |

Get Ad Details
==============

Use POST /v2/research/adlib/ad/detail/ to get ad details.

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/adlib/ad/detail/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

Request
=======

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

Query parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* ad.id<br>* ad.first\_shown\_date<br>* ad.last\_shown\_date<br>* ad.status<br>* ad.status\_statement<br>* ad.videos<br>* ad.image\_urls<br>* ad.reach<br>* advertiser.business\_id<br>* advertiser.business\_name<br>* advertiser.paid\_for\_by<br>* advertiser.follower\_count<br>* advertiser.avatar\_url<br>* advertiser.profile\_url<br>* ad\_group.targeting\_info | ad.id,ad.first\_shown\_date,ad.last\_shown\_date | true |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_id | i64 | The ad ID. | 104836593772645 | false |

Request example
---------------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/detail/?fields=ad.id,ad.first_shown_date,ad.last_shown_date' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "ad_id": 104836593772645
    }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | AdDetailData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

Response example
----------------

    {
       "data": {
          "ad": {
             "first_shown_date": 20210101,
             "id": 1923845247192304,
             "image_urls": [
                "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf"
             ],
             "last_shown_date": 20210101,
             "status": "active",
             "videos": [
                {"url": "https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime_type=video_mp4"},
                {"url": "https://asdfcdn.com/..../1kmeidhfb38u21nd82hsk389fd/?mime_type=video_mp4"}
             ],
             "reach": {
                "unique_users_seen": "30K",
                "unique_users_seen_by_country": {
                   "GB": "18K",
                   "IT": "12K"
                }
             },
             "rejection_info": {
                 "affected_countries": ["FR", "IT"] 
             }
          },
          "ad_group": {
             "target" {
                "number_of_users_targeted": "50K",
                "country": ["IT", "GB"],
                "age": {
                   "13-17": false,
                   "18-24": false,
                   "25-34": false,
                   "35-44": true,
                   "35-44": true,
                   "55+": true,
                },
                "gender": {
                   "female": true,
                   "male": true,
                   "other_genders": true
                },
                "audience_targeting": "No",
                "video_interactions": "Entertainment",
                "creator_interactions": "Talent",
                "interest": "News & Entertainment, Business Services"
             }
          },
          "advertiser": {
              "business_id": 1755645247067185,
              "business_name": "Awesome Co.",
              "country_code": "US",
              "paid_by": "Awesome Co.",
              "tiktok_account": {
                "avatar_url": "https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600\u0026x-signature=asdf",
                "follower_count": 26374,
                "profile_url": "https://www.tiktok.com/@awesome_co"
              }
          }
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

Data structures
---------------

### GetAdDetailData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| advertiser | Advertiser | The advertiser metadata. |     |
| ad\_group | AdGroup | The ad group metadata. |     |
| ad  | Ad  | The ad metadata. |     |

### Advertiser

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| business\_id | i64 | The advertiser's business ID. | 1755645247067185 |
| business\_name | string | The advertiser's business name. | Awesome Co. |
| country\_code | string | The advertiser's country in the format of a two-letter code defined in ISO 3166-1. | US  |
| paid\_by | string | The advertiser's funding source. | Awesome Co. |
| tiktok\_account | TikTokAccount | The advertiser's TikTok account information. | See example in TikTokAccount table |

### TikTokAccount

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| profile\_url | string | The advertiser's TikTok profile link. | https://www.tiktok.com/@awesome\_co |
| avatar\_url | string | The advertiser's TikTok avatar link. | https://asdf.tiktokcdn.com/1736254.jpeg?x-expires=1679169600&x-signature=asdf |
| follower\_count | i64 | The advertiser's TikTok follower count. | 26374 |

### AdGroup

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| targeting\_info | TargetingInfo | The targeting of this ad group. | See example in Targeted table |

### TargetingInfo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| number\_of\_users\_targeted | string | The total number of users targeted. | "20K" |
| country | list<string> | The targeted countries. | \["FR", "GB"\] |
| age | map<string,bool> | The targeted ages. | {<br><br>"female": true,<br><br>"male": false,<br><br>"unknown": true<br><br>} |
| gender | map<string,bool> | The targeted genders. | {<br><br>"13-17": false,<br><br>"18-24": false,<br><br>"25-34": false,<br><br>"35-44": true,<br><br>"35-44": true,<br><br>"55+": true,<br><br>} |
| audience\_targeting | string | A flag that indicates if the user is part of an audience list uploaded by the advertiser. | "Yes" |
| video\_interactions | string | The list of video categories that the user engaged with | "Entertainment" |
| creator\_interactions | string | The list of creator categories based on how the user followed or viewed creators | "Talent" |
| interest | string | The list of interest categories that the viewers of this ad were grouped into | "News & Entertainment, Business Services" |

### Ad

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The ad ID. | 1923845247192304 |
| first\_shown\_date | string | The first day when this ad was shown. | 20210101 |
| last\_shown\_date | string | The last day when this ad was shown. | 20210101 |
| status | string | The audit status of this ad: active or inactive. | active |
| ad\_videos | list<AdVideo> | The list of videos. |     |
| image\_urls | list<string> | The image URL list of this ad. | \[<br><br>"https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\\u0026x-signature=asdf"<br><br>\] |
| reach | Reach | The audience of this ad group. | See example in Reach table |
| rejection\_info | Rejection\_info |     | See example in RejectionInfo |

### AdVideo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| url | string | The video url of this ad. | https://asdfcdn.com/..../127364jmdfjsa93d8cn30dm2di/?mime\_type=video\_mp4 |

### Reach

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| unique\_users\_seen | string | The total number of unique users who have seen this ad. | 10K |
| unique\_users\_seen\_by\_country | map<string,string> | The total number of unique users who have seen this ad in each country. | {<br><br>"GB": "13K",<br><br>"IT": "12K"<br><br>} |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. |     |
| log\_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |

### RejectionInfo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| reasons | list<string> | The reason that an ad has been rejected, when applicable. | \["The product/service promoted on the ad/landing page belongs to a prohibited industry of the targeted location(s) in your ad when we take our own business evaluation, user experience and the value of advertisement impact, etc. into consideration."\] |
| affected\_countries | list<string> | The affected region(s), if any, where the listed rejection reasons may apply to the ad. If an ad is rejected but no affected regions are specified, it may be rejected in all applicable regions. | \["Austria", "Belgium"\] |
| reporting\_source | string | The reporting or detection source that led to the ad's rejection(s), when applicable. | Users and third parties can report policy violations to us. We have detected this policy violation based on a report that the content violated our Advertising Policies. |
| automated\_notice | string | The notice that describes when TikTok's moderation decision relied on automated measures. This field returns a null value if the decision was based on a manual review. | We have used automated measures in making this decision. |

Get Ad Report
=============

Use POST /v2/research/adlib/ad/report/ to get a report on ad publishing.

|     |     |
| --- | --- |
| **HTTP** **URL** | https://open.tiktokapis.com/v2/research/adlib/ad/report/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

Request
=======

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The token that bears the authorization of the TikTok user, which is obtained through /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | Indicate the original media type of the resource. | application/json | true |

Query parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields:<br><br>* count\_time\_series\_by\_country | count\_time\_series\_by\_country | true |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below. | true |

Data structures
---------------

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| ad\_published\_date\_range | DateRange | The time range when the ads were published.<br><br>"min" needs to be after October 1st, 2022. | {<br><br>"min": "20230102",<br><br>"max": "20230109"<br><br>} | true |
| country\_code | string | The country where the ads/ad groups were created. The default value is ALL.<br><br>[Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries) | FR  | false |
| advertiser\_business\_ids | list<i64> | The advertiser's business ID of the ads/ad groups. | \[21836478203048,3484763562784\] | false |

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range.<br><br>"min" needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

Request example
---------------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/ad/report/?fields=count_time_series_by_country' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json'
    --data-raw '{
       "filters":{
           "ad_published_date_range": {
                "min": "20230102",
                "max": "20230109"
           },
           "country_code":"ALL",
           "advertiser_business_ids":[21836478203048,3484763562784]
       }
    }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | ReportData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

Response example
----------------

    {
       "data": {
          "count_time_series_by_country": {
              "IT": [{"date": "20210109", "count": 45}, {"date": "20210108", "count": 24}],
              "ES": [{"date": "20210109", "count": 48}, {"date": "20210108", "count": 22}],
              ...
        }
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

Data structures
---------------

### ReportData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| count\_time\_series\_by\_country | map<string,list<DateCount>> | The ad count time series of each country. |     |

### DateCount

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| date | string | The date when ads were published in the format YYYYMMDD. | 20230101 |
| count | i64 | The total number of ads published on that date. | 500032 |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. | ""  |
| log\_id | string | The unique ID associated with every request for debugging purposes. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |

Query Commercial Content
========================

Use POST /v2/research/adlib/commercial\_content/query/ to query commercial content

|     |     |
| --- | --- |
| **HTTP URL** | https://open.tiktokapis.com/v2/research/adlib/commercial\_content/query/ |
| **HTTP Method** | POST |
| **Scopes** | research.adlib.basic |

Request
=======

Headers
-------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| Authorization | string | The client access token obtained from /v2/oauth/token/. | Bearer clt.example12345Example12345Example | true |
| Content-Type | string | The original media type of the resource. | application/json | true |

Query parameters
----------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| fields | string | The requested fields<br><br>* id<br>* create\_timestamp<br>* create\_date<br>* label<br>* brand\_names<br>* creator<br>* videos | id,create\_timestamp,brand\_names,creator,videos | true |

Body
----

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| filters | RequestFilters | Filters that will be applied to the query. | See the request example below | true |
| max\_count | i64 | The max number of results returned at once. The default value is 10, and the maximum value is 50. | 20  | false |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria. | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" | false |

Data structures
---------------

### RequestFilters

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| content\_published\_date\_range | DateRange | The time range during which the commercial contents were published.<br><br>"min" needs to be after October 1st, 2022. | {<br><br>"min": 20230102,<br><br>"max": 20230109<br><br>} | true |
| creator\_country\_code | string | The country of the commercial content's author. The default value is ALL.<br><br>Supported countries: European Economic Area (EEA) countries [Supported Countries](https://developers.tiktok.com/doc/commercial-content-api-supported-countries)<br><br>Note: United Kingdom and Switzerland are not included in this API | FR  | false |
| creator\_usernames | list<string> | The commercial contents' creators. | \[<br><br>"joe123",<br><br>"emma\_lol"<br><br>\] | false |

### DateRange

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** | **Required** |
| min | string | The first date of the range and this needs to be after October 1st, 2022. | 20230102 | true |
| max | string | The last date of the range. | 20230109 | true |

Request example
---------------

    curl -L -X POST 'https://open.tiktokapis.com/v2/research/adlib/commercial_content/report/?fields=ad_id,video_urls,business_name' \
    -H 'Authorization: Bearer clt.example12345Example12345Example' \
    -H 'Content-Type: application/json' \
    --data-raw '{
       "filters":{
           "content_published_date_range": {
                "min": "20210102",
                "max": "20210109"
           },
           "creator_country_code": "FR"
       }
     }'
    

Response
========

|     |     |     |
| --- | --- | --- |
| **Key** | **Type** | **Example** |
| data | QueryCommercialContentData | See the response example below. |
| error | ErrorStructV2 | See the response example below. |

Response example
----------------

    {
       "data": {
          "commercial_contents": [
             {
                "brand_names": [
                   "My Awesome Co.",
                   "HelloWorld Inc."
                ],
                "create_date": "20230109",
                "create_timestamp": 1696875852,
                "creator": {
                   "username": "joe1234567"
                },
                "id": "v09044g40000ce6enu3c77u36l73sp20",
                "label": "Paid partnership",
                "videos": [
                   {
                      "cover_image_url": "https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\u0026x-signature=asdf",
                      "url":"https://www.tiktok.com/@joe1234567/video/19384729204821234" 
                   }
                ]
             }
          ],
          "has_more": "true",
          "search_id": "2837438294054038"
       },
       "error": {
          "code": "ok",
          "http_status_code": 200,
          "log_id": "202207280326050102231031430C7E754E",
          "message": ""
       }
    }
    

Data structures
---------------

### QueryCommercialContentData

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| commercial\_contents | list<CommercialContent> | The list of commercial contents. |     |
| has\_more | bool | The flag that indicates if there are more items to be returned. | true |
| search\_id | string | A search\_id is a unique identifier assigned to a cached search result. This identifier enables the resumption of a prior search and retrieval of additional results based on the same search criteria.<br><br>If you update the`filters` in the request, please remove the `search_id` to avoid getting back unexpected results | "eyJsYXN0X3NvcnQiOlsyNTQxMTkwLCIzNDk1NzA4NjI0N" |

### CommercialContent

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The commercial content ID. | 38267490502373 |
| create\_date | string | The create date of the commercial content in format of YYYYMMDD. | 20230109 |
| create\_timestamp | i64 | The create date of the commercial content in format of Unix timestamp. | 1696875852 |
| label | string | The label of this commercial content. | Paid partnership |
| brand\_names | list<string> | The brands that sponsor this commercial content. | \[<br><br>"My Awesome Co.",<br><br>"HelloWorld Inc."<br><br>\] |
| creator | CommercialContentCreator | The commercial content creator's public information. |     |
| video | CommercialContentVideo | The commercial content video's public information. |     |

### CommercialContentCreator

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| username | string | The commercial content creator's TikTok handler. | joe123 |

### CommercialContentVideo

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| id  | i64 | The commercial content video's ID. | 19384729204821234 |
| status | string | The commercial content video's status. | active |
| url | string | The commercial content video's URL. | https://www.tiktok.com/@joe1234567/video/19384729204821234 |
| cover\_image\_url | string | The commercial content video's cover image URL. | https://asdfcdn.com/17392712.jpeg?x-expires=1679169600\\u0026x-signature=asdf |

### ErrorStructV2

|     |     |     |     |
| --- | --- | --- | --- |
| **Key** | **Type** | **Description** | **Example** |
| code | string | The error category in string. | ok  |
| message | string | The detailed error description. |     |
| log\_id | string | The unique id associated with every request for debugging purpose. | 202207280326050102231031430C7E754E |
| http\_status\_code | i32 | The http status code. | 200 |

Supported Countries
===================

European Union (EU)
-------------------

|     |     |
| --- | --- |
| **Country** | **Country Code** |
| Austria | AT  |
| Belgium | BE  |
| Bulgaria | BG  |
| Croatia | HR  |
| Republic of Cyprus | CY  |
| Czech Repub­lic | CZ  |
| Denmark | DK  |
| Estonia | EE  |
| Finland | FI  |
| France | FR  |
| Germany | DE  |
| Greece | GR  |
| Hungary | HU  |
| Ireland | IE  |
| Italy | IT  |
| Latvia | LV  |
| Lithuania | LT  |
| Luxembourg | LU  |
| Malta | MT  |
| Netherlands | NL  |
| Poland | PL  |
| Portugal | PT  |
| Romania | RO  |
| Slovakia | SK  |
| Slovenia | SI  |
| Spain | ES  |
| Sweden | SE  |

European Economic Area (EEA)
----------------------------

Comprised of the European Union (EU) member states and Iceland, Liechtenstein, and Norway

|     |     |
| --- | --- |
| **Country** | **Country Code** |
| Norway | NO  |
| Iceland | IS  |
| Liechtenstein | LI  |

Continental Europe
------------------

The United Kingdom (England, Wales, Scotland, and Northern Ireland) and Switzerland are not in the EU or the EEA but are part of continental Europe.

|     |     |
| --- | --- |
| United Kingdom | GB  |
| Switzerland | CH  |