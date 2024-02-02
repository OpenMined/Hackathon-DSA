::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Non-streaming standard endpoints have been updated to provide edited
Tweet metadata. The statuses/filter and statuses/sample streaming
endpoints have not been updated, while other endpoints that provide
Tweet objects have been updated. The *Edit Tweets* feature was first
introduced for testing among Twitter employees on September 1, 2022.
Starting on that date, eligible Tweets are editable for 30 minutes and
up to 5 times. *All objects for Tweets created since September 29, 2022*
include Tweet edit metadata, even if the Tweet was never edited. Each
time a Tweet is edited, a new Tweet ID is created. A Tweet\'s edit
history can be described by chaining these IDs together, starting with
the original ID. Additionally, if any Tweet in the edit chain is
deleted, all Tweets in that chain are deleted as well.

These edit metadata details are included when the
include_ext_edit_control request parameter is set to true:

[ include_ext_edit_control=true ]{.code-inline}

With these new metadata, a developer can find out: \

-   If a Tweet was edit eligible at the time of creation. Some Tweets,
    such as those with polls or scheduled Tweets, cannot be edited.
-   Tweets are editable for 30 minutes, and can be edited up to 5 times.
    For editable Tweets, you can see if time for editing remains and how
    many more edits are possible.
-   If you are viewing an edited version of a Tweet. In most cases, the
    API will return the most recent version of a Tweet, unless a
    specific past version is requested by Tweet

One new Tweet attribute has been added at the root level:

-   **ext_edit_control** - Provides all Tweet IDs associated with the
    edit history of the Tweet. The \"edit_tweet_ids\" attribute is an
    array that provides all IDs associated with its edit history. If the
    Tweet has not been edited, this array will contain a single ID.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 "ext_edit_control": {
    "initial": {
      "edit_tweet_ids":["1550220531252678656"], 
      "editable_until_msecs": "123",
      "edits_remaining": "5",
      "is_edit_eligible": true
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
-   Tweet is promoted
-   Tweet has a poll
-   Tweet is a non-self-thread reply
-   Tweet is a Retweet (note that Quote Tweets are eligible for edit)
-   Tweet is nullcast
-   Community Tweet
-   Superfollow Tweet
-   Collaborative Tweet

## Example attributes for unedited Tweet 

The JSON below highlights edit metadata that is included for a Tweet
posted after the edit Tweet feature was added. This example is for a
Tweet that has no edit history.

Note that the \"edit_tweet_ids\" array has a single ID.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "created_at": "Wed Aug 16 18:29:02 +0000 2022",
  "id": 1557433858676740098,
  "id_str": "1557433858676740098",
  "text": "I wonder if I will every use teh edit button",
  "ext_edit_control": {
    "initial": {
      "edit_tweet_ids":["1557433858676740098"], 
      "editable_until_msecs": "1658438151000",
      "edits_remaining": "5",
      "is_edit_eligible": true
    }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
The JSON below highlights edit metadata that is included for a Tweet
posted after the edit Tweet feature was added. This example is for a
Tweet that has had a single edit.

Note that the \"edit_tweet_ids\" array has two IDs, one for the original
Tweet and one for the edited update.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "created_at": "Wed Aug 16 18:35:42 +0000 2022",
  "id": 1557445923210514432,
  "id_str": "1557445923210514432",
  "text": "I wonder if I will ever use the edit button",
 "ext_edit_control": {
        "edit": {
          "edit_control_initial": {
            "edit_tweet_ids": [
              "1557433858676740098",
              "1557445923210514432"
            ],
            "editable_until_msecs": "1658438151000",
            "edits_remaining": "4",
            "is_edit_eligible": true
          },
          "initial_tweet_id": "1557433858676740098"
        }
   }

}

    
```
:::
:::
:::
:::
