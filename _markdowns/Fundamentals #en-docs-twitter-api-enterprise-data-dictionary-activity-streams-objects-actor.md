



Activity Streams actor object | Docs | Twitter Developer Platform 





































































































Actor object



Actor object
------------


The actor object contains Twitter User account metadata that describes the Twitter User which created the activity.


 


### Data Dictionary




| Attribute | Type | Description |
| --- | --- | --- |
| objectType | string | **"objectType":** "person" |
| id | string | The string representation of the unique identifier for this author. Example:

```

"id:twitter.com:2244994945"

```


 |
| link |  | "http://www.twitter.com/TwitterDev |
| displayName | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:

```


**"displayName":** "Twitter Dev"

```


 |
| preferredUsername | string | The screen name, handle, or alias that this user identifies themselves with. Unique but subject to change. Use `id` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:

```


**"preferredUsername":** "TwitterDev"

```


 |
| location | object | **"location": {**
**"objectType":** "place"**,**
**"displayName":** "127.0.0.1"
**}** |
| links | array | *Nullable* . A URL provided by the user in association with their profile. Example:

```


**"links": [**

```

**{**
**"href":** "https://developer.twitter.com/en/community"**,**
**"rel":** "me"
**}**
**]**

 |
| summary | string | *Nullable* . The user-defined UTF-8 string describing their account. Example:

```


**"summary":** "The voice of the #TwitterDev team..."

```


 |
| protected | Boolean | When true, indicates that this user has chosen to protect their Tweets. See About Public and Protected Tweets . Example:

```

"protected": true

```


 |
| verified | Boolean | When true, indicates that the user has a verified account. See Verified Accounts . Example:

```

"verified": false

```


 |
| followersCount | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:

```

"followers_count": 21

```


 |
| friendsCount | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:

```

"friends_count": 32

```


 |
| listedCount | Int | The number of public lists that this user is a member of. Example:

```

"listed_count": 9274

```


 |
| favoritesCount | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:

```

"favourites_count": 13

```


 |
| statusesCount | Int | The number of Tweets (including retweets) issued by the user. Example:

```

"statuses_count": 42

```


 |
| postedTime | date | The UTC datetime that the user account was created on Twitter. Example:

```


**"postedTime":** "2013-12-14T04:35:55.036Z"

```


 |
| image | string | A HTTPS-based URL pointing to the user’s profile image. Example:

```


**"image":** "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg"

```


 |


### 
No longer supported (deprecated) attributes




| Field | Type | Description |
| --- | --- | --- |
| utcOffset | null | Value will be set to null. Still available via GET account/settings |
| twitterTimeZone | null | Value will be set to null. Still available via GET account/settings as tzinfo\_name |
| languages | null | Value will be set to null. Still available via GET account/settings as language |


### 
Examples:












```

            "actor": {
        "objectType": "person",
        "id": "id:twitter.com:2244994945",
        "link": "http://www.twitter.com/TwitterDev",
        "displayName": "Twitter Dev",
        "postedTime": "2013-12-14T04:35:55.036Z",
        "image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
        "summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "friendsCount": 2039,
        "followersCount": 512197,
        "listedCount": 1662,
        "statusesCount": 3632,
        "twitterTimeZone": null,
        "verified": true,
        "utcOffset": null,
        "preferredUsername": "TwitterDev",
        "languages": [],
        "links": [
          {
            "href": "https://developer.twitter.com/en/community",
            "rel": "me"
          }
        ],
        "location": {
          "objectType": "place",
          "displayName": "127.0.0.1"
        },
        "favoritesCount": 2147
      }
    
```





Code copied to clipboard














```

      "actor": {
    "objectType": "person",
    "id": "id:twitter.com:6253282",
    "link": "http://www.twitter.com/TwitterAPI",
    "displayName": "Twitter API",
    "postedTime": "2007-05-23T06:01:13.000Z",
    "image": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
    "summary": "Tweets about changes and service issues. Follow @TwitterDev for more.",
    "friendsCount": 39,
    "followersCount": 6054164,
    "listedCount": 12285,
    "statusesCount": 3689,
    "twitterTimeZone": null,
    "verified": true,
    "utcOffset": null,
    "preferredUsername": "TwitterAPI",
    "languages": [
      
    ],
    "links": [
      {
        "href": "https://developer.twitter.com",
        "rel": "me"
      }
    ],
    "favoritesCount": 4
  }
    
```





Code copied to clipboard








### Next Steps


Explore the other sub-objects that a Tweet contains:


* Tweet object and data dictionary
* Entities object and data dictionary
* Extended Entities object and data dictionary
* Tweet geo objects and data dictionaries



















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















