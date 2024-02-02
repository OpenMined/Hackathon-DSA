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
choose \"Pin a List\".\

#### Step two: Specify the List to pin

Manage pinned List endpoints require two IDs: one for the user (the
authenticated user to pin a List) and the target List (the List to be
pinned). The user's ID must correspond to the authenticating user's ID,
meaning that you must pass the Access Tokens associated with the user ID
when authenticating your request. In this case, you can specify the ID
belonging to your user. You can find your ID in two ways:

1.  Using the [users
    lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference)
    by username endpoint, you can pass a username and receive the [ id
    ]{.code-inline} field.
2.  Looking at your Access Token, you will find that the numeric part is
    your user ID.

The target List ID can be any valid list. In Postman, navigate to the
\"Params\" tab, and enter the user ID into the \"Value\" column of the [
id ]{.code-inline} path variable. Navigate to the "Body" tab and ID of
the List you wish to pin as the value for the [ list_id ]{.code-inline}
parameter. Be sure not to include any spaces before or after any ID.

  --------------------------- --------------------------------- --------------------
  **Key**                     **Value**                         **Parameter type**
  [ ` id ` ]{.code-inline}    The user ID                       path
  [ list_id ]{.code-inline}   The target List ID to be pinned   body
  --------------------------- --------------------------------- --------------------

You should now see a similar URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/users/2244994945/pinned_lists
    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Step three: Make your request and review your response \

Once you have everything set up, hit the \"Send\" button, and you will
receive a similar response to the following example response:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "pinned": true
  }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
You have successfully pinned the target List if the returned response
object contains a [ true ]{.code-inline} value for the key [ pinned
]{.code-inline} .

To unpin a List, select the Unpin List" request also found in the
"Lists" folder of the Twitter API v2 collection loaded in Postman. This
endpoint requires the authenticated user ID and the ID of the List to be
unpinned. In the "Params" tab, enter the user ID as the value for the [
id ]{.code-inline} column and ID of the List to be unpinned as the value
for the [ list_id ]{.code-inline} column.

On successful delete request, you will receive a response similar to the
following example:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 {
  "data": {
    "pinned": false
  }
}

    
```
:::
:::
:::
:::
