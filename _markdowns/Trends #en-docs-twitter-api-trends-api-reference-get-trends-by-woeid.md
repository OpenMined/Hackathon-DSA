



GET /2/trends/by/woeid/:woeid | Docs | Twitter Developer Platform 





































































































GET /2/trends/by/woeid/:woeid



GET /2/trends/by/woeid/:woeid
=============================


Get the trends for a location


### Endpoint URL


`https://api.twitter.com/2/trends/by/woeid/:woeid`  

  




### Authentication and rate limits




|  |  |
| --- | --- |
| Authentication methods
supported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 75 requests per 15-minute window shared among all users of your app |


### Path parameters




| Name | Type | Description |
| --- | --- | --- |
| `woeid`
 Required  | number | The where-on-earth ID (woeid) for a location |






### Example responses








* Default Fields


















 Default Fields
 
















```

      {
  "data": [
    {
      "trend_name": "#TEZOSTUESDAY",
      "tweet_count": 14869
    },
    {
      "trend_name": "Copenhagen",
      "tweet_count": 13005
    },
    {
      "trend_name": "Roses",
      "tweet_count": 32193
    },
    {
      "trend_name": "Heroes",
      "tweet_count": 69798
    },
    {
      "trend_name": "Cedric",
      "tweet_count": 14259
    },
    {
      "trend_name": "#AskSonic",
      "tweet_count": 8908
    },
    {
      "trend_name": "Nelson",
      "tweet_count": 29841
    },
    {
      "trend_name": "#PSVARS",
      "tweet_count": 4915
    },
    {
      "trend_name": "Eddie",
      "tweet_count": 34139
    },
    {
      "trend_name": "Saliba",
      "tweet_count": 7191
    },
    {
      "trend_name": "Walters",
      "tweet_count": 8095
    },
    {
      "trend_name": "Bakayoko",
      "tweet_count": 1809
    },
    {
      "trend_name": "Bibby Stockholm",
      "tweet_count": 21021
    },
    {
      "trend_name": "Nwaneri",
      "tweet_count": 5783
    },
    {
      "trend_name": "Doncaster",
      "tweet_count": 3551
    },
    {
      "trend_name": "Kiwior",
      "tweet_count": 1535
    }
  ]
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `trend_name` | string | The name of the Trend. |
| `tweet_count` | integer | The total number of Tweets that are part of this Trend. |



















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















