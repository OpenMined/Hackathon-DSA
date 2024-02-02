<div>

::: c01-rich-text-editor
Returns the locations that Twitter has trending topic information for,
closest to a specified location.

The response is an array of \"locations\" that encode the location\'s
` WOEID ` and some other human-readable information such as a canonical
name and country the location belongs in.

Note: The \"where on earth identifier\" or WOEID, is a legacy identifier
created by Yahoo and has been deprecated. Twitter API v1.1 still uses
the numeric value to identify town and country trend locations.
Reference our legacy [blog
post](https://blog.twitter.com/engineering/en_us/a/2010/woeids-in-twitters-trends.html)
, or [archived
data](https://archive.org/details/geoplanet_data_7.10.0.zip0.) . The url
returned in the response, ` where.yahooapis.com ` is no longer valid.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/trends/closest.json `

  -------------------------------------- ------
  Response formats                       JSON
  Requires authentication?               Yes
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   75
  Requests / 15-min window (app auth)    75
  -------------------------------------- ------

## Parameters [¶](#parameters){.headerlink}

  ------ ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------- ---------------------
  Name   Required   Description                                                                                                                                                                                                                                      Default Value   Example
  lat    required   If provided with a *long* parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.                   *37.781157*
  long   required   If provided with a *lat* parameter the available trend locations will be sorted by distance, nearest to furthest, to the co-ordinate pair. The valid ranges for longitude is -180.0 to +180.0 (West is negative, East is positive) inclusive.                    *-122.400612831116*
  ------ ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------- ---------------------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/trends/closest.json?lat=37.781157&long=-122.400612831116 `

## Example Response [¶](#example-response){.headerlink}

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
:::

</div>
