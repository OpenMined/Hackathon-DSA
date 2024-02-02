::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Creates a Direct Message on behalf of an authenticated user, and adds it
to the specified conversation.

### Endpoint URL

` https://api.twitter.com/2/dm_conversations/:dm_conversation_id/messages `

  ------------------------- ----------------------- ------------------------
  Name                      Type                    Description

  ` dm_conversation_id `\   string                  The
  [Required]{.small}                                ` dm_conversation_id `
                                                    of the conversation to
                                                    add the Direct Message
                                                    to. Supports both 1-1
                                                    and group conversations.
  ------------------------- ----------------------- ------------------------

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` attachments `\      | array                 | A single Media ID     |
| [Optional]{.small}    |                       | being attached to the |
|                       |                       | Direct Message. This  |
|                       |                       | field is required if  |
|                       |                       | ` text ` is not       |
|                       |                       | present. For this     |
|                       |                       | launch, only 1        |
|                       |                       | attachment is         |
|                       |                       | supported.            |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text"             |
|                       |                       | : "Sending a DM with  |
|                       |                       | media!", "attachments |
|                       |                       | ": [{"media_id": "145 |
|                       |                       | 5952740635586573"}] ` |
+-----------------------+-----------------------+-----------------------+
| ` text `\             | string                | Text of the Direct    |
| [Optional]{.small}    |                       | Message being         |
|                       |                       | created. This field   |
|                       |                       | is required if        |
|                       |                       | ` attachments ` is    |
|                       |                       | not present. Text     |
|                       |                       | messages support up   |
|                       |                       | to 10,000 characters. |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "Hell      |
|                       |                       | o just you conversati |
|                       |                       | on participants!""} ` |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ------------------------ -------- -----------------------------------------------------------------------------------------
  Name                     Type     Description
  ` dm_conversation_id `   string   Contains the ` id ` of the Direct Message conversation the Direct Message was added to.
  ` dm_event_id `          string   Contains the ` id ` of the event created by this request.
  ------------------------ -------- -----------------------------------------------------------------------------------------
:::
:::
:::
