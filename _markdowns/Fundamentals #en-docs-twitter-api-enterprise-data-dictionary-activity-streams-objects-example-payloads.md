



Activity Streams example payloads | Docs | Twitter Developer Platform 





































































































Activity Streams example payloads



Activity streams payload examples
---------------------------------






Tweet activity












```

      {
	"id": "tag:search.twitter.com,2005:1307025659294674945",
	"objectType": "activity",
	"verb": "post",
	"postedTime": "2020-09-18T18:36:15.000Z",
	"generator": {
		"displayName": "Twitter Web App",
		"link": "https://mobile.twitter.com"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1307025659294674945",
	"body": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ",
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"objectType": "note",
		"id": "object:search.twitter.com,2005:1307025659294674945",
		"summary": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ",
		"link": "http://twitter.com/TwitterDev/statuses/1307025659294674945",
		"postedTime": "2020-09-18T18:36:15.000Z"
	},
	"inReplyTo": {
		"link": "http://twitter.com/TwitterDev/statuses/1304102743196356610"
	},
	"favoritesCount": 70,
	"twitter_entities": {
		"hashtags": [],
		"urls": [{
			"url": "https://t.co/oeF3ZHeKQQ",
			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
			"display_url": "dev.to/twitterdev/und…",
			"indices": [
				74,
				97
			]
		}],
		"user_mentions": [],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 11,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
			"url": "https://t.co/oeF3ZHeKQQ",
			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
			"expanded_status": 200,
			"expanded_url_title": "Understanding the new Tweet payload in the Twitter API v2",
			"expanded_url_description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features..."
		}]
	},
	"twitter_filter_level": "low"
}
    
```





Code copied to clipboard








Reply Tweet activity












```

      {
	"id": "tag:search.twitter.com,2005:1296887316556980230",
	"objectType": "activity",
	"verb": "post",
	"postedTime": "2020-08-21T19:10:05.000Z",
	"generator": {
		"displayName": "Twitter Web App",
		"link": "https://mobile.twitter.com"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1296887316556980230",
	"body": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes",
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"objectType": "note",
		"id": "object:search.twitter.com,2005:1296887316556980230",
		"summary": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes",
		"link": "http://twitter.com/TwitterDev/statuses/1296887316556980230",
		"postedTime": "2020-08-21T19:10:05.000Z"
	},
	"inReplyTo": {
		"link": "http://twitter.com/TwitterDev/statuses/1296887091901718529"
	},
	"favoritesCount": 26,
	"twitter_entities": {
		"hashtags": [],
		"urls": [{
			"url": "https://t.co/1tdA8uDWes",
			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn",
			"display_url": "developer.twitter.com/en/use-cases/s…",
			"indices": [
				87,
				110
			]
		}],
		"user_mentions": [{
			"screen_name": "PennMedCDH",
			"name": "Penn Med CDH",
			"id": 1615654896,
			"id_str": "1615654896",
			"indices": [
				8,
				19
			]
		}],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 9,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
			"url": "https://t.co/1tdA8uDWes",
			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn",
			"expanded_status": 200,
			"expanded_url_title": "Penn Medicine Center for Digital Health",
			"expanded_url_description": "Penn Med Center for Digital Health has created a COVID-19 Twitter map that includes charts detailing sentiment, symptoms reported, state-by-state data cuts, and border data on the COVID-19 outbreak. In addition, their Penn Med With You initiative uses aggregate regional information from Twitter to inform their website and text-messaging service. The service uses this information to disseminate relevant and timely resources."
		}]
	},
	"twitter_filter_level": "low"
}
    
```





Code copied to clipboard








Tweet activity with long\_object












```

      {
	"id": "tag:search.twitter.com,2005:1296121314218897408",
	"objectType": "activity",
	"verb": "post",
	"postedTime": "2020-08-19T16:26:16.000Z",
	"generator": {
		"displayName": "Twitter Web App",
		"link": "https://mobile.twitter.com"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1296121314218897408",
	"body": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn",
	"long_object": {
		"body": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps://t.co/khXhTurm9x",
		"display_text_range": [
			0,
			215
		],
		"twitter_entities": {
			"hashtags": [{
				"text": "TwitterAPI",
				"indices": [
					178,
					189
				]
			}],
			"urls": [{
				"url": "https://t.co/khXhTurm9x",
				"expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996",
				"display_url": "twittercommunity.com/t/hide-replies…",
				"indices": [
					192,
					215
				]
			}],
			"user_mentions": [],
			"symbols": []
		}
	},
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"objectType": "note",
		"id": "object:search.twitter.com,2005:1296121314218897408",
		"summary": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn",
		"link": "http://twitter.com/TwitterDev/statuses/1296121314218897408",
		"postedTime": "2020-08-19T16:26:16.000Z"
	},
	"favoritesCount": 172,
	"twitter_entities": {
		"hashtags": [],
		"urls": [{
			"url": "https://t.co/VyfXs1RTXn",
			"expanded_url": "https://twitter.com/i/web/status/1296121314218897408",
			"display_url": "twitter.com/i/web/status/1…",
			"indices": [
				117,
				140
			]
		}],
		"user_mentions": [],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 54,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
			"url": "https://t.co/khXhTurm9x",
			"expanded_url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996",
			"expanded_status": 200,
			"expanded_url_title": "Hide replies now available in the new Twitter API",
			"expanded_url_description": "Today, we’re happy to announce the general availability of the hide replies endpoint in the new Twitter API. The hide replies endpoint allows you to build tools that help people hide or unhide replies to their Tweets. People manage their replies for many reasons, including to give less attention to comments that are abusive, distracting, misleading, or to make conversations more engaging. Through this endpoint, you can build tools to help people on Twitter hide or unhide replies faster and more..."
		}]
	},
	"twitter_filter_level": "low"
}
    
```





Code copied to clipboard








Tweet activity with twitter\_extended\_entities












```

      {
	"id": "tag:search.twitter.com,2005:1293593516040269825",
	"objectType": "activity",
	"verb": "post",
	"postedTime": "2020-08-12T17:01:42.000Z",
	"generator": {
		"displayName": "Twitter Web App",
		"link": "https://mobile.twitter.com"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1293593516040269825",
	"body": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx",
	"long_object": {
		"body": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8",
		"display_text_range": [
			0,
			218
		],
		"twitter_entities": {
			"hashtags": [{
				"text": "TwitterAPI",
				"indices": [
					42,
					53
				]
			}],
			"urls": [{
				"url": "https://t.co/32VrwpGaJw",
				"expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html",
				"display_url": "blog.twitter.com/developer/en_u…",
				"indices": [
					195,
					218
				]
			}],
			"user_mentions": [],
			"symbols": [],
			"media": [{
				"id": 1293565706408038400,
				"id_str": "1293565706408038401",
				"indices": [
					219,
					242
				],
				"additional_media_info": {
					"monetizable": false
				},
				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg",
				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg",
				"url": "https://t.co/KaFSbjWUA8",
				"display_url": "pic.twitter.com/KaFSbjWUA8",
				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1",
				"type": "video",
				"video_info": {
					"aspect_ratio": [
						16,
						9
					],
					"duration_millis": 34875,
					"variants": [{
							"bitrate": 256000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10"
						},
						{
							"bitrate": 832000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10"
						},
						{
							"content_type": "application/x-mpegURL",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10"
						},
						{
							"bitrate": 2176000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10"
						}
					]
				},
				"sizes": {
					"thumb": {
						"w": 150,
						"h": 150,
						"resize": "crop"
					},
					"medium": {
						"w": 1200,
						"h": 675,
						"resize": "fit"
					},
					"small": {
						"w": 680,
						"h": 383,
						"resize": "fit"
					},
					"large": {
						"w": 1280,
						"h": 720,
						"resize": "fit"
					}
				}
			}]
		},
		"twitter_extended_entities": {
			"media": [{
				"id": 1293565706408038400,
				"id_str": "1293565706408038401",
				"indices": [
					219,
					242
				],
				"additional_media_info": {
					"monetizable": false
				},
				"media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg",
				"media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1293565706408038401/pu/img/66P2dvbU4a02jYbV.jpg",
				"url": "https://t.co/KaFSbjWUA8",
				"display_url": "pic.twitter.com/KaFSbjWUA8",
				"expanded_url": "https://twitter.com/TwitterDev/status/1293593516040269825/video/1",
				"type": "video",
				"video_info": {
					"aspect_ratio": [
						16,
						9
					],
					"duration_millis": 34875,
					"variants": [{
							"bitrate": 256000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/480x270/Fg9lnGGsITO0uq2K.mp4?tag=10"
						},
						{
							"bitrate": 832000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/640x360/-crbtZE4y8vKN_uF.mp4?tag=10"
						},
						{
							"content_type": "application/x-mpegURL",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/pl/OvIqQojosF6sMIHR.m3u8?tag=10"
						},
						{
							"bitrate": 2176000,
							"content_type": "video/mp4",
							"url": "https://video.twimg.com/ext_tw_video/1293565706408038401/pu/vid/1280x720/xkxyb-VPVY4OI0j9.mp4?tag=10"
						}
					]
				},
				"sizes": {
					"thumb": {
						"w": 150,
						"h": 150,
						"resize": "crop"
					},
					"medium": {
						"w": 1200,
						"h": 675,
						"resize": "fit"
					},
					"small": {
						"w": 680,
						"h": 383,
						"resize": "fit"
					},
					"large": {
						"w": 1280,
						"h": 720,
						"resize": "fit"
					}
				}
			}]
		}
	},
	"display_text_range": [
		0,
		140
	],
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"objectType": "note",
		"id": "object:search.twitter.com,2005:1293593516040269825",
		"summary": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx",
		"link": "http://twitter.com/TwitterDev/statuses/1293593516040269825",
		"postedTime": "2020-08-12T17:01:42.000Z"
	},
	"favoritesCount": 2844,
	"twitter_entities": {
		"hashtags": [{
			"text": "TwitterAPI",
			"indices": [
				42,
				53
			]
		}],
		"urls": [{
			"url": "https://t.co/UeCndQGMjx",
			"expanded_url": "https://twitter.com/i/web/status/1293593516040269825",
			"display_url": "twitter.com/i/web/status/1…",
			"indices": [
				117,
				140
			]
		}],
		"user_mentions": [],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 958,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
			"url": "https://t.co/32VrwpGaJw",
			"expanded_url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html",
			"expanded_status": 200,
			"expanded_url_title": "Introducing a new and improved Twitter API",
			"expanded_url_description": "Introducing the new Twitter API - rebuilt from the ground up to deliver new features faster so developers can help the world connect to the public conversation happening on Twitter."
		}]
	},
	"twitter_filter_level": "low"
}
    
```





Code copied to clipboard








Retweet activity












```

      {
	"id": "tag:search.twitter.com,2005:1229851574555508737",
	"objectType": "activity",
	"verb": "share",
	"postedTime": "2020-02-18T19:33:59.000Z",
	"generator": {
		"displayName": "Twitter Web App",
		"link": "https://mobile.twitter.com"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1229851574555508737",
	"body": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"id": "tag:search.twitter.com,2005:1229843515603144704",
		"objectType": "activity",
		"verb": "post",
		"postedTime": "2020-02-18T19:01:58.000Z",
		"generator": {
			"displayName": "Twitter Web App",
			"link": "https://mobile.twitter.com"
		},
		"provider": {
			"objectType": "service",
			"displayName": "Twitter",
			"link": "http://www.twitter.com"
		},
		"link": "http://twitter.com/suhemparack/statuses/1229843515603144704",
		"body": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i",
		"long_object": {
			"body": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps://t.co/l5J8wq748G",
			"display_text_range": [
				0,
				150
			],
			"twitter_entities": {
				"hashtags": [],
				"urls": [{
					"url": "https://t.co/l5J8wq748G",
					"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",
					"display_url": "dev.to/twitterdev/bui…",
					"indices": [
						127,
						150
					]
				}],
				"user_mentions": [],
				"symbols": []
			}
		},
		"actor": {
			"objectType": "person",
			"id": "id:twitter.com:857699969263964161",
			"link": "http://www.twitter.com/suhemparack",
			"displayName": "Suhem Parack",
			"postedTime": "2017-04-27T20:56:22.883Z",
			"image": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg",
			"summary": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",
			"friendsCount": 501,
			"followersCount": 732,
			"listedCount": 12,
			"statusesCount": 458,
			"twitterTimeZone": null,
			"verified": false,
			"utcOffset": null,
			"preferredUsername": "suhemparack",
			"languages": [],
			"links": [{
				"href": "https://developer.twitter.com",
				"rel": "me"
			}],
			"location": {
				"objectType": "place",
				"displayName": "Seattle, WA"
			},
			"favoritesCount": 358
		},
		"object": {
			"objectType": "note",
			"id": "object:search.twitter.com,2005:1229843515603144704",
			"summary": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i",
			"link": "http://twitter.com/suhemparack/statuses/1229843515603144704",
			"postedTime": "2020-02-18T19:01:58.000Z"
		},
		"favoritesCount": 71,
		"twitter_entities": {
			"hashtags": [],
			"urls": [{
				"url": "https://t.co/RP9NgltX7i",
				"expanded_url": "https://twitter.com/i/web/status/1229843515603144704",
				"display_url": "twitter.com/i/web/status/1…",
				"indices": [
					116,
					139
				]
			}],
			"user_mentions": [],
			"symbols": []
		},
		"twitter_lang": "en",
		"twitter_filter_level": "low"
	},
	"favoritesCount": 0,
	"twitter_entities": {
		"hashtags": [],
		"urls": [],
		"user_mentions": [{
			"screen_name": "suhemparack",
			"name": "Suhem Parack",
			"id": 857699969263964200,
			"id_str": "857699969263964161",
			"indices": [
				3,
				15
			]
		}],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 19,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
			"url": "https://t.co/l5J8wq748G",
			"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",
			"expanded_status": 200,
			"expanded_url_title": null,
			"expanded_url_description": null
		}]
	},
	"twitter_filter_level": "low"
}
    
```





Code copied to clipboard








Quote Tweet activity












```

       {
 	"id": "tag:search.twitter.com,2005:1328399838128467969",
 	"objectType": "activity",
 	"verb": "post",
 	"postedTime": "2020-11-16T18:09:36.000Z",
 	"generator": {
 		"displayName": "Twitter Web App",
 		"link": "https://mobile.twitter.com"
 	},
 	"provider": {
 		"objectType": "service",
 		"displayName": "Twitter",
 		"link": "http://www.twitter.com"
 	},
 	"link": "http://twitter.com/TwitterDev/statuses/1328399838128467969",
 	"body": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ",
 	"long_object": {
 		"body": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https://t.co/JaxttUMmjX",
 		"display_text_range": [
 			0,
 			166
 		],
 		"twitter_entities": {
 			"hashtags": [],
 			"urls": [{
 				"url": "https://t.co/JaxttUMmjX",
 				"expanded_url": "https://twitter.com/TwitterDev/status/1327011423252144128",
 				"display_url": "twitter.com/TwitterDev/sta…",
 				"indices": [
 					167,
 					190
 				]
 			}],
 			"user_mentions": [],
 			"symbols": []
 		}
 	},
 	"display_text_range": [
 		0,
 		140
 	],
 	"actor": {
 		"objectType": "person",
 		"id": "id:twitter.com:2244994945",
 		"link": "http://www.twitter.com/TwitterDev",
 		"displayName": "Twitter Dev",
 		"postedTime": "2013-12-14T04:35:55.036Z",
 		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
 		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
 		"friendsCount": 2038,
 		"followersCount": 512292,
 		"listedCount": 1666,
 		"statusesCount": 3634,
 		"twitterTimeZone": null,
 		"verified": true,
 		"utcOffset": null,
 		"preferredUsername": "TwitterDev",
 		"languages": [],
 		"links": [{
 			"href": "https://developer.twitter.com/en/community",
 			"rel": "me"
 		}],
 		"location": {
 			"objectType": "place",
 			"displayName": "127.0.0.1"
 		},
 		"favoritesCount": 2147
 	},
 	"object": {
 		"objectType": "note",
 		"id": "object:search.twitter.com,2005:1328399838128467969",
 		"summary": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ",
 		"link": "http://twitter.com/TwitterDev/statuses/1328399838128467969",
 		"postedTime": "2020-11-16T18:09:36.000Z"
 	},
 	"favoritesCount": 29,
 	"twitter_entities": {
 		"hashtags": [],
 		"urls": [{
 			"url": "https://t.co/ahQvTYaOcZ",
 			"expanded_url": "https://twitter.com/i/web/status/1328399838128467969",
 			"display_url": "twitter.com/i/web/status/1…",
 			"indices": [
 				117,
 				140
 			]
 		}],
 		"user_mentions": [],
 		"symbols": []
 	},
 	"twitter_lang": "en",
 	"retweetCount": 7,
 	"gnip": {
 		"matching_rules": [{
 			"tag": null
 		}],
 		"urls": [{
 			"url": "https://t.co/r6z6CI7kEy",
 			"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",
 			"expanded_status": 200,
 			"expanded_url_title": "Retiring Labs v2 recent search and hide replies",
 			"expanded_url_description": "As we said in our Early Access and hide replies announcements, the following Twitter Developer Labs v2 endpoints will be retired on November 16th. Labs v2 recent search Labs v2 hide replies If called, these endpoints will respond with an HTTP 410 status and return no data. Based on your feedback from Labs, we incorporated corresponding functionality into the Twitter API v2. The relevant documentation can be found using the links below. Click here to enroll in v2 access if you haven’t already..."
 		}]
 	},
 	"twitter_filter_level": "low",
 	"twitter_quoted_status": {
 		"id": "tag:search.twitter.com,2005:1327011423252144128",
 		"objectType": "activity",
 		"verb": "post",
 		"postedTime": "2020-11-12T22:12:32.000Z",
 		"generator": {
 			"displayName": "Twitter Web App",
 			"link": "https://mobile.twitter.com"
 		},
 		"provider": {
 			"objectType": "service",
 			"displayName": "Twitter",
 			"link": "http://www.twitter.com"
 		},
 		"link": "http://twitter.com/TwitterDev/statuses/1327011423252144128",
 		"body": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh",
 		"long_object": {
 			"body": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https://t.co/r6z6CI7kEy",
 			"display_text_range": [
 				0,
 				273
 			],
 			"twitter_entities": {
 				"hashtags": [{
 					"text": "TwitterAPI",
 					"indices": [
 						228,
 						239
 					]
 				}],
 				"urls": [{
 					"url": "https://t.co/r6z6CI7kEy",
 					"expanded_url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",
 					"display_url": "twittercommunity.com/t/retiring-lab…",
 					"indices": [
 						250,
 						273
 					]
 				}],
 				"user_mentions": [],
 				"symbols": []
 			}
 		},
 		"actor": {
 			"objectType": "person",
 			"id": "id:twitter.com:2244994945",
 			"link": "http://www.twitter.com/TwitterDev",
 			"displayName": "Twitter Dev",
 			"postedTime": "2013-12-14T04:35:55.036Z",
 			"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
 			"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
 			"friendsCount": 2038,
 			"followersCount": 512292,
 			"listedCount": 1666,
 			"statusesCount": 3634,
 			"twitterTimeZone": null,
 			"verified": true,
 			"utcOffset": null,
 			"preferredUsername": "TwitterDev",
 			"languages": [],
 			"links": [{
 				"href": "https://developer.twitter.com/en/community",
 				"rel": "me"
 			}],
 			"location": {
 				"objectType": "place",
 				"displayName": "127.0.0.1"
 			},
 			"favoritesCount": 2147
 		},
 		"object": {
 			"objectType": "note",
 			"id": "object:search.twitter.com,2005:1327011423252144128",
 			"summary": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh",
 			"link": "http://twitter.com/TwitterDev/statuses/1327011423252144128",
 			"postedTime": "2020-11-12T22:12:32.000Z"
 		},
 		"favoritesCount": 33,
 		"twitter_entities": {
 			"hashtags": [],
 			"urls": [{
 				"url": "https://t.co/EEWN2Q9aXh",
 				"expanded_url": "https://twitter.com/i/web/status/1327011423252144128",
 				"display_url": "twitter.com/i/web/status/1…",
 				"indices": [
 					117,
 					140
 				]
 			}],
 			"user_mentions": [],
 			"symbols": []
 		},
 		"twitter_lang": "en",
 		"twitter_filter_level": "low"
 	}
 }
    
```





Code copied to clipboard








Retweetd Quote Tweet activity












```

      {
	"id": "tag:search.twitter.com,2005:1225470895902412800",
	"objectType": "activity",
	"verb": "share",
	"postedTime": "2020-02-06T17:26:44.000Z",
	"generator": {
		"displayName": "Twitter for iPhone",
		"link": "http://twitter.com/download/iphone"
	},
	"provider": {
		"objectType": "service",
		"displayName": "Twitter",
		"link": "http://www.twitter.com"
	},
	"link": "http://twitter.com/TwitterDev/statuses/1225470895902412800",
	"body": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",
	"actor": {
		"objectType": "person",
		"id": "id:twitter.com:2244994945",
		"link": "http://www.twitter.com/TwitterDev",
		"displayName": "Twitter Dev",
		"postedTime": "2013-12-14T04:35:55.036Z",
		"image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
		"summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
		"friendsCount": 2038,
		"followersCount": 512292,
		"listedCount": 1666,
		"statusesCount": 3634,
		"twitterTimeZone": null,
		"verified": true,
		"utcOffset": null,
		"preferredUsername": "TwitterDev",
		"languages": [],
		"links": [{
			"href": "https://developer.twitter.com/en/community",
			"rel": "me"
		}],
		"location": {
			"objectType": "place",
			"displayName": "127.0.0.1"
		},
		"favoritesCount": 2147
	},
	"object": {
		"id": "tag:search.twitter.com,2005:1224709550214873090",
		"objectType": "activity",
		"verb": "post",
		"postedTime": "2020-02-04T15:01:25.000Z",
		"generator": {
			"displayName": "Twitter Web App",
			"link": "https://mobile.twitter.com"
		},
		"provider": {
			"objectType": "service",
			"displayName": "Twitter",
			"link": "http://www.twitter.com"
		},
		"link": "http://twitter.com/AureliaSpecker/statuses/1224709550214873090",
		"body": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp",
		"long_object": {
			"body": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https://t.co/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https://t.co/dXrJYvn3hY",
			"display_text_range": [
				0,
				229
			],
			"twitter_entities": {
				"hashtags": [{
						"text": "DEVcommunity",
						"indices": [
							176,
							189
						]
					},
					{
						"text": "Pythontutorial",
						"indices": [
							190,
							205
						]
					}
				],
				"urls": [{
						"url": "https://t.co/87XIPZmZBJ",
						"expanded_url": "https://bit.ly/2OrnrCC",
						"display_url": "bit.ly/2OrnrCC",
						"indices": [
							151,
							174
						]
					},
					{
						"url": "https://t.co/dXrJYvn3hY",
						"expanded_url": "https://twitter.com/AureliaSpecker/status/1195000047089389573",
						"display_url": "twitter.com/AureliaSpecker…",
						"indices": [
							230,
							253
						]
					}
				],
				"user_mentions": [{
						"screen_name": "TwitterDev",
						"name": "Twitter Dev",
						"id": 2244994945,
						"id_str": "2244994945",
						"indices": [
							206,
							217
						]
					},
					{
						"screen_name": "TwitterAPI",
						"name": "Twitter API",
						"id": 6253282,
						"id_str": "6253282",
						"indices": [
							218,
							229
						]
					}
				],
				"symbols": []
			}
		},
		"display_text_range": [
			0,
			140
		],
		"actor": {
			"objectType": "person",
			"id": "id:twitter.com:1102321381",
			"link": "http://www.twitter.com/AureliaSpecker",
			"displayName": "Aurelia Specker",
			"postedTime": "2013-01-18T23:45:43.000Z",
			"image": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
			"summary": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
			"friendsCount": 1331,
			"followersCount": 1032,
			"listedCount": 26,
			"statusesCount": 854,
			"twitterTimeZone": null,
			"verified": false,
			"utcOffset": null,
			"preferredUsername": "AureliaSpecker",
			"languages": [],
			"links": [{
				"href": null,
				"rel": "me"
			}],
			"location": {
				"objectType": "place",
				"displayName": "London, UK"
			},
			"favoritesCount": 4979
		},
		"object": {
			"objectType": "note",
			"id": "object:search.twitter.com,2005:1224709550214873090",
			"summary": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp",
			"link": "http://twitter.com/AureliaSpecker/statuses/1224709550214873090",
			"postedTime": "2020-02-04T15:01:25.000Z"
		},
		"favoritesCount": 43,
		"twitter_entities": {
			"hashtags": [],
			"urls": [{
				"url": "https://t.co/cAepHunkFp",
				"expanded_url": "https://twitter.com/i/web/status/1224709550214873090",
				"display_url": "twitter.com/i/web/status/1…",
				"indices": [
					117,
					140
				]
			}],
			"user_mentions": [],
			"symbols": []
		},
		"twitter_lang": "en",
		"twitter_filter_level": "low"
	},
	"favoritesCount": 0,
	"twitter_entities": {
		"hashtags": [],
		"urls": [],
		"user_mentions": [{
			"screen_name": "AureliaSpecker",
			"name": "Aurelia Specker",
			"id": 1102321381,
			"id_str": "1102321381",
			"indices": [
				3,
				18
			]
		}],
		"symbols": []
	},
	"twitter_lang": "en",
	"retweetCount": 12,
	"gnip": {
		"matching_rules": [{
			"tag": null
		}],
		"urls": [{
				"url": "https://t.co/87XIPZmZBJ",
				"expanded_url": "https://dev.to/twitterdev/migrate-to-twitter-s-newly-released-labs-recent-search-endpoint-3npe",
				"expanded_status": 200,
				"expanded_url_title": null,
				"expanded_url_description": null
			},
			{
				"url": "https://t.co/sOjXW4YhbN",
				"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",
				"expanded_status": 200,
				"expanded_url_title": null,
				"expanded_url_description": null
			}
		]
	},
	"twitter_filter_level": "low",
	"twitter_quoted_status": {
		"id": "tag:search.twitter.com,2005:1195000047089389573",
		"objectType": "activity",
		"verb": "post",
		"postedTime": "2019-11-14T15:26:27.000Z",
		"generator": {
			"displayName": "Twitter Web App",
			"link": "https://mobile.twitter.com"
		},
		"provider": {
			"objectType": "service",
			"displayName": "Twitter",
			"link": "http://www.twitter.com"
		},
		"link": "http://twitter.com/AureliaSpecker/statuses/1195000047089389573",
		"body": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",
		"long_object": {
			"body": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN",
			"display_text_range": [
				0,
				160
			],
			"twitter_entities": {
				"hashtags": [{
						"text": "DEVcommunity",
						"indices": [
							85,
							98
						]
					},
					{
						"text": "Pythontutorial",
						"indices": [
							99,
							114
						]
					}
				],
				"urls": [{
					"url": "https://t.co/sOjXW4YhbN",
					"expanded_url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",
					"display_url": "dev.to/twitterdev/usi…",
					"indices": [
						137,
						160
					]
				}],
				"user_mentions": [],
				"symbols": []
			}
		},
		"actor": {
			"objectType": "person",
			"id": "id:twitter.com:1102321381",
			"link": "http://www.twitter.com/AureliaSpecker",
			"displayName": "Aurelia Specker",
			"postedTime": "2013-01-18T23:45:43.000Z",
			"image": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
			"summary": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
			"friendsCount": 1331,
			"followersCount": 1032,
			"listedCount": 26,
			"statusesCount": 854,
			"twitterTimeZone": null,
			"verified": false,
			"utcOffset": null,
			"preferredUsername": "AureliaSpecker",
			"languages": [],
			"links": [{
				"href": null,
				"rel": "me"
			}],
			"location": {
				"objectType": "place",
				"displayName": "London, UK"
			},
			"favoritesCount": 4979
		},
		"object": {
			"objectType": "note",
			"id": "object:search.twitter.com,2005:1195000047089389573",
			"summary": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",
			"link": "http://twitter.com/AureliaSpecker/statuses/1195000047089389573",
			"postedTime": "2019-11-14T15:26:27.000Z"
		},
		"favoritesCount": 123,
		"twitter_entities": {
			"hashtags": [{
					"text": "DEVcommunity",
					"indices": [
						85,
						98
					]
				},
				{
					"text": "Pythontutorial",
					"indices": [
						99,
						114
					]
				}
			],
			"urls": [{
				"url": "https://t.co/pL0qJ4vhtE",
				"expanded_url": "https://twitter.com/i/web/status/1195000047089389573",
				"display_url": "twitter.com/i/web/status/1…",
				"indices": [
					116,
					139
				]
			}],
			"user_mentions": [],
			"symbols": []
		},
		"twitter_lang": "en",
		"twitter_filter_level": "low"
	}
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















