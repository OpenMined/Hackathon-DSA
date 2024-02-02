



Integrate | Docs | Twitter Developer Platform 





































































































Integrate



Integration guide
-----------------


The Direct Messages endpoints v2 introduce conversations and conversation events as core Twitter API objects, and make a distinction between 1-1 and group conversations. 1-1 conversations always have two, and only two, participants, while group conversations can have two or more and memberships that can change.   


This page contains information on several tools and key concepts that you should be aware of as you integrate the Direct Messages lookup endpoints into your system. We’ve broken the page into two sections:


* Key Concepts
	+ Direct Message conversations
	+ Shared conversation and event IDs across v1.1 and v2
	+ Direct Message event fields and expansions
	+ Conversation event types
	+ Authentication
	+ Developer portal, Projects, and Apps
	+ Rate limits
	+ Pagination
* Helpful tools


 


### Key Concepts


### Direct Message conversations


All Direct Messages are part of a Direct Message conversation. These conversations can be one-to-one conversations or group conversations. This launch provides the foundational endpoints needed to create Direct Messages and retrieve events associated with Direct Message conversations. All conversations have a unique dm\_conversation\_id, and the events that make up that conversation all have a unique dm\_event\_id.  


The Direct Message lookup endpoints provide methods for retrieving events associated with conversations. These GET endpoints are used to retrieve the messages that make up a conversation, and for group conversations, can be used to understand who has joined and left group conversations.  




This initial release of Direct Messages lookup includes three GET methods:


* **GET /2/dm\_conversations/with/:participant\_id/dm\_events** - Retrieves Direct Message events associated with a one-to-one conversation. The :participant\_id path parameter is the numeric User ID of the account having the conversation with the authenticated user making this request.
* **GET /2/dm\_conversations/:dm\_conversation\_id/dm\_events** - Retrieves Direct Message events associated with a specific conversation ID, as indicated by the :dm\_conversation\_id path parameter. Both one-to-one and group conversations IDs are supported.
* **GET /2/dm\_events** - Retrieves Direct Message events associated with the authenticating user, including both one-to-one and group conversations. Events from up to 30 days ago are available.


These GET endpoints all support retrieving dm\_events by event type with an event\_types request query parameters. Currently, there are three conversation event types supported:  




* **MessageCreate** - Created when a new Direct Message is created. This event object can include the time and text of the message, along with the account ID of who sent the message, and the conversation and event IDs.
* **ParticipantsJoin** - Created when a new participant joins a group conversation. This dm\_event object includes the ID of the participant joining, along with the created\_at time and the sender\_id of the 'invite' event.
* **ParticipantsLeave** - Created when a participant leaves a conversation.This event object includes the ID of the participant leaving, along with the time of the event.


For more information see the Direct Messages lookup API References.


### Shared conversation and event IDs across v1.1 and v2


An important concept is that conversation and event IDs are shared across v1.1 and v2 versions of the Twitter Platform. This means both versions can be used together. For example, the Direct Messages v1.1 endpoints provide methods for returning a single event and for deleting events, methods not yet available with v2. Since IDs are common across v1.1 and v2, you can make v1.1 requests based on IDs provided by v2, or by referencing conversation IDs displayed in conversation URLs on the Twitter application.  


### Direct Message event fields and expansions


The Twitter API v2 allows users to select exactly which data they want to return from the API using a set of tools called fields and expansions. For example, Direct Message lookup endpoints support the following dm\_events fields: 


* id, event\_type, and text are the defaults for MessageCreate events.
* id, event\_type, and participant\_ids are the defaults for ParticipantsJoin and ParticipantsLeave events.
* dm\_conversation\_id and created\_at are available for all events.
* attachments and referenced\_tweets are available for MessageCreate events.
* sender\_id is available for MessageCreate and ParticipantsJoin events.
* participant\_ids is available for ParticipantsJoin and ParticipantsLeave events.


In addition, the Direct Message lookup endpoints support the following expansions:  




* sender\_id - Expands the User object associated with who sent the message or who invited someone to the conversation.
* referenced\_tweets.id - Expands the Tweet object if the Direct Message text includes a link to a Tweet.
* attachments.media\_keys - Expands the Media object if the Direct Message includes a media attachment.
* participant\_ids - Expands the User object associated with who joined or left a group conversation.


Since expansion include Tweets, Users, and Media objects, you can also use the tweet.fields, user.fields, and media.fields request query parameters. See our guide on how to use fields and expansions for more information.  




### Conversation event types


Below are example JSON objects for Direct Message the MessageCreate, ParticipantsJoin, and ParticipantsLeave event types.   




Available dm\_event object fields: id, text, event\_type, dm\_conversation\_id, created\_at, sender\_id, attachments, referenced\_tweets, participant\_ids. See the the Fields and Expansion section for more details on selecting these fields in your requests.   




Example MessageCreate event: 


With all the dm\_event fields specified, here is the response for a simple text Direct Message: 












```

      {
    "text": "Hi everyone.",
    "sender_id": "944480690",
    "dm_conversation_id": "1578398451921985538",
    "id": "1582838499983564806",
    "event_type": "MessageCreate",
    "created_at": "2022-10-19T20:58:00.000Z"
}
    
```





Code copied to clipboard








Example ParticipantsJoin event:


With all the dm\_event fields specified, here is the response for a participant joining a conversation:












```

      {
    "participant_ids": [
        "944480690"
    ],
    "sender_id": "17200003",
    "dm_conversation_id": "1578398451921985538",
    "id": "1582835469712138240",
    "event_type": "ParticipantsJoin",
    "created_at": "2022-10-19T20:45:58.000Z"
}

    
```





Code copied to clipboard








Example ParticipantsLeave event:


With all the dm\_event fields specified, here is the response for a participant leaving a conversation:












```

      {
    "participant_ids": [
        "944480690"
    ],
    "dm_conversation_id": "1578398451921985538",
    "id": "1582838535115067392",
    "event_type": "ParticipantsLeave",
    "created_at": "2022-10-19T20:58:09.000Z"
    }
    
```





Code copied to clipboard








### Authentication


All Twitter API v2 endpoints require for you to authenticate your requests with a set of credentials, also known as keys and tokens. All Direct Messages are private and require user authorization to access them. 


These Direct Message endpoints require the use of OAuth 2.0 Authorization Flow with PKCE or 1.0a User Context, which means that you must use a set of API keys and user Access Tokens to make a successful request. The Access Tokens must be associated with the user that you are requesting on behalf of. If you want to generate a set of Access Tokens for another user, they must authorize or authenticate your App using the 3-legged OAuth flow.


Please note that OAuth user-context can be tricky to use. If you are not familiar with this authentication method, we recommend using a library or a tool like Postman to properly authenticate your requests. 


OAuth 2.0 Authorization Code with PKCE allows for greater control over an application’s scope, and authorization flows across multiple devices. OAuth 2.0 allows you to pick specific fine-grained scopes which give you specific permissions on behalf of a user. The Direct Messages lookup endpoints require these scopes:  dm.read, tweet.read, user.read


To enable OAuth 2.0 in your App, you must enable it in your’s App’s authentication settings found in the App settings section of the developer portal.


### Developer portal, Projects, and developer Apps


To retrieve a set of authentication credentials that will work with the Twitter API v2 endpoints, you must have an approved developer account, set up a Project within that account, and create a developer App within that Project. You can then find your keys and tokens within your developer App. 


### Rate limits


Everyday many thousands of developers make requests to the Twitter API. To help manage the sheer volume of these requests, rate limits are placed on each endpoint that limits the number of requests that you can make on behalf of your app or on behalf of an authenticated user. 


The Direct Message lookup endpoints are rate limited at the user-level, meaning that the authenticated user that you are making the request on behalf of can only make a certain number of requests with your Twitter App. There is a user rate limit of 300 requests per 15 minutes for the GET methods. These rate limits are shared across the GET endpoints.   




### Pagination


These endpoints utilize pagination so that responses are returned quickly. In cases where there are more results than what can be sent in a single response (up to 100 events) you will need to paginate. Use the max\_results parameter to identify how many results will return per page, and the pagination\_token parameter to return the next page of results. You can learn more by reviewing our pagination guide.  




Helpful tools
-------------


Here are some helpful tools we encourage you to explore as you work with the Direct Messages lookup endpoints: 


****Postman****


Postman is a great tool that you can use to test out an endpoint. Each Postman request includes every path and body parameter to help you quickly understand what is available to you. To learn more about our Postman collections, please visit our Using Postman page. 


****Code samples****


Python sample code for the v2 Direct Messages endpoints is available in our Twitter API v2 sample code GitHub repository. The "Manage-Direct-Messages" folder contains examples for the POST methods, and the "Direct-Messages-lookup" folder contains examples for the GET methods.


****TwitterDev Software Development Kits (SDKs)****


These libraries are being updated for the v2 Direct Messages endpoints and should be ready soon:  




* Twitter API Java SDK - Official Java SDK for the Twitter API v2
* Twitter API TypeScript/JavaScript SDK - Official TS/JS SDK for the Twitter API v2


**Third-party libraries**  




There is a growing number of third-party libraries developed by our community. These libraries are designed to help you get started, and several are expected to support v2 Direct Messages endpoints soon. You can find a library that works with the v2 endpoints by looking for the proper version tag.










Next steps
----------






Visit the API reference page for this endpoint



















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















