::: {._4-u3 ._588p}
All Marketing API requests, and Pages API requests made with a system or
page access token, are subject to Business Use Case (BUC) Rate Limits,
and depend on the endpoints you are querying.

For Marketing API, the rate limit is applied to the ad account across
the same Business Use Case. For example, all endpoints with the Ads
Management business use case will share the total quota within the same
ad account. If a certain endpoint makes a lot of API requests and causes
throttling, other endpoints configured with the same business use case
will also receive rate limiting errors. The quota depends on the app\'s
Marketing API Access Tier. The standard access Marketing API tier will
have more quotas than the development access Marketing API tier. By
default, an new app should be on the development tier. If you need to
upgrade to get more rate limiting quota, upgrade to Advanced Access of
[Ads Management Standard
Access](/docs/features-reference/ads-management-standard-access/) in App
Review.

### Ads Insights

Requests made by your app to the Ads Insights API are counted against
the app\'s rate limit metrics such as call count, total CPU time and
total time. An app\'s call count is the number of calls it can make
during a rolling one hour window and is calculated as follows:

For apps with [Standard
Access](/docs/graph-api/overview/access-levels/#standard-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 600 + 400 * Number of Active ads - 0.001 * User Errors `

For apps with [Advanced
Access](/docs/graph-api/overview/access-levels/#advanced-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 190000 + 400 * Number of Active ads - 0.001 * User Errors `

The Number of Active ads is the number of ads currently running per ad
account. User Errors is the number of errors received when calling the
API. To get a higher rate limit, you can apply for the [Ads Management
Standard
Access](/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features)
feature.

Rate limiting may also be subject to the total CPU time and total wall
time during a rolling one hour window. For more details, check the HTTP
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header ` total_cputime ` and ` total_time ` .

If you are receiving rate limiting errors, you can also refer to
` estimated_time_to_regain_access ` in the
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header for the estimated blocking time.

### Ads Management

Requests made by your app to the Ads Management API are counted against
the app\'s rate limit metrics such as call count, total CPU time and
total time. An app\'s call count is the number of calls it can make
during a rolling one hour window and is calculated as follows:

For apps with [Standard
Access](/docs/graph-api/overview/access-levels/#standard-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 300 + 40 * Number of Active ads `

For apps with [Advanced
Access](/docs/graph-api/overview/access-levels/#advanced-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 100000 + 40 * Number of Active ads `

The Number of Active Ads is the number of ads for each ad account.

Rate limiting may also be subject to the total CPU time and total wall
time during a rolling one hour window. For more details, check the HTTP
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header ` total_cputime ` and ` total_time ` .

If you are receiving rate limiting errors, you can also refer to
` estimated_time_to_regain_access ` in the
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header for the estimated blocking time.

### Catalog

#### Catalog Batch

Requests made by your app are counted against the rate limit metrics
such as call count, total CPU time and total time your app can make in a
rolling one hour period per each catalog ID and is calculated as
follows:

` Calls within one hour = 200 + 200 * log2(unique users) `

The unique users is a number of unique users of the business (on all
catalogs) with intent in the last 28 days. The more users see products
from your catalogs, the more call quota is allocated.

::: _57-c
  Type of Call   Endpoint
  -------------- -------------------------------------
  POST           /{catalog_id}/items_batch
  POST           /{catalog_id}/localized_items_batch
  POST           /{catalog_id}/batch
:::

#### Catalog Management

Requests made by your app are counted against the number of calls your
app can make in a rolling one hour period per each catalog ID and is
calculated as follows:

` Calls within one hour = 20,000 + 20,000 * log2(unique users) `

The unique users is a number of unique users of the business (on all
catalogs) with intent in the last 28d. The more users see products from
your catalogs, the more call quota is allocated.

This formula is applied on various catalog endpoints.

For more information on how to get your current rate usage, see
[Headers](/docs/graph-api/overview/rate-limiting/#headers) .

Rate limiting may also be subject to the total CPU time and total wall
time during a rolling one hour window. For more details, check the HTTP
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header ` total_cputime ` and ` total_time ` .

If you are receiving rate limiting errors, you can also refer to
` estimated_time_to_regain_access ` in the
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header for the estimated blocking time.

### Custom Audience

Requests made by your app to the Custom Audience API are counted against
the app\'s rate limit metrics such as call count, total CPU time and
total time. An app\'s call count is the number of calls it can make
during a rolling one hour window and is calculated as follows but will
never exceed 700000:

For apps with [Standard
Access](/docs/graph-api/overview/access-levels/#standard-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 5000 + 40 * Number of Active Custom Audiences `

For apps with [Advanced
Access](/docs/graph-api/overview/access-levels/#advanced-access) to the
Ads Management Standard Access feature:

` Calls within one hour = 190000 + 40 * Number of Active Custom Audiences `

The Number of Active Custom Audiences is the number of active [custom
audiences](https://developers.facebook.com/docs/marketing-api/audiences-api)
for each ad account.

Rate limiting may also be subject to the total CPU time and total wall
time during a rolling one hour window. For more details, check the HTTP
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header ` total_cputime ` and ` total_time ` .

If you are receiving rate limiting errors, you can also refer to
` estimated_time_to_regain_access ` in the
[` X-Business-Use-Case `](/docs/graph-api/overview/rate-limiting/#headers-2)
header for the estimated blocking time.

### Instagram Graph API

Calls to the [Instagram Graph API](/docs/instagram-api) are counted
against the calling app\'s call count. An app\'s call count is unique
for each app and app user pair, and is the number of calls the app has
made in a rolling 24 hour window. It is calculated as follows:

` Calls within 24 hours = 4800 * Number of Impressions `

The Number of Impressions is the number of times any content from the
app user\'s Instagram account has entered a person\'s screen within the
last 24 hours.

#### Notes

### LeadGen

Requests made by your app to the LeadGen API are counted against the
app's call count. An app's call count is the number of calls it can make
during a rolling 24 hour window and is calculated as follows:

` Calls within 24 hours = 4800 * Leads Generated `

The Number of Leads Generated is the number of leads generated per Page
for this Ad Account over the past 90 days.

### Messenger Platform

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Rate limits for the Messenger Platform are dependent on the API used
and, in some instances, the message content.

#### Messenger API

Requests made by your app are counted against the number of calls your
app can make in a rolling 24 hour period and is calculated as follows:

` Calls within 24 hours = 200 * Number of Engaged Users `

The Number of Engaged Users is the number of people the business can
message via Messenger.

#### Messenger API for Instagram

Requests made by your app are counted against the number of calls your
app can make per Instagram Professional account and the API used.

<div>

**Conversations API**

-   Your app can make 2 calls per second per Instagram Professional
    account

**Send API**

-   Your app can make 100 calls per second per Instagram Professional
    account for messages that contain text, links, reactions, and
    stickers
-   Your app can make 10 calls per second per Instagram Professional
    account for messages that contain audio or video content

**Private Replies API**

-   Your app can make 100 calls per second per Instagram Professional
    account for private replies to Instagram Live comments
-   Your app can make 750 calls per hour per Instagram Professional
    account for private replies to comments on Instagram posts and reels

</div>
:::
:::

</div>

### Pages

The Page Rate Limits may use either the Platform or BUC rate limit logic
depending on the type of token used. Any Pages API calls that are made
using a
[Page](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens)
or [system user access
token](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser#systemusertoken)
use the rate limit calculation below. Any calls made with
[application](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens)
or [user access
tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens)
are subject to application or User rate limits.

Requests made by your app to the Pages API using a Page access token or
system User access token are counted against the app's call count. An
app's call count is the number of calls it can make during a rolling one
hour window and is calculated as follows:

` Calls within one hour = 4800 * Number of Engaged Users `

The Number of Engaged Users is the number of Users who engaged with the
Page per 24 hours.

Requests made by your app to the Pages API using a User access token or
App access token follow the [Platform Rate Limit
logic](#platform-rate-limits) .

To avoid [rate limiting](/docs/graph-api/overview/rate-limiting#pages)
issues when using the [Page Public Access Content
feature](/docs/pages/overview/permissions-features#features) , using a
[system user access
token](https://www.facebook.com/business/help/503306463479099) is
recommended.

### Spark AR Commerce Effect Management {#spark-ar}

Requests made by your app to any Commerce endpoints are counted against
the app's call count. An app's call count is the number of calls it can
make during a rolling one hour window and is calculated as follows:

` Calls within one hour = 200 + 40 * Number of Catalogs `

The Number of Catalogs is the total number of catalogs across all
commerce accounts managed by your app.

### WhatsApp Business Management API {#wa-biz-api}

<div>

Requests made by your app to the [WhatsApp Business Management
API](/docs/whatsapp/business-management-api) are counted against your
app's count. An app's call count is the number of calls it can make
during a rolling one hour. For the following WhatsApp Business
Management API, your app can make 200 calls per hour, per app, per
WhatsApp Business Account (WABA) by default. For active WABAs with at
least one registered phone number, your app can make 5000 calls per
hour, per app, per active WABA.

::: _57-c
  Type of Call                          Endpoint
  ------------------------------------- --------------------------------------------------------------
  ` GET `                               ` /{whatsapp-business-account-id} `
  ` GET ` , ` POST ` , and ` DELETE `   ` /{whatsapp-business-account-id}/assigned_users `
  ` GET `                               ` /{whatsapp-business-account-id}/phone_numbers `
  ` GET ` , ` POST ` , and ` DELETE `   ` /{whatsapp-business-account-id}/message_templates `
  ` GET ` , ` POST ` , and ` DELETE `   ` /{whatsapp-business-account-id}/subscribed_apps `
  ` GET `                               ` /{whatsapp-business-account-to-number-current-status-id} `
:::

For the following [Credit Line
APIs](/docs/whatsapp/embedded-signup/manage-accounts/share-and-revoke-credit-lines)
, your app can make 5000 calls per hour, per app.

::: _57-c
  Type of Call             Endpoint
  ------------------------ --------------------------------------------------------------
  ` GET `                  ` /{business-id}/extendedcredits `
  ` POST `                 ` /{extended-credit-id}/whatsapp_credit_sharing_and_attach `
  ` GET ` and ` DELETE `   ` /{allocation-config-id} `
  ` GET `                  ` /{extended-credit-id}/owning_credit_allocation_configs `
:::

To avoid hitting rate limits, we recommend using
[webhooks](/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp#setup)
to keep track of status updates for message templates, phone numbers,
and WABAs.

For more information on how to get your current rate usage, see
[Headers](/docs/graph-api/overview/rate-limiting/#headers) .

</div>

All API responses made by your app that are rate limited using the BUC
logic include an ` X-Business-Use-Case-Usage ` (for v3.3 and older Ads
API calls) HTTP header with a JSON-formatted string that describes
current application rate limit usage. This header can return up to 32
objects in one call.

#### X-Business-Use-Case Usage Header Contents

::: _57-c
  Error Code                            Value Description
  ------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ` business-id `                       The ID of the business associated with the token making the API calls.
  ` call_count `                        A whole number expressing the percentage of allowed calls made by your app over a rolling one hour period.
  ` estimated_time_to_regain_access `   Time, in minutes, until calls will not longer be throttled.
  ` total_cputime `                     A whole number expressing the percentage of CPU time allotted for query processing.
  ` total_time `                        A whole number expressing the percentage of total time allotted for query processing.
  ` type `                              Type of rate limit applied. Value can be one of the following: ` ads_insights ` , ` ads_management ` , ` custom_audience ` , ` instagram ` , ` leadgen ` , ` messenger ` , or ` pages ` .
  ` ads_api_access_tier `               For ` ads_insights ` and ` ads_management ` types only. Tiers allows your app to access the Marketing API. By default, apps are in the ` development_access ` tier. ` Standard_access ` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the \"Advanced Access\" to the [Ads Management Standard Access](/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature.
:::

#### Total CPU Time

The amount of CPU time the request takes to process. When total_cputime
reaches 100, calls may be throttled.

#### Total Time

The length of time the request takes to process. When total_time reaches
100, calls may be throttled.

#### Ads API Access Tier

For ` ads_insights ` and ` ads_management ` types only. Tiers allows
your app to access the Marketing API. By default, apps are in the
` development_access ` tier. ` Standard_access ` enables lower rate
limiting. To get a higher rate limit and get to the standard tier, you
can apply for the \"Advanced Access\" to the [Ads Management Standard
Access](/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features)
feature.

#### Sample X-Business-Use-Case-Usage Header Value

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
x-business-use-case-usage: { "{business-object-id}": [ { "type": "{rate-limit-type}", //Type of BUC rate limit logic being applied. "call_count": 100, //Percentage of calls made. "total_cputime": 25, //Percentage of the total CPU time that has been used. "total_time": 25, //Percentage of the total time that has been used. "estimated_time_to_regain_access": 19, //Time in minutes to regain access. "ads_api_access_tier": "standard_access" //Tiers allows your app to access the Marketing API. standard_access enables lower rate limiting. } ], "66782684": [ { "type": "ads_management", "call_count": 95, "total_cputime": 20, "total_time": 20, "estimated_time_to_regain_access": 0, "ads_api_access_tier": "development_access" } ], "10153848260347724": [ { "type": "ads_insights", "call_count": 97, "total_cputime": 23, "total_time": 23, "estimated_time_to_regain_access": 0, "ads_api_access_tier": "development_access" } ], "10153848260347724": [ { "type": "pages", "call_count": 97, "total_cputime": 23, "total_time": 23, "estimated_time_to_regain_access": 0 } ],
...
}
```

### Error Codes {#error-codes-2}

When your app reaches its Business Use Case rate limit, subsequent
requests made by your app will fail and the API will respond with an
error code.

::: _57-c
  Error Code                                    BUC Rate Limit Type
  --------------------------------------------- ---------------------------------------------------------
  ` error code 80000, error subcode 2446079 `   Ads Insights
  ` error code 80004, error subcode 2446079 `   Ads Management
  ` error code 80003, error subcode 2446079 `   Custom Audience
  ` error code 80002 `                          Instagram
  ` error code 80005 `                          LeadGen
  ` error code 80006 `                          Messenger
  ` error code 32 `                             Page calls made with a User access token
  ` error code 80001 `                          Page calls made with a Page or System User access token
  ` error code 17, error subcode 2446079 `      V3.3 and Older Ads API excluding Ads Insights
  ` error code 80008 `                          WhatsApp Business Management API
  ` error code 80014 `                          Catalog Batch
  ` error code 80009 `                          Catalog Management
:::

#### SampleError Code Message

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{ "error": { "message": "(#80001) There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.", "type": "OAuthException", "code": 80001, "fbtrace_id": "AmFGcW_3hwDB7qFbl_QdebZ" }
}
```

### Best Practices {#best-practices-2}

-   When the limit has been reached, stop making API calls. Continuing
    to make calls will continue to increase your call count, which will
    increase the time before calls will be successful again.
-   Check the ` X-Business-Use-Case-Usage ` HTTP header to see how close
    your ad account is to its limit and when you can resume making
    calls.
-   Verify the error code and API endpoint to confirm the throttling
    type.
-   Switch to other ad accounts and come back to this account later.
-   It is better to create a new ad than to change existing ones.
-   Spread out queries evenly between two time intervals to avoid
    sending traffic in spikes.
-   Use filters to limit the data response size and avoid calls that
    request overlapping data.
:::
