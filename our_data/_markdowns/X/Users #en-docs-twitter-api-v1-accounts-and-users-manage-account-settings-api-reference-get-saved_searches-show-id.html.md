
GET saved\_searches/show/:id | Docs | Twitter Developer Platform 

GET saved\_searches/show/:id

get-saved\_searches-show-id
GET saved\_searches/show/:id
============================

Retrieve the information for the saved search represented by the
given id. The authenticating user must be the owner of saved search ID
being requested.

Resource URL¶
-------------

`https://api.twitter.com/1.1/saved_searches/show/:id.json`

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
| id | required | The ID of the saved search. |  | *313006* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/saved_searches/show/9569704.json`

Example Response¶
-----------------

```
{
  "created_at": "Fri Nov 04 18:46:41 +0000 2011", 
  "id": 62353170, 
  "id_str": "62353170", 
  "name": "@anywhere", 
  "position": null, 
  "query": "@anywhere"
}
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