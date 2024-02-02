
Integrating compliance streams | Docs | Twitter Developer Platform 

Integrating compliance streams

The Tweet and User compliance streams are realtime streaming endpoints that delivers compliance events that occur on the Twitter platform. For an understanding of compliance events and how they are generated on Twitter, please reference our article, Honoring User Intent on Twitter.

It is important to note that Tweet and User events are delivered independently and that each should be processed independently (i.e. a Tweet delete doesn’t imply a User event, and vice versa.) Several User events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.

User\_deletes are followed by Tweet deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their Tweets 30 days later do not occur.

User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.

It is never suitable to display compliance events directly to users of your software or to otherwise incorporate them into your products or customer experiences. They are intended solely for maintaining compliance and honoring the actions of Twitter users.

Integrating the compliance streams
----------------------------------

To integrate the compliance streams into your system, you will need to build an integration that can do the following:

1. Establish a streaming connection to each streaming endpoint partition of the compliance streams. The Tweet and User streams are both split into 4 partitions, and a connect must be established for each partition.
2. Handle high data volumes – de-couple stream ingestion from additional processing using asynchronous processes
3. Reconnect to the stream partitions automatically when disconnected for any reason. After a disconnection, reconnect using the 'backfill\_minutes' request parameter to avoid missing any events. Your system needs to be tolerant of duplicate events.
4. Process compliance events that are relevant to Tweet and User data you have stored in accordance with the guidance presented above

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