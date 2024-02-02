::: {._4-u3 ._588p}
Get reactions on an object.

View
[Insights](https://developers.facebook.com/docs/graph-api/reference/insights#availmetrics)
for more information on Page and Post reactions.

### New Page Experience

This endpoint is supported for New Page Experience.

### Requirements

**Marketing Apps**

-   ` ads_management `
-   ` pages_read_engagement `
-   ` pages_show_list `

**Page Management Apps**

### Sample Request

The following example is a ` GET ` request made by a User who has
reacted to their own object.

::: _4gnb
::: {#u_0_a_gh ._4gnf ._4fa6}
``` {.prettyprint .lang-sh .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/your-post-id/reactions?access_token=your-user-access-token"
```
:::
:::

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data": [ { "id": "your-user-id", "name": "Your Name", "type": "HAHA" } ], "paging": { "cursors": { "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR", "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD" } }
}
```

If the User or Page has not reacted to the object being queried,
` data ` will be empty.

The following example is a ` GET ` request for the total reactions to an
object.

::: _4gnb
::: {#u_0_k_0Y ._4gnf ._4fa6}
``` {.prettyprint .lang-sh .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/your-post-id ?fields=reactions.summary(total_count) &access_token=your-access-token"
```
:::
:::

The JSON Response if the User or Page has reacted to their own object.

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "reactions": { "data": [ { "id": "your-user-id", "name": "Your Name", "type": "HAHA" } ], "paging": { "cursors": { "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR", "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD" } }, "summary": { "total_count": 28 } }, "id": "your-post-id"
}
```

The JSON Response if the User or Page has **not** reacted to their own
object.

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "reactions": { "data": [ ], "paging": { "cursors": { "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR", "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD" } }, "summary": { "total_count": 28 } }, "id": "your-post-id"
}
```

::: {._57yz ._57z0 ._3-8p}
::: _57y-
A User or Page can only query their own reactions. Other Users\' or
Pages\' reactions are unavailable due to privacy concerns.
:::
:::

::: {._57yz ._57z1 ._3-8p}
::: _57y-
The \"like\" reaction counts include both \"like\" and \"care\"
reactions.
:::
:::

### Parameters

::: _57-c
+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` type `                          | The type of reaction a Page or    |
|                                   | User marked an object.            |
| enum {NONE, LIKE, LOVE, WOW,      |                                   |
| HAHA, SORRY, ANGRY}               |                                   |
+-----------------------------------+-----------------------------------+
:::

### Fields

Reading from this edge will return a JSON formatted result

``` {._5s-8 .prettyprint .lang-sh .prettyprinted}
{ "data": [], "paging": {}, "summary": {}
}
```

` data `

The [Profile](/docs/graph-api/reference/profile/) of the Page or User
running the query, if the object being queried was reacted to by the
Page or User, and a list of reaction types:

::: _57-c
+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| ` type `                          | The type of reaction a Page or    |
|                                   | User marked an object.            |
| enum {NONE, LIKE, LOVE, WOW,      |                                   |
| HAHA, SORRY, ANGRY}               |                                   |
+-----------------------------------+-----------------------------------+
:::

For reactions on Posts, this edge does not return a Profile except for
the current user, if read with a user access token.

#### View the count of an individual reaction

::: _4gnb
::: {#u_0_w_X6 ._4gnf ._4fa6}
``` {.prettyprint .lang-sh .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/your-object-id ?fields=reactions.type(LOVE).limit(0).summary(total_count) &access_token=your-access-token"
```
:::
:::

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "reactions": { "data": [ ], "summary": { "total_count": 3498 } }, "id": "your-object-id"
}
```

` paging `

For more details about pagination, see the Graph API\'s [paging
documentation](/docs/graph-api/using-graph-api/#paging) . Adding
` limit(0) ` to ` reactions ` will remove ` paging ` from the output.

` summary `

Aggregated information about the edge, such as counts. Specify the
fields to fetch in the summary param (like ` summary=total_count ` ).

::: _57-c
+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| ` total_count `                   | Total number of reactions         |
|                                   |                                   |
| unsigned int32                    |                                   |
+-----------------------------------+-----------------------------------+
| ` viewer_reaction `               | The type of reaction a Page or    |
|                                   | User marked an object.            |
| enum {NONE, LIKE, LOVE, WOW,      |                                   |
| HAHA, SORRY, ANGRY}               |                                   |
+-----------------------------------+-----------------------------------+
:::

### Error Codes

::: _57-c
  Error   Description
  ------- -------------------
  100     Invalid parameter
:::
:::
