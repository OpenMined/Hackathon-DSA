
About collections | Docs | Twitter Developer Platform 

About collections

### About Collections

Collections are a type of timeline that can be controlled and hand-curated, or programmed using an API.

As a unit, collections operate under the following rules:

* Collections are created by users.
* Each collection has a name and description.
* The collection creator can add any public Tweet to the collection.
* When new Tweets are added, they appear at the top of the collection.
* Collections are public, have their own URL on twitter.com, and are viewable by all.

By design, collections do not implement specific rules or logic for sourcing or adding Tweets, leaving that strategy entirely up to you. For example if you want a collection that sources Tweets from multiple lists + a search + your own secret sauce, you can build that easily using the API.

Differences with other methods
------------------------------

Those familiar with Twitter’s family of REST APIs may notice some differences in object structure compared to typical APIs.

Pay close attention to the differences in how collections are presented — often they will be decomposed, efficient objects with information about users, Tweets, and timelines grouped, simplified, and stripped of unnecessary repetition.

Navigating collections also differs from the other APIs in that the collection is not strictly creation-time oriented. Navigating by since\_id and last\_id has been replaced with a position-based pagination system that should still be familiar.

See Response structures for a deeper overview of these differences.

Authenticating Requests
-----------------------

It is important to note that the Twitter API is strict about character encoding in OAuth 1.0a and HTTP. Reserved characters in query strings and application/x-www-form-urlencoded POST bodies must first be encoded according to RFC 3986.

OAuth 1.0a handles requests of other content-types slightly differently. A POST body that is not application/x-www-form-urlencoded is not considered as part of the parameters that will be encoded in the OAuth signature base string. Instead your signature base string will contain only any parameters contained on the query string and the oauth\_\* parameters that are typically part of the OAuth signature generation process. POST collections / entries / curate uses application/json POST bodies.

Working with the Collections API
--------------------------------

Use these methods to browse Collections, whether by ID, those owned by a specific user, or those containing a specific Tweet.

* GET collections / list
* GET collections / show

These methods allow you to create, modify, or delete a collection on behalf of the currently authenticated user.

* POST collections / create
* POST collections / destroy
* POST collections / update

To curate a collection, add or remove Tweets with these methods:

* GET collections / entries
* POST collections / entries / add
* POST collections / entries / remove
* POST collections / entries / move
* POST collections / entries / curate

Collections on Twitter.com
--------------------------

Once created, Collections are available to view on twitter.com through a web and mobile-friendly permalink. Collections are meant to be shared with the world! Feel free to Tweet these permalink URLs to share your collection with followers.

Each Collections permalink is indicated in the custom\_timeline\_url field found in Collection timeline object responses.

Embedded Collections on the Web
-------------------------------

Collections are meant to be shared with the world, on and off Twitter. To that end, embedded timelines have been expanded to support embedded collections. Use the widget configurator to prepare your collections for syndication and receive the simple HTML & JavaScript embed code for your site.

National Park Tweets

Accounts with protected Tweets and Collections
----------------------------------------------

Some accounts on Twitter have enabled a setting that “protects” the Tweets they create for an approved audience of followers. Users with protected accounts can still use Collections, but with the following caveats:

* Protected accounts can create Collections but the Collections they create will be public.
* Public users can switch to a protected state, but their Collections will remain public.
* Any user can retrieve/discover Collections belonging to any other user, regardless of the Collection owner’s protected account status.
* Tweets created by users with protected accounts cannot be included in Collections.

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