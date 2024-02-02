::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Location obejcts can exist within the actor obejct set on the Twitter
account level or within the profileLocations object of the [gnip
object](/en/docs/twitter-api/enterprise/data-dictionary/activity-streams-objects/gnip.html)
. Location objects have a place object type and can have a name,
address, or geo coordinates. Location objects are similar to
[Geo](/en/docs/twitter-api/enterprise/data-dictionary/native-enriched-objects/geo.html)
in native enriched format.

### []{#place-dictionary} Location data dictionary

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| objectType            | string                | See                   |
|                       |                       | [here](http://activit |
|                       |                       | ystrea.ms/head/activi |
|                       |                       | ty-schema.html#place) |
|                       |                       | for more detailed     |
|                       |                       | information. Example: |
+-----------------------+-----------------------+-----------------------+
| displayName           | string                | **The full name of    |
|                       |                       | the location.** [     |
|                       |                       | **\"displayName\":**  |
|                       |                       | \"United States\"     |
|                       |                       | ]{.code-inline}       |
+-----------------------+-----------------------+-----------------------+
| name                  | string                | Name of the location  |
|                       |                       | from Twitter\'s place |
|                       |                       | JSON format.          |
+-----------------------+-----------------------+-----------------------+
| link                  | string                | A link to the full    |
|                       |                       | Twitter JSON          |
|                       |                       | representation of the |
|                       |                       | place.                |
|                       |                       |                       |
|                       |                       | **\"link\":**         |
|                       |                       | \"https://api.twit    |
|                       |                       | ter.com/1.1/geo/id/27 |
|                       |                       | c45d804c777999.json\" |
+-----------------------+-----------------------+-----------------------+
| geo                   | object                | The geo coordintates  |
|                       |                       | object from Twitter.  |
|                       |                       | Either a polygon, or  |
|                       |                       | point.                |
|                       |                       |                       |
|                       |                       | See                   |
|                       |                       | [geo](/en/docs/tw     |
|                       |                       | itter-api/v1/data-dic |
|                       |                       | tionary/object-model/ |
|                       |                       | geo.html#coordinates) |
+-----------------------+-----------------------+-----------------------+
| countryCode           | String                | Shortened country     |
|                       |                       | code representing the |
|                       |                       | country containing    |
|                       |                       | this place. Example:  |
+-----------------------+-----------------------+-----------------------+
| country               | String                | Name of the country   |
|                       |                       | containing this       |
|                       |                       | place. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "coun             |
|                       |                       | try": "United States" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

#### 

##  profileLocations derived obejcts

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| address               | object                | Within                |
|                       |                       | profileLocation       |
|                       |                       | location object       |
|                       |                       | within the [gnip      |
|                       |                       | object]               |
|                       |                       | (/en/docs/twitter-api |
|                       |                       | /enterprise/data-dict |
|                       |                       | ionary/activity-strea |
|                       |                       | ms-objects/gnip.html) |
|                       |                       | .  Address of         |
|                       |                       | location derived by   |
|                       |                       | the [profile geo      |
|                       |                       | enrichement](/en/doc  |
|                       |                       | s/twitter-api/enterpr |
|                       |                       | ise/enrichments/overv |
|                       |                       | iew/profile-geo.html) |
|                       |                       | .  Level of           |
|                       |                       | granularity will      |
|                       |                       | vary.                 |
|                       |                       |                       |
|                       |                       | **\"address\": {**    |
|                       |                       |                       |
|                       |                       | **\"country\":**      |
|                       |                       | \"United States\"     |
|                       |                       | **,**                 |
|                       |                       |                       |
|                       |                       | **\"countryCode\":**  |
|                       |                       | \"US\" **,**          |
|                       |                       |                       |
|                       |                       | **\"locality\":**     |
|                       |                       | \"Providence\" **,**  |
|                       |                       |                       |
|                       |                       | **\"region\":**       |
|                       |                       | \"Rhode Island\"      |
|                       |                       | **,**                 |
|                       |                       |                       |
|                       |                       | **\"subRegion\":**    |
|                       |                       | \"Providence County\" |
|                       |                       |                       |
|                       |                       | **}**                 |
+-----------------------+-----------------------+-----------------------+
| geo                   | object                | Within                |
|                       |                       | profileLocation       |
|                       |                       | location object       |
|                       |                       | within the [gnip      |
|                       |                       | objec]                |
|                       |                       | (/en/docs/twitter-api |
|                       |                       | /enterprise/data-dict |
|                       |                       | ionary/activity-strea |
|                       |                       | ms-objects/gnip.html) |
|                       |                       | t. Centroid           |
|                       |                       | coordinates of the    |
|                       |                       | location derived by   |
|                       |                       | the [profile geo      |
|                       |                       | enrichement](/en/doc  |
|                       |                       | s/twitter-api/enterpr |
|                       |                       | ise/enrichments/overv |
|                       |                       | iew/profile-geo.html) |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | **\"geo\": {**        |
|                       |                       |                       |
|                       |                       | **\"coordinates\":    |
|                       |                       | \[**                  |
|                       |                       |                       |
|                       |                       | -98.5 **,**           |
|                       |                       |                       |
|                       |                       | 39.76                 |
|                       |                       |                       |
|                       |                       | **\],**               |
|                       |                       |                       |
|                       |                       | **\"type\":**         |
|                       |                       | \"point\"             |
|                       |                       |                       |
|                       |                       | **}**                 |
+-----------------------+-----------------------+-----------------------+

## 

## []{#location-examples} Examples
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 "location": {
    "objectType": "place",
    "displayName": "Kansas, USA",
    "name": "Kansas",
    "country_code": "United States",
    "twitter_country_code": "US",
    "twitter_place_type": "admin",
    "link": "https://api.twitter.com/1.1/geo/id/27c45d804c777999.json",
    "geo": {
      "type": "Polygon",
      "coordinates": [
        [
          [
            -102.051769,
            36.99311
          ],
          [
            -102.051769,
            40.003282
          ],
          [
            -94.588081,
            40.003282
          ],
          [
            -94.588081,
            36.99311
          ]
        ]
      ]
    }

    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
     "location": {
      "objectType": "place",
      "displayName": "California, USA"
    }
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
