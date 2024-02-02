



GET collections/entries | Docs | Twitter Developer Platform 





































































































GET collections/entries



get-collections-entries

GET collections/entries
=======================




Retrieve the identified Collection, presented as a list of the Tweets
curated within.


The response structure of this method differs significantly from
timelines you may be used to working with elsewhere in the Twitter
API.


To navigate a Collection, use the position object of a response,
which includes attributes for `max_position`,
`min_position`, and `was_truncated`.
`was_truncated` indicates whether additional Tweets exist in
the collection outside of the range of the current request. To retrieve
Tweets further back in time, use the value of `min_position`
found in the current response as the `max_position` parameter
in the next call to this endpoint.


Resource URL¶
-------------


`https://api.twitter.com/1.1/collections/entries.json`


Resource Information¶
---------------------




|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 1000 |


Parameters¶
-----------




|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The identifier of the Collection for which to return results. |  | *custom-539487832448843776* |
| count | optional | Specifies the *maximum* number of results to include in the
response. Specify a count between 1 and 200. A *next\_cursor*
value will be provided in the response if additional results are
available. |  | *100* |
| max\_position | optional | Returns results with a position value less than or equal to the
specified position. |  | *54321* |
| min\_position | optional | Returns results with a position greater than the specified
position. |  | *12345* |


Example Request¶
----------------


`GET https://api.twitter.com/1.1/collections/entries.json?id=custom-539487832448843776`


Example Response¶
-----------------



```
{
  "objects": {
    "timelines": {
      "custom-539487832448843776": {
        "collection_type": "user",
        "collection_url": "https://twitter.com/TwitterDev/timelines/539487832448843776",
        "description": "A collection of Tweets about National Parks in the United States.",
        "name": "National Park Tweets",
        "timeline_order": "curation_reverse_chron",
        "url": "",
        "user_id": "2244994945",
        "visibility": "public"
      }
    },
    "tweets": {
      "504032379045179393": {
        "contributors": null,
        "coordinates": null,
        "created_at": "Mon Aug 25 22:27:38 +0000 2014",
        "entities": {
          "hashtags": [],
          "media": [
            {
              "display_url": "pic.twitter.com/HtdvV0bPEu",
              "expanded_url": "http://twitter.com/Interior/status/504032379045179393/photo/1",
              "id": 504032378411446273,
              "id_str": "504032378411446273",
              "indices": [
                99,
                121
              ],
              "media_url": "http://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
              "media_url_https": "https://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
              "sizes": {
                "large": {
                  "h": 695,
                  "resize": "fit",
                  "w": 1024
                },
                "medium": {
                  "h": 407,
                  "resize": "fit",
                  "w": 600
                },
                "small": {
                  "h": 230,
                  "resize": "fit",
                  "w": 340
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "type": "photo",
              "url": "http://t.co/HtdvV0bPEu"
            }
          ],
          "symbols": [],
          "urls": [],
          "user_mentions": [
            {
              "id": 66453289,
              "id_str": "66453289",
              "indices": [
                47,
                60
              ],
              "name": "Lake Clark NP&P",
              "screen_name": "LakeClarkNPS"
            }
          ]
        },
        "extended_entities": {
          "media": [
            {
              "display_url": "pic.twitter.com/HtdvV0bPEu",
              "expanded_url": "http://twitter.com/Interior/status/504032379045179393/photo/1",
              "id": 504032378411446273,
              "id_str": "504032378411446273",
              "indices": [
                99,
                121
              ],
              "media_url": "http://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
              "media_url_https": "https://pbs.twimg.com/media/Bv6uxxaCcAEjWHD.jpg",
              "sizes": {
                "large": {
                  "h": 695,
                  "resize": "fit",
                  "w": 1024
                },
                "medium": {
                  "h": 407,
                  "resize": "fit",
                  "w": 600
                },
                "small": {
                  "h": 230,
                  "resize": "fit",
                  "w": 340
                },
                "thumb": {
                  "h": 150,
                  "resize": "crop",
                  "w": 150
                }
              },
              "type": "photo",
              "url": "http://t.co/HtdvV0bPEu"
            }
          ]
        },
        "favorite_count": 639,
        "favorited": false,
        "geo": null,
        "id": 504032379045179393,
        "id_str": "504032379045179393",
        "in_reply_to_screen_name": null,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "is_quote_status": false,
        "lang": "en",
        "place": null,
        "possibly_sensitive": false,
        "retweet_count": 606,
        "retweeted": false,
        "source": "Twitter for iPhone",
        "text": "How about a grizzly bear waving for the camera @LakeClarkNPS to end the day? Photo: Kevin Dietrich http://t.co/HtdvV0bPEu",
        "truncated": false,
        "user": {
          "id": 76348185,
          "id_str": "76348185"
        }
      }
  },
  "response": {
    "position": {
      "max_position": "371578415352947200",
      "min_position": "371578380871797248",
      "was_truncated": false
    },
    "timeline": [
      {
        "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
        "tweet": {
          "id": "504032379045179393",
          "sort_index": "371578415352947200"
        }
      },
      {
        "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
        "tweet": {
          "id": "532654992071852032",
          "sort_index": "371578393139797760"
        }
      },
      {
        "feature_context": "HBgGY3VzdG9tFoCAktzo1NL8DgAA",
        "tweet": {
          "id": "524573263163572224",
          "sort_index": "371578380871797248"
        }
      }
    ],
    "timeline_id": "custom-539487832448843776"
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















