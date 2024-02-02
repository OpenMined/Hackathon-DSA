<div>

::: c01-rich-text-editor
Publishes a new ` message_create ` event resulting in a Direct Message
sent to a specified user from the authenticating user. Returns an event
if successful. Supports publishing Direct Messages with optional Quick
Reply and media attachment. Replaces behavior currently provided by
[POST
direct_messages/new](/en/docs/direct-messages/sending-and-receiving/api-reference/new-message)
.

Requires a JSON POST body and ` Content-Type ` header to be set to
` application/json ` . Setting ` Content-Length ` may also be required
if it is not automatically.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/events/new.json `

  --------------------------- ------------------------------
  Response formats            JSON
  Content-Type                application/json
  Requires authentication?    Yes (user context only)
  Rate limited?               Yes
  Requests / 24-hour window   1000 per user; 15000 per app
  --------------------------- ------------------------------

## Direct Message Rate Limiting [¶](#direct-message-rate-limiting){.headerlink}

When a message is received from a user you may send up to 5 messages in
response within a 24 hour window. Each message received resets the 24
hour window and the 5 allotted messages. Sending a 6th message within a
24 hour window or sending a message outside of a 24 hour window will
count towards rate-limiting. This behavior only applies when using the
POST direct_messages/events/new endpoint.

## Event Object [¶](#event-object){.headerlink}

  --------------------------------------------------- --------------------------------------------------------------------------------
  **type** (required)                                 The type of event you are posting. For Direct Messages, use ` message_create `
  **message_create.target.recipient_id** (required)   The ID of the user who should receive the direct message.
  **message_create.message_data** (required)          The ` Message Data Object ` defining the content to deliver to the reciepient.
  --------------------------------------------------- --------------------------------------------------------------------------------

## Message Data Object [¶](#message-data-object){.headerlink}

+-----------------------------------+-----------------------------------+
| **text** (required)               | The text of your Direct Message.  |
|                                   | URL encode as necessary. Max      |
|                                   | length of 10,000 characters. Max  |
|                                   | length of 9,990 characters if     |
|                                   | used as a [Welcome                |
|                                   | Message](/en/docs/d               |
|                                   | irect-messages/welcome-messages/a |
|                                   | pi-reference/new-welcome-message) |
|                                   | .                                 |
+-----------------------------------+-----------------------------------+
| **quick_reply.type** (optional)   | The Quick Reply type to present   |
|                                   | to the user (example requests     |
|                                   | below):                           |
|                                   |                                   |
|                                   | -   **options** - Array of        |
|                                   |     ` Options ` objects (20 max). |
+-----------------------------------+-----------------------------------+
| **attachment.type** (optional)    | The attachment type. Can be media |
|                                   | or location.                      |
+-----------------------------------+-----------------------------------+
| **attachment.media.id**           | A media id to associate with the  |
| (optional)                        | message. A Direct Message may     |
|                                   | only reference a single media_id. |
|                                   | See [Uploading                    |
|                                   | Media](/e                         |
|                                   | n/docs/direct-messages/message-at |
|                                   | tachments/guides/attaching-media) |
|                                   | for further details on uploading  |
|                                   | media.                            |
+-----------------------------------+-----------------------------------+

**Note**

See [Attaching Media to Direct
Messages](/en/docs/direct-messages/message-attachments/guides/attaching-media)
for details on including an image, GIF or video in Direct Messages.

### Example request [¶](#example-request){.headerlink}

    curl --request POST 
    --url https://api.twitter.com/1.1/direct_messages/events/new.json 
    --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
    --header 'content-type: application/json' 
    --data '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'

## Example Response [¶](#example-response){.headerlink}

    {
    "event": {
      "type": "message_create",
      "message_create": {
        "target": {
          "recipient_id": "RECIPIENT_USER_ID"
        },
        "message_data": {
          "text": "Hello World!",
        }
      }
    }
    }

**Note**

See
[media/entity](/en/docs/tweets/data-dictionary/overview/entities-object1)
documentation for details on returned media object properties.
:::

</div>
