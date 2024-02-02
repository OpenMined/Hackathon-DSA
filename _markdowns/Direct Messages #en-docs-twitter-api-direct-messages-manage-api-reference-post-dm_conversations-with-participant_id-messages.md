::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Creates a one-to-one Direct Message and adds it to the one-to-one
conversation. This method either creates a new one-to-one conversation
or retrieves the current conversation and adds the Direct Message to it.

### Endpoint URL

` https://api.twitter.com/2/dm_conversations/with/:participant_id/messages `

  ----------------------- ----------------------- -----------------------
  Name                    Type                    Description

  ` participant_id `\     string                  The User ID of the
  [Required]{.small}                              account this one-to-one
                                                  Direct Message is to be
                                                  sent to.
  ----------------------- ----------------------- -----------------------

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
|                       |                       | ` {"text"             |
|                       |                       | : "Hello just you"} ` |
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
