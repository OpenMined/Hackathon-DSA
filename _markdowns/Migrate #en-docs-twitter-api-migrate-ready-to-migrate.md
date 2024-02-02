



Ready to migrate to Twitter API v2? | Docs | Twitter Developer Platform 





































































































Ready to migrate?



Ready to migrate?
-----------------


In order to use v2 endpoints, you will need the following things:


* A developer account
* A developer App created within a Project
* Keys and tokens from that Project’s developer App


Please note the importance of using keys and tokens from an App within a Project. If you are using keys and tokens from an App outside of a Project, you will not be able to make a request to v2 endpoints.


Once you have a developer account, you can set up all of the above in the developer portal. 






### 


### Authentication


With the new Twitter API, you’ll use two different authentication patterns, OAuth 1.0a User Context and OAuth 2.0 Bearer Token, to access different endpoints. Each serves a different purpose when making requests to the endpoints: 


* OAuth 1.0a User Context is required when making a request on behalf of a Twitter user
* OAuth 2.0 Bearer token is required to make requests on behalf of your developer App


 


### Tools and Code


To help you get started and familiarize yourself with the new endpoints and capabilities we have a few options to jump start your work:


First, we have a Twitter Postman collection that allows you to use the Postman client to make requests of and connect to the individual endpoints. This is a low friction way to test authentication and experiment with the endpoints. It’s important to note the Postman client is best for RESTful endpoints, but you can copy requests to streaming endpoints from the tool and paste them into your command line tool.


If you want to dig deeper, we’ve also provided a list of both Twitter supported and third party libraries in Ruby, Python, Node, Java, and many more. For additional context, take a look at our tools and libraries page.


 


### Migrating to updated endpoints


As you start to explore the new Twitter v2 endpoints, we’ve built a series of detailed migration guides to help you compare and contrast each updated endpoints' capabilities compared to older versions:


* Tweets
* Tweets lookup
* Manage Tweets
* Timelines
* Search Tweets
* Tweet counts
* Filtered stream
* Sampled stream
* Retweets
* Likes
* Hide replies
* Users
* Users lookup
* Follows
* Blocks
* Mutes
* Lists
* List lookup
* Manage Lists
* List Tweet lookup
* List members
* List follows


 






### Migrating to the new data format


As you move from v1.1 or enterprise to v2, it is important to understand that the format the data are delivered in has changed significantly. We have added new fields, modified the sequence of fields, and in some cases removed elements altogether. 


To learn more about these changes, we are developing a series of guides that will help you map out the pre-v2 data format fields to the newer fields, and describe how to request these new fields. 


You can learn more by visiting our data formats migration section of this migration hub, or by visiting our specific data format guides:  




* Native format to Twitter API v2 (standard v1.1)
* Native Enriched to Twitter API v2 (enterprise)
* Activity Streams to Twitter API v2 (enterprise)







What’s next?
-------------


Those of you who have used the platform for some time will notice that many of the new endpoints are aligned with existing standard v1.1, and enterprise endpoints. Indeed, we intend for these to replace all three versions in the future. 


We’ve put together a table to help you understand how the Twitter API endpoints map to previous versions.


If you’d like to see what’s coming next, please visit our product roadmap.


We also have a changelog that you can check out to understand what we have already released.


 


### What should we build next?


As we build out additional capabilities of the Twitter API v2 we want to continue to hear from you. We welcome and encourage feedbackfrom you. 


Take a look at the ideas that have already been submitted, show your support for those that correlate with your needs and provide feedback as well!



















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















