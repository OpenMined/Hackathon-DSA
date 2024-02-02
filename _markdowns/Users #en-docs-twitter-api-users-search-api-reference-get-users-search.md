



GET /2/users/search | Docs | Twitter Developer Platform 





































































































GET /2/users/search



GET /2/users/search
===================


The users endpoint returns Users that match a search query. This endpoint has a limit of 10,000 requests per 24 hours (in addition to the 300 requests per 15 minutes.


Run in Postman ❯

### Endpoint URL


`https://api.twitter.com/2/users/search`  

  




### Authentication and rate limits




|  |  |
| --- | --- |
| Authentication methods
supported by this endpoint | OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 300 requests per 15-minute window shared among all users of your app |


### Query parameters




| Name | Type | Description |
| --- | --- | --- |
| `query`
 Required  | string | One query for matching Tweets. You can learn how to build this query by reading our build a query guide.

If you have Essential or Elevated access, you can use the Basic operators when building your query and can make queries up to 512 characters long. If you have been approved for Academic Research access, you can use all available operators and can make queries up to 1,024 characters long.

Learn more about our access levels on the about Twitter API page. |
| `expansions`
 Optional  | enum (`pinned_tweet_id`) | Expansions enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results`
 Optional  | integer | The maximum number of search results to be returned by a request. A number between 1 and 1000. By default, a request response will return 100 results. |
| `next_token`
 Optional  | string | This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified. |
| `tweet.fields`
 Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields`
 Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |






### Example responses








* Default Fields
* Optional Fields


















 Default Fields
 

 Optional Fields
 
















```

      {
  "data": [
    {
      "id": "2244994945",
      "name": "Developers",
      "username": "XDevelopers"
    },
    {
      "id": "857699969263964161",
      "name": "Suhem Parack",
      "username": "suhemparack"
    },
    {
      "id": "2533341854",
      "name": "Chris Park",
      "username": "chrisparkX"
    },
    {
      "id": "853388192",
      "name": "Haim Vaturi",
      "username": "haimvat"
    },
    {
      "id": "829457852125306890",
      "name": "ROBLOX Devs",
      "username": "RBXdevelopers"
    },
    {
      "id": "70915829",
      "name": "Twitter Dev Japan",
      "username": "TwitterDevJP"
    },
    {
      "id": "1619352801104039936",
      "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",
      "username": "0xdevelopersTm"
    },
    {
      "id": "708786906058756096",
      "name": "Project X Developers",
      "username": "ProXDevelopers"
    },
    {
      "id": "1315227013028904960",
      "name": "XDevelopersUS",
      "username": "XDevelopersUS"
    },
    {
      "id": "3296066705",
      "name": "XDevelopers",
      "username": "XDevBrasil"
    },
    {
      "id": "1234855897370910720",
      "name": "ajX developers",
      "username": "ajXdevelopers"
    },
    {
      "id": "1453775246",
      "name": "The X Developers",
      "username": "TheXDevelopers"
    },
    {
      "id": "1513675812486193158",
      "name": "RBLXdevelopers",
      "username": "XdevelopersRbl"
    },
    {
      "id": "1375178694520627204",
      "name": "XDevelopersUK",
      "username": "XDevelopersUK"
    },
    {
      "id": "1363113804842881024",
      "name": "xDevelopers",
      "username": "xdevelopers_st"
    },
    {
      "id": "2885219741",
      "name": "xdevelopers",
      "username": "itdenps"
    },
    {
      "id": "1684769811539087362",
      "name": "X",
      "username": "xdevelopers_es"
    },
    {
      "id": "732232220803485696",
      "name": "XDevelopers",
      "username": "XDeveloper_"
    },
    {
      "id": "831241935675326464",
      "name": "xDevelopers",
      "username": "developers_x"
    },
    {
      "id": "1580611661169238016",
      "name": "0xspark",
      "username": "0xdevelopers"
    },
    {
      "id": "2175184873",
      "name": "XeXDevelopers",
      "username": "XeXDevelopers"
    },
    {
      "id": "1684141917129539585",
      "name": "Izu",
      "username": "XDevelopersJP"
    },
    {
      "id": "1521381726",
      "name": "SXDevelopers",
      "username": "SonyXDevelopers"
    }
  ],
  "meta": {
    "next_token": "5qym3iwm0eyn796h9x2mc2ri54ub5te"
  }
}
    
```
















```

      {
  "data": [
    {
      "location": "127.0.0.1",
      "name": "Developers",
      "description": "The voice of the X Dev team and your official source for updates, news, and events, related to the X API.",
      "username": "XDevelopers",
      "id": "2244994945"
    },
    {
      "location": "Seattle, WA",
      "name": "Suhem Parack",
      "description": "Partner Engineering @XDevelopers",
      "username": "suhemparack",
      "id": "857699969263964161"
    },
    {
      "location": "New York, NY",
      "name": "Chris Park",
      "description": "𝕏 | @X @API @XDevelopers",
      "username": "chrisparkX",
      "id": "2533341854"
    },
    {
      "location": "Islington, London",
      "name": "Haim Vaturi",
      "description": "@XDevelopers",
      "username": "haimvat",
      "id": "853388192"
    },
    {
      "location": "Canada",
      "name": "ROBLOX Devs",
      "description": "Follow this account for a lot of cool ROBLOXdev from all kinds of different ROBLOX developers! Not an official @ROBLOX twitter account",
      "username": "RBXdevelopers",
      "id": "829457852125306890"
    },
    {
      "location": "東京都港区",
      "name": "Twitter Dev Japan",
      "description": "This account is no longer active. Follow @XDevelopers for updates.",
      "username": "TwitterDevJP",
      "id": "70915829"
    },
    {
      "name": "Rains®™☔️🧠 0xdevelopers.eth.eth",
      "description": "",
      "username": "0xdevelopersTm",
      "id": "1619352801104039936"
    },
    {
      "name": "Project X Developers",
      "description": "",
      "username": "ProXDevelopers",
      "id": "708786906058756096"
    },
    {
      "location": "Los Angeles, CA",
      "name": "XDevelopersUS",
      "description": "",
      "username": "XDevelopersUS",
      "id": "1315227013028904960"
    },
    {
      "location": "Rio de Janeiro & São Paulo",
      "name": "XDevelopers",
      "description": "Contato e Suporte Via Telefone (RJ): 21 980534086 e Via Email: contato@XDevelopers.com.br",
      "username": "XDevBrasil",
      "id": "3296066705"
    },
    {
      "location": "India",
      "name": "ajX developers",
      "description": "app developernweb designernentrepreneurnmachine learningnAI PIONEERnage just 16",
      "username": "ajXdevelopers",
      "id": "1234855897370910720"
    },
    {
      "name": "The X Developers",
      "description": "",
      "username": "TheXDevelopers",
      "id": "1453775246"
    },
    {
      "name": "RBLXdevelopers",
      "description": "",
      "username": "XdevelopersRbl",
      "id": "1513675812486193158"
    },
    {
      "location": "London, England",
      "name": "XDevelopersUK",
      "description": "",
      "username": "XDevelopersUK",
      "id": "1375178694520627204"
    },
    {
      "name": "xDevelopers",
      "description": "",
      "username": "xdevelopers_st",
      "id": "1363113804842881024"
    },
    {
      "name": "xdevelopers",
      "description": "",
      "username": "itdenps",
      "id": "2885219741"
    },
    {
      "name": "X",
      "description": "",
      "username": "xdevelopers_es",
      "id": "1684769811539087362"
    },
    {
      "name": "XDevelopers",
      "description": "",
      "username": "XDeveloper_",
      "id": "732232220803485696"
    },
    {
      "name": "xDevelopers",
      "description": "",
      "username": "developers_x",
      "id": "831241935675326464"
    },
    {
      "location": "United States",
      "name": "0xspark",
      "description": "",
      "username": "0xdevelopers",
      "id": "1580611661169238016"
    },
    {
      "name": "XeXDevelopers",
      "description": "",
      "username": "XeXDevelopers",
      "id": "2175184873"
    },
    {
      "name": "Izu",
      "description": "",
      "username": "XDevelopersJP",
      "id": "1684141917129539585"
    },
    {
      "name": "SXDevelopers",
      "description": "",
      "username": "SonyXDevelopers",
      "id": "1521381726"
    }
  ],
  "meta": {
    "next_token": "5qym3iwm0f05lqu1ezcdkohsl2i4lyq"
  }
}
    
```












### Response fields



| Name | Type | Description |
| --- | --- | --- |
| `id` Default  | string | Unique identifier of this user. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers. |
| `name` Default  | string | The friendly name of this user, as shown on their profile. |
| `username` Default  | string | The Twitter handle (screen name) of this user. |
| `created_at` | date (ISO 8601) | Creation time of this account.To return this field, add `user.fields=created_at` in the request's query parameter. |
| `most_recent_tweet_id` | string | The ID of the User's most recent TweetTo return this field, add `user.fields=most_recent_tweet_id` in the request's query parameter. |
| `protected` | boolean | Indicates if this user has chosen to protect their Tweets (in other words, if this user's Tweets are private).To return this field, add `user.fields=protected` in the request's query parameter. |
| `withheld` | object | Contains withholding details for withheld content.To return this field, add `user.fields=withheld` in the request's query parameter. |
| `withheld.country_codes` | array | Provides a list of countries where this user is not available.To return this field, add `user.fields=withheld.country_codes` in the request's query parameter. |
| `withheld.scope` | enum (`tweet`, `user`) | Indicates whether the content being withheld is a Tweet or a user (this API will return `user`).To return this field, add `user.fields=withheld.scope` in the request's query parameter. |
| `location` | string | The location specified in the user's profile, if the user provided one. As this is a freeform value, it may not indicate a valid location, but it may be fuzzily evaluated when performing searches with location queries.To return this field, add `user.fields=location` in the request's query parameter. |
| `url` | string | The URL specified in the user's profile, if present.To return this field, add `user.fields=url` in the request's query parameter. |
| `description` | string | The text of this user's profile description (also known as bio), if the user provided one.To return this field, add `user.fields=description` in the request's query parameter. |
| `verified` | boolean | Indicate if this user is a verified Twitter user.To return this field, add `user.fields=verified` in the request's query parameter. |
| `verified_type` | enum (`blue`, `business`, `government`, `none`) | Indicates the type of verification for the Twitter account.To return this field, add `user.fields=verified_type` in the request's query parameter. |
| `entities` | object | This object and its children fields contain details about text that has a special meaning in the user's description.To return this field, add `user.fields=entities` in the request's query parameter. |
| `entities.url` | array | Contains details about the user's profile website. |
| `entities.url.urls` | array | Contains details about the user's profile website. |
| `entities.url.urls.start` | integer | The start position (zero-based) of the recognized user's profile website. All start indices are inclusive. |
| `entities.url.urls.end` | integer | The end position (zero-based) of the recognized user's profile website. This end index is exclusive. |
| `entities.url.urls.url` | string | The URL in the format entered by the user. |
| `entities.url.urls.expanded_url` | string | The fully resolved URL. |
| `entities.url.urls.display_url` | string | The URL as displayed in the user's profile. |
| `entities.description` | array | Contains details about URLs, Hashtags, Cashtags, or mentions located within a user's description. |
| `entities.description.urls` | array | Contains details about any URLs included in the user's description. |
| `entities.description.urls.start` | integer | The start position (zero-based) of the recognized URL in the user's description. All start indices are inclusive. |
| `entities.description.urls.end` | integer | The end position (zero-based) of the recognized URL in the user's description. This end index is exclusive. |
| `entities.description.urls.url` | string | The URL in the format entered by the user. |
| `entities.description.urls.expanded_url` | string | The fully resolved URL. |
| `entities.description.urls.display_url` | string | The URL as displayed in the user's description. |
| `entities.description.hashtags` | array | Contains details about text recognized as a Hashtag. |
| `entities.description.hashtags.start` | integer | The start position (zero-based) of the recognized Hashtag within the Tweet. All start indices are inclusive. |
| `entities.description.hashtags.end` | integer | The end position (zero-based) of the recognized Hashtag within the Tweet. This end index is exclusive. |
| `entities.description.hashtags.hashtag` | string | The text of the Hashtag. |
| `entities.description.mentions` | array | Contains details about text recognized as a user mention. |
| `entities.description.mentions.start` | integer | The start position (zero-based) of the recognized user mention within the Tweet. All start indices are inclusive. |
| `entities.description.mentions.end` | integer | The end position (zero-based) of the recognized user mention within the Tweet. This end index is exclusive. |
| `entities.description.mentions.username` | string | The part of text recognized as a user mention. |
| `entities.description.cashtags` | array | Contains details about text recognized as a Cashtag. |
| `entities.description.cashtags.start` | integer | The start position (zero-based) of the recognized Cashtag within the Tweet. All start indices are inclusive. |
| `entities.description.cashtags.end` | integer | The end position (zero-based) of the recognized Cashtag within the Tweet. This end index is exclusive. |
| `entities.description.cashtags.cashtag` | string | The text of the Cashtag. |
| `profile_image_url` | string | The URL to the profile image for this user, as shown on the user's profile. |
| `public_metrics` | object | Contains details about activity for this user. |
| `public_metrics.followers_count` | integer | Number of users who follow this user. |
| `public_metrics.following_count` | integer | Number of users this user is following. |
| `public_metrics.tweet_count` | integer | Number of Tweets (including Retweets) posted by this user. |
| `public_metrics.listed_count` | integer | Number of lists that include this user. |
| `pinned_tweet_id` | string | Unique identifier of this user's pinned Tweet.You can obtain the expanded object in `includes.tweets` by adding `expansions=pinned_tweet_id` in the request's query parameter. |
| `includes.tweets` | array | When including the `expansions=pinned_tweet_id` parameter, this includes the pinned Tweets attached to the returned users' profiles in the form of Tweet objects with their default fields and any additional fields requested using the `tweet.fields` parameter, assuming there is a referenced Tweet present in the returned Tweet(s). |
| `errors` | object | Contains details about errors that affected any of the requested users. See Status codes and error messages for more details. |



















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















