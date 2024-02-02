
Filtered stream - Matching returned Tweets to rules | Docs | Twitter Developer Platform 

Matching returned Tweets to rules

Matching returned Tweets to their associated rule
-------------------------------------------------

The filtered stream endpoint gives you the ability to have multiple rules in place through a single connection. Before you start receiving Tweets in your stream, you’ll need to create a rule which specifies what types of Tweets you’re interested in. 

When you specify your rules to match Tweets based on a wide variety of attributes, including user attributes, geo-location, language, and many others, you can attach a tag to distinguish this rule at a higher level. Tags are a good way to contextualize your rule, especially if you have many rules in place. The filtering rules determine which Tweet activities will be sent through the connection.

If you need to add a new filtering rule to capture a different type of Tweet, or remove an existing rule, your app can send a request to the POST tweets/search/stream/rules endpoint to make it happen. When that request is sent, the filtering rules are automatically modified and the changes simply take effect in the data stream with no need to reconnect. Most rule additions take effect  about 20 seconds or less. It’s unlikely, but depending on external factors (for example, network connectivity), it may take longer before you start receiving matching Tweets. If you can’t find a rule in the list rule endpoint, make sure that the rule creation request succeeded; this can be done by checking your logs for any error messages.

### Matching rules

When an activity is delivered through your filtered stream connection, in a matching\_rules array, it contains which list of filters matched against the Tweet delivered.

In the Tweet payload there is additional string metadata which includes the rule id and tag that caused a specific Tweet to be delivered. If multiple rules match a single Tweet, the activity is delivered a single time with each of the matching rules included in this metadata. The matching rules provide an easy way to associate a specific Tweet with specific rules, which is especially helpful if you have many distinct rules. Since the data is delivered through a single stream in this manner, ensuring you have unique id and tag is essential for matching. 

#### Here is an example of how the ”matching\_rules” array appears in the Tweet payload:

```
      "matching_rules": [
    {
      "id": "1166916266197536768",
      "tag": "test-rule-tag-00000"
    },
    {
      "id": "1166916266197536769",
      "tag": "test-rule-tag-12345"
    }
  ]
```

Code copied to clipboard

### 

### Rule tags

At the time they are created, each filtering rule may be created with a tag. Rule tags have no special meaning as they are simply treated as opaque strings carried along with a rule. They will be included in the matching\_rules metadata in activities returned, and are aimed at making distinguishing your rules easier at a higher level. 

Tags provide an easy way to create logical groupings of filtering rules. For example, you may generate a unique ID for a specific rule as its tag, and allow your app to reference that ID within activities it processes to associate a result with specific customers, campaigns, categories, or other related groups.

Note that tags cannot be updated on an existing rule and can only be included when a rule is created. In order to “update” or “rename” a tag, you need to first delete the rule, then add it again with the desired tag. The best solution is to simply use a unique identifier as your tag, which your system can associate with various other data points within your own app, all without having to change anything in the rule set.

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