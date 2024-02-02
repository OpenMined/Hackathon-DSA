::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Creates a new Welcome Message that will be stored and sent in the future
from the authenticating user in defined circumstances. Returns the
message template if successful. Supports publishing with the same
elements as Direct Messages (e.g. Quick Replies, media attachments).

Requires a JSON POST body and ` Content-Type ` header to be set to
` application/json ` . Setting ` Content-Length ` may also be required
if it is not automatically.

See the [Welcome Messages
overview](/en/docs/direct-messages/welcome-messages/overview) to learn
how to work with Welcome Messages.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/new.json `

  -------------------------- -------------------------
  Response formats           JSON
  Content-Type               application/json
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Welcome Message Object [¶](#welcome-message-object){.headerlink}

  ----------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **message_data** (required)   The ` Message Data Object ` defining the content of the message template. See [POST direct_messages/events/new (message_create)](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event) for Message Data object details.
  **name** (optional)           A human readable name for the Welcome Message. This is not displayed to the user. Max length of 100 alpha numeric characters including hyphens, underscores, spaces, hashes and at signs.
  ----------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> **Note**
>
> See [Attaching Media to Direct
> Messages](/en/docs/direct-messages/message-attachments/guides/attaching-media)
> for details on including an image, GIF or video in Direct Messages.

## Example Request [¶](#example-request){.headerlink}

    {
      "welcome_message" : {
        "name": "simple_welcome-message 01",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              "id": "48909183894931"
            }
          }
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -A 'Content-type: application/json' /1.1/direct_messages/welcome_messages/new.json -d '{"name": "simple_welcome-message 01", "welcome_message": {"message_data": {"text": "Welcome!", "attachment": {"type": "media", "media": {"id": "48909183894931"}}}}}'

## Example Response [¶](#example-response){.headerlink}

    {
      "welcome_message" : {
        "id": "844385345234",
        "created_timestamp": "1470182274821",
        "message_data": {
          "text": "Welcome!",
          "attachment": {
            "type": "media",
            "media": {
              ...
            }
          }
        }
      }
      "name": "simple_welcome-message 01"
    }
:::
:::
:::
:::
:::
:::
:::
