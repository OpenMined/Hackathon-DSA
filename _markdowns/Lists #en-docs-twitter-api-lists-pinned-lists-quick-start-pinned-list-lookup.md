



Pinned List lookup quick start guide | Docs | Twitter Developer Platform 





































































































Pinned List lookup








**Please note:** This guide assumes you have completed the prerequisites from the quick start overview.









### Steps to build a pinned List lookup request


#### Step one: Choose the List endpoint collection from Postman


Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "User's pinned Lists".  

 


#### Step two: Identify and specify the user


In order to retrieve a user’s pinned List, you must specify their user ID within the request. The user ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this example, you can specify the ID belonging to your own user. You can find your ID in two ways:


1. Using the users lookup by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.


 


In Postman, navigate to the "Params" tab and enter this user ID into the "Value" column of the `id` parameter.


 




|  |  |
| --- | --- |
| **Key** | **Value** |
| `id` | 2244994945 (user ID) |


 


#### Step three: Identify and specify which fields you would like to retrieve


If you click the "Send" button after step three, you will receive the default List object fields in your response: `id` and `name`.


If you would like to receive additional fields beyond `id` and `name`, you will have to specify those fields in your request with the `field` and/or `expansion` parameters.


For this exercise, we will request a three additional sets of fields from different objects:


* The additional `follower_count` field in the primary List object.
* The full user object using the expansion parameter.
* The additional  `tweet.created_at` field in the associated user object.


In Postman, navigate to the "Params" tab and add the following key:value pair to the "Query Params" table:




|  |  |  |
| --- | --- | --- |
| Key | Value | Returned fields |
| list.fields | follower\_count |  `follower_count` |
| expansions | owner\_id |  `includes.users.id, 
 includes.users.name,
 includes.users.username` |
| user.fields | created\_at |  `includes.users.created_at` |


You should now see a similar URL next to the “Send” button:


 












```

      https://api.twitter.com/2/users/2244994945/pinned_lists?expansions=owner_id&list.fields=follower_count&user.fields=created_at
    
```





Code copied to clipboard








Step four: Make your request and review your response  




Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:












```

      {
  "data": [
    {
      "follower_count": 0,
      "id": "1454155907651158017",
      "name": "test list",
      "owner_id": "2244994945"
    }
  ],
  "includes": {
    "users": [
      {
        "username": "TwitterDev",
        "id": "2244994945",
        "created_at": "2013-12-14T04:35:55.000Z",
        "name": "Twitter Dev"
      }
    ]
  },
  "meta": {
    "result_count": 1
  }
}
    
```





Code copied to clipboard












Next steps
----------






Customize your request using the API Reference


Reach out to the community for help



















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















