



User object | Docs | Twitter Developer Platform 





































































































User object



User
----


The user object contains Twitter user account metadata describing the referenced user. The user object is the primary object returned in the users lookup endpoint. When requesting additional user fields on this endpoint, simply use the fields parameter `user.fields`.


The user object can also be found as a child object and expanded in the Tweet object. The object is available for expansion with `?expansions=author_id` or `?expansions=in_reply_to_user_id` to get the condensed object with only default fields. Use the expansion with the field parameter: `user.fields` when requesting additional fields to complete the object.  

 




| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of this user.
`"id": "2244994945"` | Use this to programmatically retrieve information about a specific Twitter user. |
| name (default) | string | The name of the user, as they’ve defined it on their profile. Not necessarily a person’s name. Typically capped at 50 characters, but subject to change.
`"name": "Twitter Dev"` |  |
| username (default) | string | The Twitter screen name, handle, or alias that this user identifies themselves with. Usernames are unique but subject to change. Typically a maximum of 15 characters long, but some historical accounts may exist with longer names.
`"username": "TwitterDev"` |  |
| created\_at | date (ISO 8601) | The UTC datetime that the user account was created on Twitter.
`"created_at": "2013-12-14T04:35:55.000Z"` | Can be used to determine how long a someone has been using Twitter |
| description | string | The text of this user's profile description (also known as bio), if the user provided one.
`"description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter"` |  |
| entities | object | Contains details about text that has a special meaning in the user's description.
`"entities": {
        "url": {
            "urls": [
                {
                    "start": 0,
                    "end": 23,
                    "url": "https://t.co/3ZX3TNiZCY",
                    "expanded_url": "/content/developer-twitter/en/community",
                    "display_url": "developer.twitter.com/en/community"
                }
            ]
        },
        "description": {
            "urls": [
                {
                    "start": 0,
                    "end": 23,
                    "url": "https://t.co/3ZX3TNiZCY",
                    "expanded_url": "/content/developer-twitter/en/community",
                    "display_url": "developer.twitter.com/en/community"
                },
            "hashtags": [
                {
                    "start": 23,
                    "end": 30,
                    "tag": "DevRel"
                },
                {
                    "start": 113,
                    "end": 130,
                    "tag": "BlackLivesMatter"
                },
            "mentions": [
                {
                    "start": 0,
                    "end": 10,
                    "tag": "TwitterDev"
                },
            "cashtags": [
                {
                    "start": 12,
                    "end": 16,
                    "tag": "twtr"
                }
            ]
        }
    }` | Entities are JSON objects that provide additional information about hashtags, urls, user mentions, and cashtags associated with the description. Reference each respective entity for further details.
All user start indices are inclusive, while all user end indices are exclusive. |
| location | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.
`"location": "127.0.0.1"` |  |
| pinned\_tweet\_id | string | Unique identifier of this user's pinned Tweet.
`"pinned_tweet_id": "1255542774432063488"` | Determine the Tweet pinned to the top of the user’s profile. Can potentially be used to determine the user’s language. |
| profile\_image\_url | string | The URL to the profile image for this user, as shown on the user's profile.
`"profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg"` | Can be used to download this user's profile image. |
| protected | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).
`"protected": false` |  |
| public\_metrics | object | Contains details about activity for this user.
`"public_metrics": {             "followers_count": 507902,             "following_count": 1863,             "tweet_count": 3561,             "listed_count": 1550         }` | Can potentially be used to determine a Twitter user’s reach or influence, quantify the user’s range of interests, and the user’s level of engagement on Twitter. |
| url | string | The URL specified in the user's profile, if present.
`"url": "https://t.co/3ZX3TNiZCY"` | A URL provided by a Twitter user in their profile. This could be a homepage, but is not always the case. |
| verified | boolean | Indicates if this user is a verified Twitter User.
`"verified": true` | Indicates whether or not this Twitter user has a verified account. A verified account lets people know that an account of public interest is authentic. |
| withheld | object | Contains withholding details for withheld content, if applicable.
 |  |






### 


### Retrieving a user object


#### Sample Request


In the following request, we are requesting fields for the user on the users lookup endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

 












```

      curl --request GET 'https://api.twitter.com/2/users?ids=2244994945&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id' --header 'Authorization: Bearer $BEARER_TOKEN'

    
```





Code copied to clipboard








#### 
Sample Response












```

      {
    "data": [
        {
            "id": "2244994945",
            "name": "Twitter Dev",
            "username": "TwitterDev",
            "location": "127.0.0.1",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "start": 0,
                            "end": 23,
                            "url": "https://t.co/3ZX3TNiZCY",
                            "expanded_url": "/content/developer-twitter/en/community",
                            "display_url": "developer.twitter.com/en/community"
                        }
                    ]
                },
                "description": {
                    "hashtags": [
                        {
                            "start": 23,
                            "end": 30,
                            "tag": "DevRel"
                        },
                        {
                            "start": 113,
                            "end": 130,
                            "tag": "BlackLivesMatter"
                        }
                    ]
                }
            },
            "verified": true,
            "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",
            "url": "https://t.co/3ZX3TNiZCY",
            "profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg",
            "protected": false,
            "pinned_tweet_id": "1255542774432063488",
            "created_at": "2013-12-14T04:35:55.000Z"
        }
    ],
    "includes": {
        "tweets": [
            {
                "id": "1255542774432063488",
                "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"
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















