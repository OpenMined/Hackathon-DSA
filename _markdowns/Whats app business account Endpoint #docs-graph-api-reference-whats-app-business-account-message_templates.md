<div>

``` {._5s-8 .prettyprint .lang-https .prettyprinted}
POST /<WHATSAPP_BUSINESS_ACCOUNT_ID>/message_templates
```

::: _57-c
  Placeholder                          Value
  ------------------------------------ ----------------------------------------------------------------
  ` <WHATSAPP_BUSINESS_ACCOUNT_ID> `   ID of the WhatsApp Business Account to create the template on.
:::

See [Parameters](#parameters-2) for property descriptions.

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "allow_category_change": <ALLOW_CATEGORY_CHANGE>, "name": "<NAME>", "language": "<LANGUAGE>", "category": "<CATEGORY>", "components": [<COMPONENTS>]
}
```

### Response {#response-2}

See [Return Type](#return-type) .

### Sample Request {#sample-request-2}

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl 'https://graph.facebook.com/v18.0/102290129340398/message_templates' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer EAAJB...' \
-d '
{ "name": "seasonal_promotion", "language": "en", "category": "MARKETING", "components": [ { "type": "HEADER", "format": "TEXT", "text": "Our {{1}} is on!", "example": { "header_text": [ "Summer Sale" ] } }, { "type": "BODY", "text": "Shop now through {{1}} and use code {{2}} to get {{3}} off of all merchandise.", "example": { "body_text": [ [ "the end of August","25OFF","25%" ] ] } }, { "type": "FOOTER", "text": "Use the buttons below to manage your marketing subscriptions" }, { "type":"BUTTONS", "buttons": [ { "type": "QUICK_REPLY", "text": "Unsubcribe from Promos" }, { "type":"QUICK_REPLY", "text": "Unsubscribe from All" } ] } ]
}'
```

### Sample Response {#sample-response-2}

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id": "594425479261596", "status": "PENDING", "category": "MARKETING"
}
```

</div>
