::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note:** This guide assumes you have completed the prerequisites
from the [quick start
overview](/en/docs/twitter-api/lists/list-members/quick-start) .
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
Once you have the Twitter API v2 collection loaded in Postman, navigate
to the "List" folder, select another folder "List members", and then
choose \"Add a member\".\

#### Step two: Specify the user to add

Manage List member endpoints require two IDs: the ID of the List and the
ID of the user to add. You can find the user's ID using the [users
lookup](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference)
and pass a username to receive the [ id ]{.code-inline} field.

The target ID can be any valid user ID. In Postman, navigate to the
\"Params\" tab, and enter your ID into the \"Value\" column of the [ id
]{.code-inline} path variable. Navigate to the "Body" tab and ID of the
user you wish to add as the value for the [ user_id ]{.code-inline}
parameter. Be sure not to include any spaces before or after any ID.

  --------------------------- ------------------------------------------------ --------------------
  **Key**                     **Value**                                        **Parameter type**
  [ ` id ` ]{.code-inline}    The List ID                                      path
  [ user_id ]{.code-inline}   The target user ID you wish to add as a member   body
  --------------------------- ------------------------------------------------ --------------------

You should now see a similar URL next to the \"Send\" button:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.t05__pre--with-button .t05__pre--wrap-text}
 https://api.twitter.com/2/lists/1441162269824405510/members
    
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
    "is_member": true
  }
}

    
```
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
If the returned response object contains a [ true ]{.code-inline} value
for the key [ is_member ]{.code-inline} , you have successfully added
the user as a member of the List.

To remove a member from a List, select the "Remove a member" request
also found in the "Lists" folder of the Twitter API v2 collection loaded
in Postman. This endpoint requires the ID of the List and the user ID of
the member you wish to remove. In the "Params" tab, enter the ID of the
List as the value for the [ id ]{.code-inline} column and ID of the user
to be removed as the value for the [ user_id ]{.code-inline} column.

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
    "is_member": false
  }
}

    
```
:::
:::
:::
:::
