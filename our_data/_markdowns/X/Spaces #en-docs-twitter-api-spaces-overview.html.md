
Spaces overview | Docs | Twitter Developer Platform 

Spaces overview

Introduction
------------

The following page describes the Spaces endpoints included in the Twitter API. To learn more about Spaces in general, please visit help.twitter.com. 

Spaces allow expression and interaction via live audio conversation. The Spaces endpoints provide the tools to create new functionality around Spaces. You can use these endpoints to lookup live or scheduled Spaces, or to build discovery experiences to give your users ways to find Spaces they may be interested in.

We encourage you to use your creativity to extend Spaces beyond the way we built it. With these endpoints you can build experiences to suggest Spaces to listeners based on keywords present in the title, or by surfacing accounts who host live or upcoming Spaces and are followed by a user; you can also help Hosts better understand how their Spaces are performing and get more insights on their audience.  

### Important resources

The following resources will help you get started and integrate with the Spaces endpoints:

* Getting access to Twitter API v2
* Spaces data dictionary
* Make your first request to a Spaces endpoint

What's currently available
--------------------------

|  |  |
| --- | --- |
| **Spaces lookup** | Lookup by a single Spaces ID
Lookup using multiple Spaces IDs
Lookup by their creator ID
Lookup list of user who purchased a ticket |
| **Search Spaces** | Search for spaces using a keyword |

Understanding the lifecycle of Spaces
--------------------------------------

Unlike other resources of the Twitter Developer Platform, Spaces have a set lifecycle. Spaces can be scheduled up to 14 days in advance of their intended start date, and become unavailable after they end. A host can also cancel a previously scheduled Space anytime before it starts.

Spaces are accessible while they are live; once ended, they will no longer be available for retrieval using the Spaces endpoints, and an error message will be returned to indicate this condition.

When your app handles Spaces data, you are responsible for returning the most up-to-date information, and that you remove data that is no longer available from the platform. The Spaces lookup endpoint can help you ensure you respect the expectations and intent of your users.  

Roles in Spaces
---------------

These endpoints reflect the way Spaces work on the Twitter app. In Spaces, Twitter users can have defined roles depending on how they interact with and interact in a Space.  

### Creator (or primary host)

The primary Host is the user who created a Space, and the owner of the Space itself. Currently, Spaces can only have one Host, so the primary Host will be the only Host. In the Spaces data dictionary, the primary Host information will be in the creator\_id field, which can be expanded into a user object.  

### Hosts

The primary Hosts can make one or more users co-hosts. In the Spaces data dictionary, these Hosts will appear as host\_ids, which can be expanded into a list of user objects. Host designation can change throughout the duration of a Space, and the metadata returned by these endpoints will reflect the status at the time of the request.

Your app will know the primary host by checking the creator\_id value, and who are the co-hosts by checking the host\_ids values.  

### Speaker

Speakers are users who have permission to talk in the Space. Zero or more Speakers can be present at any time, and there may be up to 10 Speakers (including the Hosts) in a Space. In the Space data dictionary, speakers will be returned in the speaker\_ids list, which you can expand into a list of user objects.  

### Listener

A Listener can listen to a Space, react anytime using the predefined reactions, and ask to become a speaker (when the Hosts allows this in the Space settings). Listener information will only be returned as an aggregate count of participants (including Hosts) in the participant\_count field.  

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