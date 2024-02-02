
Conversation ID | Docs | Twitter Developer Platform 

Conversation ID

Conversation threads using the Twitter API
------------------------------------------

If you look at how conversations evolve on Twitter, one Tweet can spark several conversation threads, each of which can grow in length and complexity as more people chime in. Identifying relationships between Tweets and understanding conversation threads is a feature of the Twitter API v2 payload and search capabilities.  When Tweets are posted in response to a Tweet (known as a reply), or in response to a reply, there is now a defined conversation\_id on each reply, which matches the Tweet ID of the original Tweet that started the conversation. 

Replies to a given Tweet, as well as replies to those replies, are all included in the conversation stemming from the single original Tweet. Regardless of how many reply threads result, they will all share a common conversation\_id to the original Tweet that sparked the conversation. Using the Twitter API v2, you have the ability to retrieve and reconstruct an entire conversation thread, so that you can better understand what is being said, and how conversations and ideas evolve.   

#### The example below shows a conversation thread of five different people, including one reply to a reply:

```
      {
	"data": [{
			"conversation_id": "1279944223114900000",
			"in_reply_to_user_id": "1102323333",
			"author_id": "63044444",
			"created_at": "2020-07-06T15:58:10.000Z",
			"id": "1280169177479744444",
			"referenced_tweets": [{
				"type": "replied_to",
				"id": "1280155225706433333"
			}],
			"text": "@ThirdPerson333 @OriginalPerson000 Reply to the third reply!"
		},
		{
			"conversation_id": "1279944223114900000",
			"in_reply_to_user_id": "3001960000",
			"author_id": "1102323333",
			"created_at": "2020-07-06T15:02:44.000Z",
			"id": "1280155225706433333",
			"referenced_tweets": [{
				"type": "replied_to",
				"id": "1279944223114900000"
			}],
			"text": "@OriginalPerson000 Third reply"
		},
		{
			"conversation_id": "1279944223114900000",
			"in_reply_to_user_id": "3001960000",
			"author_id": "199562222",
			"created_at": "2020-07-06T15:02:36.000Z",
			"id": "1280155190306340864",
			"referenced_tweets": [{
				"type": "replied_to",
				"id": "1279944223114900000"
			}],
			"text": "@OriginalPerson000 Second Reply"
		},
		{
			"conversation_id": "1279944223114900000",
			"in_reply_to_user_id": "3001960000",
			"author_id": "179201111",
			"created_at": "2020-07-06T01:10:15.000Z",
			"id": "1279945722494811111",
			"referenced_tweets": [{
				"type": "replied_to",
				"id": "1279944223114900000"
			}],
			"text": "@OriginalPerson000 First Reply"
		}
	],
	"includes": {
		"users": [{
				"name": "Original person",
				"id": "3001960000",
				"username": "OriginalPerson000"
			},
			{
				"name": "First person",
				"id": "179201111",
				"username": "FirstPerson111"
			}, {
				"name": "Second person",
				"id": "199562222",
				"username": "SecondPerson222"
			}, {
				"name": "Third person",
				"id": "1102323333",
				"username": "ThirdPerson333"
			}, {
				"name": "Fourth person",
				"id": "63044444",
				"username": "FourthPerson444"
			}
		],
		"tweets": [{
				"conversation_id": "1279944223114900000",
				"in_reply_to_user_id": "3001960000",
				"author_id": "1102323333",
				"created_at": "2020-07-06T15:02:44.000Z",
				"id": "1280155225706433333",
				"referenced_tweets": [{
					"type": "replied_to",
					"id": "1279944223114900000"
				}],
				"text": "@OriginalPerson000 Third reply"
			},
			{
				"conversation_id": "1279944223114900000",
				"author_id": "3001960000",
				"created_at": "2020-07-06T01:04:17.000Z",
				"id": "1279944223114900000",
				"text": "This is the original post"
			}
		]
	},
	"meta": {
		"newest_id": "1280169177479744444",
		"oldest_id": "1279945722494811111",
		"result_count": 4
	}
}
```

### 
Retrieving conversation\_id as a tweet.fields parameter

To request the conversation\_id for all Tweets returned on a v2 endpoint, the tweet.fields=conversation\_id field can be added to the request parameters.  The conversation\_id field is always the Tweet ID of the original Tweet in the conversation reply thread.  All Tweets within the same reply thread, including reply threads that are created from earlier reply threads, will show the same conversation\_id.  

#### Request with conversation\_id parameter

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets?ids=1225917697675886593&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username' \
  --header 'Authorization: Bearer $ACCESS_TOKEN' 
```

Code copied to clipboard

#### 
Response

```
      {
    "data": [
        {
            "id": "1225917697675886593",
            "text": "@TwitterEng *ahem* https://t.co/aroJHt2zQ1",
            "created_at": "2020-02-07T23:02:10.000Z",
            "author_id": "2244994945",
            "in_reply_to_user_id": "6844292",
            "conversation_id": "1225912275971657728",
            "referenced_tweets": [
                {
                    "type": "quoted",
                    "id": "1200517737669378053"
                },
                {
                    "type": "replied_to",
                    "id": "1225912275971657728"
                }
            ]
        }
    ],
    "includes": {
        "users": [
            {
                "username": "TwitterDev",
                "name": "Twitter Dev",
                "id": "2244994945"
            },
            {
                "username": "TwitterEng",
                "name": "Twitter Engineering",
                "id": "6844292"
            }
        ],
        "tweets": [
            {
                "id": "1200517737669378053",
                "text": "|￣￣￣￣￣￣￣￣￣￣￣|\n             don't push            \n             to prod on            \n               Fridays                  \n|＿＿＿＿＿＿＿＿＿＿＿| \n(\\__/)  ||\n(•ㅅ•) ||\n/ 　 づ",
                "created_at": "2019-11-29T20:51:47.000Z",
                "author_id": "2244994945",
                "conversation_id": "1200517737669378053"
            },
            {
                "id": "1225912275971657728",
                "text": "Note to self: Don't deploy on Fridays",
                "created_at": "2020-02-07T22:40:37.000Z",
                "author_id": "6844292",
                "conversation_id": "1225912275971657728"
            }
        ]
    }
}
```

### 
Using conversation\_id as a filter operator

The conversation\_id can be used as a search query parameter when using either recent search or as an operator within a rule for filtered stream.  Using the operator on its own will result in the entire conversation thread of Tweets being returned in either real time through filtered stream, or paginated in reverse chronological order from search Tweets. You can also receive a count of the Tweets in a conversation using this operator with Tweet counts.

Additional operators can be added to the query/rule, in conjunction with the conversation\_id operator, however these will apply only to the Tweets that are part of that conversation.  Only one conversation\_id can be specified at a time without an OR clause within the query/rule.

Reconstructing the conversation can be done by ordering the Tweets with a matching conversation\_id by timestamp, and taking note of which Tweets are directly in reply to other Tweets in the conversation thread. This can be accomplished by also requesting the in\_reply\_to\_user\_id field and referenced\_tweets.id and in\_reply\_to\_user\_id expansions.

Request to query by conversation\_id  

#### 

```
      curl --request GET \
  --url 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1279940000004973111&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id' \
  --header 'Authorization: Bearer $ACCESS_TOKEN' 
```

Code copied to clipboard

#### 
Response

***Note**: Results for search Tweets are in reverse chronological order.*

```
      {
	"data": [{
			"id": "1280169000000704333",
			"text": "@attributeisland @iterationjoe What beautiful creatures! Happy #seaturtleweek",
			"conversation_id": "1279940000004973111",
			"public_metrics": {
				"retweet_count": 0,
				"reply_count": 0,
				"like_count": 7,
				"quote_count": 0
			}
		},
		{
			"id": "1280166000000519222",
			"text": "@attributeisland \"One touch of nature makes the whole world kin.\" -John Muir",
			"conversation_id": "1279940000004973111",
			"public_metrics": {
				"retweet_count": 0,
				"reply_count": 1,
				"like_count": 1,
				"quote_count": 0
			}
		},
		{
			"id": "1280166000000519221",
			"text": "@attributeisland I love turtles!",
			"conversation_id": "1279940000004973111",
			"public_metrics": {
				"retweet_count": 1,
				"reply_count": 0,
				"like_count": 4,
				"quote_count": 0
			}
		},
		{
			"id": "1280166000000519220",
			"text": "@attributeisland Turtlemoji🐢",
			"conversation_id": "1279940000004973111",
			"public_metrics": {
				"retweet_count": 0,
				"reply_count": 0,
				"like_count": 1,
				"quote_count": 0
			}
		},
		{
			"id": "1279940000004973111",
			"text": "Sea turtles are roaming in our waters!",
			"conversation_id": "1279940000004973111",
			"public_metrics": {
				"retweet_count": 67,
				"reply_count": 11,
				"like_count": 396,
				"quote_count": 2
			}
		}
	],
	"meta": {
		"newest_id": "1280169000000704333",
		"oldest_id": "1279940000004973111",
		"result_count": 5
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