
Quick start | Docs | Twitter Developer Platform 

Quick start

Getting started with the Quote Tweets lookup endpoint
-----------------------------------------------------

This quick start guide will help you make your first request to the Quote Tweets lookup endpoints with a set of specified fields using Postman.

If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository.   

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a Quote Tweets lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the timeline folder and find the "Quote Tweets by ID" request.

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with either OAuth 2.0 App-Only, OAuth 2.0 Authorization Code with PKCE, or OAuth 1.0a User Context authentication methods.

For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private metrics or Tweets. 

You must add your keys and tokens, specifically theApp Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.

#### Step three: Identify and specify the Tweet you would like to retrieve the Quote Tweets for

You must specify a Tweet you would like to retrieve Quote Tweets for within the request by passing the  Tweet ID.

In this example, the Tweet ID that we will use is 1409931481552543749.

In Postman, navigate to the "Params" tab and enter this Tweet ID into the "Value" column of the id parameter.

|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | 1409931481552543749 |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default Tweet object fields in your response: id,  text, and edit\_history\_tweet\_ids.

If you would like to receive additional fields, you will have to specify those fields in your request with the field and/or expansion parameters.

For this exercise, we will request three additional different sets of fields from different objects:

1. The additional tweet.created\_at field in the primary user objects.
2. The associated authors’ user object’s default fields for the returned Tweets: id, name, and username
3. The additional user.created\_at field in the associated user objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:  

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `tweet.fields` | `created_at` | `tweets.created_at` |
| `expansions` | `author_id` | `includes.users.id`, `includes.users.name`, `includes.users.username` |
| `user.fields` | `created_at` | `includes.users.created_at` |  |

You should now see the following URL next to the "Send" button:

```
      https://api.twitter.com/2/tweets/:id/quote_tweets?expansions=author_id&tweet.fields=created_at&user.fields=created_at
```

Code copied to clipboard

**Please note:**

In Postman, the path parameter :id in the URL field will **not** automatically update to the value that you enter into the `id` params field, which is why the above URL includes `:id` and not 1409931481552543749.

#### 
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
 "data": [
   {
     "created_at": "2022-02-22T04:31:34.000Z",
     "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…",
     "author_id": "29757971",
     "id": "1495979553889697792"
   },
   {
     "created_at": "2022-01-26T17:07:43.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "241588187",
     "id": "1486385372401737728"
   },
   {
     "created_at": "2022-01-11T17:28:04.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "24961055",
     "id": "1480954678447857669"
   },
   {
     "created_at": "2022-01-10T20:34:46.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "1441574419789324291",
     "id": "1480639272721940486"
   },
   {
     "created_at": "2021-12-16T22:55:24.000Z",
     "text": "RT @chris_bail: Twitter has created an entire course (with videos, code, and other materials) to help researchers learn how to collect data…",
     "author_id": "1623598771",
     "id": "1471614967207976961"
   },
   {
     "created_at": "2021-12-13T15:59:55.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "1506401233",
     "id": "1470423243513372679"
   },
   {
     "created_at": "2021-12-10T02:02:45.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "40103034",
     "id": "1469125403373568001"
   },
   {
     "created_at": "2021-12-08T17:27:54.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "1436400156006567936",
     "id": "1468633446935318529"
   },
   {
     "created_at": "2021-09-15T21:40:24.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "81650379",
     "id": "1438256410417143809"
   },
   {
     "created_at": "2021-08-26T16:45:16.000Z",
     "text": "RT @suhemparack: Super excited to share our course on Getting started with the #TwitterAPI v2 for academic research\n\nIf you know students w…",
     "author_id": "40462535",
     "id": "1430934381829492746"
   }
 ],
 "includes": {
   "users": [
     {
       "username": "j_a_tucker",
       "id": "29757971",
       "name": "Joshua Tucker",
       "created_at": "2009-04-08T16:45:38.000Z"
     },
     {
       "username": "whimchic",
       "id": "241588187",
       "name": "whimchic",
       "created_at": "2011-01-22T16:51:43.000Z"
     },
     {
       "username": "mattbiehl",
       "id": "24961055",
       "name": "Matthias Biehl",
       "created_at": "2009-03-17T21:41:27.000Z"
     },
     {
       "username": "weixinac",
       "id": "1441574419789324291",
       "name": "J",
       "created_at": "2021-09-25T01:25:19.000Z"
     },
     {
       "username": "RSangeleer",
       "id": "1623598771",
       "name": "Richard Sangeleer",
       "created_at": "2013-07-26T18:25:45.000Z"
     },
     {
       "username": "Gulnerman",
       "id": "1506401233",
       "name": "Giz Gulnerman",
       "created_at": "2013-06-11T20:13:40.000Z"
     },
     {
       "username": "efishman123",
       "id": "40103034",
       "name": "Elishema Fishman",
       "created_at": "2009-05-14T22:25:58.000Z"
     },
     {
       "username": "dtcxwz",
       "id": "1436400156006567936",
       "name": "Hüseyin Ateş",
       "created_at": "2021-09-10T18:44:30.000Z"
     },
     {
       "username": "brendaberkelaar",
       "id": "81650379",
       "name": "Dr. Brenda Berkelaar",
       "created_at": "2009-10-11T18:09:16.000Z"
     },
     {
       "username": "misoca",
       "id": "40462535",
       "name": "Michael Soto",
       "created_at": "2009-05-16T13:26:05.000Z"
     }
   ]
 },
 "meta": {
   "result_count": 10,
   "next_token": "avdjwk0udyx6"
 }
}
```

#### Step six: Paginate through your results

In the previous response, you will find a meta data object at the bottom that includes the following fields:

* results\_count
* next\_token

In step four, because we did not specify a max\_results parameter, we will only get 10 Tweets by default. To access the additional pages of data, we will be taking the value of the next\_token field from our last results and adding that string as the value of the pagination\_token parameter on the Postman params page, keeping everything else constant. 

|  |  |
| --- | --- |
| **Key** | **Value** |
| `pagination_token` | avdjwk0udyx6 |

Once this is all set up, you can click "Send" again and you should receive the next page of results. 

We have put together a guide on pagination to further explain this concept. 

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