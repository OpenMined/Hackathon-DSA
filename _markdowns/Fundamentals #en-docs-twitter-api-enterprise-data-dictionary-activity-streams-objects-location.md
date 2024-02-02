



Activity Streams location object | Docs | Twitter Developer Platform 





































































































Location object



Location Object
---------------


Location obejcts can exist within the actor obejct set on the Twitter account level or within the profileLocations object of the gnip object. Location objects have a place object type and can have a name, address, or geo coordinates. Location objects are similar to Geo in native enriched format.


### Location data dictionary




| Field | Type | Description |
| --- | --- | --- |
| objectType | string | See here for more detailed information. Example:

```

**"objectType":** "place"

```


 |
| displayName | string | **The full name of the location.****"displayName":** "United States" |
| name | string | Name of the location from Twitter's place JSON format.

 |
| link | string | A link to the full Twitter JSON representation of the place.

**"link":** "https://api.twitter.com/1.1/geo/id/27c45d804c777999.json" |
| geo | object | The geo coordintates object from Twitter.  Either a polygon, or point.
 
See geo |
| countryCode | String | Shortened country code representing the country containing this place. Example:

```

**"countryCode": "US**

```


 |
| country | String | Name of the country containing this place. Example:

```

**"country":**"United States"

```


 |


#### 



profileLocations derived obejcts
---------------------------------




|  |  |  |
| --- | --- | --- |
| Field | Type | Description |
| address | object | Within profileLocation location object within the gnip object.  Address of location derived by the profile geo enrichement.  Level of granularity will vary. 
**"address": {**
**"country":**"United States"**,**
**"countryCode":**"US"**,**
**"locality":**"Providence"**,**
**"region":**"Rhode Island"**,**
**"subRegion":**"Providence County"
**}** |
| geo | object | Within profileLocation location object within the gnip object. Centroid coordinates of the location derived by the profile geo enrichement.
**"geo": {**
**"coordinates": [**
-98.5**,**
39.76
**],**
**"type":**"point"
**}**
 |



Examples
--------












```

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





Code copied to clipboard














```

          "location": {
      "objectType": "place",
      "displayName": "California, USA"
    }
    
```





Code copied to clipboard








Next steps
----------


Explore other Tweet JSON objects and data dictionaries:


* Tweet object and data dictionary
* User object and data dictionary
* Entities object and data dictionary
* Extended Entitites object and data dictionary


Read more about Tweets and their location metadata:


* Introduction to Tweet geospatial metadata
* Filtering Twitter data by location



















Developer policy and terms


Follow @XDevelopers


Subscribe to developer news












#### 
 X platform


* X.com
* Status
* Accessibility
* Embed a post
* Privacy Center
* Transparency Center
* Download the X app




#### 
 X Corp.


* About the company
* Company news
* Brand toolkit
* Jobs and internships
* Investors




#### 
 Help


* Help Center
* Using X
* X for creators
* Ads Help Center
* Managing your account
* Email Preference Center
* Rules and policies
* Contact us




#### 
 Developer resources


* Developer home
* Documentation
* Forums
* Communities
* Developer blog
* Engineering blog
* Developer terms




#### 
 Business resources


* Advertise
* X for business
* Resources and guides
* X for marketers
* Marketing insights
* Brand inspiration
* X Ads Academy









 © 2024 X Corp.
 


Cookies


Privacy


Terms and conditions






















**Did someone say … cookies?**  
  


 X and its partners use cookies to provide you with a better, safer and
 faster service and to support our business. Some cookies are necessary to use
 our services, improve our services, and make sure they work properly.
 Show more about your choices.


 




* Accept all cookies
* Refuse non-essential cookies















