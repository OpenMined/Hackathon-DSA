



Poll object | Docs | Twitter Developer Platform 





































































































Poll object



Poll
----


A poll included in a Tweet is not a primary object on any endpoint, but can be found and expanded in the Tweet object. 


The object is available for expansion with `?expansions=attachments.poll_ids` to get the condensed object with only default fields. Use the expansion with the field parameter: `poll.fields` when requesting additional fields to complete the object.


 




| Field value | Type | Description |
| --- | --- | --- |
| id (default) | string | Unique identifier of the expanded poll.
`"id": "1199786642791452673"` |
| options (default) | array | Contains objects describing each choice in the referenced poll.
`"options": [
                    {
                        "position": 1,
                        "label": "“C Sharp”",
                        "votes": 795
                    },
                    {
                        "position": 2,
                        "label": "“C Hashtag”",
                        "votes": 156
                    }
                ]` |
| duration\_minutes | integer | Specifies the total duration of this poll.
`"duration_minutes": 1440` |
| end\_datetime | date (ISO 8601) | Specifies the end date and time for this poll.
`"end_datetime": "2019-11-28T20:26:41.000Z"` |
| voting\_status | string | Indicates if this poll is still active and can receive votes, or if the voting is now closed.
`"voting_status": "closed"` |


### Retrieving a poll object


#### Sample Request


In the following request, we are requesting fields for the poll object attached to the Tweet on the Tweets lookup endpoint. Since poll is a child object of a Tweet, the `attachments.poll_id` expansion is required. Be sure to replace `$BEARER_TOKEN` with your own generated Bearer Token.  

 












```

      curl --request GET 'https://api.twitter.com/2/tweets?ids=1199786642791452673&expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








#### 
Sample Response












```

      {
    "data": [
        {
            "text": "C#",
            "id": "1199786642791452673",
            "attachments": {
                "poll_ids": [
                    "1199786642468413448"
                ]
            }
        }
    ],
    "includes": {
        "polls": [
            {
                "id": "1199786642468413448",
                "voting_status": "closed",
                "duration_minutes": 1440,
                "options": [
                    {
                        "position": 1,
                        "label": "“C Sharp”",
                        "votes": 795
                    },
                    {
                        "position": 2,
                        "label": "“C Hashtag”",
                        "votes": 156
                    }
                ],
                "end_datetime": "2019-11-28T20:26:41.000Z"
            }
        ]
    }
}
    
```



















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















