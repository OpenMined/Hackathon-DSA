
Compliance Best Practices | Docs | Twitter Developer Platform 

Compliance Best Practices

Recommendations & Best Practices
--------------------------------

* **Build Data Storage Schemas That Store Numeric Tweet ID and User ID**: User messages require action to be taken on all Tweets from that User. Therefore, since all compliance messages are delivered only by numeric ID, it is important to design storage schemas that maintain the relationship between Tweet and User based on numeric IDs. Data consumers will need to monitor compliance events by both Tweet ID and User ID and be able to update the local data store appropriately.
* **Build Schemas That Address All Compliance Statuses**: Depending on how compliance activities will be addressed in various applications, it may be required to add other metadata to the data store. For instance, data consumers may decide to add metadata to an existing database to facilitate restricting the display of content in countries affected by a tweet\_withheld message.
* **Handling Retweet Deletes**: Retweets are a special kind of Tweet where the original message is nested in an object within the Retweet. In this case, there are two Tweet IDs referenced in a Retweet – the ID for the Retweet, and the ID for the original message (included in the nested object). When an original message is deleted, a Tweet delete message is issued for the original ID. Tweet deletion events typically trigger delete events for all Retweets. It is a best practice to reference the original Tweet ID when storing Retweets, and deleting all referenced Retweets when receiving Tweet delete events.

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