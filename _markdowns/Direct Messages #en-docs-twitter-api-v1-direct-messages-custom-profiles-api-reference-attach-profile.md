<div>

::: c01-rich-text-editor
To attach a custom profile to a Direct Message add a
` event.custom_profile_id ` parameter to the [POST
direct_messages/events/new.json](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
request.

*Note:* See [full
documentation](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
for all properties. Custom profiles can also be used with [welcome
messages](/en/docs/direct-messages/welcome-messages/overview) .

## Parameters [¶](#parameters){.headerlink}

  ----------------------------- ----------------------------------------------------------------------
  **event.custom_profile_id**   The string ID of the custom profile to attach to the Direct Message.
  ----------------------------- ----------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Hi, my name is Jon. How can I help?",
          },
          "custom_profile_id": "100001"
        }
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d ' { "event": { "type": "message_create", "message_create": { "target": { "recipient_id": "844385345234" }, "message_data": { "text": "Hi, my name is Jon. How can I help?", }, "custom_profile_id": "100001" } } }'

## Example Response [¶](#example-response){.headerlink}

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "sender_id": "1241124",
          "message_data": {
            "text": "Hi, my name is Jon. How can I help?",
          },
          "custom_profile_id":  "100001"
        }
      }
    }
:::

</div>
