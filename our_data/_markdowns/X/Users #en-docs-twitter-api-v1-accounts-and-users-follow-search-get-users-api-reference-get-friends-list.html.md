
GET friends/list | Docs | Twitter Developer Platform 

GET friends/list

get-friends-list
GET friends/list
================

Returns a cursored collection of user objects for every user the
specified user is following (otherwise known as their "friends").

At this time, results are ordered with the most recent following
first — however, this ordering is subject to unannounced change and
eventual consistency issues. Results are given in groups of 20 users and
multiple "pages" of results can be navigated through using the
`next_cursor` value in subsequent requests. See Using cursors to navigate
collections for more information.

Resource URL¶
-------------

`https://api.twitter.com/1.1/friends/list.json`

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
| cursor | semi-optional | Causes the results to be broken into pages. If no cursor is
provided, a value of `-1` will be assumed, which is the first
"page."The response from the API will include a
`previous_cursor` and `next_cursor` to allow
paging back and forth. See Using
cursors to navigate collections for more information. | `-1` | `12893764510938` |
| count | optional | The number of users to return per page, up to a maximum of 200. | `20` | `42` |
| skip\_status | optional | When set to either `true`, `t` or
`1` statuses will not be included in the returned user
objects. | `false` | `false` |
| include\_user\_entities | optional | The user object `entities` node will not be included when
set to `false`. | `true` | `false` |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=twitterapi&skip_status=true&include_user_entities=false`

Example Response¶
-----------------

```
{
"users": [
      {user-object},
      {user-object},
      {user-object}
  ],
  "previous_cursor": 0,
  "previous_cursor_str": "0",
  "next_cursor": 1333504313713126852,
  "next_cursor_str": "1333504313713126852"
}
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