



List object | Docs | Twitter Developer Platform 





































































































List object



List
----


The list object contains Twitter Lists metadata describing the referenced List. The List object is the primary object returned in the List lookup endpoint. When requesting additional List fields on this endpoint, simply use the fields parameter `list.fields`.


At the moment, the List object cannot be found as a child object from any other data object. However, user objects can be found and expanded in the user resource. These objects are available for expansion by adding owner\_id to the expansions query parameter. Use the expansion with the field parameter: `list.fields` when requesting additional fields to complete the primary List object and user.fields to complete the expansion object.  

 




| Field value | Type | Description | How it can be used |
| --- | --- | --- | --- |
| id (default) | string | The unique identifier of this List.
`"id": "2244994945"` | Use this to programmatically retrieve information about a specific Twitter List. |
| name (default) | string | The name of the List, as defined when creating the List. 
`"name": "Twitter Lists"` |  |
| created\_at | date (ISO 8601) | The UTC datetime that the List was created on Twitter.
`"created_at": "2013-12-14T04:35:55.000Z"` | Can be used to determine how long a List has been on Twitter |
| description | string | A brief description to let users know about the List.
`"description": "People that are active members of the Bay area cycling community on Twitter."` |  |
| follower\_count  | integer | Shows how many users follow this List,
"follower\_count": 198 |  |
| member\_count | integer | Shows how many members are part of this List.
"member\_count": 60 |  |
| private | boolean | Indicates if the List is private.
"private": false |  |
| owner\_id | string | Unique identifier of this List's owner.
`"owner_id": "1255542774432063488"` | Returns the List owner ID. Can potentially be used to find out if this specifc user owns any other Lists.
Can also be used to expand user objects. |  |






### 


### Retrieving a user object


#### Sample Request


In the following request, we are requesting fields for the user on the List lookup by ID endpoint. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

 












```

      curl --request GET 'https://api.twitter.com/2/lists/1355797419175383040?list.fields=created_at,description,private,follower_count,member_count,owner_id&expansions=owner_id' --header 'Authorization: Bearer $BEARER_TOKEN'

    
```





Code copied to clipboard








#### 
Sample Response












```

      {
  "data": {
    "name": "Twitter Comms",
    "member_count": 60,
    "id": "1355797419175383040",
    "private": false,
    "description": "",
    "follower_count": 198,
    "owner_id": "257366942",
    "created_at": "2021-01-31T08:37:48.000Z"
  },
  "includes": {
    "users": [
      {
        "created_at": "2011-02-25T07:51:26.000Z",
        "name": "Ashleigh Hay 🤸🏼‍♀️",
        "id": "257366942",
        "username": "shleighhay",
        "verified": false
      }
    ]
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















