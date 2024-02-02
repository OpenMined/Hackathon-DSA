
Timelines quick start guide | Docs | Twitter Developer Platform 

User Tweet and mention quick start

Getting started with the user Tweet and mention timeline endpoints
------------------------------------------------------------------

This quick start guide will help you make your first request to the user Tweet timeline endpoint with a set of specified fields using Postman.

If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository.   

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a timelines request

*For this example, we will make a request to the user Tweet timeline by ID endpoint, but you can apply the learnings from this quick start to user mention timelines requests as well.*

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the timeline folder and find the "User Tweet timeline by ID" request.  

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request with either OAuth 2.0 App-Only, OAuth 2.0 Authorization Code with PKCE, or OAuth 1.0a User Context authentication methods.

For simplicity's sake, we will utilize OAuth 2.0 App-Only with this request, but you will need to use one of the other authentication methods if you'd like to request private metrics or Tweets. 

You must add your keys and tokens, specifically theApp Access Token (also known as the App-only Bearer Token) to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

This variable will automatically be pulled into the request's authorization tab if you've done this correctly.  

#### Step three: Identify and specify which user from which you would like to retrieve Tweets

You must specify a user you would like to retrieve recent Tweets for within the request. In this example, we will be passing a single user ID.

User IDs are simply the numerical value that represents an account handle that you can find within an account's profile URL. For example, the following account’s username is `TwitterDev`.

`https://twitter.com/TwitterDev`

To convert this username to the user ID, you will have to use the users lookup endpoint with the username and find the numerical user ID in the payload. In the case of @TwitterDev, the user ID is 2244994945.

In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the id parameter.

|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | 2244994945 |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default Tweet object fields in your response: id and text.

If you would like to receive additional fields beyond id and text, you will have to specify those fields in your request with the field and/or expansion parameters.

For this exercise, we will request a three additional different sets of fields from different objects:

1. The additional tweet.created\_at field in the primary user objects.
2. The associated authors’ user object’s default fields for the returned Tweets: id, name, and username
3. The additional  user.created\_at field in the associated user objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:  

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `tweet.fields` | `created_at` | `tweets.created_at` |
| `expansions` | `author_id` | `includes.users.id`, `includes.users.name`, `includes.users.username` |
| `user.fields` | `created_at` | `includes.users.created_at` |
| max\_results | 5 |  |

You should now see the following URL next to the "Send" button:

```
      https://api.twitter.com/2/users/:id/tweets?tweet.fields=created_at&expansions=author_id&user.fields=created_at&max_results=5

```

Code copied to clipboard

**Please note:**

In Postman, the path parameter :id in the URL field will **not** automatically update to the value that you enter into the `id` params field, which is why the above URL includes `:id` and not 2244994945.

#### 
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
    "data": [
        {
            "author_id": "2244994945",
            "created_at": "2020-09-03T17:31:39.000Z",
            "id": "1301573587187331074",
            "text": "Starting today, you can see your monthly Tweet usage for the v2 API in the developer portal. ✨📊\n\nThis tracks how many Tweets you’ve received from filtered stream and recent search. Learn more here: https://t.co/nfJHkFRQcZ https://t.co/vFXmoj3qaA"
        },
        {
            "author_id": "2244994945",
            "created_at": "2020-09-03T15:43:00.000Z",
            "id": "1301546240887398401",
            "text": "RT @snowman: So, we built a live golf leaderboard on the Twitter API with Python, Flask, Postgres, and Heroku.\n\nSend a 'leaderboard' Direct…"
        },
        {
            "author_id": "2244994945",
            "created_at": "2020-09-01T20:07:50.000Z",
            "id": "1300888112948752389",
            "text": "⛳ Why do golfers carry an extra shirt? In case they get a hole in one.\n\nNow that we have your attention, learn how @snowman and @johnd built a real-time golf leaderboard using the #TwitterAPI. 📖\n\nhttps://t.co/rRKeKmaRrN"
        },
        {
            "author_id": "2244994945",
            "created_at": "2020-08-28T23:14:22.000Z",
            "id": "1299485505478963200",
            "text": "RT @jessicagarson: Posted my first tutorial on @ThePracticalDev on using v2 of the Twitter API! You will learn how to explore a user’s Twee…"
        },
        {
            "author_id": "2244994945",
            "created_at": "2020-08-21T19:10:05.000Z",
            "id": "1296887316556980230",
            "text": "See how @PennMedCDH are using Twitter data to understand the COVID-19 health crisis 📊\n\nhttps://t.co/1tdA8uDWes"
        }
    ],
    "includes": {
        "users": [
            {
                "created_at": "2013-12-14T04:35:55.000Z",
                "id": "2244994945",
                "name": "Twitter Dev",
                "username": "TwitterDev"
            }
        ]
    },
    "meta": {
        "newest_id": "1301573587187331074",
        "next_token": "t3buvdr5pujq9g7bggsnf3ep2ha28",
        "oldest_id": "1296887316556980230",
        "previous_token": "t3equkmcd2zffvags2nkj0nhlrn78",
        "result_count": 5
    }
}

```

#### 
Step six: Paginate through your results

In the previous response, you will find a meta data object at the bottom that includes the following fields:

* oldest\_id
* newest\_id
* results\_count
* next\_token
* previous\_token

In step four, we passed a max\_results value of 5, meaning that each page will only include up to five results. To access the additional pages of data, we will be taking the value of the next\_token field from our last results and adding that string as the value of the pagination\_token parameter on the Postman params page, keeping everything else constant. 

|  |  |
| --- | --- |
| **Key** | **Value** |
| `pagination_token` | t3buvdr5pujq9g7bggsnf3ep2ha28 |

Once this is all set up, you can click "Send" again and you should receive the next page of results. 

We have put together a guide on pagination to further explain this concept. 

Next steps
----------

Customize your request using the API Reference

Learn how to explore a user's Tweets

Reach out to the community for help

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