::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
When users communicate with businesses through Direct Messages, they may
be guided by [Welcome
Messages](https://dev.twitter.com/rest/direct-messages/direct-messages/welcome-messages)
or led to a private conversation via a Direct Message deeplink. In these
cases, it can be important for developers to know if another object
preceded the DM in conversation. For example, Initiated Via helps a
customer service agent see the full conversation history or enable a bot
developer to perform A/B testing of different welcome messages.

The initiated_via object in the Direct Message event object indicates
the ID of the Twitter entity that directly preceded the DM in the
sender's context. Currently tweet_id and welcome_message_id may be
included. The initiated_via object is only present if a Twitter entity
directly preceded the DM.

## initiated_via object

  ----------------------------------- -----------------------------------
  initiated_via.tweet_id\             The ID of the Tweet with Direct
                                      Message Prompt the event was
                                      initiated from if one was used.

  initiated_via.welcome_message_id\   The ID of the Welcome Message
                                      immediately preceding the event if
                                      one was used.\
  ----------------------------------- -----------------------------------

**Note:** Direct Messages are never referenced as an entity type under
the "initiated_via" object. Developers should continue to rely on IDs
for ordering Direct Message events.

## Example Direct Message Event

The following Direct Message event was preceded by a Direct Message
prompt from a Tweet or a Welcome Message was presented to the user.\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "type": "message_create",
  "id": "1234858592",
  "created_timestamp": "1392078023603",
  "initiated_via": {
    "tweet_id": "123456",
    "welcome_message_id": "456789"
  },
  "message_create": {
    "target": {
      "recipient_id": "1234858592"
    },
    "sender_id": "3805104374",
    "source_app_id": "268278",
    "message_data": {
      "text": "Blue Bird",
      "entities": {
        "hashtags": [],
        "symbols": [],
        "urls": [],
        "user_mentions": [],
      },
      "quick_reply_response": {
        "type": "options",
        "metadata": "external_id_2"
      },
      "attachment": {
        "type": "media",
        "media": {
         ...
        }
      }
    }
  }
}
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
