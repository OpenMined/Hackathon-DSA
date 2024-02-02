
Activity Streams Gnip object | Docs | Twitter Developer Platform 

Gnip object

Gnip object
-----------

The gnip object, within Activity streams format, contains the metadata added by the active enrichments, as well as indication of the matching rules for the activity.

### Data dictionary

|  |  |  |
| --- | --- | --- |
| **Field** | **Type** | **Description** |
| matching\_rules | array | Contains an array of matching rule objects which indicate the rule which the activity matches on.
 **"matching\_rules": [**
**{**
**"tag": null,**
**"id":** 1026514022567358500**,**
**"id\_str":** "1026514022567358464"
**}**
**]** |
| urls | array | Contains an array of the links within the activity, and the expanded url metadata for the \*\*\*URL unwinding enrichement
**"urls": [**
**{**
**"url":** "https://t.co/tGQqNxxyhU"**,**
**"expanded\_url":** "https://www.youtube.com/channel/UCwUxW2CV2p5mzjMBqvqLzJA"**,**
**"expanded\_status":** 200**,**
**"expanded\_url\_title":** "Birdys Daughter"**,**
**"expanded\_url\_description":** "Premium, single-origin, handpicked Jamaica Blue Mountain Coffee"
**}**
**]** |
| profileLocations | array of location objects | Contains the derived location object from the Profile Geo enrichment
**"profileLocations": [**
**{**
**"address": {**
**"country":** "Canada"**,**
**"countryCode":** "CA"**,**
**"locality":** "Toronto"**,**
**"region":** "Ontario"
**},**
**"displayName":** "Toronto, Ontario, Canada"**,**
**"geo": {**
**"coordinates": [**
-79.4163**,**
43.70011
**],**
**"type":** "point"
**},**
**"objectType":** "place"
**}**
**]**
**}** |

### Example:

```
        "gnip": {
    "matching_rules": [
      {
        "tag": null
      }
    ],
    "urls": [
      {
        "url": "https://t.co/Nx1XZmRCXA",
        "expanded_url": "https://twittercommunity.com/t/new-update-to-the-twitter-text-library-emoji-character-count/114607",
        "expanded_status": 200,
        "expanded_url_title": null,
        "expanded_url_description": null
      }
    ]
  }
```

Code copied to clipboard

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