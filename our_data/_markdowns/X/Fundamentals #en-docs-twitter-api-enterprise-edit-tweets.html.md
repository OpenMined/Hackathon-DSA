
Edit Tweets | Docs | Twitter Developer Platform 

Edit Tweets

Introduction
------------

Enterprise endpoints have been updated to provide edited Tweet metadata. The *Edit Tweets* feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets were editable for 30 minutes and up to 5 times. *All objects for Tweets created since September 29, 2022* include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID. Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well. 

These metadata details are included automatically. No request parameters are needed to include available edit history as part of the Tweet object. 

With these new metadata, a developer can find out:

* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, cannot be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets, you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet. In most cases, the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID.

Three new Tweet attributes have been added at the root level:

* **edit\_history**  - Provides all Tweet IDs associated with the edit history of the Tweet. The "initial\_tweet\_id" attribute indicates the original Tweet and the "edit\_tweet\_ids" attribute is an array that provides all IDs associated with its edit history. If the Tweet has not been edited, this array will contain a single ID.

```
"edit_history": {
    "initial_tweet_id": "1283764123"
    "edit_tweet_ids": ["1283764123"]
  }
```
- **edit\_controls** - Provides attributes that indicate when the 30-minute edit window ends and how many potential edits remain.

```
"edit_controls": {  
     "editable_until_ms": 1660155761384
     "edits_remaining": 3   
  }
```
- **editable** - Indicates whether a Tweet was eligible for editing when created.

```
"editable": true
```

Most Tweets are eligible. However, the following types of Tweets are not: 

* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet

Example attributes for unedited Tweet
-------------------------------------

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has no edit history. 

Note that the "edit\_tweet\_ids" array has a single ID. 

```
      {
  "created_at": "Wed Aug 16 18:29:02 +0000 2022",
  "id": 1557433858676740098,
  "id_str": "1557433858676740098",
  "text": "I wonder if I will every use teh edit button",
  "edit_history": {
    "initial_tweet_id": "1557433858676740098",
    "edit_tweet_ids": ["1557433858676740098"]
  },
  "edit_controls": {
    "editable_until_ms": 1660155761384,
    "edits_remaining": 5
  },
  "editable": true
}
```

Code copied to clipboard

Example attributes for an edited Tweet
--------------------------------------

The JSON below highlights edit metadata that is included for a Tweet posted after the edit Tweet feature was added. This example is for a Tweet that has had a single edit. 

Note that the "edit\_tweet\_ids" array has two IDs, one for the original Tweet and one for the edited update. 

```
      {
  "created_at": "Wed Aug 16 18:35:42 +0000 2022",
  "id": 1557445923210514432,
  "id_str": "1557445923210514432",
  "text": "I wonder if I will ever use the edit button",
  "edit_history": {
    "initial_tweet_id": "1557433858676740098",
    "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"]
  },
  "edit_controls": {
    "editable_until_ms": 1660155761384,
    "edits_remaining": 4
  },
  "editable": true
}
```

Code copied to clipboard

Compliance support
------------------

The Compliance Firehose and the v2 batch compliance endpoint have both been updated to provide edit Tweet support: 

A new "tweet\_edit" event type has been added to the Compliance Firehose. 

```
      {
  "tweet_edit": {
    "id": <tweetId>,
    "initial_tweet_id": <tweetId>,
    "edit_tweet_ids": [<tweetId1>, <tweetId2>, <tweetId3> ...],
    "timestamp_ms": "<timestampMsStr>"
  }
}
```

Code copied to clipboard

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