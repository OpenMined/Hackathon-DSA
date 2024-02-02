
GET users/show | Docs | Twitter Developer Platform 

GET users/show

get-users-show
GET users/show
==============

Returns a variety of
information about the user specified by the required
`user_id` or `screen_name` parameter. The author's
most recent Tweet will be returned inline when possible.

GET
users / lookup is used to retrieve a bulk collection of user
objects.

You must be following a protected user to be able to see their most
recent Tweet. If you don't follow a protected user, the user's Tweet
will be removed. A Tweet will not always be returned in the
current\_status field.

Resource URL¶
-------------

`https://api.twitter.com/1.1/users/show.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 900 |
| Requests / 15-min window (app auth) | 900 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | required | The ID of the user for whom to return results. Either an id or
screen\_name is required for this method. |  | *12345* |
| screen\_name | required | The screen name of the user for whom to return results. Either a id
or screen\_name is required for this method. |  | *noradio* |
| include\_entities | optional | The *entities* node will not be included when set to
*false*. |  | *false* |

Example Request¶
----------------

```
$ curl --request GET 
    --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
    --header 'authorization: Bearer <bearer>'
```

```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/users/show.json?screen_name=twitterdev' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
  oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
  oauth_version="1.0"'
```

```
$ twurl /1.1/users/show.json?screen_name=twitterdev
```
Example Response¶
-----------------

```
{user-object}
```
For more detail, see the user-object
definition.

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