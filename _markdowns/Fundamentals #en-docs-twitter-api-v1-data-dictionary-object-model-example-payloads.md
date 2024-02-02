



Example payloads | Docs | Twitter Developer Platform 





































































































Example payloads



### Tweet












```

      {
  "created_at": "Fri Sep 18 18:36:15 +0000 2020",
  "id": 1307025659294674945,
  "id_str": "1307025659294674945",
  "full_text": "Here’s an article that highlights the updates in the new Tweet payload v2 https:\/\/t.co\/oeF3ZHeKQQ",
  "truncated": false,
  "display_text_range": [
    0,
    97
  ],
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/oeF3ZHeKQQ",
        "expanded_url": "https:\/\/dev.to\/twitterdev\/understanding-the-new-tweet-payload-in-the-twitter-api-v2-1fg5",
        "display_url": "dev.to\/twitterdev\/und…",
        "indices": [
          74,
          97
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
  "in_reply_to_status_id": 1304102743196356610,
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 11,
  "favorite_count": 70,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Tweet reply












```

      {
  "created_at": "Fri Aug 21 19:10:05 +0000 2020",
  "id": 1296887316556980230,
  "id_str": "1296887316556980230",
  "text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps:\/\/t.co\/1tdA8uDWes",
  "truncated": false,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "PennMedCDH",
        "name": "Penn Med CDH",
        "id": 1615654896,
        "id_str": "1615654896",
        "indices": [
          8,
          19
        ]
      }
    ],
    "urls": [
      {
        "url": "https:\/\/t.co\/1tdA8uDWes",
        "expanded_url": "https:\/\/developer.twitter.com\/en\/use-cases\/success-stories\/penn",
        "display_url": "developer.twitter.com\/en\/use-cases\/s…",
        "indices": [
          87,
          110
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
  "in_reply_to_status_id": 1296887091901718529,
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 9,
  "favorite_count": 26,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Extended Tweet (default)












```

      {
  "created_at": "Wed Aug 19 16:26:16 +0000 2020",
  "id": 1296121314218897408,
  "id_str": "1296121314218897408",
  "text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers ca… https:\/\/t.co\/VyfXs1RTXn",
  "truncated": true,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/VyfXs1RTXn",
        "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1296121314218897408",
        "display_url": "twitter.com\/i\/web\/status\/1…",
        "indices": [
          117,
          140
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 54,
  "favorite_count": 172,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Extended Tweet (with tweet\_mode=extended)












```

      {
  "created_at": "Wed Aug 19 16:26:16 +0000 2020",
  "id": 1296121314218897408,
  "id_str": "1296121314218897408",
  "full_text": "The hide replies endpoint is launching today! \n\nDevelopers can hide replies to Tweets - a crucial way developers can help improve the health of the public conversation using the #TwitterAPI.\n\nhttps:\/\/t.co\/khXhTurm9x",
  "truncated": false,
  "display_text_range": [
    0,
    215
  ],
  "entities": {
    "hashtags": [
      {
        "text": "TwitterAPI",
        "indices": [
          178,
          189
        ]
      }
    ],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/khXhTurm9x",
        "expanded_url": "https:\/\/twittercommunity.com\/t\/hide-replies-now-available-in-the-new-twitter-api\/140996",
        "display_url": "twittercommunity.com\/t\/hide-replies…",
        "indices": [
          192,
          215
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 54,
  "favorite_count": 172,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Tweet with extended\_entities (with tweet\_mode=extended)












```

      {
  "created_at": "Wed Aug 12 17:01:42 +0000 2020",
  "id": 1293593516040269825,
  "id_str": "1293593516040269825",
  "full_text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.\n\nWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.\n\nhttps:\/\/t.co\/32VrwpGaJw https:\/\/t.co\/KaFSbjWUA8",
  "truncated": false,
  "display_text_range": [
    0,
    218
  ],
  "entities": {
    "hashtags": [
      {
        "text": "TwitterAPI",
        "indices": [
          42,
          53
        ]
      }
    ],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/32VrwpGaJw",
        "expanded_url": "https:\/\/blog.twitter.com\/developer\/en_us\/topics\/tools\/2020\/introducing_new_twitter_api.html",
        "display_url": "blog.twitter.com\/developer\/en_u…",
        "indices": [
          195,
          218
        ]
      }
    ],
    "media": [
      {
        "id": 1293565706408038401,
        "id_str": "1293565706408038401",
        "indices": [
          219,
          242
        ],
        "media_url": "http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",
        "media_url_https": "https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",
        "url": "https:\/\/t.co\/KaFSbjWUA8",
        "display_url": "pic.twitter.com\/KaFSbjWUA8",
        "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1293593516040269825\/video\/1",
        "type": "photo",
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
      }
    ]
  },
  "extended_entities": {
    "media": [
      {
        "id": 1293565706408038401,
        "id_str": "1293565706408038401",
        "indices": [
          219,
          242
        ],
        "media_url": "http:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",
        "media_url_https": "https:\/\/pbs.twimg.com\/ext_tw_video_thumb\/1293565706408038401\/pu\/img\/66P2dvbU4a02jYbV.jpg",
        "url": "https:\/\/t.co\/KaFSbjWUA8",
        "display_url": "pic.twitter.com\/KaFSbjWUA8",
        "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1293593516040269825\/video\/1",
        "type": "video",
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
        },
        "video_info": {
          "aspect_ratio": [
            16,
            9
          ],
          "duration_millis": 34875,
          "variants": [
            {
              "bitrate": 256000,
              "content_type": "video\/mp4",
              "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/480x270\/Fg9lnGGsITO0uq2K.mp4?tag=10"
            },
            {
              "bitrate": 832000,
              "content_type": "video\/mp4",
              "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/640x360\/-crbtZE4y8vKN_uF.mp4?tag=10"
            },
            {
              "content_type": "application\/x-mpegURL",
              "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/pl\/OvIqQojosF6sMIHR.m3u8?tag=10"
            },
            {
              "bitrate": 2176000,
              "content_type": "video\/mp4",
              "url": "https:\/\/video.twimg.com\/ext_tw_video\/1293565706408038401\/pu\/vid\/1280x720\/xkxyb-VPVY4OI0j9.mp4?tag=10"
            }
          ]
        },
        "additional_media_info": {
          "monetizable": false
        }
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": false,
  "retweet_count": 958,
  "favorite_count": 2850,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Retweet (default)












```

      {
  "created_at": "Tue Feb 18 19:33:59 +0000 2020",
  "id": 1229851574555508737,
  "id_str": "1229851574555508737",
  "text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",
  "truncated": false,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "suhemparack",
        "name": "Suhem Parack",
        "id": 857699969263964161,
        "id_str": "857699969263964161",
        "indices": [
          3,
          15
        ]
      }
    ],
    "urls": []
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "retweeted_status": {
    "created_at": "Tue Feb 18 19:01:58 +0000 2020",
    "id": 1229843515603144704,
    "id_str": "1229843515603144704",
    "text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it… https:\/\/t.co\/RP9NgltX7i",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https:\/\/t.co\/RP9NgltX7i",
          "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1229843515603144704",
          "display_url": "twitter.com\/i\/web\/status\/1…",
          "indices": [
            116,
            139
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 857699969263964161,
      "id_str": "857699969263964161",
      "name": "Suhem Parack",
      "screen_name": "suhemparack",
      "location": "Seattle, WA",
      "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",
      "url": "https:\/\/t.co\/8IkCzClPCz",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https:\/\/t.co\/8IkCzClPCz",
              "expanded_url": "https:\/\/developer.twitter.com",
              "display_url": "developer.twitter.com",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 738,
      "friends_count": 512,
      "listed_count": 12,
      "created_at": "Thu Apr 27 20:56:22 +0000 2017",
      "favourites_count": 365,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": false,
      "statuses_count": 460,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "F5F8FA",
      "profile_background_image_url": null,
      "profile_background_image_url_https": null,
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/857699969263964161\/1593055939",
      "profile_link_color": "1DA1F2",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": true,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "none"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 19,
    "favorite_count": 71,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "is_quote_status": false,
  "retweet_count": 19,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Retweet (with tweet\_mode=extended)












```

      {
  "created_at": "Tue Feb 18 19:33:59 +0000 2020",
  "id": 1229851574555508737,
  "id_str": "1229851574555508737",
  "full_text": "RT @suhemparack: I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out her…",
  "truncated": false,
  "display_text_range": [
    0,
    140
  ],
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "suhemparack",
        "name": "Suhem Parack",
        "id": 857699969263964161,
        "id_str": "857699969263964161",
        "indices": [
          3,
          15
        ]
      }
    ],
    "urls": []
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "retweeted_status": {
    "created_at": "Tue Feb 18 19:01:58 +0000 2020",
    "id": 1229843515603144704,
    "id_str": "1229843515603144704",
    "full_text": "I built an Alexa Skill for Twitter using APL that allows you to view Tweets and Trends on the echo show!\n\nCheck it out here 👇\n\nhttps:\/\/t.co\/l5J8wq748G",
    "truncated": false,
    "display_text_range": [
      0,
      150
    ],
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https:\/\/t.co\/l5J8wq748G",
          "expanded_url": "https:\/\/dev.to\/twitterdev\/building-an-alexa-skill-for-twitter-using-alexa-presentation-language-1aj0",
          "display_url": "dev.to\/twitterdev\/bui…",
          "indices": [
            127,
            150
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
      "id": 857699969263964161,
      "id_str": "857699969263964161",
      "name": "Suhem Parack",
      "screen_name": "suhemparack",
      "location": "Seattle, WA",
      "description": "Developer Relations for Academic Research @Twitter. Talk to me about research with Twitter data. Previously: Amazon Alexa. Views are my own",
      "url": "https:\/\/t.co\/8IkCzClPCz",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https:\/\/t.co\/8IkCzClPCz",
              "expanded_url": "https:\/\/developer.twitter.com",
              "display_url": "developer.twitter.com",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 738,
      "friends_count": 512,
      "listed_count": 12,
      "created_at": "Thu Apr 27 20:56:22 +0000 2017",
      "favourites_count": 365,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": false,
      "verified": false,
      "statuses_count": 460,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "F5F8FA",
      "profile_background_image_url": null,
      "profile_background_image_url_https": null,
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1230703695051935747\/TbQKe91L_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/857699969263964161\/1593055939",
      "profile_link_color": "1DA1F2",
      "profile_sidebar_border_color": "C0DEED",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": true,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "none"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 19,
    "favorite_count": 71,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "is_quote_status": false,
  "retweet_count": 19,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Quote Tweet (default)












```

      {
  "created_at": "Mon Nov 16 18:09:36 +0000 2020",
  "id": 1328399838128467969,
  "id_str": "1328399838128467969",
  "text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you h… https:\/\/t.co\/ahQvTYaOcZ",
  "truncated": true,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/ahQvTYaOcZ",
        "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1328399838128467969",
        "display_url": "twitter.com\/i\/web\/status\/1…",
        "indices": [
          117,
          140
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": true,
  "quoted_status_id": 1327011423252144128,
  "quoted_status_id_str": "1327011423252144128",
  "quoted_status": {
    "created_at": "Thu Nov 12 22:12:32 +0000 2020",
    "id": 1327011423252144128,
    "id_str": "1327011423252144128",
    "text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, Nove… https:\/\/t.co\/EEWN2Q9aXh",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https:\/\/t.co\/EEWN2Q9aXh",
          "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1327011423252144128",
          "display_url": "twitter.com\/i\/web\/status\/1…",
          "indices": [
            117,
            140
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
      "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
      "url": "https:\/\/t.co\/3ZX3TNiZCY",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https:\/\/t.co\/3ZX3TNiZCY",
              "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
              "display_url": "developer.twitter.com\/en\/community",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 513958,
      "friends_count": 2039,
      "listed_count": 1672,
      "created_at": "Sat Dec 14 04:35:55 +0000 2013",
      "favourites_count": 2145,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": true,
      "verified": true,
      "statuses_count": 3635,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "FFFFFF",
      "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
      "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "FFFFFF",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": false,
      "has_extended_profile": true,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 8,
    "favorite_count": 33,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "retweet_count": 7,
  "favorite_count": 29,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Quote Tweet (with tweet\_mode=extended)












```

      {
  "created_at": "Mon Nov 16 18:09:36 +0000 2020",
  "id": 1328399838128467969,
  "id_str": "1328399838128467969",
  "full_text": "As planned, the Labs v2 endpoints referenced below have now been retired. Please let us know in the forums if you have questions or need help with the Twitter API v2! https:\/\/t.co\/JaxttUMmjX",
  "truncated": false,
  "display_text_range": [
    0,
    166
  ],
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [],
    "urls": [
      {
        "url": "https:\/\/t.co\/JaxttUMmjX",
        "expanded_url": "https:\/\/twitter.com\/TwitterDev\/status\/1327011423252144128",
        "display_url": "twitter.com\/TwitterDev\/sta…",
        "indices": [
          167,
          190
        ]
      }
    ]
  },
  "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "is_quote_status": true,
  "quoted_status_id": 1327011423252144128,
  "quoted_status_id_str": "1327011423252144128",
  "quoted_status_permalink": {
    "url": "https:\/\/t.co\/JaxttUMmjX",
    "expanded": "https:\/\/twitter.com\/TwitterDev\/status\/1327011423252144128",
    "display": "twitter.com\/TwitterDev\/sta…"
  },
  "quoted_status": {
    "created_at": "Thu Nov 12 22:12:32 +0000 2020",
    "id": 1327011423252144128,
    "id_str": "1327011423252144128",
    "full_text": "👋 Friendly reminder that Twitter Developer Labs v2 hide replies and recent search will be retired next Monday, November 16! We encourage you to migrate to the new hide replies and recent search endpoints now available in the v2 #TwitterAPI. Details: https:\/\/t.co\/r6z6CI7kEy",
    "truncated": false,
    "display_text_range": [
      0,
      273
    ],
    "entities": {
      "hashtags": [
        {
          "text": "TwitterAPI",
          "indices": [
            228,
            239
          ]
        }
      ],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https:\/\/t.co\/r6z6CI7kEy",
          "expanded_url": "https:\/\/twittercommunity.com\/t\/retiring-labs-v2-recent-search-and-hide-replies\/145795",
          "display_url": "twittercommunity.com\/t\/retiring-lab…",
          "indices": [
            250,
            273
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
      "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
      "url": "https:\/\/t.co\/3ZX3TNiZCY",
      "entities": {
        "url": {
          "urls": [
            {
              "url": "https:\/\/t.co\/3ZX3TNiZCY",
              "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
              "display_url": "developer.twitter.com\/en\/community",
              "indices": [
                0,
                23
              ]
            }
          ]
        },
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 513958,
      "friends_count": 2039,
      "listed_count": 1672,
      "created_at": "Sat Dec 14 04:35:55 +0000 2013",
      "favourites_count": 2145,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": true,
      "verified": true,
      "statuses_count": 3635,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "FFFFFF",
      "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
      "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
      "profile_link_color": "0084B4",
      "profile_sidebar_border_color": "FFFFFF",
      "profile_sidebar_fill_color": "DDEEF6",
      "profile_text_color": "333333",
      "profile_use_background_image": false,
      "has_extended_profile": true,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 8,
    "favorite_count": 33,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "retweet_count": 7,
  "favorite_count": 29,
  "favorited": false,
  "retweeted": false,
  "possibly_sensitive": false,
  "possibly_sensitive_appealable": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Retweeted Quote Tweet (default)












```

      {
  "created_at": "Thu Feb 06 17:26:44 +0000 2020",
  "id": 1225470895902412800,
  "id_str": "1225470895902412800",
  "text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",
  "truncated": false,
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "AureliaSpecker",
        "name": "Aurelia Specker",
        "id": 1102321381,
        "id_str": "1102321381",
        "indices": [
          3,
          18
        ]
      }
    ],
    "urls": []
  },
  "source": "<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "retweeted_status": {
    "created_at": "Tue Feb 04 15:01:25 +0000 2020",
    "id": 1224709550214873090,
    "id_str": "1224709550214873090",
    "text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that u… https:\/\/t.co\/cAepHunkFp",
    "truncated": true,
    "entities": {
      "hashtags": [],
      "symbols": [],
      "user_mentions": [],
      "urls": [
        {
          "url": "https:\/\/t.co\/cAepHunkFp",
          "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1224709550214873090",
          "display_url": "twitter.com\/i\/web\/status\/1…",
          "indices": [
            117,
            140
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
      "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
      "url": null,
      "entities": {
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 1036,
      "friends_count": 1330,
      "listed_count": 26,
      "created_at": "Fri Jan 18 23:45:43 +0000 2013",
      "favourites_count": 4990,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": true,
      "verified": false,
      "statuses_count": 855,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "8B542B",
      "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
      "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",
      "profile_link_color": "5E341C",
      "profile_sidebar_border_color": "D9B17E",
      "profile_sidebar_fill_color": "EADEAA",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "none"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": true,
    "quoted_status_id": 1195000047089389573,
    "quoted_status_id_str": "1195000047089389573",
    "quoted_status": {
      "created_at": "Thu Nov 14 15:26:27 +0000 2019",
      "id": 1195000047089389573,
      "id_str": "1195000047089389573",
      "text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial… https:\/\/t.co\/pL0qJ4vhtE",
      "truncated": true,
      "entities": {
        "hashtags": [
          {
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
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https:\/\/t.co\/pL0qJ4vhtE",
            "expanded_url": "https:\/\/twitter.com\/i\/web\/status\/1195000047089389573",
            "display_url": "twitter.com\/i\/web\/status\/1…",
            "indices": [
              116,
              139
            ]
          }
        ]
      },
      "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
        "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
        "url": null,
        "entities": {
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 1036,
        "friends_count": 1330,
        "listed_count": 26,
        "created_at": "Fri Jan 18 23:45:43 +0000 2013",
        "favourites_count": 4990,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": true,
        "verified": false,
        "statuses_count": 855,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "8B542B",
        "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
        "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
        "profile_background_tile": false,
        "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
        "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
        "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",
        "profile_link_color": "5E341C",
        "profile_sidebar_border_color": "D9B17E",
        "profile_sidebar_fill_color": "EADEAA",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": false,
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "none"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 31,
      "favorite_count": 123,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    },
    "retweet_count": 12,
    "favorite_count": 43,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "is_quote_status": true,
  "quoted_status_id": 1195000047089389573,
  "quoted_status_id_str": "1195000047089389573",
  "retweet_count": 12,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
}
    
```





Code copied to clipboard








### Retweeted Quote Tweet (with tweet\_mode=extended)












```

      {
  "created_at": "Thu Feb 06 17:26:44 +0000 2020",
  "id": 1225470895902412800,
  "id_str": "1225470895902412800",
  "full_text": "RT @AureliaSpecker: 📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses…",
  "truncated": false,
  "display_text_range": [
    0,
    139
  ],
  "entities": {
    "hashtags": [],
    "symbols": [],
    "user_mentions": [
      {
        "screen_name": "AureliaSpecker",
        "name": "Aurelia Specker",
        "id": 1102321381,
        "id_str": "1102321381",
        "indices": [
          3,
          18
        ]
      }
    ],
    "urls": []
  },
  "source": "<a href=\"http:\/\/twitter.com\/download\/iphone\" rel=\"nofollow\">Twitter for iPhone<\/a>",
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
    "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
    "url": "https:\/\/t.co\/3ZX3TNiZCY",
    "entities": {
      "url": {
        "urls": [
          {
            "url": "https:\/\/t.co\/3ZX3TNiZCY",
            "expanded_url": "https:\/\/developer.twitter.com\/en\/community",
            "display_url": "developer.twitter.com\/en\/community",
            "indices": [
              0,
              23
            ]
          }
        ]
      },
      "description": {
        "urls": []
      }
    },
    "protected": false,
    "followers_count": 513958,
    "friends_count": 2039,
    "listed_count": 1672,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "favourites_count": 2145,
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "verified": true,
    "statuses_count": 3635,
    "lang": null,
    "contributors_enabled": false,
    "is_translator": false,
    "is_translation_enabled": false,
    "profile_background_color": "FFFFFF",
    "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png",
    "profile_background_tile": false,
    "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1283786620521652229\/lEODkLTh_normal.jpg",
    "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/2244994945\/1594913664",
    "profile_link_color": "0084B4",
    "profile_sidebar_border_color": "FFFFFF",
    "profile_sidebar_fill_color": "DDEEF6",
    "profile_text_color": "333333",
    "profile_use_background_image": false,
    "has_extended_profile": true,
    "default_profile": false,
    "default_profile_image": false,
    "following": null,
    "follow_request_sent": null,
    "notifications": null,
    "translator_type": "regular"
  },
  "geo": null,
  "coordinates": null,
  "place": null,
  "contributors": null,
  "retweeted_status": {
    "created_at": "Tue Feb 04 15:01:25 +0000 2020",
    "id": 1224709550214873090,
    "id_str": "1224709550214873090",
    "full_text": "📣 If you enjoyed the London commute tutorial I wrote in November last year, check out the refactored version that uses Twitter's new search endpoint 🚇 https:\/\/t.co\/87XIPZmZBJ\n\n#DEVcommunity #Pythontutorial @TwitterDev @TwitterAPI https:\/\/t.co\/dXrJYvn3hY",
    "truncated": false,
    "display_text_range": [
      0,
      229
    ],
    "entities": {
      "hashtags": [
        {
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
      "symbols": [],
      "user_mentions": [
        {
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
      "urls": [
        {
          "url": "https:\/\/t.co\/87XIPZmZBJ",
          "expanded_url": "https:\/\/bit.ly\/2OrnrCC",
          "display_url": "bit.ly\/2OrnrCC",
          "indices": [
            151,
            174
          ]
        },
        {
          "url": "https:\/\/t.co\/dXrJYvn3hY",
          "expanded_url": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",
          "display_url": "twitter.com\/AureliaSpecker…",
          "indices": [
            230,
            253
          ]
        }
      ]
    },
    "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
      "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
      "url": null,
      "entities": {
        "description": {
          "urls": []
        }
      },
      "protected": false,
      "followers_count": 1036,
      "friends_count": 1330,
      "listed_count": 26,
      "created_at": "Fri Jan 18 23:45:43 +0000 2013",
      "favourites_count": 4990,
      "utc_offset": null,
      "time_zone": null,
      "geo_enabled": true,
      "verified": false,
      "statuses_count": 855,
      "lang": null,
      "contributors_enabled": false,
      "is_translator": false,
      "is_translation_enabled": false,
      "profile_background_color": "8B542B",
      "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
      "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
      "profile_background_tile": false,
      "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
      "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
      "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",
      "profile_link_color": "5E341C",
      "profile_sidebar_border_color": "D9B17E",
      "profile_sidebar_fill_color": "EADEAA",
      "profile_text_color": "333333",
      "profile_use_background_image": true,
      "has_extended_profile": false,
      "default_profile": false,
      "default_profile_image": false,
      "following": null,
      "follow_request_sent": null,
      "notifications": null,
      "translator_type": "none"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": true,
    "quoted_status_id": 1195000047089389573,
    "quoted_status_id_str": "1195000047089389573",
    "quoted_status_permalink": {
      "url": "https:\/\/t.co\/dXrJYvn3hY",
      "expanded": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",
      "display": "twitter.com\/AureliaSpecker…"
    },
    "quoted_status": {
      "created_at": "Thu Nov 14 15:26:27 +0000 2019",
      "id": 1195000047089389573,
      "id_str": "1195000047089389573",
      "full_text": "I wrote a tutorial on how to get bespoke commute information using the Twitter API🚇\n\n#DEVcommunity #Pythontutorial \n\nCheck it out here 👇\nhttps:\/\/t.co\/sOjXW4YhbN",
      "truncated": false,
      "display_text_range": [
        0,
        160
      ],
      "entities": {
        "hashtags": [
          {
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
        "symbols": [],
        "user_mentions": [],
        "urls": [
          {
            "url": "https:\/\/t.co\/sOjXW4YhbN",
            "expanded_url": "https:\/\/dev.to\/twitterdev\/using-the-twitter-api-to-make-your-commute-easier-3od0",
            "display_url": "dev.to\/twitterdev\/usi…",
            "indices": [
              137,
              160
            ]
          }
        ]
      },
      "source": "<a href=\"https:\/\/mobile.twitter.com\" rel=\"nofollow\">Twitter Web App<\/a>",
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
        "description": "devrel @TwitterUK • Swiss in London • mother of houseplants • personal hairdresser to @_dormrod",
        "url": null,
        "entities": {
          "description": {
            "urls": []
          }
        },
        "protected": false,
        "followers_count": 1036,
        "friends_count": 1330,
        "listed_count": 26,
        "created_at": "Fri Jan 18 23:45:43 +0000 2013",
        "favourites_count": 4990,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": true,
        "verified": false,
        "statuses_count": 855,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "8B542B",
        "profile_background_image_url": "http:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
        "profile_background_image_url_https": "https:\/\/abs.twimg.com\/images\/themes\/theme8\/bg.gif",
        "profile_background_tile": false,
        "profile_image_url": "http:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
        "profile_image_url_https": "https:\/\/pbs.twimg.com\/profile_images\/1137517534104772608\/8FBYgc6G_normal.jpg",
        "profile_banner_url": "https:\/\/pbs.twimg.com\/profile_banners\/1102321381\/1587552672",
        "profile_link_color": "5E341C",
        "profile_sidebar_border_color": "D9B17E",
        "profile_sidebar_fill_color": "EADEAA",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": false,
        "default_profile": false,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null,
        "translator_type": "none"
      },
      "geo": null,
      "coordinates": null,
      "place": null,
      "contributors": null,
      "is_quote_status": false,
      "retweet_count": 31,
      "favorite_count": 123,
      "favorited": false,
      "retweeted": false,
      "possibly_sensitive": false,
      "possibly_sensitive_appealable": false,
      "lang": "en"
    },
    "retweet_count": 12,
    "favorite_count": 43,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "possibly_sensitive_appealable": false,
    "lang": "en"
  },
  "is_quote_status": true,
  "quoted_status_id": 1195000047089389573,
  "quoted_status_id_str": "1195000047089389573",
  "quoted_status_permalink": {
    "url": "https:\/\/t.co\/dXrJYvn3hY",
    "expanded": "https:\/\/twitter.com\/AureliaSpecker\/status\/1195000047089389573",
    "display": "twitter.com\/AureliaSpecker…"
  },
  "retweet_count": 12,
  "favorite_count": 0,
  "favorited": false,
  "retweeted": false,
  "lang": "en"
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















