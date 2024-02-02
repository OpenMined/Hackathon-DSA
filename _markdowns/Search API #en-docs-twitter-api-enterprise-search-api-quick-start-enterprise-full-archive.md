



Enterprise Search Tweets: Full-Archive API | Docs | Twitter Developer Platform 





































































































Enterprise Search Tweets: Full-Archive API



Getting started with enterprise Search Tweets: Full-Archive API
---------------------------------------------------------------


**⏱ 10 min read**


The enterprise Search Tweets: Full-Archive API provides you with Tweets since the first one posted in 2006. Tweets are matched and sent back to you based on the query you specify in your request. A query is a rule in which you define what the Tweet you get back should contain. In this tutorial, we will search for Tweets originating from the Twitter account @TwitterDev in English.


The Tweets you get back in your payload can be in a data format, which provides you with the full Tweet payload, or it can be in a counts format which gives you numerical count data of matched Tweets. We will be using cURL to make requests to the data and counts endpoints.


You will need the following:






* An enterprise account
* Your username, password, and account name
* Label associated with your search endpoint, as displayed at console.gnip.com


 






### Accessing the data endpoint


  

The data endpoint will provide us with the full Tweet payload of matched Tweets. We will use the `from:` and `lang:` operators to find Tweets originating from @TwitterDev in English. *For more operators click here.*


 








* cURL
* cURL example
* 


















 cURL
 

 cURL example
 












*cURL is a command-line tool for getting or sending files using the URL syntax.*


 


Copy the following cURL request into your command line after making changes to the following:


 


* **Username** `<USERNAME>` e.g. `email@domain.com`
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`
* **Label** `<LABEL>` e.g. `prod`
* **fromDate and toDate** e.g. `"fromDate":"201802010000", "toDate":"201802282359"`






*After sending your request, you will be prompted for your password.*












```

      curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/fullarchive/accounts/<ACCOUNT-NAME>/<LABEL>.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>"}'
    
```





Code copied to clipboard












*This is an example cURL request. If you try to run this it will not work.*












```

      curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/fullarchive/accounts/john-doe/prod.json" -d '{"query":"from:TwitterDev lang:en","maxResults":"500","fromDate":"201802010000","toDate":"201802282359"}'
    
```





Code copied to clipboard


















#### Data endpoint response payload


The payload you get back from your API request will appear in JSON format, as shown below.












```

      {
	"results": [
		{
			"created_at": "Fri Nov 02 17:18:31 +0000 2018",
			"id": 1058408022936977409,
			"id_str": "1058408022936977409",
			"text": "RT @harmophone: \"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conv…",
			"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>",
			"truncated": false,
			"in_reply_to_status_id": null,
			"in_reply_to_status_id_str": null,
			"in_reply_to_user_id": null,
			"in_reply_to_user_id_str": null,
			"in_reply_to_screen_name": null,
			"user": {
				"id": 2244994945,
				"id_str": "2244994945",
				"name": "Twitter Dev",
				"screen_name": "TwitterDev",
				"location": "Internet",
				"url": "https:\/\/developer.twitter.com\/",
				"description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ ⌨️ #TapIntoTwitter",
				"translator_type": "null",
				"protected": false,
				"verified": true,
				"followers_count": 503828,
				"friends_count": 1477,
				"listed_count": 1437,
				"favourites_count": 2199,
				"statuses_count": 3380,
				"created_at": "Sat Dec 14 04:35:55 +0000 2013",
				"utc_offset": null,
				"time_zone": null,
				"geo_enabled": true,
				"lang": "en",
				"contributors_enabled": false,
				"is_translator": false,
				"profile_background_color": "null",
				"profile_background_image_url": "null",
				"profile_background_image_url_https": "null",
				"profile_background_tile": null,
				"profile_link_color": "null",
				"profile_sidebar_border_color": "null",
				"profile_sidebar_fill_color": "null",
				"profile_text_color": "null",
				"profile_use_background_image": null,
				"profile_image_url": "null",
				"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/880136122604507136\/xHrnqf1T_normal.jpg",
				"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1498675817",
				"default_profile": false,
				"default_profile_image": false,
				"following": null,
				"follow_request_sent": null,
				"notifications": null
			},
			"geo": null,
			"coordinates": null,
			"place": null,
			"contributors": null,
			"retweeted_status": {
				"created_at": "Tue Oct 30 21:30:25 +0000 2018",
				"id": 1057384253116289025,
				"id_str": "1057384253116289025",
				"text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relev… https:\/\/t.co\/w46U5TRTzQ",
				"source": "<a href=\"http:\/\/twitter.com\" rel=\"nofollow\">Twitter Web Client<\/a>",
				"truncated": true,
				"in_reply_to_status_id": null,
				"in_reply_to_status_id_str": null,
				"in_reply_to_user_id": null,
				"in_reply_to_user_id_str": null,
				"in_reply_to_screen_name": null,
				"user": {
					"id": 175187944,
					"id_str": "175187944",
					"name": "Tyler Singletary",
					"screen_name": "harmophone",
					"location": "San Francisco, CA",
					"url": "http:\/\/medium.com\/@harmophone",
					"description": "SVP Product at @Tagboard. Did some Data, biz, and product @Klout & for @LithiumTech; @BBI board member; @Insightpool advisor. World's worst whiteboarder.",
					"translator_type": "null",
					"protected": false,
					"verified": false,
					"followers_count": 1982,
					"friends_count": 1877,
					"listed_count": 245,
					"favourites_count": 23743,
					"statuses_count": 12708,
					"created_at": "Thu Aug 05 22:59:29 +0000 2010",
					"utc_offset": null,
					"time_zone": null,
					"geo_enabled": false,
					"lang": "en",
					"contributors_enabled": false,
					"is_translator": false,
					"profile_background_color": "null",
					"profile_background_image_url": "null",
					"profile_background_image_url_https": "null",
					"profile_background_tile": null,
					"profile_link_color": "null",
					"profile_sidebar_border_color": "null",
					"profile_sidebar_fill_color": "null",
					"profile_text_color": "null",
					"profile_use_background_image": null,
					"profile_image_url": "null",
					"profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/719985428632240128\/WYFHcK-m_normal.jpg",
					"profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/175187944\/1398653841",
					"default_profile": false,
					"default_profile_image": false,
					"following": null,
					"follow_request_sent": null,
					"notifications": null
				},
				"geo": null,
				"coordinates": null,
				"place": null,
				"contributors": null,
				"is_quote_status": false,
				"extended_tweet": {
					"full_text": "\"The innovative crowdsourcing that the Tagboard, Twitter and TEGNA collaboration enables is surfacing locally relevant conversations in real-time and enabling voters to ask questions during debates,”  -- @adamostrow, @TEGNA\nLearn More: https:\/\/t.co\/ivAFtanfje",
					"display_text_range": [
						0,
						259
					],
					"entities": {
						"hashtags": [],
						"urls": [
							{
								"url": "https:\/\/t.co\/ivAFtanfje",
								"expanded_url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4",
								"display_url": "blog.tagboard.com\/twitter-and-ta…",
								"unwound": {
									"url": "https:\/\/blog.tagboard.com\/twitter-and-tagboard-collaborate-to-bring-best-election-content-to-news-outlets-with-tagboard-e85fc864bcf4",
									"status": 200,
									"title": "Twitter and Tagboard Collaborate to Bring Best Election Content to News Outlets With Tagboard…",
									"description": "By Tyler Singletary, Head of Product, Tagboard"
								},
								"indices": [
									236,
									259
								]
							}
						],
						"user_mentions": [
							{
								"screen_name": "adamostrow",
								"name": "Adam Ostrow",
								"id": 5695942,
								"id_str": "5695942",
								"indices": [
									204,
									215
								]
							},
							{
								"screen_name": "TEGNA",
								"name": "TEGNA",
								"id": 34123003,
								"id_str": "34123003",
								"indices": [
									217,
									223
								]
							}
						],
						"symbols": []
					}
				},
				"quote_count": 0,
				"reply_count": 1,
				"retweet_count": 6,
				"favorite_count": 19,
				"entities": {
					"hashtags": [],
					"urls": [
						{
							"url": "https:\/\/t.co\/w46U5TRTzQ",
							"expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1057384253116289025",
							"display_url": "twitter.com\/i\/web\/status\/1…",
							"indices": [
								117,
								140
							]
						}
					],
					"user_mentions": [],
					"symbols": []
				},
				"favorited": false,
				"retweeted": false,
				"possibly_sensitive": false,
				"filter_level": "low",
				"lang": "en"
			},
			"is_quote_status": false,
			"quote_count": 0,
			"reply_count": 0,
			"retweet_count": 0,
			"favorite_count": 0,
			"entities": {
				"hashtags": [],
				"urls": [],
				"user_mentions": [
					{
						"screen_name": "harmophone",
						"name": "Tyler Singletary",
						"id": 175187944,
						"id_str": "175187944",
						"indices": [
							3,
							14
						]
					}
				],
				"symbols": []
			},
			"favorited": false,
			"retweeted": false,
			"filter_level": "low",
			"lang": "en",
			"matching_rules": [
				{
					"tag": null
				}
			]
		}
	],
	"requestParameters": {
		"maxResults": 100,
		"fromDate": "201811010000",
		"toDate": "201811060000"
	}
}
    
```










### Accessing the counts endpoint


With the counts endpoint, we’ll retrieve the number of Tweets originating from the @TwitterDev account in English grouped by `day`.


 








* cURL
* cURL example
* 


















 cURL
 

 cURL example
 












*cURL is a command-line tool for getting or sending files using the URL syntax.*


 


Copy the following cURL request into your command line after making changes to the following:


 


* **Username** `<USERNAME>` e.g. `email@domain.com`
* **Account name** `<ACCOUNT-NAME>` e.g. `john-doe`
* **Label** `<LABEL>` e.g. `prod`
* **fromDate and toDate** e.g. `"fromDate":"201802010000", "toDate":"201802282359"`






*After sending your request, you will be prompted for your password.*












```

      curl -X POST -u<USERNAME> "https://gnip-api.twitter.com/search/fullarchive/accounts/<ACCOUNT-NAME>/<LABEL>/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>","bucket":"day"}'
    
```





Code copied to clipboard












*This is an example cURL request. If you try to run this it will not work.*












```

      curl -X POST -uemail@domain.com "https://gnip-api.twitter.com/search/fullarchive/accounts/john-doe/prod/counts.json" -d '{"query":"from:TwitterDev lang:en","fromDate":"201802010000","toDate":"201802282359","bucket":"day"}'
    
```





Code copied to clipboard


















#### Counts endpoint response payload


The payload you get back from your API request will appear in JSON format, as shown below.












```

      {
	"results": [
		{
			"timePeriod": "201811010000",
			"count": 0
		},
		{
			"timePeriod": "201811020000",
			"count": 1
		},
		{
			"timePeriod": "201811030000",
			"count": 0
		},
		{
			"timePeriod": "201811040000",
			"count": 0
		},
		{
			"timePeriod": "201811050000",
			"count": 0
		}
	],
	"totalCount": 1,
	"requestParameters": {
		"bucket": "day",
		"fromDate": "201811010000",
		"toDate": "201811060000"
	}
}
    
```






  

Great job! Now you've successfully accessed the enterprise Search Tweets: Full-Archive API.  

 


### Referenced articles


* Introduction to Tweet objects
* Premium search operators
* Tweet objects and payloads



Next Steps
-----------


* Discover more about the counts endpoint
* Join the conversation on Twitter community forums



















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















