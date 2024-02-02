
GET custom\_profiles/list | Docs | Twitter Developer Platform 

GET custom\_profiles/list

get-profile-list
GET custom\_profiles/list
=========================

Retrieves all custom profiles for the authenticated account. Default
page size is 20.

Resource URL¶
-------------

`https://api.twitter.com/1.1/custom_profiles/list.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 24 hour window (user auth) | Yes (180 / 15 min) |

Parameters¶
-----------

|  |  |
| --- | --- |
| **count** (optional) | Number of custom profile objects to be returned. Max of 50. Default
is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page. Use the
`next_cursor` property returned from the previous
request. |

*Note:* In rare cases a response may contain an empty custom
profile object with `next_cursor` defined. The presence of a
`next_cursor` property in the response indicates there are
more custom profiles to retrieve.

Example request using Twurl¶
----------------------------

```
twurl -X GET /1.1/custom_profiles/list.json?count=2&cursor=MTIzNDU2Nzg
```
Example Response¶
-----------------

```
{
  "custom_profiles": [
    {
      "id": "100001",
      "created_timestamp": "1479767168196",
      "name": "Carol",
      "avatar": {
        "media": {
          "url": "https://pbs.twimg.com/some_img/987654321/ABC?format=jpg&name=normal"
        }
      }
    },
    {
      "id": "100002",
      "created_timestamp": "1479767168197",
      "name": "Andy",
      "avatar": {
        "media": {
          "url": "https://pbs.twimg.com/some_img/56565656/DEF?format=jpg&name=normal"
        }
      }
    }
 ],
 "next_cursor": "NDUzNDUzNDY3Nzc3"
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