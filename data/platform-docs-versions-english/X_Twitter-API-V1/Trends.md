Overview

An API to return the [trending topics](https://support.twitter.com/articles/101125) near a specific latitude, longitude location.

GET trends/place

get-trends-place

GET trends/place
================

Returns the top 50 trending topics for a specific `id`, if trending information is available for it.

Note: The `id` parameter for this endpoint is the "where on earth identifier" or WOEID, which is a legacy identifier created by Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html), or [archived data](https://archive.org/details/geoplanet_data_7.10.0.zip0.)

Example WOEID locations include: Worldwide: 1 UK: 23424975 Brazil: 23424768 Germany: 23424829 Mexico: 23424900 Canada: 23424775 United States: 23424977 New York: 2459115

To identify other ids, please use the [GET trends/available](https://developer.twitter.com/en/docs/twitter-api/v1/trends/locations-with-trending-topics/api-reference/get-trends-available) endpoint.

The response is an array of `trend` objects that encode the name of the trending topic, the query parameter that can be used to search for the topic on [Twitter Search](http://search.twitter.com/), and the Twitter Search URL.

The most up to date info available is returned on request. The `created_at` field will show when the oldest trend started trending. The `as_of` field contains the timestamp when the list of trends was created.

The `tweet_volume` for the last 24 hours is also returned for many trends if this is available.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/trends/place.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id  | required | The numeric value that represents the location from where to return trending information for from. Formerly linked to the Yahoo! Where On Earth ID Global information is available by using _1_ as the _WOEID_ . |     | _1_ |
| exclude | optional | Setting this equal to _hashtags_ will remove all hashtags from the trends list. |     |     |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/trends/place.json?id=1`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "trends": [
          {
            "name": "#GiftAGamer",
            "url": "http://twitter.com/search?q=%23GiftAGamer",
            "promoted_content": null,
            "query": "%23GiftAGamer",
            "tweet_volume": null
          },
          {
            "name": "#AskCuppyAnything",
            "url": "http://twitter.com/search?q=%23AskCuppyAnything",
            "promoted_content": null,
            "query": "%23AskCuppyAnything",
            "tweet_volume": 14504
          },
          {
            "name": "#givethanks",
            "url": "http://twitter.com/search?q=%23givethanks",
            "promoted_content": null,
            "query": "%23givethanks",
            "tweet_volume": null
          },
          {
            "name": "Carrefour",
            "url": "http://twitter.com/search?q=Carrefour",
            "promoted_content": null,
            "query": "Carrefour",
            "tweet_volume": 438616
          },
          {
            "name": "#StreamLifeGoesOn",
            "url": "http://twitter.com/search?q=%23StreamLifeGoesOn",
            "promoted_content": null,
            "query": "%23StreamLifeGoesOn",
            "tweet_volume": 179026
          },
          {
            "name": "STREAM BE PARTY",
            "url": "http://twitter.com/search?q=%22STREAM+BE+PARTY%22",
            "promoted_content": null,
            "query": "%22STREAM+BE+PARTY%22",
            "tweet_volume": 71404
          },
          {
            "name": "#TransDayOfRemembrance",
            "url": "http://twitter.com/search?q=%23TransDayOfRemembrance",
            "promoted_content": null,
            "query": "%23TransDayOfRemembrance",
            "tweet_volume": 45852
          },
          {
            "name": "Mourão",
            "url": "http://twitter.com/search?q=Mour%C3%A3o",
            "promoted_content": null,
            "query": "Mour%C3%A3o",
            "tweet_volume": 12614
          },
          {
            "name": "Taysom Hill",
            "url": "http://twitter.com/search?q=%22Taysom+Hill%22",
            "promoted_content": null,
            "query": "%22Taysom+Hill%22",
            "tweet_volume": 20311
          },
          {
            "name": "Geraldo",
            "url": "http://twitter.com/search?q=Geraldo",
            "promoted_content": null,
            "query": "Geraldo",
            "tweet_volume": 30166
          }
        ],
        "as_of": "2020-11-20T19:37:52Z",
        "created_at": "2020-11-19T14:15:43Z",
        "locations": [
          {
            "name": "Worldwide",
            "woeid": 1
          }
        ]
      }
    ]

Overview

Retrieve a full or nearby locations list of trending topics by location.

GET trends/available

get-trends-available

GET trends/available
====================

Returns the locations that Twitter has trending topic information for.

The response is an array of "locations" that encode the location's `WOEID` and some other human-readable information such as a canonical name and country the location belongs in.

Note: This endpoint uses the "where on earth identifier" or WOEID, which is a legacy identifier created by Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html) for more details. The url returned in the response, `where.yahooapis.com` is no longer valid.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/trends/available.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

None

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/trends/available.json`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "country": "Sweden",
        "countryCode": "SE",
        "name": "Sweden",
        "parentid": 1,
        "placeType": {
          "code": 12,
          "name": "Country"
        },
        "url": "http://where.yahooapis.com/v1/place/23424954",
        "woeid": 23424954
      },
      {
        "country": "United States",
        "countryCode": "US",
        "name": "New Haven",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2458410",
        "woeid": 2458410
      },
      {
        "country": "Japan",
        "countryCode": "JP",
        "name": "Sapporo",
        "parentid": 23424856,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/1118108",
        "woeid": 1118108
      },
      ...
      {
        "country": "United States",
        "countryCode": "US",
        "name": "Providence",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2477058",
        "woeid": 2477058
      },
      {
        "country": "United States",
        "countryCode": "US",
        "name": "Cincinnati",
        "parentid": 23424977,
        "placeType": {
          "code": 7,
          "name": "Town"
        },
        "url": "http://where.yahooapis.com/v1/place/2380358",
        "woeid": 2380358
      }
    ]

GET trends/closest

get-trends-closest

GET trends/closest
==================

Returns the locations that Twitter has trending topic information for, closest to a specified location.

The response is an array of "locations" that encode the location's `WOEID` and some other human-readable information such as a canonical name and country the location belongs in.

Note: The "where on earth identifier" or WOEID, is a legacy identifier created by Yahoo and has been deprecated. Twitter API v1.1 still uses the numeric value to identify town and country trend locations. Reference our legacy [blog post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html), or [archived data](https://archive.org/details/geoplanet_data_7.10.0.zip0.). The url returned in the response, `where.yahooapis.com` is no longer valid.

Resource URL[¶](#resource-url "Permalink to this headline")
-----------------------------------------------------------

`https://api.twitter.com/1.1/trends/closest.json`

Resource Information[¶](#resource-information "Permalink to this headline")
---------------------------------------------------------------------------

|     |     |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 75  |
| Requests / 15-min window (app auth) | 75  |

Parameters[¶](#parameters "Permalink to this headline")
-------------------------------------------------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| lat | required | If provided with a _long_ parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive. |     | _37.781157_ |
| long | required | If provided with a _lat_ parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive. |     | _\-122.400612831116_ |

Example Request[¶](#example-request "Permalink to this headline")
-----------------------------------------------------------------

`GET https://api.twitter.com/1.1/trends/closest.json?lat=37.781157&long=-122.400612831116`

Example Response[¶](#example-response "Permalink to this headline")
-------------------------------------------------------------------

    [
      {
        "country": "Australia",
        "countryCode": "AU",
        "name": "Australia",
        "parentid": 1,
        "placeType": {
          "code": 12,
          "name": "Country"
        },
        "url": "http://where.yahooapis.com/v1/place/23424748",
        "woeid": 23424748
      }
    ]