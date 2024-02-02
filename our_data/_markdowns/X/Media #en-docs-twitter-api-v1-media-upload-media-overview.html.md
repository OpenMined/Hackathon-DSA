
Overview | Docs | Twitter Developer Platform 

Overview

A media object represents a single photo, video or animated GIF. Media objects are used by many endpoints within the Twitter API, and may be included in Tweets, Direct Messages, user profiles, advertising creatives and elsewhere. Each media object may have multiple display or playback variants, with different resolutions or formats.  

Media types & size restrictions
-------------------------------

Size restrictions for uploading via API   

* Image 5 MB
* GIF 15 MB
* Video 512 MB (when using media\_category=amplify)

Creation
--------

Objects such as Tweets, Direct Messages, user profile pictures, hosted Ads cards, etc. can contain one or more media objects. These top-level objects are collectively known as entities. The relevant entity creation API (e.g. POST statuses/update) can be passed one or more media objects using a unique media\_id.

An entity which contains media object(s) can be created by following these steps:

1. Upload the media file(s) using either the recommended chunked upload (images/GIF/video), or the older simple upload (images only).
2. Receive a media\_id from step 1. This step may be repeated multiple times with different media if the entity allows multiple media\_id parameters to be passed in.
3. Create the entity by calling the appropriate endpoint, including the media\_id and other required parameters. For example, attach a media\_id to a Tweet using the POST statuses/update endpoint.

Retrieving
----------

Please refer to the Media Object in the Tweet data dictionary.

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