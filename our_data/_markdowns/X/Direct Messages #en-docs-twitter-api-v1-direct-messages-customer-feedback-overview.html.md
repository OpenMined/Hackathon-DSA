
Overview | Docs | Twitter Developer Platform 

Overview

Enterprise

Product & development guidance
------------------------------

Collecting structured feedback about customer interactions is a useful part of the customer service experience, providing quantitative measures of service quality and effectiveness that benefits both people and businesses. By asking for feedback in context and shortly after the interaction is complete, people are more likely to provide a response and more likely to provide feedback that reflects their interaction. This feature supports the programmatic creation and delivery of feedback prompts that allow someone to submit responses to feedback surveys after a conversation in Direct Messages.

* Feedback should ideally be built into your product so it can be kicked off automatically, not manually. The goal is to remove potential bias in results and to give a sense of trust to the user (for more honest feedback) that the agent who handled the interaction is not reading the results.
* Feedback results should be delivered to the business via your product. We've built our APIs with an assumption that you could create a dashboard or file download to provide reports to managers. Twitter is not planning to provide an interface for businesses to retrieve results directly from Twitter.
* Feedback results should ideally not be surfaced directly to an agent, and instead, be surfaced in supervisor reports or in an asynchronous way such that an agent doesn’t see the feedback and change their interaction demeanor or behavior.
* Initially, Feedback can only be requested along with a Direct Message. Make sure to check the user object can\_dm to see if you have the ability to send Feedback before hitting the POST endpoint. (Particularly relevant if sending a Feedback prompt after a public interaction.)
* A Direct Message must be sent before prompting a user for Feedback. When brands are considering the Direct Message text preceding the Feedback prompt, make sure it makes sense in the case that the Feedback experience does not render (web client, old clients, 3rd party clients, etc).
* Scores and text can be submitted independently and will likely have different timestamps. A score may be submitted without a text comment ever being completed. Both scores and text are immutable once submitted.
* Code should be tolerant of n ­number of updates per Feedback object. It should not assume a max of three possible updates. You should always rely on the most recent “updated\_at” timestamp.
* An empty next\_cursor value indicates you have reached the end of the result set. You should make no assumption about empty/partial page returned in "events" array as a signal that there is no more data to be fetched.

---

Access & authentication
------------------------

Customer feedback cards only display to users in the iOS or Android Twitter apps. They do not display on twitter.com, mobile.twitter.com, TweekDeck, or 3rd-party Twitter apps, even if a feedback request is sent. 

Customer feedback cards are only available to Twitter enterprise data customers.

* Your client app ID and a @username must each be added to an allowlist to get app ­level access to the API.
* Authentication is 3-­legged OAuth currently used with the Twitter public API.
* We must additionally add the @username to an allowlist for any accounts you wish to send Feedback requests FROM (either your customer’s handles or your own if used for testing purposes).

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