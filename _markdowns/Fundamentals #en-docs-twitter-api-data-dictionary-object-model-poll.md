::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
A poll included in a Tweet is not a primary object on any endpoint, but
can be found and expanded in the Tweet object.

The object is available for expansion with
` ?expansions=attachments.poll_ids ` to get the condensed object with
only default fields. Use the expansion with the field parameter:
` poll.fields ` when requesting additional fields to complete the
object.

+-----------------------+-----------------------+-----------------------+
| Field value           | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| id (default)          | string                | Unique identifier of  |
|                       |                       | the expanded poll.    |
|                       |                       |                       |
|                       |                       | ` "id": "1            |
|                       |                       | 199786642791452673" ` |
+-----------------------+-----------------------+-----------------------+
| options (default)     | array                 | Contains objects      |
|                       |                       | describing each       |
|                       |                       | choice in the         |
|                       |                       | referenced poll.      |
|                       |                       |                       |
|                       |                       | `                     |
|                       |                       |  "options": [ { "posi |
|                       |                       | tion": 1, "label": "“ |
|                       |                       | C Sharp”", "votes": 7 |
|                       |                       | 95 }, { "position": 2 |
|                       |                       | , "label": "“C Hashta |
|                       |                       | g”", "votes": 156 } ` |
|                       |                       |                       |
|                       |                       | \]                    |
+-----------------------+-----------------------+-----------------------+
| duration_minutes      | integer               | Specifies the total   |
|                       |                       | duration of this      |
|                       |                       | poll.                 |
|                       |                       |                       |
|                       |                       | ` "dura               |
|                       |                       | tion_minutes": 1440 ` |
+-----------------------+-----------------------+-----------------------+
| end_datetime          | date (ISO 8601)       | Specifies the end     |
|                       |                       | date and time for     |
|                       |                       | this poll.            |
|                       |                       |                       |
|                       |                       | ` "e                  |
|                       |                       | nd_datetime": "2019-1 |
|                       |                       | 1-28T20:26:41.000Z" ` |
+-----------------------+-----------------------+-----------------------+
| voting_status         | string                | Indicates if this     |
|                       |                       | poll is still active  |
|                       |                       | and can receive       |
|                       |                       | votes, or if the      |
|                       |                       | voting is now closed. |
|                       |                       |                       |
|                       |                       | ` "votin              |
|                       |                       | g_status": "closed" ` |
+-----------------------+-----------------------+-----------------------+

### Retrieving a poll object

#### Sample Request

In the following request, we are requesting fields for the poll object
attached to the Tweet on the [Tweets
lookup](/en/docs/twitter-api/tweets/lookup/introduction.html) endpoint.
Since poll is a child object of a Tweet, the ` attachments.poll_id `
expansion is required. Be sure to replace ` $BEARER_TOKEN ` with your
own generated [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/tweets?ids=1199786642791452673&expansions=attachments.poll_ids&poll.fields=duration_minutes,end_datetime,id,options,voting_status' --header 'Authorization: Bearer $BEARER_TOKEN'
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "text": "C#",
            "id": "1199786642791452673",
            "attachments": {
                "poll_ids": [
                    "1199786642468413448"
                ]
            }
        }
    ],
    "includes": {
        "polls": [
            {
                "id": "1199786642468413448",
                "voting_status": "closed",
                "duration_minutes": 1440,
                "options": [
                    {
                        "position": 1,
                        "label": "“C Sharp”",
                        "votes": 795
                    },
                    {
                        "position": 2,
                        "label": "“C Hashtag”",
                        "votes": 156
                    }
                ],
                "end_datetime": "2019-11-28T20:26:41.000Z"
            }
        ]
    }
}
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
