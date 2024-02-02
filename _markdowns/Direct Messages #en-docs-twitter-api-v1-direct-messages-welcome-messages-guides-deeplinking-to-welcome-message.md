



Deeplinking to a Welcome Message | Docs | Twitter Developer Platform 





































































































Deeplinking to a Welcome Message



Deeplinking to a Welcome Message
================================


Every Welcome Message can be deeplinked to. When a user follows the deeplink, the Direct Message compose view will be opened with the specified Welcome Message presented. Deeplinks can be used anywhere from a website, an app, a Tweet or even another Direct Message conversation.


To create a Welcome Message deeplink:


1. Create a new Welcome Message with POST direct\_messages/welcome\_messages/new. Take note of the returned Welcome Message ID.
2. Construct a Direct Message deeplink with the recipient\_id and welcome\_message\_id query string parameters defined.


Example Direct Message Deeplink:  




https://twitter.com/messages/compose?recipient\_id= 3805104374&welcome\_message\_id=12345


**Note:** You can create as many Welcome Messages as you require and all Welcome Messages can be deeplinked to.


Deeplinking from a Tweet
------------------------


By simply including the Direct Message deeplink URL at the end of a Tweet, your can append a "Send a private message" button to the bottom of the Tweet. Read more about using Direct Message deeplinks in Tweets in this blog post.


Using a Direct Message Card, businesses can capture people’s attention with engaging image or video creatives, and include up to four fully customizable call-to-action buttons. Each call-to-action button can deeplink to a unique Welcome Message. The Direct Message Card is currently available in limited beta to Twitter advertisers. Contact your Twitter representative for more information.  




Deeplinking from a Website
--------------------------


Direct Message deeplinks may also be used to deeplink from a website or other external source like a mobile app. For more details on deeplinking to Welcome Messages from a website, see Message Button documentation.  





















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















