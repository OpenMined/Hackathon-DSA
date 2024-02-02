
Native Enriched example payloads | Docs | Twitter Developer Platform 

Native Enriched example payloads

### Tweet

```
      {
	"created_at": "Fri Sep 18 18:36:15 +0000 2020",
	"id": 1307025659294675000,
	"id_str": "1307025659294674945",
	"text": "Here’s an article that highlights the updates in the new Tweet payload v2 https://t.co/oeF3ZHeKQQ",
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
	"truncated": false,
	"in_reply_to_status_id": 1304102743196356600,
	"in_reply_to_status_id_str": "1304102743196356610",
	"in_reply_to_user_id": 2244994945,
	"in_reply_to_user_id_str": "2244994945",
	"in_reply_to_screen_name": "TwitterDev",
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"is_quote_status": false,
	"quote_count": 1,
	"reply_count": 2,
	"retweet_count": 11,
	"favorite_count": 70,
	"entities": {
		"hashtags": [],
		"urls": [{
			"url": "https://t.co/oeF3ZHeKQQ",
			"expanded_url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
			"display_url": "dev.to/twitterdev/und…",
			"unwound": {
				"url": "https://dev.to/twitterdev/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
				"status": 200,
				"title": "Understanding the new Tweet payload in the Twitter API v2",
				"description": "Twitter recently announced the new Twitter API v2, rebuilt from the ground up to deliver new features..."
			},
			"indices": [
				74,
				97
			]
		}],
		"user_mentions": [],
		"symbols": []
	},
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Tweet reply

```
      {
	"created_at": "Fri Aug 21 19:10:05 +0000 2020",
	"id": 1296887316556980200,
	"id_str": "1296887316556980230",
	"text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes",
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
	"truncated": false,
	"in_reply_to_status_id": 1296887091901718500,
	"in_reply_to_status_id_str": "1296887091901718529",
	"in_reply_to_user_id": 2244994945,
	"in_reply_to_user_id_str": "2244994945",
	"in_reply_to_screen_name": "TwitterDev",
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"is_quote_status": false,
	"quote_count": 2,
	"reply_count": 3,
	"retweet_count": 9,
	"favorite_count": 26,
	"entities": {
		"hashtags": [],
		"urls": [{
			"url": "https://t.co/1tdA8uDWes",
			"expanded_url": "https://developer.twitter.com/en/use-cases/success-stories/penn",
			"display_url": "developer.twitter.com/en/use-cases/s…",
			"unwound": {
				"url": "https://developer.twitter.com/en/use-cases/success-stories/penn",
				"status": 200,
				"title": "Penn Medicine Center for Digital Health",
				"description": "Penn Med Center for Digital Health has created a COVID-19 Twitter map that includes charts detailing sentiment, symptoms reported, state-by-state data cuts, and border data on the COVID-19 outbreak. In addition, their Penn Med With You initiative uses aggregate regional information from Twitter to inform their website and text-messaging service. The service uses this information to disseminate relevant and timely resources."
			},
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
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Extended Tweet

```
      {
	"created_at": "Wed Aug 19 16:26:16 +0000 2020",
	"id": 1296121314218897400,
	"id_str": "1296121314218897408",
	"text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https://t.co/VyfXs1RTXn",
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
	"truncated": true,
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"is_quote_status": false,
	"extended_tweet": {
		"full_text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps://t.co/khXhTurm9x",
		"display_text_range": [
			0,
			215
		],
		"entities": {
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
				"unwound": {
					"url": "https://twittercommunity.com/t/hide-replies-now-available-in-the-new-twitter-api/140996",
					"status": 200,
					"title": "Hide replies now available in the new Twitter API",
					"description": "Today, we’re happy to announce the general availability of the hide replies endpoint in the new Twitter API. The hide replies endpoint allows you to build tools that help people hide or unhide replies to their Tweets. People manage their replies for many reasons, including to give less attention to comments that are abusive, distracting, misleading, or to make conversations more engaging. Through this endpoint, you can build tools to help people on Twitter hide or unhide replies faster and more..."
				},
				"indices": [
					192,
					215
				]
			}],
			"user_mentions": [],
			"symbols": []
		}
	},
	"quote_count": 23,
	"reply_count": 9,
	"retweet_count": 54,
	"favorite_count": 172,
	"entities": {
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
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Tweet with extended\_entitites

```
      {
	"created_at": "Wed Aug 12 17:01:42 +0000 2020",
	"id": 1293593516040269800,
	"id_str": "1293593516040269825",
	"text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to b… https://t.co/UeCndQGMjx",
	"display_text_range": [
		0,
		140
	],
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
	"truncated": true,
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"is_quote_status": false,
	"extended_tweet": {
		"full_text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8",
		"display_text_range": [
			0,
			218
		],
		"entities": {
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
				"unwound": {
					"url": "https://blog.twitter.com/developer/en_us/topics/tools/2020/introducing_new_twitter_api.html",
					"status": 200,
					"title": "Introducing a new and improved Twitter API",
					"description": "Introducing the new Twitter API - rebuilt from the ground up to deliver new features faster so developers can help the world connect to the public conversation happening on Twitter."
				},
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
		"extended_entities": {
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
	"quote_count": 332,
	"reply_count": 172,
	"retweet_count": 958,
	"favorite_count": 2844,
	"entities": {
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
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Retweet

```
      {
	"created_at": "Tue Feb 18 19:33:59 +0000 2020",
	"id": 1229851574555508700,
	"id_str": "1229851574555508737",
	"text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"retweeted_status": {
		"created_at": "Tue Feb 18 19:01:58 +0000 2020",
		"id": 1229843515603144700,
		"id_str": "1229843515603144704",
		"text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https://t.co/RP9NgltX7i",
		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
		"truncated": true,
		"in_reply_to_status_id": null,
		"in_reply_to_status_id_str": null,
		"in_reply_to_user_id": null,
		"in_reply_to_user_id_str": null,
		"in_reply_to_screen_name": null,
		"user": {
			"id": 857699969263964200,
			"id_str": "857699969263964161",
			"name": "Suhem Parack",
			"screen_name": "suhemparack",
			"location": "Seattle, WA",
			"url": "https://developer.twitter.com",
			"description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",
			"translator_type": "none",
			"protected": false,
			"verified": false,
			"followers_count": 732,
			"friends_count": 501,
			"listed_count": 12,
			"favourites_count": 358,
			"statuses_count": 458,
			"created_at": "Thu Apr 27 20:56:22 +0000 2017",
			"utc_offset": null,
			"time_zone": null,
			"geo_enabled": false,
			"lang": null,
			"contributors_enabled": false,
			"is_translator": false,
			"profile_background_color": "F5F8FA",
			"profile_background_image_url": "",
			"profile_background_image_url_https": "",
			"profile_background_tile": false,
			"profile_link_color": "1DA1F2",
			"profile_sidebar_border_color": "C0DEED",
			"profile_sidebar_fill_color": "DDEEF6",
			"profile_text_color": "333333",
			"profile_use_background_image": true,
			"profile_image_url": "http://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg",
			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1230703695051935747/TbQKe91L_normal.jpg",
			"profile_banner_url": "https://pbs.twimg.com/profile_banners/857699969263964161/1593055939",
			"default_profile": true,
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
			"full_text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps://t.co/l5J8wq748G",
			"display_text_range": [
				0,
				150
			],
			"entities": {
				"hashtags": [],
				"urls": [{
					"url": "https://t.co/l5J8wq748G",
					"expanded_url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",
					"display_url": "dev.to/twitterdev/bui…",
					"unwound": {
						"url": "https://dev.to/twitterdev/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",
						"status": 200,
						"title": null,
						"description": null
					},
					"indices": [
						127,
						150
					]
				}],
				"user_mentions": [],
				"symbols": []
			}
		},
		"quote_count": 6,
		"reply_count": 1,
		"retweet_count": 19,
		"favorite_count": 71,
		"entities": {
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
	"favorited": false,
	"retweeted": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Quote Tweet

```
      {
	"created_at": "Mon Nov 16 18:09:36 +0000 2020",
	"id": 1328399838128468000,
	"id_str": "1328399838128467969",
	"text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https://t.co/ahQvTYaOcZ",
	"display_text_range": [
		0,
		140
	],
	"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
	"truncated": true,
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
	},
	"geo": null,
	"coordinates": null,
	"place": null,
	"contributors": null,
	"quoted_status_id": 1327011423252144000,
	"quoted_status_id_str": "1327011423252144128",
	"quoted_status": {
		"created_at": "Thu Nov 12 22:12:32 +0000 2020",
		"id": 1327011423252144000,
		"id_str": "1327011423252144128",
		"text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https://t.co/EEWN2Q9aXh",
		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
		"truncated": true,
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
		},
		"geo": null,
		"coordinates": null,
		"place": null,
		"contributors": null,
		"is_quote_status": false,
		"extended_tweet": {
			"full_text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https://t.co/r6z6CI7kEy",
			"display_text_range": [
				0,
				273
			],
			"entities": {
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
					"unwound": {
						"url": "https://twittercommunity.com/t/retiring-labs-v2-recent-search-and-hide-replies/145795",
						"status": 200,
						"title": "Retiring Labs v2 recent search and hide replies",
						"description": "As we said in our Early Access and hide replies announcements, the following Twitter Developer Labs v2 endpoints will be retired on November 16th. Labs v2 recent search Labs v2 hide replies If called, these endpoints will respond with an HTTP 410 status and return no data. Based on your feedback from Labs, we incorporated corresponding functionality into the Twitter API v2. The relevant documentation can be found using the links below. Click here to enroll in v2 access if you haven’t already..."
					},
					"indices": [
						250,
						273
					]
				}],
				"user_mentions": [],
				"symbols": []
			}
		},
		"quote_count": 4,
		"reply_count": 2,
		"retweet_count": 8,
		"favorite_count": 33,
		"entities": {
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
		"favorited": false,
		"retweeted": false,
		"possibly_sensitive": false,
		"filter_level": "low",
		"lang": "en"
	},
	"quoted_status_permalink": {
		"url": "https://t.co/JaxttUMmjX",
		"expanded": "https://twitter.com/TwitterDev/status/1327011423252144128",
		"display": "twitter.com/TwitterDev/sta…"
	},
	"is_quote_status": true,
	"extended_tweet": {
		"full_text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https://t.co/JaxttUMmjX",
		"display_text_range": [
			0,
			166
		],
		"entities": {
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
	"quote_count": 1,
	"reply_count": 4,
	"retweet_count": 7,
	"favorite_count": 29,
	"entities": {
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
	"favorited": false,
	"retweeted": false,
	"possibly_sensitive": false,
	"filter_level": "low",
	"lang": "en",
	"matching_rules": [{
		"tag": null
	}]
}
```

Code copied to clipboard

### Retweeted Quote Tweet

```
       {
 	"created_at": "Thu Feb 06 17:26:44 +0000 2020",
 	"id": 1225470895902412800,
 	"id_str": "1225470895902412800",
 	"text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",
 	"source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
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
 	},
 	"geo": null,
 	"coordinates": null,
 	"place": null,
 	"contributors": null,
 	"retweeted_status": {
 		"created_at": "Tue Feb 04 15:01:25 +0000 2020",
 		"id": 1224709550214873000,
 		"id_str": "1224709550214873090",
 		"text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https://t.co/cAepHunkFp",
 		"display_text_range": [
 			0,
 			140
 		],
 		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
 		"truncated": true,
 		"in_reply_to_status_id": null,
 		"in_reply_to_status_id_str": null,
 		"in_reply_to_user_id": null,
 		"in_reply_to_user_id_str": null,
 		"in_reply_to_screen_name": null,
 		"user": {
 			"id": 1102321381,
 			"id_str": "1102321381",
 			"name": "Aurelia Specker",
 			"screen_name": "AureliaSpecker",
 			"location": "London, UK",
 			"url": null,
 			"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
 			"translator_type": "none",
 			"protected": false,
 			"verified": false,
 			"followers_count": 1032,
 			"friends_count": 1331,
 			"listed_count": 26,
 			"favourites_count": 4979,
 			"statuses_count": 854,
 			"created_at": "Fri Jan 18 23:45:43 +0000 2013",
 			"utc_offset": null,
 			"time_zone": null,
 			"geo_enabled": true,
 			"lang": null,
 			"contributors_enabled": false,
 			"is_translator": false,
 			"profile_background_color": "8B542B",
 			"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",
 			"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",
 			"profile_background_tile": false,
 			"profile_link_color": "5E341C",
 			"profile_sidebar_border_color": "D9B17E",
 			"profile_sidebar_fill_color": "EADEAA",
 			"profile_text_color": "333333",
 			"profile_use_background_image": true,
 			"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 			"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",
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
 		"quoted_status_id": 1195000047089389600,
 		"quoted_status_id_str": "1195000047089389573",
 		"quoted_status": {
 			"created_at": "Thu Nov 14 15:26:27 +0000 2019",
 			"id": 1195000047089389600,
 			"id_str": "1195000047089389573",
 			"text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",
 			"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
 			"truncated": true,
 			"in_reply_to_status_id": null,
 			"in_reply_to_status_id_str": null,
 			"in_reply_to_user_id": null,
 			"in_reply_to_user_id_str": null,
 			"in_reply_to_screen_name": null,
 			"user": {
 				"id": 1102321381,
 				"id_str": "1102321381",
 				"name": "Aurelia Specker",
 				"screen_name": "AureliaSpecker",
 				"location": "London, UK",
 				"url": null,
 				"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
 				"translator_type": "none",
 				"protected": false,
 				"verified": false,
 				"followers_count": 1032,
 				"friends_count": 1331,
 				"listed_count": 26,
 				"favourites_count": 4979,
 				"statuses_count": 854,
 				"created_at": "Fri Jan 18 23:45:43 +0000 2013",
 				"utc_offset": null,
 				"time_zone": null,
 				"geo_enabled": true,
 				"lang": null,
 				"contributors_enabled": false,
 				"is_translator": false,
 				"profile_background_color": "8B542B",
 				"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",
 				"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",
 				"profile_background_tile": false,
 				"profile_link_color": "5E341C",
 				"profile_sidebar_border_color": "D9B17E",
 				"profile_sidebar_fill_color": "EADEAA",
 				"profile_text_color": "333333",
 				"profile_use_background_image": true,
 				"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 				"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 				"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",
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
 				"full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN",
 				"display_text_range": [
 					0,
 					160
 				],
 				"entities": {
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
 						"unwound": {
 							"url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",
 							"status": 200,
 							"title": null,
 							"description": null
 						},
 						"indices": [
 							137,
 							160
 						]
 					}],
 					"user_mentions": [],
 					"symbols": []
 				}
 			},
 			"quote_count": 4,
 			"reply_count": 5,
 			"retweet_count": 31,
 			"favorite_count": 123,
 			"entities": {
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
 			"favorited": false,
 			"retweeted": false,
 			"possibly_sensitive": false,
 			"filter_level": "low",
 			"lang": "en"
 		},
 		"quoted_status_permalink": {
 			"url": "https://t.co/dXrJYvn3hY",
 			"expanded": "https://twitter.com/AureliaSpecker/status/1195000047089389573",
 			"display": "twitter.com/AureliaSpecker…"
 		},
 		"is_quote_status": true,
 		"extended_tweet": {
 			"full_text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https://t.co/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https://t.co/dXrJYvn3hY",
 			"display_text_range": [
 				0,
 				229
 			],
 			"entities": {
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
 						"unwound": {
 							"url": "https://dev.to/twitterdev/migrate-to-twitter-s-newly-released-labs-recent-search-endpoint-3npe",
 							"status": 200,
 							"title": null,
 							"description": null
 						},
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
 		"quote_count": 2,
 		"reply_count": 0,
 		"retweet_count": 12,
 		"favorite_count": 43,
 		"entities": {
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
 		"favorited": false,
 		"retweeted": false,
 		"possibly_sensitive": false,
 		"filter_level": "low",
 		"lang": "en"
 	},
 	"quoted_status_id": 1195000047089389600,
 	"quoted_status_id_str": "1195000047089389573",
 	"quoted_status": {
 		"created_at": "Thu Nov 14 15:26:27 +0000 2019",
 		"id": 1195000047089389600,
 		"id_str": "1195000047089389573",
 		"text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https://t.co/pL0qJ4vhtE",
 		"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
 		"truncated": true,
 		"in_reply_to_status_id": null,
 		"in_reply_to_status_id_str": null,
 		"in_reply_to_user_id": null,
 		"in_reply_to_user_id_str": null,
 		"in_reply_to_screen_name": null,
 		"user": {
 			"id": 1102321381,
 			"id_str": "1102321381",
 			"name": "Aurelia Specker",
 			"screen_name": "AureliaSpecker",
 			"location": "London, UK",
 			"url": null,
 			"description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
 			"translator_type": "none",
 			"protected": false,
 			"verified": false,
 			"followers_count": 1032,
 			"friends_count": 1331,
 			"listed_count": 26,
 			"favourites_count": 4979,
 			"statuses_count": 854,
 			"created_at": "Fri Jan 18 23:45:43 +0000 2013",
 			"utc_offset": null,
 			"time_zone": null,
 			"geo_enabled": true,
 			"lang": null,
 			"contributors_enabled": false,
 			"is_translator": false,
 			"profile_background_color": "8B542B",
 			"profile_background_image_url": "http://abs.twimg.com/images/themes/theme8/bg.gif",
 			"profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme8/bg.gif",
 			"profile_background_tile": false,
 			"profile_link_color": "5E341C",
 			"profile_sidebar_border_color": "D9B17E",
 			"profile_sidebar_fill_color": "EADEAA",
 			"profile_text_color": "333333",
 			"profile_use_background_image": true,
 			"profile_image_url": "http://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 			"profile_image_url_https": "https://pbs.twimg.com/profile_images/1137517534104772608/8FBYgc6G_normal.jpg",
 			"profile_banner_url": "https://pbs.twimg.com/profile_banners/1102321381/1587552672",
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
 			"full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps://t.co/sOjXW4YhbN",
 			"display_text_range": [
 				0,
 				160
 			],
 			"entities": {
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
 					"unwound": {
 						"url": "https://dev.to/twitterdev/using-the-twitter-api-to-make-your-commute-easier-3od0",
 						"status": 200,
 						"title": null,
 						"description": null
 					},
 					"indices": [
 						137,
 						160
 					]
 				}],
 				"user_mentions": [],
 				"symbols": []
 			}
 		},
 		"quote_count": 4,
 		"reply_count": 5,
 		"retweet_count": 31,
 		"favorite_count": 123,
 		"entities": {
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
 		"favorited": false,
 		"retweeted": false,
 		"possibly_sensitive": false,
 		"filter_level": "low",
 		"lang": "en"
 	},
 	"quoted_status_permalink": {
 		"url": "https://t.co/dXrJYvn3hY",
 		"expanded": "https://twitter.com/AureliaSpecker/status/1195000047089389573",
 		"display": "twitter.com/AureliaSpecker…"
 	},
 	"is_quote_status": true,
 	"quote_count": 0,
 	"reply_count": 0,
 	"retweet_count": 0,
 	"favorite_count": 0,
 	"entities": {
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
 	"favorited": false,
 	"retweeted": false,
 	"filter_level": "low",
 	"lang": "en",
 	"matching_rules": [{
 		"tag": null
 	}]
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