::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Spaces allow expression and interaction via live audio conversations.
The Space data dictionary contains relevant metadata about a Space; all
the details are updated in real time.

User objects can found and expanded in the user resource. These objects
are available for expansion by adding at least one of [ host_ids
]{.code-inline} , [ creator_id ]{.code-inline} , [ speaker_ids
]{.code-inline} , [ mentioned_user_ids ]{.code-inline} to the [
expansions ]{.code-inline} query parameter.

Unlike Tweets, Spaces are ephemeral and become unavailable after they
end or when they are canceled by their creator. When your app handles
Spaces data, you are responsible for returning the most up-to-date
information, and must remove data that is no longer available from the
platform. The [Spaces lookup
endpoints](/en/docs/twitter-api/spaces/lookup/introduction) can help you
ensure you respect the users' expectations and intent.

+-----------------+-----------------+-----------------+-----------------+
| Field value     | Type            | Description     | How it can be   |
|                 |                 |                 | used            |
+-----------------+-----------------+-----------------+-----------------+
| id (default)    | string          | The unique      | Uniquely        |
|                 |                 | identifier of   | identify a      |
|                 |                 | the requested   | Space returned  |
|                 |                 | Space.          | in the          |
|                 |                 |                 | response.       |
|                 |                 | ` "id": "1      |                 |
|                 |                 | zqKVXPQhvZJB" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| state (default) | string          | Indicates if    | Filter live or  |
|                 |                 | the Space has   | scheduled       |
|                 |                 | started or will | Spaces.         |
|                 |                 | start in the    |                 |
|                 |                 | future, or if   |                 |
|                 |                 | it has ended.   |                 |
|                 |                 |                 |                 |
|                 |                 | ` "s            |                 |
|                 |                 | tate": "live" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \               |                 |
+-----------------+-----------------+-----------------+-----------------+
| created_at      | date (ISO 8601) | Creation time   | Understand when |
|                 |                 | of this Space.  | a Space was     |
|                 |                 |                 | first created   |
|                 |                 | ` "created_at"  | and sort Spaces |
|                 |                 | : "2021-07-04T2 | by creation     |
|                 |                 | 3:12:08.000Z" ` | time.           |
+-----------------+-----------------+-----------------+-----------------+
| ended_at        | date (ISO 8601) | Time when the   | Understand when |
|                 |                 | Space was       | a live Space    |
|                 |                 | ended. Only     | ended in order  |
|                 |                 | available for   | to comput its   |
|                 |                 | ended Spaces.   | runtime         |
|                 |                 |                 | duration.       |
|                 |                 | ` "ended_at"    |                 |
|                 |                 | : "2021-07-04T0 |                 |
|                 |                 | 0:11:44.000Z" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| host_ids        | array           | The unique      | Expand User     |
|                 |                 | identifier of   | objects,        |
|                 |                 | the users who   | understand      |
|                 |                 | are hosting     | engagement.     |
|                 |                 | this Space.     |                 |
|                 |                 |                 |                 |
|                 |                 | ` "             |                 |
|                 |                 | host_ids": [ `\ |                 |
|                 |                 | ` "224499494    |                 |
|                 |                 | 5", "6253282" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \]              |                 |
+-----------------+-----------------+-----------------+-----------------+
| lang            | string          | Language of the | Classify Spaces |
|                 |                 | Space, if       | by inferred     |
|                 |                 | detected by     | language.       |
|                 |                 | Twitter.        |                 |
|                 |                 | Returned as a   |                 |
|                 |                 | BCP47 language  |                 |
|                 |                 | tag.            |                 |
|                 |                 |                 |                 |
|                 |                 | `               |                 |
|                 |                 |  "lang": "en" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| is_ticketed     | boolean         | Indicates is    | Create user     |
|                 |                 | this is a       | experiences to  |
|                 |                 | ticketed Space. | highlight       |
|                 |                 |                 | content of      |
|                 |                 | ` "is_tic       | interest.       |
|                 |                 | keted": false ` |                 |
|                 |                 |                 |                 |
|                 |                 | \               |                 |
+-----------------+-----------------+-----------------+-----------------+
| i               | array           | The list of     | Expand User     |
| nvited_user_ids |                 | user IDs that   | objects,        |
|                 |                 | were invited to | understand      |
|                 |                 | join as         | engagement.     |
|                 |                 | speakers.       |                 |
|                 |                 | Usually, users  |                 |
|                 |                 | in this list    |                 |
|                 |                 | are invited to  |                 |
|                 |                 | speak via the   |                 |
|                 |                 | Invite user     |                 |
|                 |                 | option.         |                 |
|                 |                 |                 |                 |
|                 |                 | ` "men          |                 |
|                 |                 | tioned_user_ids |                 |
|                 |                 | ": [ "224499494 |                 |
|                 |                 | 5", "6253282" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \]              |                 |
+-----------------+-----------------+-----------------+-----------------+
| pa              | integer         | The current     | Understand      |
| rticipant_count |                 | number of users | engagement, and |
|                 |                 | in the Space,   | create reports  |
|                 |                 | including Hosts | and             |
|                 |                 | and Speakers.   | visualizations  |
|                 |                 |                 | for creators.   |
|                 |                 | ` "participan   |                 |
|                 |                 | t_count": 420 ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| s               | integer         | The number of   | Understand how  |
| ubscriber_count |                 | people who set  | many people are |
|                 |                 | a reminder to a | interested in   |
|                 |                 | Space.\         | attending the   |
|                 |                 | ` "subscribe    | event. This     |
|                 |                 | r_count": 36 `\ | metric is       |
|                 |                 |                 | available for   |
|                 |                 |                 | scheduled       |
|                 |                 |                 | Spaces and      |
|                 |                 |                 | Spaces          |
|                 |                 |                 | scheduled in    |
|                 |                 |                 | the past that   |
|                 |                 |                 | are currently   |
|                 |                 |                 | live.           |
+-----------------+-----------------+-----------------+-----------------+
| scheduled_start | date (ISO 8601) | Indicates the   | Integrate with  |
|                 |                 | start time of a | calendar        |
|                 |                 | scheduled       | notifications,  |
|                 |                 | Space, as set   | filter and sort |
|                 |                 | by the creator  | Spaces by time. |
|                 |                 | of the Space.   |                 |
|                 |                 | This field is   |                 |
|                 |                 | returned only   |                 |
|                 |                 | if the Space    |                 |
|                 |                 | has been        |                 |
|                 |                 | scheduled; in   |                 |
|                 |                 | other words, if |                 |
|                 |                 | the field is    |                 |
|                 |                 | returned, it    |                 |
|                 |                 | means the Space |                 |
|                 |                 | is a scheduled  |                 |
|                 |                 | Space.          |                 |
|                 |                 |                 |                 |
|                 |                 | ` "s            |                 |
|                 |                 | cheduled_start" |                 |
|                 |                 | : "2021-07-14T0 |                 |
|                 |                 | 8:00:00.000Z" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| speaker_ids     | array           | The list of     | Expand User     |
|                 |                 | users who were  | objects,        |
|                 |                 | speaking at any | understand      |
|                 |                 | point during    | engagement.     |
|                 |                 | the Space. This |                 |
|                 |                 | list contains   |                 |
|                 |                 | all the users   |                 |
|                 |                 | in **[          |                 |
|                 |                 | i               |                 |
|                 |                 | nvited_user_ids |                 |
|                 |                 | ]{              |                 |
|                 |                 | .code-inline}** |                 |
|                 |                 | in addition to  |                 |
|                 |                 | any user who    |                 |
|                 |                 | requested to    |                 |
|                 |                 | speak and was   |                 |
|                 |                 | allowed via the |                 |
|                 |                 | Add speaker     |                 |
|                 |                 | option.         |                 |
|                 |                 |                 |                 |
|                 |                 | ` "speaker_ids  |                 |
|                 |                 | ": [ "224499494 |                 |
|                 |                 | 5", "6253282" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \]              |                 |
+-----------------+-----------------+-----------------+-----------------+
| started_at      | date (ISO 8601) | Indicates the   | Determine start |
|                 |                 | actual start    | time of a       |
|                 |                 | time of a       | Space.          |
|                 |                 | Space.          |                 |
|                 |                 |                 |                 |
|                 |                 | ` "started_at"  |                 |
|                 |                 | : "2021-07-14T0 |                 |
|                 |                 | 8:00:12.000Z" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| title           | string          | The title of    | Determine the   |
|                 |                 | the Space as    | title of a      |
|                 |                 | specified by    | Space,          |
|                 |                 | the creator.    | understand      |
|                 |                 |                 | referenced      |
|                 |                 | ` "ti           | keywords,       |
|                 |                 | tle": "Say hell | hashtags, and   |
|                 |                 | o to the Space  | mentions.       |
|                 |                 | data object!" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| topic_ids       | array           | A list of IDs   | Determine the   |
|                 |                 | of the topics   | title of a      |
|                 |                 | selected by the | Space,          |
|                 |                 | creator of the  | understand      |
|                 |                 | Space.          | referenced      |
|                 |                 |                 | keywords,       |
|                 |                 | ` "topic_ids    | hashtags, and   |
|                 |                 | ": [ "224499494 | mentions.       |
|                 |                 | 5", "6253282" ` |                 |
|                 |                 |                 |                 |
|                 |                 | \]              |                 |
+-----------------+-----------------+-----------------+-----------------+
| updated_at      | date (ISO 8601) | Specifies the   | Keep            |
|                 |                 | date and time   | information up  |
|                 |                 | of the last     | to date.        |
|                 |                 | update to any   |                 |
|                 |                 | of the Space\'s |                 |
|                 |                 | metadata, such  |                 |
|                 |                 | as its title or |                 |
|                 |                 | scheduled       |                 |
|                 |                 | time.\          |                 |
|                 |                 | \               |                 |
|                 |                 | `"updated_at"   |                 |
|                 |                 | : "2021-07-11T1 |                 |
|                 |                 | 4:44:44.000Z" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the following request, we are requesting fields for the Space on the
[Spaces lookup](/en/docs/twitter-api/spaces/lookup/introduction.html)
endpoint. Be sure to replace ` $BEARER_TOKEN ` with your own generated
[Bearer Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl "https://api.twitter.com/2/spaces/1DXxyRYNejbKM?space.fields=created_at,creator_id,created_athost_ids,lang,is_ticketed,invited_user_ids,participant_count,scheduled_start,speaker_ids,started_at,state,title,updated_at&expansions=creator_id,host_ids,invited_user_ids,speaker_ids" --header "Authorization: Bearer $BEARER_TOKEN"
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": {
        "id": "1zqKVXPQhvZJB",
        "state": "live",
        "created_at": "2021-07-04T23:12:08.000Z",
        "host_ids": [
          "2244994945",
          "6253282"
        ],
        "lang": "en",
        "is_ticketed": false,
        "invited_user_ids": [
          "2244994945",
          "6253282"
        ],
        "participant_count": 420,
        "scheduled_start": "2021-07-14T08:00:00.000Z",
        "speaker_ids": [
          "2244994945",
          "6253282"
        ],        
        "started_at": "2021-07-14T08:00:12.000Z",
        "title": "Say hello to the Space data object!",
        "updated_at": "2021-07-11T14:44:44.000Z"
    },
    "includes": {
        "users": [
            {
                "id": "2244994945",
                "name": "Twitter Dev",
                "username": "TwitterDev"
           },
           {
            "id": "6253282",
            "name": "Twitter API",
            "username": "TwitterAPI"
          }
    ]
    }
}
    
```
:::
:::
:::
:::
