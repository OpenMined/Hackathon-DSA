



Overview | Docs | Twitter Developer Platform 





































































































Overview



Overview
--------


Annotations have been added to the Tweet object from all v2 endpoints that return a Tweet object. Tweet annotations offer a way to understand contextual information about the Tweet itself. Though 100% of Tweets are reviewed, due to the contents of Tweet text, only a portion are annotated.


**Entity annotations (NER):** Entities are comprised of people, places, products, and organizations. Entities are delivered as part of the entity payload section. They are programmatically assigned based on what is explicitly mentioned (named-entity recognition) in the Tweet text.


**Context annotations:** Derived from the analysis of a Tweet’s text and will include a domain and entity pairing which can be used to discover Tweets on topics that may have been previously difficult to surface. At present, we’re using a list of 80+ domains to categorize Tweets. A CSV file of the available context annotation entities is available for download at our Github repository.



Tweet annotation types
----------------------


### Entities


Entity annotations are programmatically defined entities that are nested within the entities field and are reflected as annotations in the payload. Each annotation has a confidence score and an indication of where in the Tweet text the entities were identified (start and end fields).


The entity annotations can have the following types:


**Person** - Barack Obama, Daniel, or George W. Bush


**Place** - Detroit, Cali, or "San Francisco, California"


**Product** - Mountain Dew, Mozilla Firefox


**Organization** - Chicago White Sox, IBM


**Other** - Diabetes, Super Bowl 50



### Context


*Last updated: June 2022*


Context annotations are delivered as a context\_annotations field in the payload. These annotations are inferred based on semantic analysis (keywords, hashtags, handles, etc) of the Tweet text and result in domain and/or entity labels. Context annotations can yield one or many domains. At present, we’re using a list of 80+ domains reflected in the table below.




|  |  |  |  |
| --- | --- | --- | --- |
| 3: TV Shows
4: TV Episodes
6: Sports Events
10: Person
11: Sport
12: Sports Team
13: Place
22: TV Genres
23: TV Channels
26: Sports League
27: American Football Game
28: NFL Football Game
29: Events
31: Community
35: Politicians
38: Political Race
39: Basketball Game
40: Sports Series
43: Soccer Match
44: Baseball Game
45: Brand Vertical | 46: Brand Category
47: Brand
48: Product
54: Musician
55: Music Genre
56: Actor
58: Entertainment Personality
60: Athlete
65: Interests and Hobbies Vertical
66: Interests and Hobbies Category
67: Interests and Hobbies
68: Hockey Game
71: Video Game
78: Video Game Publisher
79: Video Game Hardware
83: Cricket Match
84: Book
85: Book Genre
86: Movie
87: Movie Genre
88: Political Body | 89: Music Album
90: Radio Station
91: Podcast
92: Sports Personality
93: Coach
94: Journalist
95: TV Channel [Entity Service]
109: Reoccurring Trends
110: Viral Accounts
114: Concert
115: Video Game Conference
116: Video Game Tournament
117: Movie Festival
118: Award Show
119: Holiday
120: Digital Creator
122: Fictional Character
130: Multimedia Franchise
131: Unified Twitter Taxonomy
136: Video Game Personality | 137: eSports Team
138: eSports Player

139: Fan Community
149: Esports League
152: Food
155: Weather
156: Cities
157: Colleges & Universities
158: Points of Interest
159: States
160: Countries
162: Exercise & fitness
163: Travel
164: Fields of study
165: Technology
166: Stocks
167: Animals
171: Local News
172: Global TV Show
173: Google Product Taxonomy
174: Digital Assets & Crypto
175: Emergency Events |


*Note:* Domain 131 (Unified Twitter Taxonomy) refers to Twitter's User Facing Interest Taxonomy. This taxonomy helps to power features on the platform such as, Topics.  


 


Requesting annotations
----------------------


### **Sample Request**












```

      curl --location --request GET 'https://api.twitter.com/2/tweets/1212092628029698048?tweet.fields=context_annotations,entities' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








 **Sample Response**












```

      {
    "data": {
        "context_annotations": [
            {
                "domain": {
                    "id": "119",
                    "name": "Holiday",
                    "description": "Holidays like Christmas or Halloween"
                },
                "entity": {
                    "id": "1186637514896920576",
                    "name": " New Years Eve"
                }
            },
            {
                "domain": {
                    "id": "119",
                    "name": "Holiday",
                    "description": "Holidays like Christmas or Halloween"
                },
                "entity": {
                    "id": "1206982436287963136",
                    "name": "Happy New Year: It’s finally 2020 everywhere!",
                    "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
                }
            },
            {
                "domain": {
                    "id": "45",
                    "name": "Brand Vertical",
                    "description": "Top level entities that describe a Brands industry"
                }
            },
            {
                "domain": {
                    "id": "46",
                    "name": "Brand Category",
                    "description": "Categories within Brand Verticals that narrow down the scope of Brands"
                },
                "entity": {
                    "id": "781974596752842752",
                    "name": "Services"
                }
            },
            {
                "domain": {
                    "id": "47",
                    "name": "Brand",
                    "description": "Brands and Companies"
                },
                "entity": {
                    "id": "10045225402",
                    "name": "Twitter"
                }
            },
            {
                "domain": {
                    "id": "119",
                    "name": "Holiday",
                    "description": "Holidays like Christmas or Halloween"
                },
                "entity": {
                    "id": "1206982436287963136",
                    "name": "Happy New Year: It’s finally 2020 everywhere!",
                    "description": "Catch fireworks and other celebrations as people across the globe enter the new year.\nPhoto via @GettyImages "
                }
            }
        ],
        "entities": {
            "annotations": [
                {
                    "start": 144,
                    "end": 150,
                    "probability": 0.626,
                    "type": "Product",
                    "normalized_text": "Twitter"
                }
            ],
            "urls": [
                {
                    "start": 222,
                    "end": 245,
                    "url": "https://t.co/yvxdK6aOo2",
                    "expanded_url": "https://twitter.com/LovesNandos/status/1211797914437259264/photo/1",
                    "display_url": "pic.twitter.com/yvxdK6aOo2"
                }
            ]
        },
        "id": "1212092628029698048",
        "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"
    }
}
    
```






 **Sample App**


See the Tweet Entity Extractor on Glitch to easily discover context annotations in Tweets and see how this feature works.



















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















