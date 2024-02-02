
Setting a default Welcome Message | Docs | Twitter Developer Platform 

Setting a default Welcome Message

Setting a Default Welcome Message
=================================

Without a default Welcome Message, users are presented with an empty Direct Message conversation view or the state of the previous conversation.  A Welcome Message may be set to default so that it is presented to the user when a Welcome Message deeplink is not used. Use a default Welcome Message to provide context to users including what services are provided, when they can receive response or provide Quick Reply options to start an automated conversation flow. All features available to Direct Messages can be used in a default Welcome Message.

When a Welcome Message is set as default, it will be presented to the user in the following scenarios:

* Direct Message compose view opened for the first time.
* Direct Message compose view opened for the first time since leaving a conversation.
* Direct Message compose view opened after no message activity for 7 days.

**Note:** Specifying a Welcome Message in a deeplink will always override the default Welcome Message. Deeplinking without a defined Welcome Message will follow default Welcome Message behavior defined above.

To set a default Welcome Message:

1. Create a new Welcome Message with POST direct\_messages/welcome\_messages/new. Take note of the returned Welcome Message ID.
2. Create a new Welcome Message Rule using the Welcome Message ID with POST direct\_messages/welcome\_messages/rules/new.

**Note:** Although an account can have many Welcome Messages, an account may only have a single “default” Welcome Message and only a single rule. If you have previously created a rule, you must delete the current rule before creating a new one. See POST direct\_messages/welcome\_messages/rules/new documentation for more information regarding the future of rules.  

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