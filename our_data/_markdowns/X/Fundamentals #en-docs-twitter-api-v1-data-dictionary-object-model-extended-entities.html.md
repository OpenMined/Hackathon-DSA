
Extended entities object | Docs | Twitter Developer Platform 

Extended entities object

Twitter extended entities
-------------------------

 Jump to on this page

Introduction

Extended Entities object

Example Tweets and JSON payloads

  - Tweet with four native photos

  - Tweet with native video

  - Tweet with an animated GIF

Next Steps

Introduction
------------

If a Tweet contains native media (shared with the Tweet user-interface as opposed via a link to elsewhere), there will also be a extended\_entities section. When it comes to any native media (photo, video, or GIF), the extended\_entities is the preferred metadata source for several reasons. Currently, up to four photos can be attached to a Tweet. The entities metadata will only contain the first photo (until 2014, only one photo could be included), while the extended\_entities section will include all attached photos. With native media, another deficiency of the entities.media metadata is that the media type will always indicate ‘photo’, even in cases where the attached media is a video or animated GIF. The actual type of media is specified in the extended\_entities.media[].type attribute and is set to either *photo*, *video*, or *animated\_gif*. For these reasons, if you are working with native media, the extended\_entities metadata is the way to go.

All Tweets with attached photos, videos and animated GIFs will include an `extended_entities` JSON object. The `extended_entities` object contains a single `media` array of `media` objects (see the `entities` section for its data dictionary). No other entity types, such as hashtags and links, are included in the `extended_entities` section. The `media` object in the `extended_entities` section is identical in structure to the one included in the `entities` section.  

Tweets can only have one type of media attached to it. For photos, up to four photos can be attached. For videos and GIFs, one can be attached. Since the media `type` metadata in the `extended_entities` section correctly indicates the media type (‘photo’, ‘video’ or ‘animated\_gif’), and supports up to 4 photos, it is the preferred metadata source for native media.

```
{
  "extended_entities": {
    "media": [
    ]
  }
}
```

Example Tweets and JSON payloads
--------------------------------

Below are some example Tweets and their associated entities metadata.

Tweet with four native photos

Tweet with hashtag, user mention, cashtag, URL, and four native photos:

> Test Tweet with @mentionThis $twtr https://t.co/RzmrQ6wAzD #hashtag pic.twitter.com/9r69akA484
> 
> 
> — @FloodSocial (@FloodSocial) May 8, 2017

Here is the `entities` section for this Tweet:

```
{
  "entities": {
    "hashtags": [
      {
        "text": "hashtag",
        "indices": [
          59,
          67
        ]
      }
    ],
    "urls": [
      {
        "url": "https://t.co/RzmrQ6wAzD",
        "expanded_url": "http://bit.ly/2pUk4be",
        "display_url": "bit.ly/2pUk4be",
        "unwound": {
          "url": "https://blog.gnip.com/tweeting-in-the-rain/",
          "status": 200,
          "title": "Tweeting in the Rain, Part 1 - Gnip Blog - Social Data and Data Science Blog",
          "description": "If you would have told me a few years ago that one day I’d be comparing precipitation and social media time-series data, I would have assumed you were joking.  For 13 years at OneRain I helped develop software and monitoring … Continue reading →"
        },
        "indices": [
          35,
          58
        ]
      }
    ],
    "user_mentions": [
      {
        "screen_name": "MentionThis",
        "name": "Just Me",
        "id": 50247739,
        "id_str": "50247739",
        "indices": [
          16,
          28
        ]
      }
    ],
    "symbols": [
      {
        "text": "twtr",
        "indices": [
          29,
          34
        ]
      }
    ],
    "media": [
      {
        "id": 861627472244162561,
        "id_str": "861627472244162561",
        "indices": [
          68,
          91
        ],
        "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
        "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
        "url": "https://t.co/9r69akA484",
        "display_url": "pic.twitter.com/9r69akA484",
        "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
        "type": "photo",
        "sizes": {
          "medium": {
            "w": 1200,
            "h": 900,
            "resize": "fit"
          },
          "small": {
            "w": 680,
            "h": 510,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "large": {
            "w": 2048,
            "h": 1536,
            "resize": "fit"
          }
        }
      }
    ]
  }
}
```
Only in this ‘extended’ payload below will you find the four (maximum) native photos. Notice that the first photo in the array is the same as the single photo included in the non-extended Twitter *entities* section. The *media* metadata structure for photos is the same for both *entities* and *extended\_entities* sections.

Here is the `extented_entities` section for this Tweet:

```
{
"extended_entities": {
    "media": [
      {
        "id": 861627472244162561,
        "id_str": "861627472244162561",
        "indices": [
          68,
          91
        ],
        "media_url": "http://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
        "media_url_https": "https://pbs.twimg.com/media/C_UdnvPUwAE3Dnn.jpg",
        "url": "https://t.co/9r69akA484",
        "display_url": "pic.twitter.com/9r69akA484",
        "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
        "type": "photo",
        "sizes": {
          "medium": {
            "w": 1200,
            "h": 900,
            "resize": "fit"
          },
          "small": {
            "w": 680,
            "h": 510,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "large": {
            "w": 2048,
            "h": 1536,
            "resize": "fit"
          }
        }
      },
      {
        "id": 861627472244203520,
        "id_str": "861627472244203520",
        "indices": [
          68,
          91
        ],
        "media_url": "http://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
        "media_url_https": "https://pbs.twimg.com/media/C_UdnvPVYAAZbEs.jpg",
        "url": "https://t.co/9r69akA484",
        "display_url": "pic.twitter.com/9r69akA484",
        "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
        "type": "photo",
        "sizes": {
          "small": {
            "w": 680,
            "h": 680,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "medium": {
            "w": 1200,
            "h": 1200,
            "resize": "fit"
          },
          "large": {
            "w": 2048,
            "h": 2048,
            "resize": "fit"
          }
        }
      },
      {
        "id": 861627474144149504,
        "id_str": "861627474144149504",
        "indices": [
          68,
          91
        ],
        "media_url": "http://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
        "media_url_https": "https://pbs.twimg.com/media/C_Udn2UUQAADZIS.jpg",
        "url": "https://t.co/9r69akA484",
        "display_url": "pic.twitter.com/9r69akA484",
        "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
        "type": "photo",
        "sizes": {
          "medium": {
            "w": 1200,
            "h": 900,
            "resize": "fit"
          },
          "small": {
            "w": 680,
            "h": 510,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "large": {
            "w": 2048,
            "h": 1536,
            "resize": "fit"
          }
        }
      },
      {
        "id": 861627474760708096,
        "id_str": "861627474760708096",
        "indices": [
          68,
          91
        ],
        "media_url": "http://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
        "media_url_https": "https://pbs.twimg.com/media/C_Udn4nUMAAgcIa.jpg",
        "url": "https://t.co/9r69akA484",
        "display_url": "pic.twitter.com/9r69akA484",
        "expanded_url": "https://twitter.com/FloodSocial/status/861627479294746624/photo/1",
        "type": "photo",
        "sizes": {
          "small": {
            "w": 680,
            "h": 680,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "medium": {
            "w": 1200,
            "h": 1200,
            "resize": "fit"
          },
          "large": {
            "w": 2048,
            "h": 2048,
            "resize": "fit"
          }
        }
      }
    ]
  }
}
```

Tweet with native video
-----------------------

Below is the extended entities metadata for this Tweet with a video:

> St. Vrain River @ Crane Hollow pic.twitter.com/TLSTTOvvmP
> 
> 
> — @FloodSocial demo (@FloodSocial) May 29, 2017

```
{
  "extended_entities": {
    "media": [
      {
        "id": 869317980307415040,
        "id_str": "869317980307415040",
        "indices": [
          31,
          54
        ],
        "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
        "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
        "url": "https://t.co/TLSTTOvvmP",
        "display_url": "pic.twitter.com/TLSTTOvvmP",
        "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
        "type": "video",
        "sizes": {
          "small": {
            "w": 340,
            "h": 604,
            "resize": "fit"
          },
          "large": {
            "w": 720,
            "h": 1280,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "medium": {
            "w": 600,
            "h": 1067,
            "resize": "fit"
          }
        },
        "video_info": {
          "aspect_ratio": [
            9,
            16
          ],
          "duration_millis": 10704,
          "variants": [
            {
              "bitrate": 320000,
              "content_type": "video/mp4",
              "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/180x320/FMei8yCw7yc_Z7e-.mp4"
            },
            {
              "bitrate": 2176000,
              "content_type": "video/mp4",
              "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/720x1280/octt5pFbISkef8RB.mp4"
            },
            {
              "bitrate": 832000,
              "content_type": "video/mp4",
              "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/vid/360x640/2OmqK74SQ9jNX8mZ.mp4"
            },
            {
              "content_type": "application/x-mpegURL",
              "url": "https://video.twimg.com/ext_tw_video/869317980307415040/pu/pl/wcJQJ2nxiFU4ZZng.m3u8"
            }
          ]
        }
      }
    ]
  }
}
```
When an advertiser chooses to limit video playback to just Twitter owned and operated platforms, the `video_info` object will be replaced with an `additional_media_info` object.  

The `additional_media_info` will contain additional media info provided by the publisher, such as `title`, `description` and `embeddable flag`. Video content is made available only to Twitter official clients when `embeddable=false`. In this case, all video URLs provided in the payload will be Twitter-based, so the user can open the video in a Twitter owned property by clicking the link.  

Here is an example of what the extended entities object will look like in this situation:

```
{
  "extended_entities": {
    "media": [
      {
        "id": 924685332347469824,
        "id_str": "924685332347469824",
        "indices": [
          49,
          72
        ],
        "media_url": "http://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
        "media_url_https": "https://pbs.twimg.com/media/DNUkdLMVwAEzj8K.jpg",
        "url": "https://t.co/90xOJqKMox",
        "display_url": "pic.twitter.com/90xOJqKMox",
        "expanded_url": "https://twitter.com/nyjets/status/924685391524798464/video/1",
        "type": "photo",
        "sizes": {
          "small": {
            "w": 680,
            "h": 383,
            "resize": "fit"
          },
          "medium": {
            "w": 1200,
            "h": 675,
            "resize": "fit"
          },
          "large": {
            "w": 1280,
            "h": 720,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          }
        },
        "additional_media_info": {
          "title": "#ATLvsNYJ: Tomlinson TD from McCown",
          "description": "NFL",
          "embeddable": false,
          "monetizable": true
        }
      }
    ]
  }
}

```
As discussed above, here is the `entities` section that incorrectly has the `type` set to ‘photo’. Again, the `extended_entities` section is preferred for all native media types, including ‘video’ and ‘animated\_gif’.

```
{
"entities": {
    "hashtags": [
    ],
    "urls": [
    ],
    "user_mentions": [
    ],
    "symbols": [
    ],
    "media": [
      {
        "id": 869317980307415040,
        "id_str": "869317980307415040",
        "indices": [
          31,
          54
        ],
        "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
        "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/869317980307415040/pu/img/t_E6wyADk_PvxuzF.jpg",
        "url": "https://t.co/TLSTTOvvmP",
        "display_url": "pic.twitter.com/TLSTTOvvmP",
        "expanded_url": "https://twitter.com/FloodSocial/status/869318041078820864/video/1",
        "type": "photo",
        "sizes": {
          "small": {
            "w": 340,
            "h": 604,
            "resize": "fit"
          },
          "large": {
            "w": 720,
            "h": 1280,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "medium": {
            "w": 600,
            "h": 1067,
            "resize": "fit"
          }
        }
      }
    ]
  }
}
```

Tweet with an animated GIF
--------------------------

Below is the extended entities metadata for this Tweet with an animated GIF:

> Test Tweet with animated GIF pic.twitter.com/nD6G4bWSKb
> 
> 
> — @FloodSocial demo (@FloodSocial) May 31, 2017

```
{
  "extended_entities": {
    "media": [
      {
        "id": 870042654213459968,
        "id_str": "870042654213459968",
        "indices": [
          29,
          52
        ],
        "media_url": "http://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
        "media_url_https": "https://pbs.twimg.com/tweet_video_thumb/DBMDLy_U0AAqUWP.jpg",
        "url": "https://t.co/nD6G4bWSKb",
        "display_url": "pic.twitter.com/nD6G4bWSKb",
        "expanded_url": "https://twitter.com/FloodSocial/status/870042717589340160/photo/1",
        "type": "animated_gif",
        "sizes": {
          "medium": {
            "w": 350,
            "h": 262,
            "resize": "fit"
          },
          "small": {
            "w": 340,
            "h": 255,
            "resize": "fit"
          },
          "thumb": {
            "w": 150,
            "h": 150,
            "resize": "crop"
          },
          "large": {
            "w": 350,
            "h": 262,
            "resize": "fit"
          }
        },
        "video_info": {
          "aspect_ratio": [
            175,
            131
          ],
          "variants": [
            {
              "bitrate": 0,
              "content_type": "video/mp4",
              "url": "https://video.twimg.com/tweet_video/DBMDLy_U0AAqUWP.mp4"
            }
          ]
        }
      }
    ]
  }
}
```

Next steps
----------

Explore other Tweet JSON objects and data dictionaries:

* Entities object and data dictionary
* Tweet object and data dictionary
* User object and data dictionary
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