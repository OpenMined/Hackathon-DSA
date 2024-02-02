
Volume streams introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

Volume streams consist of two streaming endpoints that deliver a random sample of publicly available Tweets in real-time. They are available to Enterprise levels of access only.

* 1% sampled stream.
* 10% sampled stream. Commonly referred to as the "Decahose."

These are referred to as "volume streams" because they both deliver large volumes of data. Even the 1% stream can emit many dozens of Tweets every second. With these streams, you can identify and track trends, monitor general sentiment, monitor global events, and much more.   

These streaming endpoints deliver Tweet objects through a persistent HTTP GET connection and use OAuth 2.0 App-Only authentication. With Essential access, you can have one connection at a time. With all levels of access, connection requests can be made up to 50 times per 15-minute window.

These volume stream endpoints support edited Tweets. These endpoints will deliver edited Tweets, along with its edit history, including an array of Tweet IDs. For Tweets with no edit history, this array will hold a single ID. For Tweets that have been edited, this array contains multiple IDs, arranged in ascending order reflecting the order of edits, with the most recent version in the last position of the array. To learn more about how Tweet edits work, see the Tweet edits fundamentals page. 

*To use these APIs, you must first set up an account with our enterprise sales team.*

### 

**Account setup**

To access these endpoints, you will need:

* An approved developer account.
* To authenticate using the keys and tokens from a developer App that is located within a Project.

Learn more about getting access to the Twitter API v2 endpoints in our getting started guide.

Quick start

Sample code

Run in Postman

Try with API Explorer

Supporting resources
--------------------

Learn how to use Postman to make requests

Troubleshoot an error

Visit the API reference page for this endpoint

Tutorials
---------

Stream Tweets in real-time

Listen for important events

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