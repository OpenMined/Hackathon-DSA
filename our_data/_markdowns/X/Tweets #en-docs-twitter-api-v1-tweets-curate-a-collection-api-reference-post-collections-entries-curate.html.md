
POST
collections/entries/curate | Docs | Twitter Developer Platform 

POST
collections/entries/curate

post-collections-entries-curate
POST
collections/entries/curate
===============================

Curate a Collection by adding or removing Tweets in bulk. Updates
must be limited to 100 cumulative additions or removals per request.

Use POST
collections / entries / add and POST
collections / entries / remove to add or remove a single Tweet.

Resource URL¶
-------------

`https://api.twitter.com/1.1/collections/entries/curate.json`

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

Example Request¶
----------------

`POST https://api.twitter.com/1.1/collections/entries/curate.json`

Example Response¶
-----------------

```
POST /1.1/collections/entries/curate.json
Content-Type: application/json
Content-Length: 226
```

```
{"id":"custom-388061495298244609","changes":[{"op":"add","tweet_id":"390897780949925889"},{"op":"add","tweet_id":"390853164611555329"},{"op":"add","tweet_id":"390892747810295808"},{"op":"add","tweet_id":"390898463090561024"}]} 
```
Success:¶
---------

```
{"objects":{},"response":{"errors":[]}}
```
Failure:¶
---------

```
{"objects":{},"response":{"errors":[{"reason":"duplicate","change":{"op":"add","tweet_id":"390897780949925889"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390853164611555329"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390892747810295808"}},{"reason":"duplicate","change":{"op":"add","tweet_id":"390898463090561024"}}]}}
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