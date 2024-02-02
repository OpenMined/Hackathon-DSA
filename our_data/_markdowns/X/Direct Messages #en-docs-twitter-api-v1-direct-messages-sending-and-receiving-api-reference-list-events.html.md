
GET
direct\_messages/events/list | Docs | Twitter Developer Platform 

GET
direct\_messages/events/list

list-events
GET
direct\_messages/events/list
================================

Returns all Direct Message events (both sent *and* received)
within the last 30 days. Sorted in reverse-chronological order.

Resource URL¶
-------------

`https://api.twitter.com/1.1/direct_messages/events/list.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 15/user |

Parameters¶
-----------

|  |  |
| --- | --- |
| **count** (optional) | Max number of events to be returned. 20 default. 50 max. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the
“next\_cursor” property from the previous request. |

Example request using Twurl¶
----------------------------

```
twurl -X GET /1.1/direct_messages/events/list.json
```
Example Response¶
-----------------

Events are returned in the `events` array. A
`next_cursor` property will be returned if there are more
events to be retrieved.

> 
> **Note**
> 
> 
> To determine if there are more event to retrieve, always look for the
> presence of a `next_cursor`. In rare cases the
> `events` array may be empty.
> 
> 
> 

```
{
  "next_cursor": "AB345dkfC",
  "events": [
    { "id": "110", "created_timestamp": "5300", ... },
    { "id": "109", "created_timestamp": "5200", ... },
    { "id": "108", "created_timestamp": "5200", ... },
    { "id": "107", "created_timestamp": "5200", ... },
    { "id": "106", "created_timestamp": "5100", ... },
    { "id": "105", "created_timestamp": "5100", ... },
    ...
  ]
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