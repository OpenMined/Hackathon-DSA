



GET /2/users/:id/followers | Docs | Twitter Developer Platform 





































































































GET /2/users/:id/followers



 GET /2/users/:id/followers
==========================

Returns a list of users who are followers of the specified user ID.

Run in Postman ❯Try a live request ❯Build request with API Explorer ❯### Endpoint URL

`https://api.twitter.com/2/users/:id/followers`  
  
### Authentication and rate limits



|  |  |
| --- | --- |
| Authentication methodssupported by this endpoint | OAuth 2.0 Authorization Code with PKCEOAuth 1.0a is also available for this endpoint.OAuth 2.0 App-only |
| Rate limit | App rate limit (Application-only): 15 requests per 15-minute window shared among all users of your appUser rate limit (User context): 15 requests per 15-minute window per each authenticated user |

### OAuth 2.0 scopes required by this endpoint



|  |
| --- |
| `tweet.read``users.read``follows.read` |
| Learn more about OAuth 2.0 Authorization Code with PKCE |

### Path parameters



| Name | Type | Description |
| --- | --- | --- |
| `id` Required  | string | The user ID whose followers you would like to retrieve. |

  
  
### Query parameters



| Name | Type | Description |
| --- | --- | --- |
| `expansions` Optional  | enum (`pinned_tweet_id`) | Expansions enable you to request additional data objects that relate to the originally returned users. The ID that represents the expanded data object will be included directly in the user data object, but the expanded object metadata will be returned within the `includes` response object, and will also include the ID so that you can match this data object to the original Tweet object. At this time, the only expansion available to endpoints that primarily return user objects is `expansions=pinned_tweet_id`. You will find the expanded Tweet data object living in the `includes` response object. |
| `max_results` Optional  | integer | The maximum number of results to be returned per page. This can be a number between 1 and the 1000. By default, each page will return 100 results. |
| `pagination_token` Optional  | string | Used to request the next page of results if all results weren't returned with the latest request, or to go back to the previous page of results. To return the next page, pass the `next_token` returned in your previous response. To go back one page, pass the `previous_token` returned in your previous response. |
| `tweet.fields` Optional  | enum (`attachments`, `author_id`, `context_annotations`, `conversation_id`, `created_at`, `edit_controls`, `entities`, `geo`, `id`, `in_reply_to_user_id`, `lang`, `non_public_metrics`, `public_metrics`, `organic_metrics`, `promoted_metrics`, `possibly_sensitive`, `referenced_tweets`, `reply_settings`, `source`, `text`, `withheld`) | This fields parameter enables you to select which specific Tweet fields will deliver in each returned pinned Tweet. Specify the desired fields in a comma-separated list without spaces between commas and fields. The Tweet fields will only return if the user has a pinned Tweet and if you've also included the `expansions=pinned_tweet_id` query parameter in your request. While the referenced Tweet ID will be located in the original Tweet object, you will find this ID and all additional Tweet fields in the `includes` data object. |
| `user.fields` Optional  | enum (`created_at`, `description`, `entities`, `id`, `location`, `most_recent_tweet_id`, `name`, `pinned_tweet_id`, `profile_image_url`, `protected`, `public_metrics`, `url`, `username`, `verified`, `verified_type`, `withheld`) | This fields parameter enables you to select which specific user fields will deliver with each returned users objects. Specify the desired fields in a comma-separated list without spaces between commas and fields. These specified user fields will display directly in the user data objects. |

  
  
### Example code with offical SDKs








* TypeScript (Default fields)
* TypeScript (Optional fields)
* Java (Default fields)
* Java (Optional fields)


















 TypeScript (Default fields)
 

 TypeScript (Optional fields)
 

 Java (Default fields)
 

 Java (Optional fields)
 
















```

      (async () => {
  try {
    const getUsersFollowers = await twitterClient.users.usersIdFollowers(
      //The ID of the user for whom to return results
      "2244994945"
    );
    console.dir(getUsersFollowers, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      (async () => {
  try {
    const getUsersFollowers = await twitterClient.users.usersIdFollowers(
      //The ID of the user for whom to return results
      "2244994945",
      {
        //A comma separated list of User fields to display
        "user.fields": ["created_at"],
        
        //A comma separated list of Tweet fields to display.
        "tweet.fields": ["created_at"],
        
        //A comma separated list of fields to expand
        expansions: ["pinned_tweet_id"],

        //The maximum number of results
        max_results: 10,
      }
    );
    console.dir(getUsersFollowers, {
      depth: null,
    });
  } catch (error) {
    console.log(error);
  }
})();

    
```
















```

      // Set the params values

// String | The ID of the user for whom to return results
String id = "2244994945";

try {
    GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdFollowers(id, null, null, null, null, null);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#usersIdFollowers");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```
















```

      // Set the params values

// String | The ID of the user for whom to return results
String id = "2244994945";

// Integer | The maximum number of results to be returned.
Integer maxResults = 10;

// Set<String> | A comma separated list of fields to expand.
Set<String> expansions = new HashSet<>(Arrays.asList("pinned_tweet_id"));

// Set<String> | A comma separated list of Tweet fields to display.
Set<String> tweetFields = new HashSet<>(Arrays.asList("created_at")); 

// Set<String> | A comma separated list of User fields to display.
Set<String> userFields = new HashSet<>(Arrays.asList("created_at"));

try {
    GenericMultipleUsersLookupResponse result = apiInstance.users().usersIdFollowers(id, maxResults, null, userFields, expansions, tweetFields);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling UsersApi#usersIdFollowers");
    System.err.println("Status code: " + e.getCode());
    System.err.println("Reason: " + e.getResponseBody());
    System.err.println("Response headers: " + e.getResponseHeaders());
    e.printStackTrace();
}

    
```












### Example responses








* Default fields
* Optional fields


















 Default fields
 

 Optional fields
 
















```

      {
  "data": [
    {
      "id": "6253282",
      "name": "Twitter API",
      "username": "TwitterAPI"
    },
    {
      "id": "2244994945",
      "name": "Twitter Dev",
      "username": "TwitterDev"
    },
    {
      "id": "783214",
      "name": "Twitter",
      "username": "Twitter"
    },
    {
      "id": "95731075",
      "name": "Twitter Safety",
      "username": "TwitterSafety"
    },
    {
      "id": "3260518932",
      "name": "Twitter Moments",
      "username": "TwitterMoments"
    },
    {
      "id": "373471064",
      "name": "Twitter Music",
      "username": "TwitterMusic"
    },
    {
      "id": "791978718",
      "name": "Twitter Official Partner",
      "username": "OfficialPartner"
    },
    {
      "id": "17874544",
      "name": "Twitter Support",
      "username": "TwitterSupport"
    },
    {
      "id": "234489024",
      "name": "Twitter Comms",
      "username": "TwitterComms"
    },
    {
      "id": "1526228120",
      "name": "Twitter Data",
      "username": "TwitterData"
    }
  ],
  "meta": {
    "result_count": 10,
    "next_token": "DFEDBNRFT3MHCZZZ"
  }
}
    
```
















```

      {
  "data": [
    {
      "pinned_tweet_id": "1293595870563381249",
      "id": "6253282",
      "username": "TwitterAPI",
      "name": "Twitter API"
    },
    {
      "pinned_tweet_id": "1293593516040269825",
      "id": "2244994945",
      "username": "TwitterDev",
      "name": "Twitter Dev"
    },
    {
      "id": "783214",
      "username": "Twitter",
      "name": "Twitter"
    },
    {
      "pinned_tweet_id": "1271186240323432452",
      "id": "95731075",
      "username": "TwitterSafety",
      "name": "Twitter Safety"
    },
    {
      "id": "3260518932",
      "username": "TwitterMoments",
      "name": "Twitter Moments"
    },
    {
      "pinned_tweet_id": "1293216056274759680",
      "id": "373471064",
      "username": "TwitterMusic",
      "name": "Twitter Music"
    },
    {
      "id": "791978718",
      "username": "OfficialPartner",
      "name": "Twitter Official Partner"
    },
    {
      "pinned_tweet_id": "1289000334497439744",
      "id": "17874544",
      "username": "TwitterSupport",
      "name": "Twitter Support"
    },
    {
      "pinned_tweet_id": "1283543147444711424",
      "id": "234489024",
      "username": "TwitterComms",
      "name": "Twitter Comms"
    },
    {
      "id": "1526228120",
      "username": "TwitterData",
      "name": "Twitter Data"
    }
  ],
  "includes": {
    "tweets": [
      {
        "context_annotations": [
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
              "id": "65",
              "name": "Interests and Hobbies Vertical",
              "description": "Top level interests and hobbies groupings, like Food or Travel"
            },
            "entity": {
              "id": "848920371311001600",
              "name": "Technology",
              "description": "Technology and computing"
            }
          },
          {
            "domain": {
              "id": "66",
              "name": "Interests and Hobbies Category",
              "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
            },
            "entity": {
              "id": "848921413196984320",
              "name": "Computer programming",
              "description": "Computer programming"
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
          }
        ],
        "id": "1293595870563381249",
        "text": "Twitter API v2: Early Access releasednnToday we announced Early Access to the first endpoints of the new Twitter API!nn#TwitterAPI #EarlyAccess #VersionBump https://t.co/g7v3aeIbtQ"
      },
      {
        "context_annotations": [
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
              "id": "65",
              "name": "Interests and Hobbies Vertical",
              "description": "Top level interests and hobbies groupings, like Food or Travel"
            },
            "entity": {
              "id": "848920371311001600",
              "name": "Technology",
              "description": "Technology and computing"
            }
          },
          {
            "domain": {
              "id": "66",
              "name": "Interests and Hobbies Category",
              "description": "A grouping of interests and hobbies entities, like Novelty Food or Destinations"
            },
            "entity": {
              "id": "848921413196984320",
              "name": "Computer programming",
              "description": "Computer programming"
            }
          }
        ],
        "id": "1293593516040269825",
        "text": "It’s finally here! 🥁 Say hello to the new #TwitterAPI.nnWe’re rebuilding the Twitter API v2 from the ground up to better serve our developer community. And today’s launch is only the beginning.nnhttps://t.co/32VrwpGaJw https://t.co/KaFSbjWUA8"
      },
      {
        "id": "1271186240323432452",
        "text": "We’re disclosing new state-linked information operations to our public archive — the only one of its kind in the industry. Originating from the People’s Republic of China (PRC), Russia, and Turkey, all associated accounts and content have been removed. https://t.co/obRqr96iYm"
      },
      {
        "id": "1293216056274759680",
        "text": "say howdy to your new yeehaw king @orvillepeck—our #ArtistToFollow this month 🤠 https://t.co/3pk9fYcPHb"
      },
      {
        "context_annotations": [
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
          }
        ],
        "id": "1289000334497439744",
        "text": "We’ve significantly limited access to our internal tools and systems. Until we can safely resume normal operations, our response times to some support needs and reports will be slower. Thank you for your patience as we work through this."
      },
      {
        "context_annotations": [
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
          }
        ],
        "id": "1283543147444711424",
        "text": "Follow @TwitterSupport for the latest on the security incident ⬇️ https://t.co/7FKKksJqxV"
      }
    ],
    "meta": {
      "result_count": 10,
      "next_token": "DFEDBNRFT3MHCZZZ"
    }
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
| `meta` Default  | object | This object contains information about the number of users returned in the current request, and pagination details. |
| `meta.result_count` Default  | integer | The number of users returned in this request. Note that this number may be lower than what was specified in the `max_results` query parameter. |
| `meta.previous_token` | string | Pagination token for the previous page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To go back to the previous page, passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you are on the first page of results. |
| `meta.next_token` | string | Pagination token for the next page of results. This value is returned when there are multiple pages of results, as the current request may only return a subset of results. To retrieve the full list, keep passing the value from this field in the `pagination_token` query parameter. When this field is not returned in the response, it means you've reached the last page of results, and that there are no further pages. |



















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















