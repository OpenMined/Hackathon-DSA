
GET
direct\_messages/welcome\_messages/rules/list | Docs | Twitter Developer Platform 

GET
direct\_messages/welcome\_messages/rules/list

list-welcome-message-rules
GET
direct\_messages/welcome\_messages/rules/list
=================================================

Returns a list of Welcome Message Rules.

Resource URL¶
-------------

`https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/list.json`

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

|  |  |
| --- | --- |
| **count** (optional) | Number of welcome message rules to be returned. Max of 50. Default
is 20. |
| **cursor** (optional) | For paging through result sets greater than 1 page, use the
“next\_cursor” property from the previous request. |

Example request using Twurl¶
----------------------------

```
twurl -X GET "/1.1/direct_messages/welcome_messages/rules/list.json?count=2&cursor=MTIzNDU2Nzg"
```
Example Responses¶
------------------

Welcome message rules are returned in the
`welcome_message_rules` array. A `next_cursor`
property will be returned if there are more welcome message rules to be
retrieved.

> 
> **Note**
> 
> 
> To determine if there are more welcome message rules to retrieve,
> always look for the presence of a `next_cursor`. In rare
> cases the `welcome_message_rules` array may be empty.
> 
> 
> 

```
{
  "welcome_message_rules": [
    {
      "id": "9910934913490319",
      "created_timestamp": "1470182394258",
      "welcome_message_id": "844385345234"
    },
    {
      "id": "9910934913490431",
      "created_timestamp": "1470182394265",
      "welcome_message_id": "844385345238"
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