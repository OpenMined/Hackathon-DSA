
PowerTrack rules & filtering | Docs | Twitter Developer Platform 

PowerTrack rules & filtering

Rules & Filtering
-----------------

Take a deeper dive into building PowerTrack rules using our learning path: How to detect signal from noise and build powerful filtering rules

PowerTrack enhances the ability to filter Twitter’s full firehose, and only receive the data that they or their customers are interested in. This is accomplished by applying PowerTrack filtering language to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others. Using PowerTrack rules to filter a data source ensures that customers receive all of the data, and *only* the data they need for your app.

As described, customers add filtering rules to the PowerTrack stream to determine which activities will be sent through the connection. The PowerTrack stream can support thousands of these individual rules, and deliver the combined set of matching activities through the single stream connection.

The set of PowerTrack rules used to filter a customer’s stream is highly flexible. If a customer needs to add a new filtering rule to capture a different type of content, or remove an existing rule, their app can send a request to the PowerTrack API to make it happen. When that request is sent, the filtering rules are automatically modified and the changes simply take effect in the data stream with no need to reconnect. This allows customers to provide data for many customers at scale, while supporting distinct filtering requirements for each of those customers.

See Complete List of Operators »

#### Data

Data is delivered to the customer’s app through a constant stream as it is created. The realtime stream does not provide recent data – rather, it begins filtering for and delivering results based on the time a filtering rule is added to the stream. If, in addition to realtime data, your product also requires instant access to recent data, we recommend using the Search API.

Data is in Gzip compressed JSON format.

#### Matching Rules

When an activity is delivered through the PowerTrack stream, adds metadata in the “matching rules” portion of that activity to indicate which rule or rules caused that specific activity to be delivered. If multiple rules match a single activity, the activity is delivered a single time with each of the matching rules included in this metadata. The matching rules provide an easy way to associate a specific activity with specific rules and customers in your product, even where you have many customers with lots of distinct rules. Since the data is delivered through a single stream in this manner, scaling up as your product gains additional customers is simple.

#### Rule Tags

At the time they are created, each filtering rule may be created with a tag. Rule tags have no special meaning, they are simply treated as opaque strings carried along with the rule. They will be included in the “matching rules” metadata in activities returned. Tags provide an easy way to create logical groupings of PowerTrack rules. For example, you may generate a unique ID for a specific rule as its tag, and allow your app to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.

Note that tags cannot be updated on an existing rule, but can only be included when a rule is created. In order to “update” a tag, you need to first remove the rule, then add it again with the updated tag. The best solution is to simply use a unique identifier as your tag, which your system can associate with various other data points within your own app, all without having to change anything in the rule set.

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