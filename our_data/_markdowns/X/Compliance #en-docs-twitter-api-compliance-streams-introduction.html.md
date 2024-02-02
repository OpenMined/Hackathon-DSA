
Compliance streams | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Twitter is committed to our community of developers who build with the Twitter API. As part of this commitment, we aim to make our API open and fair to developers, safe for people on Twitter, and beneficial for the Twitter platform as a whole. It is crucial that any developer who stores Twitter content offline, ensures the data reflects user intent and the current state of content on Twitter. For example, when someone on Twitter deletes a Tweet or their account, protects their Tweets, edits a Tweet, or scrubs the geo information from their Tweets, it is critical for both Twitter and our developers to honor that person’s expectations and intent.

Real-time streams of compliance events provide developers the tools to maintain Twitter data in compliance with the Twitter Developer Agreement and Policy. 

There are two c*ompliance event* streams, one for *Tweet compliance* events, and one for *User compliance* events. These streams are available with Enterprise access and are designed to help partners that ingest high volumes of data 'listen' for compliance events such as Tweet edit events.

These streams provide the following events: 

**Tweet compliance stream:**

* delete - indicates that the Tweet was deleted.
* tweet\_edit - indicates a Tweet has been edited and provides the ID of the updated Tweet.
* withheld - indicates that the Tweet has been withheld from one or more countries.
* drop - indicates that the Tweet should be removed from public view.
* undrop - indicates that the Tweet may be displayed again and treated as public.

**User compliance stream:**  

* user\_delete - indicates that the User account was deleted
* user\_undelete - indicates that the User account was undeleted
* user\_protect - indicates that the User account became private
* user\_unprotect - indicates that the User account became public
* user\_withheld - indicates that the User account has been withheld from one or more countries.
* user\_suspend - indicates that the User account was suspended
* user\_unsuspend - indicates that the User account was unsuspended
* user\_profile\_modification - indicates that the User profile has been updated. This includes an updated description, name, location, and URL.

* ****scrub\_geo**** - indicates that the location information associated with the User was removed

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

Quick start

Jump to example requests

Python client

Run in Postman

Try with API Explorer

Supporting resources
--------------------

Learn how to use Postman to make requests

Troubleshoot an error

Visit the API reference page for this endpoint

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