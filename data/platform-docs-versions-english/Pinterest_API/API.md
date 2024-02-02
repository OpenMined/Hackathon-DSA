Pinterest REST API (5.12.0)
===========================

URL: [https://developers.pinterest.com/](https://developers.pinterest.com/) License: [MIT](https://spdx.org/licenses/MIT) [Terms of Service](https://developers.pinterest.com/terms/)

Pinterest's REST API

[](#tag/ad_accounts)ad\_accounts
================================

View analytical information about advertising.

Note: If the current operation\_user\_account (defined by the access token) has access to another user's Ad Accounts via [Pinterest Business Access](https://developers.pinterest.com/docs/reference/business-access/), you can modify your request to use the current operation\_user\_account's permissions to those Ad Accounts by including the ad\_account\_id in the path parameters for the request (e.g. .../?ad\_account\_id=12345&...).

[](#operation/ad_accounts/list)List ad accounts
-----------------------------------------------

Get a list of the ad\_accounts that the "operation user\_account" has access to.

* This includes ad\_accounts they own and ad\_accounts that are owned by others who have granted them [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| include\_shared\_accounts | boolean<br><br>Default: true<br><br>Include shared ad accounts |

### Responses

**200**

response

**default**

Unexpected error

get/ad\_accounts

https://api.pinterest.com/v5/ad\_accounts

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "string",                      * "name": "string",                      * "owner": {                          * "username": "string",                              * "id": "string"                                           },                      * "country": "US",                      * "currency": "USD",                      * "permissions": [                          * "ADMIN"                                           ],                      * "created_time": 1451431341,                      * "updated_time": 1451431341                               }                   ],      * "bookmark": "string"       }`

[](#operation/ad_accounts/create)Create ad account
--------------------------------------------------

Create a new ad account. Different ad accounts can support different currencies, payment methods, etc. An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners) can be assigned business access and appropriate roles to access an ad account.

You can set up up to 50 ad accounts per user. (The user must have a business account to create an ad account.)

For more, see [Create an advertiser account](https://help.pinterest.com/en/business/article/create-an-advertiser-account).

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### Request Body schema: application/json

Ad account to create.

|     |     |
| --- | --- |
| country | string (Country)<br><br>Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more<br><br>Country ID from ISO 3166-1 alpha-2. |
| name | string (name) <= 256 characters<br><br>Ad Account name. |
| owner\_user\_id | string (owner\_user\_id) ^\\d+$<br><br>Advertiser's owning user ID. |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts

https://api.pinterest.com/v5/ad\_accounts

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "country": "US",      * "owner_user_id": "383791336903426391",      * "name": "ACME Tools"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "string",      * "name": "string",      * "owner": {          * "username": "string",              * "id": "string"                   },      * "country": "US",      * "currency": "USD",      * "permissions": [          * "ADMIN"                   ],      * "created_time": 1451431341,      * "updated_time": 1451431341       }`

[](#operation/ad_accounts/get)Get ad account
--------------------------------------------

Get an ad account

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "string",      * "name": "string",      * "owner": {          * "username": "string",              * "id": "string"                   },      * "country": "US",      * "currency": "USD",      * "permissions": [          * "ADMIN"                   ],      * "created_time": 1451431341,      * "updated_time": 1451431341       }`

[](#operation/ad_account/analytics)Get ad account analytics
-----------------------------------------------------------

Get analytics for the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |

### Responses

**200**

Success

**400**

Invalid ad account analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "AD_ACCOUNT_ID": "547602124502",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`

[](#operation/ad_accounts_subscriptions/post)Create lead ads subscription
-------------------------------------------------------------------------

Create a lead ads webhook subscription.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.
* Advertisers can set up multiple integrations using ad\_account\_id + lead\_form\_id but only one integration per unique records.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Subscription to create.

|     |     |
| --- | --- |
| webhook\_url<br><br>required | string (webhook\_url)<br><br>Standard HTTPS webhook URL. |
| lead\_form\_id | string (Lead form ID) ^\\d+$<br><br>Lead form ID. |
| partner\_access\_token | string<br><br>Partner access token. Only for clients that requires authentication. We recommend to avoid this param. |
| partner\_refresh\_token | string<br><br>Partner refresh token. Only for clients that requires authentication. We recommend to avoid this param. |

### Responses

**200**

Success

**400**

Invalid input parameters.

**403**

Can't access this subscription.

**default**

Unexpected error.

post/ad\_accounts/{ad\_account\_id}/leads/subscriptions

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "webhook_url": "[https://webhook.example.com/xyz](https://webhook.example.com/xyz)",      * "lead_form_id": "383791336903426390"       }`

### Response samples

* 200
* 400
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "8078432025948590686",      * "cryptographic_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",      * "cryptographic_algorithm": "AES-256-GCM",      * "created_time": 1699209842000       }`

[](#operation/ad_accounts_subscriptions/get_list)Get lead ads subscriptions
---------------------------------------------------------------------------

Get the advertiser's list of lead ads subscriptions.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**403**

Can't access this subscription.

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/leads/subscriptions

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "lead_form_id": "383791336903426390",                      * "webhook_url": "[https://webhook.example.com/xyz](https://webhook.example.com/xyz)",                      * "id": "8078432025948590686",                      * "user_account_id": "549755885175",                      * "ad_account_id": "549755885176",                      * "api_version": "v5",                      * "cryptographic_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",                      * "cryptographic_algorithm": "AES-256-GCM",                      * "created_time": 1699209842000                               }                   ],      * "bookmark": "string"       }`

[](#operation/ad_accounts_subscriptions/get_by_id)Get lead ads subscription
---------------------------------------------------------------------------

Get a specific lead ads subscription record.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| subscription\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a subscription. |

### Responses

**200**

Success

**400**

Invalid input parameters.

**403**

Can't access this subscription.

**404**

Subscription not found.

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}

### Response samples

* 200
* 400
* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "lead_form_id": "383791336903426390",      * "webhook_url": "[https://webhook.example.com/xyz](https://webhook.example.com/xyz)",      * "id": "8078432025948590686",      * "user_account_id": "549755885175",      * "ad_account_id": "549755885176",      * "api_version": "v5",      * "cryptographic_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",      * "cryptographic_algorithm": "AES-256-GCM",      * "created_time": 1699209842000       }`

[](#operation/ad_accounts_subscriptions/del_by_id)Delete lead ads subscription
------------------------------------------------------------------------------

Delete an existing lead ads webhook subscription by ID.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| subscription\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a subscription. |

### Responses

**204**

Subscription deleted successfully

**400**

Invalid input parameters.

**403**

You are not authorized to delete this subscription.

**404**

Subscription not found.

**default**

Unexpected error.

delete/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}

### Response samples

* 400
* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 1,      * "message": "Advertiser ID must be numeric."       }`

[](#operation/analytics/get_mmm_report)Get advertiser Marketing Mix Modeling (MMM) report.
------------------------------------------------------------------------------------------

Get an mmm report for an ad account. This returns a URL to an mmm metrics report given a token returned from the create mmm report endpoint.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| token<br><br>required | string<br><br>Token returned from the post request creation call |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/mmm\_reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 0,      * "data": {          * "report_status": "DOES_NOT_EXIST",              * "url": "string",              * "size": 0                   },      * "message": "ok",      * "status": "success"       }`

[](#operation/analytics/create_mmm_report)Create a request for a Marketing Mix Modeling (MMM) report
----------------------------------------------------------------------------------------------------

This creates an asynchronous mmm report based on the given request. It returns a token that you can use to download the report when it is ready. NOTE: An additional limit of 5 queries per minute per advertiser applies to this endpoint while it's in beta release.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| report\_name<br><br>required | string (report\_name)<br><br>Name of the Marketing Mix Modeling (MMM) report |
| start\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report start date (UTC). Format: YYYY-MM-DD |
| end\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report end date (UTC). Format: YYYY-MM-DD |
| granularity<br><br>required | string<br><br>Enum: "DAY" "WEEK"<br><br>DAY - metrics are broken down daily.  <br>WEEK - metrics are broken down weekly. |
| level<br><br>required | string<br><br>Enum: "CAMPAIGN\_TARGETING" "AD\_GROUP\_TARGETING"<br><br>Level of the report |
| targeting\_types<br><br>required | Array of strings (targeting\_types) \[ 1 .. 5 \] items<br><br>Items Enum: "APPTYPE" "COUNTRY" "CREATIVE\_TYPE" "GENDER" "LOCATION"<br><br>List of targeting types |
| columns<br><br>required | Array of strings (MMMReportingColumn)<br><br>Items Enum: "SPEND\_IN\_DOLLAR" "SPEND\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "ECTR" "CAMPAIGN\_NAME" "TOTAL\_ENGAGEMENT" "EENGAGEMENT\_RATE" "ECPM\_IN\_DOLLAR" "CAMPAIGN\_ID" "ADVERTISER\_ID" "AD\_GROUP\_ID" "AD\_GROUP\_NAME" "CLICKTHROUGH\_1" "IMPRESSION\_1" "CLICKTHROUGH\_2" "IMPRESSION\_2" "TOTAL\_CLICKTHROUGH" "TOTAL\_IMPRESSION" "ADVERTISER\_NAME" "SPEND\_ORDER\_LINE\_PAID\_TYPE"<br><br>Metric and entity columns |
| countries | Array of strings (TargetingAdvertiserCountry)<br><br>Items Enum: "US" "GB" "CA" "IE" "AU" "NZ" "FR" "SE" "IL" "DE" "AT" "IT" "ES" "NL" "BE" "PT" "CH" "HK" "JP" "KR" … 18 more<br><br>A List of countries for filtering |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics mmm parameters

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/mmm\_reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_name": "string",      * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "granularity": "DAY",      * "level": "CAMPAIGN_TARGETING",      * "targeting_types": [          * "GENDER"                   ],      * "columns": [          * "SPEND_IN_DOLLAR"                   ],      * "countries": [          * "US"                   ]       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 0,      * "data": {          * "report_status": "FINISHED",              * "token": "string",              * "message": "string",              * "status": "success"                   }       }`

[](#operation/analytics/get_report)Get the account analytics report created by the async call
---------------------------------------------------------------------------------------------

This returns a URL to an analytics report given a token returned from the post request report creation call. You can use the URL to download the report. The link is valid for five minutes and the report is valid for one hour.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| token<br><br>required | string<br><br>Token returned from the post request creation call |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/reports

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_status": "FINISHED",      * "url": "string",      * "size": 0       }`

[](#operation/analytics/create_report)Create async request for an account analytics report
------------------------------------------------------------------------------------------

This returns a token that you can use to download the report when it is ready. Note that this endpoint requires the parameters to be passed as JSON-formatted in the request body. This endpoint does not support URL query parameters.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 914 days before the current date in UTC time and the max time range supported is 186 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.
* If level is PRODUCT\_ITEM, the furthest back you can are allowed to pull data is 92 days before the current date in UTC time and the max time range supported is 31 days.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| start\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report start date (UTC). Format: YYYY-MM-DD |
| end\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Metric report end date (UTC). Format: YYYY-MM-DD |
| granularity<br><br>required | string<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | Array of strings (ConversionReportAttributionType)<br><br>Items Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>List of types of attribution for the conversion report |
| campaign\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of campaign ids |
| campaign\_statuses | Array of strings (CampaignSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of status values for filtering |
| campaign\_objective\_types | Array of strings (ObjectiveType) \[ 1 .. 6 \] items<br><br>Items Enum: "AWARENESS" "CONSIDERATION" "VIDEO\_VIEW" "WEB\_CONVERSION" "CATALOG\_SALES" "WEB\_SESSIONS"<br><br>List of values for filtering. \["WEB\_SESSIONS"\] in BETA. |
| ad\_group\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of ad group ids |
| ad\_group\_statuses | Array of strings (AdGroupSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of values for filtering |
| ad\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of ad ids |
| ad\_statuses | Array of strings (PinPromotionSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "APPROVED" "PAUSED" "PENDING" "REJECTED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>List of values for filtering |
| product\_group\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of product group ids |
| product\_group\_statuses | Array of strings (ProductGroupSummaryStatus) \[ 1 .. 6 \] items<br><br>Items Enum: "RUNNING" "PAUSED" "EXCLUDED" "ARCHIVED"<br><br>List of values for filtering |
| product\_item\_ids | Array of strings \[ 1 .. 500 \] items<br><br>List of product item ids |
| targeting\_types | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 5 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>List of targeting types. Requires `level` to be a value ending in `_TARGETING`. |
| metrics\_filters | Array of objects (AdsAnalyticsMetricsFilter) non-empty<br><br>List of metrics filters |
| columns<br><br>required | Array of strings (ReportingColumnAsync)<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "OUTBOUND\_CTR" "COST\_PER\_OUTBOUND\_CLICK" "CAMPAIGN\_NAME" "CAMPAIGN\_STATUS" "PIN\_PROMOTION\_STATUS" "AD\_STATUS" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" … 540 more<br><br>Metric and entity columns |
| level<br><br>required | string<br><br>Enum: "ADVERTISER" "ADVERTISER\_TARGETING" "CAMPAIGN" "CAMPAIGN\_TARGETING" "AD\_GROUP" "AD\_GROUP\_TARGETING" "PIN\_PROMOTION" "PIN\_PROMOTION\_TARGETING" "KEYWORD" "PRODUCT\_GROUP" "PRODUCT\_GROUP\_TARGETING" "PRODUCT\_ITEM"<br><br>Level of the report |
| report\_format | string<br><br>Default: "JSON"<br><br>Enum: "JSON" "CSV"<br><br>Specification for formatting the report data. Reports in JSON will not zero-fill metrics, whereas reports in CSV will. Both report formats will omit rows where all the columns are equal to 0. |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/reports

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "granularity": "TOTAL",      * "click_window_days": 0,      * "engagement_window_days": 0,      * "view_window_days": 0,      * "conversion_report_time": "TIME_OF_AD_ACTION",      * "attribution_types": [          * "INDIVIDUAL"                   ],      * "campaign_ids": [          * "12345678"                   ],      * "campaign_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "campaign_objective_types": [          * "AWARENESS",              * "VIDEO_VIEW"                   ],      * "ad_group_ids": [          * "12345678"                   ],      * "ad_group_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "ad_ids": [          * "12345678"                   ],      * "ad_statuses": [          * "APPROVED",              * "PAUSED"                   ],      * "product_group_ids": [          * "12345678"                   ],      * "product_group_statuses": [          * "RUNNING",              * "PAUSED"                   ],      * "product_item_ids": [          * "12345678"                   ],      * "targeting_types": [          * "APPTYPE"                   ],      * "metrics_filters": [          * {                  * "field": "SPEND_IN_DOLLAR",                      * "operator": "LESS_THAN",                      * "values": [                          * 0                                           ]                               }                   ],      * "columns": [          * "SPEND_IN_MICRO_DOLLAR"                   ],      * "level": "CAMPAIGN",      * "report_format": "JSON"       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_status": "FINISHED",      * "token": "string",      * "message": "string"       }`

[](#operation/sandbox/delete)Delete ads data for ad account in API Sandbox
--------------------------------------------------------------------------

Delete an ad account and all the ads data associated with that account. A string message is returned indicating the status of the delete operation.

Note: This endpoint is only allowed in the Pinterest API Sandbox ([https://api-sandbox.pinterest.com/v5](https://api-sandbox.pinterest.com/v5)). Go to [https://developers.pinterest.com/docs/dev-tools/sandbox/](https://developers.pinterest.com/docs/dev-tools/sandbox/) for more information.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

OK

**400**

Invalid ad account id.

**default**

Unexpected error

delete/ad\_accounts/{ad\_account\_id}/sandbox

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/sandbox

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`"Delete Success"`

[](#operation/ssio_accounts/get)Get Salesforce account details including bill-to information.
---------------------------------------------------------------------------------------------

Get Salesforce account details including bill-to information to be used in insertion orders process for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid request parameter.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/accounts

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/accounts

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "eligible": true,      * "can_edit": true,      * "billto_infos": [          * {                  * "id": "0011N00001LW8kAQAT",                      * "io_terms_id": "a2S1N000000bKHgUAM",                      * "io_terms": "The IO is governed by the terms available at https://business.pinterest.com/en/pinterest-advertising-services-agreement/. If a budget is listed on this IO, the parties agree that Advertiser (or if applicable, its Agency) may apply any of the budget to any auction bid type or ad product. Price will be determined by auction closing price, plus any applicable non-auction fees. The terms of the Agreement supersede any terms on this IO. ANY ADDITIONAL TERMS AND CONDITIONS ON THIS IO ARE NULL AND VOID.",                      * "us_terms_id": "a2S1N000000bKIOUA2",                      * "us_terms": "This Insertion Order (\"IO\") is subject to the Pinterest Addendum To IAB Standard Terms and Conditions for Internet Advertising For Media Buys One Year or Less (Version 3.0), as executed by Pinterest, Inc. and GroupM Worldwide LLC on May 7, 2014 and Amendment No. 1 to Pinterest Addendum to IAB Standard Terms and Conditions for Internet Advertising For Media Buys One Year or Less (Version 3.0) as executed by Pinterest, Inc. and GroupM Worldwide LLC on August 20, 2015. The parties agree that Agency may apply any of the budget listed on this IO to any auction bid type or ad product. Price will be determined by auction closing price, plus any applicable non-auction fees.The terms of the Addendum supersede any terms on this IO. ANY ADDITIONAL TERMS AND CONDITIONS ON THIS IO ARE NULL AND VOID.",                      * "row_terms_id": "a2S1N000000bKHhUAM",                      * "row_terms": "The IO is governed by the terms available at\r\nhttps://business.pinterest.com/en-gb/pinterest-advertising-services-agreement",                      * "io_type": "Pinterest Paper",                      * "addresses": [                          * {                                  * "display": "475 Brannan Street, San Francisco, CA 94103",                                      * "purpose": "Billing",                                      * "address_id": "a1C1N000004MUrLUAW",                                      * "order_legal_entity": "PIN US OU"                                                       }                                           ]                               }                   ],      * "currency": "USD",      * "pmp_names": [          * {                  * "name": "Bidalgo",                      * "id": "0011N00001LW2aSQAT"                               }                   ],      * "error": "No Error"       }`

[](#operation/ssio_insertion_order/create)Create insertion order through SSIO.
------------------------------------------------------------------------------

Create insertion order through SSIO for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Order line to create.

|     |     |
| --- | --- |
| start\_date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Starting date of time period. Format: YYYY-MM-DD |
| end\_date | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>End date of time period. Format: YYYY-MM-DD |
| po\_number<br><br>required | string<br><br>The po number |
| budget\_amount | number<br><br>If Budget order line, the budget amount. |
| billing\_contact\_firstname<br><br>required | string<br><br>The billing contact first name |
| billing\_contact\_lastname<br><br>required | string<br><br>The billing contact last name |
| billing\_contact\_email<br><br>required | string<br><br>The billing contact email |
| media\_contact\_firstname<br><br>required | string<br><br>The media contact first name |
| media\_contact\_lastname<br><br>required | string<br><br>The media contact last name |
| media\_contact\_email<br><br>required | string<br><br>The media contact email |
| agency\_link | string<br><br>URL link for agency |
| user\_email | string<br><br>The email of user submitting the insertion order |
| accepted\_terms\_time | integer<br><br>The UTC timestamp (to the nearest sec) of when terms were accepted |
| pmp\_id<br><br>required | string<br><br>The pmp id |
| order\_name<br><br>required | string<br><br>The order name |
| order\_line\_type<br><br>required | string<br><br>Enum: "BUDGET" "PERPETUALS"<br><br>Type can be Budget or Perpetual |
| accepted\_terms\_id<br><br>required | string<br><br>The SFDC id for the terms |
| billto\_company\_id<br><br>required | string<br><br>The bill-to company id |
| billto\_business\_address\_id<br><br>required | string<br><br>The bill-to business address id |
| billto\_billing\_address\_id<br><br>required | string<br><br>The bill-to billing address id |
| estimated\_monthly\_spend | number<br><br>If Ongoing (perpetual) order line, the estimated monthly spend |
| currency\_info<br><br>required | string (Currency)<br><br>Enum: "UNK" "USD" "GBP" "CAD" "EUR" "AUD" "NZD" "SEK" "ILS" "CHF" "HKD" "JPY" "SGD" "KRW" "NOK" "DKK" "PLN" "RON" "HUF" "CZK" … 5 more<br><br>Currency Codes from ISO 4217 |

### Responses

**200**

Success

**400**

Invalid request.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "po_number": "string",      * "budget_amount": 5000000,      * "billing_contact_firstname": "string",      * "billing_contact_lastname": "string",      * "billing_contact_email": "test@example",      * "media_contact_firstname": "string",      * "media_contact_lastname": "string",      * "media_contact_email": "test@example",      * "agency_link": "string",      * "user_email": "test@example",      * "accepted_terms_time": 0,      * "pmp_id": "string",      * "order_name": "string",      * "order_line_type": "BUDGET",      * "accepted_terms_id": "string",      * "billto_company_id": "string",      * "billto_business_address_id": "string",      * "billto_billing_address_id": "string",      * "estimated_monthly_spend": 0,      * "currency_info": "USD"       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "pin_order_id": "string"       }`

[](#operation/ssio_insertion_order/edit)Edit insertion order through SSIO.
--------------------------------------------------------------------------

Edit insertion order through SSIO for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Order line to create.

|     |     |
| --- | --- |
| start\_date | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Starting date of time period. Format: YYYY-MM-DD |
| end\_date | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>End date of time period. Format: YYYY-MM-DD |
| po\_number | string<br><br>The po number |
| budget\_amount | number<br><br>If Budget order line, the budget amount. |
| billing\_contact\_firstname | string<br><br>The billing contact first name |
| billing\_contact\_lastname | string<br><br>The billing contact last name |
| billing\_contact\_email | string<br><br>The billing contact email |
| media\_contact\_firstname | string<br><br>The media contact first name |
| media\_contact\_lastname | string<br><br>The media contact last name |
| media\_contact\_email | string<br><br>The media contact email |
| agency\_link | string<br><br>URL link for agency |
| user\_email | string<br><br>The email of user submitting the insertion order |
| oracle\_line\_id | string<br><br>LineId in the Oracle DB |
| salesforce\_order\_id | string<br><br>OrderId in SFDC |
| salesforce\_order\_line\_id | string<br><br>OrderLineId in SFDC |
| ads\_manager\_order\_line\_id | string<br><br>Ads manager OrderLineId |

### Responses

**200**

Success

**400**

Invalid request.

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "start_date": "2020-12-20",      * "end_date": "2020-12-20",      * "po_number": "string",      * "budget_amount": 5000000,      * "billing_contact_firstname": "string",      * "billing_contact_lastname": "string",      * "billing_contact_email": "test@example",      * "media_contact_firstname": "string",      * "media_contact_lastname": "string",      * "media_contact_email": "test@example",      * "agency_link": "string",      * "user_email": "test@example",      * "oracle_line_id": "string",      * "salesforce_order_id": "string",      * "salesforce_order_line_id": "string",      * "ads_manager_order_line_id": "string"       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "pin_order_id": "string"       }`

[](#operation/ssio_insertion_orders_status/get_by_ad_account)Get insertion order status by ad account id.
---------------------------------------------------------------------------------------------------------

Get insertion order status for account id `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**400**

Invalid request parameter.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/status

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/status

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "pin_order_id": "0Q01N0000015hekSAB",                      * "status": "Approved",                      * "creation_time": "2017-06-21T23:11:11.000Z"                               }                   ],      * "bookmark": "string"       }`

[](#operation/ssio_insertion_orders_status/get_by_pin_order_id)Get insertion order status by pin order id.
----------------------------------------------------------------------------------------------------------

Get insertion order status for pin order id `pin_order_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| pin\_order\_id<br><br>required | string<br><br>Example: 0Q01N0000015hekSVDFDC<br><br>The pin order id associated with the ssio insertion order |

### Responses

**200**

Success

**400**

Invalid request parameter.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/{pin\_order\_id}/status

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/{pin\_order\_id}/status

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "pin_order_id": "0Q01N0000015hekSAB",      * "status": "Approved",      * "creation_time": "2017-06-21T23:11:11.000Z"       }`

[](#operation/ssio_order_lines/get_by_ad_account)Get Salesforce order lines by ad account id.
---------------------------------------------------------------------------------------------

Get Salesforce order lines for account id `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Finance, Campaign.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| pin\_order\_id | string<br><br>Example: pin\_order\_id=0Q01N0000015hekSVDFDC<br><br>The pin order id associated with the ssio insertino order |

### Responses

**200**

Success

**400**

Invalid request parameter.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/order\_lines

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/order\_lines

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "salesforce_order_line_id": "string",                      * "ads_manager_order_line_id": "string",                      * "pin_order_id": "string",                      * "last_modified_date_time": "2020-10-06T13:07:04.000Z",                      * "start_date": "2018-03-01",                      * "end_date": "2020-10-05",                      * "bill_to_company_name": "Home Depot Inc.",                      * "billing_contact_firstname": "Mary",                      * "billing_contact_lastname": "Smith",                      * "billing_contact_email": "mail@test.com",                      * "media_contact_email": "mail@test.com",                      * "media_contact_firstname": "John",                      * "media_contact_lastname": "Doe",                      * "currency_info": "USD",                      * "agency_link": "",                      * "po_number": "string",                      * "order_name": "string",                      * "pmp_name": "string",                      * "accepted_terms_id": "string",                      * "accepted_terms_time": "2020-10-06T13:07:04.000Z",                      * "budget_amount": 5000000,                      * "estimated_monthly_spend": 0                               }                   ],      * "bookmark": "string"       }`

[](#operation/ad_account_targeting_analytics/get)Get targeting analytics for an ad account
------------------------------------------------------------------------------------------

Get targeting analytics for an ad account. For the requested account and metrics, the response will include the requested metric information (e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49").

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| targeting\_types<br><br>required | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 15 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>Example: targeting\_types=APPTYPE<br><br>Targeting type breakdowns for the report. The reporting per targeting type  <br>is independent from each other. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | string (ConversionReportAttributionType)<br><br>Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>Example: attribution\_types=INDIVIDUAL<br><br>List of types of attribution for the conversion report |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/targeting\_analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/targeting\_analytics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "targeting_type": "KEYWORD",                      * "targeting_value": "christmas decor ideas",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "iphone",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "ipad",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_tablet",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GENDER",                      * "targeting_value": "female",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "LOCATION",                      * "targeting_value": 500,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PLACEMENT",                      * "targeting_value": "SEARCH",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "COUNTRY",                      * "targeting_value": "US",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "TARGETED_INTEREST",                      * "targeting_value": "Food and Drinks",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PINNER_INTEREST",                      * "targeting_value": "Chocolate Cookies",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AUDIENCE_INCLUDE",                      * "targeting_value": 254261234567,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GEO",                      * "targeting_value": "US:94102",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AGE_BUCKET",                      * "targeting_value": "45-49",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "REGION",                      * "targeting_value": "US-CA",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               }                   ]       }`

[](#operation/templates/list)List templates
-------------------------------------------

Gets all Templates associated with an ad account ID.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**400**

Invalid ad account template parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/templates

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/templates

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "6739202847590",                      * "ad_account_id": "547664674848",                      * "ad_account_ids": [                          * "547664674848"                                           ],                      * "user_id": "784762938748396",                      * "name": "Week over week spend",                      * "report_start_relative_days_in_past": 7,                      * "report_end_relative_days_in_past": 7,                      * "date_range": {                          * "dynamic_date_range": {                                  * "range": "YEAR_TO_DATE",                                      * "type": "dynamic"                                                       },                              * "relative_date_range": {                                  * "end_days_in_past": 7,                                      * "type": "relative",                                      * "start_days_in_past": 14                                                       },                              * "absolute_date_range": {                                  * "end_date": 6.027456183070403,                                      * "type": "absolute",                                      * "start_date": 0.8008281904610115                                                       }                                           },                      * "report_level": "CAMPAIGN",                      * "report_format": "JSON",                      * "columns": [                          * "SPEND_IN_DOLLAR"                                           ],                      * "granularity": "TOTAL",                      * "view_window_days": 7,                      * "click_window_days": 7,                      * "engagement_window_days": 7,                      * "conversion_report_time_type": "TIME_OF_AD_ACTION",                      * "filters_json": "[{\"field\": \"SPEND_IN_DOLLAR\", \"operator\": \"=\", \"value\": 100}]",                      * "is_owned_by_user": true,                      * "is_scheduled": true,                      * "creation_source": "ADS_MANAGER_REPORT_BUILDER",                      * "is_deleted": false,                      * "updated_time": 1432744744,                      * "custom_column_ids": [                          * "1597252063"                                           ],                      * "type": "BULK",                      * "ingestion_sources": [                          * "CONVERSIONS_API"                                           ]                               }                   ],      * "bookmark": "string"       }`

[](#operation/analytics/create_template_report)Create async request for an analytics report using a template
------------------------------------------------------------------------------------------------------------

This takes a template ID and an optional custom timeframe and constructs an asynchronous report based on the template. It returns a token that you can use to download the report when it is ready.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| template\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of a template. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years back from today. |
| end\_date | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years past start date. |
| granularity | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics template parameters.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reports

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reports

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "report_status": "FINISHED",      * "token": "string",      * "message": "string"       }`

[](#tag/ad_groups)ad\_groups
============================

View, create or update ad groups.

[](#operation/ad_groups/list)List ad groups
-------------------------------------------

List ad groups based on provided campaign IDs or ad group IDs.(campaign\_ids or ad\_group\_ids).

**Note:**

Provide only campaign\_id or ad\_group\_id. Do not provide both.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| ad\_group\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad group Ids to use to filter the results. |
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| translate\_interests\_to\_names | boolean<br><br>Default: false<br><br>Return interests as text names (if value is true) rather than topic IDs. |

### Responses

**200**

Success

**400**

Invalid ad account group parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "name": "Ad Group For Pin: 687195905986",                      * "status": "ACTIVE",                      * "budget_in_micro_currency": 5000000,                      * "bid_in_micro_currency": 5000000,                      * "optimization_goal_metadata": {                          * "conversion_tag_v3_goal_metadata": {                                  * "attribution_windows": {                                          * "click_window_days": 0,                                              * "engagement_window_days": 0,                                              * "view_window_days": 0                                                                   },                                      * "conversion_event": "PAGE_VISIT",                                      * "conversion_tag_id": "string",                                      * "cpa_goal_value_in_micro_currency": "string",                                      * "is_roas_optimized": true,                                      * "learning_mode_type": "ACTIVE"                                                       },                              * "frequency_goal_metadata": {                                  * "frequency": 0,                                      * "timerange": "DAY"                                                       },                              * "scrollup_goal_metadata": {                                  * "scrollup_goal_value_in_micro_currency": "string"                                                       }                                           },                      * "budget_type": "DAILY",                      * "start_time": 5686848000,                      * "end_time": 5705424000,                      * "targeting_spec": {                          * "AGE_BUCKET": [                                  * "35-44",                                      * "50-54"                                                       ],                              * "APPTYPE": [                                  * "ipad",                                      * "iphone"                                                       ],                              * "AUDIENCE_EXCLUDE": [                                  * "string"                                                       ],                              * "AUDIENCE_INCLUDE'": [                                  * "string"                                                       ],                              * "GENDER": [                                  * "unknown"                                                       ],                              * "GEO": [                                  * "string"                                                       ],                              * "INTEREST": [                                  * "string"                                                       ],                              * "LOCALE": [                                  * "string"                                                       ],                              * "LOCATION": [                                  * "string"                                                       ],                              * "SHOPPING_RETARGETING": [                                  * {                                          * "lookback_window": 30,                                              * "exclusion_window": 14,                                              * "tag_types": [                                                  * 0,                                                      * 6                                                                               ]                                                                   }                                                       ],                              * "TARGETING_STRATEGY": [                                  * "CHOOSE_YOUR_OWN"                                                       ]                                           },                      * "lifetime_frequency_cap": 100,                      * "tracking_urls": {                          * "impression": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "click": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "engagement": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "buyable_button": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "audience_verification": [                                  * "URL1",                                      * "URL2"                                                       ]                                           },                      * "auto_targeting_enabled": true,                      * "placement_group": "ALL",                      * "pacing_delivery_type": "STANDARD",                      * "campaign_id": "626736533506",                      * "billable_event": "CLICKTHROUGH",                      * "bid_strategy_type": "MAX_BID",                      * "id": "2680060704746",                      * "ad_account_id": "549755885175",                      * "created_time": 1476477189,                      * "updated_time": 1476477189,                      * "type": "adgroup",                      * "conversion_learning_mode_type": "ACTIVE",                      * "summary_status": "RUNNING",                      * "feed_profile_id": "626736533506",                      * "dca_assets": null                               }                   ],      * "bookmark": "string"       }`

[](#operation/ad_groups/create)Create ad groups
-----------------------------------------------

Create multiple new ad groups. All ads in a given ad group will have the same budget, bid, run dates, targeting, and placement (search, browse, other). For more information, [click here](https://help.pinterest.com/en/business/article/campaign-structure).

**Note:**

* 'bid\_in\_micro\_currency' and 'budget\_in\_micro\_currency' should be expressed in microcurrency amounts based on the currency field set in the advertiser's profile.
    
    Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.
    
    A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.
    
    **Equivalency equations**, using dollars as an example currency:
    
    * $1 = 1,000,000 microdollars
    * 1 microdollar = $0.000001
    
    **To convert between currency and microcurrency**, using dollars as an example currency:
    
    * To convert dollars to microdollars, mutiply dollars by 1,000,000
    * To convert microdollars to dollars, divide microdollars by 1,000,000
* Ad groups belong to ad campaigns. Some types of campaigns (e.g. budget optimization) have limits on the number of ad groups they can hold. If you exceed those limits, you will get an error message.
* Start and end time cannot be set for ad groups that belong to CBO campaigns. Currently, campaigns with the following objective types: TRAFFIC, AWARENESS, WEB\_CONVERSIONS, and CATALOG\_SALES will default to CBO.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ad groups to create, size limit \[1, 30\].

Array ()

|     |     |
| --- | --- |
| name<br><br>required | string<br><br>Ad group name. |
| status | string<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Ad group/entity status. |
| budget\_in\_micro\_currency | integer Nullable<br><br>Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups. |
| bid\_in\_micro\_currency | integer Nullable<br><br>Bid price in micro currency. This field is **REQUIRED** for the following campaign objective\_type/billable\_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG\_SALES/CLICKTHROUGH, VIDEO\_VIEW/VIDEO\_V\_50\_MRC. |
| optimization\_goal\_metadata | object Nullable<br><br>Optimization goals for objective-based performance campaigns. **REQUIRED** when campaign's `objective_type` is set to `"WEB_CONVERSION"`. |
| budget\_type | string<br><br>Default: "DAILY"<br><br>Enum: "DAILY" "LIFETIME" "CBO\_ADGROUP"<br><br>Budget type. If DAILY, an ad group's daily spend will not exceed the budget parameter value. If LIFETIME, the end\_time parameter is **REQUIRED**, and the ad group spend is spread evenly between the ad group `start_time` and `end_time` range. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. For CBO campaigns, only "CBO\_ADGROUP" is allowed. For WEB\_SESSIONS campaigns, only "LIFETIME" is allowed. |
| start\_time | integer Nullable<br><br>Ad group start time. Unix timestamp in seconds. Defaults to current time. |
| end\_time | integer Nullable<br><br>Ad group end time. Unix timestamp in seconds. |
| targeting\_spec | object (TargetingSpec)<br><br>Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":\["iphone"\], "GENDER":\["male"\], "LOCALE":\["en-US"\], "LOCATION":\["501"\], "AGE\_BUCKET":\["25-34"\]} |
| lifetime\_frequency\_cap | integer<br><br>Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions)) ad groups. A CPM ad group has an IMPRESSION [billable\_event](https://developers.pinterest.com/docs/redoc/#section/Billable-event) value. This field **REQUIRES** the `end_time` field. |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs.  <br>JSON object with the format: {"[Tracking event enum](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)":\[URL string array\],...}  <br>For example: {"impression": \["URL1", "URL2"\], "click": \["URL1", "URL2", "URL3"\]}.  <br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs.  <br>  <br>For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| auto\_targeting\_enabled | boolean Nullable<br><br>Default: true<br><br>Enable auto-targeting for ad group. Also known as ["expanded targeting"](https://help.pinterest.com/en/business/article/expanded-targeting). |
| placement\_group | string<br><br>Enum: "ALL" "SEARCH" "BROWSE" "OTHER"<br><br>[Placement group](https://developers.pinterest.com/docs/redoc/#section/Placement-group). |
| pacing\_delivery\_type | string<br><br>Default: "STANDARD"<br><br>Enum: "STANDARD" "ACCELERATED"<br><br>Ad group pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day. When using CBO, only the STANDARD pacing delivery type is allowed. |
| campaign\_id<br><br>required | string^\[C\]?\\d+$<br><br>Campaign ID of the ad group. |
| billable\_event<br><br>required | string (ActionType)<br><br>Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO\_V\_50\_MRC"<br><br>Ad group billable event type. |
| bid\_strategy\_type | string (BidStrategyType) Nullable<br><br>Enum: "AUTOMATIC\_BID" "MAX\_BID" "TARGET\_AVG" null<br><br>Bid strategy type |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ad\_groups

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "name": "Ad Group For Pin: 687195905986",              * "status": "ACTIVE",              * "budget_in_micro_currency": 5000000,              * "bid_in_micro_currency": 5000000,              * "optimization_goal_metadata": {                  * "conversion_tag_v3_goal_metadata": {                          * "attribution_windows": {                                  * "click_window_days": 0,                                      * "engagement_window_days": 0,                                      * "view_window_days": 0                                                       },                              * "conversion_event": "PAGE_VISIT",                              * "conversion_tag_id": "string",                              * "cpa_goal_value_in_micro_currency": "string",                              * "is_roas_optimized": true,                              * "learning_mode_type": "ACTIVE"                                           },                      * "frequency_goal_metadata": {                          * "frequency": 0,                              * "timerange": "DAY"                                           },                      * "scrollup_goal_metadata": {                          * "scrollup_goal_value_in_micro_currency": "string"                                           }                               },              * "budget_type": "DAILY",              * "start_time": 5686848000,              * "end_time": 5705424000,              * "targeting_spec": {                  * "AGE_BUCKET": [                          * "35-44",                              * "50-54"                                           ],                      * "APPTYPE": [                          * "ipad",                              * "iphone"                                           ],                      * "AUDIENCE_EXCLUDE": [                          * "string"                                           ],                      * "AUDIENCE_INCLUDE'": [                          * "string"                                           ],                      * "GENDER": [                          * "unknown"                                           ],                      * "GEO": [                          * "string"                                           ],                      * "INTEREST": [                          * "string"                                           ],                      * "LOCALE": [                          * "string"                                           ],                      * "LOCATION": [                          * "string"                                           ],                      * "SHOPPING_RETARGETING": [                          * {                                  * "lookback_window": 30,                                      * "exclusion_window": 14,                                      * "tag_types": [                                          * 0,                                              * 6                                                                   ]                                                       }                                           ],                      * "TARGETING_STRATEGY": [                          * "CHOOSE_YOUR_OWN"                                           ]                               },              * "lifetime_frequency_cap": 100,              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "auto_targeting_enabled": true,              * "placement_group": "ALL",              * "pacing_delivery_type": "STANDARD",              * "campaign_id": "626736533506",              * "billable_event": "CLICKTHROUGH",              * "bid_strategy_type": "MAX_BID"                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "name": "Ad Group For Pin: 687195905986",                              * "status": "ACTIVE",                              * "budget_in_micro_currency": 5000000,                              * "bid_in_micro_currency": 5000000,                              * "optimization_goal_metadata": {                                  * "conversion_tag_v3_goal_metadata": {                                          * "attribution_windows": {                                                  * "click_window_days": 0,                                                      * "engagement_window_days": 0,                                                      * "view_window_days": 0                                                                               },                                              * "conversion_event": "PAGE_VISIT",                                              * "conversion_tag_id": "string",                                              * "cpa_goal_value_in_micro_currency": "string",                                              * "is_roas_optimized": true,                                              * "learning_mode_type": "ACTIVE"                                                                   },                                      * "frequency_goal_metadata": {                                          * "frequency": 0,                                              * "timerange": "DAY"                                                                   },                                      * "scrollup_goal_metadata": {                                          * "scrollup_goal_value_in_micro_currency": "string"                                                                   }                                                       },                              * "budget_type": "DAILY",                              * "start_time": 5686848000,                              * "end_time": 5705424000,                              * "targeting_spec": {                                  * "AGE_BUCKET": [                                          * "35-44",                                              * "50-54"                                                                   ],                                      * "APPTYPE": [                                          * "ipad",                                              * "iphone"                                                                   ],                                      * "AUDIENCE_EXCLUDE": [                                          * "string"                                                                   ],                                      * "AUDIENCE_INCLUDE'": [                                          * "string"                                                                   ],                                      * "GENDER": [                                          * "unknown"                                                                   ],                                      * "GEO": [                                          * "string"                                                                   ],                                      * "INTEREST": [                                          * "string"                                                                   ],                                      * "LOCALE": [                                          * "string"                                                                   ],                                      * "LOCATION": [                                          * "string"                                                                   ],                                      * "SHOPPING_RETARGETING": [                                          * {                                                  * "lookback_window": 30,                                                      * "exclusion_window": 14,                                                      * "tag_types": [                                                          * 0,                                                              * 6                                                                                           ]                                                                               }                                                                   ],                                      * "TARGETING_STRATEGY": [                                          * "CHOOSE_YOUR_OWN"                                                                   ]                                                       },                              * "lifetime_frequency_cap": 100,                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "auto_targeting_enabled": true,                              * "placement_group": "ALL",                              * "pacing_delivery_type": "STANDARD",                              * "campaign_id": "626736533506",                              * "billable_event": "CLICKTHROUGH",                              * "bid_strategy_type": "MAX_BID",                              * "id": "2680060704746",                              * "ad_account_id": "549755885175",                              * "created_time": 1476477189,                              * "updated_time": 1476477189,                              * "type": "adgroup",                              * "conversion_learning_mode_type": "ACTIVE",                              * "summary_status": "RUNNING",                              * "feed_profile_id": "626736533506",                              * "dca_assets": null                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/ad_groups/update)Update ad groups
-----------------------------------------------

Update multiple existing ad groups.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ad groups to update, size limit \[1, 30\].

Array ()

|     |     |
| --- | --- |
| name | string<br><br>Ad group name. |
| status | string<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Ad group/entity status. |
| budget\_in\_micro\_currency | integer Nullable<br><br>Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups. |
| bid\_in\_micro\_currency | integer Nullable<br><br>Bid price in micro currency. This field is **REQUIRED** for the following campaign objective\_type/billable\_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG\_SALES/CLICKTHROUGH, VIDEO\_VIEW/VIDEO\_V\_50\_MRC. |
| optimization\_goal\_metadata | object Nullable<br><br>Optimization goals for objective-based performance campaigns. **REQUIRED** when campaign's `objective_type` is set to `"WEB_CONVERSION"`. |
| budget\_type | string<br><br>Enum: "DAILY" "LIFETIME" "CBO\_ADGROUP"<br><br>Budget type. If DAILY, an ad group's daily spend will not exceed the budget parameter value. If LIFETIME, the end\_time parameter is **REQUIRED**, and the ad group spend is spread evenly between the ad group `start_time` and `end_time` range. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. For CBO campaigns, only "CBO\_ADGROUP" is allowed. For WEB\_SESSIONS campaigns, only "LIFETIME" is allowed. |
| start\_time | integer Nullable<br><br>Ad group start time. Unix timestamp in seconds. Defaults to current time. |
| end\_time | integer Nullable<br><br>Ad group end time. Unix timestamp in seconds. |
| targeting\_spec | object (TargetingSpec)<br><br>Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":\["iphone"\], "GENDER":\["male"\], "LOCALE":\["en-US"\], "LOCATION":\["501"\], "AGE\_BUCKET":\["25-34"\]} |
| lifetime\_frequency\_cap | integer<br><br>Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions)) ad groups. A CPM ad group has an IMPRESSION [billable\_event](https://developers.pinterest.com/docs/redoc/#section/Billable-event) value. This field **REQUIRES** the `end_time` field. |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs.  <br>JSON object with the format: {"[Tracking event enum](https://developers.pinterest.com/docs/redoc/#section/Tracking-URL-event)":\[URL string array\],...}  <br>For example: {"impression": \["URL1", "URL2"\], "click": \["URL1", "URL2", "URL3"\]}.  <br>Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs.  <br>  <br>For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| auto\_targeting\_enabled | boolean Nullable<br><br>Enable auto-targeting for ad group. Also known as ["expanded targeting"](https://help.pinterest.com/en/business/article/expanded-targeting). |
| placement\_group | string<br><br>Enum: "ALL" "SEARCH" "BROWSE" "OTHER"<br><br>[Placement group](https://developers.pinterest.com/docs/redoc/#section/Placement-group). |
| pacing\_delivery\_type | string<br><br>Enum: "STANDARD" "ACCELERATED"<br><br>Ad group pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day. When using CBO, only the STANDARD pacing delivery type is allowed. |
| campaign\_id | string^\[C\]?\\d+$<br><br>Campaign ID of the ad group. |
| billable\_event | string (ActionType)<br><br>Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO\_V\_50\_MRC"<br><br>Ad group billable event type. |
| bid\_strategy\_type | string (BidStrategyType) Nullable<br><br>Enum: "AUTOMATIC\_BID" "MAX\_BID" "TARGET\_AVG" null<br><br>Bid strategy type |
| id<br><br>required | string^\\d+$<br><br>Ad group ID. |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/ad\_groups

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "name": "Ad Group For Pin: 687195905986",              * "status": "ACTIVE",              * "budget_in_micro_currency": 5000000,              * "bid_in_micro_currency": 5000000,              * "optimization_goal_metadata": {                  * "conversion_tag_v3_goal_metadata": {                          * "attribution_windows": {                                  * "click_window_days": 0,                                      * "engagement_window_days": 0,                                      * "view_window_days": 0                                                       },                              * "conversion_event": "PAGE_VISIT",                              * "conversion_tag_id": "string",                              * "cpa_goal_value_in_micro_currency": "string",                              * "is_roas_optimized": true,                              * "learning_mode_type": "ACTIVE"                                           },                      * "frequency_goal_metadata": {                          * "frequency": 0,                              * "timerange": "DAY"                                           },                      * "scrollup_goal_metadata": {                          * "scrollup_goal_value_in_micro_currency": "string"                                           }                               },              * "budget_type": "DAILY",              * "start_time": 5686848000,              * "end_time": 5705424000,              * "targeting_spec": {                  * "AGE_BUCKET": [                          * "35-44",                              * "50-54"                                           ],                      * "APPTYPE": [                          * "ipad",                              * "iphone"                                           ],                      * "AUDIENCE_EXCLUDE": [                          * "string"                                           ],                      * "AUDIENCE_INCLUDE'": [                          * "string"                                           ],                      * "GENDER": [                          * "unknown"                                           ],                      * "GEO": [                          * "string"                                           ],                      * "INTEREST": [                          * "string"                                           ],                      * "LOCALE": [                          * "string"                                           ],                      * "LOCATION": [                          * "string"                                           ],                      * "SHOPPING_RETARGETING": [                          * {                                  * "lookback_window": 30,                                      * "exclusion_window": 14,                                      * "tag_types": [                                          * 0,                                              * 6                                                                   ]                                                       }                                           ],                      * "TARGETING_STRATEGY": [                          * "CHOOSE_YOUR_OWN"                                           ]                               },              * "lifetime_frequency_cap": 100,              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "auto_targeting_enabled": true,              * "placement_group": "ALL",              * "pacing_delivery_type": "STANDARD",              * "campaign_id": "626736533506",              * "billable_event": "CLICKTHROUGH",              * "bid_strategy_type": "MAX_BID",              * "id": "2680060704746"                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "name": "Ad Group For Pin: 687195905986",                              * "status": "ACTIVE",                              * "budget_in_micro_currency": 5000000,                              * "bid_in_micro_currency": 5000000,                              * "optimization_goal_metadata": {                                  * "conversion_tag_v3_goal_metadata": {                                          * "attribution_windows": {                                                  * "click_window_days": 0,                                                      * "engagement_window_days": 0,                                                      * "view_window_days": 0                                                                               },                                              * "conversion_event": "PAGE_VISIT",                                              * "conversion_tag_id": "string",                                              * "cpa_goal_value_in_micro_currency": "string",                                              * "is_roas_optimized": true,                                              * "learning_mode_type": "ACTIVE"                                                                   },                                      * "frequency_goal_metadata": {                                          * "frequency": 0,                                              * "timerange": "DAY"                                                                   },                                      * "scrollup_goal_metadata": {                                          * "scrollup_goal_value_in_micro_currency": "string"                                                                   }                                                       },                              * "budget_type": "DAILY",                              * "start_time": 5686848000,                              * "end_time": 5705424000,                              * "targeting_spec": {                                  * "AGE_BUCKET": [                                          * "35-44",                                              * "50-54"                                                                   ],                                      * "APPTYPE": [                                          * "ipad",                                              * "iphone"                                                                   ],                                      * "AUDIENCE_EXCLUDE": [                                          * "string"                                                                   ],                                      * "AUDIENCE_INCLUDE'": [                                          * "string"                                                                   ],                                      * "GENDER": [                                          * "unknown"                                                                   ],                                      * "GEO": [                                          * "string"                                                                   ],                                      * "INTEREST": [                                          * "string"                                                                   ],                                      * "LOCALE": [                                          * "string"                                                                   ],                                      * "LOCATION": [                                          * "string"                                                                   ],                                      * "SHOPPING_RETARGETING": [                                          * {                                                  * "lookback_window": 30,                                                      * "exclusion_window": 14,                                                      * "tag_types": [                                                          * 0,                                                              * 6                                                                                           ]                                                                               }                                                                   ],                                      * "TARGETING_STRATEGY": [                                          * "CHOOSE_YOUR_OWN"                                                                   ]                                                       },                              * "lifetime_frequency_cap": 100,                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "auto_targeting_enabled": true,                              * "placement_group": "ALL",                              * "pacing_delivery_type": "STANDARD",                              * "campaign_id": "626736533506",                              * "billable_event": "CLICKTHROUGH",                              * "bid_strategy_type": "MAX_BID",                              * "id": "2680060704746",                              * "ad_account_id": "549755885175",                              * "created_time": 1476477189,                              * "updated_time": 1476477189,                              * "type": "adgroup",                              * "conversion_learning_mode_type": "ACTIVE",                              * "summary_status": "RUNNING",                              * "feed_profile_id": "626736533506",                              * "dca_assets": null                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/ad_groups/analytics)Get ad group analytics
--------------------------------------------------------

Get analytics for the specified ad groups in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| ad\_group\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad group Ids to use to filter the results. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |

### Responses

**200**

Success

**400**

Invalid ad account group analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "AD_GROUP_ID": "547602124502",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`

[](#operation/ad_groups_targeting_analytics/get)Get targeting analytics for ad groups
-------------------------------------------------------------------------------------

Get targeting analytics for one or more ad groups. For the requested ad group(s) and metrics, the response will include the requested metric information (e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49").

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_group\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad group Ids to use to filter the results. |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| targeting\_types<br><br>required | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 15 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>Example: targeting\_types=APPTYPE<br><br>Targeting type breakdowns for the report. The reporting per targeting type  <br>is independent from each other. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | string (ConversionReportAttributionType)<br><br>Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>Example: attribution\_types=INDIVIDUAL<br><br>List of types of attribution for the conversion report |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/targeting\_analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/targeting\_analytics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "targeting_type": "KEYWORD",                      * "targeting_value": "christmas decor ideas",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "iphone",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "ipad",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_tablet",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GENDER",                      * "targeting_value": "female",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "LOCATION",                      * "targeting_value": 500,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PLACEMENT",                      * "targeting_value": "SEARCH",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "COUNTRY",                      * "targeting_value": "US",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "TARGETED_INTEREST",                      * "targeting_value": "Food and Drinks",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PINNER_INTEREST",                      * "targeting_value": "Chocolate Cookies",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AUDIENCE_INCLUDE",                      * "targeting_value": 254261234567,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GEO",                      * "targeting_value": "US:94102",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AGE_BUCKET",                      * "targeting_value": "45-49",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "REGION",                      * "targeting_value": "US-CA",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               }                   ]       }`

[](#operation/ad_groups/get)Get ad group
----------------------------------------

Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will contain additional information from the Ad Review process. For more information about our policies and rejection reasons see the [Pinterest advertising standards](https://www.pinterest.com/_/_/policy/advertising-guidelines/).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| ad\_group\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad group. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/{ad\_group\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/{ad\_group\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Ad Group For Pin: 687195905986",      * "status": "ACTIVE",      * "budget_in_micro_currency": 5000000,      * "bid_in_micro_currency": 5000000,      * "optimization_goal_metadata": {          * "conversion_tag_v3_goal_metadata": {                  * "attribution_windows": {                          * "click_window_days": 0,                              * "engagement_window_days": 0,                              * "view_window_days": 0                                           },                      * "conversion_event": "PAGE_VISIT",                      * "conversion_tag_id": "string",                      * "cpa_goal_value_in_micro_currency": "string",                      * "is_roas_optimized": true,                      * "learning_mode_type": "ACTIVE"                               },              * "frequency_goal_metadata": {                  * "frequency": 0,                      * "timerange": "DAY"                               },              * "scrollup_goal_metadata": {                  * "scrollup_goal_value_in_micro_currency": "string"                               }                   },      * "budget_type": "DAILY",      * "start_time": 5686848000,      * "end_time": 5705424000,      * "targeting_spec": {          * "AGE_BUCKET": [                  * "35-44",                      * "50-54"                               ],              * "APPTYPE": [                  * "ipad",                      * "iphone"                               ],              * "AUDIENCE_EXCLUDE": [                  * "string"                               ],              * "AUDIENCE_INCLUDE'": [                  * "string"                               ],              * "GENDER": [                  * "unknown"                               ],              * "GEO": [                  * "string"                               ],              * "INTEREST": [                  * "string"                               ],              * "LOCALE": [                  * "string"                               ],              * "LOCATION": [                  * "string"                               ],              * "SHOPPING_RETARGETING": [                  * {                          * "lookback_window": 30,                              * "exclusion_window": 14,                              * "tag_types": [                                  * 0,                                      * 6                                                       ]                                           }                               ],              * "TARGETING_STRATEGY": [                  * "CHOOSE_YOUR_OWN"                               ]                   },      * "lifetime_frequency_cap": 100,      * "tracking_urls": {          * "impression": [                  * "URL1",                      * "URL2"                               ],              * "click": [                  * "URL1",                      * "URL2"                               ],              * "engagement": [                  * "URL1",                      * "URL2"                               ],              * "buyable_button": [                  * "URL1",                      * "URL2"                               ],              * "audience_verification": [                  * "URL1",                      * "URL2"                               ]                   },      * "auto_targeting_enabled": true,      * "placement_group": "ALL",      * "pacing_delivery_type": "STANDARD",      * "campaign_id": "626736533506",      * "billable_event": "CLICKTHROUGH",      * "bid_strategy_type": "MAX_BID",      * "id": "2680060704746",      * "ad_account_id": "549755885175",      * "created_time": 1476477189,      * "updated_time": 1476477189,      * "type": "adgroup",      * "conversion_learning_mode_type": "ACTIVE",      * "summary_status": "RUNNING",      * "feed_profile_id": "626736533506",      * "dca_assets": null       }`

[](#operation/ad_groups_bid_floor/get)Get bid floors
----------------------------------------------------

List bid floors for your campaign configuration. Bid floors are given in microcurrency values based on the currency in the bid floor specification.

Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.

A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’ s profile.

**Equivalency equations**, using dollars as an example currency:

* $1 = 1,000,000 microdollars
* 1 microdollar = $0.000001

**To convert between currency and microcurrency**, using dollars as an example currency:

* To convert dollars to microdollars, mutiply dollars by 1,000,000
* To convert microdollars to dollars, divide microdollars by 1,000,000

For more on bid floors see [Set your bid](https://help.pinterest.com/en/business/article/set-your-bid).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Parameters to get bid\_floor info

|     |     |
| --- | --- |
| bid\_floor\_specs<br><br>required | Array of objects (bid\_floor\_specs) |
| targeting\_spec | object (TargetingSpec)<br><br>Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":\["iphone"\], "GENDER":\["male"\], "LOCALE":\["en-US"\], "LOCATION":\["501"\], "AGE\_BUCKET":\["25-34"\]} |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/bid\_floor

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bid\_floor

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "targeting_spec": {          * "GEO": [                  * "BE-VOV"                               ],              * "LOCATION": [                  * "US"                               ],              * "LOCALE": [                  * "cs"                               ],              * "AGE_BUCKET": [                  * "25-34"                               ],              * "AUDIENCE_INCLUDE": [                  * "2542620905473"                               ],              * "SHOPPING_RETARGETING": [                  * {                          * "lookback_window": 30,                              * "exclusion_window": 14,                              * "tag_types": [                                  * 0,                                      * 6                                                       ]                                           },                      * {                          * "lookback_window": 30,                              * "exclusion_window": 14,                              * "tag_types": [                                  * 0,                                      * 6                                                       ]                                           }                               ],              * "GENDER": [                  * "male"                               ],              * "TARGETING_STRATEGY": [                  * "CHOOSE_YOUR_OWN"                               ],              * "APPTYPE": [                  * "iphone"                               ],              * "AUDIENCE_EXCLUDE": [                  * "2542620905475"                               ],              * "INTEREST": [                  * "925056443165"                               ]                   },      * "bid_floor_specs": [          * {                  * "billable_event": "CLICKTHROUGH",                      * "creative_type": "REGULAR",                      * "currency": "USD",                      * "countries": [                          * "US",                              * "US"                                           ],                      * "optimization_goal_metadata": {                          * "frequency_goal_metadata": {                                  * "timerange": "DAY",                                      * "frequency": 5                                                       },                              * "conversion_tag_v3_goal_metadata": {                                  * "attribution_windows": {                                          * "view_window_days": 1,                                              * "click_window_days": 0,                                              * "engagement_window_days": 6                                                                   },                                      * "conversion_tag_id": "123456789",                                      * "learning_mode_type": "ACTIVE",                                      * "conversion_event": "PAGE_VISIT",                                      * "is_roas_optimized": true,                                      * "cpa_goal_value_in_micro_currency": "123456789"                                                       },                              * "scrollup_goal_metadata": {                                  * "scrollup_goal_value_in_micro_currency": "123456789"                                                       }                                           }                               },              * {                  * "billable_event": "CLICKTHROUGH",                      * "creative_type": "REGULAR",                      * "currency": "USD",                      * "countries": [                          * "US",                              * "US"                                           ],                      * "optimization_goal_metadata": {                          * "frequency_goal_metadata": {                                  * "timerange": "DAY",                                      * "frequency": 5                                                       },                              * "conversion_tag_v3_goal_metadata": {                                  * "attribution_windows": {                                          * "view_window_days": 1,                                              * "click_window_days": 0,                                              * "engagement_window_days": 6                                                                   },                                      * "conversion_tag_id": "123456789",                                      * "learning_mode_type": "ACTIVE",                                      * "conversion_event": "PAGE_VISIT",                                      * "is_roas_optimized": true,                                      * "cpa_goal_value_in_micro_currency": "123456789"                                                       },                              * "scrollup_goal_metadata": {                                  * "scrollup_goal_value_in_micro_currency": "123456789"                                                       }                                           }                               }                   ]       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "bid_floors": [          * 100000,              * 200000                   ],      * "type": "bidfloor"       }`

[](#tag/ads)ads
===============

View, create or update ads.

[](#operation/ad_previews/create)Create ad preview with pin or image
--------------------------------------------------------------------

Create an ad preview given an ad account ID and either an existing organic pin ID or the URL for an image to be used to create the Pin and the ad.

If you are creating a preview from an existing Pin, that Pin must be promotable: that is, it must have a clickthrough link and meet other requirements. (See [Ads Overview](https://help.pinterest.com/en/business/article/promoted-pins-overview).)

You can view the returned preview URL on a webpage or iframe for 7 days, after which the URL expires.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Create ad preview with pin or image.

One of

AdPreviewCreateFromImageAdPreviewCreateFromPin

|     |     |
| --- | --- |
| image\_url<br><br>required | string (image\_url)<br><br>Image URL. |
| title<br><br>required | string (title)<br><br>Title displayed below ad. |

### Responses

**200**

Successful ad preview creation.

**400**

Invalid Pin parameters response

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ad\_previews

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_previews

### Request samples

* Payload

Content type

application/json

Example

AdPreviewCreateFromImage

AdPreviewCreateFromImage

AdPreviewCreateFromPin

Copy

Expand all Collapse all

`{  * "image_url": "[https://somewebsite.com/someimage.jpg](https://somewebsite.com/someimage.jpg)",      * "title": "My Preview Image"       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "url": "[https://ads.pinterest.com/ad-preview/58f1a0e9ab0bd0f99462a0e4c5dd7e8297888c8a36331e88f757abe8f0295d31/](https://ads.pinterest.com/ad-preview/58f1a0e9ab0bd0f99462a0e4c5dd7e8297888c8a36331e88f757abe8f0295d31/)"       }`

[](#operation/ads/list)List ads
-------------------------------

List ads that meet the filters provided:

* Listed campaign ids or ad group ids or ad ids
* Listed entity statuses
    
    If no filter is provided, all ads in the ad account are returned.
    
    **Note:**
    
    Provide only campaign\_id or ad\_group\_id or ad\_id. Do not provide more than one type.
    
    Review status is provided for each ad; if review\_status is REJECTED, the rejected\_reasons field will contain additional information. For more, see [Pinterest advertising standards](https://policy.pinterest.com/en/advertising-guidelines).
    

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| ad\_group\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad group Ids to use to filter the results. |
| ad\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad Ids to use to filter the results. |
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**400**

Invalid ad account ads parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "ad_group_id": "2680059592705",                      * "android_deep_link": "string",                      * "carousel_android_deep_links": [                          * "string"                                           ],                      * "carousel_destination_urls": [                          * "string"                                           ],                      * "carousel_ios_deep_links": [                          * "string"                                           ],                      * "click_tracking_url": "string",                      * "creative_type": "REGULAR",                      * "destination_url": "string",                      * "ios_deep_link": "string",                      * "is_pin_deleted": false,                      * "is_removable": false,                      * "name": "string",                      * "status": "ACTIVE",                      * "tracking_urls": {                          * "impression": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "click": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "engagement": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "buyable_button": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "audience_verification": [                                  * "URL1",                                      * "URL2"                                                       ]                                           },                      * "view_tracking_url": "string",                      * "lead_form_id": "string",                      * "quiz_pin_data": {                          * "questions": [                                  * {                                          * "question_id": 1,                                              * "question_text": "Where do you thrive?",                                              * "options": [                                                  * {                                                          * "text": "Hangout vibes"                                                                                           },                                                      * {                                                          * "text": "Time to party!"                                                                                           },                                                      * {                                                          * "text": "Keeping it lowkey"                                                                                           }                                                                               ]                                                                   },                                      * {                                          * "question_id": 2,                                              * "question_text": "Where would you nap?",                                              * "options": [                                                  * {                                                          * "text": "Hammock in the mountains"                                                                                           },                                                      * {                                                          * "text": "Beach towel in the sand"                                                                                           },                                                      * {                                                          * "text": "Tent under the stars"                                                                                           }                                                                               ]                                                                   },                                      * {                                          * "question_id": 2,                                              * "question_text": "Who are you taking?",                                              * "options": [                                                  * {                                                          * "text": "No one—solo trip!"                                                                                           },                                                      * {                                                          * "text": "My best friend"                                                                                           },                                                      * {                                                          * "text": "The family"                                                                                           }                                                                               ]                                                                   }                                                       ],                              * "results": [                                  * {                                          * "organicPinId": "1234",                                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "result_id": 1                                                                   },                                      * {                                          * "organicPinId": "1234",                                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "result_id": 2                                                                   },                                      * {                                          * "organicPinId": "1234",                                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                              * "result_id": 3                                                                   }                                                       ]                                           },                      * "pin_id": "394205773611545468",                      * "ad_account_id": "549755885175",                      * "campaign_id": "626735565838",                      * "collection_items_destination_url_template": "string",                      * "created_time": 1451431341,                      * "id": "687195134316",                      * "rejected_reasons": [                          * "HASHTAGS"                                           ],                      * "rejection_labels": [                          * "string"                                           ],                      * "review_status": "PENDING",                      * "type": "pinpromotion",                      * "updated_time": 1451431341,                      * "summary_status": "APPROVED"                               }                   ],      * "bookmark": "string"       }`

[](#operation/ads/create)Create ads
-----------------------------------

Create multiple new ads. Request must contain ad\_group\_id, creative\_type, and the source Pin pin\_id.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ads to create, size limit \[1, 30\].

Array ()

|     |     |
| --- | --- |
| ad\_group\_id<br><br>required | string^(AG)?\\d+$<br><br>ID of the ad group that contains the ad. |
| android\_deep\_link | string Nullable<br><br>Deep link URL for Android devices. Not currently available. Using this field will generate an error. |
| carousel\_android\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on Android. |
| carousel\_destination\_urls | Array of strings Nullable<br><br>Comma-separated destination URLs for the carousel pin to promote. |
| carousel\_ios\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on iOS. |
| click\_tracking\_url | string Nullable<br><br>Tracking url for the ad clicks. |
| creative\_type<br><br>required | string (CreativeType)<br><br>Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA" "SHOWCASE" "QUIZ"<br><br>Ad creative type enum.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| destination\_url | string Nullable<br><br>Destination URL. |
| ios\_deep\_link | string Nullable<br><br>Deep link URL for iOS devices. Not currently available. Using this field will generate an error. |
| is\_pin\_deleted | boolean<br><br>Is original pin deleted? |
| is\_removable | boolean<br><br>Is pin repinnable? |
| name | string Nullable<br><br>Name of the ad - 255 chars max. |
| status | string (EntityStatus)<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Entity status |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| view\_tracking\_url | string Nullable<br><br>Tracking URL for ad impressions. |
| lead\_form\_id | string Nullable ^(AG)?\\d+$<br><br>Lead form ID for lead ad generation. |
| quiz\_pin\_data | object Nullable<br><br>Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved. |
| pin\_id<br><br>required | string^\\d+$<br><br>Pin ID. |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ads

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "ad_group_id": "2680059592705",              * "android_deep_link": "string",              * "carousel_android_deep_links": [                  * "string"                               ],              * "carousel_destination_urls": [                  * "string"                               ],              * "carousel_ios_deep_links": [                  * "string"                               ],              * "click_tracking_url": "string",              * "creative_type": "REGULAR",              * "destination_url": "string",              * "ios_deep_link": "string",              * "is_pin_deleted": false,              * "is_removable": false,              * "name": "string",              * "status": "ACTIVE",              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "view_tracking_url": "string",              * "lead_form_id": "string",              * "quiz_pin_data": {                  * "questions": [                          * {                                  * "question_id": 1,                                      * "question_text": "Where do you thrive?",                                      * "options": [                                          * {                                                  * "text": "Hangout vibes"                                                                               },                                              * {                                                  * "text": "Time to party!"                                                                               },                                              * {                                                  * "text": "Keeping it lowkey"                                                                               }                                                                   ]                                                       },                              * {                                  * "question_id": 2,                                      * "question_text": "Where would you nap?",                                      * "options": [                                          * {                                                  * "text": "Hammock in the mountains"                                                                               },                                              * {                                                  * "text": "Beach towel in the sand"                                                                               },                                              * {                                                  * "text": "Tent under the stars"                                                                               }                                                                   ]                                                       },                              * {                                  * "question_id": 2,                                      * "question_text": "Who are you taking?",                                      * "options": [                                          * {                                                  * "text": "No one—solo trip!"                                                                               },                                              * {                                                  * "text": "My best friend"                                                                               },                                              * {                                                  * "text": "The family"                                                                               }                                                                   ]                                                       }                                           ],                      * "results": [                          * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 1                                                       },                              * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 2                                                       },                              * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 3                                                       }                                           ]                               },              * "pin_id": "394205773611545468"                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "ad_group_id": "2680059592705",                              * "android_deep_link": "string",                              * "carousel_android_deep_links": [                                  * "string"                                                       ],                              * "carousel_destination_urls": [                                  * "string"                                                       ],                              * "carousel_ios_deep_links": [                                  * "string"                                                       ],                              * "click_tracking_url": "string",                              * "creative_type": "REGULAR",                              * "destination_url": "string",                              * "ios_deep_link": "string",                              * "is_pin_deleted": false,                              * "is_removable": false,                              * "name": "string",                              * "status": "ACTIVE",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "view_tracking_url": "string",                              * "lead_form_id": "string",                              * "quiz_pin_data": {                                  * "questions": [                                          * {                                                  * "question_id": 1,                                                      * "question_text": "Where do you thrive?",                                                      * "options": [                                                          * {                                                                  * "text": "Hangout vibes"                                                                                                       },                                                              * {                                                                  * "text": "Time to party!"                                                                                                       },                                                              * {                                                                  * "text": "Keeping it lowkey"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Where would you nap?",                                                      * "options": [                                                          * {                                                                  * "text": "Hammock in the mountains"                                                                                                       },                                                              * {                                                                  * "text": "Beach towel in the sand"                                                                                                       },                                                              * {                                                                  * "text": "Tent under the stars"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Who are you taking?",                                                      * "options": [                                                          * {                                                                  * "text": "No one—solo trip!"                                                                                                       },                                                              * {                                                                  * "text": "My best friend"                                                                                                       },                                                              * {                                                                  * "text": "The family"                                                                                                       }                                                                                           ]                                                                               }                                                                   ],                                      * "results": [                                          * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 1                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 2                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 3                                                                               }                                                                   ]                                                       },                              * "pin_id": "394205773611545468",                              * "ad_account_id": "549755885175",                              * "campaign_id": "626735565838",                              * "collection_items_destination_url_template": "string",                              * "created_time": 1451431341,                              * "id": "687195134316",                              * "rejected_reasons": [                                  * "HASHTAGS"                                                       ],                              * "rejection_labels": [                                  * "string"                                                       ],                              * "review_status": "PENDING",                              * "type": "pinpromotion",                              * "updated_time": 1451431341,                              * "summary_status": "APPROVED"                                           },                      * "exceptions": {                          * "code": 2,                              * "message": "Advertiser not found."                                           }                               }                   ]       }`

[](#operation/ads/update)Update ads
-----------------------------------

Update multiple existing ads

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ads to update, size limit \[1, 30\]

Array ()

|     |     |
| --- | --- |
| ad\_group\_id | string^(AG)?\\d+$<br><br>ID of the ad group that contains the ad. |
| android\_deep\_link | string Nullable<br><br>Deep link URL for Android devices. Not currently available. Using this field will generate an error. |
| carousel\_android\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on Android. |
| carousel\_destination\_urls | Array of strings Nullable<br><br>Comma-separated destination URLs for the carousel pin to promote. |
| carousel\_ios\_deep\_links | Array of strings Nullable<br><br>Comma-separated deep links for the carousel pin on iOS. |
| click\_tracking\_url | string Nullable<br><br>Tracking url for the ad clicks. |
| creative\_type | string (CreativeType)<br><br>Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA" "SHOWCASE" "QUIZ"<br><br>Ad creative type enum.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| destination\_url | string Nullable<br><br>Destination URL. |
| ios\_deep\_link | string Nullable<br><br>Deep link URL for iOS devices. Not currently available. Using this field will generate an error. |
| is\_pin\_deleted | boolean<br><br>Is original pin deleted? |
| is\_removable | boolean<br><br>Is pin repinnable? |
| name | string Nullable<br><br>Name of the ad - 255 chars max. |
| status | string (EntityStatus)<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Entity status |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| view\_tracking\_url | string Nullable<br><br>Tracking URL for ad impressions. |
| lead\_form\_id | string Nullable ^(AG)?\\d+$<br><br>Lead form ID for lead ad generation. |
| quiz\_pin\_data | object Nullable<br><br>Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved. |
| id<br><br>required | string (id) ^\\d+$<br><br>The ID of this ad. |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/ads

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "ad_group_id": "2680059592705",              * "android_deep_link": "string",              * "carousel_android_deep_links": [                  * "string"                               ],              * "carousel_destination_urls": [                  * "string"                               ],              * "carousel_ios_deep_links": [                  * "string"                               ],              * "click_tracking_url": "string",              * "creative_type": "REGULAR",              * "destination_url": "string",              * "ios_deep_link": "string",              * "is_pin_deleted": false,              * "is_removable": false,              * "name": "string",              * "status": "ACTIVE",              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "view_tracking_url": "string",              * "lead_form_id": "string",              * "quiz_pin_data": {                  * "questions": [                          * {                                  * "question_id": 1,                                      * "question_text": "Where do you thrive?",                                      * "options": [                                          * {                                                  * "text": "Hangout vibes"                                                                               },                                              * {                                                  * "text": "Time to party!"                                                                               },                                              * {                                                  * "text": "Keeping it lowkey"                                                                               }                                                                   ]                                                       },                              * {                                  * "question_id": 2,                                      * "question_text": "Where would you nap?",                                      * "options": [                                          * {                                                  * "text": "Hammock in the mountains"                                                                               },                                              * {                                                  * "text": "Beach towel in the sand"                                                                               },                                              * {                                                  * "text": "Tent under the stars"                                                                               }                                                                   ]                                                       },                              * {                                  * "question_id": 2,                                      * "question_text": "Who are you taking?",                                      * "options": [                                          * {                                                  * "text": "No one—solo trip!"                                                                               },                                              * {                                                  * "text": "My best friend"                                                                               },                                              * {                                                  * "text": "The family"                                                                               }                                                                   ]                                                       }                                           ],                      * "results": [                          * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 1                                                       },                              * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 2                                                       },                              * {                                  * "organicPinId": "1234",                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "result_id": 3                                                       }                                           ]                               },              * "id": "687195134316"                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "ad_group_id": "2680059592705",                              * "android_deep_link": "string",                              * "carousel_android_deep_links": [                                  * "string"                                                       ],                              * "carousel_destination_urls": [                                  * "string"                                                       ],                              * "carousel_ios_deep_links": [                                  * "string"                                                       ],                              * "click_tracking_url": "string",                              * "creative_type": "REGULAR",                              * "destination_url": "string",                              * "ios_deep_link": "string",                              * "is_pin_deleted": false,                              * "is_removable": false,                              * "name": "string",                              * "status": "ACTIVE",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "view_tracking_url": "string",                              * "lead_form_id": "string",                              * "quiz_pin_data": {                                  * "questions": [                                          * {                                                  * "question_id": 1,                                                      * "question_text": "Where do you thrive?",                                                      * "options": [                                                          * {                                                                  * "text": "Hangout vibes"                                                                                                       },                                                              * {                                                                  * "text": "Time to party!"                                                                                                       },                                                              * {                                                                  * "text": "Keeping it lowkey"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Where would you nap?",                                                      * "options": [                                                          * {                                                                  * "text": "Hammock in the mountains"                                                                                                       },                                                              * {                                                                  * "text": "Beach towel in the sand"                                                                                                       },                                                              * {                                                                  * "text": "Tent under the stars"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Who are you taking?",                                                      * "options": [                                                          * {                                                                  * "text": "No one—solo trip!"                                                                                                       },                                                              * {                                                                  * "text": "My best friend"                                                                                                       },                                                              * {                                                                  * "text": "The family"                                                                                                       }                                                                                           ]                                                                               }                                                                   ],                                      * "results": [                                          * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 1                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 2                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 3                                                                               }                                                                   ]                                                       },                              * "pin_id": "394205773611545468",                              * "ad_account_id": "549755885175",                              * "campaign_id": "626735565838",                              * "collection_items_destination_url_template": "string",                              * "created_time": 1451431341,                              * "id": "687195134316",                              * "rejected_reasons": [                                  * "HASHTAGS"                                                       ],                              * "rejection_labels": [                                  * "string"                                                       ],                              * "review_status": "PENDING",                              * "type": "pinpromotion",                              * "updated_time": 1451431341,                              * "summary_status": "APPROVED"                                           },                      * "exceptions": {                          * "code": 2,                              * "message": "Advertiser not found."                                           }                               }                   ]       }`

[](#operation/ads/analytics)Get ad analytics
--------------------------------------------

Get analytics for the specified ads in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| ad\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad Ids to use to filter the results. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "AD_ID": "547602124502",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`

[](#operation/ad_targeting_analytics/get)Get targeting analytics for ads
------------------------------------------------------------------------

Get targeting analytics for one or more ads. For the requested ad(s) and metrics, the response will include the requested metric information (e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49").

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Ad Ids to use to filter the results. |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| targeting\_types<br><br>required | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 15 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>Example: targeting\_types=APPTYPE<br><br>Targeting type breakdowns for the report. The reporting per targeting type  <br>is independent from each other. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | string (ConversionReportAttributionType)<br><br>Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>Example: attribution\_types=INDIVIDUAL<br><br>List of types of attribution for the conversion report |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/targeting\_analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/targeting\_analytics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "targeting_type": "KEYWORD",                      * "targeting_value": "christmas decor ideas",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "iphone",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "ipad",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_tablet",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GENDER",                      * "targeting_value": "female",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "LOCATION",                      * "targeting_value": 500,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PLACEMENT",                      * "targeting_value": "SEARCH",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "COUNTRY",                      * "targeting_value": "US",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "TARGETED_INTEREST",                      * "targeting_value": "Food and Drinks",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PINNER_INTEREST",                      * "targeting_value": "Chocolate Cookies",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AUDIENCE_INCLUDE",                      * "targeting_value": 254261234567,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GEO",                      * "targeting_value": "US:94102",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AGE_BUCKET",                      * "targeting_value": "45-49",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "REGION",                      * "targeting_value": "US-CA",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               }                   ]       }`

[](#operation/ads/get)Get ad
----------------------------

Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will contain additional information from the Ad Review process. For more information about our policies and rejection reasons see the [Pinterest advertising standards](https://www.pinterest.com/_/_/policy/advertising-guidelines/).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| ad\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_group_id": "2680059592705",      * "android_deep_link": "string",      * "carousel_android_deep_links": [          * "string"                   ],      * "carousel_destination_urls": [          * "string"                   ],      * "carousel_ios_deep_links": [          * "string"                   ],      * "click_tracking_url": "string",      * "creative_type": "REGULAR",      * "destination_url": "string",      * "ios_deep_link": "string",      * "is_pin_deleted": false,      * "is_removable": false,      * "name": "string",      * "status": "ACTIVE",      * "tracking_urls": {          * "impression": [                  * "URL1",                      * "URL2"                               ],              * "click": [                  * "URL1",                      * "URL2"                               ],              * "engagement": [                  * "URL1",                      * "URL2"                               ],              * "buyable_button": [                  * "URL1",                      * "URL2"                               ],              * "audience_verification": [                  * "URL1",                      * "URL2"                               ]                   },      * "view_tracking_url": "string",      * "lead_form_id": "string",      * "quiz_pin_data": {          * "questions": [                  * {                          * "question_id": 1,                              * "question_text": "Where do you thrive?",                              * "options": [                                  * {                                          * "text": "Hangout vibes"                                                                   },                                      * {                                          * "text": "Time to party!"                                                                   },                                      * {                                          * "text": "Keeping it lowkey"                                                                   }                                                       ]                                           },                      * {                          * "question_id": 2,                              * "question_text": "Where would you nap?",                              * "options": [                                  * {                                          * "text": "Hammock in the mountains"                                                                   },                                      * {                                          * "text": "Beach towel in the sand"                                                                   },                                      * {                                          * "text": "Tent under the stars"                                                                   }                                                       ]                                           },                      * {                          * "question_id": 2,                              * "question_text": "Who are you taking?",                              * "options": [                                  * {                                          * "text": "No one—solo trip!"                                                                   },                                      * {                                          * "text": "My best friend"                                                                   },                                      * {                                          * "text": "The family"                                                                   }                                                       ]                                           }                               ],              * "results": [                  * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 1                                           },                      * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 2                                           },                      * {                          * "organicPinId": "1234",                              * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "result_id": 3                                           }                               ]                   },      * "pin_id": "394205773611545468",      * "ad_account_id": "549755885175",      * "campaign_id": "626735565838",      * "collection_items_destination_url_template": "string",      * "created_time": 1451431341,      * "id": "687195134316",      * "rejected_reasons": [          * "HASHTAGS"                   ],      * "rejection_labels": [          * "string"                   ],      * "review_status": "PENDING",      * "type": "pinpromotion",      * "updated_time": 1451431341,      * "summary_status": "APPROVED"       }`

[](#tag/audience_insights)audience\_insights
============================================

View audience insights.

[](#operation/audience_insights/get)Get audience insights
---------------------------------------------------------

Get Audience Insights for an ad account. The response will return insights for 3 types of audiences: the ad account's engaged audience on Pinterest, the ad account's total audience on Pinterest and Pinterest's total audience.

[Learn more about Audience Insights](https://help.pinterest.com/en/business/article/audience-insights).

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| audience\_insight\_type<br><br>required | string (AudienceInsightType)<br><br>Default: "YOUR\_TOTAL\_AUDIENCE"<br><br>Enum: "YOUR\_TOTAL\_AUDIENCE" "YOUR\_ENGAGED\_AUDIENCE" "PINTEREST\_TOTAL\_AUDIENCE"<br><br>Example: audience\_insight\_type=YOUR\_TOTAL\_AUDIENCE<br><br>Type of audience insights. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/audience\_insights

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audience\_insights

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "categories": [          * {                  * "key": "1234567",                      * "name": "travel",                      * "ratio": 0.551,                      * "index": 1.2,                      * "id": "1234567",                      * "subcategories": [                          * {                                  * "key": "958862518888",                                      * "name": "travel destinations",                                      * "ratio": 0.482,                                      * "index": 1.2,                                      * "id": "958862518888"                                                       }                                           ]                               }                   ],      * "demographics": {          * "ages": [                  * {                          * "name": "United States",                              * "key": "us",                              * "ratio": 0.551                                           }                               ],              * "genders": [                  * {                          * "name": "United States",                              * "key": "us",                              * "ratio": 0.551                                           }                               ],              * "devices": [                  * {                          * "name": "United States",                              * "key": "us",                              * "ratio": 0.551                                           }                               ],              * "metros": [                  * {                          * "name": "United States",                              * "key": "us",                              * "ratio": 0.551                                           }                               ],              * "countries": [                  * {                          * "name": "United States",                              * "key": "us",                              * "ratio": 0.551                                           }                               ]                   },      * "type": "YOUR_TOTAL_AUDIENCE",      * "date": "2022-10-09",      * "size": 10000,      * "size_is_upper_bound": true       }`

[](#operation/audience_insights_scope_and_type/get)Get audience insights scope and type
---------------------------------------------------------------------------------------

Get the scope and type of available audiences, which along with a date, is an audience that has recently had an interaction (referred to here as a type) on pins. Interacted pins can belong to at least the most common **partner** or **Pinterest** scopes. This means that user interactions made on advertiser or partner pins will have the **partner** scope. You can also have user interactions performed in general on Pinterest with the **Pinterest** scope. In that case, you can then use the returned type and scope values together on requests to other endpoints to retrieve insight metrics for a desired audience.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/insights/audiences

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/insights/audiences

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "date": "2022-10-09",                      * "scope": "PARTNER",                      * "type": "IMPRESSION_PLUS_ENGAGEMENT"                               }                   ]       }`

[](#tag/audiences)audiences
===========================

View, create, or update audiences.

[](#operation/audiences/list)List audiences
-------------------------------------------

Get list of audiences for the ad account.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. For received audiences, it is sorted by sharing event time. Note that higher-value IDs are associated with more-recently added items. |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ownership\_type | string<br><br>Default: "OWNED"<br><br>Enum: "OWNED" "RECEIVED"<br><br>Example: ownership\_type=OWNED<br><br>**This feature is currently in beta and not available to all apps.** Filter audiences by ownership type. |

### Responses

**200**

Success

**400**

Invalid ad account audience parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/audiences

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "ad_account_id": "549755885175",                      * "id": "1234",                      * "name": "ACME Tools",                      * "audience_type": "string",                      * "description": "People who love making quilts.",                      * "rule": {                          * "country": "US",                              * "customer_list_id": "5497558859876",                              * "engagement_domain": [                                  * "www.somedomain.com"                                                       ],                              * "engagement_type": "click",                              * "event": "checkout",                              * "event_data": {                                  * "currency": "USD",                                      * "lead_type": "Newsletter",                                      * "line_items": {                                          * "product_brand": "Parker",                                              * "product_category": "Shoes",                                              * "product_id": 1414,                                              * "product_name": "Parker Boots",                                              * "product_price": "99.99",                                              * "product_quantity": 2,                                              * "product_variant": "Red",                                              * "product_variant_id": "1414-34832"                                                                   },                                      * "order_id": "X-151481",                                      * "order_quantity": 1,                                      * "page_name": "Our Favorite Pins on Pinterest.",                                      * "promo_code": "WINTER10",                                      * "property": "Athleta",                                      * "search_query": "boots",                                      * "value": "199.98",                                      * "video_title": "How to style your Parker Boots"                                                       },                              * "percentage": 3,                              * "pin_id": [                                  * "34567"                                                       ],                              * "prefill": true,                              * "retention_days": 30,                              * "seed_id": [                                  * "2542620639259",                                      * "2542620639261"                                                       ],                              * "url": [                                  * "string"                                                       ],                              * "visitor_source_id": "549755885175",                              * "event_source": {                                  * "=": [                                          * "web",                                              * "mobile"                                                                   ]                                                       },                              * "ingestion_source": {                                  * "=": [                                          * "tag"                                                                   ]                                                       },                              * "engager_type": 1,                              * "campaign_id": [                                  * "626744528398"                                                       ],                              * "ad_id": [                                  * "687201361754"                                                       ],                              * "objective_type": [                                  * "AWARENESS"                                                       ],                              * "ad_account_id": "549755885175"                                           },                      * "size": 1000,                      * "status": "string",                      * "type": "audience",                      * "created_timestamp": 1451431341,                      * "updated_timestamp": 1451431341                               }                   ],      * "bookmark": "string"       }`

[](#operation/audiences/create)Create audience
----------------------------------------------

Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude specific audience\_ids when you create an ad group.

For more, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting).

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of ads to create, size limit \[1, 30\]

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name<br><br>required | string (name)<br><br>Audience name. |
| rule<br><br>required | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| description | string (description)<br><br>Audience description. |
| audience\_type<br><br>required | string<br><br>Enum: "CUSTOMER\_LIST" "VISITOR" "ENGAGEMENT" "ACTALIKE" "PERSONA"<br><br>Audience type |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/audiences

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "name": "string",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "description": "string",      * "audience_type": "string"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "id": "1234",      * "name": "ACME Tools",      * "audience_type": "string",      * "description": "People who love making quilts.",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "size": 1000,      * "status": "string",      * "type": "audience",      * "created_timestamp": 1451431341,      * "updated_timestamp": 1451431341       }`

[](#operation/audiences/create_custom)Create custom audience
------------------------------------------------------------

Create a custom audience and find the audiences you want your ads to reach.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Custom audience to create.

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name<br><br>required | string (name)<br><br>Audience name. |
| rule<br><br>required | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| sharing\_type<br><br>required | string (AudienceSharingType)<br><br>Enum: "CUSTOM" "SYNDICATED"<br><br>Audience sharing type: \["CUSTOM", "SYNDICATED"\] |
| data\_party<br><br>required | string (AudienceDataParty)<br><br>Enum: "1p" "3p"<br><br>Whether the data is owned by the partner (1p) or by the data provider (3p) |
| category | string |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/audiences/custom

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/custom

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "name": "string",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "sharing_type": "CUSTOM",      * "data_party": "1p",      * "category": "DLX Demographics"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "id": "1234",      * "name": "ACME Tools",      * "audience_type": "string",      * "description": "People who love making quilts.",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "size": 1000,      * "status": "string",      * "type": "audience",      * "created_timestamp": 1451431341,      * "updated_timestamp": 1451431341       }`

[](#operation/audiences/get)Get audience
----------------------------------------

Get a specific audience given the audience ID.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| audience\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an audience |

### Responses

**200**

Success

**404**

Audience not found.

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "id": "1234",      * "name": "ACME Tools",      * "audience_type": "string",      * "description": "People who love making quilts.",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "size": 1000,      * "status": "string",      * "type": "audience",      * "created_timestamp": 1451431341,      * "updated_timestamp": 1451431341       }`

[](#operation/audiences/update)Update audience
----------------------------------------------

Update (edit or remove) an existing targeting audience.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| audience\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an audience |

##### Request Body schema: application/json

The audience to be updated.

|     |     |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\\d+$<br><br>Ad account ID. |
| name | string (name)<br><br>Audience name. |
| rule | object (Rule)<br><br>JSON object defining targeted audience users. Example rule formats per audience type:  <br>CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}  <br>ACTALIKE: { "seed\_id": \["<audience ID>"\], "country": "US", "percentage": "10" }  <br>(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.  <br>The targeted audience should be this % size across Pinterest.)  <br>VISITOR: { "visitor\_source\_id": \["<conversion tag ID>"\], "retention\_days": "180", "event\_source": {"=": \["web", "mobile"\]}, "ingestion\_source": {"=": \["tag"\]}}  <br>(Retention days should be 1-540. Retention applies to specific customers.)  <br>ENGAGEMENT: {"engagement\_domain": \["[www.entomi.com"\]](http://www.entomi.com/%22%5D), "engager\_type": 1}  <br>For more details on engagement audiences, see [November 2021 changelog](https://developers.pinterest.com/docs/redoc/adtech_ads_v4/#section/November-2021). |
| description | string (description)<br><br>Audience description. |
| operation\_type | string (operation\_type)<br><br>Default: "UPDATE"<br><br>Enum: "UPDATE" "REMOVE"<br><br>Audience operation type (update or remove). |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "name": "string",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "description": "string",      * "operation_type": "UPDATE"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "id": "1234",      * "name": "ACME Tools",      * "audience_type": "string",      * "description": "People who love making quilts.",      * "rule": {          * "country": "US",              * "customer_list_id": "5497558859876",              * "engagement_domain": [                  * "www.somedomain.com"                               ],              * "engagement_type": "click",              * "event": "checkout",              * "event_data": {                  * "currency": "USD",                      * "lead_type": "Newsletter",                      * "line_items": {                          * "product_brand": "Parker",                              * "product_category": "Shoes",                              * "product_id": 1414,                              * "product_name": "Parker Boots",                              * "product_price": "99.99",                              * "product_quantity": 2,                              * "product_variant": "Red",                              * "product_variant_id": "1414-34832"                                           },                      * "order_id": "X-151481",                      * "order_quantity": 1,                      * "page_name": "Our Favorite Pins on Pinterest.",                      * "promo_code": "WINTER10",                      * "property": "Athleta",                      * "search_query": "boots",                      * "value": "199.98",                      * "video_title": "How to style your Parker Boots"                               },              * "percentage": 3,              * "pin_id": [                  * "34567"                               ],              * "prefill": true,              * "retention_days": 30,              * "seed_id": [                  * "2542620639259",                      * "2542620639261"                               ],              * "url": [                  * "string"                               ],              * "visitor_source_id": "549755885175",              * "event_source": {                  * "=": [                          * "web",                              * "mobile"                                           ]                               },              * "ingestion_source": {                  * "=": [                          * "tag"                                           ]                               },              * "engager_type": 1,              * "campaign_id": [                  * "626744528398"                               ],              * "ad_id": [                  * "687201361754"                               ],              * "objective_type": [                  * "AWARENESS"                               ],              * "ad_account_id": "549755885175"                   },      * "size": 1000,      * "status": "string",      * "type": "audience",      * "created_timestamp": 1451431341,      * "updated_timestamp": 1451431341       }`

[](#tag/billing)billing
=======================

View, create, or update information related to billing.

[](#operation/ads_credits_discounts/get)Get ads credit discounts
----------------------------------------------------------------

Returns the list of discounts applied to the account.

**This endpoint might not be available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read``billing:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/ads\_credit/discounts

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads\_credit/discounts

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "active": true,                      * "advertiser_id": "12312451231",                      * "discountInMicroCurrency": 125000000,                      * "discountCurrency": "USD",                      * "title": "Ads Credits",                      * "remainingDiscountInMicroCurrency": 125000000                               }                   ],      * "bookmark": "string"       }`

[](#operation/ads_credit/redeem)Redeem ad credits
-------------------------------------------------

Redeem ads credit on behalf of the ad account id and apply it towards billing.

**This endpoint might not be available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write``billing:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Redeem ad credits request.

|     |     |
| --- | --- |
| offerCodeHash<br><br>required | string^\[a-z0-9\]\*$<br><br>Takes in a SHA256 hash of the offerCode. |
| validateOnly<br><br>required | boolean<br><br>If true, only validate if we can redeem offer code. Otherwise it will actually apply the offer code to the account |

### Responses

**200**

Successfully redeemed ad credits.

**400**

Error thrown when unable to redeem offer code.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/ads\_credit/redeem

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads\_credit/redeem

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "offerCodeHash": "138e9e0ff7e38cf511b880975eb574c09aa9d5e1657590ab0431040da68caa67",      * "validateOnly": true       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "success": false,      * "errorCode": 2708,      * "errorMessage": "The offer has already been redeemed by this advertiser"       }`

[](#operation/billing_profiles/get)Get billing profiles
-------------------------------------------------------

Get billing profiles in the advertiser account.

**This endpoint might not be available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read``billing:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| is\_active<br><br>required | boolean<br><br>Return active billing profiles, if false return all billing profiles. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**default**

Unexpected error.

get/ad\_accounts/{ad\_account\_id}/billing\_profiles

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/billing\_profiles

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "12312451231",                      * "card_type": "VISA",                      * "status": "INVALID",                      * "advertiser_id": "12312451231",                      * "payment_method_brand": "VISA"                               }                   ],      * "bookmark": "string"       }`

[](#tag/boards)boards
=====================

View, create, update, or delete information about boards.

[](#operation/boards/list)List boards
-------------------------------------

Get a list of the boards owned by the "operation user\_account" + group boards where this account is a collaborator Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". Optional: Specify a privacy type (public, protected, or secret) to indicate which boards to return.

* If no privacy is specified, all boards that can be returned (based on the scopes of the token and ad\_account role if applicable) will be returned.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| privacy | string<br><br>Enum: "ALL" "PROTECTED" "PUBLIC" "SECRET" "PUBLIC\_AND\_SECRET"<br><br>Privacy setting for a board. |

### Responses

**200**

response

**default**

Unexpected error

get/boards

https://api.pinterest.com/v5/boards

### Request samples

* curl
* curl (Sandbox)

Copy

curl \--location \--request GET 'https://api.pinterest.com/v5/boards' \\
\--header 'Authorization: Bearer <Add your token here>' \\
\--header 'Content-Type: application/json'

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "549755885175",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",                      * "name": "Summer Recipes",                      * "description": "My favorite summer recipes",                      * "collaborator_count": 17,                      * "pin_count": 5,                      * "follower_count": 13,                      * "media": {                          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",                              * "pin_thumbnail_urls": [                                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                                                       ]                                           },                      * "owner": {                          * "username": "string"                                           },                      * "privacy": "PUBLIC"                               }                   ],      * "bookmark": "string"       }`

[](#operation/boards/create)Create board
----------------------------------------

Create a board owned by the "operation user\_account". Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Create a board using a single board json object.

|     |     |
| --- | --- |
| name<br><br>required | string |
| description | string Nullable |
| privacy | string<br><br>Default: "PUBLIC"<br><br>Enum: "PUBLIC" "PROTECTED" "SECRET"<br><br>Privacy setting for a board. Learn more about [secret boards](https://help.pinterest.com/en/article/secret-boards) and [protected boards](https://help.pinterest.com/en/business/article/protected-boards) |

### Responses

**201**

response

**400**

The board name is invalid or duplicated.

**default**

Unexpected error

post/boards

https://api.pinterest.com/v5/boards

### Request samples

* Payload
* Python SDK
* curl
* curl (Sandbox)

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Summer Recipes",      * "description": "My favorite summer recipes",      * "privacy": "PUBLIC"       }`

### Response samples

* 201
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "created_at": "2020-01-01T20:10:40-00:00",      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",      * "name": "Summer Recipes",      * "description": "My favorite summer recipes",      * "collaborator_count": 17,      * "pin_count": 5,      * "follower_count": 13,      * "media": {          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",              * "pin_thumbnail_urls": [                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                               ]                   },      * "owner": {          * "username": "string"                   },      * "privacy": "PUBLIC"       }`

[](#operation/boards/get)Get board
----------------------------------

Get a board owned by the operation user\_account - or a group board that has been shared with this account.

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

response

**404**

Board not found.

**default**

Unexpected error

get/boards/{board\_id}

https://api.pinterest.com/v5/boards/{board\_id}

### Request samples

* Python SDK
* curl
* curl (Sandbox)

Copy

\# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started

from pinterest.organic.boards import Board
\# Board information can be fetched from profile page or from create/list board method here:
\# https://developers.pinterest.com/docs/api/v5/#operation/boards/list
BOARD\_ID\="<Add your board id here>"

board\_get \= Board(board\_id\=BOARD\_ID)
print("Board Id: %s, Board name:%s"%(board\_get.id, board\_get.name))

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "created_at": "2020-01-01T20:10:40-00:00",      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",      * "name": "Summer Recipes",      * "description": "My favorite summer recipes",      * "collaborator_count": 17,      * "pin_count": 5,      * "follower_count": 13,      * "media": {          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",              * "pin_thumbnail_urls": [                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                               ]                   },      * "owner": {          * "username": "string"                   },      * "privacy": "PUBLIC"       }`

[](#operation/boards/update)Update board
----------------------------------------

Update a board owned by the "operating user\_account".

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Update a board.

|     |     |
| --- | --- |
| name | string |
| description | string Nullable |
| privacy | string<br><br>Enum: "PUBLIC" "SECRET" |

### Responses

**200**

response

**400**

Invalid board parameters.

**403**

Not authorized to update the board.

**429**

This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window.

**default**

Unexpected error

patch/boards/{board\_id}

https://api.pinterest.com/v5/boards/{board\_id}

### Request samples

* Payload
* Python SDK
* curl
* curl (Sandbox)

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Summer Recipes",      * "description": "My favorite summer recipes",      * "privacy": "PUBLIC"       }`

### Response samples

* 200
* 400
* 403
* 429
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "created_at": "2020-01-01T20:10:40-00:00",      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",      * "name": "Summer Recipes",      * "description": "My favorite summer recipes",      * "collaborator_count": 17,      * "pin_count": 5,      * "follower_count": 13,      * "media": {          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",              * "pin_thumbnail_urls": [                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                               ]                   },      * "owner": {          * "username": "string"                   },      * "privacy": "PUBLIC"       }`

[](#operation/boards/delete)Delete board
----------------------------------------

Delete a board owned by the "operation user\_account".

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**204**

Board deleted successfully

**403**

Not authorized to delete the board.

**404**

Board not found.

**409**

Could not get exclusive access to delete the board.

**429**

This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window.

**default**

Unexpected error

delete/boards/{board\_id}

https://api.pinterest.com/v5/boards/{board\_id}

### Request samples

* Python SDK
* curl
* curl (Sandbox)

Copy

\# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started

from pinterest.organic.boards import Board
\# Board information can be fetched from profile page or from create/list board method here:
\# https://developers.pinterest.com/docs/api/v5/#operation/boards/list
BOARD\_ID\="<Add your board id here>"

board\_delete\=Board.delete(board\_id\=BOARD\_ID)
print("Board was deleted? %s" % (board\_delete))

### Response samples

* 403
* 404
* 409
* 429
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 403,      * "message": "Not authorized to delete the board."       }`

[](#operation/boards/list_pins)List Pins on board
-------------------------------------------------

Get a list of the Pins on a board owned by the "operation user\_account" - or on a group board that has been shared with this account.

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| creative\_types | Array of strings<br><br>Items Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"<br><br>Example: creative\_types=REGULAR<br><br>Pin creative types filter.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| pin\_metrics | boolean<br><br>Default: false<br><br>Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. |

### Responses

**200**

response

**404**

Board not found.

**default**

Unexpected error

get/boards/{board\_id}/pins

https://api.pinterest.com/v5/boards/{board\_id}/pins

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "813744226420795884",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                      * "title": "string",                      * "description": "string",                      * "dominant_color": "#6E7874",                      * "alt_text": "string",                      * "creative_type": "REGULAR",                      * "board_id": "string",                      * "board_section_id": "string",                      * "board_owner": {                          * "username": "string"                                           },                      * "is_owner": true,                      * "media": {                          * "media_type": "string"                                           },                      * "parent_pin_id": "string",                      * "is_standard": true,                      * "has_been_promoted": true,                      * "note": "string",                      * "pin_metrics": {                          * "pin_metrics": [                                  * {                                          * "90d": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3                                                                               },                                              * "all_time": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3,                                                      * "reaction": 10,                                                      * "comment": 2                                                                               }                                                                   },                                      * null                                                       ]                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/board_sections/list)List board sections
-----------------------------------------------------

Get a list of all board sections from a board owned by the "operation user\_account" - or a group board that has been shared with this account. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

response

**default**

Unexpected error

get/boards/{board\_id}/sections

https://api.pinterest.com/v5/boards/{board\_id}/sections

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "549755885175",                      * "name": "Salads"                               }                   ],      * "bookmark": "string"       }`

[](#operation/board_sections/create)Create board section
--------------------------------------------------------

Create a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Create a board section.

|     |     |
| --- | --- |
| name<br><br>required | string \[ 1 .. 180 \] characters |

### Responses

**201**

response

**400**

Invalid board section parameters.

**403**

Not authorized to create board sections.

**409**

Could not get exclusive access to the board to create a new section.

**500**

Could not create a new board section.

**default**

Unexpected error

post/boards/{board\_id}/sections

https://api.pinterest.com/v5/boards/{board\_id}/sections

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Salads"       }`

### Response samples

* 201
* 400
* 403
* 409
* 500
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "name": "Salads"       }`

[](#operation/board_sections/update)Update board section
--------------------------------------------------------

Update a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |
| section\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board section. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Update a board section.

|     |     |
| --- | --- |
| name<br><br>required | string \[ 1 .. 180 \] characters |

### Responses

**200**

response

**400**

Invalid board section parameters.

**403**

Not authorized to update board section.

**409**

Board section conflict.

**default**

Unexpected error

patch/boards/{board\_id}/sections/{section\_id}

https://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Salads"       }`

### Response samples

* 200
* 400
* 403
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "name": "Salads"       }`

[](#operation/board_sections/delete)Delete board section
--------------------------------------------------------

Delete a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |
| section\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board section. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**204**

Board section deleted successfully

**403**

Not authorized to delete board section.

**404**

Board section not found.

**409**

Board section conflict.

**default**

Unexpected error

delete/boards/{board\_id}/sections/{section\_id}

https://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}

### Response samples

* 403
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 403,      * "message": "Not authorized to delete board section."       }`

[](#operation/board_sections/list_pins)List Pins on board section
-----------------------------------------------------------------

Get a list of the Pins on a board section of a board owned by the "operation user\_account" - or on a group board that has been shared with this account. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| board\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board. |
| section\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a board section. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

response

**403**

Not authorized to access Pins on board section.

**404**

Board or section not found.

**409**

Board section conflict.

**default**

Unexpected error

get/boards/{board\_id}/sections/{section\_id}/pins

https://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}/pins

### Response samples

* 200
* 403
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "813744226420795884",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                      * "title": "string",                      * "description": "string",                      * "dominant_color": "#6E7874",                      * "alt_text": "string",                      * "creative_type": "REGULAR",                      * "board_id": "string",                      * "board_section_id": "string",                      * "board_owner": {                          * "username": "string"                                           },                      * "is_owner": true,                      * "media": {                          * "media_type": "string"                                           },                      * "parent_pin_id": "string",                      * "is_standard": true,                      * "has_been_promoted": true,                      * "note": "string",                      * "pin_metrics": {                          * "pin_metrics": [                                  * {                                          * "90d": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3                                                                               },                                              * "all_time": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3,                                                      * "reaction": 10,                                                      * "comment": 2                                                                               }                                                                   },                                      * null                                                       ]                                           }                               }                   ],      * "bookmark": "string"       }`

[](#tag/bulk)bulk
=================

Create, update, or download ads-related entities in bulk.

[](#operation/bulk_download/create)Get advertiser entities in bulk
------------------------------------------------------------------

Create an asynchronous report that may include information on campaigns, ad groups, product groups, ads, and/or keywords; can filter by campaigns. Though the entities may be active, archived, or paused, only active entities will return data.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Parameters to get ad entities in bulk

|     |     |
| --- | --- |
| entity\_types | Array of strings \[ 1 .. 5 \] items<br><br>Items Enum: "CAMPAIGN" "AD\_GROUP" "PRODUCT\_GROUP" "AD" "KEYWORD"<br><br>All entity types specified will be downloaded. Fewer types result in faster downloads. |
| entity\_ids | Array of strings<br><br>All entities specified by these IDs as well as their children and grandchildren will be downloaded if the entity type is one of the types requested to be downloaded. |
| updated\_since | string^\\d+$<br><br>Unix UTC timestamp to retrieve all entities that have changed since this time. |
| campaign\_filter | object |
| output\_format | string<br><br>Default: "JSON"<br><br>Enum: "CSV" "JSON"<br><br>Bulk file output format |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/bulk/download

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/download

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "entity_types": [          * "CAMPAIGN",              * "AD_GROUP"                   ],      * "entity_ids": [          * "string"                   ],      * "updated_since": "1622848072",      * "campaign_filter": {          * "start_time": "1622848072",              * "end_time": "1622848072",              * "name": "campaign name",              * "campaign_status": [                  * "RUNNING"                               ],              * "objective_type": [                  * "AWARENESS"                               ]                   },      * "output_format": "CSV"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "request_id": "2680059592705"       }`

[](#operation/bulk_upsert/create)Create/update ad entities in bulk
------------------------------------------------------------------

Either create or update any combination of campaigns, ad groups, product groups, ads, or keywords. Note that this request will be processed asynchronously; the response will include a `request_id` that can be used to obtain the status of the request.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Parameters to get create/update ad entities in bulk

|     |     |
| --- | --- |
| create | object (BulkUpsertRequestCreate)<br><br>Request for creation of entities in bulk. |
| update | object (BulkUpsertRequestUpdate)<br><br>Request for creation of entities in bulk. |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/bulk/upsert

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/upsert

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "create": {          * "campaigns": [                  * {                          * "ad_account_id": "549755885175",                              * "name": "ACME Tools",                              * "status": "ACTIVE",                              * "lifetime_spend_cap": 1432744744,                              * "daily_spend_cap": 1432744744,                              * "order_line_id": "549755885175",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "start_time": 1580865126,                              * "end_time": 1644023526,                              * "summary_status": "RUNNING",                              * "is_flexible_daily_budgets": true,                              * "default_ad_group_budget_in_micro_currency": 0,                              * "is_automated_campaign": true,                              * "objective_type": "AWARENESS"                                           }                               ],              * "ad_groups": [                  * {                          * "name": "Ad Group For Pin: 687195905986",                              * "status": "ACTIVE",                              * "budget_in_micro_currency": 5000000,                              * "bid_in_micro_currency": 5000000,                              * "optimization_goal_metadata": {                                  * "conversion_tag_v3_goal_metadata": {                                          * "attribution_windows": {                                                  * "click_window_days": 0,                                                      * "engagement_window_days": 0,                                                      * "view_window_days": 0                                                                               },                                              * "conversion_event": "PAGE_VISIT",                                              * "conversion_tag_id": "string",                                              * "cpa_goal_value_in_micro_currency": "string",                                              * "is_roas_optimized": true,                                              * "learning_mode_type": "ACTIVE"                                                                   },                                      * "frequency_goal_metadata": {                                          * "frequency": 0,                                              * "timerange": "DAY"                                                                   },                                      * "scrollup_goal_metadata": {                                          * "scrollup_goal_value_in_micro_currency": "string"                                                                   }                                                       },                              * "budget_type": "DAILY",                              * "start_time": 5686848000,                              * "end_time": 5705424000,                              * "targeting_spec": {                                  * "AGE_BUCKET": [                                          * "35-44",                                              * "50-54"                                                                   ],                                      * "APPTYPE": [                                          * "ipad",                                              * "iphone"                                                                   ],                                      * "AUDIENCE_EXCLUDE": [                                          * "string"                                                                   ],                                      * "AUDIENCE_INCLUDE'": [                                          * "string"                                                                   ],                                      * "GENDER": [                                          * "unknown"                                                                   ],                                      * "GEO": [                                          * "string"                                                                   ],                                      * "INTEREST": [                                          * "string"                                                                   ],                                      * "LOCALE": [                                          * "string"                                                                   ],                                      * "LOCATION": [                                          * "string"                                                                   ],                                      * "SHOPPING_RETARGETING": [                                          * {                                                  * "lookback_window": 30,                                                      * "exclusion_window": 14,                                                      * "tag_types": [                                                          * 0,                                                              * 6                                                                                           ]                                                                               }                                                                   ],                                      * "TARGETING_STRATEGY": [                                          * "CHOOSE_YOUR_OWN"                                                                   ]                                                       },                              * "lifetime_frequency_cap": 100,                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "auto_targeting_enabled": true,                              * "placement_group": "ALL",                              * "pacing_delivery_type": "STANDARD",                              * "campaign_id": "626736533506",                              * "billable_event": "CLICKTHROUGH",                              * "bid_strategy_type": "MAX_BID"                                           }                               ],              * "ads": [                  * {                          * "ad_group_id": "2680059592705",                              * "android_deep_link": "string",                              * "carousel_android_deep_links": [                                  * "string"                                                       ],                              * "carousel_destination_urls": [                                  * "string"                                                       ],                              * "carousel_ios_deep_links": [                                  * "string"                                                       ],                              * "click_tracking_url": "string",                              * "creative_type": "REGULAR",                              * "destination_url": "string",                              * "ios_deep_link": "string",                              * "is_pin_deleted": false,                              * "is_removable": false,                              * "name": "string",                              * "status": "ACTIVE",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "view_tracking_url": "string",                              * "lead_form_id": "string",                              * "quiz_pin_data": {                                  * "questions": [                                          * {                                                  * "question_id": 1,                                                      * "question_text": "Where do you thrive?",                                                      * "options": [                                                          * {                                                                  * "text": "Hangout vibes"                                                                                                       },                                                              * {                                                                  * "text": "Time to party!"                                                                                                       },                                                              * {                                                                  * "text": "Keeping it lowkey"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Where would you nap?",                                                      * "options": [                                                          * {                                                                  * "text": "Hammock in the mountains"                                                                                                       },                                                              * {                                                                  * "text": "Beach towel in the sand"                                                                                                       },                                                              * {                                                                  * "text": "Tent under the stars"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Who are you taking?",                                                      * "options": [                                                          * {                                                                  * "text": "No one—solo trip!"                                                                                                       },                                                              * {                                                                  * "text": "My best friend"                                                                                                       },                                                              * {                                                                  * "text": "The family"                                                                                                       }                                                                                           ]                                                                               }                                                                   ],                                      * "results": [                                          * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 1                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 2                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 3                                                                               }                                                                   ]                                                       },                              * "pin_id": "394205773611545468"                                           }                               ],              * "product_groups": [                  * {                          * "product_group_promotion": [                                  * {                                          * "slideshow_collections_description": "Description",                                              * "creative_type": "REGULAR",                                              * "collections_hero_pin_id": "123123",                                              * "catalog_product_group_name": "catalogProductGroupName",                                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                                              * "slideshow_collections_title": "Title",                                              * "is_mdl": true,                                              * "status": "ACTIVE"                                                                   },                                      * {                                          * "slideshow_collections_description": "Description",                                              * "creative_type": "REGULAR",                                              * "collections_hero_pin_id": "123123",                                              * "catalog_product_group_name": "catalogProductGroupName",                                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                                              * "slideshow_collections_title": "Title",                                              * "is_mdl": true,                                              * "status": "ACTIVE"                                                                   }                                                       ],                              * "ad_group_id": "2680059592705"                                           }                               ],              * "keywords": [                  * {                          * "keywords": [                                  * {                                          * "bid": 200000,                                              * "match_type": "BROAD",                                              * "value": "string"                                                                   }                                                       ],                              * "parent_id": "383791336903426391"                                           }                               ]                   },      * "update": {          * "campaigns": [                  * {                          * "id": "549755885175",                              * "ad_account_id": "549755885175",                              * "name": "ACME Tools",                              * "status": "ACTIVE",                              * "lifetime_spend_cap": 1432744744,                              * "daily_spend_cap": 1432744744,                              * "order_line_id": "549755885175",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "start_time": 1580865126,                              * "end_time": 1644023526,                              * "summary_status": "RUNNING",                              * "is_flexible_daily_budgets": true,                              * "default_ad_group_budget_in_micro_currency": 0,                              * "is_automated_campaign": true,                              * "is_campaign_budget_optimization": true                                           }                               ],              * "ad_groups": [                  * {                          * "name": "Ad Group For Pin: 687195905986",                              * "status": "ACTIVE",                              * "budget_in_micro_currency": 5000000,                              * "bid_in_micro_currency": 5000000,                              * "optimization_goal_metadata": {                                  * "conversion_tag_v3_goal_metadata": {                                          * "attribution_windows": {                                                  * "click_window_days": 0,                                                      * "engagement_window_days": 0,                                                      * "view_window_days": 0                                                                               },                                              * "conversion_event": "PAGE_VISIT",                                              * "conversion_tag_id": "string",                                              * "cpa_goal_value_in_micro_currency": "string",                                              * "is_roas_optimized": true,                                              * "learning_mode_type": "ACTIVE"                                                                   },                                      * "frequency_goal_metadata": {                                          * "frequency": 0,                                              * "timerange": "DAY"                                                                   },                                      * "scrollup_goal_metadata": {                                          * "scrollup_goal_value_in_micro_currency": "string"                                                                   }                                                       },                              * "budget_type": "DAILY",                              * "start_time": 5686848000,                              * "end_time": 5705424000,                              * "targeting_spec": {                                  * "AGE_BUCKET": [                                          * "35-44",                                              * "50-54"                                                                   ],                                      * "APPTYPE": [                                          * "ipad",                                              * "iphone"                                                                   ],                                      * "AUDIENCE_EXCLUDE": [                                          * "string"                                                                   ],                                      * "AUDIENCE_INCLUDE'": [                                          * "string"                                                                   ],                                      * "GENDER": [                                          * "unknown"                                                                   ],                                      * "GEO": [                                          * "string"                                                                   ],                                      * "INTEREST": [                                          * "string"                                                                   ],                                      * "LOCALE": [                                          * "string"                                                                   ],                                      * "LOCATION": [                                          * "string"                                                                   ],                                      * "SHOPPING_RETARGETING": [                                          * {                                                  * "lookback_window": 30,                                                      * "exclusion_window": 14,                                                      * "tag_types": [                                                          * 0,                                                              * 6                                                                                           ]                                                                               }                                                                   ],                                      * "TARGETING_STRATEGY": [                                          * "CHOOSE_YOUR_OWN"                                                                   ]                                                       },                              * "lifetime_frequency_cap": 100,                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "auto_targeting_enabled": true,                              * "placement_group": "ALL",                              * "pacing_delivery_type": "STANDARD",                              * "campaign_id": "626736533506",                              * "billable_event": "CLICKTHROUGH",                              * "bid_strategy_type": "MAX_BID",                              * "id": "2680060704746"                                           }                               ],              * "ads": [                  * {                          * "ad_group_id": "2680059592705",                              * "android_deep_link": "string",                              * "carousel_android_deep_links": [                                  * "string"                                                       ],                              * "carousel_destination_urls": [                                  * "string"                                                       ],                              * "carousel_ios_deep_links": [                                  * "string"                                                       ],                              * "click_tracking_url": "string",                              * "creative_type": "REGULAR",                              * "destination_url": "string",                              * "ios_deep_link": "string",                              * "is_pin_deleted": false,                              * "is_removable": false,                              * "name": "string",                              * "status": "ACTIVE",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "view_tracking_url": "string",                              * "lead_form_id": "string",                              * "quiz_pin_data": {                                  * "questions": [                                          * {                                                  * "question_id": 1,                                                      * "question_text": "Where do you thrive?",                                                      * "options": [                                                          * {                                                                  * "text": "Hangout vibes"                                                                                                       },                                                              * {                                                                  * "text": "Time to party!"                                                                                                       },                                                              * {                                                                  * "text": "Keeping it lowkey"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Where would you nap?",                                                      * "options": [                                                          * {                                                                  * "text": "Hammock in the mountains"                                                                                                       },                                                              * {                                                                  * "text": "Beach towel in the sand"                                                                                                       },                                                              * {                                                                  * "text": "Tent under the stars"                                                                                                       }                                                                                           ]                                                                               },                                              * {                                                  * "question_id": 2,                                                      * "question_text": "Who are you taking?",                                                      * "options": [                                                          * {                                                                  * "text": "No one—solo trip!"                                                                                                       },                                                              * {                                                                  * "text": "My best friend"                                                                                                       },                                                              * {                                                                  * "text": "The family"                                                                                                       }                                                                                           ]                                                                               }                                                                   ],                                      * "results": [                                          * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 1                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 2                                                                               },                                              * {                                                  * "organicPinId": "1234",                                                      * "android_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "iOS_deep_link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "destination_url": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                                      * "result_id": 3                                                                               }                                                                   ]                                                       },                              * "id": "687195134316"                                           }                               ],              * "product_groups": [                  * {                          * "product_group_promotion": [                                  * {                                          * "catalog_product_group_id": "1234123",                                              * "slideshow_collections_description": "Description",                                              * "creative_type": "REGULAR",                                              * "collections_hero_pin_id": "123123",                                              * "catalog_product_group_name": "ProductGroupName",                                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                                              * "slideshow_collections_title": "Title",                                              * "status": "ACTIVE",                                              * "id": "2680059592705"                                                                   },                                      * {                                          * "catalog_product_group_id": "1231231",                                              * "slideshow_collections_description": "Other description",                                              * "creative_type": "REGULAR",                                              * "collections_hero_pin_id": "123124",                                              * "catalog_product_group_name": "ProductGroupName",                                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                                              * "slideshow_collections_title": "Title",                                              * "status": "ACTIVE",                                              * "id": "2680059592706"                                                                   }                                                       ],                              * "ad_group_id": "26823439592705"                                           }                               ],              * "keywords": [                  * {                          * "id": "2886364308355",                              * "archived": false,                              * "bid": 200000                                           }                               ]                   }       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "request_id": "549763856477-1660864560-1407e16a-c586-4add-94df-d0b160bec0ff, 549763856477-1660864560-d0b160bec0ff"       }`

[](#operation/bulk_request/get)Download advertiser entities in bulk
-------------------------------------------------------------------

Get the status of a bulk request by `request_id`, along with a download URL that will allow you to download the new or updated entity data (campaigns, ad groups, product groups, ads, or keywords).

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| bulk\_request\_id<br><br>required | string<br><br>Unique identifier of a bulk upsert request. |

##### query Parameters

|     |     |
| --- | --- |
| include\_details | boolean<br><br>Default: false<br><br>if set to True then attach the errors/details to all the requests |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/bulk/{bulk\_request\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/{bulk\_request\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "status": "SUCCEEDED",      * "result_url": "[https://pinterest-waterloo.s3.us-east-1.amazonaws.com/bulk_framework/AD_ENTITY_UPSERT/549763856637-1659122537-0b4d77d3-f620-48ce-bec9-616106afb8d4/(...)](https://pinterest-waterloo.s3.us-east-1.amazonaws.com/bulk_framework/AD_ENTITY_UPSERT/549763856637-1659122537-0b4d77d3-f620-48ce-bec9-616106afb8d4/(...))"       }`

[](#tag/campaigns)campaigns
===========================

View, create or update campaigns.

[](#operation/campaigns/list)List campaigns
-------------------------------------------

Get a list of the campaigns in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**400**

Invalid ad account campaign parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "549755885175",                      * "ad_account_id": "549755885175",                      * "name": "ACME Tools",                      * "status": "ACTIVE",                      * "lifetime_spend_cap": 1432744744,                      * "daily_spend_cap": 1432744744,                      * "order_line_id": "549755885175",                      * "tracking_urls": {                          * "impression": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "click": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "engagement": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "buyable_button": [                                  * "URL1",                                      * "URL2"                                                       ],                              * "audience_verification": [                                  * "URL1",                                      * "URL2"                                                       ]                                           },                      * "start_time": 1580865126,                      * "end_time": 1644023526,                      * "summary_status": "RUNNING",                      * "objective_type": "AWARENESS",                      * "created_time": 1432744744,                      * "updated_time": 1432744744,                      * "type": "campaign",                      * "is_flexible_daily_budgets": true,                      * "is_campaign_budget_optimization": true                               }                   ],      * "bookmark": "string"       }`

[](#operation/campaigns/create)Create campaigns
-----------------------------------------------

Create multiple new campaigns. Every campaign has its own campaign\_id and houses one or more ad groups, which contain one or more ads. For more, see [Set up your campaign](https://help.pinterest.com/en/business/article/set-up-your-campaign/).

**Note:**

* The values for 'lifetime\_spend\_cap' and 'daily\_spend\_cap' are microcurrency amounts based on the currency field set in the advertiser's profile. (e.g. USD)
    
    Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.
    
    A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.
    
    **Equivalency equations**, using dollars as an example currency:
    
    * $1 = 1,000,000 microdollars
    * 1 microdollar = $0.000001
    
    **To convert between currency and microcurrency**, using dollars as an example currency:
    
    * To convert dollars to microdollars, mutiply dollars by 1,000,000
    * To convert microdollars to dollars, divide microdollars by 1,000,000

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Array of campaigns.

Array ()

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string^\\d+$<br><br>Campaign's Advertiser ID. If you want to create a campaign in a Business Account shared account you need to specify the Business Access advertiser ID in both the query path param as well as the request body schema. |
| name<br><br>required | string<br><br>Campaign name. |
| status | string<br><br>Default: "ACTIVE"<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Entity status |
| lifetime\_spend\_cap | integer Nullable<br><br>Campaign total spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "daily\_spend\_cap" cannot be set at the same time. |
| daily\_spend\_cap | integer Nullable<br><br>Campaign daily spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "lifetime\_spend\_cap" cannot be set at the same time. |
| order\_line\_id | string Nullable ^\\d+$<br><br>Order line ID that appears on the invoice. |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| start\_time | integer Nullable<br><br>Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. |
| end\_time | integer Nullable<br><br>Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. |
| summary\_status | string<br><br>Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Summary status for campaign |
| is\_flexible\_daily\_budgets | boolean<br><br>Default: false<br><br>Determine if a campaign has flexible daily budgets setup. |
| default\_ad\_group\_budget\_in\_micro\_currency | integer Nullable<br><br>When transitioning from campaign budget optimization to non-campaign budget optimization, the default\_ad\_group\_budget\_in\_micro\_currency will propagate to each child ad groups daily budget. Unit is micro currency of the associated advertiser account. |
| is\_automated\_campaign | boolean<br><br>Default: false<br><br>Specifies whether the campaign was created in the automated campaign flow |
| objective\_type<br><br>required | string (ObjectiveType)<br><br>Enum: "AWARENESS" "CONSIDERATION" "VIDEO\_VIEW" "WEB\_CONVERSION" "CATALOG\_SALES" "WEB\_SESSIONS"<br><br>Campaign objective type. If set as one of \["AWARENESS", "CONSIDERATION", "WEB\_CONVERSION", "CATALOG\_SALES"\] the campaign is considered as a Campaign Budget Optimization (CBO) campaign, meaning budget needs to be set at the campaign level rather than at the ad group level. \["WEB\_SESSIONS"\] in BETA. |

### Responses

**200**

response

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/campaigns

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "ad_account_id": "549755885175",              * "name": "ACME Tools",              * "status": "ACTIVE",              * "lifetime_spend_cap": 1432744744,              * "daily_spend_cap": 1432744744,              * "order_line_id": "549755885175",              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "start_time": 1580865126,              * "end_time": 1644023526,              * "summary_status": "RUNNING",              * "is_flexible_daily_budgets": true,              * "default_ad_group_budget_in_micro_currency": 0,              * "is_automated_campaign": true,              * "objective_type": "AWARENESS"                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "ad_account_id": "549755885175",                              * "name": "ACME Tools",                              * "status": "ACTIVE",                              * "lifetime_spend_cap": 1432744744,                              * "daily_spend_cap": 1432744744,                              * "order_line_id": "549755885175",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "start_time": 1580865126,                              * "end_time": 1644023526,                              * "summary_status": "RUNNING",                              * "is_flexible_daily_budgets": true,                              * "default_ad_group_budget_in_micro_currency": 0,                              * "is_automated_campaign": true,                              * "id": "549755885175",                              * "objective_type": "AWARENESS",                              * "created_time": 1432744744,                              * "updated_time": 1432744744,                              * "type": "campaign",                              * "is_campaign_budget_optimization": true                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/campaigns/update)Update campaigns
-----------------------------------------------

Update multiple ad campaigns based on campaign\_ids.

**Note:**

* The values for 'lifetime\_spend\_cap' and 'daily\_spend\_cap' are microcurrency amounts based on the currency field set in the advertiser's profile. (e.g. USD)
    
    Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.
    
    A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’ s profile.
    
    **Equivalency equations**, using dollars as an example currency:
    
    * $1 = 1,000,000 microdollars
    * 1 microdollar = $0.000001
    
    **To convert between currency and microcurrency**, using dollars as an example currency:
    
    * To convert dollars to microdollars, mutiply dollars by 1,000,000
    * To convert microdollars to dollars, divide microdollars by 1,000,000

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Array of campaigns.

Array ()

|     |     |
| --- | --- |
| id<br><br>required | string^\\d+$<br><br>Campaign ID. |
| ad\_account\_id<br><br>required | string^\\d+$<br><br>Campaign's Advertiser ID. If you want to create a campaign in a Business Account shared account you need to specify the Business Access advertiser ID in both the query path param as well as the request body schema. |
| name | string<br><br>Campaign name. |
| status | string Nullable<br><br>Default: "ACTIVE"<br><br>Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Entity status |
| lifetime\_spend\_cap | integer Nullable<br><br>Campaign total spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "daily\_spend\_cap" cannot be set at the same time. |
| daily\_spend\_cap | integer Nullable<br><br>Campaign daily spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "lifetime\_spend\_cap" cannot be set at the same time. |
| order\_line\_id | string Nullable ^\\d+$<br><br>Order line ID that appears on the invoice. |
| tracking\_urls | object Nullable<br><br>Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see [Third-party and dynamic tracking](https://help.pinterest.com/en/business/article/third-party-and-dynamic-tracking). |
| start\_time | integer Nullable<br><br>Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. |
| end\_time | integer Nullable<br><br>Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns. |
| summary\_status | string<br><br>Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"<br><br>Summary status for campaign |
| is\_flexible\_daily\_budgets | boolean Nullable<br><br>Default: false<br><br>Determine if a campaign has flexible daily budgets setup. |
| default\_ad\_group\_budget\_in\_micro\_currency | integer Nullable<br><br>When transitioning from campaign budget optimization to non-campaign budget optimization, the default\_ad\_group\_budget\_in\_micro\_currency will propagate to each child ad groups daily budget. Unit is micro currency of the associated advertiser account. |
| is\_automated\_campaign | boolean Nullable<br><br>Default: false<br><br>Specifies whether the campaign was created in the automated campaign flow |
| is\_campaign\_budget\_optimization | boolean Nullable<br><br>Determines if a campaign automatically generate ad-group level budgets given a campaign budget to maximize campaign outcome. When transitioning from non-cbo to cbo, all previous child ad group budget will be cleared. |

### Responses

**200**

response

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/campaigns

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "id": "549755885175",              * "ad_account_id": "549755885175",              * "name": "ACME Tools",              * "status": "ACTIVE",              * "lifetime_spend_cap": 1432744744,              * "daily_spend_cap": 1432744744,              * "order_line_id": "549755885175",              * "tracking_urls": {                  * "impression": [                          * "URL1",                              * "URL2"                                           ],                      * "click": [                          * "URL1",                              * "URL2"                                           ],                      * "engagement": [                          * "URL1",                              * "URL2"                                           ],                      * "buyable_button": [                          * "URL1",                              * "URL2"                                           ],                      * "audience_verification": [                          * "URL1",                              * "URL2"                                           ]                               },              * "start_time": 1580865126,              * "end_time": 1644023526,              * "summary_status": "RUNNING",              * "is_flexible_daily_budgets": true,              * "default_ad_group_budget_in_micro_currency": 0,              * "is_automated_campaign": true,              * "is_campaign_budget_optimization": true                   }       ]`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "ad_account_id": "549755885175",                              * "name": "ACME Tools",                              * "status": "ACTIVE",                              * "lifetime_spend_cap": 1432744744,                              * "daily_spend_cap": 1432744744,                              * "order_line_id": "549755885175",                              * "tracking_urls": {                                  * "impression": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "click": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "engagement": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "buyable_button": [                                          * "URL1",                                              * "URL2"                                                                   ],                                      * "audience_verification": [                                          * "URL1",                                              * "URL2"                                                                   ]                                                       },                              * "start_time": 1580865126,                              * "end_time": 1644023526,                              * "summary_status": "RUNNING",                              * "is_flexible_daily_budgets": true,                              * "default_ad_group_budget_in_micro_currency": 0,                              * "is_automated_campaign": true,                              * "id": "549755885175",                              * "objective_type": "AWARENESS",                              * "created_time": 1432744744,                              * "updated_time": 1432744744,                              * "type": "campaign",                              * "is_campaign_budget_optimization": true                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/campaigns/analytics)Get campaign analytics
--------------------------------------------------------

Get analytics for the specified campaigns in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| campaign\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |

### Responses

**200**

Success

**400**

Invalid ad account campaign analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "CAMPAIGN_ID": "547602124502",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`

[](#operation/campaign_targeting_analytics/get)Get targeting analytics for campaigns
------------------------------------------------------------------------------------

Get targeting analytics for one or more campaigns. For the requested account and metrics, the response will include the requested metric information (e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49").

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Campaign Ids to use to filter the results. |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| targeting\_types<br><br>required | Array of strings (AdsAnalyticsTargetingType) \[ 1 .. 15 \] items<br><br>Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"<br><br>Example: targeting\_types=APPTYPE<br><br>Targeting type breakdowns for the report. The reporting per targeting type  <br>is independent from each other. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |
| attribution\_types | string (ConversionReportAttributionType)<br><br>Enum: "INDIVIDUAL" "HOUSEHOLD"<br><br>Example: attribution\_types=INDIVIDUAL<br><br>List of types of attribution for the conversion report |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/targeting\_analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/targeting\_analytics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "targeting_type": "KEYWORD",                      * "targeting_value": "christmas decor ideas",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "iphone",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "ipad",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "web_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_mobile",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "APPTYPE",                      * "targeting_value": "android_tablet",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GENDER",                      * "targeting_value": "female",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "LOCATION",                      * "targeting_value": 500,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PLACEMENT",                      * "targeting_value": "SEARCH",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "COUNTRY",                      * "targeting_value": "US",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "TARGETED_INTEREST",                      * "targeting_value": "Food and Drinks",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "PINNER_INTEREST",                      * "targeting_value": "Chocolate Cookies",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AUDIENCE_INCLUDE",                      * "targeting_value": 254261234567,                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "GEO",                      * "targeting_value": "US:94102",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "AGE_BUCKET",                      * "targeting_value": "45-49",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               },              * {                  * "targeting_type": "REGION",                      * "targeting_value": "US-CA",                      * "metrics": {                          * "AD_GROUP_ID": 2680067996745,                              * "DATE": "2022-04-26",                              * "SPEND_IN_DOLLAR": 240                                           }                               }                   ]       }`

[](#operation/campaigns/get)Get campaign
----------------------------------------

Get a specific campaign given the campaign ID.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| campaign\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Campaign ID, must be associated with the ad account ID provided in the path. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/{campaign\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/{campaign\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "549755885175",      * "ad_account_id": "549755885175",      * "name": "ACME Tools",      * "status": "ACTIVE",      * "lifetime_spend_cap": 1432744744,      * "daily_spend_cap": 1432744744,      * "order_line_id": "549755885175",      * "tracking_urls": {          * "impression": [                  * "URL1",                      * "URL2"                               ],              * "click": [                  * "URL1",                      * "URL2"                               ],              * "engagement": [                  * "URL1",                      * "URL2"                               ],              * "buyable_button": [                  * "URL1",                      * "URL2"                               ],              * "audience_verification": [                  * "URL1",                      * "URL2"                               ]                   },      * "start_time": 1580865126,      * "end_time": 1644023526,      * "summary_status": "RUNNING",      * "objective_type": "AWARENESS",      * "created_time": 1432744744,      * "updated_time": 1432744744,      * "type": "campaign",      * "is_flexible_daily_budgets": true,      * "is_campaign_budget_optimization": true       }`

[](#tag/catalogs)catalogs
=========================

Manage information about shopping product catalogs and items.

[](#operation/catalogs/list)List catalogs
-----------------------------------------

Fetch catalogs owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid parameters.

**401**

Unauthorized access.

**default**

Unexpected error.

get/catalogs

https://api.pinterest.com/v5/catalogs

### Response samples

* 200
* 400
* 401
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "created_at": "2022-03-14T15:15:22Z",                      * "id": "864344156814050986",                      * "updated_at": "2022-03-14T15:16:34Z",                      * "name": "string",                      * "catalog_type": "RETAIL"                               }                   ],      * "bookmark": "string"       }`

[](#operation/feeds/list)List feeds
-----------------------------------

Fetch feeds owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to [Before you get started with Catalogs](https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs). For Hotel parterns, refer to [Pinterest API for shopping](https://developers.pinterest.com/docs/shopping/catalog/).

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| catalog\_id | string^\\d+$<br><br>Filter entities for a given catalog\_id. If not given, all catalogs are considered. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid parameters.

**401**

Unauthorized access.

**default**

Unexpected error.

get/catalogs/feeds

https://api.pinterest.com/v5/catalogs/feeds

### Response samples

* 200
* 400
* 401
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "created_at": "2022-03-14T15:15:22Z",                      * "id": "string",                      * "updated_at": "2022-03-14T15:16:34Z",                      * "name": "string",                      * "format": "TSV",                      * "catalog_type": "RETAIL",                      * "credentials": {                          * "password": "pa$$word",                              * "username": "string"                                           },                      * "location": "string",                      * "preferred_processing_schedule": {                          * "time": "02:59",                              * "timezone": "Africa/Abidjan"                                           },                      * "status": "ACTIVE",                      * "default_currency": "USD",                      * "default_locale": "en-US",                      * "default_country": "US",                      * "default_availability": "IN_STOCK"                               }                   ],      * "bookmark": "string"       }`

[](#operation/feeds/create)Create feed
--------------------------------------

Create a new feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Please, be aware that "default\_country" and "default\_locale" are not required in the spec for forward compatibility but for now the API will not accept requests without those fields.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to [Before you get started with Catalogs](https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs). For Hotel parterns, refer to [Pinterest API for shopping](https://developers.pinterest.com/docs/shopping/catalog/).

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read``catalogs:write`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to created a feed.

One of

feeds\_create\_requestlegacy\_retail\_only

|     |     |
| --- | --- |
| default\_currency | string (NullableCurrency) Nullable<br><br>Enum: "AED" "AFN" "ALL" "AMD" "ANG" "AOA" "ARS" "AUD" "AWG" "AZN" "BAM" "BBD" "BDT" "BGN" "BHD" "BIF" "BMD" "BND" "BOB" "BRL" … 144 more<br><br>Currency Codes from ISO 4217. |
| name<br><br>required | string<br><br>A human-friendly name associated to a given feed. |
| format<br><br>required | string (CatalogsFormat)<br><br>Enum: "TSV" "CSV" "XML"<br><br>The file format of a feed. |
| default\_locale<br><br>required | CatalogsLocale (string) or string<br><br>The locale used within a feed for product descriptions. |
| credentials | object (CatalogsFeedCredentials) Nullable<br><br>This field is **OPTIONAL**. Use this if your feed file requires username and password. |
| location<br><br>required | string^(http\|https\|ftp\|sftp)://<br><br>The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. |
| preferred\_processing\_schedule | object (catalogs\_processing\_schedule) Nullable<br><br>Daily processing schedule. This field is **OPTIONAL**. Use this to configure the preferred time for processing a feed (otherwise random). |
| catalog\_type<br><br>required | string (CatalogsType)<br><br>Type of the catalog entity.<br><br>RETAIL<br><br>RETAIL<br><br>HOTEL |
| default\_country<br><br>required | string (Country)<br><br>Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more<br><br>Country ID from ISO 3166-1 alpha-2. |
| default\_availability | string (ProductAvailabilityType) Nullable<br><br>Enum: "IN\_STOCK" "OUT\_OF\_STOCK" "PREORDER" null<br><br>Default availability for products in a feed. |

### Responses

**201**

Success

**400**

Invalid feed parameters.

**401**

Unauthorized access.

**403**

Business account required.

**409**

User website required.

**422**

Unique feed name is required.

**501**

Not implemented (absent "default\_country" or "default\_locale").

**default**

Unexpected error

post/catalogs/feeds

https://api.pinterest.com/v5/catalogs/feeds

### Request samples

* Payload

Content type

application/json

Example

feeds\_create\_request

feeds\_create\_request

legacy\_retail\_only

Copy

Expand all Collapse all

`{  * "default_currency": "USD",      * "name": "string",      * "format": "TSV",      * "default_locale": "en-US",      * "credentials": {          * "password": "pa$$word",              * "username": "string"                   },      * "location": "string",      * "preferred_processing_schedule": {          * "time": "02:59",              * "timezone": "Africa/Abidjan"                   },      * "catalog_type": "RETAIL",      * "default_country": "US",      * "default_availability": "IN_STOCK"       }`

### Response samples

* 201
* 400
* 401
* 403
* 409
* 422
* 501
* default

Content type

application/json

Example

RETAIL

RETAIL

HOTEL

Copy

Expand all Collapse all

`{  * "created_at": "2022-03-14T15:15:22Z",      * "id": "string",      * "updated_at": "2022-03-14T15:16:34Z",      * "name": "string",      * "format": "TSV",      * "catalog_type": "RETAIL",      * "credentials": {          * "password": "pa$$word",              * "username": "string"                   },      * "location": "string",      * "preferred_processing_schedule": {          * "time": "02:59",              * "timezone": "Africa/Abidjan"                   },      * "status": "ACTIVE",      * "default_currency": "USD",      * "default_locale": "en-US",      * "default_country": "US",      * "default_availability": "IN_STOCK"       }`

[](#operation/feeds/get)Get feed
--------------------------------

Get a single feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to [Before you get started with Catalogs](https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs). For Hotel parterns, refer to [Pinterest API for shopping](https://developers.pinterest.com/docs/shopping/catalog/).

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| feed\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a feed |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid feed parameters.

**401**

Unauthorized access.

**404**

Data feed not found.

**default**

Unexpected error.

get/catalogs/feeds/{feed\_id}

https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}

### Response samples

* 200
* 400
* 401
* 404
* default

Content type

application/json

Example

RETAIL

RETAIL

HOTEL

Copy

Expand all Collapse all

`{  * "created_at": "2022-03-14T15:15:22Z",      * "id": "string",      * "updated_at": "2022-03-14T15:16:34Z",      * "name": "string",      * "format": "TSV",      * "catalog_type": "RETAIL",      * "credentials": {          * "password": "pa$$word",              * "username": "string"                   },      * "location": "string",      * "preferred_processing_schedule": {          * "time": "02:59",              * "timezone": "Africa/Abidjan"                   },      * "status": "ACTIVE",      * "default_currency": "USD",      * "default_locale": "en-US",      * "default_country": "US",      * "default_availability": "IN_STOCK"       }`

[](#operation/feeds/update)Update feed
--------------------------------------

Update a feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to [Before you get started with Catalogs](https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs). For Hotel parterns, refer to [Pinterest API for shopping](https://developers.pinterest.com/docs/shopping/catalog/).

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read``catalogs:write`)

##### path Parameters

|     |     |
| --- | --- |
| feed\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a feed |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to update a feed.

One of

feeds\_update\_requestlegacy\_retail\_only

|     |     |
| --- | --- |
| default\_currency | string (NullableCurrency) Nullable<br><br>Enum: "AED" "AFN" "ALL" "AMD" "ANG" "AOA" "ARS" "AUD" "AWG" "AZN" "BAM" "BBD" "BDT" "BGN" "BHD" "BIF" "BMD" "BND" "BOB" "BRL" … 144 more<br><br>Currency Codes from ISO 4217. |
| name | string<br><br>A human-friendly name associated to a given feed. |
| format | string (CatalogsFormat)<br><br>Enum: "TSV" "CSV" "XML"<br><br>The file format of a feed. |
| credentials | object (CatalogsFeedCredentials) Nullable<br><br>This field is **OPTIONAL**. Use this if your feed file requires username and password. |
| location | string^(http\|https\|ftp\|sftp)://<br><br>The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing. |
| preferred\_processing\_schedule | object (catalogs\_processing\_schedule) Nullable<br><br>Daily processing schedule. This field is **OPTIONAL**. Use this to configure the preferred time for processing a feed (otherwise random). |
| status | string (CatalogsStatus)<br><br>Enum: "ACTIVE" "INACTIVE"<br><br>Status for catalogs entities. Present in catalogs\_feed values. When a feed is deleted, the response will inform DELETED as status. |
| catalog\_type<br><br>required | string (CatalogsType)<br><br>Type of the catalog entity.<br><br>RETAIL<br><br>RETAIL<br><br>HOTEL |
| default\_availability | string (ProductAvailabilityType) Nullable<br><br>Enum: "IN\_STOCK" "OUT\_OF\_STOCK" "PREORDER" null<br><br>Default availability for products in a feed. |

### Responses

**200**

Success

**400**

Invalid feed parameters.

**403**

Forbidden. Account not approved for feed mutations yet.

**404**

Data feed not found.

**default**

Unexpected error

patch/catalogs/feeds/{feed\_id}

https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}

### Request samples

* Payload

Content type

application/json

Example

feeds\_update\_request

feeds\_update\_request

legacy\_retail\_only

Copy

Expand all Collapse all

`{  * "default_currency": "USD",      * "name": "string",      * "format": "TSV",      * "credentials": {          * "password": "pa$$word",              * "username": "string"                   },      * "location": "string",      * "preferred_processing_schedule": {          * "time": "02:59",              * "timezone": "Africa/Abidjan"                   },      * "status": "ACTIVE",      * "catalog_type": "RETAIL",      * "default_availability": "IN_STOCK"       }`

### Response samples

* 200
* 400
* 403
* 404
* default

Content type

application/json

Example

RETAIL

RETAIL

HOTEL

Copy

Expand all Collapse all

`{  * "created_at": "2022-03-14T15:15:22Z",      * "id": "string",      * "updated_at": "2022-03-14T15:16:34Z",      * "name": "string",      * "format": "TSV",      * "catalog_type": "RETAIL",      * "credentials": {          * "password": "pa$$word",              * "username": "string"                   },      * "location": "string",      * "preferred_processing_schedule": {          * "time": "02:59",              * "timezone": "Africa/Abidjan"                   },      * "status": "ACTIVE",      * "default_currency": "USD",      * "default_locale": "en-US",      * "default_country": "US",      * "default_availability": "IN_STOCK"       }`

[](#operation/feeds/delete)Delete feed
--------------------------------------

Delete a feed owned by the "operating user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to [Before you get started with Catalogs](https://help.pinterest.com/en/business/article/before-you-get-started-with-catalogs). For Hotel parterns, refer to [Pinterest API for shopping](https://developers.pinterest.com/docs/shopping/catalog/).

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read``catalogs:write`)

##### path Parameters

|     |     |
| --- | --- |
| feed\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a feed |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**204**

Feed deleted successfully.

**400**

Invalid feed parameters.

**403**

Forbidden. Account not approved for feed mutations yet.

**404**

Data feed not found.

**409**

Conflict. Can't delete a feed with active promotions.

**default**

Unexpected error

delete/catalogs/feeds/{feed\_id}

https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}

### Response samples

* 400
* 403
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 1,      * "message": "'feed_id' value '1511851494501_' must match the pattern: ^\\d+$\"}"       }`

[](#operation/feed_processing_results/list)List processing results for a given feed
-----------------------------------------------------------------------------------

Fetch a feed processing results owned by the "operation user\_account". Please note that for now the bookmark parameter is not functional and only the first page will be available until it is implemented in some release in the near future.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| feed\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a feed |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid parameters.

**401**

Unauthorized access.

**404**

Feed not found.

**default**

Unexpected error.

get/catalogs/feeds/{feed\_id}/processing\_results

https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}/processing\_results

### Response samples

* 200
* 400
* 401
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "created_at": "2022-03-14T15:15:22Z",                      * "id": "string",                      * "updated_at": "2022-03-14T15:16:34Z",                      * "ingestion_details": {                          * "errors": {                                  * "LINE_LEVEL_INTERNAL_ERROR": 0,                                      * "LARGE_PRODUCT_COUNT_DECREASE": 1,                                      * "ACCOUNT_FLAGGED": 0,                                      * "IMAGE_LEVEL_INTERNAL_ERROR": 0,                                      * "IMAGE_FILE_NOT_ACCESSIBLE": 0,                                      * "IMAGE_MALFORMED_URL": 0,                                      * "IMAGE_FILE_NOT_FOUND": 0,                                      * "IMAGE_INVALID_FILE": 0                                                       },                              * "info": {                                  * "IN_STOCK": 0,                                      * "OUT_OF_STOCK": 0,                                      * "PREORDER": 0                                                       },                              * "warnings": {                                  * "ADDITIONAL_IMAGE_LEVEL_INTERNAL_ERROR": 0,                                      * "ADDITIONAL_IMAGE_FILE_NOT_ACCESSIBLE": 0,                                      * "ADDITIONAL_IMAGE_MALFORMED_URL": 0,                                      * "ADDITIONAL_IMAGE_FILE_NOT_FOUND": 0,                                      * "ADDITIONAL_IMAGE_INVALID_FILE": 0,                                      * "HOTEL_PRICE_HEADER_IS_PRESENT": 0                                                       }                                           },                      * "status": "COMPLETED",                      * "product_counts": {                          * "original": 0,                              * "ingested": 0                                           },                      * "validation_details": {                          * "errors": {                                  * "FETCH_ERROR": 0,                                      * "FETCH_INACTIVE_FEED_ERROR": 0,                                      * "ENCODING_ERROR": 0,                                      * "DELIMITER_ERROR": 0,                                      * "REQUIRED_COLUMNS_MISSING": 0,                                      * "DUPLICATE_PRODUCTS": 0,                                      * "IMAGE_LINK_INVALID": 0,                                      * "ITEMID_MISSING": 0,                                      * "TITLE_MISSING": 0,                                      * "DESCRIPTION_MISSING": 0,                                      * "PRODUCT_LINK_MISSING": 0,                                      * "IMAGE_LINK_MISSING": 0,                                      * "AVAILABILITY_INVALID": 0,                                      * "PRODUCT_PRICE_INVALID": 0,                                      * "LINK_FORMAT_INVALID": 0,                                      * "PARSE_LINE_ERROR": 0,                                      * "ADWORDS_FORMAT_INVALID": 0,                                      * "INTERNAL_SERVICE_ERROR": 0,                                      * "NO_VERIFIED_DOMAIN": 0,                                      * "ADULT_INVALID": 0,                                      * "IMAGE_LINK_LENGTH_TOO_LONG": 0,                                      * "INVALID_DOMAIN": 0,                                      * "FEED_LENGTH_TOO_LONG": 0,                                      * "LINK_LENGTH_TOO_LONG": 0,                                      * "MALFORMED_XML": 0,                                      * "PRICE_MISSING": 0,                                      * "FEED_TOO_SMALL": 0,                                      * "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED": 0,                                      * "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE": 0,                                      * "PINJOIN_CONTENT_UNSAFE": 0,                                      * "BLOCKLISTED_IMAGE_SIGNATURE": 0,                                      * "LIST_PRICE_INVALID": 0,                                      * "PRICE_CANNOT_BE_DETERMINED": 0                                                       },                              * "warnings": {                                  * "AD_LINK_FORMAT_WARNING": 0,                                      * "AD_LINK_SAME_AS_LINK": 0,                                      * "TITLE_LENGTH_TOO_LONG": 0,                                      * "DESCRIPTION_LENGTH_TOO_LONG": 0,                                      * "GENDER_INVALID": 0,                                      * "AGE_GROUP_INVALID": 0,                                      * "SIZE_TYPE_INVALID": 0,                                      * "SIZE_SYSTEM_INVALID": 0,                                      * "LINK_FORMAT_WARNING": 0,                                      * "SALES_PRICE_INVALID": 0,                                      * "PRODUCT_CATEGORY_DEPTH_WARNING": 0,                                      * "ADWORDS_FORMAT_WARNING": 0,                                      * "ADWORDS_SAME_AS_LINK": 0,                                      * "DUPLICATE_HEADERS": 0,                                      * "FETCH_SAME_SIGNATURE": 1,                                      * "ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG": 0,                                      * "ADDITIONAL_IMAGE_LINK_WARNING": 0,                                      * "IMAGE_LINK_WARNING": 0,                                      * "SHIPPING_INVALID": 0,                                      * "TAX_INVALID": 0,                                      * "SHIPPING_WEIGHT_INVALID": 0,                                      * "EXPIRATION_DATE_INVALID": 0,                                      * "AVAILABILITY_DATE_INVALID": 0,                                      * "SALE_DATE_INVALID": 0,                                      * "WEIGHT_UNIT_INVALID": 0,                                      * "IS_BUNDLE_INVALID": 0,                                      * "UPDATED_TIME_INVALID": 0,                                      * "CUSTOM_LABEL_LENGTH_TOO_LONG": 0,                                      * "PRODUCT_TYPE_LENGTH_TOO_LONG": 0,                                      * "TOO_MANY_ADDITIONAL_IMAGE_LINKS": 0,                                      * "MULTIPACK_INVALID": 0,                                      * "INDEXED_PRODUCT_COUNT_LARGE_DELTA": 0,                                      * "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE": 0,                                      * "OPTIONAL_PRODUCT_CATEGORY_MISSING": 0,                                      * "OPTIONAL_PRODUCT_CATEGORY_INVALID": 0,                                      * "OPTIONAL_CONDITION_MISSING": 0,                                      * "OPTIONAL_CONDITION_INVALID": 0,                                      * "IOS_DEEP_LINK_INVALID": 0,                                      * "ANDROID_DEEP_LINK_INVALID": 0,                                      * "UTM_SOURCE_AUTO_CORRECTED": 0,                                      * "COUNTRY_DOES_NOT_MAP_TO_CURRENCY": 0,                                      * "MIN_AD_PRICE_INVALID": 0,                                      * "GTIN_INVALID": 0,                                      * "INCONSISTENT_CURRENCY_VALUES": 0,                                      * "SALES_PRICE_TOO_LOW": 0,                                      * "SHIPPING_WIDTH_INVALID": 0,                                      * "SHIPPING_HEIGHT_INVALID": 0,                                      * "SALES_PRICE_TOO_HIGH": 0,                                      * "MPN_INVALID": 0                                                       }                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/items/get)Get catalogs items
------------------------------------------

Get the items of the catalog owned by the "operation user\_account". [See detailed documentation here.](https://developers.pinterest.com/docs/shopping/catalog/#Update%20items%20in%20batch)

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| country<br><br>required | string<br><br>Example: country=US<br><br>Country for the Catalogs Items |
| language<br><br>required | string<br><br>Example: language=EN<br><br>Language for the Catalogs Items |
| item\_ids | Array of strings<br><br>Deprecated<br><br>Example: item\_ids=CR123<br><br>This parameter is deprecated. Use filters instead. |
| filters | object (CatalogsItemsFilters)<br><br>Identifies items to be retrieved. This is a required parameter. |

### Responses

**200**

Response containing the requested catalogs items

**400**

Invalid request parameters.

**401**

Not authorized to access catalogs items

**403**

Not authorized to access catalogs items

**default**

Unexpected error

get/catalogs/items

https://api.pinterest.com/v5/catalogs/items

### Response samples

* 200
* 400
* 401
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "catalog_type": "RETAIL",                      * "item_id": "DS0294-M",                      * "pins": [                          * {                                  * "id": "813744226420795884",                                      * "created_at": "2020-01-01T20:10:40-00:00",                                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                                      * "title": "string",                                      * "description": "string",                                      * "dominant_color": "#6E7874",                                      * "alt_text": "string",                                      * "creative_type": "REGULAR",                                      * "board_id": "string",                                      * "board_section_id": "string",                                      * "board_owner": {                                          * "username": "string"                                                                   },                                      * "is_owner": true,                                      * "media": {                                          * "media_type": "string"                                                                   },                                      * "parent_pin_id": "string",                                      * "is_standard": true,                                      * "has_been_promoted": true,                                      * "note": "string",                                      * "pin_metrics": {                                          * "pin_metrics": [                                                  * {                                                          * "90d": {                                                                  * "pin_click": 7,                                                                      * "impression": 2,                                                                      * "clickthrough": 3                                                                                                       },                                                              * "all_time": {                                                                  * "pin_click": 7,                                                                      * "impression": 2,                                                                      * "clickthrough": 3,                                                                      * "reaction": 10,                                                                      * "comment": 2                                                                                                       }                                                                                           },                                                      * null                                                                               ]                                                                   }                                                       }                                           ],                      * "attributes": {                          * "additional_image_link": [                                  * "[https://scene.example.com/image/image_v2.jpg](https://scene.example.com/image/image_v2.jpg)",                                      * "[https://scene.example.com/image/image_v3.jpg](https://scene.example.com/image/image_v3.jpg)"                                                       ],                              * "image_link": [                                  * "[https://scene.example.com/image/image.jpg](https://scene.example.com/image/image.jpg)"                                                       ],                              * "ad_link": "[https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest](https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest)",                              * "adult": true,                              * "age_group": "newborn",                              * "availability": "in stock",                              * "average_review_rating": 5,                              * "brand": "Josie’s Denim",                              * "checkout_enabled": false,                              * "color": "blue",                              * "condition": "new",                              * "custom_label_0": "Best sellers",                              * "custom_label_1": "Summer promotion",                              * "custom_label_2": "Winter sales",                              * "custom_label_3": "Woman dress",                              * "custom_label_4": "Man hat",                              * "description": "Casual fit denim shirt made with the finest quality Japanese denim.",                              * "free_shipping_label": true,                              * "free_shipping_limit": "35 USD",                              * "gender": "unisex",                              * "google_product_category": "Apparel & Accessories > Clothing > Shirts & Tops",                              * "gtin": 3234567890126,                              * "id": "DS0294-L",                              * "item_group_id": "DS0294",                              * "last_updated_time": 1641483432072,                              * "link": "[https://www.example.com/cat/womens-clothing/denim-shirt-0294](https://www.example.com/cat/womens-clothing/denim-shirt-0294)",                              * "material": "cotton",                              * "min_ad_price": "19.99 USD",                              * "mobile_link": "[https://m.example.com/cat/womens-clothing/denim-shirt-0294](https://m.example.com/cat/womens-clothing/denim-shirt-0294)",                              * "mpn": "PI12345NTEREST",                              * "number_of_ratings": 10,                              * "number_of_reviews": 10,                              * "pattern": "plaid",                              * "price": "24.99 USD",                              * "product_type": "Clothing > Women’s > Shirts > Denim",                              * "sale_price": "14.99 USD",                              * "shipping": "US:CA:Ground:0 USD",                              * "shipping_height": "12 in",                              * "shipping_weight": "3 kg",                              * "shipping_width": "16 in",                              * "size": "M",                              * "size_system": "US",                              * "size_type": "regular",                              * "tax": "US:1025433:6.00:y",                              * "title": "Women’s denim shirt, large",                              * "variant_names": [                                  * "Color",                                      * "Size"                                                       ],                              * "variant_values": [                                  * "Red",                                      * "Small"                                                       ]                                           }                               }                   ]       }`

[](#operation/items_batch/post)Operate on item batch
----------------------------------------------------

This endpoint supports multiple operations on a set of one or more catalog items owned by the "operation user\_account". [See detailed documentation here.](https://developers.pinterest.com/docs/shopping/catalog/#Update%20items%20in%20batch)

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read``catalogs:write`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to create catalogs items in a batch

One of

operate on item batchlegacy\_retail\_only

|     |     |
| --- | --- |
| catalog\_type<br><br>required | string (CatalogsType)<br><br>Type of the catalog entity.<br><br>RETAIL<br><br>RETAIL<br><br>HOTEL |
| country<br><br>required | string (Country)<br><br>Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more<br><br>Country ID from ISO 3166-1 alpha-2. |
| language<br><br>required | string (Language)<br><br>Enum: "AM" "AR" "AZ" "BG" "BN" "BS" "CA" "CS" "DA" "DV" "DZ" "DE" "EL" "EN" "ES" "ET" "FA" "FI" "FR" "HE" … 41 more<br><br>Language code, which is among the offical ISO 639-1 language list. |
| items<br><br>required | Array of any \[ 1 .. 1000 \] items<br><br>Array with catalogs item operations |

### Responses

**200**

Response containing the requested catalogs items batch

**400**

Invalid request parameters.

**401**

Not authenticated to post catalogs items

**403**

Not authorized to post catalogs items

**default**

Unexpected error

post/catalogs/items/batch

https://api.pinterest.com/v5/catalogs/items/batch

### Request samples

* Payload

Content type

application/json

Example

operate on item batch

operate on item batch

legacy\_retail\_only

Copy

Expand all Collapse all

`{  * "catalog_type": "RETAIL",      * "country": "US",      * "language": "EN",      * "items": [          * {                  * "item_id": "DS0294-M",                      * "operation": "CREATE",                      * "attributes": {                          * "additional_image_link": [                                  * "[https://scene.example.com/image/image_v2.jpg](https://scene.example.com/image/image_v2.jpg)",                                      * "[https://scene.example.com/image/image_v3.jpg](https://scene.example.com/image/image_v3.jpg)"                                                       ],                              * "image_link": [                                  * "[https://scene.example.com/image/image.jpg](https://scene.example.com/image/image.jpg)"                                                       ],                              * "ad_link": "[https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest](https://www.example.com/cat/denim-shirt/item012?utm_source=Pinterest)",                              * "adult": true,                              * "age_group": "newborn",                              * "availability": "in stock",                              * "average_review_rating": 5,                              * "brand": "Josie’s Denim",                              * "checkout_enabled": false,                              * "color": "blue",                              * "condition": "new",                              * "custom_label_0": "Best sellers",                              * "custom_label_1": "Summer promotion",                              * "custom_label_2": "Winter sales",                              * "custom_label_3": "Woman dress",                              * "custom_label_4": "Man hat",                              * "description": "Casual fit denim shirt made with the finest quality Japanese denim.",                              * "free_shipping_label": true,                              * "free_shipping_limit": "35 USD",                              * "gender": "unisex",                              * "google_product_category": "Apparel & Accessories > Clothing > Shirts & Tops",                              * "gtin": 3234567890126,                              * "id": "DS0294-L",                              * "item_group_id": "DS0294",                              * "last_updated_time": 1641483432072,                              * "link": "[https://www.example.com/cat/womens-clothing/denim-shirt-0294](https://www.example.com/cat/womens-clothing/denim-shirt-0294)",                              * "material": "cotton",                              * "min_ad_price": "19.99 USD",                              * "mobile_link": "[https://m.example.com/cat/womens-clothing/denim-shirt-0294](https://m.example.com/cat/womens-clothing/denim-shirt-0294)",                              * "mpn": "PI12345NTEREST",                              * "number_of_ratings": 10,                              * "number_of_reviews": 10,                              * "pattern": "plaid",                              * "price": "24.99 USD",                              * "product_type": "Clothing > Women’s > Shirts > Denim",                              * "sale_price": "14.99 USD",                              * "shipping": "US:CA:Ground:0 USD",                              * "shipping_height": "12 in",                              * "shipping_weight": "3 kg",                              * "shipping_width": "16 in",                              * "size": "M",                              * "size_system": "US",                              * "size_type": "regular",                              * "tax": "US:1025433:6.00:y",                              * "title": "Women’s denim shirt, large",                              * "variant_names": [                                  * "Color",                                      * "Size"                                                       ],                              * "variant_values": [                                  * "Red",                                      * "Small"                                                       ]                                           }                               }                   ]       }`

### Response samples

* 200
* 400
* 401
* 403
* default

Content type

application/json

Example

RETAIL

RETAIL

HOTEL

Copy

Expand all Collapse all

`{  * "batch_id": "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e",      * "created_time": "2020-01-01T20:10:40-00:00",      * "completed_time": "2022-03-10T15:37:10-00:00",      * "status": "PROCESSING",      * "catalog_type": "RETAIL",      * "items": [          * {                  * "item_id": "DS0294-M",                      * "errors": [                          * {                                  * "attribute": "title",                                      * "code": 106,                                      * "message": "Title is missing from product metadata."                                                       }                                           ],                      * "warnings": [                          * {                                  * "attribute": "title",                                      * "code": 106,                                      * "message": "Title is missing from product metadata."                                                       }                                           ],                      * "status": "SUCCESS"                               }                   ]       }`

[](#operation/items_batch/get)Get catalogs items batch
------------------------------------------------------

Get a single catalogs items batch owned by the "operating user\_account". [See detailed documentation here.](https://developers.pinterest.com/docs/shopping/catalog/#Update%20items%20in%20batch)

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| batch\_id<br><br>required | string<br><br>Example: 595953100599279259-66753b9bb65c46c49bd8503b27fecf9e<br><br>Id of a catalogs items batch to fetch |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Response containing the requested catalogs items batch

**401**

Not authenticated to access catalogs items batch

**403**

Not authorized to access catalogs items batch

**404**

Catalogs items batch not found

**405**

Method Not Allowed.

**default**

Unexpected error

get/catalogs/items/batch/{batch\_id}

https://api.pinterest.com/v5/catalogs/items/batch/{batch\_id}

### Response samples

* 200
* 401
* 403
* 404
* 405
* default

Content type

application/json

Example

RETAIL

RETAIL

HOTEL

Copy

Expand all Collapse all

`{  * "batch_id": "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e",      * "created_time": "2020-01-01T20:10:40-00:00",      * "completed_time": "2022-03-10T15:37:10-00:00",      * "status": "PROCESSING",      * "catalog_type": "RETAIL",      * "items": [          * {                  * "item_id": "DS0294-M",                      * "errors": [                          * {                                  * "attribute": "title",                                      * "code": 106,                                      * "message": "Title is missing from product metadata."                                                       }                                           ],                      * "warnings": [                          * {                                  * "attribute": "title",                                      * "code": 106,                                      * "message": "Title is missing from product metadata."                                                       }                                           ],                      * "status": "SUCCESS"                               }                   ]       }`

[](#operation/items_issues/list)List item issues for a given processing result
------------------------------------------------------------------------------

List item validation issues for a given feed processing result owned by the "operation user\_account". Please note that for now query parameters 'item\_numbers' and 'item\_validation\_issue' cannot be used simultaneously until it is implemented in some release in the future.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| processing\_result\_id<br><br>required | string^\\d+$<br><br>Example: 5224831246441439241<br><br>Unique identifier of a feed processing result. It can be acquired from the "id" field of the "items" array within the response of the [List processing results for a given feed](https://developers.pinterest.com/docs/api/v5/#operation/feed_processing_results/list). |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| item\_numbers | Array of integers<br><br>Example: item\_numbers=1&item\_numbers=5<br><br>Item number based on order of appearance in the Catalogs Feed. For example, '0' refers to first item found in a feed that was downloaded from a 'location' specified during feed creation. |
| item\_validation\_issue | string (CatalogsItemValidationIssue)<br><br>Enum: "AD\_LINK\_FORMAT\_WARNING" "AD\_LINK\_SAME\_AS\_LINK" "ADDITIONAL\_IMAGE\_LINK\_LENGTH\_TOO\_LONG" "ADDITIONAL\_IMAGE\_LINK\_WARNING" "ADULT\_INVALID" "ADWORDS\_FORMAT\_INVALID" "ADWORDS\_FORMAT\_WARNING" "ADWORDS\_SAME\_AS\_LINK" "AGE\_GROUP\_INVALID" "ANDROID\_DEEP\_LINK\_INVALID" "AVAILABILITY\_DATE\_INVALID" "AVAILABILITY\_INVALID" "BLOCKLISTED\_IMAGE\_SIGNATURE" "COUNTRY\_DOES\_NOT\_MAP\_TO\_CURRENCY" "CUSTOM\_LABEL\_LENGTH\_TOO\_LONG" "DESCRIPTION\_LENGTH\_TOO\_LONG" "DESCRIPTION\_MISSING" "DUPLICATE\_PRODUCTS" "EXPIRATION\_DATE\_INVALID" "GENDER\_INVALID" … 47 more<br><br>Example: item\_validation\_issue=TITLE\_MISSING<br><br>Filter item validation issues that have a given type of item validation issue. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**401**

Unauthorized access.

**404**

Processing Result not found.

**501**

Not implemented.

**default**

Unexpected error.

get/catalogs/processing\_results/{processing\_result\_id}/item\_issues

https://api.pinterest.com/v5/catalogs/processing\_results/{processing\_result\_id}/item\_issues

### Response samples

* 200
* 401
* 404
* 501
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "item_number": 0,                      * "item_id": "DS0294-L",                      * "errors": {                          * "ADULT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ADWORDS_FORMAT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "AVAILABILITY_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "BLOCKLISTED_IMAGE_SIGNATURE": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "DESCRIPTION_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "DUPLICATE_PRODUCTS": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IMAGE_LINK_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IMAGE_LINK_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IMAGE_LINK_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "INVALID_DOMAIN": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ITEMID_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ITEM_MAIN_IMAGE_DOWNLOAD_FAILURE": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "LINK_FORMAT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "LINK_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "LIST_PRICE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "MAX_ITEMS_PER_ITEM_GROUP_EXCEEDED": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PARSE_LINE_ERROR": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PINJOIN_CONTENT_UNSAFE": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRICE_CANNOT_BE_DETERMINED": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRICE_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRODUCT_LINK_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRODUCT_PRICE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "TITLE_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       }                                           },                      * "warnings": {                          * "AD_LINK_FORMAT_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "AD_LINK_SAME_AS_LINK": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ADDITIONAL_IMAGE_LINK_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ADDITIONAL_IMAGE_LINK_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ADWORDS_FORMAT_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ADWORDS_SAME_AS_LINK": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "AGE_GROUP_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SIZE_SYSTEM_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ANDROID_DEEP_LINK_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "AVAILABILITY_DATE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "COUNTRY_DOES_NOT_MAP_TO_CURRENCY": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "CUSTOM_LABEL_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "DESCRIPTION_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "EXPIRATION_DATE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "GENDER_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "GTIN_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IMAGE_LINK_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IOS_DEEP_LINK_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "IS_BUNDLE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "ITEM_ADDITIONAL_IMAGE_DOWNLOAD_FAILURE": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "LINK_FORMAT_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "MIN_AD_PRICE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "MPN_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "MULTIPACK_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "OPTIONAL_CONDITION_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "OPTIONAL_CONDITION_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "OPTIONAL_PRODUCT_CATEGORY_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "OPTIONAL_PRODUCT_CATEGORY_MISSING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRODUCT_CATEGORY_DEPTH_WARNING": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "PRODUCT_TYPE_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SALES_PRICE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SALES_PRICE_TOO_LOW": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SALES_PRICE_TOO_HIGH": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SALE_DATE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SHIPPING_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SHIPPING_HEIGHT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SHIPPING_WEIGHT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SHIPPING_WIDTH_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "SIZE_TYPE_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "TAX_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "TITLE_LENGTH_TOO_LONG": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "TOO_MANY_ADDITIONAL_IMAGE_LINKS": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "UTM_SOURCE_AUTO_CORRECTED": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       },                              * "WEIGHT_UNIT_INVALID": {                                  * "attribute_name": "TITLE",                                      * "provided_value": "string"                                                       }                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/catalogs_product_groups/list)List product groups
--------------------------------------------------------------

Get a list of product groups for a given Catalogs Feed Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### query Parameters

|     |     |
| --- | --- |
| feed\_id | string^\\d+$<br><br>Filter entities for a given feed\_id. If not given, all feeds are considered. |
| catalog\_id | string^\\d+$<br><br>Filter entities for a given catalog\_id. If not given, all catalogs are considered. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid feed parameters.

**401**

Unauthorized access.

**403**

Forbidden. Account not approved for catalog product group mutations yet.

**404**

Data feed not found.

**409**

Conflict. Can't create this catalogs product group with this value.

**default**

Unexpected error.

get/catalogs/product\_groups

https://api.pinterest.com/v5/catalogs/product\_groups

### Response samples

* 200
* 400
* 401
* 403
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "443727193917",                      * "name": "Most Popular",                      * "description": "string",                      * "filters": {                          * "any_of": [                                  * {                                          * "MIN_PRICE": {                                                  * "inclusion": true,                                                      * "values": 0,                                                      * "negated": false                                                                               }                                                                   }                                                       ]                                           },                      * "is_featured": true,                      * "type": "TOP_SELLERS",                      * "status": "ACTIVE",                      * "created_at": 1621350033000,                      * "updated_at": 1622742155000,                      * "feed_id": "2680059592705",                      * "catalog_type": "RETAIL"                               }                   ],      * "bookmark": "string"       }`

[](#operation/catalogs_product_groups/create)Create product group
-----------------------------------------------------------------

Create product group to use in Catalogs owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:write`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to created a catalogs product group.

One of

retailhotel

|     |     |
| --- | --- |
| name<br><br>required | string |
| description | string Nullable |
| is\_featured | boolean<br><br>Default: false<br><br>boolean indicator of whether the product group is being featured or not |
| filters<br><br>required | object or object (catalogs\_product\_group\_filters)<br><br>Object holding a group of filters for request on catalog product group. This is a distinct schema It is not possible to create or update a Product Group with empty filters. But some automatically generated Product Groups might have empty filters. |
| feed\_id<br><br>required | string^\\d+$<br><br>Catalog Feed id pertaining to the catalog product group. |

### Responses

**201**

Success

**400**

Invalid body.

**401**

Unauthorized access.

**403**

Forbidden. Account not approved for catalog product group mutations yet.

**409**

Conflict. Can't create this catalogs product group with this value.

**default**

Unexpected error.

post/catalogs/product\_groups

https://api.pinterest.com/v5/catalogs/product\_groups

### Request samples

* Payload

Content type

application/json

Example

A simple retail example that applies "all of the following filters".

A simple retail example that applies "all of the following filters".

A more complete retail example that applies "any of the following filters".

A simple hotel example that applies "all of the following filters".

The use of "all\_of" creates a Product Group where all of the individual filters must be satisfied by a product to be included in the Product Group.

Copy

Expand all Collapse all

`{  * "name": "Few Filters using \"all_of\"",      * "feed_id": "2680059592705",      * "featured": false,      * "filters": {          * "all_of": [                  * {                          * "MIN_PRICE": {                                  * "values": 999.99,                                      * "inclusion": true                                                       }                                           },                      * {                          * "CURRENCY": {                                  * "values": "USD"                                                       }                                           },                      * {                          * "CUSTOM_LABEL_0": {                                  * "values": [                                          * "Luxury Items"                                                                   ]                                                       }                                           }                               ]                   }       }`

### Response samples

* 201
* 400
* 401
* 403
* 409
* default

Content type

application/json

Example

feed\_based\_product\_group

feed\_based\_product\_group

catalog\_based\_product\_group

Copy

Expand all Collapse all

`{  * "id": "443727193917",      * "name": "Most Popular",      * "description": "string",      * "filters": {          * "any_of": [                  * {                          * "MIN_PRICE": {                                  * "inclusion": true,                                      * "values": 0,                                      * "negated": false                                                       }                                           }                               ]                   },      * "is_featured": true,      * "type": "TOP_SELLERS",      * "status": "ACTIVE",      * "created_at": 1621350033000,      * "updated_at": 1622742155000,      * "feed_id": "2680059592705",      * "catalog_type": "RETAIL"       }`

[](#operation/catalogs_product_groups/get)Get product group
-----------------------------------------------------------

Get a singe product group for a given Catalogs Product Group Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| product\_group\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a product group |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid catalogs product group id parameters.

**401**

Unauthorized access.

**403**

Forbidden. Account not approved for catalog product group mutations yet.

**404**

Catalogs product group not found.

**409**

Conflict. Can't get a catalogs product group without an existing catalog.

**default**

Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}

https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}

### Response samples

* 200
* 400
* 401
* 403
* 404
* 409
* default

Content type

application/json

Example

feed\_based\_product\_group

feed\_based\_product\_group

catalog\_based\_product\_group

Copy

Expand all Collapse all

`{  * "id": "443727193917",      * "name": "Most Popular",      * "description": "string",      * "filters": {          * "any_of": [                  * {                          * "MIN_PRICE": {                                  * "inclusion": true,                                      * "values": 0,                                      * "negated": false                                                       }                                           }                               ]                   },      * "is_featured": true,      * "type": "TOP_SELLERS",      * "status": "ACTIVE",      * "created_at": 1621350033000,      * "updated_at": 1622742155000,      * "feed_id": "2680059592705",      * "catalog_type": "RETAIL"       }`

[](#operation/catalogs_product_groups/delete)Delete product group
-----------------------------------------------------------------

Delete a product group owned by the "operation user\_account" from being in use in Catalogs.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:write`)

##### path Parameters

|     |     |
| --- | --- |
| product\_group\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a product group |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**204**

Catalogs Product Group deleted successfully.

**400**

Invalid catalogs product group id parameters.

**401**

Unauthorized access.

**403**

Forbidden. Account not approved for catalog product group mutations yet.

**404**

Catalogs product group not found.

**409**

Conflict. Can't delete this catalogs product group.

**default**

Unexpected error.

delete/catalogs/product\_groups/{product\_group\_id}

https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}

### Response samples

* 400
* 401
* 403
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 1,      * "message": "'product_group_id' value '11851494501_' must match the pattern: ^\\d+$\"}"       }`

[](#operation/catalogs_product_groups/update)Update product group
-----------------------------------------------------------------

Update product group owned by the "operation user\_account" to use in Catalogs.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:write`)

##### path Parameters

|     |     |
| --- | --- |
| product\_group\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a product group |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to Update a catalogs product group.

One of

retailhotel

|     |     |
| --- | --- |
| name | string |
| description | string Nullable |
| is\_featured | boolean<br><br>boolean indicator of whether the product group is being featured or not |
| filters | object or object (catalogs\_product\_group\_filters)<br><br>Object holding a group of filters for request on catalog product group. This is a distinct schema It is not possible to create or update a Product Group with empty filters. But some automatically generated Product Groups might have empty filters. |

### Responses

**200**

Success

**400**

Invalid parameters.

**401**

Unauthorized access.

**403**

Forbidden. Account not approved for catalog product group mutations yet.

**404**

Catalogs product group not found.

**409**

Conflict. Can't update this catalogs product group to this value.

**default**

Unexpected error.

patch/catalogs/product\_groups/{product\_group\_id}

https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}

### Request samples

* Payload

Content type

application/json

Example

retail

retail

hotel

Copy

Expand all Collapse all

`{  * "name": "string",      * "description": "string",      * "is_featured": true,      * "filters": {          * "any_of": [                  * {                          * "MIN_PRICE": {                                  * "inclusion": true,                                      * "values": 0,                                      * "negated": false                                                       }                                           }                               ]                   }       }`

### Response samples

* 200
* 400
* 401
* 403
* 404
* 409
* default

Content type

application/json

Example

feed\_based\_product\_group

feed\_based\_product\_group

catalog\_based\_product\_group

Copy

Expand all Collapse all

`{  * "id": "443727193917",      * "name": "Most Popular",      * "description": "string",      * "filters": {          * "any_of": [                  * {                          * "MIN_PRICE": {                                  * "inclusion": true,                                      * "values": 0,                                      * "negated": false                                                       }                                           }                               ]                   },      * "is_featured": true,      * "type": "TOP_SELLERS",      * "status": "ACTIVE",      * "created_at": 1621350033000,      * "updated_at": 1622742155000,      * "feed_id": "2680059592705",      * "catalog_type": "RETAIL"       }`

[](#operation/catalogs_product_groups/product_counts_get)Get product counts for a Product Group
-----------------------------------------------------------------------------------------------

Get a product counts for a given Catalogs Product Group owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`catalogs:read`)

##### path Parameters

|     |     |
| --- | --- |
| product\_group\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a product group |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**404**

Product Group Not Found.

**409**

Can't access this feature without an existing catalog.

**default**

Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}/product\_counts

https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}/product\_counts

### Response samples

* 200
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "in_stock": 0,      * "out_of_stock": 0,      * "preorder": 0,      * "total": 0       }`

[](#operation/catalogs_product_group_pins/list)List products for a Product Group
--------------------------------------------------------------------------------

Get a list of product pins for a given Catalogs Product Group Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``catalogs:read``pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| product\_group\_id<br><br>required | string^\\d+$<br><br>Unique identifier of a product group |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid parameters.

**401**

Unauthorized access.

**404**

Catalogs product group not found.

**default**

Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}/products

https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}/products

### Response samples

* 200
* 400
* 401
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "metadata": {                          * "item_id": "DS0294-L",                              * "item_group_id": "DS0294",                              * "availability": "IN_STOCK",                              * "price": 24.99,                              * "sale_price": 14.99,                              * "currency": "USD"                                           },                      * "pin": {                          * "id": "813744226420795884",                              * "created_at": "2020-01-01T20:10:40-00:00",                              * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "title": "string",                              * "description": "string",                              * "dominant_color": "#6E7874",                              * "alt_text": "string",                              * "creative_type": "REGULAR",                              * "board_id": "string",                              * "board_section_id": "string",                              * "board_owner": {                                  * "username": "string"                                                       },                              * "is_owner": true,                              * "media": {                                  * "media_type": "string"                                                       },                              * "parent_pin_id": "string",                              * "is_standard": true,                              * "has_been_promoted": true,                              * "note": "string",                              * "pin_metrics": {                                  * "pin_metrics": [                                          * {                                                  * "90d": {                                                          * "pin_click": 7,                                                              * "impression": 2,                                                              * "clickthrough": 3                                                                                           },                                                      * "all_time": {                                                          * "pin_click": 7,                                                              * "impression": 2,                                                              * "clickthrough": 3,                                                              * "reaction": 10,                                                              * "comment": 2                                                                                           }                                                                               },                                              * null                                                                   ]                                                       }                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/products_by_product_group_filter/list)List filtered products
--------------------------------------------------------------------------

List products Pins owned by the "operation user\_account" that meet the criteria specified in the Catalogs Product Group Filter given in the request.

* This endpoint has been implemented in POST to allow for complex filters. This specific POST endpoint is designed to be idempotent.
* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account: Owner, Admin, Catalogs Manager.

[Learn more](https://developers.pinterest.com/docs/shopping/catalog/)

ratelimit-category: catalogs\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``catalogs:read``pins:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Object holding a group of filters for a catalog product group

One of

object

|     |     |
| --- | --- |
| feed\_id<br><br>required | string^\\d+$<br><br>Catalog Feed id pertaining to the catalog product group filter. |
| filters<br><br>required | CatalogsProductGroupFiltersAnyOf (object) or CatalogsProductGroupFiltersAllOf (object) (catalogs\_product\_group\_filters)<br><br>Object holding a group of filters for a catalog product group |

### Responses

**200**

Success

**401**

Unauthorized access.

**409**

Conflict. Can't get products.

**default**

Unexpected error.

post/catalogs/products/get\_by\_product\_group\_filters

https://api.pinterest.com/v5/catalogs/products/get\_by\_product\_group\_filters

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "feed_id": "2680059592705",      * "filters": {          * "any_of": [                  * {                          * "MIN_PRICE": {                                  * "inclusion": true,                                      * "values": 0,                                      * "negated": false                                                       }                                           }                               ]                   }       }`

### Response samples

* 200
* 401
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "metadata": {                          * "item_id": "DS0294-L",                              * "item_group_id": "DS0294",                              * "availability": "IN_STOCK",                              * "price": 24.99,                              * "sale_price": 14.99,                              * "currency": "USD"                                           },                      * "pin": {                          * "id": "813744226420795884",                              * "created_at": "2020-01-01T20:10:40-00:00",                              * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                              * "title": "string",                              * "description": "string",                              * "dominant_color": "#6E7874",                              * "alt_text": "string",                              * "creative_type": "REGULAR",                              * "board_id": "string",                              * "board_section_id": "string",                              * "board_owner": {                                  * "username": "string"                                                       },                              * "is_owner": true,                              * "media": {                                  * "media_type": "string"                                                       },                              * "parent_pin_id": "string",                              * "is_standard": true,                              * "has_been_promoted": true,                              * "note": "string",                              * "pin_metrics": {                                  * "pin_metrics": [                                          * {                                                  * "90d": {                                                          * "pin_click": 7,                                                              * "impression": 2,                                                              * "clickthrough": 3                                                                                           },                                                      * "all_time": {                                                          * "pin_click": 7,                                                              * "impression": 2,                                                              * "clickthrough": 3,                                                              * "reaction": 10,                                                              * "comment": 2                                                                                           }                                                                               },                                              * null                                                                   ]                                                       }                                           }                               }                   ],      * "bookmark": "string"       }`

[](#tag/conversion_events)conversion\_events
============================================

Submit conversion events via the Pinterest API.

[](#operation/events/create)Send conversions
--------------------------------------------

The Pinterest API offers advertisers a way to send Pinterest their conversion information (including web conversions, in-app conversions, or even offline conversions) based on their `ad_account_id`. The request body should be a JSON object.

* This endpoint requires an `access_token` be generated through Ads Manager. Review the [Conversions Guide](https://developers.pinterest.com/docs/conversions/conversions/) for more details.
* The token's `user_account` must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Audience, Campaign. (Note that the token can be used across multiple ad accounts under an user ID.)
* This endpoint has a rate limit of 5,000 calls per minute per ad account.
* If the merchant is submitting this information using both Pinterest conversion tags and the Pinterest API, Pinterest will remove duplicate information before reporting. (Note that events that took place offline cannot be deduplicated.)

ratelimit-category: ads\_conversions

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`) [conversion\_token](#section/Authentication/conversion_token)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| test | boolean<br><br>Include query param ?test=true to mark the request as a test request. The events will not be recorded but the API will still return the same response messages. Use this mode to verify your requests are working and your events are constructed correctly. Warning: If you use this query parameter, be certain that it is off (set to false or deleted) before sending a legitimate (non-testing) request. |

##### Request Body schema: application/json

Conversion events.

|     |     |
| --- | --- |
| data<br><br>required | Array of objects \[ 1 .. 1000 \] items |

### Responses

**200**

Success

**400**

The request was invalid.

**401**

Not authorized to send conversion events

**403**

Unauthorized access.

**422**

Not all events were successfully processed.

**429**

This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits within a short time window.

**503**

The endpoint has been ramped down and is currently not accepting any traffic.

**default**

Unexpected errors

post/ad\_accounts/{ad\_account\_id}/events

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/events

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "event_name": "checkout",                      * "action_source": "app_ios",                      * "event_time": 1451431341,                      * "event_id": "eventId0001",                      * "event_source_url": "[https://www.my-clothing-shop.org/](https://www.my-clothing-shop.org/)",                      * "opt_out": false,                      * "partner_name": "ss-partnername",                      * "user_data": {                          * "em": [                                  * "411e44ce1261728ffd2c0686e44e3fffe413c0e2c5adc498bc7da883d476b9c8",                                      * "09831ea51bd1b7b32a836683a00a9ccaf3d05f59499f42d9883412ed79289969"                                                       ],                              * "hashed_maids": [                                  * "0192518eb84137ccfe82c8b6322d29631dae7e28ed9d0f6dd5f245d73a58c5f1",                                      * "837b850ac46d62b2272a71de73c27801ff011ac1e36c5432620c8755cf90db46"                                                       ],                              * "client_ip_address": "216.3.128.12",                              * "client_user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"                                           },                      * "custom_data": {                          * "currency": "USD",                              * "value": "72.39",                              * "content_ids": [                                  * "red-pinterest-shirt-logo-1",                                      * "purple-pinterest-shirt-logo-3"                                                       ],                              * "content_name": "pinterest-themed-clothing",                              * "content_category": "shirts",                              * "content_brand": "pinterest-brand",                              * "contents": [                                  * {                                          * "id": "red-pinterest-shirt-logo-1",                                              * "item_price": "1325.12",                                              * "quantity": 5                                                                   }                                                       ],                              * "num_items": 2,                              * "order_id": "my_order_id",                              * "search_string": "sample string",                              * "opt_out_type": "LDP",                              * "np": "ss-company"                                           },                      * "app_id": "429047995",                      * "app_name": "Pinterest",                      * "app_version": "7.9",                      * "device_brand": "Apple",                      * "device_carrier": "T-Mobile",                      * "device_model": "iPhone X",                      * "device_type": "iPhone",                      * "os_version": "12.1.4",                      * "wifi": false,                      * "language": "en"                               }                   ]       }`

### Response samples

* 200
* 400
* 401
* 403
* 422
* 429
* 503
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "num_events_received": 0,      * "num_events_processed": 0,      * "events": [          * {                  * "status": "processed",                      * "error_message": "string",                      * "warning_message": "string"                               }                   ]       }`

[](#tag/conversion_tags)conversion\_tags
========================================

View, create, or update conversion tags.

[](#operation/conversion_tags/list)Get conversion tags
------------------------------------------------------

List conversion tags associated with an ad account.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| filter\_deleted | boolean<br><br>Default: false<br><br>Example: filter\_deleted=true<br><br>Filter out deleted tags. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tags

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "ad_account_id": "549755885175",                      * "code_snippet": "<script type=text/javascript> [...]",                      * "enhanced_match_status": "VALIDATION_COMPLETE",                      * "id": "2617998078212",                      * "last_fired_time_ms": 1599030000000,                      * "name": "ACME Checkout Test Tag",                      * "status": "ACTIVE",                      * "version": "3",                      * "configs": {                          * "aem_enabled": true,                              * "md_frequency": 0.6,                              * "aem_fnln_enabled": true,                              * "aem_ph_enabled": true,                              * "aem_ge_enabled": true,                              * "aem_db_enabled": true,                              * "aem_loc_enabled": true                                           }                               }                   ]       }`

[](#operation/conversion_tags/create)Create conversion tag
----------------------------------------------------------

Create a conversion tag, also known as [Pinterest tag](https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag), with the option to enable enhanced match.

The Pinterest Tag tracks actions people take on the ad account’ s website after they view the ad account's ad on Pinterest. The advertiser needs to customize this tag to track conversions.

For more information, see:

[Set up the Pinterest tag](https://help.pinterest.com/en/business/article/set-up-the-pinterest-tag)

[Pinterest Tag](https://developers.pinterest.com/docs/conversions/pinterest-tag/)

[Enhanced match](https://developers.pinterest.com/docs/conversions/enhanced-match/)

sandbox: disabled

ratelimit-category: ads\_write

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Conversion Tag to create

|     |     |
| --- | --- |
| name<br><br>required | string (name)<br><br>Conversion tag name. |
| aem\_enabled | boolean (aem\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match email is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |
| md\_frequency | number (md\_frequency) Nullable<br><br>Default: 1<br><br>Metadata ingestion frequency. |
| aem\_fnln\_enabled | boolean (aem\_fnln\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match name is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |
| aem\_ph\_enabled | boolean (aem\_ph\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match phone is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |
| aem\_ge\_enabled | boolean (aem\_ge\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match gender is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |
| aem\_db\_enabled | boolean (aem\_db\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match birthdate is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |
| aem\_loc\_enabled | boolean (aem\_loc\_enabled) Nullable<br><br>Default: false<br><br>Whether Automatic Enhanced Match location is enabled. See [Enhanced match](https://help.pinterest.com/en/business/article/enhanced-match) for more information. |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/conversion\_tags

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "ACME Tools Tag"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "code_snippet": "<script type=text/javascript> [...]",      * "enhanced_match_status": "VALIDATION_COMPLETE",      * "id": "2617998078212",      * "last_fired_time_ms": 1599030000000,      * "name": "ACME Checkout Test Tag",      * "status": "ACTIVE",      * "version": "3",      * "configs": {          * "aem_enabled": true,              * "md_frequency": 0.6,              * "aem_fnln_enabled": true,              * "aem_ph_enabled": true,              * "aem_ge_enabled": true,              * "aem_db_enabled": true,              * "aem_loc_enabled": true                   }       }`

[](#operation/ocpm_eligible_conversion_tags/get)Get Ocpm eligible conversion tags
---------------------------------------------------------------------------------

Get Ocpm eligible conversion tag events for an ad account.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**default**

Unexpected errors

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/ocpm\_eligible

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/ocpm\_eligible

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "12345": [          * {                  * "conversion_event": "PAGE_LOAD",                      * "created_time": 1564768710,                      * "conversion_tag_id": "2614324385652",                      * "ad_account_id": "549757463328"                               },              * {                  * "conversion_event": "CHECKOUT",                      * "created_time": 1564710210,                      * "conversion_tag_id": "2614324315793",                      * "ad_account_id": "549757463328"                               }                   ]       }`

[](#operation/page_visit_conversion_tags/get)Get page visit conversion tags
---------------------------------------------------------------------------

Get all page visit conversion tag events for an ad account.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/page\_visit

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/page\_visit

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "conversion_event": "PAGE_LOAD",                      * "conversion_tag_id": "2614324385652",                      * "ad_account_id": "549757463328",                      * "created_time": 1564768710                               }                   ],      * "bookmark": "string"       }`

[](#operation/conversion_tags/get)Get conversion tag
----------------------------------------------------

Get information about an existing conversion tag.

sandbox: disabled

ratelimit-category: ads\_read

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| conversion\_tag\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Example: 2617998078212<br><br>Id of the conversion tag. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/{conversion\_tag\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/{conversion\_tag\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549755885175",      * "code_snippet": "<script type=text/javascript> [...]",      * "enhanced_match_status": "VALIDATION_COMPLETE",      * "id": "2617998078212",      * "last_fired_time_ms": 1599030000000,      * "name": "ACME Checkout Test Tag",      * "status": "ACTIVE",      * "version": "3",      * "configs": {          * "aem_enabled": true,              * "md_frequency": 0.6,              * "aem_fnln_enabled": true,              * "aem_ph_enabled": true,              * "aem_ge_enabled": true,              * "aem_db_enabled": true,              * "aem_loc_enabled": true                   }       }`

[](#tag/customer_lists)customer\_lists
======================================

View, create, or update customer lists.

[](#operation/customer_lists/create)Create customer lists
---------------------------------------------------------

Create a customer list from your records(hashed or plain-text email addresses, or hashed MAIDs or IDFAs).

A customer list is one of the four types of Pinterest audiences: for more information, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting) or the [Audiences](https://developers.pinterest.com/docs/ads/targeting/#Audiences) section of the ads management guide.

**Please review our [requirements](https://help.pinterest.com/en/business/article/audience-targeting#section-13341) for what type of information is allowed when uploading a customer list.**

When you create a customer list, the system scans the list for existing Pinterest accounts; the list must include at least 100 Pinterest accounts. Your original list will be deleted when the matching process is complete. The filtered list – containing only the Pinterest accounts that were included in your starting list – is what will be used to create the audience.

Note that once you have created your customer list, you must convert it into an audience (of the “ CUSTOMER\_LIST” type) using the [create audience endpoint](#operation/create_audience_handler) before it can be used.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Parameters to get Customer lists info

|     |     |
| --- | --- |
| name<br><br>required | string (name)<br><br>Customer list name. |
| records<br><br>required | string (records)<br><br>Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5. |
| list\_type | string (list\_type)<br><br>Default: "EMAIL"<br><br>Enum: "EMAIL" "IDFA" "MAID" "LR\_ID" "DLX\_ID" "HASHED\_PINNER\_ID"<br><br>User list type |
| exceptions | object (exceptions)<br><br>Customer list errors. |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/customer\_lists

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "The Glengarry Glen Ross leads",      * "records": "email1@pinterest.com,email2@pinterest.com,..<more records>",      * "list_type": "EMAIL",      * "exceptions": { }       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549756359984",      * "created_time": 1452208622,      * "id": "643",      * "name": "The Glengarry Glen Ross leads",      * "num_batches": 2,      * "num_removed_user_records": 0,      * "num_uploaded_user_records": 11,      * "status": "PROCESSING",      * "type": "customerlist",      * "updated_time": 1461269616,      * "exceptions": { }       }`

[](#operation/customer_lists/list)Get customer lists
----------------------------------------------------

Get a set of customer lists including id and name based on the filters provided.

(Customer lists are a type of audience.) For more information, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting) or the [Audiences](https://developers.pinterest.com/docs/ads/targeting/#Audiences) section of the ads management guide.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/customer\_lists

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "ad_account_id": "549756359984",                      * "created_time": 1452208622,                      * "id": "643",                      * "name": "The Glengarry Glen Ross leads",                      * "num_batches": 2,                      * "num_removed_user_records": 0,                      * "num_uploaded_user_records": 11,                      * "status": "PROCESSING",                      * "type": "customerlist",                      * "updated_time": 1461269616,                      * "exceptions": { }                               }                   ],      * "bookmark": "string"       }`

[](#operation/customer_lists/get)Get customer list
--------------------------------------------------

Gets a specific customer list given the customer list ID.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| customer\_list\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of a customer list |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549756359984",      * "created_time": 1452208622,      * "id": "643",      * "name": "The Glengarry Glen Ross leads",      * "num_batches": 2,      * "num_removed_user_records": 0,      * "num_uploaded_user_records": 11,      * "status": "PROCESSING",      * "type": "customerlist",      * "updated_time": 1461269616,      * "exceptions": { }       }`

[](#operation/customer_lists/update)Update customer list
--------------------------------------------------------

Append or remove records to/from an existing customer list. (A customer list is one of the four types of Pinterest audiences.)

When you add records to an existing customer list, the system scans the additions for existing Pinterest accounts; those are the records that will be added to your “CUSTOMER\_LIST” audience. Your original list of records to add will be deleted when the matching process is complete.

For more information, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting) or the [Audiences](https://developers.pinterest.com/docs/ads/targeting/#Audiences) section of the ads management guide.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| customer\_list\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of a customer list |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| records<br><br>required | string (records)<br><br>Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5. |
| operation\_type<br><br>required | string (operation\_type)<br><br>Enum: "ADD" "REMOVE"<br><br>User list operation type (add or remove) |
| exceptions | object (Generic exception class to be used within schemas) |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "records": "email2@pinterest.com,email6@pinterest.com,",      * "operation_type": "REMOVE",      * "exceptions": {          * "code": 2,              * "message": "Advertiser not found."                   }       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "ad_account_id": "549756359984",      * "created_time": 1452208622,      * "id": "643",      * "name": "The Glengarry Glen Ross leads",      * "num_batches": 2,      * "num_removed_user_records": 0,      * "num_uploaded_user_records": 11,      * "status": "PROCESSING",      * "type": "customerlist",      * "updated_time": 1461269616,      * "exceptions": { }       }`

[](#tag/integrations)integrations
=================================

View, create, or update commerce integrations.

[](#operation/integrations_commerce/post)Create commerce integration
--------------------------------------------------------------------

Create commerce integration metadata to link an external business ID with a Pinterest merchant & ad account. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### Request Body schema: application/json

Parameters to get create/update the Integration Metadata

|     |     |
| --- | --- |
| external\_business\_id | string Nullable<br><br>External business ID for the integration. |
| connected\_merchant\_id | string |
| connected\_advertiser\_id | string |
| connected\_lba\_id | string |
| connected\_tag\_id | string |
| partner\_access\_token | string |
| partner\_refresh\_token | string |
| partner\_primary\_email | string |
| partner\_access\_token\_expiry | integer |
| partner\_refresh\_token\_expiry | integer |
| scopes | string |
| additional\_id\_1 | string |
| partner\_metadata | string |

### Responses

**200**

Success

**404**

Integration not found.

**409**

Can't access this integration metadata.

**default**

Unexpected error.

post/integrations/commerce

https://api.pinterest.com/v5/integrations/commerce

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "external_business_id": "string",      * "connected_merchant_id": "string",      * "connected_advertiser_id": "string",      * "connected_lba_id": "string",      * "connected_tag_id": "string",      * "partner_access_token": "string",      * "partner_refresh_token": "string",      * "partner_primary_email": "string",      * "partner_access_token_expiry": 0,      * "partner_refresh_token_expiry": 0,      * "scopes": "string",      * "additional_id_1": "string",      * "partner_metadata": "string"       }`

### Response samples

* 200
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "7329167449607351372",      * "external_business_id": "1238401984",      * "connected_merchant_id": "1445572885401",      * "connected_user_id": "871939315263957401",      * "connected_advertiser_id": "549764738871",      * "connected_lba_id": "871939315263957402",      * "connected_tag_id": "2412141155151",      * "partner_access_token_expiry": 1621350033000,      * "partner_refresh_token_expiry": 1621350033000,      * "scopes": "accounts:read",      * "created_timestamp": 1621350033000,      * "updated_timestamp": 1621350033000,      * "additional_id_1": "128464",      * "partner_metadata": ""       }`

[](#operation/integrations_commerce/get)Get commerce integration
----------------------------------------------------------------

Get commerce integration metadata associated with the given external business ID. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| external\_business\_id<br><br>required | string<br><br>External business ID for the integration. |

### Responses

**200**

Success

**404**

Integration not found.

**409**

Can't access this integration metadata.

**default**

Unexpected error.

get/integrations/commerce/{external\_business\_id}

https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}

### Response samples

* 200
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "7329167449607351372",      * "external_business_id": "1238401984",      * "connected_merchant_id": "1445572885401",      * "connected_user_id": "871939315263957401",      * "connected_advertiser_id": "549764738871",      * "connected_lba_id": "871939315263957402",      * "connected_tag_id": "2412141155151",      * "partner_access_token_expiry": 1621350033000,      * "partner_refresh_token_expiry": 1621350033000,      * "scopes": "accounts:read",      * "created_timestamp": 1621350033000,      * "updated_timestamp": 1621350033000,      * "additional_id_1": "128464",      * "partner_metadata": ""       }`

[](#operation/integrations_commerce/patch)Update commerce integration
---------------------------------------------------------------------

Update commerce integration metadata for the given external business ID. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| external\_business\_id<br><br>required | string<br><br>External business ID for the integration. |

##### Request Body schema: application/json

Parameters to get create/update the Integration Metadata

|     |     |
| --- | --- |
| connected\_merchant\_id | string |
| connected\_advertiser\_id | string |
| connected\_lba\_id | string |
| connected\_tag\_id | string |
| partner\_access\_token | string |
| partner\_refresh\_token | string |
| partner\_primary\_email | string |
| partner\_access\_token\_expiry | number |
| partner\_refresh\_token\_expiry | number |
| scopes | string |
| additional\_id\_1 | string |
| partner\_metadata | string |

### Responses

**200**

Success

**404**

Integration not found.

**409**

Can't access this integration metadata.

**default**

Unexpected error.

patch/integrations/commerce/{external\_business\_id}

https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "connected_merchant_id": "string",      * "connected_advertiser_id": "string",      * "connected_lba_id": "string",      * "connected_tag_id": "string",      * "partner_access_token": "string",      * "partner_refresh_token": "string",      * "partner_primary_email": "string",      * "partner_access_token_expiry": 0,      * "partner_refresh_token_expiry": 0,      * "scopes": "string",      * "additional_id_1": "string",      * "partner_metadata": "string"       }`

### Response samples

* 200
* 404
* 409
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "7329167449607351372",      * "external_business_id": "1238401984",      * "connected_merchant_id": "1445572885401",      * "connected_user_id": "871939315263957401",      * "connected_advertiser_id": "549764738871",      * "connected_lba_id": "871939315263957402",      * "connected_tag_id": "2412141155151",      * "partner_access_token_expiry": 1621350033000,      * "partner_refresh_token_expiry": 1621350033000,      * "scopes": "accounts:read",      * "created_timestamp": 1621350033000,      * "updated_timestamp": 1621350033000,      * "additional_id_1": "128464",      * "partner_metadata": ""       }`

[](#operation/integrations_commerce/del)Delete commerce integration
-------------------------------------------------------------------

Delete commerce integration metadata for the given external business ID. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| external\_business\_id<br><br>required | string<br><br>External business ID for the integration. |

### Responses

**204**

Commerce Integration deleted successfully

**default**

Unexpected error.

delete/integrations/commerce/{external\_business\_id}

https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}

### Response samples

* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 0,      * "message": "string"       }`

[](#operation/integrations_logs/post)Receives batched logs from integration applications.
-----------------------------------------------------------------------------------------

This endpoint receives batched logs from integration applications on partner platforms. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### Request Body schema: application/json

Ingest log information from external integration application.

|     |     |
| --- | --- |
| logs<br><br>required | Array of objects (IntegrationLog) |

### Responses

**200**

Success.

**400**

Bad request.

**default**

Unexpected error

post/integrations/logs

https://api.pinterest.com/v5/integrations/logs

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "logs": [          * {                  * "client_timestamp": 0,                      * "event_type": "APP",                      * "log_level": "INFO",                      * "external_business_id": "string",                      * "advertiser_id": "string",                      * "merchant_id": "string",                      * "tag_id": "string",                      * "feed_profile_id": "string",                      * "message": "string",                      * "app_version_number": "string",                      * "platform_version_number": "string",                      * "error": {                          * "cause": "string",                              * "column_number": 0,                              * "file_name": "string",                              * "line_number": 0,                              * "message": "string",                              * "message_detail": "string",                              * "name": "string",                              * "number": 0,                              * "stack_trace": "string"                                           },                      * "request": {                          * "method": "GET",                              * "host": "string",                              * "path": "string",                              * "request_headers": {                                  * "property1": "string",                                      * "property2": "string"                                                       },                              * "response_headers": {                                  * "property1": "string",                                      * "property2": "string"                                                       },                              * "response_status_code": 0                                           }                               }                   ]       }`

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "message": "string"       }`

[](#operation/integrations/get_list)Get integration metadata list
-----------------------------------------------------------------

Get integration metadata list. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**default**

Unexpected error.

get/integrations

https://api.pinterest.com/v5/integrations

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "7329123456789012345",                      * "external_business_id": "1234567890",                      * "connected_merchant_id": "1234567890123",                      * "connected_user_id": "123456789012345678",                      * "connected_advertiser_id": "123456789012",                      * "connected_lba_id": "871234567890123456",                      * "connected_tag_id": "2412345678901",                      * "partner_access_token": "ABCLUOJS5XDMWDE",                      * "partner_refresh_token": "ABCLUOJS5XDMWDE",                      * "partner_primary_email": "partner@server.com",                      * "partner_access_token_expiry": 1621350033000,                      * "partner_refresh_token_expiry": 1621350033000,                      * "scopes": "accounts:read",                      * "partner_metadata": "",                      * "additional_id_1": "123456",                      * "created_time": 1621350033000,                      * "updated_time": 1621350033000                               }                   ],      * "bookmark": "string"       }`

[](#operation/integrations/get_by_id)Get integration metadata
-------------------------------------------------------------

Get integration metadata by ID. Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| id<br><br>required | string<br><br>Integration ID. |

### Responses

**200**

Success

**404**

Integration not found.

**default**

Unexpected error.

get/integrations/{id}

https://api.pinterest.com/v5/integrations/{id}

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "7329123456789012345",      * "external_business_id": "1234567890",      * "connected_merchant_id": "1234567890123",      * "connected_user_id": "123456789012345678",      * "connected_advertiser_id": "123456789012",      * "connected_lba_id": "871234567890123456",      * "connected_tag_id": "2412345678901",      * "partner_access_token": "ABCLUOJS5XDMWDE",      * "partner_refresh_token": "ABCLUOJS5XDMWDE",      * "partner_primary_email": "partner@server.com",      * "partner_access_token_expiry": 1621350033000,      * "partner_refresh_token_expiry": 1621350033000,      * "scopes": "accounts:read",      * "partner_metadata": "",      * "additional_id_1": "123456",      * "created_time": 1621350033000,      * "updated_time": 1621350033000       }`

[](#tag/keywords)keywords
=========================

View, create or update keywords.

[](#operation/keywords/get)Get keywords
---------------------------------------

Get a list of keywords based on the filters provided. If no filter is provided, it will default to the ad\_account\_id filter, which means it will only return keywords that specifically have parent\_id set to the ad\_account\_id. Note: Keywords can have ad\_account\_ids, campaign\_ids, and ad\_group\_ids set as their parent\_ids. Keywords created through Ads Manager will have their parent\_id set to an ad\_group\_id, not ad\_account\_id.

For more information, see [Keyword targeting](https://help.pinterest.com/en/business/article/keyword-targeting).

**Notes:**

* Advertisers and campaigns can only be assigned keywords with excluding ('\_NEGATIVE').
* All keyword match types are available for ad groups.

For more information on match types, see [match type enums](https://developers.pinterest.com/docs/ads/targeting/#Match%20type%20and%20targeting%20level).

**Returns:**

* A successful call returns an object containing an array of new keyword objects and an empty "errors" object array.
    
* An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the "errors" object array:
    
     { "keywords": \[\], "errors": \[ { "data": { "archived": null, "match\_type": "EXACT", "parent\_type": null, "value": "foobar", "parent\_id": null, "type": "keyword", "id": null }, "error\_messages": \[ "Advertisers and Campaigns only accept excluded targeting attributes." \] } } 
    

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| campaign\_id | string <= 18 characters ^\\d+$<br><br>Campaign Id to use to filter the results. |
| ad\_group\_id | string <= 18 characters ^\\d+$<br><br>Example: ad\_group\_id=123123123<br><br>Ad group Id. |
| match\_types | Array of strings (MatchType) \[ 1 .. 5 \] items<br><br>Items Enum: "BROAD" "PHRASE" "EXACT" "EXACT\_NEGATIVE" "PHRASE\_NEGATIVE"<br><br>Example: match\_types=BROAD<br><br>Keyword [match type](https://developers.pinterest.com/docs/ads/targeting/#Match%20type%20and%20targeting%20level) |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/keywords

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "archived": false,                      * "id": "383791336903426391",                      * "parent_id": "383791336903426391",                      * "parent_type": "campaign",                      * "type": "keyword",                      * "bid": 200000,                      * "match_type": "BROAD",                      * "value": "string"                               }                   ],      * "bookmark": "string"       }`

[](#operation/keywords/create)Create keywords
---------------------------------------------

Create keywords for following entity types(advertiser, campaign, ad group or ad).

For more information, see [Keyword targeting](https://help.pinterest.com/en/business/article/keyword-targeting).

**Notes:**

* Advertisers and campaigns can only be assigned keywords with excluding ('\_NEGATIVE').
* All keyword match types are available for ad groups.

For more information on match types, see [match type enums](https://developers.pinterest.com/docs/ads/targeting/#Match%20type%20and%20targeting%20level).

**Returns:**

* A successful call returns an object containing an array of new keyword objects and an empty "errors" object array.
    
* An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the "errors" object array:
    
     { "keywords": \[\], "errors": \[ { "data": { "archived": null, "match\_type": "EXACT", "parent\_type": null, "value": "foobar", "parent\_id": null, "type": "keyword", "id": null }, "error\_messages": \[ "Advertisers and Campaigns only accept excluded targeting attributes." \] } } 
    

**Rate limit**: [WRITE](https://developers.pinterest.com/docs/redoc/#tag/Rate-Limits).

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| keywords<br><br>required | Array of objects (KeywordsCommon)<br><br>Keyword JSON array. Each array element has 3 fields |
| parent\_id<br><br>required | string (parent\_id) ^((AG)\|C)?\\d+$<br><br>Keyword parent entity ID (advertiser, campaign, ad group). |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/keywords

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "keywords": [          * {                  * "bid": 200000,                      * "match_type": "BROAD",                      * "value": "string"                               }                   ],      * "parent_id": "383791336903426391"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "errors": [          * {                  * "data": {                          * "archived": false,                              * "id": "383791336903426391",                              * "parent_id": "383791336903426391",                              * "parent_type": "campaign",                              * "type": "keyword",                              * "bid": 200000,                              * "match_type": "BROAD",                              * "value": "string"                                           },                      * "error_messages": [                          * "string"                                           ]                               }                   ],      * "keywords": [          * {                  * "archived": false,                      * "id": "383791336903426391",                      * "parent_id": "383791336903426391",                      * "parent_type": "campaign",                      * "type": "keyword",                      * "bid": 200000,                      * "match_type": "BROAD",                      * "value": "string"                               }                   ]       }`

[](#operation/keywords/update)Update keywords
---------------------------------------------

Update one or more keywords' bid and archived fields.

Archiving a keyword effectively deletes it - keywords no longer receive metrics and no longer visible within the parent entity's keywords list.

ratelimit-category: ads\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| keywords<br><br>required | Array of objects (keywords)<br><br>Keywords to update. Object array. Each object has 3 possible fields:  <br>1\. "id": (required) keyword ID  <br>2\. "archived": boolean. Should keyword be archived?  <br>3\. "bid": number  <br>For example: \[{"id":"2886610576653", "archived": false, "bid": 20000}, {"id":"2886610576654", "archived": true, "bid": 20000}, ...\] |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/keywords

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "keywords": [          * {                  * "id": "2886364308355",                      * "archived": false,                      * "bid": 200000                               }                   ]       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "errors": [          * {                  * "data": {                          * "archived": false,                              * "id": "383791336903426391",                              * "parent_id": "383791336903426391",                              * "parent_type": "campaign",                              * "type": "keyword",                              * "bid": 200000,                              * "match_type": "BROAD",                              * "value": "string"                                           },                      * "error_messages": [                          * "string"                                           ]                               }                   ],      * "keywords": [          * {                  * "archived": false,                      * "id": "383791336903426391",                      * "parent_id": "383791336903426391",                      * "parent_type": "campaign",                      * "type": "keyword",                      * "bid": 200000,                      * "match_type": "BROAD",                      * "value": "string"                               }                   ]       }`

[](#operation/country_keywords_metrics/get)Get country's keyword metrics
------------------------------------------------------------------------

See keyword metrics for a specified country, aggregated across all of Pinterest. (Definitions are available from the "Get delivery metrics definitions" [API endpoint](https://developers.pinterest.com/docs/api/v5/#operation/delivery_metrics/get)).

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| country\_code<br><br>required | string<br><br>Example: country\_code=US<br><br>Two letter country code (ISO 3166-1 alpha-2) |
| keywords<br><br>required | Array of strings \[ 1 .. 2000 \] items<br><br>Comma-separated keywords |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/keywords/metrics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords/metrics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "data": [          * {                  * "keyword": "animals",                      * "metrics": {                          * "avg_cpc_in_micro_currency": 100000,                              * "keyword_query_volume": "5M+"                                           }                               }                   ]       }`

[](#operation/trending_keywords/list)List trending keywords
-----------------------------------------------------------

Get the top trending search keywords among the Pinterest user audience. This is an alpha endpoint only available to select participants.

Trending keywords can be used to inform ad targeting, budget strategy, and creative decisions about which products and Pins will resonate with your audience.

Geographic, demographic and interest-based filters are available to narrow down to the top trends among a specific audience. Multiple trend types are supported that can be used to identify newly-popular, evergreen or seasonal keywords.

For an interactive way to explore this data, please visit [trends.pinterest.com](https://trends.pinterest.com/).

ratelimit-category: trends\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| region<br><br>required | string (Region)<br><br>Enum: "US" "CA" "DE" "FR" "ES" "IT" "DE+AT+CH" "GB+IE" "IT+ES+PT+GR+MT" "PL+RO+HU+SK+CZ" "SE+DK+FI+NO" "NL+BE+LU" "AR" "BR" "CO" "MX" "MX+AR+CO+CL" "AU+NZ"<br><br>Example: GB+IE<br><br>The geographic region of interest. Only top trends within the specified region will be returned.  <br>The `region` parameter is formatted as ISO 3166-2 country codes delimited by `+`, corresponding to the following geographic areas:<br><br>* `US` - United States<br>* `CA` - Canada<br>* `DE` - Germany<br>* `FR` - France<br>* `ES` - Spain<br>* `IT` - Italy<br>* `DE+AT+CH` - Germanic countries<br>* `GB+IE` - Great Britain & Ireland<br>* `IT+ES+PT+GR+MT` - Southern Europe<br>* `PL+RO+HU+SK+CZ` - Eastern Europe<br>* `SE+DK+FI+NO` - Nordic countries<br>* `NL+BE+LU` - Benelux<br>* `AR` - Argentina<br>* `BR` - Brazil<br>* `CO` - Colombia<br>* `MX` - Mexico<br>* `MX+AR+CO+CL` - Hispanic LatAm<br>* `AU+NZ` - Australasia |
| trend\_type<br><br>required | string (TrendType)<br><br>Enum: "growing" "monthly" "yearly" "seasonal"<br><br>Example: monthly<br><br>The methodology used to rank how trendy a keyword is.<br><br>* `growing` trends have high upward growth in search volume over the last quarter<br>* `monthly` trends have high search volume in the last month<br>* `yearly` trends have high search volume in the last year<br>* `seasonal` trends have high upward growth in search volume over the last month and exhibit a seasonal recurring pattern (typically annual) |

##### query Parameters

|     |     |
| --- | --- |
| interests | Array of strings (Interest)<br><br>Items Enum: "animals" "architecture" "art" "beauty" "childrens\_fashion" "design" "diy\_and\_crafts" "education" "electronics" "entertainment" "event\_planning" "finance" "food\_and\_drinks" "gardening" "health" "home\_decor" "mens\_fashion" "parenting" "quotes" "sport" … 4 more<br><br>Example: interests=beauty&interests=womens\_fashion<br><br>If set, filters the results to trends associated with the specified interests.  <br>If unset, trends for all interests will be returned.  <br>The list of supported interests is:<br><br>* `animals` - Animals<br>* `architecture` - Architecture<br>* `art` - Art<br>* `beauty` - Beauty<br>* `childrens_fashion` - Children's Fashion<br>* `design` - Design<br>* `diy_and_crafts` - DIY & Crafts<br>* `education` - Education<br>* `electronics` - Electronics<br>* `entertainment` - Entertainment<br>* `event_planning` - Event Planning<br>* `finance` - Finance<br>* `food_and_drinks` - Food & Drink<br>* `gardening` - Gardening<br>* `health` - Health<br>* `home_decor` - Home Decor<br>* `mens_fashion` - Men's Fashion<br>* `parenting` - Parenting<br>* `quotes` - Quotes<br>* `sport` - Sports<br>* `travel` - Travel<br>* `vehicles` - Vehicles<br>* `wedding` - Wedding<br>* `womens_fashion` - Women's Fashion |
| genders | Array of strings (Gender)<br><br>Items Enum: "female" "male" "unknown"<br><br>Example: genders=female&genders=unknown<br><br>If set, filters the results to trends among users who identify with the specified gender(s).  <br>If unset, trends among all genders will be returned.  <br>The `unknown` group includes users with unspecified or customized gender profile settings. |
| ages | Array of strings (AgeRange)<br><br>Items Enum: "18-24" "25-34" "35-44" "45-49" "50-54" "55-64" "65+"<br><br>Example: ages=35-44&ages=50-54<br><br>If set, filters the results to trends among users in the specified age range(s).  <br>If unset, trends among all age groups will be returned. |
| normalize\_against\_group | boolean<br><br>Default: false<br><br>Example: normalize\_against\_group=true<br><br>Governs how the resulting time series data will be normalized to a \[0-100\] scale.  <br>By default (`false`), the data will be normalized independently for each keyword. The peak search volume observation in _each_ keyword's time series will be represented by the value 100. This is ideal for analyzing when an individual keyword is expected to peak in interest.  <br>If set to `true`, the data will be normalized as a group. The peak search volume observation across _all_ keywords in the response will be represented by the value 100, and all other values scaled accordingly. Use this option when you wish to compare relative search volume between multiple keywords. |
| limit | integer \[ 1 .. 50 \]<br><br>Default: 50<br><br>Example: limit=25<br><br>The maximum number of trending keywords that will be returned. Keywords are returned in trend-ranked order, so a `limit` of 50 will return the top 50 trends. |

### Responses

**200**

Success

**400**

Invalid trending keywords request parameters

**default**

Unexpected error

get/trends/keywords/{region}/top/{trend\_type}

https://api.pinterest.com/v5/trends/keywords/{region}/top/{trend\_type}

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "trends": [          * {                  * "keyword": "couples halloween costumes",                      * "pct_growth_wow": 50,                      * "pct_growth_mom": 400,                      * "pct_growth_yoy": -5,                      * "time_series": {                          * "2023-10-10": 31,                              * "2023-10-17": 54,                              * "2023-10-24": 77,                              * "2023-10-31": 100                                           }                               }                   ]       }`

[](#tag/lead_forms)lead\_forms
==============================

View lead forms.

[](#operation/lead_forms/list)Get lead forms
--------------------------------------------

Gets all Lead Forms associated with an ad account ID. Retrieving an advertiser's list of lead forms will only contain results if you're a part of the Lead ads beta. If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**400**

Invalid ad account lead forms parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/lead\_forms

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "name": "Lead Form 3/14/2023",                      * "privacy_policy_link": "[https://www.advertisername.com/privacy-policy](https://www.advertisername.com/privacy-policy)",                      * "has_accepted_terms": false,                      * "completion_message": "Thank you for submitting. We will contact you soon.",                      * "status": "DRAFT",                      * "disclosure_language": "By entering your personal information, you agree that your data will be collected and used.",                      * "questions": [                          * {                                  * "question_type": "CUSTOM",                                      * "custom_question_field_type": "CHECKBOX",                                      * "custom_question_label": "What is your favorite animal?",                                      * "custom_question_options": [                                          * "Dog",                                              * "Cat",                                              * "Bird",                                              * "Turtle"                                                                   ]                                                       }                                           ],                      * "id": "7765300871171",                      * "ad_account_id": "549755885175",                      * "created_time": 1451431341,                      * "updated_time": 1451431341                               }                   ],      * "bookmark": "string"       }`

[](#operation/lead_form/get)Get lead form by id
-----------------------------------------------

Gets a lead form given it's ID. It must also be associated with the provided ad account ID. Retrieving an advertiser's lead form will only contain results if you're a part of the Lead ads beta. If you're interested in joining the beta, please reach out to your Pinterest account manager.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| lead\_form\_id<br><br>required | string^\\d+$<br><br>Example: 1234567890123<br><br>Unique identifier of a lead form. |

### Responses

**200**

Success

**400**

Invalid ad account lead forms parameters.

**404**

The lead form ID for the given ad account ID does not exist.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}

### Response samples

* 200
* 400
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "name": "Lead Form 3/14/2023",      * "privacy_policy_link": "[https://www.advertisername.com/privacy-policy](https://www.advertisername.com/privacy-policy)",      * "has_accepted_terms": false,      * "completion_message": "Thank you for submitting. We will contact you soon.",      * "status": "DRAFT",      * "disclosure_language": "By entering your personal information, you agree that your data will be collected and used.",      * "questions": [          * {                  * "question_type": "CUSTOM",                      * "custom_question_field_type": "CHECKBOX",                      * "custom_question_label": "What is your favorite animal?",                      * "custom_question_options": [                          * "Dog",                              * "Cat",                              * "Bird",                              * "Turtle"                                           ]                               }                   ],      * "id": "7765300871171",      * "ad_account_id": "549755885175",      * "created_time": 1451431341,      * "updated_time": 1451431341       }`

[](#operation/lead_form_test/create)Create lead form test data
--------------------------------------------------------------

Create lead form test data based on the list of answers provided as part of the body.

* List of answers should follow the questions creation order.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| lead\_form\_id<br><br>required | string^\\d+$<br><br>Example: 1234567890123<br><br>Unique identifier of a lead form. |

##### Request Body schema: application/json

Subscription to create.

|     |     |
| --- | --- |
| answers<br><br>required | Array of strings<br><br>Test lead answers. Should follow the creation order. |

### Responses

**200**

Success

**400**

Invalid parameters.

**404**

Lead not found.

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}/test

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}/test

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "answers": [          * "John",              * "Doe",              * "abc@email.com",              * "987654321"                   ]       }`

### Response samples

* 200
* 400
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "subscription_id": "8078432025948590686"       }`

[](#tag/media)media
===================

Register and manage media uploads.

[](#operation/media/list)List media uploads
-------------------------------------------

List media uploads filtered by given parameters.

**[Learn more](https://developers.pinterest.com/docs/content/content-creation/#Creating%20video%20Pins)** about video Pin creation.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`pins:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

response

**default**

Unexpected error

get/media

https://api.pinterest.com/v5/media

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "media_id": "12345",                      * "media_type": "video",                      * "status": "succeeded"                               }                   ],      * "bookmark": "string"       }`

[](#operation/media/create)Register media upload
------------------------------------------------

Register your intent to upload media

The response includes all of the information needed to upload the media to Pinterest.

To upload the media, make an HTTP POST request (using curl, for example) to upload\_url using the Content-Type header value. Send the media file's contents as the request's file parameter and also include all of the parameters from upload\_parameters.

**[Learn more](https://developers.pinterest.com/docs/content/content-creation/#Creating%20video%20Pins)** about video Pin creation.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`pins:read``pins:write`)

##### Request Body schema: application/json

Create a media upload request

|     |     |
| --- | --- |
| media\_type<br><br>required | string<br><br>Value: "video" |

### Responses

**201**

response

**default**

Unexpected error

post/media

https://api.pinterest.com/v5/media

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "media_type": "video"       }`

### Response samples

* 201
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "media_id": "12345",      * "media_type": "video",      * "upload_url": "[https://pinterest-media-upload.s3-accelerate.amazonaws.com/](https://pinterest-media-upload.s3-accelerate.amazonaws.com/)",      * "upload_parameters": {          * "x-amz-data": "20220127T185143Z",              * "x-amz-signature": "fcd6309a6aaee213348666a72abed8b44552a43acb6b340e8e1b288d21a5fe92",              * "key": "uploads/11/aa/22/3:video:203014033110991560:5212123920968240771",              * "policy": "eyJleHBpcmF0aW9uIjoiMj..==",              * "x-amz-credential": "ASIA6QZJ64OPIKV7FRVX/20220127/us-east-1/s3/aws4_request",              * "x-amz-security-token": "IQoJb3JpZ2luX2VjEJr...==",              * "x-amz-algorithm": "AWS4-HMAC-SHA256",              * "Content-Type": "multipart/form-data"                   }       }`

[](#operation/media/get)Get media upload details
------------------------------------------------

Get details for a registered media upload, including its current status.

**[Learn more](https://developers.pinterest.com/docs/content/content-creation/#Creating%20video%20Pins)** about video Pin creation.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| media\_id<br><br>required | string^\\d+$<br><br>Media identifier |

### Responses

**200**

response

**404**

Media upload not found

**default**

Unexpected error

get/media/{media\_id}

https://api.pinterest.com/v5/media/{media\_id}

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "media_id": "12345",      * "media_type": "video",      * "status": "succeeded"       }`

[](#tag/oauth)oauth
===================

Generate and refresh OAuth access tokens.

[](#operation/oauth/token)Generate OAuth access token
-----------------------------------------------------

Generate an OAuth access token by using an authorization code or a refresh token.

IMPORTANT: You need to start the OAuth flow via [www.pinterest.com/oauth](http://www.pinterest.com/oauth) before calling this endpoint (or have an existing refresh token).

See [Authentication](https://developers.pinterest.com/docs/getting-started/authentication/) for more.

**Parameter _refresh\_on_ and its corresponding response type _everlasting\_refresh_ are currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[basic](#section/Authentication/basic)

##### Request Body schema: application/x-www-form-urlencoded

Generate an OAuth access token.

|     |     |
| --- | --- |
| grant\_type<br><br>required | string<br><br>authorization\_code<br><br>authorization\_code<br><br>refresh\_token |
| code<br><br>required | string |
| redirect\_uri<br><br>required | string |

### Responses

**200**

response

**default**

Unexpected error

post/oauth/token

https://api.pinterest.com/v5/oauth/token

### Response samples

* 200
* default

Content type

application/json

Example

authorization\_code

authorization\_code

refresh\_token

integration\_refresh

everlasting\_refresh

Copy

Expand all Collapse all

`{  * "response_type": "authorization_code",      * "access_token": "string",      * "token_type": "bearer",      * "expires_in": 0,      * "scope": "string",      * "refresh_token": "string",      * "refresh_token_expires_in": 0       }`

[](#tag/order_lines)order\_lines
================================

View order lines.

[](#operation/order_lines/list)Get order lines
----------------------------------------------

List existing order lines associated with an ad account.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/order\_lines

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/order\_lines

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "2680059592705",                      * "type": "orderline",                      * "ad_account_id": "549755885175",                      * "purchase_order_id": "PO12345",                      * "start_time": 1452208622,                      * "end_time": 1461269616,                      * "budget": 5000000,                      * "paid_budget": 5000000,                      * "status": "ACTIVE",                      * "name": "Order Line Name 1",                      * "paid_type": "PAID",                      * "campaign_ids": [                          * "626735565838"                                           ]                               }                   ],      * "bookmark": "string"       }`

[](#operation/order_lines/get)Get order line
--------------------------------------------

Get a specific existing order line associated with an ad account.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| order\_line\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an order line. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/order\_lines/{order\_line\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/order\_lines/{order\_line\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "2680059592705",      * "type": "orderline",      * "ad_account_id": "549755885175",      * "purchase_order_id": "PO12345",      * "start_time": 1452208622,      * "end_time": 1461269616,      * "budget": 5000000,      * "paid_budget": 5000000,      * "status": "ACTIVE",      * "name": "Order Line Name 1",      * "paid_type": "PAID",      * "campaign_ids": [          * "626735565838"                   ]       }`

[](#tag/pins)pins
=================

View, create, update, or delete information about Pins.

[](#operation/pins/list)List Pins
---------------------------------

Get a list of the Pins owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.
* All Pins owned by the "operation user\_account" are included, regardless of who owns the board they are on. Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| pin\_filter | string<br><br>Enum: "exclude\_native" "exclude\_repins" "has\_been\_promoted"<br><br>Pin filter. |
| include\_protected\_pins | boolean<br><br>Default: false<br><br>Specify if return pins from protected boards |
| pin\_type | string<br><br>Value: "PRIVATE"<br><br>The type of pins to return, currently only enabled for private pins |
| creative\_types | Array of strings<br><br>Items Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"<br><br>Example: creative\_types=REGULAR<br><br>Pin creative types filter.<br><br>**Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| pin\_metrics | boolean<br><br>Default: false<br><br>Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. |

### Responses

**200**

Success

**400**

Invalid pin filter value

**default**

Unexpected error

get/pins

https://api.pinterest.com/v5/pins

### Request samples

* curl
* curl (Sandbox)

Copy

curl \--location \--request GET 'https://api.pinterest.com/v5/pins' \\
\--header 'Authorization: Bearer <Add your token here>' \\
\--header 'Content-Type: application/json'

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "813744226420795884",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                      * "title": "string",                      * "description": "string",                      * "dominant_color": "#6E7874",                      * "alt_text": "string",                      * "creative_type": "REGULAR",                      * "board_id": "string",                      * "board_section_id": "string",                      * "board_owner": {                          * "username": "string"                                           },                      * "is_owner": true,                      * "media": {                          * "media_type": "string"                                           },                      * "parent_pin_id": "string",                      * "is_standard": true,                      * "has_been_promoted": true,                      * "note": "string",                      * "pin_metrics": {                          * "pin_metrics": [                                  * {                                          * "90d": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3                                                                               },                                              * "all_time": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3,                                                      * "reaction": 10,                                                      * "comment": 2                                                                               }                                                                   },                                      * null                                                       ]                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/pins/create)Create Pin
------------------------------------

Create a Pin on a board or board section owned by the "operation user\_account".

Note: If the current "operation user\_account" (defined by the access token) has access to another user's Ad Accounts via Pinterest Business Access, you can modify your request to make use of the current operation\_user\_account's permissions to those Ad Accounts by including the ad\_account\_id in the path parameters for the request (e.g. .../?ad\_account\_id=12345&...).

* This function is intended solely for publishing new content created by the user. If you are interested in saving content created by others to your Pinterest boards, sometimes called 'curated content', please use our [Save button](https://developers.pinterest.com/docs/add-ons/save-button) instead. For more tips on creating fresh content for Pinterest, review our [Content App Solutions Guide](https://developers.pinterest.com/docs/content/content-creation/).

**[Learn more](https://developers.pinterest.com/docs/content/content-creation/#Creating%20video%20Pins)** about video Pin creation.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write``pins:read``pins:write`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Create a new Pin.

|     |     |
| --- | --- |
| link | string <= 2048 characters Nullable |
| title | string <= 100 characters Nullable |
| description | string <= 800 characters Nullable |
| dominant\_color | string Nullable<br><br>Dominant pin color. Hex number, e.g. "#6E7874". |
| alt\_text | string <= 500 characters Nullable |
| board\_id | string^\\d+$<br><br>The board to which this Pin belongs. |
| board\_section\_id | string Nullable ^\\d+$<br><br>The board section to which this Pin belongs. |
| media\_source | object<br><br>Pin media source. |
| parent\_pin\_id | string Nullable ^\\d+$<br><br>The source pin id if this pin was saved from another pin. [Learn more](https://help.pinterest.com/article/save-pins-on-pinterest). |
| note | string Nullable<br><br>Private note for this Pin. [Learn more](https://help.pinterest.com/en/article/add-notes-to-your-pins). |

### Responses

**201**

Successful pin creation.

**400**

Invalid Pin parameters response

**403**

The Pin's image is too small, too large or is broken

**404**

Board or section not found

**429**

This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window.

**default**

Unexpected error

post/pins

https://api.pinterest.com/v5/pins

### Request samples

* Payload
* Python SDK
* curl
* curl (Sandbox)

Content type

application/json

Copy

Expand all Collapse all

`{  * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "description": "string",      * "dominant_color": "#6E7874",      * "alt_text": "string",      * "board_id": "string",      * "board_section_id": "string",      * "media_source": {          * "source_type": "image_base64",              * "content_type": "image/jpeg",              * "data": "string",              * "is_standard": true                   },      * "parent_pin_id": "string",      * "note": "string"       }`

### Response samples

* 201
* 400
* 403
* 404
* 429
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "813744226420795884",      * "created_at": "2020-01-01T20:10:40-00:00",      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "description": "string",      * "dominant_color": "#6E7874",      * "alt_text": "string",      * "creative_type": "REGULAR",      * "board_id": "string",      * "board_section_id": "string",      * "board_owner": {          * "username": "string"                   },      * "is_owner": true,      * "media": {          * "media_type": "string"                   },      * "parent_pin_id": "string",      * "is_standard": true,      * "has_been_promoted": true,      * "note": "string",      * "pin_metrics": {          * "pin_metrics": [                  * {                          * "90d": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3                                                       },                              * "all_time": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3,                                      * "reaction": 10,                                      * "comment": 2                                                       }                                           },                      * null                               ]                   }       }`

[](#operation/pins/get)Get Pin
------------------------------

Get a Pin owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| pin\_id<br><br>required | string<br><br>Unique identifier of a Pin. |

##### query Parameters

|     |     |
| --- | --- |
| pin\_metrics | boolean<br><br>Default: false<br><br>Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

response

**403**

Not authorized to access board or Pin.

**404**

Pin not found.

**default**

Unexpected error

get/pins/{pin\_id}

https://api.pinterest.com/v5/pins/{pin\_id}

### Request samples

* Python SDK
* curl
* curl (Sandbox)

Copy

\# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started

from pinterest.organic.pins import Pin
\# Pin information can be fetched from profile page or from list pin method here:
\# https://developers.pinterest.com/docs/api/v5/#operation/pins/list
PIN\_ID\="<Add your pin id here>"

pin\_get \= Pin(pin\_id\=PIN\_ID)
print("Pin Id: %s, Pin Title:%s" %(pin\_get.id, pin\_get.title))

### Response samples

* 200
* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "813744226420795884",      * "created_at": "2020-01-01T20:10:40-00:00",      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "description": "string",      * "dominant_color": "#6E7874",      * "alt_text": "string",      * "creative_type": "REGULAR",      * "board_id": "string",      * "board_section_id": "string",      * "board_owner": {          * "username": "string"                   },      * "is_owner": true,      * "media": {          * "media_type": "string"                   },      * "parent_pin_id": "string",      * "is_standard": true,      * "has_been_promoted": true,      * "note": "string",      * "pin_metrics": {          * "pin_metrics": [                  * {                          * "90d": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3                                                       },                              * "all_time": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3,                                      * "reaction": 10,                                      * "comment": 2                                                       }                                           },                      * null                               ]                   }       }`

[](#operation/pins/delete)Delete Pin
------------------------------------

Delete a Pins owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write``pins:read``pins:write`)

##### path Parameters

|     |     |
| --- | --- |
| pin\_id<br><br>required | string<br><br>Unique identifier of a Pin. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**204**

Successfully deleted Pin

**403**

Not authorized to access board or Pin.

**404**

Pin not found.

**default**

Unexpected error

delete/pins/{pin\_id}

https://api.pinterest.com/v5/pins/{pin\_id}

### Request samples

* Python SDK
* curl
* curl (Sandbox)

Copy

\# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started

from pinterest.organic.pins import Pin
\# Pin information can be fetched from profile page or from create/list pin method here:
\# https://developers.pinterest.com/docs/api/v5/#operation/pins/list
PIN\_ID\="<Add your pin id here>"

pin\_delete\=Pin.delete(pin\_id\=PIN\_ID)

print("Pin was deleted? %s" % (pin\_delete))

### Response samples

* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 403,      * "message": "Not authorized to access board or Pin."       }`

[](#operation/pins/update)Update Pin
------------------------------------

Update a pin owned by the "operating user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write``pins:read``pins:write`)

##### path Parameters

|     |     |
| --- | --- |
| pin\_id<br><br>required | string<br><br>Unique identifier of a Pin. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

|     |     |
| --- | --- |
| alt\_text | string <= 500 characters Nullable<br><br>Pin's alternative text. |
| board\_id | string Nullable ^\\d+$<br><br>The id of the board to move the Pin onto. |
| board\_section\_id | string Nullable ^\\d+$<br><br>[Board section](https://help.pinterest.com/en/article/create-a-board-section) ID. |
| description | string <= 800 characters Nullable<br><br>Pin description - 800 characters maximum. |
| link | string <= 2048 characters Nullable<br><br>URL viewer is taken to when they click pin. |
| title | string <= 100 characters Nullable<br><br>The native pin title that creators explicitly prefer to display. |
| carousel\_slots | Array of objects<br><br>Carousel Pin slots data. |
| note | string Nullable<br><br>Private note for this Pin. [Learn more](https://help.pinterest.com/en/article/add-notes-to-your-pins). |

### Responses

**200**

response

**403**

Not authorized to update Pin.

**404**

Pin not found.

**429**

This request exceeded a rate limit. This can happen if the client exceeds one of the published rate limits or if multiple write operations are applied to an object within a short time window.

**default**

Unexpected error

patch/pins/{pin\_id}

https://api.pinterest.com/v5/pins/{pin\_id}

### Request samples

* Payload
* curl
* curl (Sandbox)

Content type

application/json

Copy

Expand all Collapse all

`{  * "alt_text": "string",      * "board_id": "string",      * "board_section_id": "string",      * "description": "string",      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "carousel_slots": [          * {                  * "title": "string",                      * "description": "string",                      * "link": "string"                               }                   ],      * "note": "string"       }`

### Response samples

* 200
* 403
* 404
* 429
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "813744226420795884",      * "created_at": "2020-01-01T20:10:40-00:00",      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "description": "string",      * "dominant_color": "#6E7874",      * "alt_text": "string",      * "creative_type": "REGULAR",      * "board_id": "string",      * "board_section_id": "string",      * "board_owner": {          * "username": "string"                   },      * "is_owner": true,      * "media": {          * "media_type": "string"                   },      * "parent_pin_id": "string",      * "is_standard": true,      * "has_been_promoted": true,      * "note": "string",      * "pin_metrics": {          * "pin_metrics": [                  * {                          * "90d": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3                                                       },                              * "all_time": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3,                                      * "reaction": 10,                                      * "comment": 2                                                       }                                           },                      * null                               ]                   }       }`

[](#operation/pins/analytics)Get Pin analytics
----------------------------------------------

Get analytics for a Pin owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account:

* For Pins on public or protected boards: Admin, Analyst.
* For Pins on secret boards: Admin.

If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then.

ratelimit-category: org\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### path Parameters

|     |     |
| --- | --- |
| pin\_id<br><br>required | string<br><br>Unique identifier of a Pin. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| app\_types | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "MOBILE" "TABLET" "WEB"<br><br>Apps or devices to get data for, default is all. |
| metric\_types<br><br>required | Array of strings or strings<br><br>Pin metric types to get data for, default is all. |
| split\_field | string<br><br>Default: "NO\_SPLIT"<br><br>Enum: "NO\_SPLIT" "APP\_TYPE"<br><br>How to split the data into groups. Not including this param means data won't be split. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

response

**400**

Invalid pins analytics parameters.

**403**

Not authorized to access board or Pin.

**404**

Pin not found.

**default**

Unexpected error

get/pins/{pin\_id}/analytics

https://api.pinterest.com/v5/pins/{pin\_id}/analytics

### Response samples

* 200
* 400
* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "property1": {          * "lifetime_metrics": {                  * "TOTAL_COMMENTS": 10,                      * "TOTAL_REACTIONS": 12                               },              * "daily_metrics": [                  * {                          * "data_status": "READY",                              * "date": "2019-12-01",                              * "metrics": {                                  * "IMPRESSION": 240,                                      * "OUTBOUND_CLICK": 20,                                      * "PIN_CLICK": 37,                                      * "QUARTILE_95_PERCENT_VIEW": 8,                                      * "SAVE": 20,                                      * "SAVE_RATE": 0.18,                                      * "VIDEO_10S_VIEW": 2,                                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                                      * "VIDEO_MRC_VIEW": 20,                                      * "VIDEO_START": 29,                                      * "VIDEO_V50_WATCH_TIME": 10031                                                       }                                           }                               ],              * "summary_metrics": {                  * "IMPRESSION": 240,                      * "OUTBOUND_CLICK": 20,                      * "PIN_CLICK": 37,                      * "QUARTILE_95_PERCENT_VIEW": 8,                      * "SAVE": 20,                      * "SAVE_RATE": 0.18,                      * "VIDEO_10S_VIEW": 2,                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                      * "VIDEO_MRC_VIEW": 20,                      * "VIDEO_START": 29,                      * "VIDEO_V50_WATCH_TIME": 10031                               }                   },      * "property2": {          * "lifetime_metrics": {                  * "TOTAL_COMMENTS": 10,                      * "TOTAL_REACTIONS": 12                               },              * "daily_metrics": [                  * {                          * "data_status": "READY",                              * "date": "2019-12-01",                              * "metrics": {                                  * "IMPRESSION": 240,                                      * "OUTBOUND_CLICK": 20,                                      * "PIN_CLICK": 37,                                      * "QUARTILE_95_PERCENT_VIEW": 8,                                      * "SAVE": 20,                                      * "SAVE_RATE": 0.18,                                      * "VIDEO_10S_VIEW": 2,                                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                                      * "VIDEO_MRC_VIEW": 20,                                      * "VIDEO_START": 29,                                      * "VIDEO_V50_WATCH_TIME": 10031                                                       }                                           }                               ],              * "summary_metrics": {                  * "IMPRESSION": 240,                      * "OUTBOUND_CLICK": 20,                      * "PIN_CLICK": 37,                      * "QUARTILE_95_PERCENT_VIEW": 8,                      * "SAVE": 20,                      * "SAVE_RATE": 0.18,                      * "VIDEO_10S_VIEW": 2,                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                      * "VIDEO_MRC_VIEW": 20,                      * "VIDEO_START": 29,                      * "VIDEO_V50_WATCH_TIME": 10031                               }                   }       }`

[](#operation/pins/save)Save Pin
--------------------------------

Save a Pin on a board or board section owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account. Optional: Business Access: Specify an `ad_account_id` (obtained via [List ad accounts](https://developers.pinterest.com/docs/api/v5/#operation/ad_accounts/list)) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts) roles on the ad\_account:
    
* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
    
* For Pins on secret boards: Owner, Admin.
    
* Any Pin type can be saved: image Pin, video Pin, Idea Pin, product Pin, etc.
    
* Any public Pin can be saved given a pin ID.
    

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:write``pins:read``pins:write`)

##### path Parameters

|     |     |
| --- | --- |
| pin\_id<br><br>required | string<br><br>Unique identifier of a Pin. |

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Request object used to save an existing pin

|     |     |
| --- | --- |
| board\_id | string Nullable ^\\d+$<br><br>Unique identifier of the board to which the pin will be saved. |
| board\_section\_id | string Nullable ^\\d+$<br><br>Unique identifier of the board section to which the pin will be saved. |

### Responses

**201**

Successfully saved pin.

**403**

Not authorized to access Board or Pin.

**404**

Board or Pin not found.

**default**

Unexpected error

post/pins/{pin\_id}/save

https://api.pinterest.com/v5/pins/{pin\_id}/save

### Request samples

* Payload
* Python SDK
* curl
* curl (Sandbox)

Content type

application/json

Copy

Expand all Collapse all

`{  * "board_id": "string",      * "board_section_id": "string"       }`

### Response samples

* 201
* 403
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "813744226420795884",      * "created_at": "2020-01-01T20:10:40-00:00",      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",      * "title": "string",      * "description": "string",      * "dominant_color": "#6E7874",      * "alt_text": "string",      * "creative_type": "REGULAR",      * "board_id": "string",      * "board_section_id": "string",      * "board_owner": {          * "username": "string"                   },      * "is_owner": true,      * "media": {          * "media_type": "string"                   },      * "parent_pin_id": "string",      * "is_standard": true,      * "has_been_promoted": true,      * "note": "string",      * "pin_metrics": {          * "pin_metrics": [                  * {                          * "90d": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3                                                       },                              * "all_time": {                                  * "pin_click": 7,                                      * "impression": 2,                                      * "clickthrough": 3,                                      * "reaction": 10,                                      * "comment": 2                                                       }                                           },                      * null                               ]                   }       }`

[](#tag/product_group_promotions)product\_group\_promotions
===========================================================

View, create, update, or delete information about promoted product groups.

[](#operation/product_group_promotions/create)Create product group promotions
-----------------------------------------------------------------------------

Add one or more product groups from your catalog to an existing ad group. (Product groups added to an ad group are a 'product group promotion.')

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

List of Product Group Promotions to create, size limit \[1, 30\].

|     |     |
| --- | --- |
| ad\_group\_id<br><br>required | string (ad\_group\_id) ^(AG)?\\d+$<br><br>ID of the Ad Group the Product Group Promotion belongs to. |
| product\_group\_promotion<br><br>required | Array of objects (product\_group\_promotion) |

### Responses

**200**

Success

**default**

Unexpected error

post/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "product_group_promotion": [          * {                  * "slideshow_collections_description": "Description",                      * "creative_type": "REGULAR",                      * "collections_hero_pin_id": "123123",                      * "catalog_product_group_name": "catalogProductGroupName",                      * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                      * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                      * "slideshow_collections_title": "Title",                      * "is_mdl": true,                      * "status": "ACTIVE"                               },              * {                  * "slideshow_collections_description": "Description",                      * "creative_type": "REGULAR",                      * "collections_hero_pin_id": "123123",                      * "catalog_product_group_name": "catalogProductGroupName",                      * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                      * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                      * "slideshow_collections_title": "Title",                      * "is_mdl": true,                      * "status": "ACTIVE"                               }                   ],      * "ad_group_id": "2680059592705"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "id": "2680059592705",                              * "ad_group_id": "2680059592705",                              * "bid_in_micro_currency": 14000000,                              * "included": true,                              * "definition": "*/product_type_0='kitchen'/product_type_1='beverage appliances'",                              * "relative_definition": "product_type_1='beverage appliances'",                              * "parent_id": "1231234",                              * "slideshow_collections_title": "slideshow title",                              * "slideshow_collections_description": "slideshow description",                              * "is_mdl": true,                              * "status": "ACTIVE",                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                              * "catalog_product_group_id": "1231235",                              * "catalog_product_group_name": "catalogProductGroupName",                              * "creative_type": "REGULAR",                              * "collections_hero_pin_id": "123123",                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)"                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/product_group_promotions/update)Update product group promotions
-----------------------------------------------------------------------------

Update multiple existing Product Group Promotions (by product\_group\_id)

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### Request Body schema: application/json

Parameters to update Product group promotions

|     |     |
| --- | --- |
| ad\_group\_id<br><br>required | string (ad\_group\_id) ^(AG)?\\d+$<br><br>ID of the ad group the product group belongs to. |
| product\_group\_promotion<br><br>required | Array of objects (product\_group\_promotion) |

### Responses

**200**

Success

**default**

Unexpected error

patch/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "product_group_promotion": [          * {                  * "catalog_product_group_id": "1234123",                      * "slideshow_collections_description": "Description",                      * "creative_type": "REGULAR",                      * "collections_hero_pin_id": "123123",                      * "catalog_product_group_name": "ProductGroupName",                      * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                      * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                      * "slideshow_collections_title": "Title",                      * "status": "ACTIVE",                      * "id": "2680059592705"                               },              * {                  * "catalog_product_group_id": "1231231",                      * "slideshow_collections_description": "Other description",                      * "creative_type": "REGULAR",                      * "collections_hero_pin_id": "123124",                      * "catalog_product_group_name": "ProductGroupName",                      * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)",                      * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                      * "slideshow_collections_title": "Title",                      * "status": "ACTIVE",                      * "id": "2680059592706"                               }                   ],      * "ad_group_id": "26823439592705"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "id": "2680059592705",                              * "ad_group_id": "2680059592705",                              * "bid_in_micro_currency": 14000000,                              * "included": true,                              * "definition": "*/product_type_0='kitchen'/product_type_1='beverage appliances'",                              * "relative_definition": "product_type_1='beverage appliances'",                              * "parent_id": "1231234",                              * "slideshow_collections_title": "slideshow title",                              * "slideshow_collections_description": "slideshow description",                              * "is_mdl": true,                              * "status": "ACTIVE",                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                              * "catalog_product_group_id": "1231235",                              * "catalog_product_group_name": "catalogProductGroupName",                              * "creative_type": "REGULAR",                              * "collections_hero_pin_id": "123123",                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)"                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/product_group_promotions/list)Get product group promotions
------------------------------------------------------------------------

List existing product group promotions associated with an ad account.

Include either ad\_group\_id or product\_group\_promotion\_ids in your request.

**Note:** ad\_group\_ids and product\_group\_promotion\_ids are mutually exclusive parameters. Only provide one. If multiple options are provided, product\_group\_promotion\_ids takes precedence over ad\_group\_ids. If none are provided, the endpoint returns an error.

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| product\_group\_promotion\_ids | Array of strings \[ 1 .. 100 \] items<br><br>List of Product group promotion Ids. |
| entity\_statuses | Array of strings<br><br>Default: \["ACTIVE","PAUSED"\]<br><br>Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"<br><br>Example: entity\_statuses=ACTIVE<br><br>Entity status |
| ad\_group\_id | string <= 18 characters ^\\d+$<br><br>Example: ad\_group\_id=123123123<br><br>Ad group Id. |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| order | string<br><br>Enum: "ASCENDING" "DESCENDING"<br><br>Example: order=ASCENDING<br><br>The order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID. Note that higher-value IDs are associated with more-recently added items. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "id": "2680059592705",                              * "ad_group_id": "2680059592705",                              * "bid_in_micro_currency": 14000000,                              * "included": true,                              * "definition": "*/product_type_0='kitchen'/product_type_1='beverage appliances'",                              * "relative_definition": "product_type_1='beverage appliances'",                              * "parent_id": "1231234",                              * "slideshow_collections_title": "slideshow title",                              * "slideshow_collections_description": "slideshow description",                              * "is_mdl": true,                              * "status": "ACTIVE",                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                              * "catalog_product_group_id": "1231235",                              * "catalog_product_group_name": "catalogProductGroupName",                              * "creative_type": "REGULAR",                              * "collections_hero_pin_id": "123123",                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)"                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ],      * "bookmark": "string"       }`

[](#operation/product_group_promotions/get)Get a product group promotion by id
------------------------------------------------------------------------------

Get a product group promotion by id

ratelimit-category: ads\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| product\_group\_promotion\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of a product group promotion |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_group\_promotions/{product\_group\_promotion\_id}

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions/{product\_group\_promotion\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "data": {                          * "id": "2680059592705",                              * "ad_group_id": "2680059592705",                              * "bid_in_micro_currency": 14000000,                              * "included": true,                              * "definition": "*/product_type_0='kitchen'/product_type_1='beverage appliances'",                              * "relative_definition": "product_type_1='beverage appliances'",                              * "parent_id": "1231234",                              * "slideshow_collections_title": "slideshow title",                              * "slideshow_collections_description": "slideshow description",                              * "is_mdl": true,                              * "status": "ACTIVE",                              * "tracking_url": "[https://www.pinterest.com](https://www.pinterest.com/)",                              * "catalog_product_group_id": "1231235",                              * "catalog_product_group_name": "catalogProductGroupName",                              * "creative_type": "REGULAR",                              * "collections_hero_pin_id": "123123",                              * "collections_hero_destination_url": "[http://www.pinterest.com](http://www.pinterest.com/)"                                           },                      * "exceptions": [                          * {                                  * "code": 2,                                      * "message": "Advertiser not found."                                                       }                                           ]                               }                   ]       }`

[](#operation/product_groups/analytics)Get product group analytics
------------------------------------------------------------------

Get analytics for the specified product groups in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via [Business Access](https://help.pinterest.com/en/business/article/share-and-manage-access-to-your-ad-accounts): Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

ratelimit-category: ads\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| product\_group\_ids<br><br>required | Array of strings \[ 1 .. 100 \] items<br><br>List of Product group Ids to use to filter the results. |
| columns<br><br>required | Array of strings<br><br>Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more<br><br>Example: columns=TOTAL\_CONVERSIONS<br><br>Columns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.  <br>For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).  <br>If a column has no value, it may not be returned |
| granularity<br><br>required | string (Granularity)<br><br>Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"<br><br>Example: granularity=DAY<br><br>TOTAL - metrics are aggregated over the specified date range.  <br>DAY - metrics are broken down daily.  <br>HOUR - metrics are broken down hourly.  <br>WEEKLY - metrics are broken down weekly.  <br>MONTHLY - metrics are broken down monthly |
| click\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Example: click\_window\_days=1<br><br>Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| engagement\_window\_days | integer<br><br>Default: 30<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days. |
| view\_window\_days | integer<br><br>Default: 1<br><br>Enum: 0 1 7 14 30 60<br><br>Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day. |
| conversion\_report\_time | string<br><br>Default: "TIME\_OF\_AD\_ACTION"<br><br>Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"<br><br>Example: conversion\_report\_time=TIME\_OF\_AD\_ACTION<br><br>The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event. |

### Responses

**200**

Success

**400**

Invalid ad account ads analytics parameters.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_groups/analytics

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_groups/analytics

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "DATE": "2021-04-01",              * "PRODUCT_GROUP_ID": "74629351736530",              * "SPEND_IN_DOLLAR": 30,              * "TOTAL_CLICKTHROUGH": 216                   }       ]`

[](#tag/product_groups)product\_groups
======================================

View, create, update, or delete information about product groups.

[](#operation/ad_accounts_catalogs_product_groups/list)Get catalog product groups Deprecated
--------------------------------------------------------------------------------------------

This endpoint is completely deprecated. Please use [List product groups](https://developers.pinterest.com/docs/api/v5/#operation/catalogs_product_groups/list) from Catalogs API instead.

ratelimit-category: ads\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:write`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| feed\_profile\_id | string <= 18 characters ^\\d+$<br><br>The feed profile id whose catalog product groups we want to return. |

### Responses

**200**

Success

**400**

Invalid ad account ads parameters.

**401**

Access Denied. This can happen if account is not yet approved to operate as Merchant on Pinterest.

**404**

Merchant data not found.

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_groups/catalogs

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_groups/catalogs

### Response samples

* 200
* 400
* 401
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "2680059592705",                      * "merchant_id": "2680059592705",                      * "name": "Most Popular",                      * "filters": {                          * "1": [                                  * "123chars_title"                                                       ]                                           },                      * "filter_v2": {                          * "1": [                                  * "123chars_title"                                                       ]                                           },                      * "type": {                          * "id": "549755885175",                              * "created_at": "2020-01-01T20:10:40-00:00",                              * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",                              * "name": "Summer Recipes",                              * "description": "My favorite summer recipes",                              * "collaborator_count": 17,                              * "pin_count": 5,                              * "follower_count": 13,                              * "media": {                                  * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",                                      * "pin_thumbnail_urls": [                                          * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                                              * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                                              * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                                              * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                                                                   ]                                                       },                              * "owner": {                                  * "username": "string"                                                       },                              * "privacy": "PUBLIC"                                           },                      * "status": "ACTIVE",                      * "feed_profile_id": "string",                      * "created_at": 1621350033000,                      * "last_update": 1622742155000,                      * "product_count": 6,                      * "featured_position": 2                               }                   ],      * "bookmark": "string"       }`

[](#tag/resources)resources
===========================

View metadata about available metrics and targeting options in the Pinterest API.

[](#operation/ad_account_countries/get)Get ad accounts countries
----------------------------------------------------------------

Get Ad Accounts countries

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

### Responses

**200**

Success

**default**

Unexpected error

get/resources/ad\_account\_countries

https://api.pinterest.com/v5/resources/ad\_account\_countries

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "code": "US",                      * "currency": "Dollars",                      * "index": 1,                      * "name": "United States of America"                               }                   ]       }`

[](#operation/delivery_metrics/get)Get available metrics' definitions
---------------------------------------------------------------------

Get the definitions for ads and organic metrics available across both synchronous and asynchronous report endpoints. The `display_name` attribute will match how the metric is named in our native tools like Ads Manager. See [Organic Analytics](https://developers.pinterest.com/docs/content/analytics/) and [Ads Analytics](https://developers.pinterest.com/docs/ads/ad-analytics-reporting/) for more information.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read``pins:read``user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| report\_type | string<br><br>Enum: "SYNC" "ASYNC"<br><br>Report type. |

### Responses

**200**

Success

**default**

Unexpected error

get/resources/delivery\_metrics

https://api.pinterest.com/v5/resources/delivery\_metrics

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "name": "AD_GROUP_ID",                      * "category": "ADS",                      * "definition": "Unique ID for your ad group",                      * "display_name": "Ad group ID"                               }                   ]       }`

[](#operation/lead_form_questions/get)Get lead form questions
-------------------------------------------------------------

Get a list of all lead form question type names. Some questions might not be used.

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

### Responses

**200**

Success

**default**

Unexpected error

get/resources/lead\_form\_questions

https://api.pinterest.com/v5/resources/lead\_form\_questions

### Response samples

* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 0,      * "message": "string"       }`

[](#operation/metrics_ready_state/get)Get metrics ready state
-------------------------------------------------------------

Learn whether conversion or non-conversion metrics are finalized and ready to query.

ratelimit-category: ads\_analytics

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| date<br><br>required | string^(\\d{4})-(\\d{2})-(\\d{2})$<br><br>Example: date=2022-07-13<br><br>Analytics reports request date (UTC). Format: YYYY-MM-DD |

### Responses

**200**

Success

**default**

Unexpected error

get/resources/metrics\_ready\_state

https://api.pinterest.com/v5/resources/metrics\_ready\_state

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "conversion_metrics_ready": false,      * "non_conversion_metrics_ready": false       }`

[](#operation/interest_targeting_options/get)Get interest details
-----------------------------------------------------------------

Get details of a specific interest given interest ID.

Click [here](https://docs.google.com/spreadsheets/d/1HxL-0Z3p2fgxis9YBP2HWC3tvPrs1hAuHDRtH-NJTIM/edit#gid=118370875) for a spreadsheet listing interests and their IDs.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| interest\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an interest. |

### Responses

**200**

Success

**default**

Unexpected error

get/resources/targeting/interests/{interest\_id}

https://api.pinterest.com/v5/resources/targeting/interests/{interest\_id}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "945391946569",      * "name": "Dress",      * "child_interests": [          * "string"                   ],      * "level": 2       }`

[](#operation/targeting_options/get)Get targeting options
---------------------------------------------------------

You can use targeting values in ads placement to define your intended audience.

Targeting metrics are organized around targeting specifications.

For more information on ads targeting, see [Audience targeting](https://help.pinterest.com/en/business/article/audience-targeting).

**Sample return:**

 \[{"36313": "Australia: Moreton Bay - North", "124735": "Canada: North Battleford", "36109": "Australia: Murray", "36108": "Australia: Mid North Coast", "36101": "Australia: Capital Region", "811": "U.S.: Reno", "36103": "Australia: Central West", "36102": "Australia: Central Coast", "36105": "Australia: Far West and Orana", "36104": "Australia: Coffs Harbour - Grafton", "36107": "Australia: Illawarra", "36106": "Australia: Hunter Valley Exc Newcastle", "554017": "New Zealand: Wanganui", "554016": "New Zealand: Marlborough", "554015": "New Zealand: Gisborne", "554014": "New Zealand: Tararua", "554013": "New Zealand: Invercargill", "GR": "Greece", "554011": "New Zealand: Whangarei", "554010": "New Zealand: Far North", "717": "U.S.: Quincy-Hannibal-Keokuk", "716": "U.S.: Baton Rouge",...}\] 

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| targeting\_type<br><br>required | string (PublicTargetingType)<br><br>Enum: "APPTYPE" "GENDER" "LOCALE" "AGE\_BUCKET" "LOCATION" "GEO" "INTEREST" "KEYWORD" "AUDIENCE\_INCLUDE" "AUDIENCE\_EXCLUDE"<br><br>Example: APPTYPE<br><br>Public targeting type. |

##### query Parameters

|     |     |
| --- | --- |
| client\_id | string <= 18 characters ^\\d+$<br><br>Example: client\_id=1094834<br><br>Client ID. |
| oauth\_signature | string<br><br>Example: oauth\_signature=8209f<br><br>Oauth signature |
| timestamp | string\\d+<br><br>Example: timestamp=1618338184277<br><br>Timestamp |

### Responses

**200**

Success

**default**

Unexpected error

get/resources/targeting/{targeting\_type}

https://api.pinterest.com/v5/resources/targeting/{targeting\_type}

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "36313": "Australia: Moreton Bay - North",              * "124735": "Canada: North Battleford"                   }       ]`

[](#tag/search)search
=====================

Search for Pins and boards owned by the current user.

[](#operation/search_user_boards/get)Search user's boards
---------------------------------------------------------

Search for boards for the "operation user\_account". This includes boards of all board types.

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See [Understanding Business Access](https://developers.pinterest.com/docs/reference/business-access/) for more information.

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:read_secret`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| query | string<br><br>Search query. Can contain pin description keywords or comma-separated pin IDs. |

### Responses

**200**

response

**default**

Unexpected error

get/search/boards

https://api.pinterest.com/v5/search/boards

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "549755885175",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",                      * "name": "Summer Recipes",                      * "description": "My favorite summer recipes",                      * "collaborator_count": 17,                      * "pin_count": 5,                      * "follower_count": 13,                      * "media": {                          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",                              * "pin_thumbnail_urls": [                                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                                                       ]                                           },                      * "owner": {                          * "username": "string"                                           },                      * "privacy": "PUBLIC"                               }                   ],      * "bookmark": "string"       }`

[](#operation/search_user_pins/list)Search user's Pins
------------------------------------------------------

Search for pins for the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See [Understanding Business Access](https://developers.pinterest.com/docs/reference/business-access/) for more information.

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``boards:read_secret``pins:read``pins:read_secret`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |
| query<br><br>required | string<br><br>Example: query=Plants<br><br>Search query. Can contain pin description keywords or comma-separated pin IDs. |
| bookmark | string<br><br>Cursor used to fetch the next page of items |

### Responses

**200**

Success

**404**

User not found

**default**

Unexpected error

get/search/pins

https://api.pinterest.com/v5/search/pins

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "813744226420795884",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                      * "title": "string",                      * "description": "string",                      * "dominant_color": "#6E7874",                      * "alt_text": "string",                      * "creative_type": "REGULAR",                      * "board_id": "string",                      * "board_section_id": "string",                      * "board_owner": {                          * "username": "string"                                           },                      * "is_owner": true,                      * "media": {                          * "media_type": "string"                                           },                      * "parent_pin_id": "string",                      * "is_standard": true,                      * "has_been_promoted": true,                      * "note": "string",                      * "pin_metrics": {                          * "pin_metrics": [                                  * {                                          * "90d": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3                                                                               },                                              * "all_time": {                                                  * "pin_click": 7,                                                      * "impression": 2,                                                      * "clickthrough": 3,                                                      * "reaction": 10,                                                      * "comment": 2                                                                               }                                                                   },                                      * null                                                       ]                                           }                               }                   ],      * "bookmark": "string"       }`

[](#operation/search_partner_pins)Search pins by a given search term
--------------------------------------------------------------------

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

Get the top 10 Pins by a given search term.

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`boards:read``pins:read`)

##### query Parameters

|     |     |
| --- | --- |
| term<br><br>required | string<br><br>Search term to look up pins. |
| country\_code<br><br>required | string<br><br>Example: country\_code=US<br><br>Two letter country code (ISO 3166-1 alpha-2) |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| locale | string<br><br>Search locale. |
| limit | integer \[ 1 .. 50 \]<br><br>Default: 10<br><br>Example: limit=4<br><br>Max search result size |

### Responses

**200**

Success

**400**

Invalid pins

**default**

Unexpected error

get/search/partner/pins

https://api.pinterest.com/v5/search/partner/pins

### Request samples

* curl

Copy

curl \--location \--request GET 'https://api.pinterest.com/v5/search/partner/pins' \\
\--header 'Authorization: Bearer <Add your token here>' \\
\--header 'Content-Type: application/json'

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "media": {                          * "media_type": "string"                                           },                      * "alt_text": "string",                      * "link": "[https://www.pinterest.com/](https://www.pinterest.com/)",                      * "title": "string",                      * "description": "string"                               }                   ],      * "bookmark": "string"       }`

[](#tag/terms)terms
===================

View related and suggested terms for ads targeting.

[](#operation/terms_related/list)List related terms
---------------------------------------------------

Get a list of terms logically related to each input term.

Example: the term 'workout' would list related terms like 'one song workout', 'yoga workout', 'workout motivation', etc.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| terms<br><br>required | Array of strings<br><br>Example: terms=workout<br><br>List of input terms. |

### Responses

**200**

Success

**400**

Invalid terms related parameters.

**default**

Unexpected error

get/terms/related

https://api.pinterest.com/v5/terms/related

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "id": "clothes",      * "related_term_count": 2,      * "related_terms_list": [          * {                  * "term": "clothes",                      * "related_terms": [                          * "shoes",                              * "cute clothes"                                           ]                               }                   ]       }`

[](#operation/terms_suggested/list)List suggested terms
-------------------------------------------------------

Get popular search terms that begin with your input term.

Example: 'sport' would return popular terms like 'sports bar' and 'sportswear', but not 'motor sports' since the phrase does not begin with the given term.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### query Parameters

|     |     |
| --- | --- |
| term<br><br>required | string<br><br>Example: term=sports<br><br>Input term. |
| limit | integer \[ 1 .. 10 \]<br><br>Default: 4<br><br>Example: limit=4<br><br>Max suggested terms to return. |

### Responses

**200**

Success

**400**

Invalid terms suggested parameters.

**default**

Unexpected error

get/terms/suggested

https://api.pinterest.com/v5/terms/suggested

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * "string"       ]`

[](#tag/terms_of_service)terms\_of\_service
===========================================

View Advertising Terms Of Service.

[](#operation/terms_of_service/get)Get terms of service
-------------------------------------------------------

Get the text of the terms of service and see whether the advertiser has accepted the terms of service.

sandbox: enabled

ratelimit-category: ads\_read

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`ads:read`)

##### path Parameters

|     |     |
| --- | --- |
| ad\_account\_id<br><br>required | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

##### query Parameters

|     |     |
| --- | --- |
| include\_html | boolean<br><br>Default: false<br><br>Return HTML in TOS text. |
| tos\_type | string<br><br>Request type. |

### Responses

**200**

Success

**default**

Unexpected error

get/ad\_accounts/{ad\_account\_id}/terms\_of\_service

https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/terms\_of\_service

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "has_accepted": true,      * "html": "example test",      * "id": "2650449554526",      * "ad_account_id": "549755885175"       }`

[](#tag/user_account)user\_account
==================================

View user accounts associated with a given access token.

[](#operation/user_account/get)Get user account
-----------------------------------------------

Get account information for the "operation user\_account"

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See [Understanding Business Access](https://developers.pinterest.com/docs/reference/business-access/) for more information.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

response

**403**

Not authorized to access the user account.

**default**

Unexpected error

get/user\_account

https://api.pinterest.com/v5/user\_account

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "account_type": "PINNER",      * "id": "2783136121146311751",      * "profile_image": "string",      * "website_url": "string",      * "username": "string",      * "about": "string",      * "business_name": "string",      * "board_count": 14,      * "pin_count": 339,      * "follower_count": 10,      * "following_count": 347,      * "monthly_views": 163       }`

[](#operation/user_account/analytics)Get user account analytics
---------------------------------------------------------------

Get analytics for the "operation user\_account"

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

ratelimit-category: org\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| from\_claimed\_content | string<br><br>Default: "BOTH"<br><br>Enum: "OTHER" "CLAIMED" "BOTH"<br><br>Filter on Pins that match your claimed domain. |
| pin\_format | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"<br><br>Pin formats to get data for, default is all. |
| app\_types | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "MOBILE" "TABLET" "WEB"<br><br>Apps or devices to get data for, default is all. |
| content\_type | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "PAID" "ORGANIC"<br><br>Filter to paid or organic data. Default is all. |
| source | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"<br><br>Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts |
| metric\_types | Array of strings<br><br>Items Enum: "ENGAGEMENT" "ENGAGEMENT\_RATE" "IMPRESSION" "OUTBOUND\_CLICK" "OUTBOUND\_CLICK\_RATE" "PIN\_CLICK" "PIN\_CLICK\_RATE" "SAVE" "SAVE\_RATE"<br><br>Metric types to get data for, default is all. |
| split\_field | string<br><br>Default: "NO\_SPLIT"<br><br>Enum: "NO\_SPLIT" "APP\_TYPE" "OWNED\_CONTENT" "SOURCE" "PIN\_FORMAT"<br><br>How to split the data into groups. Not including this param means data won't be split. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid user accounts analytics parameters.

**403**

Not authorized to access the user account analytics.

**default**

Unexpected error

get/user\_account/analytics

https://api.pinterest.com/v5/user\_account/analytics

### Response samples

* 200
* 400
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "property1": {          * "summary_metrics": {                  * "CLOSEUP": 1,                      * "CLOSEUP_RATE": 0,                      * "ENGAGEMENT": 1,                      * "ENGAGEMENT_RATE": 0,                      * "IMPRESSION": 240,                      * "OUTBOUND_CLICK": 20,                      * "OUTBOUND_CLICK_RATE": 0.08,                      * "PIN_CLICK": 37,                      * "PIN_CLICK_RATE": 0.15,                      * "PROFILE_VISIT": 0,                      * "QUARTILE_95_PERCENT_VIEW": 8,                      * "SAVE": 20,                      * "SAVE_RATE": 0.18,                      * "VIDEO_10S_VIEW": 2,                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                      * "VIDEO_MRC_VIEW": 20,                      * "VIDEO_START": 29,                      * "VIDEO_V50_WATCH_TIME": 10031                               },              * "daily_metrics": [                  * {                          * "data_status": "READY",                              * "date": "2019-12-01",                              * "metrics": {                                  * "CLOSEUP": 1,                                      * "CLOSEUP_RATE": 0,                                      * "ENGAGEMENT": 1,                                      * "ENGAGEMENT_RATE": 0,                                      * "IMPRESSION": 240,                                      * "OUTBOUND_CLICK": 20,                                      * "OUTBOUND_CLICK_RATE": 0.08,                                      * "PIN_CLICK": 37,                                      * "PIN_CLICK_RATE": 0.15,                                      * "QUARTILE_95_PERCENT_VIEW": 8,                                      * "SAVE": 20,                                      * "SAVE_RATE": 0.18,                                      * "VIDEO_10S_VIEW": 2,                                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                                      * "VIDEO_MRC_VIEW": 20,                                      * "VIDEO_START": 29,                                      * "VIDEO_V50_WATCH_TIME": 10031                                                       }                                           }                               ]                   },      * "property2": {          * "summary_metrics": {                  * "CLOSEUP": 1,                      * "CLOSEUP_RATE": 0,                      * "ENGAGEMENT": 1,                      * "ENGAGEMENT_RATE": 0,                      * "IMPRESSION": 240,                      * "OUTBOUND_CLICK": 20,                      * "OUTBOUND_CLICK_RATE": 0.08,                      * "PIN_CLICK": 37,                      * "PIN_CLICK_RATE": 0.15,                      * "PROFILE_VISIT": 0,                      * "QUARTILE_95_PERCENT_VIEW": 8,                      * "SAVE": 20,                      * "SAVE_RATE": 0.18,                      * "VIDEO_10S_VIEW": 2,                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                      * "VIDEO_MRC_VIEW": 20,                      * "VIDEO_START": 29,                      * "VIDEO_V50_WATCH_TIME": 10031                               },              * "daily_metrics": [                  * {                          * "data_status": "READY",                              * "date": "2019-12-01",                              * "metrics": {                                  * "CLOSEUP": 1,                                      * "CLOSEUP_RATE": 0,                                      * "ENGAGEMENT": 1,                                      * "ENGAGEMENT_RATE": 0,                                      * "IMPRESSION": 240,                                      * "OUTBOUND_CLICK": 20,                                      * "OUTBOUND_CLICK_RATE": 0.08,                                      * "PIN_CLICK": 37,                                      * "PIN_CLICK_RATE": 0.15,                                      * "QUARTILE_95_PERCENT_VIEW": 8,                                      * "SAVE": 20,                                      * "SAVE_RATE": 0.18,                                      * "VIDEO_10S_VIEW": 2,                                      * "VIDEO_AVG_WATCH_TIME": 2507.75,                                      * "VIDEO_MRC_VIEW": 20,                                      * "VIDEO_START": 29,                                      * "VIDEO_V50_WATCH_TIME": 10031                                                       }                                           }                               ]                   }       }`

[](#operation/user_account/analytics/top_pins)Get user account top pins analytics
---------------------------------------------------------------------------------

Gets analytics data about a user's top pins (limited to the top 50).

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

ratelimit-category: org\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`pins:read``user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| sort\_by<br><br>required | string<br><br>Enum: "ENGAGEMENT" "IMPRESSION" "OUTBOUND\_CLICK" "PIN\_CLICK" "SAVE"<br><br>Specify sorting order for metrics |
| from\_claimed\_content | string<br><br>Default: "BOTH"<br><br>Enum: "OTHER" "CLAIMED" "BOTH"<br><br>Filter on Pins that match your claimed domain. |
| pin\_format | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"<br><br>Pin formats to get data for, default is all. |
| app\_types | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "MOBILE" "TABLET" "WEB"<br><br>Apps or devices to get data for, default is all. |
| content\_type | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "PAID" "ORGANIC"<br><br>Filter to paid or organic data. Default is all. |
| source | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"<br><br>Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts |
| metric\_types | Array of strings<br><br>Items Enum: "ENGAGEMENT" "ENGAGEMENT\_RATE" "IMPRESSION" "OUTBOUND\_CLICK" "OUTBOUND\_CLICK\_RATE" "PIN\_CLICK" "PIN\_CLICK\_RATE" "SAVE" "SAVE\_RATE"<br><br>Metric types to get data for, default is all. |
| num\_of\_pins | integer \[ 1 .. 50 \]<br><br>Default: 10<br><br>Example: num\_of\_pins=25<br><br>Number of pins to include, default is 10. Max is 50. |
| created\_in\_last\_n\_days | integer<br><br>Value: 30<br><br>Example: created\_in\_last\_n\_days=30<br><br>Get metrics for pins created in the last "n" days. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**403**

Not authorized to access the user account analytics.

**default**

Unexpected error

get/user\_account/analytics/top\_pins

https://api.pinterest.com/v5/user\_account/analytics/top\_pins

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "date_availability": {          * "latest_available_timestamp": 1649116799000,              * "is_realtime": false                   },      * "pins": [          * {                  * "metrics": {                          * "CLOSEUP": 1,                              * "CLOSEUP_RATE": 0,                              * "ENGAGEMENT": 1,                              * "ENGAGEMENT_RATE": 0,                              * "IMPRESSION": 240,                              * "OUTBOUND_CLICK": 20,                              * "OUTBOUND_CLICK_RATE": 0.08,                              * "PIN_CLICK": 37,                              * "PIN_CLICK_RATE": 0.15,                              * "QUARTILE_95_PERCENT_VIEW": 8,                              * "SAVE": 20,                              * "SAVE_RATE": 0.18,                              * "VIDEO_10S_VIEW": 2,                              * "VIDEO_AVG_WATCH_TIME": 2507.75,                              * "VIDEO_MRC_VIEW": 20,                              * "VIDEO_START": 29,                              * "VIDEO_V50_WATCH_TIME": 10031                                           },                      * "data_status": {                          * "property1": "READY",                              * "property2": "READY"                                           },                      * "pin_id": "642396334344813594"                               }                   ],      * "sort_by": "IMPRESSION"       }`

[](#operation/user_account/analytics/top_video_pins)Get user account top video pins analytics
---------------------------------------------------------------------------------------------

Gets analytics data about a user's top video pins (limited to the top 50).

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

ratelimit-category: org\_analytics

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`pins:read``user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| start\_date<br><br>required | string <date><br><br>Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today. |
| end\_date<br><br>required | string <date><br><br>Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date. |
| sort\_by<br><br>required | string<br><br>Enum: "IMPRESSION" "SAVE" "OUTBOUND\_CLICK" "VIDEO\_MRC\_VIEW" "VIDEO\_AVG\_WATCH\_TIME" "VIDEO\_V50\_WATCH\_TIME" "QUARTILE\_95\_PERCENT\_VIEW" "VIDEO\_10S\_VIEW" "VIDEO\_START"<br><br>Specify sorting order for video metrics |
| from\_claimed\_content | string<br><br>Default: "BOTH"<br><br>Enum: "OTHER" "CLAIMED" "BOTH"<br><br>Filter on Pins that match your claimed domain. |
| pin\_format | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"<br><br>Pin formats to get data for, default is all. |
| app\_types | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "MOBILE" "TABLET" "WEB"<br><br>Apps or devices to get data for, default is all. |
| content\_type | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "PAID" "ORGANIC"<br><br>Filter to paid or organic data. Default is all. |
| source | string<br><br>Default: "ALL"<br><br>Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"<br><br>Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts |
| metric\_types | Array of strings<br><br>Items Enum: "IMPRESSION" "SAVE" "VIDEO\_MRC\_VIEW" "VIDEO\_AVG\_WATCH\_TIME" "VIDEO\_V50\_WATCH\_TIME" "QUARTILE\_95\_PERCENT\_VIEW" "VIDEO\_10S\_VIEW" "VIDEO\_START" "OUTBOUND\_CLICK"<br><br>Metric types to get video data for, default is all. |
| num\_of\_pins | integer \[ 1 .. 50 \]<br><br>Default: 10<br><br>Example: num\_of\_pins=25<br><br>Number of pins to include, default is 10. Max is 50. |
| created\_in\_last\_n\_days | integer<br><br>Value: 30<br><br>Example: created\_in\_last\_n\_days=30<br><br>Get metrics for pins created in the last "n" days. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**403**

Not authorized to access the user account analytics.

**default**

Unexpected error

get/user\_account/analytics/top\_video\_pins

https://api.pinterest.com/v5/user\_account/analytics/top\_video\_pins

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "date_availability": {          * "latest_available_timestamp": 1649116799000,              * "is_realtime": false                   },      * "pins": [          * {                  * "metrics": {                          * "IMPRESSION": 7,                              * "QUARTILE_95_PERCENT_VIEW": 2,                              * "SAVE": 1,                              * "VIDEO_10S_VIEW": 5,                              * "VIDEO_AVG_WATCH_TIME": 86989,                              * "VIDEO_MRC_VIEW": 2,                              * "VIDEO_START": 2,                              * "VIDEO_V50_WATCH_TIME": 173979,                              * "OUTBOUND_CLICK": 2                                           },                      * "data_status": {                          * "property1": "READY",                              * "property2": "READY"                                           },                      * "pin_id": "642396334344813594"                               }                   ],      * "sort_by": "IMPRESSION"       }`

[](#operation/linked_business_accounts/get)List linked businesses
-----------------------------------------------------------------

Get a list of your linked business accounts.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

### Responses

**200**

Success

**default**

Unexpected error

get/user\_account/businesses

https://api.pinterest.com/v5/user\_account/businesses

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`[  * {          * "username": "username",              * "image_small_url": "[https://www.example.com/dj23454f53dfk2324.jpg](https://www.example.com/dj23454f53dfk2324.jpg)",              * "image_medium_url": "[https://www.example.com/dj23454f53dfk2324.jpg](https://www.example.com/dj23454f53dfk2324.jpg)",              * "image_large_url": "[https://www.example.com/dj23454f53dfk2324.jpg](https://www.example.com/dj23454f53dfk2324.jpg)",              * "image_xlarge_url": "[https://www.example.com/dj23454f53dfk2324.jpg](https://www.example.com/dj23454f53dfk2324.jpg)"                   }       ]`

[](#operation/followers/list)List followers
-------------------------------------------

Get a list of your followers.

ratelimit-category: ads\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**400**

Invalid user id

**default**

Unexpected error

get/user\_account/followers

https://api.pinterest.com/v5/user\_account/followers

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "username": "username",                      * "type": "user"                               }                   ],      * "bookmark": "string"       }`

[](#operation/user_following/get)List following
-----------------------------------------------

Get a list of who a certain user follows.

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| feed\_type | string (UserFollowingFeedType)<br><br>Default: "ALL"<br><br>Enum: "ALL" "RANKED" "CREATOR\_ONLY" "RANKED\_CREATOR\_ONLY"<br><br>Example: feed\_type=CREATOR\_ONLY<br><br>Thrift param specifying what type of followees will be kept. Default to include all followees. |
| explicit\_following | boolean<br><br>Default: false<br><br>Whether or not to include implicit user follows, which means followees with board follows. When explicit\_following is True, it means we only want explicit user follows. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

response

**default**

Unexpected error

get/user\_account/following

https://api.pinterest.com/v5/user\_account/following

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "username": "username",                      * "type": "user"                               }                   ],      * "bookmark": "string"       }`

[](#operation/boards_user_follows/list)List following boards
------------------------------------------------------------

Get a list of the boards a user follows. The request returns a board summary object array.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |
| explicit\_following | boolean<br><br>Default: false<br><br>Whether or not to include implicit user follows, which means followees with board follows. When explicit\_following is True, it means we only want explicit user follows. |
| ad\_account\_id | string <= 18 characters ^\\d+$<br><br>Unique identifier of an ad account. |

### Responses

**200**

Success

**400**

Invalid user id

**default**

Unexpected error

get/user\_account/following/boards

https://api.pinterest.com/v5/user\_account/following/boards

### Response samples

* 200
* 400
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "id": "549755885175",                      * "created_at": "2020-01-01T20:10:40-00:00",                      * "board_pins_modified_at": "2020-01-01T20:10:40-00:00",                      * "name": "Summer Recipes",                      * "description": "My favorite summer recipes",                      * "collaborator_count": 17,                      * "pin_count": 5,                      * "follower_count": 13,                      * "media": {                          * "image_cover_url": "[https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg](https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg)",                              * "pin_thumbnail_urls": [                                  * "[https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg](https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg)",                                      * "[https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg](https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg)",                                      * "[https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg](https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg)",                                      * "[https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg](https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg)"                                                       ]                                           },                      * "owner": {                          * "username": "string"                                           },                      * "privacy": "PUBLIC"                               }                   ],      * "bookmark": "string"       }`

[](#operation/follow_user/update)Follow user
--------------------------------------------

**This endpoint is currently in beta and not available to all apps. [Learn more](https://developers.pinterest.com/docs/new/about-beta-access/).**

Use this request, as a signed-in user, to follow another user.

ratelimit-category: org\_write

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:write`)

##### path Parameters

|     |     |
| --- | --- |
| username<br><br>required | string(?!^\\d+$)^.+$<br><br>Example: username<br><br>A valid username |

##### Request Body schema: application/json

Follow a user.

|     |     |
| --- | --- |
| auto\_follow | boolean (auto\_follow)<br><br>Default: false<br><br>Whether this request comes as result of auto-follow after clicking on a link. Follow links can be used by partners on their site or in emails. Only selected partners can be followed this way. We verify that partner can be auto-followed. |

### Responses

**200**

Success

**404**

User not found

**default**

Unexpected error

post/user\_account/following/{username}

https://api.pinterest.com/v5/user\_account/following/{username}

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "auto_follow": false       }`

### Response samples

* 200
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "username": "username",      * "type": "user"       }`

[](#operation/verify_website/update)Verify website
--------------------------------------------------

Verify a website as a signed-in user.

ratelimit-category: org\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:write`)

##### Request Body schema: application/json

Verify a website.

|     |     |
| --- | --- |
| website | string |
| verification\_method | string<br><br>Default: "METATAG"<br><br>Enum: "FILENAME" "METATAG" "DNSTXT" |

### Responses

**200**

Success

**default**

Unexpected error

post/user\_account/websites

https://api.pinterest.com/v5/user\_account/websites

### Request samples

* Payload

Content type

application/json

Copy

Expand all Collapse all

`{  * "website": "pintest-website-12345678.test/test_1",      * "verification_method": "METATAG"       }`

### Response samples

* 200
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "website": "mysite.test",      * "status": "success",      * "verified_at": "2022-12-14T21:03:01.602000"       }`

[](#operation/user_websites/get)Get user websites
-------------------------------------------------

Get user websites, claimed or not

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**403**

Not authorized to access the user website list.

**default**

Unexpected error

get/user\_account/websites

https://api.pinterest.com/v5/user\_account/websites

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "website": "mysite.test",                      * "status": "success",                      * "verified_at": "2022-12-14T21:03:01.602000"                               }                   ],      * "bookmark": "string"       }`

[](#operation/unverify_website/delete)Unverify website
------------------------------------------------------

Unverifu a website verified by the signed-in user.

ratelimit-category: org\_write

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:write`)

##### query Parameters

|     |     |
| --- | --- |
| website<br><br>required | string<br><br>Example: website=mysite.test<br><br>Website with path or domain only |

### Responses

**204**

Successfully unverified website

**404**

Website not in user list.

**default**

Unexpected error

delete/user\_account/websites

https://api.pinterest.com/v5/user\_account/websites

### Response samples

* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "code": 404,      * "message": "Website not in user list."       }`

[](#operation/website_verification/get)Get user verification code for website claiming
--------------------------------------------------------------------------------------

Get verification code for user to install on the website to claim it.

ratelimit-category: org\_read

sandbox: disabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

### Responses

**200**

Success

**403**

Not authorized to access the user verification code for website claiming.

**default**

Unexpected error

get/user\_account/websites/verification

https://api.pinterest.com/v5/user\_account/websites/verification

### Response samples

* 200
* 403
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "verification_code": "e1edcc1a43976c646367e9c6c9a9b7b6",      * "dns_txt_record": "pinterest-site-verification=e1edcc1a43976c646367e9c6c9a9b7b6",      * "metatag": "<meta name=\"p:domain_verify\" content=\"e1edcc1a43976c646367e9c6c9a9b7b6\"/>",      * "filename": "pinterest-e1edc.html",      * "file_content": "string"       }`

[](#operation/user_account/followed_interests)List following interests
----------------------------------------------------------------------

Get a list of a user's following interests in one place.

ratelimit-category: org\_read

sandbox: enabled

##### Authorizations:

[pinterest\_oauth2](#section/Authentication/pinterest_oauth2) (`user_accounts:read`)

##### path Parameters

|     |     |
| --- | --- |
| username<br><br>required | string(?!^\\d+$)^.+$<br><br>Example: username<br><br>A valid username |

##### query Parameters

|     |     |
| --- | --- |
| bookmark | string<br><br>Cursor used to fetch the next page of items |
| page\_size | integer \[ 1 .. 250 \]<br><br>Default: 25<br><br>Maximum number of items to include in a single page of the response. See documentation on [Pagination](https://developers.pinterest.com/docs/getting-started/pagination/) for more information. |

### Responses

**200**

Success

**400**

Invalid parameters

**401**

Authorization failed

**404**

User not found

**default**

Unexpected error

get/users/{username}/interests/follow

https://api.pinterest.com/v5/users/{username}/interests/follow

### Response samples

* 200
* 400
* 401
* 404
* default

Content type

application/json

Copy

Expand all Collapse all

`{  * "items": [          * {                  * "canonical_url": "string",                      * "id": "903972677830",                      * "key": "man cave",                      * "name": "Man cave"                               }                   ],      * "bookmark": "string"       }`