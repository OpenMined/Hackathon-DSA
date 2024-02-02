



Migration introduction | Docs | Twitter Developer Platform 





































































































Migration introduction



Migration introduction
----------------------


**We retired the Site Streams, User Streams, and standard beta version of the Account Activity API - DM Only products in 2018. If you had been using those products, please make sure to migrate over to the premium or enterprise version of the Account Activity API.**


**We have also retired the legacy Direct Message endpoints. If you had been using those endpoints, please make sure to migrate over to either the new DM endpoints, or to the premium or enterprise version of the Account Activity API.**


**Please review this announcment to learn more.**


Here are the endpoints that will be affected by these changes:  




* User Streams
* Site Streams
* GET direct\_messages
* GET direct\_messages/sent
* GET direct\_messages/show
* POST direct\_messages/new
* POST direct\_messages/destroy


We have new endpoints and services available that provide similar access and, for Direct Messages, some additional functionality:


* Account Activity API enterprise and premium
* GET direct\_messages/events/list
* GET direct\_messages/events/show
* POST direct\_messages/events/new
* POST direct\_messages/events/destroy


To help you make a smooth migration to these new endpoints and services we have two migration guides:


* Account Activity API migration guide for those going from User Streams and Site Streams to our new webhooks based service
* Direct Message migration guide for those migrating between Direct Message REST endpoints


Additionally, we have a series of videos about the Account Activity API and how to get started.


And, finally, we have code samples to further your understanding and help you get started quickly:


* The Account Activity Dashboard is a sample Node.js web app with helper scripts to get started with the Account Activity API.
* SnowBot is a sample chatbot using the Account Activity API and REST Direct Message endpoints. It’s written in Ruby, uses the Sinatra web app framework, and is deployed on Heroku.


If you are building solutions that ingest data and respond in Direct Messages we also have a Building a Customer Engagement Application on Twitter playbook.


 


Next steps
----------


Review our User Streams and Site Streams migration guide


Review our Direct Message API migration guide


Learn more about the Account Activity API



















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















