



Place objects | Docs | Twitter Developer Platform 





































































































Place objects



Place
-----


The place tagged in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet resource. 


The object is available for expansion with `?expansions=geo.place_id` to get the condensed object with only default fields. Use the expansion with the field parameter: `place.fields` when requesting additional fields to complete the object.


 




| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| full\_name (default) | string | A longer-form detailed place name.
`"full_name": "Manhattan, NY"` | Classify a Tweet by a specific place name |
| id (default) | string | The unique identifier of the expanded place, if this is a point of interest tagged in the Tweet.
`"id": "01a9a39529b27f36"` | Use this to programmatically retrieve a place |
| contained\_within | array | Returns the identifiers of known places that contain the referenced place. |  |
| country | string | The full-length name of the country this place belongs to.
`"country": "United States"` | Classify a Tweet by country name |
| country\_code | string | The ISO Alpha-2 country code this place belongs to.
`"country_code": "US"` | Classify a Tweet by country code |
| geo | object | Contains place details in GeoJSON format.
`"geo": {
      "type": "Feature",
      "bbox": [
            -74.026675, 
            40.683935, 
            -73.910408, 
            40.877483 
       ], 
       "properties": {}
    }` |  |
| name | string | The short name of this place.
`"name": "Manhattan"` | Classify a Tweet by a specific place name |
| place\_type | string | Specified the particular type of information represented by this place information, such as a city name, or a point of interest.
`"place_type": "city"` | Classify a Tweet by a specific type of place |


### 
Retrieving a place object


#### Sample Request


In the following request, we are requesting fields for the place object attached to the Tweet on the Tweets lookup endpoint. Since place is a child object of a Tweet, the `geo.place_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

 












```

      curl --request GET 'https://api.twitter.com/2/tweets?ids=1136048014974423040&expansions=geo.place_id&place.fields=contained_within,country,country_code,full_name,geo,id,name,place_type' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








#### 
Sample Response












```

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















