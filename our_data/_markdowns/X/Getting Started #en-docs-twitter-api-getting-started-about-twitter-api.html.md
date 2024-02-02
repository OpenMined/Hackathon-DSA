
Getting Started with the Twitter API | Docs | Twitter Developer Platform 

About the Twitter API

About the Twitter API
---------------------

The Twitter API can be used to programmatically retrieve and analyze Twitter data, as well as build for the conversation on Twitter.

Over the years, the Twitter API has grown by adding additional levels of access for developers and academic researchers to be able to scale their access to enhance and research the public conversation. 

Recently, we released the Twitter API v2. The Twitter API v2 includes a modern foundation, new and advanced features, and quick onboarding to Basic access.   

The following three tabs explain the different versions and access levels of the Twitter API, what’s new with v2, and which Twitter resources you can retrieve, create, destroy, and adjust using the API.   

* Access levels and versions
* What's new with v2
* Twitter API resources

 Access levels and versions

 What's new with v2

 Twitter API resources

Twitter API access levels and versions
--------------------------------------

While the Twitter API v2 is the primary Twitter API, the platform currently supports previous versions (v1.1, Gnip 2.0) as well. We recommend that all users start with v2 as this is where all future innovation will happen. 

The Twitter API v2 includes a few access levels to help you scale your usage on the platform. In general, new accounts can quickly sign up for Basic access. Should you want additional access, you may choose to apply for Enterprise access.   

|  | **Free** | **Basic** | **Pro** | **Enterprise** |
| **Getting access** | Get Started | Get Started | Get Started | Get Started |
| **Price** | Free | $100/month | $5000/month |
| **Access to Twitter API v2** | ✔️ (Only Tweet creation) | ✔️ | ✔️ |
| **Access to standard v1.1** | ✔️(Only Media Upload, Help, Rate Limit, and Login with Twitter) | ✔️(Only Media Upload, Help, Rate Limit, and Login with Twitter) | ✔️(Only Media Upload, Help, Rate Limit, and Login with Twitter) |
| **Project limits** | 1 Project | 1 Project | 1 Project |
| **App limits** | 1 App per Project | 2 Apps per Project | 3 Apps per Project |
| **Tweet caps - Post** | 1,500 | 3,000 | 300,000 |
| **Tweet caps - Pull** | ❌ | 10,000 | 1,000,000 |
| **Filteres stream API** | ❌ | ❌ | ✔️ |
| **Access to full-archive search** | ❌ | ❌ | ✔️ |
| **Access to Ads API** | ✔️ | ✔️ | ✔️ |

Other Twitter API offerings
---------------------------

### Enterprise APIs (Formerly Gnip 2.0)

Enterprise-level products that provide access to Twitter’s data, including Full Archive and 30 Day Search API, PowerTrack API, Historical PowerTrack API, Decahose API, Engagement API, and much more!

Learn more

### Standard v1.1

The standard v1.1 endpoints were launched in 2012 and enable you to post, interact, and retrieve data for resources such as Tweets, Users, Direct Messages, Lists, Trends, Media, and Places.

Learn more

### Migrate to Twitter API v2

Interested in migrating your current integration to Twitter API v2? Check out our migration hub for resources that will help you understand what is different between v2 and previous versions, including the data formats. You can also access migration guides for each endpoint listed in the new v2 endpoint sections.

Learn more

Twitter API endpoint map

What's new with v2
------------------

The Twitter API v2 represents the largest upgrade of the Twitter API since 2012. With it comes a host of new and advanced features, as well as fast and free access to the API. 

Some of the features that are available with v2 include the following:  

### New endpoints

We have released a set of net-new endpoints to Twitter API v2. You can see a full list of v2 endpoints, including those that are new, on our Twitter API endpoint map guide.

Visit the Twitter API endpoint map >

### 
New and more detailed data objects

We've modernized our data objects with a variety off new improvements that will enable you to more easily navigate and parse data.

Visit the data dictionary >  

### New parameters to help you retrieve just those objects and fields that you want

We’ve added fields and expansions parameters to our data endpoints that allow you to request related objects and fields beyond those fields that return by default.

Learn how to use fields and expansions >  

### Advanced metrics

More easily understand the performance of Tweets, users, media, and polls from directly within your payload by requesting both public and private metrics including impressions, video views, user profile, and URL clicks, some of which are separated into an organic and promoted context.

Learn more about metrics >  

### Filter on and identify which Tweets contain different topics

When using search Tweets or filtered stream, you can now filter by topic using our entity and context operators. We’ve also provided these topics within the Tweet payload to help with analysis. 

Learn more about Tweet annotations >  

### FIlter on and identify which Tweets belong to a reply thread

Make it easier to identify a Tweet as part of a conversation thread when using search Tweets, filtered stream, and Tweet lookup. We've also added the ability to determine whether conversation reply settings have been set for a Tweet with the Tweet field reply\_settings.

Learn more about conversation tracking >  

### And so much more...

* High confidence spam filtering
* Shortened URLs are fully unwound for easier URL analysis
* Simplified JSON response objects by removing deprecated fields and modernizing labels
* Recovery and redundancy functionality for our streaming endpoints
* Return of 100% of matching public and available Tweets in search queries
* Streaming "rules" so you can make changes without dropping connections
* More expressive query language for filtered stream and search
* OpenAPI spec to build new libraries & more transparently track changes
* API support for new features and endpoints more quickly as our platform evolves to meet the needs of developers, researchers, businesses, and people using Twitter

Twitter API platform resources
------------------------------

In the API design space, a resource is an entity with associated data, relationships to other resources, and a set of methods that operate on it. For example, a Tweet is a resource that you can create, delete, or retrieve using a variety of different tools, such as historically searching for them, or retrieving them in real-time. 

The Twitter API provides access to create, delete, receive, or adjust a variety of different resources on the platform including the following:

| Resource | Description |
| --- | --- |
| **Tweets** | Tap into millions of Tweets to understand the public conversation, or create your own to engage with the conversation.
Current availability:* Twitter API v2
* Enterprise
* Premium v1.1
* Standard v1.1
 |
| **Users** | Manage or look up Twitter users to analyze networks, understand your audience, or foster positive online relationships.
Current availability:* Twitter API v2
* Enterprise
* Premium v1.1
* Standard v1.1
 |
| **Spaces** | Look up and search Twitter Spaces and their attendees to help people find interesting and relevant audio conversations.
Current availability:* Twitter API v2
 |
| **Direct Messages** | Send and receive Direct Messages to triage customer issues, send welcome messages, or create positive human interaction.
Current availability:* Standard v1.1
 |
| **Lists** | Curate and manage lists of accounts to keep a pulse on industry experts, powerful voices, or organize who you follow.
Current availability:* Twitter API v2
* Standard v1.1
 |
| **Trends** | Identify geographic trends first to pinpoint industry movement, discover hot topics, or stay ahead of the latest fad.
Current availability:* Standard v1.1
 |
| **Media** | Upload media objects to share your creative energy, create interactive experiences, or build accessibility tools.
Current availability:* Standard v1.1
 |
| **Places** | Search for places to understand what’s happening in your neighborhood and around the world.
Current availability:* Standard v1.1
 |

Next steps
----------

You can sign up for the Twitter API, or review our Getting access to the Twitter API guide for more details.

We’ve also put together a guide describing how to make your first request to the Twitter API. 

If you have any feedback on these getting started resources, we’d love to hear from you!  
Please fill out the brief survey at the bottom of each page to help us improve. 

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