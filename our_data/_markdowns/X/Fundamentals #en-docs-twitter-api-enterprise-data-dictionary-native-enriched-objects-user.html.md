
Native Enriched user object | Docs | Twitter Developer Platform 

User object

User object
-----------

The User object contains Twitter User account metadata that describes the Twitter User referenced. 

### User Data Dictionary

| Attribute | Type | Description |
| --- | --- | --- |
| id | Int64 | The integer representation of the unique identifier for this User. This number is greater than 53 bits and some programming languages may have difficulty/silent defects in interpreting it. Using a signed 64 bit integer for storing this identifier is safe. Use `id\_str` to fetch the identifier to be safe. See Twitter IDs for more information. Example:
```
"id": 6253282
```

 |
| id\_str | String | The string representation of the unique identifier for this User. Implementations should use this rather than the large, possibly un-consumable integer in `id`. Example:
```
"id_str": "6253282"
```

 |
| name | String | The name of the user, as they’ve defined it. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change. Example:
```
"name": "Twitter API"
```

 |
| screen\_name | String | The screen name, handle, or alias that this user identifies themselves with. screen\_names are unique but subject to change. Use `id\_str` as a user identifier whenever possible. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names. Example:
```
"screen_name": "twitterapi"
```

 |
| location | String | *Nullable* . The user-defined location for this account’s profile. Not necessarily a location, nor machine-parseable. This field will occasionally be fuzzily interpreted by the Search service. Example:
```
"location": "San Francisco, CA"
```

 |
| derived | Arrays of Enrichment Objects | Enterprise APIs only Collection of Enrichment metadata derived for user. Provides the *Profile Geo* Enrichment metadata. See referenced documentation for more information, including JSON data dictionaries. Example:
```
"derived":{"locations": [{"country":"United States","country_code":"US","locality":"Denver"}]}
```

 |
| url | String | *Nullable* . A URL provided by the user in association with their profile. Example:
```
"url": "https://developer.twitter.com"
```

 |
| description | String | *Nullable* . The user-defined UTF-8 string describing their account. Example:
```
"description": "The Real Twitter API."
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
| followers\_count | Int | The number of followers this account currently has. Under certain conditions of duress, this field will temporarily indicate “0”. Example:
```
"followers_count": 21
```

 |
| friends\_count | Int | The number of users this account is following (AKA their “followings”). Under certain conditions of duress, this field will temporarily indicate “0”. Example:
```
"friends_count": 32
```

 |
| listed\_count | Int | The number of public lists that this user is a member of. Example:
```
"listed_count": 9274
```

 |
| favourites\_count | Int | The number of Tweets this user has liked in the account’s lifetime. British spelling used in the field name for historical reasons. Example:
```
"favourites_count": 13
```

 |
| statuses\_count | Int | The number of Tweets (including retweets) issued by the user. Example:
```
"statuses_count": 42
```

 |
| created\_at | String | The UTC datetime that the user account was created on Twitter. Example:
```
"created_at": "Mon Nov 29 21:18:15 +0000 2010"
```

 |
| profile\_banner\_url | String | The HTTPS-based URL pointing to the standard web representation of the user’s uploaded profile banner. By adding a final path element of the URL, it is possible to obtain different image sizes optimized for specific displays. For size variants, please see User Profile Images and Banners .
Example:
```
"profile_banner_url": "https://si0.twimg.com/profile_banners/819797/1348102824"
```

 |
| profile\_image\_url\_https | String | A HTTPS-based URL pointing to the user’s profile image. Example:
```
"profile_image_url_https":
"https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png"
```

 |
| default\_profile | Boolean | When true, indicates that the user has not altered the theme or background of their user profile. Example:
```
"default_profile": false
```

 |
| default\_profile\_image | Boolean | When true, indicates that the user has not uploaded their own profile image and a default image is used instead. Example:
```
"default_profile_image": false
```

 |

### 
No longer supported (deprecated) attributes

| Field | Type | Description |
| --- | --- | --- |
| utc\_offset | null | Value will be set to null. Still available via GET account/settings |
| time\_zone | null | Value will be set to null. Still available via GET account/settings as tzinfo\_name |
| lang | null | Value will be set to null. Still available via GET account/settings as language |
| geo\_enabled | null | Value will be set to null.  Still available via GET account/settings. This field must be true for the current user to attach geographic data when using POST statuses / update |
| following | null | Value will be set to null. Still available via GET friendships/lookup |
| follow\_request\_sent | null | Value will be set to null. Still available via GET friendships/lookup |
| has\_extended\_profile | null | **Deprecated**. Value will be set to null. |
| notifications | null | **Deprecated**. Value will be set to null. |
| profile\_location | null | **Deprecated**. Value will be set to null. |
| contributors\_enabled | null | **Deprecated**. Value will be set to null. |
| profile\_image\_url | null | **Deprecated**. Value will be set to null. NOTE: Profile images are only available using the profile\_image\_url\_https field. |
| profile\_background\_color | null | **Deprecated**. Value will be set to null. |
| profile\_background\_image\_url | null | **Deprecated**. Value will be set to null. |
| profile\_background\_image\_url\_https | null | **Deprecated**. Value will be set to null. |
| profile\_background\_tile | null | **Deprecated**. Value will be set to null. |
| profile\_link\_color | null | **Deprecated**. Value will be set to null. |
| profile\_sidebar\_border\_color | null | **Deprecated**. Value will be set to null. |
| profile\_sidebar\_fill\_color | null | **Deprecated**. Value will be set to null. |
| profile\_text\_color | null | **Deprecated**. Value will be set to null. |
| profile\_use\_background\_image | null | **Deprecated**. Value will be set to null. |
| is\_translator | null | **Deprecated**. Value will be set to null. |
| is\_translation\_enabled | null | **Deprecated**. Value will be set to null. |
| translator\_type | null | **Deprecated**. Value will be set to null. |

### 
Example user object:

```
      "user": {
		"id": 2244994945,
		"id_str": "2244994945",
		"name": "Twitter Dev",
		"screen_name": "TwitterDev",
		"location": "127.0.0.1",
		"url": "https://developer.twitter.com/en/community",
		"description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"translator_type": "regular",
		"protected": false,
		"verified": true,
		"followers_count": 512292,
		"friends_count": 2038,
		"listed_count": 1666,
		"favourites_count": 2147,
		"statuses_count": 3634,
		"created_at": "Sat Dec 14 04:35:55 +0000 2013",
		"utc_offset": null,
		"time_zone": null,
		"geo_enabled": true,
		"lang": null,
		"contributors_enabled": false,
		"is_translator": false,
		"profile_background_color": "FFFFFF",
		"profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png",
		"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png",
		"profile_background_tile": false,
		"profile_link_color": "0084B4",
		"profile_sidebar_border_color": "FFFFFF",
		"profile_sidebar_fill_color": "DDEEF6",
		"profile_text_color": "333333",
		"profile_use_background_image": false,
		"profile_image_url": "http://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"profile_image_url_https": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"profile_banner_url": "https://pbs.twimg.com/profile_banners/2244994945/1594913664",
		"default_profile": false,
		"default_profile_image": false,
		"following": null,
		"follow_request_sent": null,
		"notifications": null
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