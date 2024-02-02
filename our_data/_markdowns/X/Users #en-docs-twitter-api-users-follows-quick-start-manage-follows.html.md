
Manage follows quick start guide | Docs | Twitter Developer Platform 

Manage follows quick start

Getting started with the manage follows endpoints
-------------------------------------------------

This quick start guide will help you make your first request to the manage follows endpoints using Postman.

If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository.   

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a manage follows request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we are going to use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Follows” folder, and select “Follow a user ID”.  

#### Step two: Authenticate your request

To properly make a request to the Twitter API, you need to verify that you have permission. To do so with this endpoint, you must authenticate your request using either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.

In this example, we are going to use OAuth 1.0a User Context.

You must add your keys and tokens – specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret – to Postman. You can do this by selecting the environment named “Twitter API v2” in the top-right corner of Postman and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).

These variables will automatically be pulled into the request's authorization tab if you've done this correctly.  

#### Step three: Specify who is going to follow whom

Manage follows endpoints take two IDs: one for the source user (the user who wishes to follow or unfollow another user) and the target user (the user that will be followed or unfollowed). The source user’s ID must correspond to the user ID of the authenticating user. In this case, you can specify the ID belonging to your own user. You can find your ID in two ways:

1. Using the user lookup by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

The target ID can be any valid user ID. For example the user ID for @TwitterDev is 2244994945.

In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and and 2244994945 (the user ID for @TwitterDev) as the value for the target\_user\_id parameter. Making sure to not include any spaces before or after any ID.

|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | (your user ID) |
| target\_user\_id | 2244994945 |

If you click the "Send" button, you will receive a response object containing the status of the relationship:

* If you receive a "following": true, then the id is successfully following the target\_user\_id.
* If you receive a "pending": true, then the target\_user\_id is protected and must accept your follow request.

#### 
Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive the following response:

```
      {
    "data": {
        "following": true,
        "pending_follow": false
    }
}
```

Similarly, if you were trying to unfollow a user, you would use the "Unfollow a user ID" request within the same Postman collection. However, both the source\_user\_id and target\_user\_id parameters should be passed as path variables using the unfollow endpoint. 

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