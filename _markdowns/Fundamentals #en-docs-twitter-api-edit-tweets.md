



Edit Tweets | Docs | Twitter Developer Platform 





































































































Edit Tweets



Introduction
------------


The Twitter API v2 endpoints provide edited Tweet metadata. The *Edit Tweets* feature was first introduced for testing among Twitter employees on September 1, 2022. Starting on that date, eligible Tweets are editable for 30 minutes and up to 5 times. *All objects for Tweets created since September 29, 2022* include Tweet edit metadata, even if the Tweet was never edited. Each time a Tweet is edited, a new Tweet ID is created. A Tweet's edit history can be described by chaining these IDs together, starting with the original ID.  Additionally, if any Tweet in the edit chain is deleted, all Tweets in that chain are deleted as well.


Using the Twitter API v2, a developer can find out:


* If a Tweet was edit eligible at the time of creation. Some Tweets, such as those with polls or scheduled Tweets, can not be edited.
* Tweets are editable for 30 minutes, and can be edited up to 5 times. For editable Tweets you can see if time for editing remains and how many more edits are possible.
* If you are viewing an edited version of a Tweet (in most cases the API will return the most recent version of a Tweet, unless a specific past version is requested by Tweet ID).
* The entire edit history of the Tweet.
* The engagement attributed to each version of the Tweet.


There are three components to a Tweet’s edit history:


1. By default, the Tweet payload will contain an array of Tweet IDs that are part of a Tweet’s edit history. This information is specified by the edit\_history\_tweet\_ids, which is a default field in the Tweet payload. This array will contain at least one ID, the ID of the original, unedited Tweet. When there is only one ID that means the Tweet has no edit history.
2. You can get information such as whether a Tweet was editable at the time it was created, how much time, if any, is remaining for a Tweet to be edited, and how many edits remain by specifying edit\_controls in your tweet.fields parameter.
3. Finally, you can get the Tweet objects for each Tweet in a Tweet’s edit history, by specifying the edit\_history\_tweet\_ids using the expansion parameter


 


Most Tweets are eligible for editing. However, the following types of Tweets are not:   




* Tweet is promoted
* Tweet has a poll
* Tweet is a non-self-thread reply
* Tweet is a Retweet (note that Quote Tweets are eligible for edit)
* Tweet is nullcast
* Community Tweet
* Superfollow Tweet
* Collaborative Tweet



Examples
--------


The examples below demonstrate how a developer can request edited Tweet metadata using the Twitter API v2. 


**Note:** The examples below use the User Tweet Timeline endpoint, but you can request this metadata using the same parameters (with fields and expansions) for all endpoints that return Tweets (e.g. Tweets lookup, search, filtered stream,  etc.)


### Default behavior


By default, an API request to any endpoint that returns Tweet objects in the Twitter API v2, you get:


* The Tweet ID
* The Tweet Text
* An array of Tweet IDs that are part of a Tweet’s edit history. If there is only one ID provided, that means the Tweet has not been edited.


**Request:**












```

      curl --request GET 'https://api.twitter.com/2/users/:id/tweets' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








**Sample Response:**












```

      {
  "data": [
    {
      "id": "1514991667853602823",
      "text": "we have an edit button",
      "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"]
    }
  ]
}
    
```





Code copied to clipboard








### Getting additional data with edit\_controls


If you want additional edited Tweet metadata such as whether a Tweet was eligible to be edited when it was created and how much time is remaining for a Tweet to be editable, you can request this information using the tweet.fields parameter and setting it to edit\_control.


**Request:**












```

      curl --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








**Sample Response:**












```

      {
  "data": [
    {
      "id": "1514991667853602823",
      "text": "we have an edit button",
      "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],
      "edit_controls": {
        "is_edit_eligible": true,
        "editable_until": "2022-04-21 09:35:20.311",
        "edits_remaining": 4
      }
    }
  ]
}
    
```





Code copied to clipboard








### Getting Tweet objects for all Tweets in a Tweet’s edit history


The examples above provide an array of Tweet IDs in a Tweet’s edit history. If you want the actual Tweet object for each of these Tweet IDs, you can use the expansion parameter and set it to edit\_history\_tweet\_ids. The Tweet objects that make up the edit history will be provided in the "includes" object. 


**Request:**












```

      curl --location --request GET 'https://api.twitter.com/2/users/:id/tweets?tweet.fields=edit_control&expansions=edit_history_tweet_ids' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








**Sample Response:**












```

      {
  "data": [
    {
      "id": "1514991667853602823",
      "text": "we have an edit button",
      "edit_history_tweet_ids": ["1514991667853602822", "1514991667853602823"],
      "edit_controls": {
        "is_edit_eligible": true,
        "editable_until": "2022-04-21 09:35:20.311",
        "edits_remaining": 4
      }
    }
  ],
  "includes": {
    "tweets": [
      {
        "id": "1514991667853602822",
        "text": "we need an eidt button",
        "edit_history_tweet_ids": [
          "1514991667853602822",
          "1514991667853602823"
        ],
        "edit_controls": {
          "is_edit_eligible": true,
          "editable_until": "2022-04-21 09:35:20.311",
          "edits_remaining": 4
        }
      }
    ]
  }
}
    
```





Code copied to clipboard





















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















