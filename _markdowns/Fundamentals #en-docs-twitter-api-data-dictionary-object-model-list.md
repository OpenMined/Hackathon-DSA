::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The list object contains [Twitter
Lists](https://help.twitter.com/en/using-twitter/twitter-lists) metadata
describing the referenced List. The List object is the primary object
returned in the List lookup endpoint. When requesting additional List
fields on this endpoint, simply use the fields parameter ` list.fields `
.

At the moment, the List object cannot be found as a child object from
any other data object. However, user objects can be found and expanded
in the user resource. These objects are available for expansion by
adding [ owner_id ]{.code-inline} to the [ expansions ]{.code-inline}
query parameter. Use the expansion with the field parameter:
` list.fields ` when requesting additional fields to complete the
primary List object and [ user.fields ]{.code-inline} to complete the
expansion object.\

+-------------+-------------+-------------+-------------+-------------+
| Field value | Type        | Description | How it can  |             |
|             |             |             | be used     |             |
+-------------+-------------+-------------+-------------+-------------+
| id          | string      | The unique  | Use this to |             |
| (default)   |             | identifier  | progr       |             |
|             |             | of this     | ammatically |             |
|             |             | List.       | retrieve    |             |
|             |             |             | information |             |
|             |             | ` "id": "22 | about a     |             |
|             |             | 44994945" ` | specific    |             |
|             |             |             | Twitter     |             |
|             |             |             | List.       |             |
+-------------+-------------+-------------+-------------+-------------+
| name        | string      | The name of |             |             |
| (default)   |             | the List,   |             |             |
|             |             | as defined  |             |             |
|             |             | when        |             |             |
|             |             | creating    |             |             |
|             |             | the List.   |             |             |
|             |             |             |             |             |
|             |             | ` "na       |             |             |
|             |             | me": "Twitt |             |             |
|             |             | er Lists" ` |             |             |
+-------------+-------------+-------------+-------------+-------------+
| created_at  | date (ISO   | The UTC     | Can be used |             |
|             | 8601)       | datetime    | to          |             |
|             |             | that the    | determine   |             |
|             |             | List was    | how long a  |             |
|             |             | created on  | List has    |             |
|             |             | Twitter.    | been on     |             |
|             |             |             | Twitter     |             |
|             |             | ` "created_ |             |             |
|             |             | at": "2013- |             |             |
|             |             | 12-14T04:35 |             |             |
|             |             | :55.000Z" ` |             |             |
+-------------+-------------+-------------+-------------+-------------+
| description | string      | A brief     |             |             |
|             |             | description |             |             |
|             |             | to let      |             |             |
|             |             | users know  |             |             |
|             |             | about the   |             |             |
|             |             | List.       |             |             |
|             |             |             |             |             |
|             |             | ` "descri   |             |             |
|             |             | ption": "Pe |             |             |
|             |             | ople that a |             |             |
|             |             | re active m |             |             |
|             |             | embers of t |             |             |
|             |             | he Bay area |             |             |
|             |             |  cycling co |             |             |
|             |             | mmunity on  |             |             |
|             |             | Twitter." ` |             |             |
+-------------+-------------+-------------+-------------+-------------+
| fol         | integer     | Shows how   |             |             |
| lower_count |             | many users  |             |             |
|             |             | follow this |             |             |
|             |             | List,       |             |             |
|             |             |             |             |             |
|             |             | [           |             |             |
|             |             | \"follow    |             |             |
|             |             | er_count\": |             |             |
|             |             | 198         |             |             |
|             |             | ]{.c        |             |             |
|             |             | ode-inline} |             |             |
+-------------+-------------+-------------+-------------+-------------+
| m           | integer     | Shows how   |             |             |
| ember_count |             | many        |             |             |
|             |             | members are |             |             |
|             |             | part of     |             |             |
|             |             | this List.  |             |             |
|             |             |             |             |             |
|             |             | [           |             |             |
|             |             | \"memb      |             |             |
|             |             | er_count\": |             |             |
|             |             | 60          |             |             |
|             |             | ]{.c        |             |             |
|             |             | ode-inline} |             |             |
+-------------+-------------+-------------+-------------+-------------+
| private     | boolean     | Indicates   |             |             |
|             |             | if the List |             |             |
|             |             | is private. |             |             |
|             |             |             |             |             |
|             |             | [           |             |             |
|             |             | \           |             |             |
|             |             | "private\": |             |             |
|             |             | false       |             |             |
|             |             | ]{.c        |             |             |
|             |             | ode-inline} |             |             |
+-------------+-------------+-------------+-------------+-------------+
| owner_id    | string      | Unique      | Returns the |             |
|             |             | identifier  | List owner  |             |
|             |             | of this     | ID. Can     |             |
|             |             | List\'s     | potentially |             |
|             |             | owner.      | be used to  |             |
|             |             |             | find out if |             |
|             |             | ` "o        | this        |             |
|             |             | wner_id": " | specifc     |             |
|             |             | 12555427744 | user owns   |             |
|             |             | 32063488" ` | any other   |             |
|             |             |             | Lists.      |             |
|             |             |             |             |             |
|             |             |             | Can also be |             |
|             |             |             | used to     |             |
|             |             |             | expand user |             |
|             |             |             | objects.    |             |
+-------------+-------------+-------------+-------------+-------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the following request, we are requesting fields for the user on the
[List lookup by
ID](/en/docs/twitter-api/lists/list-lookup/introduction.html) endpoint.
Be sure to replace ` $BEARER_TOKEN ` with your own generated [Bearer
Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/lists/1355797419175383040?list.fields=created_at,description,private,follower_count,member_count,owner_id&expansions=owner_id' --header 'Authorization: Bearer $BEARER_TOKEN'

    
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
    "name": "Twitter Comms",
    "member_count": 60,
    "id": "1355797419175383040",
    "private": false,
    "description": "",
    "follower_count": 198,
    "owner_id": "257366942",
    "created_at": "2021-01-31T08:37:48.000Z"
  },
  "includes": {
    "users": [
      {
        "created_at": "2011-02-25T07:51:26.000Z",
        "name": "Ashleigh Hay 🤸🏼‍♀️",
        "id": "257366942",
        "username": "shleighhay",
        "verified": false
      }
    ]
  }
}
    
```
:::
:::
:::
:::
