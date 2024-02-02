
Hide replies - Manage replies in realtime | Docs | Twitter Developer Platform 

Manage replies in realtime

Manage replies in realtime
--------------------------

With the hide replies endpoint, you can build a workflow to helps your users hide replies that have a very high-probability of being irrelevant.

Useful apps often combine technologies so that they can be valuable to their users. This page shows how to hide replies by using the Perspective API. This API is an artificial intelligence trained by Jigsaw, a unit within Google, to detect toxic comments. The application logic will work in the following way:

1. It asks the user’s permission to read their Tweets and hide or unhide their replies.
2. It uses the Account Activity API to detect incoming replies.
3. It asks the Perspective API to give a “score” (a number between 0 and 1) that indicates how confident their algorithm is that a comment is similar to toxic comments it’s seen in the past. (Perspective does not store the text sent to the service).
4. It calls hide replies if the algorithm’s score is very high.

### Strive for transparency

Because Perspective is not trained on actual Tweets, certain language nuances may cause this app to hide a reply that a user wants to remain unhidden. Regardless of the technology or the approach you use when designing your app, always make the best possible effort to ensure that your users understand what your app has hidden and can make changes.

* The best option is to always trust the user and to give them full control over their decisions. This means your user experience should include controls to undo any action taken by your app on behalf of the user.
* When using an artificial intelligence, your app should use a very high confidence threshold to detect and hide Tweets.
* Not everybody uses the same words, and your app should be designed to avoid any bias. Be mindful of reclaimed words and slang that may lead to false positives.
* If you are training an artificial intelligence, consider adopting a model that closely reflects language often used on Twitter.

Next steps
----------

Learn how to manage replies by topic

Visit the API Reference for this endpoint

Reach out to the community for help

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