<div>

::: c01-rich-text-editor
Returns settings (including current trend, geo and sleep time
information) for the authenticating user.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account/settings.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

None

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/account/settings.json `

## Example Response [¶](#example-response){.headerlink}

    {
        "always_use_https": true,
        "discoverable_by_email": true,
        "geo_enabled": true,
        "language": "en",
        "protected": false,
        "screen_name": "theSeanCook",
        "show_all_inline_media": false,
        "sleep_time": {
            "enabled": false,
            "end_time": null,
            "start_time": null
        },
        "time_zone": {
            "name": "Pacific Time (US & Canada)",
            "tzinfo_name": "America/Los_Angeles",
            "utc_offset": -28800
        },
        "trend_location": [
            {
                "country": "United States",
                "countryCode": "US",
                "name": "Atlanta",
                "parentid": 23424977,
                "placeType": {
                    "code": 7,
                    "name": "Town"
                },
                "url": "http://where.yahooapis.com/v1/place/2357024",
                "woeid": 2357024
            }
        ],
        "use_cookie_personalization": true,
        "allow_contributor_request": "all"
    }
:::

</div>
