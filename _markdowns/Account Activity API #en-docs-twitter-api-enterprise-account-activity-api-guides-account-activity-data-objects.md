::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  Object                            Details
  [ for_user_id ]{.code-inline}     Identifies the user subscription subscribed that the event is related to.
  [ is_blocked_by ]{.code-inline}   (conditional) Shown only when another user mentions your subscribed user. Included if true for Tweet mention events only.
  [ source ]{.code-inline}          The user that is performing the activity. For example, the user that is following, blocking, or muting is the source user.
  [ target ]{.code-inline}          The user that the activity applies to. For example, the user that is being followed, blocked, or muted is the target user.
  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------
:::
:::

::: c01-rich-text-editor
::: is-table-default
## Payload examples

See the payload examples below for each Account Activity event described
in the table above.
:::
:::

::: c01-rich-text-editor
#### []{#tweet_create_events} tweet_create_events (Tweets, Retweets, Replies, QuoteTweets)
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "tweet_create_events": [
      {
        <Tweet Object>
      }
    ]
}
    
```
:::
:::
:::

::: c01-rich-text-editor
#### []{#tweet_create_events} tweet_create_events (@mentions)
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "user_has_blocked": "false",
    "tweet_create_events": [
      {
        <Tweet Object>
      }
    ]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "favorite_events": [{
        "id": "a7ba59eab0bfcba386f7acedac279542",
        "created_at": "Mon Mar 26 16:33:26 +0000 2018",
        "timestamp_ms": 1522082006140,
        "favorited_status": {
            <Tweet Object>
        },
        "user": {
            <User Object>
        }
    }]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "follow_events": [{
            "type": "follow",
            "created_timestamp": "1517588749178",
            "target": {
                <User Object >
            },
            "source": {
                < User Object >
            }
        ]
    }
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "follow_events": [{
            "type": "unfollow",
            "created_timestamp": "1517588749178",
            "target": {
                <User Object >
            },
            "source": {
                < User Object >
            }
        ]
    }
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "block_events": [{
        "type": "block",
        "created_timestamp": "1518127020304",
        "source": {
            <User Object>
        },
        "target": {
            <User Object>
        }
    }]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "block_events": [{
        "type": "unblock",
        "created_timestamp": "1518127020304",
        "source": {
            <User Object>
        },
        "target": {
            <User Object>
        }
    }]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "mute_events": [
        {
            "type": "mute",
            "created_timestamp": "1518127020304",
            "source": {
                <User Object>
            },
            "target": {
                <User Object>
            }
        }
    ]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "2244994945",
    "mute_events": [
        {
            "type": "unmute",
            "created_timestamp": "1518127020304",
            "source": {
                <User Object>
            },
            "target": {
                <User Object>
            }
        }
    ]
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "user_event": {
        "revoke": {
            "date_time": "2018-05-24T09:48:12+00:00",
            "target": {
                "app_id": "13090192"
            },
            "source": {
                "user_id": "63046977"
            }
        }
    }
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "4337869213",
    "direct_message_events": [{
        "type": "message_create",
        "id": "954491830116155396",
        "created_timestamp": "1516403560557",
        "message_create": {
            "target": {
                "recipient_id": "4337869213"
            },
            "sender_id": "3001969357",
            "source_app_id": "13090192",
            "message_data": {
                "text": "Hello World!",
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "user_mentions": [],
                    "urls": []
                }
            }
        }
    }],
    "apps": {
        "13090192": {
            "id": "13090192",
            "name": "FuriousCamperTestApp1",
            "url": "https://twitter.com/furiouscamper"
        },
        "users": {},
        "3001969357": {
            "id": "3001969357",
            "created_timestamp": "1422556069340",
            "name": "Jordan Brinks",
            "screen_name": "furiouscamper",
            "location": "Boulder, CO",
            "description": "Alter Ego - Twitter PE opinions-are-my-own",
            "url": "https://t.co/SnxaA15ZuY",
            "protected": false,
            "verified": false,
            "followers_count": 22,
            "friends_count": 45,
            "statuses_count": 494,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg"
        },
        "4337869213": {
            "id": "4337869213",
            "created_timestamp": "1448312972328",
            "name": "Harrison Test",
            "screen_name": "Harris_0ff",
            "location": "Burlington, MA",
            "protected": false,
            "verified": false,
            "followers_count": 8,
            "friends_count": 8,
            "profile_image_url": "null",
            "statuses_count": 240,
            "profile_image_url_https": "https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png"
        }
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
####  direct_message_indicate_typing_events
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "4337869213",
    "direct_message_indicate_typing_events": [{
        "created_timestamp": "1518127183443",
        "sender_id": "3284025577",
        "target": {
            "recipient_id": "3001969357"
        }
    }],
    "users": {
        "3001969357": {
            "id": "3001969357",
            "created_timestamp": "1422556069340",
            "name": "Jordan Brinks",
            "screen_name": "furiouscamper",
            "location": "Boulder, CO",
            "description": "Alter Ego - Twitter PE opinions-are-my-own",
            "url": "https://t.co/SnxaA15ZuY",
            "protected": false,
            "verified": false,
            "followers_count": 23,
            "friends_count": 47,
            "statuses_count": 509,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg"
        },
        "3284025577": {
            "id": "3284025577",
            "created_timestamp": "1437281176085",
            "name": "Bogus Bogart",
            "screen_name": "bogusbogart",
            "protected": true,
            "verified": false,
            "followers_count": 1,
            "friends_count": 4,
            "statuses_count": 35,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/763383202857779200/ndvZ96mE_normal.jpg"
        }
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
####  direct_message_mark_read_events
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "4337869213",
    "direct_message_mark_read_events": [{
        "created_timestamp": "1518452444662",
        "sender_id": "199566737",
        "target": {
            "recipient_id": "3001969357"
        },
        "last_read_event_id": "963085315333238788"
    }],
    "users": {
        "199566737": {
            "id": "199566737",
            "created_timestamp": "1286429788000",
            "name": "Le Braat",
            "screen_name": "LeBraat",
            "location": "Denver, CO",
            "description": "data by day @twitter, design by dusk",
            "protected": false,
            "verified": false,
            "followers_count": 299,
            "friends_count": 336,
            "statuses_count": 752,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/936652894371119105/YHEozVAg_normal.jpg"
        },
        "3001969357": {
            "id": "3001969357",
            "created_timestamp": "1422556069340",
            "name": "Jordan Brinks",
            "screen_name": "furiouscamper",
            "location": "Boulder, CO",
            "description": "Alter Ego - Twitter PE opinions-are-my-own",
            "url": "https://t.co/SnxaA15ZuY",
            "protected": false,
            "verified": false,
            "followers_count": 23,
            "friends_count": 48,
            "statuses_count": 510,
            "profile_image_url": "null",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/851526626785480705/cW4WTi7C_normal.jpg"
        }
    }
}
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "for_user_id": "930524282358325248",
    "tweet_delete_events": [
{
        "status": {
            "id": "1045405559317569537",
            "user_id": "930524282358325248"
        },
        "timestamp_ms": "1432228155593"
    }
   ]
}
    
```
:::
:::
:::
:::
