
Twitter API v2 data dictionary | Docs | Twitter Developer Platform 

Introduction

Across the Twitter API endpoints, there are a variety of objects available to request such as Tweets and users. Each GET endpoint will have a top-level resource and object, such as Tweets in recent search and filtered stream, and users in users lookup.

To see each object and it's included fields, please visit the following:

* Tweets
* Users
* Spaces
* Lists
* Media
* Polls
* Places

### Expanded objects

Additional objects related to the top-level object, such as media, place, poll, author (user) of the Tweet, and user's pinned-Tweet are available as expansions, which you can request using the expansions query parameter.   

### Fields: defaults and requesting additional fields

If you make a request without any fields parameters, you will receive just a few default fields for your top-level object and any expansion objects. For example, Tweets will return just the id and text of a Tweet by default. If you would like to request additional fields, such as the Tweet created\_at or lang fields, you will have to use the fields parameters.   

### Key fields

Other useful fields that you should expect in the Twitter API v2 data format:

* Metrics available in the Tweet, user, Spaces, lists objects
* Annotation topics available in the Tweet payload
* A new conversation\_id field to help you track Tweets included in a conversation
* A new reply\_settings field to help you understand who has the ability to reply to specific Tweets

### Migrating to the Twitter API v2 data format

Interested in learning more about how the Twitter API v2 data format compares to standard, premium, or enterprises' formats? Check out our data format comparison guides:

* Standard v1.1 Native format to Twitter API v2 format migration guide
* Native Enriched to Twitter API v2 format migration guide
* Activity Streams to Twitter API v2 format migration guide

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