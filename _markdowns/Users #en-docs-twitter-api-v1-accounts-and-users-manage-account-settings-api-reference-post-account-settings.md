<div>

::: c01-rich-text-editor
Updates the authenticating user\'s settings.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account/settings.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ---------------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------
  Name                   Required   Description                                                                                                                                                                                                                                                                                            Example
  sleep_time_enabled     optional   When set to *true* , *t* or *1* , will enable sleep time for the user. Sleep time is the time when push or SMS notifications should not be sent to the user.                                                                                                                                           *true*
  start_sleep_time       optional   The hour that sleep time should begin if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user\'s *time_zone* setting.                                *13*
  end_sleep_time         optional   The hour that sleep time should end if it is enabled. The value for this parameter should be provided in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) format (i.e. 00-23). The time is considered to be in the same timezone as the user\'s *time_zone* setting.                                  *13*
  time_zone              optional   The timezone dates and times should be displayed in for the user. The timezone must be one of the [Rails TimeZone](http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html) names.                                                                                                              *Europe/Copenhagen* *Pacific/Tongatapu*
  trend_location_woeid   optional   The Yahoo! Where On Earth ID to use as the user\'s default trend location. Global information is available by using 1 as the WOEID. The WOEID must be one of the locations returned by [GET trends/available](/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available) .     *1*
  lang                   optional   The language which Twitter should render in for this user. The language must be specified by the appropriate two letter ISO 639-1 representation. Currently supported languages are provided by [this endpoint](/en/docs/developer-utilities/supported-languages/api-reference/get-help-languages) .   *it* *en* *es*
  ---------------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/account/settings.json?lang=en `

## Example Response [¶](#example-response){.headerlink}

    {
      "sleep_time": {
        "end_time": null,
        "enabled": false,
        "start_time": null
      },
      "use_cookie_personalization": true,
      "trend_location": [
        {
          "name": "San Francisco",
          "placeType": {
            "name": "Town",
            "code": 7
          },
          "woeid": 2487956,
          "country": "United States",
          "url": "http://where.yahooapis.com/v1/place/2487956",
          "countryCode": "US",
          "parentid": 23424977
        }
      ],
      "language": "en",
      "discoverable_by_email": true,
      "always_use_https": true,
      "protected": false,
      "geo_enabled": true,
      "show_all_inline_media": false,
      "screen_name": "oauth_dancer"
    }
:::

</div>
