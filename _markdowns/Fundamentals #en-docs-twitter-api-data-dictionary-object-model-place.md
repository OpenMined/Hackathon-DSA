::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The place tagged in a Tweet is not a primary object on any endpoint, but
can be found and expanded in the Tweet resource.

The object is available for expansion with ` ?expansions=geo.place_id `
to get the condensed object with only default fields. Use the expansion
with the field parameter: ` place.fields ` when requesting additional
fields to complete the object.

+-----------------+-----------------+-----------------+-----------------+
| Field value     | Type            | Description     | How it can be   |
|                 |                 |                 | used            |
+-----------------+-----------------+-----------------+-----------------+
| full_name       | string          | A longer-form   | Classify a      |
| (default)       |                 | detailed place  | Tweet by a      |
|                 |                 | name.           | specific place  |
|                 |                 |                 | name            |
|                 |                 | `               |                 |
|                 |                 | "full_name": "M |                 |
|                 |                 | anhattan, NY" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| id (default)    | string          | The unique      | Use this to     |
|                 |                 | identifier of   | p               |
|                 |                 | the expanded    | rogrammatically |
|                 |                 | place, if this  | retrieve a      |
|                 |                 | is a point of   | place           |
|                 |                 | interest tagged |                 |
|                 |                 | in the Tweet.   |                 |
|                 |                 |                 |                 |
|                 |                 | ` "id": "01a9   |                 |
|                 |                 | a39529b27f36" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| c               | array           | Returns the     |                 |
| ontained_within |                 | identifiers of  |                 |
|                 |                 | known places    |                 |
|                 |                 | that contain    |                 |
|                 |                 | the referenced  |                 |
|                 |                 | place.          |                 |
+-----------------+-----------------+-----------------+-----------------+
| country         | string          | The full-length | Classify a      |
|                 |                 | name of the     | Tweet by        |
|                 |                 | country this    | country name    |
|                 |                 | place belongs   |                 |
|                 |                 | to.             |                 |
|                 |                 |                 |                 |
|                 |                 | ` "country": "U |                 |
|                 |                 | nited States" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| country_code    | string          | The ISO Alpha-2 | Classify a      |
|                 |                 | country code    | Tweet by        |
|                 |                 | this place      | country code    |
|                 |                 | belongs to.     |                 |
|                 |                 |                 |                 |
|                 |                 | ` "countr       |                 |
|                 |                 | y_code": "US" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| geo             | object          | Contains place  |                 |
|                 |                 | details in      |                 |
|                 |                 | GeoJSON format. |                 |
|                 |                 |                 |                 |
|                 |                 | `               |                 |
|                 |                 |  "geo": { "type |                 |
|                 |                 | ": "Feature", " |                 |
|                 |                 | bbox": [ -74.02 |                 |
|                 |                 | 6675, 40.683935 |                 |
|                 |                 | , -73.910408, 4 |                 |
|                 |                 | 0.877483 ], "pr |                 |
|                 |                 | operties": {} ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| name            | string          | The short name  | Classify a      |
|                 |                 | of this place.  | Tweet by a      |
|                 |                 |                 | specific place  |
|                 |                 | ` "name"        | name            |
|                 |                 | : "Manhattan" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| place_type      | string          | Specified the   | Classify a      |
|                 |                 | particular type | Tweet by a      |
|                 |                 | of information  | specific type   |
|                 |                 | represented by  | of place        |
|                 |                 | this place      |                 |
|                 |                 | information,    |                 |
|                 |                 | such as a city  |                 |
|                 |                 | name, or a      |                 |
|                 |                 | point of        |                 |
|                 |                 | interest.       |                 |
|                 |                 |                 |                 |
|                 |                 | ` "place_       |                 |
|                 |                 | type": "city" ` |                 |
+-----------------+-----------------+-----------------+-----------------+

###  Retrieving a place object

#### Sample Request

In the following request, we are requesting fields for the place object
attached to the Tweet on the [Tweets
lookup](/en/docs/twitter-api/tweets/lookup) endpoint. Since place is a
child object of a Tweet, the ` geo.place_id ` expansion is required. Be
sure to replace ` $BEARER_TOKEN ` with your own generated [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/tweets?ids=1136048014974423040&expansions=geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "text": "We’re sharing a live demo of the new Twitter Developer Labs program, led by a member of our DevRel team, @jessicagarson #TapIntoTwitter https://t.co/ghv7f4dW5M",
            "id": "1136048014974423040",
            "geo": {
                "place_id": "01a9a39529b27f36"
            }
        }
    ],
    "includes": {
        "places": [
            {
                "geo": {
                    "type": "Feature",
                    "bbox": [
                        -74.026675,
                        40.683935,
                        -73.910408,
                        40.877483
                    ],
                    "properties": {}
                },
                "country_code": "US",
                "name": "Manhattan",
                "id": "01a9a39529b27f36",
                "place_type": "city",
                "country": "United States",
                "full_name": "Manhattan, NY"
            }
        ]
    }
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
