::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Creates a new group conversation and adds a Direct Message to it on
behalf of an authenticated user.

### Endpoint URL

` https://api.twitter.com/2/dm_conversations `

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| `                     | string                | The                   |
|  conversation_type `\ |                       | ` conversation_type ` |
| [Required]{.small}    |                       | attribute must be set |
|                       |                       | to \"Group\" (case    |
|                       |                       | sensitive).           |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"conversat         |
|                       |                       | ion_type": "Group"} ` |
+-----------------------+-----------------------+-----------------------+
| ` message `\          | object                | A JSON object that    |
| [Required]{.small}    |                       | contains either or    |
|                       |                       | both the ` text ` and |
|                       |                       | ` attachments `       |
|                       |                       | parameters.           |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"me                |
|                       |                       | ssage": {text": "Hell |
|                       |                       | o just you conversati |
|                       |                       | on participants!"}} ` |
+-----------------------+-----------------------+-----------------------+
| ` participant_ids `\  | array                 | An array of User IDs  |
| [Required]{.small}    |                       | that the conversation |
|                       |                       | is created with.      |
|                       |                       | Conversations can     |
|                       |                       | have up to 50         |
|                       |                       | participants.         |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"participant_i     |
|                       |                       | ds": ["944480690","90 |
|                       |                       | 6948460078698496"]} ` |
+-----------------------+-----------------------+-----------------------+
| ` m                   | array                 | A single Media ID     |
| essage.attachments `\ |                       | being attached to the |
| [Optional]{.small}    |                       | Direct Message. This  |
|                       |                       | field is required if  |
|                       |                       | ` message.text ` is   |
|                       |                       | not present. For this |
|                       |                       | launch, only 1        |
|                       |                       | attachment is         |
|                       |                       | supported.            |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | `                     |
|                       |                       |  {"message": {"text": |
|                       |                       |  "Sending a DM with m |
|                       |                       | edia!", "attachments" |
|                       |                       | : [{"media_id": "1455 |
|                       |                       | 952740635586573"}]} ` |
+-----------------------+-----------------------+-----------------------+
| ` message.text `\     | string                | Text of the Direct    |
| [Optional]{.small}    |                       | Message being         |
|                       |                       | created. This field   |
|                       |                       | is required if        |
|                       |                       | `                     |
|                       |                       | message.attachments ` |
|                       |                       | is not present. Text  |
|                       |                       | messages support up   |
|                       |                       | to 10,000 characters. |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"mes               |
|                       |                       | sage": {"text": "Hell |
|                       |                       | o just you conversati |
|                       |                       | on participants!"}} ` |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ------------------------ -------- ---------------------------------------------------------
  Name                     Type     Description
  ` dm_conversation_id `   string   Contains ` id ` of the DM conversation.
  ` dm_event_id `          string   Contains ` id ` of the event sent in this conversation.
  ------------------------ -------- ---------------------------------------------------------
:::
:::
:::
