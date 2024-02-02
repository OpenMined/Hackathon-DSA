<div>

-   Only two templates can be compared at a time.
-   Templates must have been sent at least 1,000 times in the queries
    specified timeframe.
-   Timeframes are limited to 7, 30, 60 and 90 day lookbacks from the
    time of the request.

``` {._5s-8 .prettyprint .lang-http}
GET /<WHATSAPP_MESSAGE_TEMPLATE_ID>/compare
  ?template_ids=[<TEMPLATE_IDS]
  &start=<START>
  &end=<END>
```

``` {._5s-8 .prettyprint .lang-json}
{
  "data": [
    {
      "metric": "BLOCK_RATE",
      "type": "RELATIVE",
      "order_by_relative_metric": [<ORDER_BY_RELATIVE_METRIC>]
    },
    {
      "metric": "MESSAGE_SENDS",
      "type": "NUMBER_VALUES",
      "number_values": [<NUMBER_VALUES>]
    },
    {
      "metric": "TOP_BLOCK_REASON",
      "type": "STRING_VALUES",
      "string_values": [<STRING_VALUES>]
    }
  ]
}
```

``` {._5s-8 .prettyprint .lang-curl}
curl -X GET 'https://graph.facebook.com/v19.0/5289179717853347/compare?template_ids=[1533406637136032]&start=1674844791182&end=1674845395982' \
-H 'Authorization: Bearer EAAJB...'
```

``` {._5s-8 .prettyprint .lang-json}
{
  "data": [
    {
      "metric": "BLOCK_RATE",
      "type": "RELATIVE",
      "order_by_relative_metric": [
        "1533406637136032",
        "5289179717853347"
      ]
    },
    {
      "metric": "MESSAGE_SENDS",
      "type": "NUMBER_VALUES",
      "number_values": [
        {
          "key": "5289179717853347",
          "value": 1273
        },
        {
          "key": "1533406637136032",
          "value": 1042
        }
      ]
    },
    {
      "metric": "TOP_BLOCK_REASON",
      "type": "STRING_VALUES",
      "string_values": [
        {
          "key": "5289179717853347",
          "value": "UNKNOWN_BLOCK_REASON"
        },
        {
          "key": "1533406637136032",
          "value": "UNKNOWN_BLOCK_REASON"
        }
      ]
    }
  ]
}
```

</div>
