
Tweets lookup introduction | Docs | Twitter Developer Platform 

Introduction

Introduction
------------

The Tweet is one of the primary resources on Twitter. In its simplest form, a Tweet can contain up to 280 characters and can be posted either publicly or privately, depending on an account’s settings. However, a variety of different objects can also be attached to Tweet, including media, a place, polls, and URLs. In addition, most Tweets can be edited for up to 30 minutes after being created. 

While there are a variety of different HTTP, selection, and delivery methods that can deliver, publish, and act upon Tweets, this group of REST endpoints simply returns a Tweet or group of Tweets, specified by a Tweet ID. While simple, these endpoints can be used to receive up-to-date details on a Tweet, verify that a Tweet is available, and examine its edit history. These endpoints are also important tools for managing compliance events.

The Tweet lookup endpoint provides edited Tweet metadata. All objects for Tweets created since September 29, 2022, include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history is documented by an array of Tweet IDs, starting with the original ID.

This endpoint will always return the most recent edit, along with any edit history. Any Tweet collected after its 30-minute edit window has expired will represent its final version. To learn more about Edit Tweet metadata, check out the Edit Tweets fundamentals page.

These endpoints utilize the GET HTTP method and return one or many Tweet objects, which include fields such as the Tweet text, a timestamp from when it was created, and lists and metadata of hashtags, mentions, and photos, and more.   

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

Relevant tutorials
------------------

Measure Tweet performance

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