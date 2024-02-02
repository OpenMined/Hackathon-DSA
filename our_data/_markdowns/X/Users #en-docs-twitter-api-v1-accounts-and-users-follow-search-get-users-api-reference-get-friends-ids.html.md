
GET friends/ids | Docs | Twitter Developer Platform 

GET friends/ids

get-friends-ids
GET friends/ids
===============

Returns a cursored collection of user IDs for every user the
specified user is following (otherwise known as their "friends").

At this time, results are ordered with the most recent following
first — however, this ordering is subject to unannounced change and
eventual consistency issues. Results are given in groups of 5,000 user
IDs and multiple "pages" of results can be navigated through using the
`next_cursor` value in subsequent requests. See Using cursors to navigate
collections for more information.

This method is especially powerful when used in conjunction with GET
users / lookup, a method that allows you to convert user IDs into
full user
objects in bulk.

Resource URL¶
-------------

`https://api.twitter.com/1.1/friends/ids.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15 |
| Requests / 15-min window (app auth) | 15 |

Parameters¶
-----------

| Name | Required | Description | Default Value | Example |
| --- | --- | --- | --- | --- |
| user\_id | optional | The ID of the user for whom to return results. |  | `12345` |
| screen\_name | optional | The screen name of the user for whom to return results. |  | `noradio` |
| cursor | semi-optional | Causes the list of connections to be broken into pages of no more
than 5000 IDs at a time. The number of IDs returned is not guaranteed to
be 5000 as suspended users are filtered out after connections are
queried. If no cursor is provided, a value of `-1` will be
assumed, which is the first "page."The response from the API will
include a `previous_cursor` and `next_cursor` to
allow paging back and forth. See Using cursors to navigate
collections for more information. | `-1` | `12893764510938` |
| stringify\_ids | optional | Some programming environments will not consume Twitter IDs due to
their size. Provide this option to have IDs returned as strings instead.
More about Twitter IDs. | `false` | `true` |
| count | optional | Specifies the number of IDs attempt retrieval of, up to a maximum of
5,000 per distinct request. The value of `count` is best
thought of as a limit to the number of results to return. When using the
count parameter with this method, it is wise to use a consistent count
value across all requests to the same user's collection. Usage of this
parameter is encouraged in environments where all 5,000 IDs constitutes
too large of a response. |  | `2048` |

Example Request¶
----------------

```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
  --header 'authorization: Bearer <bearer>'
```

```
$ curl --request GET 
  --url 'https://api.twitter.com/1.1/friends/ids.json?screen_name=twitterdev' 
  --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app", 
  oauth_nonce="generated-nonce", oauth_signature="generated-signature", 
  oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp", 
  oauth_version="1.0"'
```

```
$ twurl /1.1/friends/ids.json?screen_name=twitterdev
```
Example Response¶
-----------------

```
{
  "previous_cursor": 0,
  "ids": [
    657693,
    183709371,
    7588892,
    38895958,
    22891211,
    9019482,
    14488353,
    11750202,
    12249,
    22915745,
    1249881,
    14927800,
    1523501,
    22548447,
    15062340,
    133031077,
    17874544,
    777925,
    4265731,
    27674040,
    26123649,
    9576402,
    821958,
    7852612,
    819797,
    1401881,
    8285392,
    9160152,
    795649,
    3191321,
    783214
  ],
  "previous_cursor_str": "0",
  "next_cursor": 0,
  "next_cursor_str": "0"
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