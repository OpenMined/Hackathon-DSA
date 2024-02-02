<div>

``` {._5s-8 .prettyprint .lang-http .prettyprinted}
GET https://graph.facebook.com/<API_VERSION>/<WABA_ID>/phone_numbers
```

A list of [WhatsApp Business Phone
Number](/docs/graph-api/reference/whats-app-business-account-to-number-current-status/)
nodes and their default fields.

### Sample Request

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl \
'https://graph.facebook.com/v15.0/102289599326934/phone_numbers' \
-H 'Authorization: Bearer EAAJi...'
```

### Sample Response

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "data" : [ { "code_verification_status" : "VERIFIED", "display_phone_number" : "+1 555-555-5555", "id" : "106853218861309", "quality_rating" : "GREEN", "verified_name" : "Jaspers Market" } ], "paging" : { "cursors" : { "after" : "QVFIU...", "before" : "QVFIU..." } }
}
```

### Sample Request with Filtering

See [Filtering Phone
Numbers](/docs/whatsapp/business-management-api/manage-phone-numbers#filter-phone-numbers)
.

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl GET \
"https://graph.facebook.com/v18.0/102289599326934/phone_numbers \ ?fields=id,is_official_business_account,display_phone_number,verified_name \ &filtering=[{'field':'account_mode','operator':'EQUAL','value':'SANDBOX'}]" \
-H 'Authorization: Bearer EAAJi...'
```

### Sample Response 2

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "id" : "106853218861309", "is_official_business_account" : true, "display_phone_number" : "+1 555-555-5555", "verified_name" : "Jaspers Market"
}
```

</div>
