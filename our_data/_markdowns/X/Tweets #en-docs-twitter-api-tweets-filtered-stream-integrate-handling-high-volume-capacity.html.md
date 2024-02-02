
Filtered stream - Handling high-volume capacity | Docs | Twitter Developer Platform 

Handling high-volume capacity

How to plan for high-volume social data events
----------------------------------------------

Major national and global events are often accompanied by dramatic spikes in user activity across social media platforms. Sometimes these events are known about in advance, like the Super Bowl, political elections, and New Year’s celebrations around the world. Other times, the spikes in volume are due to unexpected happenings such as natural disasters, unplanned political events, pop culture moments, or health pandemics like COVID-19.

These bursts of user activity may sometimes be short-lived (measured in seconds), or they may even be sustained over several minutes’ time. No matter their origin, it is important to consider the impact that they can have on applications consuming real-time data from Twitter. Here are some best practices that will help your team prepare for high-volume social data events.

#### Review your current filtered stream rules

* Certain keywords can skyrocket during high volume events, such as brand mentions when a brand sponsors a major sporting event.
* Be careful to avoid any unnecessary or overly generic rules that may generate unnecessary activity volumes.
* Consider communicating with your clients prior to known high-volume events to help them plan appropriately.

#### Stress test your application

Anticipate that burst volumes may reach 5-10x average daily consumption levels. Depending on your rule set, the increase may be much higher.

#### Understand delivery caps for connections

Flow and delivery caps are based on levels of access. This results in a static volume of delivered results for streams.

* **Academic**: 250 Tweets/second
* **Enterprise**: Tweets/second is set at access level

#### Optimize to stay connected

With real-time streams, staying connected is essential to avoid missing data. Your client application should be able to detect a disconnect and have logic to immediately retry its connection, using an exponential backoff if the reconnect attempt fails.  

#### Add built-in buffering on your end

Building a multi-threaded application is a key strategy for handling high-volume streams. At a high-level, a best practice for managing data streams is to have a separate thread/process that establishes the streaming connection and then writes received JSON activities to a memory structure or a buffered stream reader. This ‘light-weight’ stream processing thread is responsible for handling incoming data, which can be buffered in memory, growing and shrinking as needed. Then a different thread consumes that hash and does the ‘heavy lifting’ of parsing the JSON, preparing database writes, or whatever else your application needs to do.  

#### Global events = global time zones

The events may occur after business hours or over the weekend, so be sure that your team is prepared for spikes to occur outside your normal business hours.

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