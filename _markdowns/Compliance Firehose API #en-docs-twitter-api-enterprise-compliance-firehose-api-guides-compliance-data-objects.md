::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Possible types of compliance events will include Tweet (or "status")
events and User events, for which there are multiple types described
below.\

Please note:

-   Read more about User statuses
    [here](https://support.twitter.com/articles/14016) and our developer
    policy around deleted Tweets
    [here](https://dev.twitter.com/overview/terms/policy#3.Update_Respect_Users_Control_and_Privacy)
    .
-   The Compliance Firehose has been updated to provide \'tweet_edit\'
    events.
-   Several User delete, protect and suspend events are not necessarily
    permanent and can toggle between states infinitely. These include:
    user_delete,user_undelete, user_protect, user_unprotect and
    user_suspend, user_unsuspend.
-   User_deletes are followed by status_deletes 30 days later only if
    the user has not selected to user_undelete their account. It is
    possible that a user_delete is reversed by the user and deletes for
    all of their tweets 30 days later do not occur.
-   User_suspend is an action that remains true unless the user is
    subject to an user_unsuspend event. These are not subject to any
    changes on a 30 day time period.

Refer to the 'Recommended Action' column to understand how to process
each type of event in order to respect the privacy and intent of the end
user.

  ----------------------- ---------- -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Original Message Type   Object     Permanent (Yes/No)   Recommended Action
  delete                  Status     Yes                  Delete associated Tweet.
  status_withheld         Status     Yes                  Suppress associated Tweet in specific countries listed in the status_withheld message.
  drop                    Status     No                   Remove the Tweet from public view.
  undrop                  Status     No                   Status may be displayed again and treated as public.
  tweet_edit              Status     Yes                  Honor and, where relevant, display the new edit.
  user_delete             User       No                   Suppress or delete all Tweets by associated user.
  user_undelete           User       No                   All Tweets by associated user may be displayed again and treated as public.
  user_protect            User       No                   Suppress or delete all Tweets by associated user.
  user_unprotect          User       No                   All Tweets by associated user may be displayed again and treated as public.
  user_suspend            User       No                   Suppress or delete all Tweets by associated user.
  user_unsuspend          User       No                   All Tweets by associated user may be displayed again and treated as public.
  scrub_geo               User       Yes                  Delete all geodata provided by Twitter for all Tweets by the user prior to the specified Tweet in the scrub_geomessage. Note that subsequent Tweets by a user may contain geodata that may be used.
  user_withheld           User       Yes                  Suppress Tweets by associated user in specific countries listed in the user_withheld message.
  delete                  Favorite   Yes                  Delete associated like/favorite.
  ----------------------- ---------- -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
``` {.line-numbers .t05__pre--with-button}
 {"tweet_edit":
   {
     "id": "1557445923210514432"
     "initial_tweet_id": "1557433858676740098",
     "edit_tweet_ids": ["1557433858676740098", "1557445923210514432"],
     "timestamp_ms": "1660155761384"
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
  "delete": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220608",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
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
  "status_withheld": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220608",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "withheld_in_countries": [
      "XY"
    ],
    "timestamp_ms": "1432228155593"
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
  "drop": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220600",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
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
  "undrop": {
    "status": {
      "id": 601430178305220600,
      "id_str": "601430178305220600",
      "user_id": 3198576760,
      "user_id_str": "3198576760"
    },
    "timestamp_ms": "1432228155593"
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
  "scrub_geo": {
    "user_id": 519761961,
    "up_to_status_id": 411552403083628540,
    "up_to_status_id_str": "411552403083628544",
    "user_id_str": "519761961",
    "timestamp_ms": "1432228180345"
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
  "user_delete": {
    "id": 771136850,
    "timestamp_ms": "1432228153548"
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
  "user_undelete": {
    "id": 796250066,
    "timestamp_ms": "1432228149062"
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
  "user_withheld": {
    "user": {
      "id": 1375036644,
      "id_str": "1375036644"
    },
    "withheld_in_countries": [
      "XY"
    ],
    "timestampMs": "2014-08-27T23:49:41.839+00:00"
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
  "user_protect": {
    "id": 3182003550,
    "timestamp_ms": "1432228177137"
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
  "user_unprotect": {
    "id": 2911076065,
    "timestamp_ms": "1432228180113"
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
  "user_suspend": {
    "id": 3120539094,
    "timestamp_ms": "1432228194217"
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
  "user_unsuspend": {
    "id": 3293130873,
    "timestamp_ms": "1432228193828"
  }
}
    
```
:::
:::
:::
:::
