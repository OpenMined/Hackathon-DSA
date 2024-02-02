
Manage List members quick start guide | Docs | Twitter Developer Platform 

Manage List members

**Please note:** This guide assumes you have completed the prerequisites from the quick start overview.

### Steps to build a manage List member request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “List members”, and then choose "Add a member".  

#### Step two: Specify the user to add

Manage List member endpoints require two IDs: the ID of the List and the ID of the user to add. You can find the user’s ID using the users lookup and pass a username to receive the id field.

The target ID can be any valid user ID. In Postman, navigate to the "Params" tab, and enter your ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the user you wish to add as the value for the user\_id parameter. Be sure not to include any spaces before or after any ID.

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The List ID | path |
| user\_id | The target user ID you wish to add as a member | body |

You should now see a similar URL next to the "Send" button:

```
      https://api.twitter.com/2/lists/1441162269824405510/members
```

Code copied to clipboard

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

```
      {
  "data": {
    "is_member": true
  }
}

```

Code copied to clipboard

If the returned response object contains a true value for the key is\_member, you have successfully added the user as a member of the List. 

To remove a member from a List, select the “Remove a member” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the ID of the List and the user ID of the member you wish to remove. In the “Params” tab, enter the ID of the List as the value for the id column and ID of the user to be removed as the value for the  user\_id column. 

On successful delete request, you will receive a response similar to the following example:

```
      {
  "data": {
    "is_member": false
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