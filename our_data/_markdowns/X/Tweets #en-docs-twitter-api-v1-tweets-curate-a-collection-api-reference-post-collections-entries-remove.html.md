
POST
collections/entries/remove | Docs | Twitter Developer Platform 

POST
collections/entries/remove

post-collections-entries-remove
POST
collections/entries/remove
===============================

Remove the specified Tweet from a Collection.

Use POST
collections / entries / curate to remove Tweets from a Collection in
bulk.

Resource URL¶
-------------

`https://api.twitter.com/1.1/collections/entries/remove.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The identifier of the target Collection. |  | *custom-388061495298244609* |
| tweet\_id | required | The identifier of the Tweet to remove. |  | *390839888012382208* |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/collections/entries/remove.json?id=custom-388061495298244609&tweet_id=390890231215292416`

Example Response¶
-----------------

Success:

```
{
  "response": {
    "errors": [
    ]
  },
  "objects": {
  }
}
```
Failure:

```
{
  "response": {
    "errors": [
      {
        "change": {
          "tweet_id": "390890231215292416",
          "op": "remove"
        },
        "reason": "not_found"
      }
    ]
  },
  "objects": {
  }
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