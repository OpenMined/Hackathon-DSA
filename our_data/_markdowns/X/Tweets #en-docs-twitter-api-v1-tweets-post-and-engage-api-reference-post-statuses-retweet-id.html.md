
POST statuses/retweet/:id | Docs | Twitter Developer Platform 

POST statuses/retweet/:id

post-statuses-retweet-id
POST statuses/retweet/:id
=========================

Retweets a tweet. Returns the original Tweet with Retweet details
embedded.

*Usage Notes*:

* This method is subject to update limits. A HTTP 403 will be returned
if this limit as been hit.
* Twitter will ignore attempts to perform duplicate retweets.
* The retweet\_count will be current as of when the payload is
generated and may not reflect the exact count. It is intended as an
approximation.

Resource URL¶
-------------

`https://api.twitter.com/1.1/statuses/retweet/:id.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 3-hour window | 300\* per user; 300\* per app |

*Please note* - The 300 per 3 hours is a combined limit with
the POST
statuses/update endpoint. You can only post 300 Tweets or Retweets
during a 3 hour period.

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| id | required | The numerical ID of the desired status. |  | *123* |
| trim\_user | optional | When set to either *true* , *t* or *1* , each
tweet returned in a timeline will include a user object including only
the status authors numerical ID. Omit this parameter to receive the
complete user object. |  | *true* |

Example Request¶
----------------

```
$ curl --request POST 
--url 'https://api.twitter.com/1.1/statuses/retweet/TWEET_ID.json' 
--header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
--header 'content-type: application/json'
```
Example Response¶
-----------------

```
{retweet-status-object,
"user": {retweeting-user-object},
"retweeted_status": {retweeted-status-object,
  "user": {retweeted-user-object}
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