::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Creates a Tweet on behalf of an authenticated user.

### Endpoint URL

` https://api.twitter.com/2/tweets `

+-----------------------+-----------------------+-----------------------+
| Name                  | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| ` direct              | string                | [Tweets a link        |
| _message_deep_link `\ |                       | directly to a Direct  |
| [Optional]{.small}    |                       | Message               |
|                       |                       | conversation](ht      |
|                       |                       | tps://business.twitte |
|                       |                       | r.com/en/help/campaig |
|                       |                       | n-editing-and-optimiz |
|                       |                       | ation/public-to-priva |
|                       |                       | te-conversation.html) |
|                       |                       | with an account.      |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"te                |
|                       |                       | xt": "Tweeting a DM d |
|                       |                       | eep link!", "direct_m |
|                       |                       | essage_deep_link": "h |
|                       |                       | ttps://twitter.com/me |
|                       |                       | ssages/compose?recipi |
|                       |                       | ent_id=2244994945"} ` |
+-----------------------+-----------------------+-----------------------+
| ` for_su              | boolean               | Allows you to Tweet   |
| per_followers_only `\ |                       | exclusively for       |
| [Optional]{.small}    |                       | [Super                |
|                       |                       | Foll                  |
|                       |                       | owers](https://help.t |
|                       |                       | witter.com/en/using-t |
|                       |                       | witter/super-follows) |
|                       |                       | .                     |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "Hello Wo  |
|                       |                       | rld!", "for_super_fol |
|                       |                       | lowers_only": true} ` |
+-----------------------+-----------------------+-----------------------+
| ` geo `\              | object                | A JSON object that    |
| [Optional]{.small}    |                       | contains location     |
|                       |                       | information for a     |
|                       |                       | Tweet. You can only   |
|                       |                       | add a location to     |
|                       |                       | Tweets if you have    |
|                       |                       | geo enabled in your   |
|                       |                       | profile settings. If  |
|                       |                       | you don\'t have geo   |
|                       |                       | enabled, you can      |
|                       |                       | still add a location  |
|                       |                       | parameter in your     |
|                       |                       | request body, but it  |
|                       |                       | won\'t get attached   |
|                       |                       | to your Tweet         |
+-----------------------+-----------------------+-----------------------+
| ` geo.place_id `\     | string                | Place ID being        |
| [Optional]{.small}    |                       | attached to the Tweet |
|                       |                       | for geo location.     |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text":            |
|                       |                       | "Tweeting with geo!", |
|                       |                       | "geo": {"place_id": " |
|                       |                       | 5a110d312052166f"}} ` |
+-----------------------+-----------------------+-----------------------+
| ` media `\            | object                | A JSON object that    |
| [Optional]{.small}    |                       | contains media        |
|                       |                       | information being     |
|                       |                       | attached to created   |
|                       |                       | Tweet. This is        |
|                       |                       | mutually exclusive    |
|                       |                       | from Quote Tweet ID   |
|                       |                       | and Poll.             |
+-----------------------+-----------------------+-----------------------+
| ` media.media_ids `\  | array                 | A list of Media IDs   |
| [Optional]{.small}    |                       | being attached to the |
|                       |                       | Tweet. This is only   |
|                       |                       | required if the       |
|                       |                       | request includes the  |
|                       |                       | ` tagged_user_ids ` . |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | `                     |
|                       |                       |  {"text": "Tweeting w |
|                       |                       | ith media!", "media": |
|                       |                       |  {"media_ids": ["1455 |
|                       |                       | 952740635586573"]}} ` |
+-----------------------+-----------------------+-----------------------+
| ` med                 | array                 | A list of User IDs    |
| ia.tagged_user_ids `\ |                       | being tagged in the   |
| [Optional]{.small}    |                       | Tweet with Media. If  |
|                       |                       | the user you\'re      |
|                       |                       | tagging doesn\'t have |
|                       |                       | photo-tagging         |
|                       |                       | enabled, their names  |
|                       |                       | won\'t show up in the |
|                       |                       | list of tagged users  |
|                       |                       | even though the Tweet |
|                       |                       | is successfully       |
|                       |                       | created.              |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text              |
|                       |                       | ": "Tagging users in  |
|                       |                       | images!", "media": {" |
|                       |                       | media_ids": ["1455952 |
|                       |                       | 740635586573"], "tagg |
|                       |                       | ed_user_ids": ["22449 |
|                       |                       | 94945","6253282"]}} ` |
+-----------------------+-----------------------+-----------------------+
| ` poll `\             | object                | A JSON object that    |
| [Optional]{.small}    |                       | contains options for  |
|                       |                       | a Tweet with a poll.  |
|                       |                       | This is mutually      |
|                       |                       | exclusive from Media  |
|                       |                       | and Quote Tweet ID.   |
+-----------------------+-----------------------+-----------------------+
| ` pol                 | number                | Duration of the poll  |
| l.duration_minutes `\ |                       | in minutes for a      |
| [Optional]{.small}    |                       | Tweet with a poll.    |
|                       |                       | This is only required |
|                       |                       | if the request        |
|                       |                       | includes              |
|                       |                       | ` poll.options ` .    |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | `                     |
|                       |                       |  {"text": "Tweeting w |
|                       |                       | ith polls!", "poll":  |
|                       |                       | {"options": ["yes", " |
|                       |                       | maybe", "no"], "durat |
|                       |                       | ion_minutes": 120}} ` |
+-----------------------+-----------------------+-----------------------+
| ` poll.options `\     | array                 | A list of poll        |
| [Optional]{.small}    |                       | options for a Tweet   |
|                       |                       | with a poll. For the  |
|                       |                       | request to be         |
|                       |                       | successful it must    |
|                       |                       | also include          |
|                       |                       | ` duration_minutes `  |
|                       |                       | too.                  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | `                     |
|                       |                       | {"text": "Tweeting wi |
|                       |                       | th polls!", "poll": { |
|                       |                       | "options": ["yes", "m |
|                       |                       | aybe", "no"], "durati |
|                       |                       | on_minutes": 120}}" ` |
+-----------------------+-----------------------+-----------------------+
| ` quote_tweet_id `\   | string                | Link to the Tweet     |
| [Optional]{.small}    |                       | being quoted.         |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "Yay!",    |
|                       |                       | "quote_tweet_id": "14 |
|                       |                       | 55953449422516226"} ` |
+-----------------------+-----------------------+-----------------------+
| ` reply `\            | object                | A JSON object that    |
| [Optional]{.small}    |                       | contains information  |
|                       |                       | of the Tweet being    |
|                       |                       | replied to.           |
+-----------------------+-----------------------+-----------------------+
| ` reply.excl          | array                 | A list of User IDs to |
| ude_reply_user_ids `\ |                       | be excluded from the  |
| [Optional]{.small}    |                       | reply Tweet thus      |
|                       |                       | removing a user from  |
|                       |                       | a thread.             |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "          |
|                       |                       | Yay!", "reply": {"in_ |
|                       |                       | reply_to_tweet_id": " |
|                       |                       | 1455953449422516226", |
|                       |                       |  "exclude_reply_user_ |
|                       |                       | ids": ["6253282"]}} ` |
+-----------------------+-----------------------+-----------------------+
| ` reply.in            | string                | Tweet ID of the Tweet |
| _reply_to_tweet_id `\ |                       | being replied to.     |
| [Optional]{.small}    |                       | Please note that      |
|                       |                       | ` i                   |
|                       |                       | n_reply_to_tweet_id ` |
|                       |                       | needs to be in the    |
|                       |                       | request if            |
|                       |                       | ` exc                 |
|                       |                       | lude_reply_user_ids ` |
|                       |                       | is present.           |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "Excited   |
|                       |                       | !", "reply": {"in_rep |
|                       |                       | ly_to_tweet_id": "145 |
|                       |                       | 5953449422516226"}} ` |
+-----------------------+-----------------------+-----------------------+
| ` reply_settings `\   | string                | [Settings]            |
| [Optional]{.small}    |                       | (https://blog.twitter |
|                       |                       | .com/en_us/topics/pro |
|                       |                       | duct/2020/new-convers |
|                       |                       | ation-settings-coming |
|                       |                       | -to-a-tweet-near-you) |
|                       |                       | to indicate who can   |
|                       |                       | reply to the Tweet.   |
|                       |                       | Options include       |
|                       |                       | \"mentionedUsers\"    |
|                       |                       | and \"following\". If |
|                       |                       | the field isn't       |
|                       |                       | specified, it will    |
|                       |                       | default to everyone.  |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"text": "Tweeti    |
|                       |                       | ng with reply setting |
|                       |                       | s!", "reply_settings" |
|                       |                       | : "mentionedUsers"} ` |
+-----------------------+-----------------------+-----------------------+
| ` text `\             | string                | Text of the Tweet     |
| [Optional]{.small}    |                       | being created. This   |
|                       |                       | field is required if  |
|                       |                       | ` media.media_ids `   |
|                       |                       | is not present.       |
|                       |                       |                       |
|                       |                       | Example:              |
|                       |                       | ` {"tex               |
|                       |                       | t": "Hello World!"} ` |
+-----------------------+-----------------------+-----------------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
  ---------- -------- --------------------------------------
  Name       Type     Description
  ` id `     string   The ID of the newly created Tweet.
  ` text `   string   The text of the newly created Tweet.
  ---------- -------- --------------------------------------
:::
:::
:::
