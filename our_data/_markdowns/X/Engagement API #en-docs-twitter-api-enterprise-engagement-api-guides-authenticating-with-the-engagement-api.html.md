
Authenticating with the Engagement API | Docs | Twitter Developer Platform 

Authenticating with the Engagement API

**Please note**: 

Twitter needs to enable access to the Engagement API for your developer App before you can start using the API. To this end, make sure to share the App ID that you intend to use for authentication purposes with your account manager or technical support team.

There are two authentication methods available with the Engagement API: OAuth 1.0a and OAuth 2.0 Bearer Token. 

**OAuth 2.0 Bearer Token** (also referred to as “application-only”) allows you to access publicly available engagement metrics. This authentication method can be used to get total counts for Favorites (aka Likes), Retweets, Quote Tweets, Replies, and video views for any publicly available Tweets when making requests to the /totals endpoint. 

**OAuth 1.0a** (also referred to as “user context”) allows you to make requests on behalf of a user and access private engagement metrics that belong to the user in question. 

This authentication method is required for:

* All requests sent to the /28hr endpoint and /historical endpoint
* Accessing any of the following private metrics: Impressions, Engagements, Media Views, Media Engagements, URL Clicks, Hashtag Clicks, Detail Expands, Permalink Clicks, App Install Attempts, App Opens, Email Tweet, User Follows, and User Profile Clicks

When sending a request with OAuth 1.0a, you need to include the Access Tokens (Access Token and Secret) of the user who owns the Tweet or protected resource of interest. If you do not provide the correct user Access Tokens when requesting protected user data, the Engagement API will return a `403 Forbidden` error.

The Engagement API will not allow you to fetch engagement data for protected Tweets, even if you are authenticating on behalf of the user who owns these Tweets. Attempting to do so will return a `400 Bad Request` error, with the message `"Tweet ID(s) are unavailable"`.

If you are sending a request on behalf of your own Twitter account (in other words, the account that owns the developer App), you can generate the required Access Tokens directly from within the developer portal, under the “Keys and tokens” tab for the developer App.

If you are making a request on behalf of any other user, you will need to use the 3-legged OAuth flow to obtain the required Access Tokens. The following documentation contains more information on how to do this: OAuth 1.0a: how to obtain a user’s access tokens.

For additional examples, including how to authenticate using OAuth 1.0a, check out TwitterDev’s sample Python code for the Engagement API.

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