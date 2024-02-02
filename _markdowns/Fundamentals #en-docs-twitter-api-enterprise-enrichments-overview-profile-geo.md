::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Many Twitter user profiles include public location information provided
by the user. This data is returned as a normal string in user.location
(see [User object data
dictionary](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-object/user.html)
). The Profile Geo Enrichment adds structured geodata relevant to the
user.location value by geocoding and normalizing location strings where
possible. Both latitude/longitude coordinates and related place metadata
are added to user.derived.locations *only* when included as part of the
Tweet payload in enterprise API products. This data is available when
using [the enriched native
format](/en/docs/twitter-api/enterprise/data-dictionary/overview.html)
and can be filtered with a combination of [PowerTrack
rules](/en/docs/twitter-api/enterprise/rules-and-filtering/enterprise-operators)
.\

**Note:** Some of the supporting geodata used to create the Profile Geo
enrichment comes from GeoNames.org and is used by Twitter under the
[Creative Commons Attribution 3.0
License](https://creativecommons.org/licenses/by/3.0/us/legalcode) .

Profile Geo data will be included in Twitter\'s PowerTrack, Replay,
Volume Stream, Search, and Historical PowerTrack APIs.

### Profile Geo Data

  ------------------------------------- ------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Enriched native field name            Example value                        Description
  user.derived.locations.country        United States                        The country location for where the user that created the Tweet is from.
  user.derived.locations.country_code   US                                   A two-letter ISO-3166 country code that corresponds to the country location for where the user that created the Tweet is from.
  user.derived.locations.locality       Birmingham                           The locality location (generally city) for where the user that created the Tweet is from.
  user.derived.locations.region         Alabama                              The region location (generally state/province) for where the user that created the Tweet is from.
  user.derived.locations.sub_region     Jefferson County                     The sub-region location (generally county) for where the user that created the Tweet is from.
  user.derived.locations.full_name      Birmingham, Alabama, United States   The full name (excluding sub-region) for where the user that created the Tweet is from.
  User.derived.locations.geo            See Below                            An array that includes a lat/long value for a coordinate that corresponds to the lowers granularity location for where the user that created the Tweet is from.
  ------------------------------------- ------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------

The Historical PowerTrack, Search, and PowerTrack APIs supports
filtering based on Profile Geo data. See the appropriate product
documentation for more details on what operators are available for
filtering on Profile Geo data.

### Sample Payload

    {
        "user": {
            "derived": {
                "locations": [
                    {
                        "country": "United States",
                        "country_code": "US",
                        "locality": "Birmingham",
                        "region": "Alabama",
                        "sub_region": "Jefferson County",
                        "full_name": "Birmingham, Alabama, United States",
                        "geo": {
                            "coordinates": [
                                -86.80249,
                                33.52066
                            ],
                            "type": "point"
                        }
                    }
                ]
            }
        }
    }

### Limitations

-   The Profile Geo enrichment attempts to determine the best choice for
    the geographic place described in the profile location string. The
    result may not be accurate in all cases due to factors such as
    multiple places with similar names or ambiguous names.
-   If a value is not provided in a user's profile location field
    (actor.location), we will not attempt to make a classification.
-   Precision Level: If a Profile Geo Enrichment can only be determined
    with confidence at the country or region level, lower-level
    geographies such as subRegion and locality will be omitted from the
    payload.
-   The Profile Geo enrichment provides lat/long coordinates (a single
    point) that corresponds to the Precision Level of the enrichment's
    results. These coordinates represent the geographic center of the
    enrichment location results. For example, if the Precision Level is
    at the Country level, then those coordinates are set to the
    geographic center of that Country.
-   The PowerTrack operators provided for address properties
    (locality/region/country/country code) are intentionally granular to
    allow for many rule combinations. When attempting to target a
    specific location that shares a name with another location, consider
    combining address rules. For instance, the following would avoid
    matches for "San Francisco, Philippines": profile_locality:"San
    Francisco" profile_region:California When building rules that target
    individual Profile Geo fields, keep in mind that each increased
    level of granularity will limit the results you see. In some cases
    when attempting to look at data from a city, you may wish to only
    rely on a region rule where the region offers significant overlap
    with the city, e.g. the city of Zurich, Switzerland can be
    effectively targeted along with surrounding areas with
    profile_region:"Zurich".
-   Use with Native Geo Tweets: The Profile Geo enrichment provides an
    alternative type of geography for a Tweet, different from the native
    geo value in the payload. These two types of geography can be
    combined together to capture all of the possible tweets related to a
    given area (based on available geodata), though they are not
    conceptually equivalent.
:::
:::
:::
:::
:::
:::
:::
:::
