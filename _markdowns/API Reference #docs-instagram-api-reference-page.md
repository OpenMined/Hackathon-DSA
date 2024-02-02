
Page - Instagram Platform - Documentation - Meta for Developers









Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
Page
====


Represents a Facebook Page.


This node allows you to:


* get the IG User connected to a Facebook Page.


Creating
--------


This operation is not supported.


Reading
-------


### Getting a Page's IG User


`GET /{page-id}?fields=instagram_business_account`


Returns the IG User connected to the Facebook Page.


#### Permissions


A Facebook User access token with the following permissions:


* `instagram_basic`
* `pages_show_list`


If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:


* `ads_management`
* `pages_read_engagement`
* `business_management`


#### Sample Request



```
GET graph.facebook.com
  /134895793791914?fields=instagram_business_account
```
#### Sample Response



```
{
  "instagram_business_account": {
    "id": "17841405822304914"
  },
  "id": "134895793791914"
}
```
Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
