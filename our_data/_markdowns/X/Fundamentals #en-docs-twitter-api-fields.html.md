
Fields | Docs | Twitter Developer Platform 

Fields

The Twitter API v2 endpoints are equipped with a set of parameters called *fields,* which allows you to select just the data that you want from each of the objects in your endpoint response.

By default, the Tweet object only returns the id and the text fields, and for Tweets created since September 29, 2022, the edit\_history\_tweet\_ids field. If you need the Tweet’s created date or public metrics, you will need to use the tweet.fields parameters to request them. This provides a higher degree of customization by enabling you to only request the fields you require depending on your use case. For example, you would include this query string in your request 

?tweet.fields=created\_at,public\_metrics

Each object has its own parameter which is used to specifically request the fields that are associated with that object. Here are the different fields parameters that are currently available:  

* Tweet → `tweet.fields`
* User → `user.fields`
* Media → `media.fields`
* Poll → `poll.fields`
* Place → `place.fields`

When using an endpoint that primarily returns a particular object, simply use the matching field parameter and specify the field(s) desired in a comma-separated list as the value to that parameter to retrieve those fields in the response.  

### Example

If you are using the GET /tweets/search/recent endpoint, you will primarily receive Tweet objects in that response. Without specifying any fields parameters, you will just receive the default values, `id` and `text`. If you are interested in receiving the public metrics of the Tweets that are returned in the response, you will want to include the `tweet.fields` parameter in your request, with `public_metrics` set as the value. 

This request would look like the following. If you would like to use this request, make sure to replace $BEARER\_TOKEN with your Bearer Token and send it using your command line tool.  

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
```

Code copied to clipboard

If you send this request in your terminal, then each of the Tweets that return will include the following fields:

```
      {
   "data": {
       "id": "1263150595717730305",
       "public_metrics": {
           "retweet_count": 12,
           "reply_count": 14,
           "like_count": 49,
           "quote_count": 7
       },
       "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER"
   }
}
```

If you would like to retrieve a set of fields from a secondary object that is associated with the primary object returned by an endpoint, you will need to include an additional `expansions` parameter. 

For example, if you were using the same GET search/tweets/recent endpoint as earlier, and you wanted to retrieve the author's profile description, you will have to pass the expansions=author\_id and user.fields=description with your request. Here is an example of what this might look like. If you would like to try this request, make sure to replace the $BEARER\_TOKEN with your Bearer Token before pasting it into your command line tool.

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=from%3Atwitterdev&tweet.fields=public_metrics&expansions=author_id&user.fields=description' \
  --header 'Authorization: Bearer $BEARER_TOKEN'
```

Code copied to clipboard

If you specify this in the request, then each of the Tweets that deliver will have the following fields, and the related user object's default and specified fields will return within includes. The user object can be mapped back to the corresponding Tweet(s) by matching the tweet.author\_id and users.id fields.  

```
      {
  "data": [
    {
      "id": "1263150595717730305",
      "author_id": "2244994945",
      "text": "Do you 👀our new Tweet settings?\n\nWe want to know how and why you’d use a feature like this in the API. Get the details and let us know what you think👇\nhttps://t.co/RtMhhfAcIB https://t.co/8wxeZ9fJER",
      "public_metrics": {
        "retweet_count": 12,
        "reply_count": 13,
        "like_count": 51,
        "quote_count": 7
      }
    }
  ],
  "includes": {
    "users": [
      {
        "id": "2244994945",
        "username": "TwitterDev",
        "description": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "name": "Twitter Dev"
      }
    ]
  }
}
```

Bear in mind that you cannot request specific subfields (for example, `public_metrics.retweet_count`). All subfields will be returned when the top-level field (`public_metrics`) is specified. We have listed all possible fields that you can request in each endpoints' API reference page's parameters table. 

A full list of fields are listed in the object model. To expand and request fields on an object that is not that endpoint’s primary resource, use the expansions parameter with fields.

Next step
---------

Learn how to use fields with expansions

Review the different data objects available with Twitter API v2

Make your first request with fields and expansions

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