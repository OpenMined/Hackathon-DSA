::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:** This guide assumes you have completed the prerequisites
from the [quick start
overview](/content/developer-twitter/en/docs/twitter-api/lists/pinned-lists/quick-start)
.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the "List" folder, select another folder "Pinned Lists", and then
choose \"User\'s pinned Lists\".\

#### Step two: Identify and specify the user

In order to retrieve a user's pinned List, you must specify their user
ID within the request. The user ID must correspond to the authenticating
user's ID, meaning that you must pass the Access Tokens associated with
the user ID when authenticating your request. In this example, you can
specify the ID belonging to your own user. You can find your ID in two
ways:

1.  Using the [users
    lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference)
    by username endpoint, you can pass a username and receive the [ id
    ]{.code-inline} field.
2.  Looking at your Access Token, you will find that the numeric part is
    your user ID.

In Postman, navigate to the \"Params\" tab and enter this user ID into
the \"Value\" column of the ` id ` parameter.

  -------------------------- ----------------------------------------
  **Key**                    **Value**
  [ ` id ` ]{.code-inline}   [ 2244994945 ]{.code-inline} (user ID)
  -------------------------- ----------------------------------------

#### Step three: Identify and specify which fields you would like to retrieve

If you click the \"Send\" button after step three, you will receive the
default [List
object](/en/docs/twitter-api/data-dictionary/object-model/lists) fields
in your response: ` id ` and ` name ` .

If you would like to receive additional fields beyond ` id ` and
` name ` , you will have to specify those fields in your request with
the
[` field `](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/data-dictionary/introduction/fields)
and/or
[` expansion `](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction/expansions)
parameters.

For this exercise, we will request a three additional sets of fields
from different objects:

-   The additional ` follower_count ` field in the primary List object.
-   The full [user
    object](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user)
    using the expansion parameter.
-   The additional ` tweet.created_at ` field in the associated user
    object.

In Postman, navigate to the \"Params\" tab and add the following
key:value pair to the \"Query Params\" table:

+-----------------------+-----------------------+-----------------------+
| Key                   | Value                 | Returned fields       |
+-----------------------+-----------------------+-----------------------+
| list.fields           | follower_count        | ` follower_count `    |
+-----------------------+-----------------------+-----------------------+
| expansions            | owner_id              | `                     |
|                       |                       |  includes.users.id, i |
|                       |                       | ncludes.users.name, ` |
|                       |                       |                       |
|                       |                       | in                    |
|                       |                       | cludes.users.username |
+-----------------------+-----------------------+-----------------------+
| user.fields           | created_at            | ` includ              |
|                       |                       | es.users.created_at ` |
+-----------------------+-----------------------+-----------------------+

You should now see a similar URL next to the "Send" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/users/2244994945/pinned_lists?expansions=owner_id&list.fields=follower_count&user.fields=created_at
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Step four: Make your request and review your response \

Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": [
    {
      "follower_count": 0,
      "id": "1454155907651158017",
      "name": "test list",
      "owner_id": "2244994945"
    }
  ],
  "includes": {
    "users": [
      {
        "username": "TwitterDev",
        "id": "2244994945",
        "created_at": "2013-12-14T04:35:55.000Z",
        "name": "Twitter Dev"
      }
    ]
  },
  "meta": {
    "result_count": 1
  }
}
    
```
:::
:::
:::
:::
