
GET users/profile\_banner | Docs | Twitter Developer Platform 

GET users/profile\_banner

get-users-profile\_banner
GET users/profile\_banner
=========================

Returns a map of the available size variations of the specified
user's profile banner. If the user has not uploaded a profile banner, a
HTTP 404 will be served instead. This method can be used instead of
string manipulation on the `profile_banner_url` returned in
user objects as described in Profile
Images and Banners.

The profile banner data available at each size variant's URL is in
PNG format.

Resource URL¶
-------------

`https://api.twitter.com/1.1/users/profile_banner.json`

Resource Information¶
---------------------

|  |  |
| --- | --- |
| Response formats | JSON |
| Requires authentication? | Yes (user context only) |
| Rate limited? | Yes |
| Requests / 15-min window (user auth) | 180 |

Parameters¶
-----------

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Name | Required | Description | Default Value | Example |
| user\_id | optional | The ID of the user for whom to return results. Helpful for
disambiguating when a valid user ID is also a valid screen name. |  | *12345* |
| screen\_name | optional | The screen name of the user for whom to return results. Helpful for
disambiguating when a valid screen name is also a user ID. |  | *noradio* |

Example Request¶
----------------

`GET https://api.twitter.com/1.1/users/profile_banner.json?screen_name=twitterapi`

Example Response¶
-----------------

```
{
  "sizes": {
    "ipad": {
      "h": 313,
      "w": 626,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad"
    },
    "ipad_retina": {
      "h": 626,
      "w": 1252,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/ipad_retina"
    },
    "web": {
      "h": 260,
      "w": 520,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web"
    },
    "web_retina": {
      "h": 520,
      "w": 1040,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/web_retina"
    },
    "mobile": {
      "h": 160,
      "w": 320,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile"
    },
    "mobile_retina": {
      "h": 320,
      "w": 640,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/mobile_retina"
    },
    "300x100": {
      "h": 100,
      "w": 300,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/300x100"
    },
    "600x200": {
      "h": 200,
      "w": 600,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/600x200"
    },
    "1500x500": {
      "h": 500,
      "w": 1500,
      "url": "https://pbs.twimg.com/profile_banners/6253282/1347394302/1500x500"
    }
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