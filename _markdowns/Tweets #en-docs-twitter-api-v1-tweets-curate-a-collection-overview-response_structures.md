



Response structures | Docs | Twitter Developer Platform 





































































































Response structures



Response Structures
===================


The Collections API responds with data structures that often depart from the objects you traditionally encounter in the Twitter API.


In the Collections API, all identifiers (IDs, cursors, collection positions) are presented as strings. These strings are safe to consume and utilize in all programming languages, including those that do not support 64-bit integers.


While representations of Tweets and Users generally match other Twitter API representations, watch for minor differences in the object structure, especially around data related to counts.


While the API typically returns objects-embedded-within-objects (such as the author of a Tweet being embedded within the Tweet itself), these API methods provide decomposed responses where each object type is grouped together and each object is represented only once. Instead of containing associated child objects, the objects contain simple ID references to the association.


Here are some of the response structures you will encounter in the Collections API.


Object collections
------------------


API methods that return multiple objects of the same type are segmented such that one component of the response contains the objects and any associated objects while another component simply lists references to those same objects and contextual information (such as cursors) needed to navigate the boundaries of the collection in subsequent requests.


You will see responses like this in GET collections / list.


### Structure


* response (object)
	+ results (array of objects)
		- each object typically contains one key/value pair housing an object’s ID
	+ cursors (object)
		- next\_cursor (string)
		- previous\_cursor (string)
* objects (object)
	+ users (object, ID as key)
	+ tweets (object, ID as key)
	+ timelines (object, ID as key)


Single objects
--------------


Even methods that return a single “primary object” respond with a decomposed structure, similar to a collection.


Methods that can return only one core object:


You will see responses like this in: GET collections / show


### Structure


response (object)


* a key/value pair indicating the object’s type and identifier (e.g. "timeline\_id":"custom-393773270547177472")


objects (object)


* users (object, ID as key)
* tweets (object, ID as key)
* timelines (object, ID as key)


 


 



















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















