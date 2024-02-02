
GET
friendships/no\_retweets/ids | Docs | Twitter Developer Platform 

GET
friendships/no\_retweets/ids

get-friendships-no\_retweets-ids
GET
friendships/no\_retweets/ids
================================

Returns a collection of user\_ids that the currently authenticated
user does not want to receive retweets from.

Use POST
friendships / update to set the "no retweets" status for a given
user account on behalf of the current user.

Resource URL¶
-------------

`https://api.twitter.com/1.1/friendships/no_retweets/ids.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to
their size. Provide this option to have IDs returned as strings instead.
Read more about Twitter IDs.
This parameter is important to use in Javascript environments. | *false* | *true* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/friendships/no_retweets/ids.json?stringify_ids=true`

Example Response¶
-----------------

```
["777925","732321"]
```

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