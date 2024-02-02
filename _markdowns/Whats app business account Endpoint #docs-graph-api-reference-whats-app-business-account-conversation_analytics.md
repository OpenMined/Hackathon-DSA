<div>

Requirements

-   whatsapp_business_management permission

-   whatsapp_business_messaging permission

-   public_profile permission

-   WHATSAPP BUSINESS ACCOUNT ID

-   USER ACCESS TOKEN

Request

*Formatted for readability.*

::: _4gnb
::: _51xa
:::

::: {#u_0_8_13 ._4gnf ._4fa6}
``` {.prettyprint .lang-sh .prettyprinted}
curl -i -X GET \ "https://graph.facebook.com/LATEST-VERSION/WHATSAPP-BUSINESS-ACCOUNT-ID?fields=conversation_analytics.start(1651698000).end(1652302800).granularity(DAILY).phone_numbers(PHONE-NUMBER).country_codes().metric_types().conversation_types().conversation_directions().dimensions(CONVERSATION_DIRECTIONCONVERSATION_TYPECOUNTRYPHONE)&
access_token=USER-ACCESS-TOKEN"
```
:::
:::

Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "conversation_analytics": { "data": [ { "data_points": [ { "start": 1651698000, "end": 1651784400, "conversation": 281, "phone_number": "PHONE-NUMBER", "country": "US", "conversation_type": "FREE_TIER", "conversation_direction": "BUSINESS_INITIATED", "cost": 0 }, { "start": 1652130000, "end": 1652216400, "conversation": 631, "phone_number": "PHONE-NUMBER", "country": "US", "conversation_type": "FREE_TIER", "conversation_direction": "BUSINESS_INITIATED", "cost": 0 } ] } ] }, "id": "WHATSAPP-BUSINESS-ACCOUNT-ID"
}
```

</div>
