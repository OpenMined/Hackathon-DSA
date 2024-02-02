
POST collections/entries/move | Docs | Twitter Developer Platform 

POST collections/entries/move

post-collections-entries-move
POST collections/entries/move
=============================

Move a specified Tweet to a new position in a
`curation_reverse_chron` ordered collection.

Resource URL¶
-------------

`https://api.twitter.com/1.1/collections/entries/move.json`

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
| id | required | The identifier of the Collection receiving the Tweet. |  | *custom-388061495298244609* |
| tweet\_id | required | The identifier of the Tweet to add to the Collection. |  | *390839888012382208* |
| relative\_to | required | The identifier of the Tweet used for relative positioning. |  | *614929127313965056* |
| above | optional | Set to *false* to insert the specified *tweet\_id*
below the *relative\_to* Tweet in the collection. Default:
*true* |  | *false* |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/collections/entries/move.json?id=custom-388061495298244609&tweet_id=390839888012382208&relative_to=614929127313965056`

Example Response¶
-----------------

Success:¶
---------

```
{
  "objects": {},
  "response": {
    "errors": []
  }
}
```
Failure:¶
---------

```
{
  "objects": {},
  "response": {
    "errors": [
      {
        "change": {
          "op": "move",
          "tweet_id": "610990849493762050"
        },
        "reason": "not_found"
      }
    ]
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