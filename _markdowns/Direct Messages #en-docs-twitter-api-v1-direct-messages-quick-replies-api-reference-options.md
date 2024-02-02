<div>

::: c01-rich-text-editor
List of up to 20 predefined options presented for a user to choose from.
For use with [POST direct_messages/events/new
(message_create)](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
.

## Quick Reply Object [¶](#quick-reply-object){.headerlink}

  ----------------------------------- ----------------------------------
  **quick_reply.type** (required)     Must be set to ` options `
  **quick_reply.option** (required)   An array of ` options ` objects.
  ----------------------------------- ----------------------------------

## Option Object [¶](#option-object){.headerlink}

  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **label** (required)         The text label displayed on the button face. Label text is returned as the user\'s message response. String, max length of 36 characters including spaces. Values with URLs are not allowed and will return an error.
  **description** (optional)   Optional description text displayed under label text. All options must have this property defined if property is present in any option. Text is auto-wrapped and will display on a max of two lines and supports ` n ` for controlling line breaks. Description text is not include in the user\'s message response. String, max length of 72 characters including spaces.
  **metadata** (optional)      Metadata that will be sent back in the webhook request. String, max length of 1,000 characters including spaces.
  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

Although not required, if one option defines the ` description ` , then
all ` options ` must contain the ` description ` .

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "What's your favorite type of bird?",
            "quick_reply": {
              "type": "options",
              "options": [
                {
                  "label": "Red Bird",
                  "description": "A description about the red bird.",
                  "metadata": "external_id_1"
                },
                {
                  "label": "Blue Bird",
                  "description": "A description about the blue bird.",
                  "metadata": "external_id_2"
                },
                {
                  "label": "Black Bird",
                  "description": "A description about the black bird.",
                  "metadata": "external_id_3"
                },
                {
                  "label": "White Bird",
                  "description": "A description about the white bird.",
                  "metadata": "external_id_4"
                }
              ]
            }
          }
        }
      }
    }

## Example User Response [¶](#example-user-response){.headerlink}

The ` type ` and ` metadata ` will be present in the
` quick_reply_response ` object. The ` label ` for the chosen option is
sent as the message ` text ` .

    {
      "event": {
        "type": "message_create",
        "id": "1234858592",
        "created_timestamp": "1392078023603",
        "message_create": {
          "target": {
            "recipient_id": "1234858592"
          },
          "sender_id": "3805104374",
          "message_data": {
            "text": "Blue Bird",
            "entities": {
              "hashtags": [],
              "symbols": [],
              "urls": [],
              "user_mentions": []
            },
            "quick_reply_response": {
              "type": "options",
              "metadata": "external_id_2"
            }
          }
        }
      }
    }
:::

</div>
