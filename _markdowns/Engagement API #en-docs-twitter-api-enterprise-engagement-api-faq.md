



FAQ | Docs | Twitter Developer Platform 





































































































FAQ



Frequently asked questions
--------------------------


Enterprise


### Engagement API


**How can I access the Engagement API?**


Access to the Engagement API is provisioned through an enterprise subscription.  Please fill out this form to get in touch with our sales team.  

 


**How is my usage tracked by '@handle'?**


If your contract includes a limit for the number of unique handles that can be used with Engagement API.  The internal Twitter system will keep track of the number of Authenticated users owning Tweets that are queried with the Engagement API.  Customers should also keep track of this unique number on the client side.  Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.


 


**Can I check my @handle usage for Engagement API?**


Currently, there is no usage API or UI to check the @handle usage for the Engagement API.  The system will not block overages if there are more @handles requested than what is contracted.  At the end of the billing month, the number of unique @handles queried is compared to the contracted amount and an overage will be charged in accordance with the contract terms.


 


**The `engagements` metadata field returned in the payload is not equal to the sum of all the various engagement metric totals. Why is this the case?**


This is to be expected. The `engagements` metadata field may not always correlate with the sum of all individual engagement metrics returned by the API. This is because the `engagements` metadata field may include additional engagements that do not have specific metrics broken out in the payload. Said another way, adding all of the various engagement metric totals together may not equal the value you are seeing in the `engagements` metric field that is returned to you in the payload.


You can think of the `engagements` metadata field as any click or interaction made on the Tweet.  

 


**The `url_clicks` field in the payload response is returning a number, when in fact the Tweet does not have a URL. How is this possible?**


This may be because a Tweet that contains something like a hashtag (that creates a link to another page) will count as a URL click if it is clicked on by a user.  

 


**Why can I not receive engagement data for a specific Tweet?**


There are various reasons why you might not be able to retrieve engagement data for a specific Tweet, including:


* The Tweet ID or IDs you have requested are not available based on the authentication token you are using to retrieve data on behalf of a third party.
* The Tweet ID or IDs you have requested specific to the /totals endpoint are not 90 days or newer and are thus not available for returning the impressions or engagement metrics.
* The Tweet ID or IDs you have requested are no longer available, usually indicating that they have been deleted or are no longer publicly available for another reason.


Please review the different error messages that you will likely receive in any of the above cases.  

 


**How can I handle rate limiting with the Engagement API?**


You can use the `x-per-minute-limit` and `x-per-minute-remaining` information returned by the response header when you make a request to the Engagement API to monitor your consumption.  

  

`x-per-minute-limit` tells you what your allowance is and `x-per-minute-remaining` tells you how many calls you have left.  




### 
Error troubleshooting guide


**I am having problems authenticating**


Please make sure to review our guidelines on authenticating with the Engagement API.  

 


**I have passed the correct consumer key and secret, as well as access token and access token secret, but the following error is being returned. What can I do?**



```

[
    Your account could not be authenticated. Reason: Unknown Authorization Type;
]

```

  

Make sure not to use any access tokens or secrets when you try and authenticate with the /totals endpoint. This is because if you do include these tokens, and are attempting to pull content from a Tweet not associated with these tokens, you will likely receive an error such as:



```

[
    Forbidden to access tweets: 1054424731825229824;
]

```

### 

Still can't find what you're looking for?


**I have a question that hasn't yet been answered**


Please reach out to technical support and we will respond to you promptly.



















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















