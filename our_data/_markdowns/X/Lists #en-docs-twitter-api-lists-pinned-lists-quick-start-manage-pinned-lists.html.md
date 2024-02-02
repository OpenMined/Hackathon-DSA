
Manage pinned List quick start guide | Docs | Twitter Developer Platform 

Manage pinned List

**Please note:** This guide assumes you have completed the prerequisites from the quick start overview.

### Steps to build a manage pinned List request

#### Step one: Choose the List endpoint collection from Postman

Once you have the Twitter API v2 collection loaded in Postman, navigate to the “List” folder, select another folder “Pinned Lists”, and then choose "Pin a List".  

#### Step two: Specify the List to pin

Manage pinned List endpoints require two IDs: one for the user (the authenticated user to pin a List) and the target List (the List to be pinned). The user’s ID must correspond to the authenticating user’s ID, meaning that you must pass the Access Tokens associated with the user ID when authenticating your request. In this case, you can specify the ID belonging to your user. You can find your ID in two ways:

1. Using the users lookup by username endpoint, you can pass a username and receive the id field.
2. Looking at your Access Token, you will find that the numeric part is your user ID.

The target List ID can be any valid list. In Postman, navigate to the "Params" tab, and enter the user ID into the "Value" column of the id path variable. Navigate to the “Body” tab and ID of the List you wish to pin as the value for the list\_id  parameter. Be sure not to include any spaces before or after any ID.

|  |  |  |
| --- | --- | --- |
| **Key** | **Value** | **Parameter type** |
| `id` | The user ID | path |
| list\_id | The target List ID to be pinned | body |

You should now see a similar URL next to the "Send" button:

```
      https://api.twitter.com/2/users/2244994945/pinned_lists
```

Code copied to clipboard

Step three: Make your request and review your response  

Once you have everything set up, hit the "Send" button, and you will receive a similar response to the following example response:

```
      {
  "data": {
    "pinned": true
  }
}

```

Code copied to clipboard

You have successfully pinned the target List if the returned response object contains a true value for the key pinned. 

To unpin a List, select the Unpin List” request also found in the “Lists” folder of the Twitter API v2 collection loaded in Postman. This endpoint requires the authenticated user ID and the ID of the List to be unpinned. In the “Params” tab, enter the user ID as the value for the id column and ID of the List to be unpinned as the value for the  list\_id column. 

On successful delete request, you will receive a response similar to the following example:

```
      {
  "data": {
    "pinned": false
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