::: {._4-u3 ._588p}
Query the ` GET /me/accounts ` endpoint (this translates to
` GET /{user-id}/accounts ` , which perform a ` GET ` on the Facebook
[User](/docs/graph-api/reference/user) node, based on your access
token).

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/v18.0/me/accounts?access_token={access-token}"
```

This should return a collection of Facebook Pages that the current
Facebook User can perform the ` MANAGE ` , ` CREATE_CONTENT ` ,
` MODERATE ` , or ` ADVERTISE ` tasks on:

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data": [ { "access_token": "EAAJjmJ...", "category": "App Page", "category_list": [ { "id": "2301", "name": "App Page" } ], "name": "Metricsaurus", "id": "134895793791914", // capture the Page ID "tasks": [ "ANALYZE", "ADVERTISE", "MODERATE", "CREATE_CONTENT", "MANAGE" ] } ]
}
```

Capture the ID of the Facebook Page that\'s connected to the Instagram
account that you want to query. Keep in mind that your app users may be
able to perform tasks on multiple pages, so you eventually will have to
introduce logic that can determine the correct Page ID to capture (or
devise a UI where your app users can identify the correct Page for you).

<div>

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/57437240_2085096038272793_3947769475595501568_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=FVVIXaHgG6IAX_09EcU&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBNAiL95Vw5cWF4yCfZN4AZsx8VUBKk281vg_EgXHSO3w&oe=65C37446){._254
.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/57437240_2085096038272793_3947769475595501568_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=FVVIXaHgG6IAX_09EcU&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBNAiL95Vw5cWF4yCfZN4AZsx8VUBKk281vg_EgXHSO3w&oe=65C37446"}

</div>
:::
