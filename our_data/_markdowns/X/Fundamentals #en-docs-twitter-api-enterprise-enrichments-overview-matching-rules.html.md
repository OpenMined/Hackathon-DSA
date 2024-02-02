
Matching rules object | Docs | Twitter Developer Platform 

Matching rules object

Matching rules
==============

The matching rules enrichment is an object of metadata that indicates which rule or rules matched the Tweets received. This is most commonly used with the PowerTrack stream.

Matching will be done via exact match on the terms contained in a rule, scanning the content of the activity with and without punctuation. Matching is not case sensitive. When the content is found to contain all terms defined in the rule, there will be a root-level a matching\_rules object indicating the rule(s) that led to the match.

PowerTrack
----------

Tweets delivered through PowerTrack (realtime, Replay, and Historical) will contain the matching\_rules object as follows:

```
      "matching_rules": [{
        "tag": null,
        "id": 907728589029646336,
        "id_str": "907728589029646336"
    }]
```

In PowerTrack, the matching\_rules object reflects *all* rules that matched the given result. In other words, if more than one rule matches a specific Tweet, it will only be delivered once, but the matching\_rules element will contain all the rules that matched.

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