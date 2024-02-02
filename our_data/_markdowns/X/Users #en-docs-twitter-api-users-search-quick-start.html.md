
User Search Quick start | Docs | Twitter Developer Platform 

Quick start

Getting started with the users search endpoint
----------------------------------------------

This quick start guide will help you make your first request to the users search endpoints using Postman.

If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository.   

**Note**: This endpoint is available only to developers with Pro access. Sign up for Pro access here.

### Prerequisites

For you to be able to complete this guide, you will have need to have a set of keys and tokens, which you can generate by following these steps:

1. Sign up for a developer account.
2. Create a Project and an associated developer App in the developer portal.
3. Navigate to your app's “Keys and tokens” page, and save your credentials in a secure location.

### Steps to build a users lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the GET /users/search.  

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission to do so. To do this with the GET /users/by endpoint, you must pass your developer App's Bearer Token along with your request.

First, from within the GET /users/by request in Postman, navigate to the “Authentication” tab. In the "Type" dropdown, select "Bearer Token", and then copy and paste your App only Bearer Token from your password manager into the "Token" field.  

#### Step three: Identify and specify the query for which you want to get the Users for

You must specify the query for which you want to get the Users for. In this example, we will get Users for the search term xdevelopers

In Postman, navigate to the "Params" tab and enter your query i.e. xdevelopers into the "Value" column of the query parameter

|  |  |
| --- | --- |
| **Key** | **Value** |
| `username` | xdevelopers |

#### Step four: Identify and specify which fields you would like to retrieve

If you click the "Send" button after step three, you will receive the default user object fields in your response: id, name, and username.

If you would like to receive additional fields beyond id, name, and username, you will have to specify those fields in your request with the field and/or expansion parameters.

For this exercise, we will request a three additional sets of fields from different objects:

1. The additional user.created\_at field in the primary user objects.
2. The associated pinned Tweets’ object’s default fields for the returned users: id and text.
3. The additional  tweet.created\_at field in the associated Tweet objects.

In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Returned fields** |
| `user.fields` | `created_at` | `user.created_at` |
| `expansions` | `author_id` | tweet.id, tweet.text |
| `tweet.fields` | `created_at` | `includes.users.created_at` |

You should now see the following URL next to the "Send" button:

```
      https://api.twitter.com/2/users/search?query=xdevelopers&user.fields=description,location
```

Code copied to clipboard

#### 
Step five: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
    "data": [
        {
            "location": "127.0.0.1",
            "name": "Developers",
            "description": "The voice of the X Dev team and your official source for updates, news, and events, related to the X API.",
            "username": "XDevelopers",
            "id": "2244994945"
        },
        {
            "location": "Seattle, WA",
            "name": "Suhem Parack",
            "description": "Partner Engineering @XDevelopers",
            "username": "suhemparack",
            "id": "857699969263964161"
        },
        {
            "location": "New York, NY",
            "name": "Chris Park",
            "description": "𝕏 | @X @API @XDevelopers",
            "username": "chrisparkX",
            "id": "2533341854"
        },
        {
            "location": "Islington, London",
            "name": "Haim Vaturi",
            "description": "@XDevelopers",
            "username": "haimvat",
            "id": "853388192"
        },
        {
            "location": "Canada",
            "name": "ROBLOX Devs",
            "description": "Follow this account for a lot of cool ROBLOXdev from all kinds of different ROBLOX developers! Not an official @ROBLOX twitter account",
            "username": "RBXdevelopers",
            "id": "829457852125306890"
        },
        {
            "location": "東京都港区",
            "name": "Twitter Dev Japan",
            "description": "This account is no longer active. Follow @XDevelopers for updates.",
            "username": "TwitterDevJP",
            "id": "70915829"
        },
        {
            "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",
            "description": "",
            "username": "0xdevelopersTm",
            "id": "1619352801104039936"
        },
        {
            "name": "Project X Developers",
            "description": "",
            "username": "ProXDevelopers",
            "id": "708786906058756096"
        },
        {
            "location": "Los Angeles, CA",
            "name": "XDevelopersUS",
            "description": "",
            "username": "XDevelopersUS",
            "id": "1315227013028904960"
        },
        {
            "location": "Rio de Janeiro & São Paulo",
            "name": "XDevelopers",
            "description": "Contato e Suporte Via Telefone (RJ): 21 980534086 e Via Email: contato@XDevelopers.com.br",
            "username": "XDevBrasil",
            "id": "3296066705"
        }
    ],
    "meta": {
        "next_token": "5qym3iwo3naekslszn59lxy1d9nmc6q"
    }
}
```

Code copied to clipboard

Next steps
----------

Customize your request using the API Reference

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