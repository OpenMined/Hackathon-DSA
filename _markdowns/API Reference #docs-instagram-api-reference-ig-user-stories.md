
Stories - Instagram Platform - Documentation - Meta for Developers









Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Stories
=======


Represents a collection of story IG Media objects on an IG User.


Creating
--------


For creating Stories Media, refer to the Instagram User Media documentation.


Reading
-------


### Getting Stories


`GET /{ig-user-id}/stories`


Returns a list of story IG Media objects on an IG User.


#### Limitations


* Responses will not include Live Video stories.
* Stories are only available for 24 hours.
* New stories created when a user reshares a story will not be returned.


#### Permissions


A Facebook User access token with the following permissions:


* `instagram_basic`
* `instagram_manage_insights`
* `pages_read_engagement`
* `pages_show_list`


If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:


* `ads_management`
* `pages_read_engagement`
* `business_management`


#### Sample Request



```
GET graph.facebook.com
  /17841405822304914/stories
```
#### Sample Response



```
{
  "data": [
    {
      "id": "17861937508009798"
    },
    {
      "id": "17862253585030136"
    },
    {
      "id": "17856428680064034"
    },
    {
      "id": "17862537148046301"
    },
    {
      "id": "17852121721080875"
    },
    {
      "id": "17862694123018235"
    }
  ]
}
```
Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
