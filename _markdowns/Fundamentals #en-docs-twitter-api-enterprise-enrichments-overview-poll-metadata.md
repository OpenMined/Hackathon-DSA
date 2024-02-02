



Poll metadata | Docs | Twitter Developer Platform 





































































































Poll metadata








Poll metadata
=============




Poll metadata is a free enrichment available across all products (Realtime & Historical APIs) in enriched native format payloads. The metadata notes the presence of the poll in a Tweet, includes the list of poll choices, and includes both the poll duration and expiration time. This enrichment makes it easy to acknowledge the presence of a poll and enables proper rendering of a poll Tweet for display.


##### Important Details:


* Available across all enterprise APIs (PowerTrack, Replay, Search, Historical PowerTrack)
	+ *Note:* For Replay and Historical PowerTrack, this metadata was first made available on 02/22/17 - see documented enrichment availability.
* Does not include vote information or poll results
* Does not currently have filter/operator support
* Available in **enriched native format** only
	+ Enriched native format is a user-controlled setting that can be changed at any time through the Console: *Select a Product (PowerTrack, Replay, Search) > Settings tab > Output Format (Leave data in its original format)*


### Tweet Payload


Poll Tweets will contain the following metadata in the “entities.polls” object in the payload:


* An “options” array with up to four options that include the position (1-4) and option text
* Poll expiration date
* Poll duration


See the sample payload below for further reference.


### Sample Payload


Below is a snippet of the enriched native format payload highlighting the added poll metadata:



```

"entities":{  
      "hashtags":[],
      "urls":[],
      "user_mentions":[],
      "symbols":[],
      "polls":[  
         {  
            "options":[  
               {  
                  "position":1,
                  "text":"The better answer"
               },
               {  
                  "position":2,
                  "text":"The best answer"
               }
            ],
            "end_datetime":"Sat Feb 04 15:33:11 +0000 2017",
            "duration_minutes":1440
         }
      ]
   },

```



---




























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















