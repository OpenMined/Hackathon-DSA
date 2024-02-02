
POST lists/members/destroy | Docs | Twitter Developer Platform 

POST lists/members/destroy

post-lists-members-destroy
POST lists/members/destroy
==========================

Removes the specified member from the list. The authenticated user
must be the list's owner to remove members from the list.

Resource URL¶
-------------

`https://api.twitter.com/1.1/lists/members/destroy.json`

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
| list\_id | optional | The numerical *id* of the list. |  |  |
| slug | optional | You can identify a list by its slug instead of its numerical id. If
you decide to do so, note that you'll also have to specify the list
owner using the *owner\_id* or *owner\_screen\_name*
parameters. |  |  |
| user\_id | optional | The ID of the user to remove from the list. Helpful for
disambiguating when a valid user ID is also a valid screen name. |  |  |
| screen\_name | optional | The screen name of the user for whom to remove from the list.
Helpful for disambiguating when a valid screen name is also a user
ID. |  |  |
| owner\_screen\_name | optional | The screen name of the user who owns the list being requested by a
*slug* . |  |  |
| owner\_id | optional | The user ID of the user who owns the list being requested by a
*slug* . |  |  |

Example Request¶
----------------

`POST https://api.twitter.com/1.1/lists/members/destroy?screen_name=episod&slug=cool_people&owner_screen_name=twitter`

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