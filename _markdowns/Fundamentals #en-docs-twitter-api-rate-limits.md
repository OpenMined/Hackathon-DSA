



Rate limits | Docs | Twitter Developer Platform 






































































































Rate limits



Every day many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. 


The maximum number of requests that are allowed is based on a time interval, some specified period or window of time. The most common request limit interval is fifteen minutes. If an endpoint has a rate limit of 900 requests/15-minutes, then up to 900 requests over any 15-minute interval is allowed. 


Rate limits are applied based on which authentication method you are using. For example, if you are using OAuth 1.0a User Context, you will have one limit per time period for each set of users’ Access Tokens, while if you are using OAuth 2.0 Bearer Token, you will have a separate limit per time period for requests made by your app. When these limits are exceeded, an error is returned. Keep reading to learn more about these details and tips on how to avoid being rate limited.   

 


### Table of contents


* Twitter API v2 Free rate limits
* Twitter API v2 Basic rate limits
* Twitter API v2 Pro rate limits
* Twitter API Enterprise rate limits
* Rate limits and authentication method
* HTTP headers and response codes
* Recovering from rate limits
* Tips to avoid being rate limited


 


### Twitter API v2 rate limits - Free


The following table lists the rate limits for the Twitter API v2 Free access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  developer portal's products section.


 


 






|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| POST\_2\_tweets | 50 | 24 hours | per user | no | 1,500 |
| 50 | 24 hours | per app | no | 1,500 |
| DELETE\_2\_tweets\_id                                            | 50 | 24 hours | per user | no | 1,500 |
| 50 | 24 hours | per app | no | 1,500 |
| GET\_2\_users\_me | 25 | 24 hours | per user | no | 750 |




 


### Twitter API v2 rate limits - Basic


The following table lists the rate limits for the Twitter API v2 Basic access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  developer portal's products section.


 




|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| DELETE\_2\_lists\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_lists\_param\_members\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_tweets\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_id\_bookmarks\_tweet\_id | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_blocking\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_followed\_lists\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_following\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_likes\_param | 5 | 15 minutes | per user | no | 14,400 |
| 100 | 24 hours | per user | no | 3,000 |
| DELETE\_2\_users\_param\_muting\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_pinned\_lists\_param | 5 | 15 minutes | per user | no | 14,400 |
| DELETE\_2\_users\_param\_retweets\_param | 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_compliance\_jobs | 5 | 15 minutes | per app | no | 14,400 |
| GET\_2\_compliance\_jobs\_param | 5 | 15 minutes | per app | no | 14,400 |
| GET\_2\_dm\_conversations\_param\_dm\_events | 3 | 15 minutes | per user | no | 8,640 |
| GET\_2\_dm\_conversations\_with\_param\_dm\_events | 3 | 15 minutes | per user | no | 8,640 |
| GET\_2\_dm\_events | 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_lists\_id | 5 | 15 minutes | per user | no | 14,400 |
| 5 | 15 minutes | per app | no | 14,400 |  |
| GET\_2\_lists\_id\_members | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_lists\_id\_tweets | 5 | 15 minutes | per user | yes | 10,000 |
| 25 | 15 minutes | per app | yes | 10,000 |
| GET\_2\_spaces | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_spaces\_by\_creator\_ids | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_spaces\_param | 25 | 15 minutes | per app | no | 72,000 |
| 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_spaces\_param\_buyers | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_spaces\_param\_tweets | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_spaces\_search | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_tweets | 15 | 15 minutes | per user | yes | 10,000 |
| 15 | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_counts\_recent | 5 | 15 minutes | per app | no | 14,400 |
| GET\_2\_tweets\_param | 15 | 15 minutes | per user | yes | 10,000 |
| 15 | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_liking\_users | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_tweets\_param\_quote\_tweets | 5 | 15 minutes | per user | yes | 10,000 |
| 5 | 15 minutes | per app | yes | 10,000 |
| GET\_2\_tweets\_param\_retweeted\_by | 5 | 15 minutes | per app | yes | 10,000 |
| 5 | 15 minutes | per user | yes | 10,000 |  |
| GET\_2\_tweets\_search\_recent | 60 | 15 minutes  | per app  | yes | 10,000 |
| 60 | 15 minutes  | per user | yes |  |
| GET\_2\_users | 500 | 24 hours | per app | no | 15,000 |
| 100 | 24 hours | per user | no | 3,000 |
| GET\_2\_users\_by | 100 | 24 hours | per user | no | 3,000 |
| 500 | 24 hours | per app | no | 15,000 |
| GET\_2\_users\_by\_username\_param | 100 | 24 hours | per user | no | 3,000 |
| 500 | 24 hours | per app | no | 15,000 |
| GET\_2\_users\_by\_username\_param\_followers | 100 | 24 hours | per user | no | 3,000 |
| 500 | 24 hours | per app | no | 15,000 |
| GET\_2\_users\_by\_username\_param\_mentions | 25 | 15 minutes | per app | no | 72,000 |
| 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_users\_by\_username\_param\_tweets | 25 | 15 minutes | per app | yes | 10,000 |
| 5 | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_id\_bookmarks | 10 | 15 minutes | per user | no | 28,800 |
| GET\_2\_users\_id\_list\_memberships | 25 | 15 minutes | per app | no | 72,000 |
| 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_users\_id\_owned\_lists | 500 | 24 hours | per app | no | 15,000 |
| 100 | 24 hours | per user | no | 3,000 |
| GET\_2\_users\_id\_pinned\_lists | 100 | 24 hours | per user | no | 3,000 |
| 500 | 24 hours | per app | no | 15,000 |
| GET\_2\_users\_me | 250 | 24 hours | per user | no | 7,500 |
| GET\_2\_users\_param | 500 | 24 hours | per user | no | 15,000 |
| 100 | 24 hours | per app | no | 3,000 |
| GET\_2\_users\_param\_blocking | 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_users\_param\_following\_spaces | 5 | 15 minutes | per user | no | 14,400 |
| 25 | 15 minutes | per app | no | 72,000 |
| GET\_2\_users\_param\_liked\_tweets | 5 | 15 minutes | per app | yes | 10,000 |
| 5 | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_mentions | 15 | 15 minutes | per app | yes | 10,000 |
| 10 | 15 minutes | per user | yes | 10,000 |
| GET\_2\_users\_param\_muting | 100 | 24 hours | per user | no | 3,000 |
| GET\_2\_users\_param\_timelines\_reverse\_chronological | 5 | 15 minutes | per user | no | 14,400 |
| GET\_2\_users\_param\_tweets | 10 | 15 minutes | per app | yes | 10,000 |
| 5 | 15 minutes | per user | yes | 10,000 |
| POST\_2\_compliance\_jobs | 15 | 15 minutes | per app | no | 43,200 |
| POST\_2\_dm\_conversations | 5 | 15 minutes | per user | no | 14,400 |
| 500 | 24 hours | per app | no | 15,000 |
| 50 | 24 hours | per user | no | 1,500 |
| POST\_2\_dm\_conversations\_param\_messages | 500 | 24 hours | per app | no | 15,000 |
| 50 | 24 hours | per user | no | 1,500 |
| 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_dm\_conversations\_with\_param\_messages | 500 | 24 hours | per app | no | 15,000 |
| 50 | 24 hours | per user | no | 1,500 |
| 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_lists | 100 | 24 hours | per user | no | 3,000 |
| POST\_2\_lists\_param\_members | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_tweets | 100 | 24 hours | per user | no | 3,000 |
| 1667 | 24 hours | per app | no | 50,010 |
| POST\_2\_users\_id\_bookmarks | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_blocking | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_followed\_lists | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_following | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_likes | 200 | 24 hours | per user | no | 6,000 |
| 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_muting | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_pinned\_lists | 5 | 15 minutes | per user | no | 14,400 |
| POST\_2\_users\_param\_retweets | 5 | 15 minutes | per user | no | 14,400 |
| PUT\_2\_lists\_param | 5 | 15 minutes | per user | no | 14,400 |
| PUT\_2\_tweets\_param\_hidden | 5 | 15 minutes | per user | no | 14,400 |




 


### Twitter API v2 rate limits - Pro


The following table lists the rate limits for the Twitter API v2 Pro access. These rate limits are also documented on each endpoint's API Reference page and also displayed in the  developer portal's products section.


 




|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Endpoint** | **#Requests** | **Window of time** | **Per** | **Part of the Tweet pull cap?** | **Effective 30-day limit** |
| DELETE\_2\_lists\_param | 300 | 15 minutes | per user | no | 864,000 |
| DELETE\_2\_lists\_param\_members\_param | 300 | 15 minutes | per user | no | 864,000 |
| DELETE\_2\_tweets\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_id\_bookmarks\_tweet\_id | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_blocking\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_followed\_lists\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_following\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_likes\_param | 50 | 15 minutes | per user | no | 144,000 |
| 1000 | 24 hours | per user | no | 30,000 |
| DELETE\_2\_users\_param\_muting\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_pinned\_lists\_param | 50 | 15 minutes | per user | no | 144,000 |
| DELETE\_2\_users\_param\_retweets\_param | 50 | 15 minutes | per user | no | 144,000 |
| GET\_2\_compliance\_jobs | 150 | 15 minutes | per app | no | 432,000 |
| GET\_2\_compliance\_jobs\_param | 150 | 15 minutes | per app | no | 432,000 |
| GET\_2\_dm\_conversations\_param\_dm\_events | 100 | 15 minutes | per user | no | 288,000 |
| GET\_2\_dm\_conversations\_with\_param\_dm\_events | 100 | 15 minutes | per user | no | 288,000 |
| GET\_2\_dm\_events | 100 | 15 minutes | per user | no | 288,000 |
| GET\_2\_lists\_id | 75 | 15 minutes | per user | no | 216,000 |
| 75 | 15 minutes | per app | no | 216,000 |
| GET\_2\_lists\_id\_members | 900 | 15 minutes | per user | no | 2,592,000 |
| 900 | 15 minutes | per app | no | 2,592,000 |
| GET\_2\_lists\_id\_tweets | 900 | 15 minutes | per user | yes | 2,592,000 |
| 900 | 15 minutes | per app | yes | 2,592,000 |
| GET\_2\_spaces | 300 | 15 minutes | per user | no | 864,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_spaces\_by\_creator\_ids | 300 | 15 minutes | per user | no | 864,000 |
| 1 | 1 second | per app | no | 2,592,000 |
| 1 | 1 second | per user | no | 2,592,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_spaces\_param | 300 | 15 minutes | per app | no | 864,000 |
| 300 | 15 minutes | per user | no | 864,000 |
| GET\_2\_spaces\_param\_buyers | 300 | 15 minutes | per user | no | 864,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_spaces\_param\_tweets | 300 | 15 minutes | per user | no | 864,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_spaces\_search | 300 | 15 minutes | per user | no | 864,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_tweets | 900 | 15 minutes | per user | yes | 2,592,000 |
| 450 | 15 minutes | per app | yes | 1,296,000 |
| GET\_2\_tweets\_counts\_recent | 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_tweets\_param | 900 | 15 minutes | per user | yes | 2,592,000 |
| 450 | 15 minutes | per app | yes | 1,296,000 |
| GET\_2\_tweets\_param\_liking\_users | 75 | 15 minutes | per user | no | 216,000 |
| 75 | 15 minutes | per app | no | 216,000 |
| GET\_2\_tweets\_param\_quote\_tweets | 75 | 15 minutes | per user | yes | 216,000 |
| 75 | 15 minutes | per app | yes | 216,000 |
| GET\_2\_tweets\_param\_retweeted\_by | 75 | 15 minutes | per app | yes | 216,000 |
| 75 | 15 minutes | per user | yes | 216,000 |
| GET\_2\_tweets\_search\_recent | 450 | 15 minutes | per app | yes | 1,296,000 |
| 300 | 15 minutes | per user | yes | 864,000 |
| GET\_2\_tweets\_search\_stream | 50 | 15 minutes | per app | yes | 144,000 |
| GET\_2\_tweets\_search\_stream\_rules | 450 | 15 minutes | per app | no | 1,296,000 |
| GET\_2\_users | 300 | 15 minutes | per app | no | 864,000 |
| 900 | 15 minutes | per user | no | 2,592,000 |
| GET\_2\_users\_by | 900 | 15 minutes | per user | no | 2,592,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_users\_by\_username\_param | 900 | 15 minutes | per user | no | 2,592,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_users\_by\_username\_param\_followers | 15 | 15 minutes | per user | no | 43,200 |
| 15 | 15 minutes | per app | no | 43,200 |
| GET\_2\_users\_by\_username\_param\_mentions | 450 | 15 minutes | per app | no | 1,296,000 |
| 180 | 15 minutes | per user | no | 518,400 |
| GET\_2\_users\_by\_username\_param\_tweets | 1500 | 15 minutes | per app | yes | 4,320,000 |
| 900 | 15 minutes | per user | yes | 2,592,000 |
| GET\_2\_users\_id\_bookmarks | 180 | 15 minutes | per user | no | 518,400 |
| GET\_2\_users\_id\_list\_memberships | 75 | 15 minutes | per app | no | 216,000 |
| 75 | 15 minutes | per user | no | 216,000 |
| GET\_2\_users\_id\_owned\_lists | 15 | 15 minutes | per app | no | 43,200 |
| 15 | 15 minutes | per user | no | 43,200 |
| GET\_2\_users\_id\_pinned\_lists | 15 | 15 minutes | per user | no | 43,200 |
| 15 | 15 minutes | per app | no | 43,200 |
| GET\_2\_users\_me | 75 | 15 minutes | per user | no | 216,000 |
| GET\_2\_users\_param | 900 | 15 minutes | per user | no | 2,592,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_users\_param\_blocking | 15 | 15 minutes | per user | no | 43,200 |
| GET\_2\_users\_param\_following\_spaces | 300 | 15 minutes | per user | no | 864,000 |
| 300 | 15 minutes | per app | no | 864,000 |
| GET\_2\_users\_param\_liked\_tweets | 75 | 15 minutes | per app | yes | 216,000 |
| 75 | 15 minutes | per user | yes | 216,000 |
| GET\_2\_users\_param\_mentions | 450 | 15 minutes | per app | yes | 1,296,000 |
| 300 | 15 minutes | per user | yes | 864,000 |
| GET\_2\_users\_param\_muting | 15 | 15 minutes | per user | no | 43,200 |
| GET\_2\_users\_param\_timelines\_reverse\_chronological | 180 | 15 minutes | per user | no | 518,400 |
| GET\_2\_users\_param\_tweets | 1500 | 15 minutes | per app | yes | 4,320,000 |
| 900 | 15 minutes | per user | yes | 2,592,000 |
| POST\_2\_compliance\_jobs | 150 | 15 minutes | per app | no | 432,000 |
| POST\_2\_dm\_conversations | 200 | 15 minutes | per user | no | 576,000 |
| 2500 | 24 hours | per app | no | 75,000 |
| 1000 | 24 hours | per user | no | 30,000 |
| POST\_2\_dm\_conversations\_param\_messages | 2500 | 24 hours | per app | no | 75,000 |
| 1000 | 24 hours | per user | no | 30,000 |
| 200 | 15 minutes | per user | no | 576,000 |
| POST\_2\_dm\_conversations\_with\_param\_messages | 2500 | 24 hours | per app | no | 75,000 |
| 1000 | 24 hours | per user | no | 30,000 |
| 200 | 15 minutes | per user | no | 576,000 |
| POST\_2\_lists | 300 | 15 minutes | per user | no | 864,000 |
| POST\_2\_lists\_param\_members | 300 | 15 minutes | per user | no | 864,000 |
| POST\_2\_tweets | 100 | 15 minutes | per user | no | 288,000 |
| 10000 | 24 hours | per app | no | 300,000 |
| POST\_2\_tweets\_search\_stream\_rules | 100 | 15 minutes | per user | no | 288,000 |
| POST\_2\_users\_id\_bookmarks | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_blocking | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_followed\_lists | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_following | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_likes | 1000 | 24 hours | per user | no | 30,000 |
| 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_muting | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_pinned\_lists | 50 | 15 minutes | per user | no | 144,000 |
| POST\_2\_users\_param\_retweets | 50 | 15 minutes | per user | no | 144,000 |
| PUT\_2\_lists\_param | 300 | 15 minutes | per user | no | 864,000 |
| PUT\_2\_tweets\_param\_hidden | 50 | 15 minutes | per user | no | 144,00 |


### Twitter API v2 rate limits - Enterprise


To learn more about enterprise access rate limits reach out to your account manager.

























**Please note**  




In addition to rate limits, we also have Tweet caps that limit the number of Tweets that any Project can retrieve from certain endpoints in a given month, which is based on your access level.









### 
Rate limits and authentication method


Rate limits are set at both the developer App and the user access token levels:


* **OAuth 2.0 Bearer Token: App rate limit**This authentication method and rate limit allows you to make a certain number of requests to endpoints on behalf of your developer App. When using this authentication method, rate limits are determined by the number of requests you make using a Bearer Token.  

  

If an endpoint has an App rate limit of 450 requests per 15 minute interval, then you can make 450 requests per window on behalf of your App when you use your Bearer Token.  

  

This limit is considered completely separate from the user rate limit.
* **OAuth 1.0a User Context: User rate limit**  

This authentication method and rate limit allows for you to make a certain number of requests to endpoints on behalf of a Twitter user, identified by the user Access Token used when authenticating the request. For example, if you would like to retrieve private metrics from Tweets, you would need to authenticate with the user Access Tokens associated with that user, which can be generated by using the 3-legged OAuth flow.   

  

If ten users have authorized your developer App, and the endpoint you are making a request to has a user rate limit of 900 requests per 15-minute interval, then you can make up to 900 requests per user in that 15 minute time period, for a total of 9000 requests.  

  

This limit is considered completely separate from App rate limit.











**Please note**


Users' rate limits are shared across all Apps that they have authorized. For example, if a specific user likes 20 Tweets using one developer App and likes 20 Tweets on a separate developer App within a 15 minute time period, the 40 requests would pull out of the same per user rate limit bucket. That means that if this endpoint has a user rate limit of 1,000 requests per 15 minutes, then this user would be able to like 960 more Tweets within that 24 hour period of time across all Twitter and third-party apps. 









### 


### HTTP headers and response codes


Use the HTTP headers in order to understand where the application is at for a given rate limit, on the method that was just utilized.  




Note that the HTTP headers are contextual. When using application-only authentication, they indicate the rate limit for the application context. When using user-based authentication, they indicate the rate limit for that user context.  




* x-rate-limit-limit: the rate limit ceiling for that given endpoint
* x-rate-limit-remaining: the number of requests left for the 15-minute window
* x-rate-limit-reset: the remaining window before the rate limit resets, in UTC epoch seconds


When an application exceeds the rate limit for a given Twitter API endpoint, the API will return a HTTP 429 “Too Many Requests” response code, and the following error will be returned in the response body:


{ "errors": [ { "code": 88, "message": "Rate limit exceeded" } ] } 


 


### Recovering from a rate limit


When these rate limits are exceeded, a 429 'Too many requests' error is returned from the endpoint.  As discussed below, when rate limit errors occur, a best practice is to examine HTTP headers that indicate when the limit resets and pause requests until then.    




When a "too many requests" or rate-limiting error occurs, the frequency of making requests needs to be slowed down. When a rate limit error is hit, the x-rate-limit-reset: HTTP header can be checked to learn when the rate-limiting will reset.   




Another common pattern is based on exponential backoff, where the time between requests starts off small (for example, a few seconds), then doubled before each retry. This is continued until a request is successful, or some reasonable maximum time between requests is reached (for example, a few minutes).    




Ideally, the client-side is self-aware of existing rate limits and can pause requests until the currently exceeded window expires. If you exceed a 15-minute limit, then waiting a minute or two before retrying makes sense.


Note that beyond these limits on the number of requests, the Standard Basic level of access provides up to 500,000 Tweets per month from the recent search and filtered stream endpoints. If you have exceeded the monthly limit on the number of Tweets, then it makes more sense for your app to raise a notification and know its enrollment day of the month and hold off requests until that day.    

 


### Tips to avoid being rate limited


The tips below are there to help you code defensively and reduce the possibility of being rate limited. Some application features that you may want to provide are simply impossible in light of rate-limiting, especially around the freshness of results. If real-time information is an aim of your application, look into the filtered and sampled stream endpoints.   

 


#### Caching


Store API responses in your application or on your site if you expect a lot of use. For example, don’t try to call the Twitter API on every page load of your website landing page. Instead, call the API infrequently and load the response into a local cache. When users hit your website load the cached version of the results.  

 


#### Prioritize active users


If your site keeps track of many Twitter users (for example, fetching their current status or statistics about their Twitter usage), consider only requesting data for users who have recently signed into your site.  

 


#### Adapt to the search results


If your application monitors a high volume of search terms, query less often for searches that have no results than for those that do. By using a back-off you can keep up to date on queries that are popular but not waste cycles requesting queries that very rarely change. Alternatively, consider using the filtered stream endpoint and filter with your search queries.  

  


#### Denylist


If an application abuses the rate limits, it will be denied. Denied apps are unable to get a response from the Twitter API. If you or your application has been denied and you think there has been a mistake, you can use our Platform Support forms to request assistance. Please include the following information:


1. Explain why you think your application was denied.
2. If you are no longer being rate limited, describe in detail how you fixed the problem.


 






Next steps
----------






Learn more about Tweet caps



















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















