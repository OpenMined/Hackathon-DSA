<div>

::: c01-rich-text-editor
Returns the locations that Twitter has trending topic information for.

The response is an array of \"locations\" that encode the location\'s
` WOEID ` and some other human-readable information such as a canonical
name and country the location belongs in.

Note: This endpoint uses the \"where on earth identifier\" or WOEID,
which is a legacy identifier created by Yahoo and has been deprecated.
Twitter API v1.1 still uses the numeric value to identify town and
country trend locations. Reference our legacy [blog
post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html)
for more details. The url returned in the response,
` where.yahooapis.com ` is no longer valid.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/trends/available.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  Requests / 15-min window (app auth)    75
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

None

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/trends/available.json `

## Example Response [¶](#example-response){.headerlink}

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
:::

</div>
