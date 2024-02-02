Graph API Reference
===================

### Graph API Root Nodes

This is a full list of the Graph API root nodes. The main difference between a root node and a non-root node is that root nodes can be queried directly, while non-root nodes can be queried via root nodes or edges. If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/), and if you want to know which APIs can solve some frequent issues, try our [Common Scenarios guide](https://developers.facebook.com/docs/graph-api/common-scenarios/).

| Node | Description |
| --- | --- |
| [`Album`](https://developers.facebook.com/docs/graph-api/reference/album) | Get [Fields](#fields) and [Edges](#edges) on an Album. |
| [`App Link Host`](https://developers.facebook.com/docs/graph-api/reference/app-link-host) | An individual app link host object created by an app |
| [`Application`](https://developers.facebook.com/docs/graph-api/reference/application) | A Facebook app |
| [`CPASAdvertiser Partnership Recommendation`](https://developers.facebook.com/docs/graph-api/reference/cpas-advertiser-partnership-recommendation) | Returns a recommendation of a single retailer for a specific brand. This endpoint returns a retailer-brand pair and an advertiser who can advertise on behalf of the producer.<br><br>This endpoint is mainly for Facebook’s Marketing Partners using [Collaborative Ads](https://developers.facebook.com/docs/marketing-api/collaborative-ads). |
| [`Canvas`](https://developers.facebook.com/docs/graph-api/reference/canvas) | A canvas document |
| [`Canvas Button`](https://developers.facebook.com/docs/graph-api/reference/canvas-button) | A button inside the canvas |
| [`Canvas Carousel`](https://developers.facebook.com/docs/graph-api/reference/canvas-carousel) | A carousel inside a canvas |
| [`Canvas Footer`](https://developers.facebook.com/docs/graph-api/reference/canvas-footer) | A footer of the canvas |
| [`Canvas Header`](https://developers.facebook.com/docs/graph-api/reference/canvas-header) | A header inside the canvas. |
| [`Canvas Photo`](https://developers.facebook.com/docs/graph-api/reference/canvas-photo) | A photo inside a canvas |
| [`Canvas Product List`](https://developers.facebook.com/docs/graph-api/reference/canvas-product-list) | A product list inside the canvas |
| [`Canvas Product Set`](https://developers.facebook.com/docs/graph-api/reference/canvas-product-set) | A product set inside the canvas |
| [`Canvas Text`](https://developers.facebook.com/docs/graph-api/reference/canvas-text) | Text element of the canvas |
| [`Canvas Video`](https://developers.facebook.com/docs/graph-api/reference/canvas-video) | A video inside canvas |
| [`Collaborative Ads Directory`](https://developers.facebook.com/docs/graph-api/reference/collaborative-ads-directory) | Directory of businesses that use collaborative ads |
| [`Comment`](https://developers.facebook.com/docs/graph-api/reference/comment) | A comment can be made on various types of content on Facebook. Most Graph API nodes have a /comments edge that lists all the comments on that object. The /comment node returns a single comment. |
| [`Commerce Merchant Settings`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings) | Commerce Merchant Settings object |
| [`Conversation`](https://developers.facebook.com/docs/graph-api/reference/conversation) | Graph API Reference Conversation /conversation |
| [`Event`](https://developers.facebook.com/docs/graph-api/reference/event) | Get fields and edges on an Event. |
| [`Games IAPProduct`](https://developers.facebook.com/docs/graph-api/reference/games-iap-product) | An in-app-purchaseable product |
| [`Group`](https://developers.facebook.com/docs/graph-api/reference/group) | A Facebook group. |
| [`Group Doc`](https://developers.facebook.com/docs/graph-api/reference/groupdoc) | Graph API Reference Group Doc /group-doc |
| [`Group Message`](https://developers.facebook.com/docs/graph-api/reference/group-message) | GroupMessage |
| [`Image Copyright`](https://developers.facebook.com/docs/graph-api/reference/image-copyright) | Represents a copyright on an image asset. |
| [`Instagram Oembed`](https://developers.facebook.com/docs/graph-api/reference/instagram-oembed) | InstagramOembed |
| [`Link`](https://developers.facebook.com/docs/graph-api/reference/link) | A link shared on a wall. |
| [`Live Video`](https://developers.facebook.com/docs/graph-api/reference/live-video) | Get fields and edges on a LiveVideo. |
| [`Live Video Input Stream`](https://developers.facebook.com/docs/graph-api/reference/live-video-input-stream) | An ingest stream for a live video |
| [`Mailing Address`](https://developers.facebook.com/docs/graph-api/reference/mailing-address) | A mailing address object |
| [`Media Fingerprint`](https://developers.facebook.com/docs/graph-api/reference/media-fingerprint) | Media fingerprint |
| [`Message`](https://developers.facebook.com/docs/graph-api/reference/message) | An individual message in the Facebook messaging system. |
| [`Milestone`](https://developers.facebook.com/docs/graph-api/reference/milestone) | Graph API Reference Milestone /milestone |
| [`Object Comments`](https://developers.facebook.com/docs/graph-api/reference/object/comments) | This reference describes the `/comments` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. |
| [`Object Likes`](https://developers.facebook.com/docs/graph-api/reference/object/likes) | This reference describes the `/likes` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. |
| [`Object Private Replies`](https://developers.facebook.com/docs/graph-api/reference/object/private_replies) | Private replies for an object |
| [`Object Reactions`](https://developers.facebook.com/docs/graph-api/reference/object/reactions) | First revision to publish |
| [`Object Sharedposts`](https://developers.facebook.com/docs/graph-api/reference/object/sharedposts) | Graph API Reference /object/sharedposts |
| [`Oembed Page`](https://developers.facebook.com/docs/graph-api/reference/oembed-page) | OembedPage |
| [`Oembed Post`](https://developers.facebook.com/docs/graph-api/reference/oembed-post) | OembedPost |
| [`Oembed Video`](https://developers.facebook.com/docs/graph-api/reference/oembed-video) | OembedVideo |
| [`Offline Conversion Data Set Upload`](https://developers.facebook.com/docs/graph-api/reference/offline-conversion-data-set-upload) | A subset of Offline Event Data Set |
| [`Page`](https://developers.facebook.com/docs/graph-api/reference/page) | Get groups a Page is a member of. |
| [`Page Call To Action`](https://developers.facebook.com/docs/graph-api/reference/page-call-to-action) | Page's call-to-action |
| [`Page Post`](https://developers.facebook.com/docs/graph-api/reference/page-post) | A Facebook Feed story |
| [`Page Upcoming Change`](https://developers.facebook.com/docs/graph-api/reference/page-upcoming-change) | Notification of page upcoming changes. |
| [`Page/insights`](https://developers.facebook.com/docs/graph-api/reference/insights) | This object represents a single Insights metric that is tied to another particular Graph API object (Page, App, Post, etc.). |
| [`Payment`](https://developers.facebook.com/docs/graph-api/reference/payment) | Graph API Reference Payment /payment |
| [`Photo`](https://developers.facebook.com/docs/graph-api/reference/photo) | This represents a Photo on Facebook. |
| [`Place`](https://developers.facebook.com/docs/graph-api/reference/place) | A place |
| [`Place Topic`](https://developers.facebook.com/docs/graph-api/reference/place-topic) | The category of a place Page |
| [`Post`](https://developers.facebook.com/docs/graph-api/reference/post) | A Facebook Feed story |
| [`Profile`](https://developers.facebook.com/docs/graph-api/reference/profile) | Graph API Reference Profile /profile |
| [`Request`](https://developers.facebook.com/docs/graph-api/reference/request) | Graph API Reference Request /request |
| [`Test User`](https://developers.facebook.com/docs/graph-api/reference/test-user) | Graph API Reference Test User /test-user |
| [`Thread`](https://developers.facebook.com/docs/graph-api/reference/thread) | Graph API Reference Thread /thread |
| [`User`](https://developers.facebook.com/docs/graph-api/reference/user) | Get fields and edges on a User. |
| [`Video`](https://developers.facebook.com/docs/graph-api/reference/video) | A Video |
| [`Video Copyright`](https://developers.facebook.com/docs/graph-api/reference/video-copyright) | A video copyright |
| [`Video List`](https://developers.facebook.com/docs/graph-api/reference/video-list) | A playlist for videos |
| [`Video Poll`](https://developers.facebook.com/docs/graph-api/reference/video-poll) | Embedded video poll |
| [`Video Poll Option`](https://developers.facebook.com/docs/graph-api/reference/video-poll-option) | Represents a single poll option that may be selected by the user |
| [`Whats App Business Account`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-account) | Returns the account information of a WhatsApp Business Account |
| [`Whats App Business HSM`](https://developers.facebook.com/docs/graph-api/reference/whats-app-business-hsm) | Retrieves information about the message template |

### Graph API Root Edges

Root edges are edges that can be queried directly. They allow you to access collections of nodes that are not on a parent node.

| Node | Description |
| --- | --- |
| [`Ads Archive`](https://developers.facebook.com/docs/graph-api/reference/ads_archive/) | Returns archived ads based on your search. |
| [`Branded Content Search`](https://developers.facebook.com/docs/graph-api/reference/branded_content_search/) | Returns branded content based on your search. By default we only return content that is currently available on Facebook or Instagram, and content that was created on or after August 17, 2023. |
| [`Debug Token`](https://developers.facebook.com/docs/graph-api/reference/debug_token/) | Metadata about a particular access token |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)