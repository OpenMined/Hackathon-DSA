



Manage Lists quick start guide | Docs | Twitter Developer Platform 





































































































Quick start



Getting started with the manage Lists endpoint group
----------------------------------------------------


This quick overview will help you make your first request to the manage List endpoints using Postman.


If you would like to see sample code in different languages, please visit our Twitter API v2 sample code GitHub repository. 


**Note:**For this example, we will make a request to the *Create a List* endpoint, but you can apply the learnings from this quick start to other manage requests as well.











### Prerequisites


To complete this guide, you will need to have a set of keys and tokens to authenticate your request. You can generate these keys and tokens by following these steps:


* Sign up for a developer account and receive approval.
* Create a Project and an associated developer App in the developer portal.
* Navigate to your App's “Keys and tokens” page to generate the required credentials. Make sure to save all credentials in a secure location.









### 


### Steps to build a manage List request


Step one: Start with a tool or library
--------------------------------------


There are several different tools, code examples, and libraries that you can use to make a request to this endpoint, but we will use the Postman tool here to simplify the process.


To load the Twitter API v2 Postman collection into your environment, please click on the following button:





Add Twitter API v2 to Postman



Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Manage List”, and then choose "Create a List".


#### Step two: Authenticate your request


To properly make a request to the Twitter API, you need to verify that you have permission to do so. To do this with the manage Tweets endpoints, you must authenticate your request using either OAuth 1.0a User Context or OAuth 2.0 Authorization Code with PKCE.


In this example, we are going to use OAuth 1.0a User Context.


You must add your keys and tokens (and specifically your API Key, API Secret Key, OAuth 1.0a user Access Token, and OAuth 1.0a user Access Token Secret) to Postman. You can do this by selecting the environment named “Twitter API v2” (in the top-right corner of Postman), and adding your keys and tokens to the "initial value" and "current value" fields (by clicking the eye icon next to the environment dropdown).


If you've done this correctly, these variables will automatically be pulled into the request's authorization tab.  

 






### Step three: Specify the name for the new List


When creating a new List with this endpoint, a name for the List is a required body parameter. Optionally, you can provide a description and specify whether the List is private.


In Postman, navigate to the “Body” tab and enter the name of the List as the value for the name parameter. Additionally, if you wish to add a description for the List, simply add a new key labeled description in the same fashion as the name, followed by the description of the List as the value. Making a List private will follow the same pattern, but only true or false values are accepted for this parameter. 


 




|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `name` | Name of the list (required) | body |
| description | Description for the list (optional) | body |
| private | true or false (optional) | body |


 


You should now see a similar URL next to the "Send" button:












```

      https://api.twitter.com/2/lists
    
```





Code copied to clipboard








Step four: Make your request and review your response  




Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:












```

      {
  "data": {
    "id": "1441162269824405510",
    "name": "New list created from Postman"
  }
}

    
```





Code copied to clipboard








If the returned response object contains an id and the name of your List, you have successfully created the List. 


To delete a List, select the “Delete a List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List you wish to delete. In the “Params” tab, enter the ID of the List you wish to delete as the value for the id column. 


On successful delete request, you will receive a response similar to the following example: 


 












```

      {
  "data": {
    "deleted": true
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















