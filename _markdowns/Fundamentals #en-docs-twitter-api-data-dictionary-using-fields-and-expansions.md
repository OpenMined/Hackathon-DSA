



Using fields and expansions | Docs | Twitter Developer Platform 





































































































Using fields and expansions



How to use fields and expansions
--------------------------------


By default, the Twitter API v2 data objects include a small number of default fields when making a request without the use of the fields or expansions parameters. This guide will show you how to use the `fields` and `expansions` query parameters in your request to receive additional objects and fields in your response.


In this guide, we will be requesting several fields in the following Tweet screenshot.  

 





























As you can see in the screenshot, there are several visible pieces of information related to the Tweet, including the Tweet author, Tweet metrics, created timestamp, video, and video view count. There are also several pieces of data that are not visible within the screenshot, but are still available to request. 


When making a request to the API, the default response is simple, containing only the default Tweet fields (id and text). You will also only receive the primary object that returns with the given endpoint that you are using, and not any of the associated data objects that might relate to the primary object.


This simplicity, along with the fields and expansions parameters, enable you to request only those fields you require, depending on your use case.   

  


### Requesting additional fields and objects.


First off, we will be requesting a Tweet object using a Tweet ID and the GET /tweets endpoint.  




Request:












```

      curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








Response:












```

      {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y"
        }
    ]
}
    
```






 


The following step-by-step guide will show you how to retrieve the additional data we can see in the screenshot.  




1. Identify the additional fields that you would like to request by using our object model, or by reviewing the list of fields in the endpoints’ API reference pages.  

  

In this case, we will be requesting the following additional fields:  

attachments, author\_id, created\_at, public\_metrics, and source.
2. Build the `tweet.fields` query parameter with the above fields as its value using a comma-separated list:  

`?tweet.fields=attachments,author_id,created_at,public_metrics,source`
3. Add the query parameter to the GET /tweets request that you made earlier.


 


Request:












```

      curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








  

Response:  

 












```

      {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "author_id": "783214",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "source": "Sprinklr",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            },
            "created_at": "2020-05-12T19:44:51.000Z"
        }
    ]
}
    
```






  

4. Next, we are going to request fields related to the video that was included in the Tweet. To do so, we will use the `expansions` parameter with `attachments.media_keys` as the value, and add this to the request.


?expansions=attachments.media\_keys


Request:  

 












```

      curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








  

Response, with the media object represented in the includes object:  

 












```

      {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "created_at": "2020-05-12T19:44:51.000Z",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            },
            "author_id": "783214",
            "source": "Sprinklr"
        }
    ],
    "includes": {
        "media": [
            {
                "media_key": "13_1260294804770041858",
                "type": "video"
            }
        ]
    }
}
    
```






  

5. And finally, we are going to request the view count and duration of the video. These aren’t default fields so we have to specifically request them. Use the `media.fields` parameter with the comma-separated values, `public_metrics` and `duration_ms` in your request.


?media.fields=public\_metrics,duration\_ms


  

Request:  

 












```

      curl --request GET --url 'https://api.twitter.com/2/tweets?ids=1260294888811347969&tweet.fields=attachments,author_id,created_at,public_metrics,source&expansions=attachments.media_keys&media.fields=duration_ms,public_metrics' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








  

Response, which now includes all the data that can be seen in the Tweet screenshot:  

 












```

      {
    "data": [
        {
            "id": "1260294888811347969",
            "text": "Don’t miss the Tweets about your Tweet. \n\nNow on iOS, you can see Retweets with comments all in one place. https://t.co/oanjZfzC6y",
            "author_id": "783214",
            "public_metrics": {
                "retweet_count": 5219,
                "reply_count": 1828,
                "like_count": 17141,
                "quote_count": 3255
            },
            "created_at": "2020-05-12T19:44:51.000Z",
            "source": "Sprinklr",
            "attachments": {
                "media_keys": [
                    "13_1260294804770041858"
                ]
            }
        }
    ],
    "includes": {
        "media": [
            {
                "duration_ms": 36503,
                "media_key": "13_1260294804770041858",
                "public_metrics": {
                    "view_count": 1534703
                },
                "type": "video"
            }
        ]
    }
}
    
```









In total, we included the following parameters in this example:


* ids=1260294888811347969
* tweet.fields=attachments,author\_id,created\_at,public\_metrics,source
* expansions=attachments.media\_keys
* media.fields=public\_metrics,duration\_ms


When tied together, here is what the full query string looks like:


?ids=1260294888811347969&tweet.fields=attachments,author\_id,created\_at,public\_metrics,source&expansions=attachments.media\_keys&media.fields=public\_metrics,duration\_ms


 






Next steps
----------






Try building a query string on your own with the tweets lookup endpoint


Review a full list of the Tweet object fields


Review a full list of available expansions



















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















