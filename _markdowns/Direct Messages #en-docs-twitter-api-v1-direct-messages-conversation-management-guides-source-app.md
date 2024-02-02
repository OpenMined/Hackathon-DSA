::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Some Twitter accounts may make use of more than one application to send
Direct Messages --- such as when a human social care app is used
alongside a separate bot app to manage the same account. In these cases,
it can be helpful for developers to know which app was used to send a
given message.

The new [ source_app ]{.code-inline} object will return this information
for all DMs sent by an account. This object is included in the JSON
payload for webhooks and REST endpoints. It is relevant on the read path
only --- Twitter automatically adds this information based on the app
authentication used to post a DM. This value will not be returned in the
response for POST events/new.json.

**Note:** This same pattern exists with Tweets with the [ source
]{.code-inline} property, however the JSON structure is different.
Please also note that this object will not be included for DMs received
by an authenticating user and is only included for DMs sent by the
authenticating user.

## source_app object

  ----------------------------------- -----------------------------------
  id                                  The ID of the Twitter app used by
                                      the authenticating user to send the
                                      DM.\

  name                                The name of the Twitter app used by
                                      the authenticating user to send the
                                      DM.\

  url                                 The URL of the Twitter app used by
                                      the authenticating user to send the
                                      DM.\
  ----------------------------------- -----------------------------------

## Example for GET direct_messages/events/list
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "event": {
    "type": "message_create",
    "id": "854103000570187779",
    "created_timestamp": "1492468998459",
    "message_create": {
      "target": {
        "recipient_id": "3340250004"
      },
      "sender_id": "51378538",
      "source_app_id": "268278",
      "message_data": {
        "text": "Hello",
        "entities": {
          "hashtags": [],
          "symbols": [],
          "user_mentions": [],
          "urls": []
        }
      }
    }
  }
  "apps": {
    "268278": {
      "id": "268278",
      "name": "Twitter Web Client",
      "url": "http://twitter.com"
    }
  }
}
    
```
:::
:::
:::

::: c01-rich-text-editor
## Example for GET direct_messages/events/show
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "events": [
    {
      "type": "message_create",
      "id": "854103000570187779",
      "created_timestamp": "1492468998459",
      "message_create": {
        "target": {
          "recipient_id": "3340250004"
        },
        "sender_id": "51378538",
        "source_app_id": "268278",
        "message_data": {
          "text": "Hello",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
          }
        }
      }
    },
    {
      "type": "message_create",
      "id": "867807494898188291",
      "created_timestamp": "1495736404524",
      "message_create": {
        "target": {
          "recipient_id": "3340250004"
        },
        "sender_id": "51378538",
        "source_app_id": "9206597",
        "message_data": {
          "text": "World",
          "entities": {
            "hashtags": [],
            "symbols": [],
            "user_mentions": [],
            "urls": []
          }
        }
      }
    },
  ],
  "apps": {
    "9206597": {
      "id": "9206597",
      "name": "BeeToSeaBiz TestApp Awesome",
      "url": "https://twitter.com/beetoseabiz"
    },
    "268278": {
      "id": "268278",
      "name": "Twitter Web Client",
      "url": "http://twitter.com"
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
