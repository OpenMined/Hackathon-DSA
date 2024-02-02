::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Locations can be attached to Direct Messages created with [POST
direct_messages/events/new](https://dev.twitter.com/rest/reference/post/direct_messages/events/new)
. The location is defined as an attachement object with longitue and
latitude coordinates or a Twitter place.\

## Example message with shared coordinate attachment
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "event": {
    "type": "message_create",
    "message_create": {
      "target": {
        "recipient_id": "844385345234"
      },
      "message_data": {
        "text": "Here's my location",
        "attachment": {
          "type": "location",
          "location": {
            "type": "shared_coordinate",
            "shared_coordinate": {
              "coordinates": {
                "type": "Point",
                "coordinates": [-122.443893, 37.771718]
              }
            }
          }
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
## Example message with shared place attachment
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
  "event": {
    "type": "message_create",
      "message_create": {
        "target": {
          "recipient_id": "844385345234"
        },
        "message_data": {
          "text": "Here's my location",
          "attachment": {
            "type": "location",
            "location": {
              "type": "shared_place",
              "shared_place": {
                "place": {
                  "id": "123456"
                }
              }
            }
          }
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
:::
:::
