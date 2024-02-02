
POST
lists/members/destroy\_all | Docs | Twitter Developer Platform 

POST
lists/members/destroy\_all

post-lists-members-destroy\_all
POST
lists/members/destroy\_all
===============================

Removes multiple members from a list, by specifying a comma-separated
list of member ids or screen names. The authenticated user must own the
list to be able to remove members from it. Note that lists can't have
more than 500 members, and you are limited to removing up to 100 members
to a list at a time with this method.

Please note that there can be issues with lists that rapidly remove
and add memberships. Take care when using these methods such that you
are not too rapidly switching between removals and adds on the same
list.

Resource URL¶
-------------

`https://api.twitter.com/1.1/lists/members/destroy_all.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes |
| Rate limited? | Yes |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| list\_id | required | The numerical *id* of the list. |  |  |
| slug | required | You can identify a list by its slug instead of its numerical id. If
you decide to do so, note that you'll also have to specify the list
owner using the *owner\_id* or *owner\_screen\_name*
parameters. |  |  |
| user\_id | optional | A comma separated list of user IDs, up to 100 are allowed in a
single request. |  |  |
| screen\_name | optional | A comma separated list of screen names, up to 100 are allowed in a
single request. |  |  |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug* . |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug* . |  |  |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/lists/members/destroy_all.json?screen_name=rsarver,episod,jasoncosta,theseancook,kurrik,froginthevalley&list_id=23`

Example Response¶
-----------------

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