



Media object | Docs | Twitter Developer Platform 





































































































Media object



Media
-----


Media refers to any image, GIF, or video attached to a Tweet. The media object is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 


The object is available for expansion with `?expansions=attachments.media_keys` to get the condensed object with only default fields. Use the expansion with the field parameter: `media.fields` when requesting additional fields to complete the object.


 




| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| media\_key (default) | string | Unique identifier of the expanded media content.
`"media_key": "13_1263145212760805376"` | Can be used to programmatically retrieve media |
| type (default) | string | Type of content (animated\_gif, photo, video).
`"type": "video"` | Classify the media as a photo, GIF, or video |
| url | string | A direct URL to the media file on Twitter. | Returns a Media object with a URL field for photos |
| duration\_ms | integer | Available when type is video. Duration in milliseconds of the video.
`"duration_ms": 46947` |  |
| height | integer | Height of this content in pixels.
`"height": 1080` |  |
| non\_public\_metrics | object | Non-public engagement metrics for the media content at the time of the request. 
Requires user context authentication.
`"non_public_metrics": {
          "playback_0_count": 1561,
          "playback_100_count": 116,
          "playback_25_count": 559,
          "playback_50_count": 305,
          "playback_75_count": 183,
        }` | Determine video engagement: how many users played through to each quarter of the video. |
| organic\_metrics | object
 | Engagement metrics for the media content, tracked in an organic context, at the time of the request. 
Requires user context authentication.
`"organic_metrics": {
          "playback_0_count": 1561,
          "playback_100_count": 116,
          "playback_25_count": 559,
          "playback_50_count": 305,
          "playback_75_count": 183,
          "view_count": 629
        }` | Determine organic media engagement. |
| preview\_image\_url | string | URL to the static placeholder preview of this content.
`"preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg"`
 |  |
| promoted\_metrics | object | Engagement metrics for the media content, tracked in a promoted context, at the time of the request. 
Requires user context authentication.
`"promoted_metrics": {
          "playback_0_count": 259, 
          "playback_100_count": 15, 
          "playback_25_count": 113,
          "playback_50_count": 57,
          "playback_75_count": 25,
          "view_count": 124
        }` | Determine media engagement when the Tweet was promoted. |
| public\_metrics | object | Public engagement metrics for the media content at the time of the request.
`"public_metrics": {
          "view_count": 6865141
        }` | Determine total number of views for the video attached to the Tweet. |
| width | integer | Width of this content in pixels.
`"width": 1920` |  |
| alt\_text | string | A description of an image to enable and support accessibility. Can be up to 1000 characters long. Alt text can only be added to images at the moment. 
"alt\_text": “Rugged hills along the Na Pali coast on the island of Kauai” | Can be used to provide a written description of an image in case a user is visually impaired. |
| variants | array | Each media object may have multiple display or playback variants, with different resolutions or formats
`"variants": [`
`{
      "bit_rate": 632000,
      "content_type":"video/mp4",
      "url": "https://video.twimg.com/ext_tw_video/1527322141724532740/pu/vid/320x568/lnBaR2hCqE-R_90a.mp4?tag=12"
     }`
`]` |  |


### 


### Retrieving a media object


#### Sample Request


In the following request, we are requesting fields for the media object attached to the Tweet on the Tweet lookup endpoint. Since media is a child object of a Tweet, the `attachment.media_keys` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

 












```

      curl --request GET 'https://api.twitter.com/2/tweets?ids=1263145271946551300&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








 **Sample Response**












```

      {
    "data": [
        {
            "text": "Testing, testing...\n\nA new way to have a convo with exactly who you want. We’re starting with a small % globally, so keep your 👀 out to see it in action. https://t.co/pV53mvjAVT",
            "id": "1263145271946551300",
            "attachments": {
                "media_keys": [
                    "13_1263145212760805376"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "duration_ms": 46947,
                "type": "video",
                "height": 1080,
                "media_key": "13_1263145212760805376",
                "public_metrics": {
                    "view_count": 6909260
                },
                "preview_image_url": "https://pbs.twimg.com/media/EYeX7akWsAIP1_1.jpg",
                "width": 1920
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















