
Overview | Docs | Twitter Developer Platform 

Overview

**Please note**  

We've released the following endpoints within the Twitter API v2 . 

|  |  |  |
| --- | --- | --- |
| **v1.1 endpoints** | **Corresponding v2 endpoints** |  |
| GET users/lookup
GET users/show | User lookup | Migration guide |
| GET followers/ids
GET followers/list
GET friends/ids
GET friends/list
POST friendships/createPOST friendships/destroy | Follows | Migration guide |

Please use the migration guides to see what has changed between the standard v1.1 and v2 versions.

Overview
--------

The following API endpoints can be used to programmatically follow users, search for users, and get user information:

|  |  |  |
| --- | --- | --- |
| **Friends and followers** | **POST friendships** | **Get user info** |
| * GET followers/ids
* GET followers/list
* GET friends/ids
* GET friends/list
* GET friendships/incoming
* GET friendships/lookup
* GET friendships/no\_retweets/ids
* GET friendships/outgoing
* GET friendships/show
 | * POST friendships/create
* POST friendships/destroy
* POST friendships/update
 | * GET users/lookup
* GET users/search
* GET users/show
 |

For more details, please see the individual endpoint information within the API reference section.  

### Terminology

To avoid confusion around the term "friends" and "followers" with respect to the API endpoints, below is a definition of each:

**Friends** - we refer to "friends" as the Twitter users that a specific user follows (e.g., following). Therefore, the GET friends/ids endpoint returns a collection of user IDs that the specified user follows.

**Followers** - refers to the Twitter users that follow a specific user. Therefore, making a request to the GET followers/ids endpoint returns a collection of user IDs for every user following the specified user.

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