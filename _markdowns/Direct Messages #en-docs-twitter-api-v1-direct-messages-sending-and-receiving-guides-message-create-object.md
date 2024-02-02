::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
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

::: c01-rich-text-editor
::: is-table-default
  ---------------------------------- -----------------------------------------------------------------------------------------------------
  Property                           Description
  type                               The type of event. For Direct Messages type will be [ message_create ]{.code-inline} .
  id                                 The ID of the direct message event.
  created_timestamp                  Epoch timestamp of when the Direct Message event was created.
  initiated_via.tweet_id             The ID of the Tweet with Direct Message Prompt the conversation was initiated from if one was used.
  initiated_via.welcome_message_id   The ID of the Welcome Message immediatley preceding the conversation if one was used.
  ---------------------------------- -----------------------------------------------------------------------------------------------------

  ------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  message_create.target.recipient_id   The ID of the user receiving the message.
  message_create.sender_id             The ID of the user sending the message.
  message_create.source_app_id         The ID of the application used to create the event. App details are available in the apps object in JSON payloads containing [ message_create ]{.code-inline} events.
  message_create.message_data          A [ message_data ]{.code-inline} object.
  ------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------- ----------------------------------------------------------------------------------------
  message_data.text                   The Direct Message text.
  message_data.entities               A Twitter [entities](/en/docs/tweets/data-dictionary/overview/entities-object) object.
  message_data.quick_reply_response   A [Quick Reply](/en/docs/direct-messages/quick-replies/overview) response object.
  message_data.attachment             An [attachment](/en/docs/direct-messages/message-attachments/overview) object (media)
  ----------------------------------- ----------------------------------------------------------------------------------------
:::
:::
:::
:::
:::
:::
:::
:::
