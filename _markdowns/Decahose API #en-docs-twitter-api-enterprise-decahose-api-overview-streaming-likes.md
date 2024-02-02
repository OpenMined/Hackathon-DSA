



Streaming likes | Docs | Twitter Developer Platform 





































































































Streaming likes



Enterprise


Streaming likes
===============


*This is an enterprise API available within our managed access levels only. To use this API, you must first set up an account with our enterprise sales team. Learn more*


Likes enable insight into who likes Tweets and delivers accurate counts of likes. Gnip’s Firehose and Decahose can deliver public likes related to the Tweets delivered via Gnip. This yields real-time public engagement and audience metrics associated with a Tweet.  

 


Getting started with Likes
--------------------------


As you prepare to consume likes data, you should know that:


* Likes are delivered via an independent, separate stream
* Likes are historically referred to as “Favorites”. The enriched native format payload maintains this nomenclature
* Streams include only public likes
	+ Public means that the liking user, Tweet creator and Tweet are all public on the platform
* Likes are very similar to Retweets and represent a public signal of engagement
* Payload elements include:
	+ Original Tweet object
	+ Actor object that created the original Tweet
	+ Actor object that performed the like action
* Only original content can be liked
	+ Retweets cannot be liked. A like of a Retweet is applied to the original Tweet
	+ Quoted Tweets *can* be liked
* Like activities include applicable Gnip Enrichments (where purchased/applied)
* Supported Products / Features
	+ Likes streams support Backfill (where purchased/applied)
	+ There is no Replay support for likes streams
	+ There is no Search or Historical support for likes
	+ There are no immediate plans to add likes support to PowerTrack


 


Decahose
--------


* For the 10% sample Tweets delivered in the Decahose, stream includes 100% of the applicable public likes
* **Partitions:** 2
* **URL Structure**
	+ https://gnip-stream.twitter.com/stream/sample10-likes/accounts/<accountName>/publishers/twitter/<streamLabel>.json?partition=1


Native enriched format payload
------------------------------












```

      {  
   "id":"43560406e0ad9f68374445f5f30c33fc",
   "created_at":"Thu Dec 01 22:27:39 +0000 2016",
   "timestamp_ms":1480631259353,
   "favorited_status":{  
      "created_at":"Thu Dec 01 22:27:16 +0000 2016",
      "id":804451830033948672,
      "id_str":"804451830033948672",
      "text":"@kafammheppduman",
      "source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e",
      "truncated":false,
      "in_reply_to_status_id":803694205163814912,
      "in_reply_to_status_id_str":"803694205163814912",
      "in_reply_to_user_id":2855759795,
      "in_reply_to_user_id_str":"2855759795",
      "in_reply_to_screen_name":"kafammheppduman",
      "user":{  
         "id":2855759795,
         "id_str":"2855759795",
         "name":"delirdim kanka",
         "screen_name":"kafammheppduman",
         "location":"sanane",
         "url":"http:\/\/instagram.com\/kafammheppduman",
         "description":"Manit @GalatasaraySk \ud83d\udc9e",
         "translator_type":"none",
         "protected":false,
         "verified":false,
         "followers_count":3702,
         "friends_count":607,
         "listed_count":1,
         "favourites_count":113338,
         "statuses_count":389,
         "created_at":"Sat Nov 01 22:38:25 +0000 2014",
         "utc_offset":null,
         "time_zone":null,
         "geo_enabled":true,
         "lang":"tr",
         "contributors_enabled":false,
         "is_translator":false,
         "profile_background_color":"C0DEED",
         "profile_background_image_url":"",
         "profile_background_image_url_https":"",
         "profile_background_tile":false,
         "profile_link_color":"1DA1F2",
         "profile_sidebar_border_color":"C0DEED",
         "profile_sidebar_fill_color":"DDEEF6",
         "profile_text_color":"333333",
         "profile_use_background_image":true,
       "Profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/804421763945861121\/v3bp9pnq_normal.jpg",
         "Profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/804421763945861121\/v3bp9pnq_normal.jpg",
         "profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2855759795\/1480630085",
         "default_profile":true,
         "default_profile_image":false,
         "following":null,
         "follow_request_sent":null,
         "notifications":null
      },
      "geo":null,
      "coordinates":null,
      "place":null,
      "contributors":null,
      "is_quote_status":false,
      "retweet_count":0,
      "favorite_count":0,
      "entities":{  
         "hashtags":[],
         "urls":[],
         "user_mentions":[  
            {  
               "screen_name":"kafammheppduman",
               "name":"delirdim kanka",
               "id":2855759795,
               "id_str":"2855759795",
               "indices":[  
                  0,
                  16
               ]
            }
         ],
         "symbols":[]
      },
      "favorited":false,
      "retweeted":false,
      "filter_level":"low",
      "lang":"und"
   },
   "user":{  
      "id":774146932365070336,
      "id_str":"774146932365070336",
      "name":"Uyuyan Adam",
      "screen_name":"saykoMenn",
      "location":"Tarsus, T\u00fcrkiye",
      "url":"http:\/\/connected2.me\/pmc1i",
      "description":null,
      "translator_type":"none",
      "protected":false,
      "verified":false,
      "followers_count":414,
      "friends_count":393,
      "listed_count":0,
      "favourites_count":9868,
      "statuses_count":370,
      "created_at":"Fri Sep 09 07:26:26 +0000 2016",
      "utc_offset":null,
      "time_zone":null,
      "geo_enabled":false,
      "lang":"tr",
      "contributors_enabled":false,
      "is_translator":false,
      "profile_background_color":"F5F8FA",
      "profile_background_image_url":"",
      "profile_background_image_url_https":"",
      "profile_background_tile":false,
      "profile_link_color":"1DA1F2",
      "profile_sidebar_border_color":"C0DEED",
      "profile_sidebar_fill_color":"DDEEF6",
      "profile_text_color":"333333",
      "profile_use_background_image":true,
      "Profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/802992813424201728\/VMzcTL3x_normal.jpg",
      "Profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/802992813424201728\/VMzcTL3x_normal.jpg",
      "profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/774146932365070336\/1480283382",
      "default_profile":true,
      "default_profile_image":false,
      "following":null,
      "follow_request_sent":null,
      "notifications":null
   }
}
    
```






Like Delete / “Unlike” payload
------------------------------












```

      {  
   "delete":{  
      "favorite":{  
         "tweet_id":696615514970279937,
         "tweet_id_str":"696615514970279937",
         "user_id":2510287578,
         "user_id_str":"2510287578"
      },
      "timestamp_ms":"1480437031205"
   }
}
    
```






Compliance guidance
-------------------


* Compliance only possible via Gnip Compliance Firehose
* If a tweet is deleted, all likes associated with that Tweet should be deleted (just like its Retweets)
	+ We will not deliver individual delete events for each Like in this scenario
* If a user protects/deletes his/her account, all likes performed by that user should be scrubbed (just like their Retweets)
	+ We will not deliver individual delete events for each like in this scenario
* If a user protects/deletes his/her account, all likes of that user’s Tweets should be scrubbed (just like their Tweets and Retweets)
	+ We will not deliver individual delete events for each like in this scenario
* If a user scrubs their geo, all likes associated with their Tweets should have its geo scrubbed (because the payload contains their original Tweet)
* If a user removes a like they performed (aka unliked), this is equivalent to a delete of that like and that like should be deleted.
	+ We will deliver an event in the Compliance Firehose to reflect these like deletions
	+ These like delete events will not include an ID for the original like event and will instead include the TweetID that was liked and the User that performed that like (a user can only like a Tweet once at a time)



















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















