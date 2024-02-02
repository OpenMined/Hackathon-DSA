



Twitter API: Enterprise data dictionary | Docs | Twitter Developer Platform 





































































































Introduction








Interested in learning more about how the enterprise data formats map to the Twitter API v2 format?


Check out our comparison guides:


* Native Enriched compared to Twitter API v2
* Activity Streams compared to Twitter API v2









Introduction
------------


Enterprise


Tweets are the basic atomic building block of all things Twitter. All Twitter APIs that return Tweets provide that data encoded using JavaScript Object Notation (JSON). JSON is based on key-value pairs, with named attributes and associated values. Tweet objects retrieved from the API include a Twitter User's "status update" but Retweets, replies, and quote Tweets are all also Tweet objects.  If a Tweet is related to another Tweet, as a Retweet, reply or quote Tweet, each will be identified or embedded into the Tweet object.  Even the simplest Tweet in the native Twitter data format, will have nested JSON objects to represent the other attributes of a Tweet, such as the author, mentioned users, tagged place location, hashtags, cashtag symbols, media or URL links.  When working with Twitter data, this is an important concept to understand. The format of the Tweet data you will receive from the Twitter API depends on the type of Tweet received, the Twitter API you are using, and the format settings.


Enterprise endpoints that return Tweet objects have been updated to provide the metadata needed to understand the Tweet's edit history. Learn more about these metadata on the "Edit Tweets" fundamentals page.



> What did the developer write in their Valentine’s card?  
> 
>   
> 
> while(true) {  
> 
> I = Love(You);  
> 
> }
> 
> 
> — Twitter Dev (@TwitterDev) February 14, 2020


In native Twitter format, the JSON payload will include of ‘root-level’ attributes, and nested JSON objects (which are represented here with the `{}` notation):












```

      {
	"created_at": "Fri Feb 14 19:00:55 +0000 2020",
	"id_str": "1228393702244134912",
	"text": "What did the developer write in their Valentine’s card?\n  \nwhile(true) {\n    I = Love(You);  \n}",
	"entities": {
		"hashtags": [],
		"symbols": [],
		"user_mentions": [],
		"urls": []
	},
	"user": {
		"entities": {
			"url": {}
		}
	},
	"place": {}
}
    
```





Code copied to clipboard








Available data formats
----------------------











Please note: It is highly recommended to use the Enriched Native format for enterprise data APIs. 


* The Enriched Native format includes all new metadata since 2017, such as poll metadata, and additional metrics such as reply\_count and quote\_count.
* Activity Streams format has not been updated with new metadata or enrichments since the character update in 2017.









Enterprise data APIs deliver data in two different formats.  The enterprise format closest to the standard v1.1 native format is Native Enriched.  The legacy enterprise data format is Activity Streams, orignially implimented and used by Gnip as a normalized format across Twitter and other social media data providers at the time. While this format is still available, Twitter has only invested new features and developments on the native enriched format since 2017.  




The enriched native format is exactly how it sounds, it includes native Twitter objects as well as additional enrichments avialable for enterprise data products such as URL unwinding metadata, profile geo, poll metadata and additional engagement metrics.  


* Expanded and enhanced URLs enrichment
* Matching rules enrichment
* Poll metadata enrichment
* Profile geo enrichment






 


### Object comparison per data format


Whatever your Twitter use case, understanding what these JSON-encoded Tweet objects and attributes *represent* is critical to successfully finding your data signals of interest. To help in that effort, there are a set of pages dedicated to each object in each data format*.*


Reflecting the JSON hierarchy above, here are links to each of these objects:




| Native Enriched | Activity Streams |
| --- | --- |
| Link Tweet object | Link Activity object |
| Link User object | Link Actor object |
| Link Entities object | Link Twitter entities object |
| Link Extended entities object | Link Twitter extended entitites object |
| Link Geo object | Link Location object |
| n/a | Link Gnip object |


 


Parsing best-practices
----------------------


* Twitter JSON is encoded using UTF-8 characters.
* Parsers should tolerate variance in the ordering of fields with ease. It should be assumed that Tweet JSON is served as an unordered hash of data.
* Parsers should tolerate the addition of 'new' fields.
* JSON parsers must be tolerant of ‘missing’ fields, since not all fields appear in all contexts.
* It is generally safe to consider a nulled field, an empty set, and the absence of a field as the same thing


 
### Next Steps:


* Review the enterprise enriched native data dictionary



















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















