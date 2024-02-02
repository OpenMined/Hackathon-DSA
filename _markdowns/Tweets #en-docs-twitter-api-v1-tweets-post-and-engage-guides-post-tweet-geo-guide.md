::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
#### **Geo-Tagging**

-   Tweets can be created with geo data using the POST statuses/update
    method.
-   Any geo-tagging parameters in an API statuses/update will be ignored
    if geo_enabled for the user is false (this is the default setting
    for all users, unless the user has enabled geolocation in their
    settings).
-   The number of digits after the decimal separator passed to lat (up
    to 8) is tracked so that when the lat is returned in a status object
    it will have the same number of digits after the decimal separator.
-   Use a decimal point as the separator (and not a decimal comma) for
    the latitude and the longitude - usage of a decimal comma will cause
    the geo-tagged portion of the status update to be dropped.

#### **Geo Point** 

-   For JSON, the response mostly uses conventions described in
    [GeoJSON](http://geojson.org/) . However, the geo object coordinates
    that Twitter renders are **reversed** from the GeoJSON
    specification. GeoJSON specifies a longitude then a latitude,
    whereas Twitter represents it as a latitude then a
    longitude: \"geo\": { \"type\":\"Point\", \"coordinates\":\[37.78217, -122.40062\] }
-   The coordinates object is replacing the geo object (no deprecation
    date has been set for the geo object yet) -- the difference is that
    the coordinates object, in JSON, is now rendered correctly in
    GeoJSON.

#### **Place ID**

-   If a place_id is passed into the status update, then that place will
    be attached to the status. If no place_id was explicitly provided,
    but latitude and longitude are, the API attempts to implicitly
    provide a place by calling
    [geo/reverse_geocode](/en/docs/geo/places-near-location/api-reference/get-geo-reverse_geocode.html)
    .

#### **Geo compliance**

-   Users have the ability to remove all geotags from all their Tweets
    en masse via the user settings page. Currently there is no API
    method to remove geotags from individual Tweets.
-   The scrub_geo compliance object will be sent through the Compliance
    Firehose for the specific User\'s Tweets.
:::
:::
:::
:::
:::
:::
:::
