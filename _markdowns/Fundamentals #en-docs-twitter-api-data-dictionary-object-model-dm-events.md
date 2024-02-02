



Direct Message events | Docs | Twitter Developer Platform 





































































































Direct Message events



Direct Message events
=====================


Direct Message (DM) conversations are made up of events. The Twitter API v2 currently supports three event types: MessageCreate, ParticipantsJoin, and ParticipantsLeave.


DM event objects are returned by the Direct Message lookup endpoints, and a MessageCreate event is created when Direct Messages are successfully created with the Manage Direct Messages endpoints.


When requesting DM events, there are three default event object attributes, or fields, included: id, event\_type, and text. To receive additional event fields, use the fields parameter dm\_event.fields to select others. Other available event fields include the following: dm\_conversation\_id, created\_at, sender\_id, attachments, participant\_ids, and referenced\_tweets.


Several of these fields provide the IDs of other Twitter objects related to the Direct Message event:


* sender\_id - The ID of the account that sent the message, or who invited a participant to a group conversation
* partricipants\_ids - An array of account IDs. For ParticipantsJoin and ParticipantsLeave events this array will contain a single ID of the account that created the event
* attachments - Provides media IDs for content that has been uploaded to Twitter by the sender
* referenced\_tweets - If a Tweet URL is found in the text field, the ID of that Tweet is included in the response


The sender\_id, participant\_ids, referenced\_tweets.id, and attachments.media\_keys expansions are available to expand on these Twitter object IDs.








|  |  |  |  |
| --- | --- | --- | --- |
| **Field value** | **Type** | **Description** | **How it can be used** |
| id (default) | string | The unique identifier of the event.
"id": "1050118621198921728" | Use this to programmatically retrieve a specific conversation event (available with v1.1 endpoints). |
| event\_type (default) | string | Describes the type of event. Three types are currently supported: * MessageCreate
* ParticipantsJoin
* ParticipantsLeave

"event\_type": "MessageCreate" | When retrieving a conversation's history, understanding when messages were created, and for group conversations, understanding when participants joined and left. All GET methods support filtering on specific event types with the event\_type= query parameter. . |
| text (default) |  string | The actual UTF-8 text of the Direct Message. 
"text": "Hello, just you!" | With chatbots, this can be used to analyze message contents and determining automated responses. Could be used to build conversation search features.  |
| sender\_id | string | ID of the User creating the event. To expand this object in the response, include sender\_id as an expansion  and use the user.fields query parameter to specify User object attributes of interest.
"sender\_id": "906948460078698496" | Retrieve the User object of who created the MessageCreate or ParticipantsJoin event. |
| participant\_id | array (of strings) | IDs of the participants joining and leaving a group conversation. Also used when creating new group conversations. To expand this object in the response, include participant\_ids as an expansion and use the user.fields query parameter to specify User object attributes of interest.
"participant\_ids": [
     "906948460078698496"
] | Used to retrieve User objects for participants joining and leaving group conversations. |
| dm\_conversation\_id | string | The unique identifier of the conversation the event is apart of.
"dm\_conversation\_id": "1584988213961031680" | Use this to programmatically retrieve events from a conversation, and add Direct Messages to it. |
| created\_at | date (ISO 8601) | Creation time (UTC) of the Tweet.
"created\_at": "2019-06-04T23:12:08.000Z" | This field can be used to understand when a Direct Message was created or when conversation participants joined or left. |
| referenced\_tweets | array | ID for any Tweet mentioned in the Direct Message text. To expand this object in the response, include referenced\_tweets.id as an expansion and use the tweet.fields query parameter to specify Tweet object attributes of interest.
"referenced\_tweets": [
    {
        "id": "1578868150510456833"
    }
] | When Direct Messages reference a Tweet, these IDs can be used to lookup the Tweet's details. |
| attachments | object | For Direct Messages with attached Media, provides the media key of the uploaded content (photo, video, or GIF. To expand this object in the response, include attachments.media\_keys as an expansion and use the media.fields query parameter to specify media object attributes of interest. Currently, one attachment is supported. 
"attachments": {
    "media\_keys": [
        "3\_1136048009270239232"
    ]
} | Understanding the media objects attached to Direct Messages. |






Retrieving a Direct Message event object
----------------------------------------


### Sample Request


For this example, we will build a request that retrieves events associated with a one-to-one conversation. This request will return fundamental Direct Message event fields, along with additional fields for referenced Tweets and their authors. Let's build a query that asks for:


* Fundamental event attributes such as when it was created and what conversation it is part of (dm\_conversation).
* The account ID and description of who sent the Direct Message.
* The text of any referenced Tweet, and when it was posted.
* The account ID and description of any referenced Tweet author.


To return those attributes, your request query would include the following:












```

      ?dm_event.fields=id,sender_id,text,created_at,dm_conversation_id&expansions=sender_id,referenced_tweets.id&tweet.fields=created_at,text,author_id&user.fields=description
    
```





Code copied to clipboard














```

      curl --request GET 'https://api.twitter.com/2/dm_conversations/with/:participant_id/dm_events?tweet.fields=created_at,text,author_id&user.fields=description&expansions=sender_id,participant_ids,referenced_tweets.id&dm_event.fields=id,sender_id,text,participant_ids,created_at,' 
    --header 'Authorization: Bearer $BEARER_TOKEN'
    
```





Code copied to clipboard








Be sure to replace $BEARER\_TOKEN with your own generated Bearer Token.


### Sample Response












```

      {
	"data": [{
			"id": "1585047616894574596",
			"sender_id": "944480690",
			"text": "Hello, just you!",
			"created_at": "2022-10-25T23:16:15.000Z",
			"event_type": "MessageCreate",
			"dm_conversation_id": "944480690-906948460078698496"
		},
		{
			"id": "1581048670673260549",
			"sender_id": "944480690",
			"text": "Simple Tweet link: https://t.co/IYFbRIdXHg",
			"referenced_tweets": [{
				"id": "1578900353814519810"
			}],
			"created_at": "2022-10-14T22:25:52.000Z",
			"event_type": "MessageCreate",
			"dm_conversation_id": "944480690-906948460078698496"
		},
		{
			"id": "1580705121553420292",
			"sender_id": "944480690",
			"text": "Adding a new 1-to-1 Direct Message.",
			"created_at": "2022-10-13T23:40:43.000Z",
			"event_type": "MessageCreate",
			"dm_conversation_id": "944480690-906948460078698496"
		}
	],
	"includes": {
		"users": [{
				"name": "API Demos",
				"description": "Hosting TwitterDev integrations... @TwitterDev #DevRel",
				"id": "944480690",
				"username": "FloodSocial"
			},
			{
				"name": "the SnowBot",
				"description": "Home of the @TwitterDev SnowBot... Serving snow reports, snow photos, and snow research links... Chatbot is currently being remodeled for Twitter APIv2.",
				"id": "906948460078698496",
				"username": "SnowBotDev"
			}
		],
		"tweets": [{
				"text": "Feeling kind of bad that I didn’t wish everybody a happy new Colorado Water Year…\n\nHappy Water Year to all my Colorado friends and colleagues, new and old… \n\nMay this be a generous water year, although not too generous…",
				"id": "1578900353814519810",
				"created_at": "2022-10-09T00:09:13.000Z",
				"author_id": "944480690",
				"edit_history_tweet_ids": [
					"1578900353814519810"
				]
			}
		]
	},
	"meta": {
		"result_count": 3,
		"next_token": "18LAA581J5II7LA00C00ZZZZ",
		"previous_token": "1BLC45G1H8CAL5DG0G00ZZZZ"
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















