::: is-table-default
Tweets can be associated with a location, generating a Tweet that has
been 'geo-tagged.' Tweet locations can be assigned by using the Twitter
user-interface or when posting a Tweet using the API. Tweet locations
can be an exact 'point' location, or a Twitter Place with a 'bounding
box' that describes a larger area ranging from a venue to an entire
region.

There are two 'root-level' JSON objects used to describe the location
associated with a Tweet: ` coordinates ` and ` place ` .

    {
       "coordinates": {}, 
       "place": {}
    }

The ` place ` object is always present when a Tweet is geo-tagged, while
the ` coordinates ` object is only present (non-null) when the Tweet is
assigned an *exact location* . If an exact location is provided, the
` coordinates ` object will provide a \[long, lat\] array with the
geographical coordinates, and a Twitter Place that corresponds to that
location will be assigned.

##  Place object

Places are specific, named locations with corresponding geo coordinates.
When users decide to assign a location to their Tweet, they are
presented with a list of candidate Twitter Places. When using the API to
post a Tweet, a Twitter Place can be attached by specifying a
**place_id** when posting the Tweet. Tweets associated with Places are
not necessarily issued from that location but could also potentially be
*about* that location.

##  Place data dictionary

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| id                    | String                | ID representing this  |
|                       |                       | place. Note that this |
|                       |                       | is represented as a   |
|                       |                       | string, not an        |
|                       |                       | integer. Example:     |
+-----------------------+-----------------------+-----------------------+
| url                   | String                | URL representing the  |
|                       |                       | location of           |
|                       |                       | additional place      |
|                       |                       | metadata for this     |
|                       |                       | place. Example:       |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "                 |
|                       |                       | url":"https://api.twi |
|                       |                       | tter.com/1.1/geo/id/0 |
|                       |                       | 1a9a39529b27f36.json" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| place_type            | String                | The type of location  |
|                       |                       | represented by this   |
|                       |                       | place. Example:       |
+-----------------------+-----------------------+-----------------------+
| name                  | String                | Short human-readable  |
|                       |                       | representation of the |
|                       |                       | place's name.         |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| full_name             | String                | Full human-readable   |
|                       |                       | representation of the |
|                       |                       | place's name.         |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "full_            |
|                       |                       | name":"Manhattan, NY" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| country_code          | String                | Shortened country     |
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
|                       |                       |     "cou              |
|                       |                       | ntry":"United States" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| bounding_box          | [Object](#obj-bo      | A bounding box of     |
|                       | undingbox){.reference | coordinates which     |
|                       | .external}            | encloses this place.  |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |     "bounding_box": { |
|                       |                       |                       |
|                       |                       |      "coordinates": [ |
|                       |                       |           [           |
|                       |                       |             [         |
|                       |                       |                       |
|                       |                       |           -74.026675, |
|                       |                       |                       |
|                       |                       |             40.683935 |
|                       |                       |             ],        |
|                       |                       |             [         |
|                       |                       |                       |
|                       |                       |           -74.026675, |
|                       |                       |                       |
|                       |                       |             40.877483 |
|                       |                       |             ],        |
|                       |                       |             [         |
|                       |                       |                       |
|                       |                       |           -73.910408, |
|                       |                       |                       |
|                       |                       |             40.877483 |
|                       |                       |             ],        |
|                       |                       |             [         |
|                       |                       |                       |
|                       |                       |           -73.910408, |
|                       |                       |               40.3935 |
|                       |                       |             ]         |
|                       |                       |           ]           |
|                       |                       |         ],            |
|                       |                       |                       |
|                       |                       |     "type": "Polygon" |
|                       |                       |       }               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| attributes            | Object                | When using            |
|                       |                       | PowerTrack, 30-Day    |
|                       |                       | and Full-Archive      |
|                       |                       | Search APIs, and      |
|                       |                       | Volume Streams this   |
|                       |                       | hash is null.         |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+

::: section
+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| coordinates           | Array of Array of     | A series of longitude |
|                       | Array of Float        | and latitude points,  |
|                       |                       | defining a box which  |
|                       |                       | will contain the      |
|                       |                       | Place entity this     |
|                       |                       | bounding box is       |
|                       |                       | related to. Each      |
|                       |                       | point is an array in  |
|                       |                       | the form of           |
|                       |                       | \[longitude,          |
|                       |                       | latitude\]. Points    |
|                       |                       | are grouped into an   |
|                       |                       | array per bounding    |
|                       |                       | box. Bounding box     |
|                       |                       | arrays are wrapped in |
|                       |                       | one additional array  |
|                       |                       | to be compatible with |
|                       |                       | the polygon notation. |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     {                 |
|                       |                       |                       |
|                       |                       |      "coordinates": [ |
|                       |                       |         [             |
|                       |                       |           [           |
|                       |                       |                       |
|                       |                       |           -74.026675, |
|                       |                       |             40.683935 |
|                       |                       |           ],          |
|                       |                       |           [           |
|                       |                       |                       |
|                       |                       |           -74.026675, |
|                       |                       |             40.877483 |
|                       |                       |           ],          |
|                       |                       |           [           |
|                       |                       |                       |
|                       |                       |           -73.910408, |
|                       |                       |             40.877483 |
|                       |                       |           ],          |
|                       |                       |           [           |
|                       |                       |                       |
|                       |                       |           -73.910408, |
|                       |                       |             40.3935   |
|                       |                       |           ]           |
|                       |                       |         ]             |
|                       |                       |       ]               |
|                       |                       |     }                 |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| type                  | String                | The type of data      |
|                       |                       | encoded in the        |
|                       |                       | coordinates property. |
|                       |                       | This will be          |
|                       |                       | "Polygon" for         |
|                       |                       | bounding boxes and    |
|                       |                       | "Point" for Tweets    |
|                       |                       | with exact            |
|                       |                       | coordinates. Example: |
+-----------------------+-----------------------+-----------------------+
:::

##  Coordinates object data dictionary

+-----------------------+-----------------------+-----------------------+
| Field                 | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| coordinates           | Collection of Float   | The longitude and     |
|                       |                       | latitude of the       |
|                       |                       | Tweet's location, as  |
|                       |                       | a collection in the   |
|                       |                       | form **\[longitude,   |
|                       |                       | latitude\]** .        |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |   "coordinates":[-97. |
|                       |                       | 51087576,35.46500176] |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| type                  | String                | The type of data      |
|                       |                       | encoded in the        |
|                       |                       | coordinates property. |
|                       |                       | This will be "Point"  |
|                       |                       | for Tweet coordinates |
|                       |                       | fields. Example:      |
+-----------------------+-----------------------+-----------------------+

## JSON examples for geo-referenced Tweets

###  Tweet with Twitter Place

    {
      "geo": null,
      "coordinates": null,
      "place": {
        "id": "07d9db48bc083000",
        "url": "https://api.twitter.com/1.1/geo/id/07d9db48bc083000.json",
        "place_type": "poi",
        "name": "McIntosh Lake",
        "full_name": "McIntosh Lake",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ],
              [
                -105.14544,
                40.192138
              ]
            ]
          ]
        },
        "attributes": {
          
        }
      }
    }






###  Tweet with exact location

    {
      "geo": {
        "type": "Point",
        "coordinates": [
          40.74118764,
          -73.9998279
        ]
      },
      "coordinates": {
        "type": "Point",
        "coordinates": [
          -73.9998279,
          40.74118764
        ]
      },
      "place": {
        "id": "01a9a39529b27f36",
        "url": "https://api.twitter.com/1.1/geo/id/01a9a39529b27f36.json",
        "place_type": "city",
        "name": "Manhattan",
        "full_name": "Manhattan, NY",
        "country_code": "US",
        "country": "United States",
        "bounding_box": {
          "type": "Polygon",
          "coordinates": [
            [
              [
                -74.026675,
                40.683935
              ],
              [
                -74.026675,
                40.877483
              ],
              [
                -73.910408,
                40.877483
              ],
              [
                -73.910408,
                40.683935
              ]
            ]
          ]
        },
        "attributes": {
          
        }
      }
    }






##  Next steps

Explore other Tweet JSON objects and data dictionaries:

Read more about Tweets and their location metadata:
:::
