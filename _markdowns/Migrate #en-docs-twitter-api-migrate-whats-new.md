::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The X API v2 is now the primary X API, and is where product investment
and innovation are focused. We've partnered with developers to build the
next generation of the X API to better serve our diverse community of
developers. Based on developer feedback, we've re-built the API to
better serve a broader collection of needs, introduced new features and
endpoints, and improved upon the developer experience.\

The X API v2 is now the primary X API, and is where product investment
and innovation are focused. Over the past few years, we partnered with
developers and re-built the API to better serve a broader collection of
needs, introduce new features and endpoints, and improve upon the
developer experience. We are committed to continuing to build an open
developer platform, and are excited to see what you build with the X API
v2.

## Why migrate?

The X API v2 is built with a modern and more sustainable foundation and
includes both improved replacement endpoints for the standard v1.1, and
enterprise products, but also net-new functionality. We strongly
encourage customers of legacy APIs (v1.1, and enterprise) to begin to
migrate to v2 as we do intend to deprecate them eventually. Use the X
API to listen to and analyze the public conversation, engage with people
on X, and innovate.

In this section, we will discuss the endpoints and functionality.
:::
:::

::: c01-rich-text-editor
::: is-table-default
You can see a full list of v2 endpoints and their pre-v2 equivalent via
the following guide:
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
While most of the endpoints in X API v2 are replacements, we have
introduced several new endpoints. Here are several examples of new
endpoints that we've released to v2:

-   [Spaces endpoints](/en/docs/twitter-api/spaces/overview) to help
    people get more out of X Spaces, and to allow developers to help
    shape the future of audio conversations.
-   [Hide replies](/en/docs/twitter-api/tweets/hide-replies) , which
    allows you to build tools that help limit the impact of abusive,
    distracting, or misleading replies at scale -- a crucial piece to
    improving the health of the public conversation on X, and ensuring
    brands and people feel comfortable starting conversations.
-   New Lists endpoints that allow you to [pin and unpin
    Lists](/en/docs/twitter-api/lists/pinned-lists/introduction) , or
    look up someone's pinned Lists
-   New [batch compliance
    endpoints](/en/docs/twitter-api/compliance/batch-compliance/introduction)
    that allow you to ensure your stored user and Tweet data is in
    compliance.
:::
:::

::: c01-rich-text-editor
::: is-table-default
X API v2 also includes new features that will help you find more value
with the X API. A lot of what is new has been driven by your feedback,
and includes certain features that were reserved for enterprise
customers previously.

Some of the improvements to the API include:

Before you dive in, let's cover some of the fundamental changes we've
made to the way you will access and consume data from the endpoints.

### Discover new and updated response objects

The following six data objects are available with the v2 endpoints:

+-----------------------------------+-----------------------------------+
| **Object**                        | **Description**                   |
+===================================+===================================+
| **                                | The Tweet object has a long list  |
| [Tweet](/en/docs/twitter-api/data | of root-level fields, such as [   |
| -dictionary/object-model/tweet)** | id ]{.code-inline} , [ text       |
|                                   | ]{.code-inline} , and [           |
|                                   | created_at ]{.code-inline} .      |
|                                   | Tweet objects are also the parent |
|                                   | object to several child objects   |
|                                   | including [ user ]{.code-inline}  |
|                                   | , [ media ]{.code-inline} , [     |
|                                   | poll ]{.code-inline} , and [      |
|                                   | place ]{.code-inline} .           |
+-----------------------------------+-----------------------------------+
| **[User](/en/docs/twitter-api/dat | The user object contains X user   |
| a-dictionary/object-model/user)** | account metadata describing the   |
|                                   | referenced user.                  |
+-----------------------------------+-----------------------------------+
| **[                               | The Space object consists of      |
| Spaces](/en/docs/twitter-api/data | fields such as [ state            |
| -dictionary/object-model/space)** | ]{.code-inline} , [ host_id       |
|                                   | ]{.code-inline} , [ is_ticketed   |
|                                   | ]{.code-inline} , and even [ lang |
|                                   | ]{.code-inline} .\                |
+-----------------------------------+-----------------------------------+
| **                                | The List object contains basic    |
| [Lists](/en/docs/twitter-api/data | information about the requested   |
| -dictionary/object-model/space)** | list including [ description      |
|                                   | ]{.code-inline} , [ member_count  |
|                                   | ]{.code-inline} , and [ owner_id  |
|                                   | ]{.code-inline} .                 |
+-----------------------------------+-----------------------------------+
| **                                | If a Tweet contains media (such   |
| [Media](/en/docs/twitter-api/data | as images), then the media object |
| -dictionary/object-model/media)** | can be requested using the [      |
|                                   | media.fields ]{.code-inline}      |
|                                   | parameter and includes fields     |
|                                   | such as the [ media_key           |
|                                   | ]{.code-inline} , [ type          |
|                                   | ]{.code-inline} , [ url           |
|                                   | ]{.code-inline} , [               |
|                                   | preview_image_url, and more.      |
|                                   | ]{.code-inline}                   |
+-----------------------------------+-----------------------------------+
| **[Poll](/en/docs/twitter-api/dat | A poll included in a Tweet is not |
| a-dictionary/object-model/poll)** | a primary object on any endpoint, |
|                                   | but can be found and expanded in  |
|                                   | the Tweet object.                 |
+-----------------------------------+-----------------------------------+
| **                                | The place object consists of      |
| [Place](/en/docs/twitter-api/data | fields such as [ place_id         |
| -dictionary/object-model/place)** | ]{.code-inline} , [ geo           |
|                                   | ]{.code-inline} object, [         |
|                                   | country_code, and more            |
|                                   | ]{.code-inline} . This            |
|                                   | information can be used to        |
|                                   | identify Tweets and study Tweets  |
|                                   | by location.                      |
+-----------------------------------+-----------------------------------+

### 

### Flexibility to choose which objects and fields you receive 

When making a request to a GET endpoint, you will receive the primary
data object that relates to that endpoint, which will include a set of
default fields. For example, the Tweet object delivers the [ id
]{.code-inline} and [ text ]{.code-inline} fields as its default.

If you would like to retrieve additional fields with your request, you
will have to use the [fields](/en/docs/twitter-api/fields) and
[expansions](/en/docs/twitter-api/expansions) parameters. The expansions
parameter enables you to retrieve related data objects such as a user\'s
pinned Tweet or a media object, while the field operators enable you to
request specific fields within returned objects beyond the defaults.

Here is a full list of expansions that you can request with the
different X API v2 endpoints:\

  ----------------------------------- -----------------------------------
  **Object / Resource**               **Available expansions**

  **Tweets**                          [ author_id ]{.code-inline}\
                                      [ edit_history_tweet_ids
                                      ]{.code-inline}\
                                      [ entities.mentions.username
                                      ]{.code-inline}\
                                      [ in_reply_to_user_id
                                      ]{.code-inline}\
                                      [ referenced_tweets.id
                                      ]{.code-inline}\
                                      [ referenced_tweets.id.author_id
                                      ]{.code-inline}\
                                      [ attachments.poll_ids
                                      ]{.code-inline}\
                                      [ attachments.media_keys
                                      ]{.code-inline}\
                                      [ geo.place_id ]{.code-inline}

  **Users**                           [ pinned_tweet_id ]{.code-inline}

  **Spaces**                          [ invited_user_ids ]{.code-inline}\
                                      [ speaker_ids ]{.code-inline}\
                                      [ creator_id ]{.code-inline}\
                                      [ host_ids ]{.code-inline}\
                                      [ topic_ids ]{.code-inline}
  ----------------------------------- -----------------------------------

\
Learn more about [how to use fields and
expansions](/en/docs/twitter-api/data-dictionary/using-fields-and-expansions)
, and check out our [full list of data objects and
fields](/en/docs/twitter-api/data-dictionary) in the X API v2 data
dictionary.\
:::
:::

::: c01-rich-text-editor
<div>

More metrics are now accessible within Tweet, user, Spaces, Lists, and
media objects. These metrics are both public and private, and some
metrics can be broken down into an organic or promoted context for Tweet
ads.

Learn more about the available [metrics](/en/docs/twitter-api/metrics)
.\

  ------------------------------------------------------------------------------------------------------------------------------
                                           All Tweets  Ads                                                         
  -------------------- ------------------- ----------- ---------------------------------------------- ------------ -------------
  **Object**           **Available         **Public    **Private metrics** \                          **Organic    **Promoted
                       metrics**           metrics**   (requires [OAuth 1.0a User                     metrics**    metrics**
                                                       Context](/en/docs/authentication/oauth-1-0a)                
                                                       auth)                                                       

  [ tweets             [ retweet_count     ✔️                                                         ✔️           ✔️
  ]{.code-inline}      ]{.code-inline}                                                                             

  [ quote_count        ✔️                                                                                          
  ]{.code-inline}                                                                                                  

  [ like_count         ✔️                              ✔️                                             ✔️           
  ]{.code-inline}                                                                                                  

  [ reply_count        ✔️                              ✔️                                             ✔️           
  ]{.code-inline}                                                                                                  

  [ impression_count                       ✔️          ✔️                                             ✔️           
  ]{.code-inline}                                                                                                  

  [ url_profile_clicks                     ✔️          ✔️                                             ✔️           
  ]{.code-inline}                                                                                                  

  [ url_link_clicks                        ✔️          ✔️                                             ✔️           
  ]{.code-inline}                                                                                                  

  [ user               [ follower_count    ✔️                                                                      
  ]{.code-inline}      ]{.code-inline}                                                                             

  [ following_count    ✔️                                                                                          
  ]{.code-inline}                                                                                                  

  [ tweet_count        ✔️                                                                                          
  ]{.code-inline}                                                                                                  

  [ listed_count       ✔️                                                                                          
  ]{.code-inline}                                                                                                  

  [ media              [ view_count                    ✔️                                                          
  ]{.code-inline}      ]{.code-inline}                                                                             

  [ playback_0_count                       ✔️                                                                      
  ]{.code-inline}\                                                                                                 
  [ playback_25_count                                                                                              
  ]{.code-inline}\                                                                                                 
  [ playback_50_count                                                                                              
  ]{.code-inline}\                                                                                                 
  [ playback_75_count                                                                                              
  ]{.code-inline}\                                                                                                 
  [ playback_100_count                                                                                             
  ]{.code-inline}                                                                                                  

  [ space              [ participant_count ✔️                                                                      
  ]{.code-inline}      ]{.code-inline}                                                                             

  [ subscriber_count                       ✔️                                                                      
  ]{.code-inline}                                                                                                  

  [ list               [ follower_count    ✔️\                                                                     
  ]{.code-inline}      ]{.code-inline}\                                                                            

  [ member_count       ✔️                                                                                          
  ]{.code-inline}                                                                                                  
  ------------------------------------------------------------------------------------------------------------------------------

</div>
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
  "public_metrics": {
            "retweet_count": 5239,
            "reply_count": 1844,
            "like_count": 17168,
            "quote_count": 3275
        }


  "non_public_metrics": {
            "impression_count": 956,
            "user_profile_clicks": 34,
            "url_link_clicks": 57
   }


   "organic_metrics": {
            "impression_count": 956,
            "like_count": 1244,
            "reply_count": 300,
            "user_profile_clicks": 150
            "url_link_clicks": 57
        }


   "promoted_metrics": {
            "impression_count": 25086,
            "like_count": 9045,
            "reply_count": 637,
            "user_profile_clicks": 265,
            "url_link_clicks": 48
        }
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Annotations can be used to discover Tweets on topics of interest or to
segment Tweets by entity categories.

Tweets are analyzed and annotated based on the content of the Tweet text
by both semantic labeling (context annotations) and internal machine
learning algorithms (named entity recognition). These annotations are
now available via API in the response payload. We call these new
elements "annotations" and they are delivered as two fields, [
context_annotations ]{.code-inline} and [ entity ]{.code-inline} , and
can be used to filter search Tweets, Tweet counts, and filtered stream
responses.

Learn more about [Tweet annotations](/en/docs/twitter-api/annotations) .

Here is an example of what this would look like in your payload:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 "context_annotations": [
      {
        "domain": {
          "id": "45",
          "name": "Brand Vertical",
          "description": "Top level entities that describe a Brands industry"
        }
      },
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
          "id": "10026364281",
          "name": "Apple"
        }
      },
      {
        "domain": {
          "id": "48",
          "name": "Product",
          "description": "Products created by Brands.  Examples: Ford Explorer, Apple iPhone."
        },
        "entity": {
          "id": "10044903039",
          "name": "Apple - iOS"
        }
      }
    ],
    "created_at": "2020-05-12T19:44:51.000Z",
    "entities": {
      "annotations": [
        {
          "start": 49,
          "end": 51,
          "probability": 0.8997,
          "type": "Product",
          "normalized_text": "iOS"
        }
      ]

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
X API v2 now includes a feature that allows developers to lookup the
relationship (called connection status) between the authenticating user
and the user being looked up in the response payload.

This is comparable to [GET
friendships/show](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-show)
and [GET
friendships/lookup](https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-friendships-lookup)
endpoints in V1.1.

The sample API Request to get the connection status using the [User
Lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction)
Endpoint in the X API v2 is:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 https://api.twitter.com/2/users/by/username/XDevelopers?user.fields=connection_status
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "data": {
        "username": "XDevelopers",
        "name": "Developers",
        "connection_status": [
            "following"
        ],
        "id": "2244994945"
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Using the X API v2, a developer can programmatically find out if the
authenticating user:

-   is being followed by the user being looked up.
-   is following the user being looked up.
-   has received a follow request from the user being looked up.
-   sent a follow request to the user being looked up.
-   blocked the user being looked up.
-   muted the user being looked up.
:::
:::

::: c01-rich-text-editor
::: is-table-default
The X API v2 endpoints provide edited Tweet metadata. The *Edit Tweet*
feature was first introduced for testing among X employees on September
1, 2022. Starting on that date, eligible Tweets are editable for 30
minutes and up to 5 times. Also, all objects for Tweets since September
29, 2022  include Tweet edit metadata, even if the Tweet was never
edited. Each time a Tweet is edited, a new Tweet ID is created. A
Tweet\'s edit history can be described by chaining these IDs together,
starting with the original ID.

Using the X API v2, a developer can find out:

-   If a Tweet was edit eligible at the time of creation. Some Tweets,
    such as those with polls or scheduled Tweets, can not be edited.
-   Tweets are editable for 30 minutes, and can be edited up to 5 times.
    For editable Tweets you can see if time for editing remains and how
    many more edits are possible.
-   If you are viewing an edited version of a Tweet (in most cases the
    API will return the most recent version of a Tweet, unless a
    specific past version is requested by Tweet ID).
-   The entire edit history of the Tweet.
-   The engagement attributed to each version of the Tweet.

Learn more about [Edit
Tweets](https://developer.twitter.com/en/docs/twitter-api/edit-tweets) .
:::
:::

::: c01-rich-text-editor
::: is-table-default
We have introduced a new Tweet field to help you identify which
conversation thread that Tweet belongs to. In addition to this, we
launched a new filter operator that matches Tweets that share a common
conversation ID, and is available for search Tweets, Tweet counts, and
filtered stream.

A conversation ID is the Tweet ID of the Tweet that started the
conversation.

Learn more about [conversation
tracking](https://developer.twitter.com/en/docs/twitter-api/conversation-id)
.
:::
:::
:::
