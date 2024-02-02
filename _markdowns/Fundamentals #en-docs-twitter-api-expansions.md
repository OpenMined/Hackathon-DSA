::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
With expansions, developers can expand objects referenced in the
payload. Objects available for expansion are referenced by ID. For
example, the ` referenced_tweets.id ` and ` author_id ` fields returned
in the [Tweets
lookup](/en/docs/twitter-api/tweets/lookup/introduction.html) payload
can be expanded into complete objects. If you would like to request
fields related to the user that posted that Tweet, or the media, poll,
or place that was included in that Tweet, you will need to pass the
related expansion query parameter in your request to receive that data
in your response. Currently, v2 endpoints that return Tweets, Users,
Lists, Spaces, and Direct Message event objects all support expansions
(see examples below).

When including an expansion in your request, we will include that
expanded object's default fields within the same response. It helps
return additional data in the same response without the need for
separate requests. If you would like to request additional
[fields](/en/docs/twitter-api/fields.html) related to the expanded
object, you can include the field parameter associated with that
expanded object, along with a comma-separated list of fields that you
would like to receive in your response. Please note fields are not
always returned in the same order they were requested in the query.

The Tweet payload below contains reference IDs for complementary objects
we can expand on, including the [ author_id ]{.code-inline} of who
posted the Tweet, the [ id ]{.code-inline} of a *referenced* Tweet, and
a [ media_key ]{.code-inline} for a media attachment.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "attachments": {
            "media_keys": [
                "16_1211797899316740096"
            ]
        },
        "author_id": "2244994945",
        "id": "1212092628029698048",
        "referenced_tweets": [
            {
                "type": "replied_to",
                "id": "1212092627178287104"
            }
        ],
        "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
\
We can expand on ` attachments.media_keys ` to view the media object,
` author_id ` to view the user object, and ` referenced_tweets.id ` to
view the Tweet object the originally requested Tweet was referencing.
Expanded objects will be nested in the ` "includes" ` object, as can be
seen in the sample response below. \

### Available expansions for Tweet payloads

  ------------------------------------------ -----------------------------------------------------------------------------------------------------
  Expansion                                  Description
  ` author_id `                              Returns a user object representing the Tweet's author
  ` referenced_tweets.id `                   Returns a Tweet object that this Tweet is referencing (either as a Retweet, Quoted Tweet, or reply)
  [ edit_history_tweet_ids ]{.code-inline}   Returns Tweet objects that are part of a Tweet\'s edit history
  ` in_reply_to_user_id `                    Returns a user object representing the Tweet author this requested Tweet is a reply of
  ` attachments.media_keys `                 Returns a media object representing the images, videos, GIFs included in the Tweet
  ` attachments.poll_ids `                   Returns a poll object containing metadata for the poll included in the Tweet
  ` geo.place_id `                           Returns a place object containing metadata for the location tagged in the Tweet
  ` entities.mentions.username `             Returns a user object for the user mentioned in the Tweet
  ` referenced_tweets.id.author_id `         Returns a user object for the author of the referenced Tweet
  ------------------------------------------ -----------------------------------------------------------------------------------------------------

### 

### Available expansion for User payloads

  --------------------- ---------------------------------------------------------------------------------------
  Expansion             Description
  ` pinned_tweet_id `   Returns a Tweet object representing the Tweet pinned to the top of the user's profile
  --------------------- ---------------------------------------------------------------------------------------

### 

### Available expansions for Direct Message event payloads

  ---------------------------- ------------------------------------------------------------------------------------------------------------------------
  Expansion                    Description
  ` attachments.media_keys `   Returns a Media object that was attached to a Direct Message
  ` referenced_tweets.id `     Returns a Tweet object that was referenced in a Direct Message
  ` sender_id `                Returns a User object representing the author of a Direct Message and who invited a participant to join a conversation
  ` participant_ids `          Returns a User object representing a participant that joined or left a conversation
  ---------------------------- ------------------------------------------------------------------------------------------------------------------------

### 

### Available expansions for Spaces payloads

  ---------------------- ----------------------------------------------------------------------
  Expansion              Description
  ` invited_user_ids `   Returns User objects representing what accounts were invited
  ` speaker_ids `        Returns User objects representing what accounts spoke during a Space
  ` creator_id `         Returns a User object representing what account created the Space
  ` host_ids `           Returns User objects representing what accounts were set up as hosts
  ` topics_ids `         Returns topic descriptions that were set up by the creator
  ---------------------- ----------------------------------------------------------------------

### 

### Available expansion for Lists payloads

  -------------- --------------------------------------------------------------------------------
  Expansion      Description
  ` owner_id `   Returns a User object representing what account created and maintains the List
  -------------- --------------------------------------------------------------------------------

## 

## Expanding the media, Tweet, and user objects

####  In the following request, we are requesting the following expansions to include alongside the default Tweet fields.  Be sure to replace ` $ACCESS_TOKEN ` with your own generated [App-only Token](/content/developer-twitter/en/docs/authentication/app-only) . 

-   ` attachments.media_keys `
-   ` referenced_tweets.id `
-   ` author_id `

**Sample Request**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets/1212092628029698048?expansions=attachments.media_keys,referenced_tweets.id,author_id' --header 'Authorization: Bearer $ACCESS_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "attachments": {
            "media_keys": [
                "16_1211797899316740096"
            ]
        },
        "author_id": "2244994945",
        "id": "1212092628029698048",
        "referenced_tweets": [
            {
                "type": "replied_to",
                "id": "1212092627178287104"
            }
        ],
        "text": "We believe the best future version of our API will come from building it with YOU. Here’s to another great year with everyone who builds on the Twitter platform. We can’t wait to continue working with you in the new year. https://t.co/yvxdK6aOo2"
    },
    "includes": {
        "media": [
            {
                "media_key": "16_1211797899316740096",
                "type": "animated_gif"
            }
        ],
        "users": [
            {
                "id": "2244994945",
                "name": "Twitter Dev",
                "username": "TwitterDev"
            }
        ],
        "tweets": [
            {
                "author_id": "2244994945",
                "id": "1212092627178287104",
                "referenced_tweets": [
                    {
                        "type": "replied_to",
                        "id": "1212092626247110657"
                    }
                ],
                "text": "These launches would not be possible without the feedback you provided along the way, so THANK YOU to everyone who has contributed your time and ideas. Have more feedback? Let us know ⬇️ https://t.co/Vxp4UKnuJ9"
            }
        ]
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the following request, we are requesting the following expansions to
include alongside the default Tweet fields:

**Sample Request**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets/1199786642791452673?expansions=attachments.poll_ids' --header 'Authorization: Bearer $ACCESS_TOKEN'

    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "attachments": {
            "poll_ids": [
                "1199786642468413448"
            ]
        },
        "id": "1199786642791452673",
        "text": "C#"
    },
    "includes": {
        "polls": [
            {
                "id": "1199786642468413448",
                "options": [
                    {
                        "position": 1,
                        "label": "“C Sharp”",
                        "votes": 795
                    },
                    {
                        "position": 2,
                        "label": "“C Hashtag”",
                        "votes": 156
                    }
                ]
            }
        ]
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the following request, we are requesting the following expansions to
include alongside the default Tweet fields:

**Sample Request**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 curl 'https://api.twitter.com/2/tweets/:ID?expansions=geo.place_id’ --header 'Authorization: Bearer $ACCESS_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "geo": {
            "place_id": "01a9a39529b27f36"
        },
        "id": "ID",
        "text": "Test"
    },
    "includes": {
        "places": [
            {
                "full_name": "Manhattan, NY",
                "id": "01a9a39529b27f36"
            }
        ]
    }
}
    
```
:::
:::
:::
:::
