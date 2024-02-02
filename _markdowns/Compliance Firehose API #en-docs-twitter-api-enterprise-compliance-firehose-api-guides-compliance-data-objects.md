



Compliance Data Objects | Docs | Twitter Developer Platform 





































































































Compliance Data Objects



Possible types of compliance events will include Tweet (or “status”) events and User events, for which there are multiple types described below.    




Please note:


* Read more about User statuses here and our developer policy around deleted Tweets here.
* The Compliance Firehose has been updated to provide 'tweet\_edit' events.
* Several User delete, protect and suspend events are not necessarily permanent and can toggle between states infinitely. These include: user\_delete,user\_undelete, user\_protect, user\_unprotect and user\_suspend, user\_unsuspend.
* User\_deletes are followed by status\_deletes 30 days later only if the user has not selected to user\_undelete their account. It is possible that a user\_delete is reversed by the user and deletes for all of their tweets 30 days later do not occur.
* User\_suspend is an action that remains true unless the user is subject to an user\_unsuspend event. These are not subject to any changes on a 30 day time period.


Refer to the ‘Recommended Action’ column to understand how to process each type of event in order to respect the privacy and intent of the end user.  

  




 




| Original Message Type | Object | Permanent (Yes/No) | Recommended Action |
| --- | --- | --- | --- |
| delete | Status | Yes | Delete associated Tweet. |
| status\_withheld | Status | Yes | Suppress associated Tweet in specific countries listed in the status\_withheld message. |
| drop | Status | No | Remove the Tweet from public view. |
| undrop | Status | No | Status may be displayed again and treated as public. |
| tweet\_edit | Status | Yes | Honor and, where relevant, display the new edit. |
| user\_delete | User | No | Suppress or delete all Tweets by associated user. |
| user\_undelete | User | No | All Tweets by associated user may be displayed again and treated as public. |
| user\_protect | User | No | Suppress or delete all Tweets by associated user. |
| user\_unprotect | User | No | All Tweets by associated user may be displayed again and treated as public. |
| user\_suspend | User | No | Suppress or delete all Tweets by associated user. |
| user\_unsuspend | User | No | All Tweets by associated user may be displayed again and treated as public. |
| scrub\_geo | User | Yes | Delete all geodata provided by Twitter for all Tweets by the user prior to the specified Tweet in the scrub\_geomessage. Note that subsequent Tweets by a user may contain geodata that may be used. |
| user\_withheld | User | Yes | Suppress Tweets by associated user in specific countries listed in the user\_withheld message. |
| delete | Favorite | Yes | Delete associated like/favorite.  |






Payload examples
----------------


See the payload examples below for each compliance event described in the table above.






**Tweet edit**












```

      {"tweet_edit":
   {
     "id": "1557445923210514432"
     "initial_tweet_id": "1557433858676740098",
     "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"],
     "timestamp_ms": "1660155761384"
   }
 }

    
```





Code copied to clipboard








#### Tweet delete












```

      {
  "delete": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220608",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
  }
}
    
```






#### Tweet withheld












```

      {
  "status_withheld": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220608",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "withheld_in_countries": [
      "XY"
    ],
    "timestamp_ms": "1432228155593"
  }
}
    
```






#### Drop












```

      {
  "drop": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220600",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
  }
}
    
```






#### Undrop












```

      {
  "undrop": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220600",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
  }
}
    
```






#### Scrub geo












```

      {
  "scrub_geo": {
    "user_id": 519761961,
    "up_to_status_id": 411552403083628540,
    "up_to_status_id_str": "411552403083628544",
    "user_id_str": "519761961",
    "timestamp_ms": "1432228180345"
  }
}
    
```






#### User delete












```

      {
  "user_delete": {
    "id": 771136850,
    "timestamp_ms": "1432228153548"
  }
}
    
```






#### User undelete












```

      {
  "user_undelete": {
    "id": 796250066,
    "timestamp_ms": "1432228149062"
  }
}
    
```






#### User withheld












```

      {
  "user_withheld": {
    "user": {
      "id": 1375036644,
      "id_str": "1375036644"
    },
    "withheld_in_countries": [
      "XY"
    ],
    "timestampMs": "2014-08-27T23:49:41.839+00:00"
  }
}
    
```






#### User protect












```

      {
  "user_protect": {
    "id": 3182003550,
    "timestamp_ms": "1432228177137"
  }
}
    
```






#### User unprotect












```

      {
  "user_unprotect": {
    "id": 2911076065,
    "timestamp_ms": "1432228180113"
  }
}
    
```






#### User suspend












```

      {
  "user_suspend": {
    "id": 3120539094,
    "timestamp_ms": "1432228194217"
  }
}
    
```






#### User unsuspend












```

      {
  "user_unsuspend": {
    "id": 3293130873,
    "timestamp_ms": "1432228193828"
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















