
Post Tweet geo guide | Docs | Twitter Developer Platform 

Post Tweet geo guide

#### **Geo-Tagging**

* Tweets can be created with geo data using the POST statuses/update method.
* Any geo-tagging parameters in an API statuses/update will be ignored if geo\_enabled for the user is false (this is the default setting for all users, unless the user has enabled geolocation in their settings).
* The number of digits after the decimal separator passed to lat (up to 8) is tracked so that when the lat is returned in a status object it will have the same number of digits after the decimal separator.
* Use a decimal point as the separator (and not a decimal comma) for the latitude and the longitude - usage of a decimal comma will cause the geo-tagged portion of the status update to be dropped.

#### **Geo Point**

* For JSON, the response mostly uses conventions described in GeoJSON. However, the geo object coordinates that Twitter renders are **reversed** from the GeoJSON specification. GeoJSON specifies a longitude then a latitude, whereas Twitter represents it as a latitude then a longitude: "geo": { "type":"Point", "coordinates":[37.78217, -122.40062] }
* The coordinates object is replacing the geo object (no deprecation date has been set for the geo object yet) – the difference is that the coordinates object, in JSON, is now rendered correctly in GeoJSON.

#### **Place ID**

* If a place\_id is passed into the status update, then that place will be attached to the status. If no place\_id was explicitly provided, but latitude and longitude are, the API attempts to implicitly provide a place by calling geo/reverse\_geocode.

#### **Geo compliance**

* Users have the ability to remove all geotags from all their Tweets en masse via the user settings page. Currently there is no API method to remove geotags from individual Tweets.
* The scrub\_geo compliance object will be sent through the Compliance Firehose for the specific User's Tweets.

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