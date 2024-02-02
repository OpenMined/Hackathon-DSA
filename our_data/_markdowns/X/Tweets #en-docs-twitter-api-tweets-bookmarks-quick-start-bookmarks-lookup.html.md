
Bookmarks lookup quick start guide | Docs | Twitter Developer Platform 

Bookmarks lookup quick start

Getting started with the Bookmarks lookup endpoint
--------------------------------------------------

This quick start guide will help you make your first request to the Bookmarks lookup endpoint using Postman.  

Please visit our Twitter API v2 sample code GitHub repository if you want to see sample code in different languages.

### Prerequisites

To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:

* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.

### Steps to build a Bookmarks lookup request

#### Step one: Start with a tool or library

There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.

To load the Twitter API v2 Postman collection into your environment, please click on the following button:

Add Twitter API v2 to Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “Bookmarks” folder, and select “ Bookmarks lookup”.

### Step two: Authenticate your request

To make a successful request to this endpoint, you will need to use OAuth 2.0 Authorization Code Flow with PKCE. You can generate an access token within Postman. 

If you go to the tab entitled “Authorization” and select “OAuth 2.0”.

In this tab, be sure to follow these steps:

1. Name your token
2. Select the Grant Type as Authorization Code (with PKCE)
3. Update the parameters:

**Callback URL** - https://www.example.com

This should be matching the callback URL you set in your auth settings page in the Developer Portal.

**Auth URL** - https://twitter.com/i/oauth2/authorize

**Access Token URL** - https://api.twitter.com/2/oauth2/token

**Client ID** - Cut and paste OAuth 2.0 client ID from the Developer Portal

**Client Secret** - Cut and paste OAuth 2.0 client ID from the Developer Portal. You will need this only if you are using an App type that is a confidential client.
4. Update the scopes with the following values: tweet.read users.read bookmark.read
5. Populate the field state with “State”
6. Click where it says “Generate Token”
7. Press the save icon to save the folder changes.

You may get a message that you are not logged into Twitter. If you get this error, you will need to log in to the Twitter account inside of Postman you are trying to post on behalf of.

#### Step three: Specify a user

With this endpoint, you must specify the user ID whose followers you would like to receive in the response. For example, the user ID for @TwitterDev is2244994945. In Postman, navigate to the “Params” tab and enter the ID of yourself or an authenticated user as the value for the id parameter.

|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | 2244994945 |

#### Step four: Make your request and review your response

Once you have everything set up, hit the "Send" button and you will receive a similar response to the following example response:

```
      {
   "data": [
       {
           "id": "1501258597237342208",
           "text": "🗣 Have you built a project using the Twitter API you’d like to share with the community? We’d love to hear from you. Share your project with us!"
       },
       {
           "id": "1501258542258348032",
           "text": "🧰🛠 This is just one way developer innovation helps make Twitter a better place. You can find other ready-to-use tools built by our developer community in our Twitter Toolbox here ⬇️ https://t.co/rK0X30JSYU"
       },
       {
           "id": "1501257716941000709",
           "text": "📣Today’s an important day! \nWe’ve partnered with @Jigsaw on the launch of this new tool. This collaboration allows NGOs and nonprofits to build tools that help people stay safe on Twitter by addressing the needs and preferences of the communities they serve. Learn More ⬇️ https://t.co/MmznmgxoWT"
       },
       {
           "id": "1501686770810900485",
           "text": "Join us tomorrow for a continued conversation on customizing timelines and how this might work for developers. And stay tuned for more Spaces coming up next week. 👀 https://t.co/P4JTc14mdC"
       },
       {
           "id": "1501596763194593285",
           "text": "Developer innovation is always important, including in times of crisis. If you're building tools to help connect people, keep them safe, or share information with the world, we're here to support—reply to this Tweet to tell us more about your app."
       }
   ]
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