::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Possible types of compliance events will include Tweet events and User
events, for which there are multiple types described below.\

Please note:

-   Read more about Tweet visibility
    [here](https://support.twitter.com/articles/14016) and our developer
    policy around deleted Tweets
    [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy)
    .
-   The Tweet Compliance stream includes events triggered by Tweets
    getting edited. See the \'tweet_edit\' example event below.
-   Several User delete, protect and suspend events are not necessarily
    permanent and can toggle between states infinitely. These include:
    user_delete, user_undelete, user_protect, user_unprotect and
    user_suspend, user_unsuspend.
-   User_deletes are followed by Tweet deletes 30 days later only if the
    user has not selected to user_undelete their account. It is possible
    that a user_delete is reversed by the user and deletes for all of
    their Tweets 30 days later do not occur.
-   User_suspend is an action that remains true unless the user is
    subject to an user_unsuspend event. These are not subject to any
    changes on a 30 day time period.

Refer to the 'Recommended Action' column to understand how to process
each type of event in order to respect the privacy and intent of the end
user.
:::
:::

::: c01-rich-text-editor
::: is-table-default
See the payload examples below for each compliance event described in
the table above.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "delete": {
            "tweet": {
                "id": "601430178305220608",
                "author_id": "3198576760"
            },
            "event_at": "2022-12-23T12:34:56.789Z"
        }
    }

}
    
```
:::
:::
:::

::: {.b02-rich-text .twtr-rte .twtr-component-space--md}
::: {.b02__rich-text .twtr-scribe-clicks-within .b02__type--large}
When a deleted Tweet has been Quote Tweeted, there will be an additional
Tweet \'delete\' event with a \"quote_tweet_id\" attribute for each
Quote Tweet.

#### Tweet edit
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
    "data": {
        "tweet_edit": {
            "tweet": {
                "id": "1567233994734948354"
            },
            "initial_tweet_id": "1567233844205453313",
            "edit_tweet_ids": [
                "1567233844205453313",
                "1567233994734948354"
            ],
            "event_at": "2022-09-06T19:31:16.801Z"
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
``` line-numbers
 {
    "data": {
        "withheld": {
            "tweet": {
                "id": "601430178305220608",
                "author_id": "3198576760"
            },
            "withheld_in_countries": [
                "XY"
            ],
            "event_at": "2022-12-23T12:34:56.789Z"
        }
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
When a withheld Tweet has been Quote Tweeted, there will be an
additional Tweet \'withheld\' event with a \"quote_tweet_id\" attribute
for each Quote Tweet.

#### 

#### Tweet Drop
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "drop": {
            "tweet": {
                "id": "601430178305220600",
                "author_id": "3198576760"
            },
            "event_at": "2022-12-23T12:34:56.789Z"
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
``` line-numbers
 {
  "data": 
     {
       "undrop": {
          "tweet": {
             "id": "601430178305220600",
             "author_id": "3198576760"
           },
         "event_at": "2022-12-23T12:34:56.789Z"
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
``` line-numbers
 {
   "data": 
    {
      "scrub_geo": {
        "user": {
          "id": "1375036644"
        },
      "up_to_tweet_id": "411552403083628544",
      "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_delete": {
            "user": {
                "id": "1375036644"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_undelete": {
            "user": {
                "id": "1375036644"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_withheld": {
            "user": {
                "id": "1375036644"
            },
            "withheld_in_countries": [
                "XY"
            ],
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_protect": {
            "user": {
                "id": "3182003550"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_unprotect": {
            "user": {
                "id": "3182003550"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_suspend": {
            "user": {
                "id": "1375036644"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
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
``` line-numbers
 {
    "data": {
        "user_unsuspend": {
            "user": {
                "id": "1375036644"
            },
            "event_at": "2022-06-27T23:49:41.839+00:00"
        }
    }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
**User profile modification**
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "user_profile_modification": {
      "user": {
        "id": "906948460078698496"
      },
      "event_at": "2022-07-12T19:47:59.442Z",
      "profile_field": "profile.description",
      "new_value": "Home of the @SnowbotDev chatbot."
    }
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The \"profile_field\" attribute indicates what in the User profile
changed, and can contain the following values:

-   \"profile.name\"\
-   \"profile.location\"
-   \"profile.description\"
-   \"profile.url\"
-   \"profile.profileBanner\"
-   \"profile.profileBanner.url\"
-   \"profile.profileImage\"
-   \"profile.profileImage.url\"
:::
:::
:::
