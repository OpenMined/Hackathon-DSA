Graph API Reference - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Graph API Reference
===================
### Graph API Root Nodes
This is a full list of the Graph API root nodes. The main difference between a root node and a non-root node is that root nodes can be queried directly, while non-root nodes can be queried via root nodes or edges. If you want to learn how to use the Graph API, read our Using Graph API guide, and if you want to know which APIs can solve some frequent issues, try our Common Scenarios guide.
| Node | Description |
| --- | --- |
| `Album` | Get Fields and Edges on an Album. |
| `App Link Host` | An individual app link host object created by an app |
| `Application` | A Facebook app |
| `CPASAdvertiser Partnership Recommendation` | Returns a recommendation of a single retailer for a specific brand. This endpoint returns a retailer-brand pair and an advertiser who can advertise on behalf of the producer.
This endpoint is mainly for Facebook’s Marketing Partners using Collaborative Ads. |
| `Canvas` | A canvas document |
| `Canvas Button` | A button inside the canvas |
| `Canvas Carousel` | A carousel inside a canvas |
| `Canvas Footer` | A footer of the canvas |
| `Canvas Header` | A header inside the canvas. |
| `Canvas Photo` | A photo inside a canvas |
| `Canvas Product List` | A product list inside the canvas |
| `Canvas Product Set` | A product set inside the canvas |
| `Canvas Text` | Text element of the canvas |
| `Canvas Video` | A video inside canvas |
| `Collaborative Ads Directory` | Directory of businesses that use collaborative ads |
| `Comment` | A comment can be made on various types of content on Facebook. Most Graph API nodes have a /comments edge that lists all the comments on that object. The /comment node returns a single comment. |
| `Commerce Merchant Settings` | Commerce Merchant Settings object |
| `Conversation` | Graph API Reference Conversation /conversation |
| `Event` | Get fields and edges on an Event. |
| `Games IAPProduct` | An in-app-purchaseable product |
| `Group` | A Facebook group. |
| `Group Doc` | Graph API Reference Group Doc /group-doc |
| `Group Message` | GroupMessage |
| `Image Copyright` | Represents a copyright on an image asset. |
| `Instagram Oembed` | InstagramOembed |
| `Link` | A link shared on a wall. |
| `Live Video` | Get fields and edges on a LiveVideo. |
| `Live Video Input Stream` | An ingest stream for a live video |
| `Mailing Address` | A mailing address object |
| `Media Fingerprint` | Media fingerprint |
| `Message` | An individual message in the Facebook messaging system. |
| `Milestone` | Graph API Reference Milestone /milestone |
| `Object Comments` | This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. |
| `Object Likes` | This reference describes the `/likes` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. |
| `Object Private Replies` | Private replies for an object |
| `Object Reactions` | First revision to publish |
| `Object Sharedposts` | Graph API Reference /object/sharedposts |
| `Oembed Page` | OembedPage |
| `Oembed Post` | OembedPost |
| `Oembed Video` | OembedVideo |
| `Offline Conversion Data Set Upload` | A subset of Offline Event Data Set |
| `Page` | Get groups a Page is a member of. |
| `Page Call To Action` | Page's call-to-action |
| `Page Post` | A Facebook Feed story |
| `Page Upcoming Change` | Notification of page upcoming changes. |
| `Page/insights` | This object represents a single Insights metric that is tied to another particular Graph API object (Page, App, Post, etc.). |
| `Payment` | Graph API Reference Payment /payment |
| `Photo` | This represents a Photo on Facebook. |
| `Place` | A place |
| `Place Topic` | The category of a place Page |
| `Post` | A Facebook Feed story |
| `Profile` | Graph API Reference Profile /profile |
| `Request` | Graph API Reference Request /request |
| `Test User` | Graph API Reference Test User /test-user |
| `Thread` | Graph API Reference Thread /thread |
| `User` | Get fields and edges on a User. |
| `Video` | A Video |
| `Video Copyright` | A video copyright |
| `Video List` | A playlist for videos |
| `Video Poll` | Embedded video poll |
| `Video Poll Option` | Represents a single poll option that may be selected by the user |
| `Whats App Business Account` | Returns the account information of a WhatsApp Business Account |
| `Whats App Business HSM` | Retrieves information about the message template |
### Graph API Root Edges
Root edges are edges that can be queried directly. They allow you to access collections of nodes that are not on a parent node.
| Node | Description |
| --- | --- |
| `Ads Archive` | Returns archived ads based on your search. |
| `Branded Content Search` | Returns branded content based on your search. By default we only return content that is currently available on Facebook or Instagram, and content that was created on or after August 17, 2023. |
| `Debug Token` | Metadata about a particular access token |