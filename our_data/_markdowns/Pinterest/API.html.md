Pinterest Developers | API (v5)Skip to contentDeveloper Platform
------------------DocsAPI referenceMy appsLog inSign up* Endpoints
	+ ad\_accounts
		- getList ad accounts
		- postCreate ad account
		- getGet ad account
		- getGet ad account analytics
		- getGet advertiser Marketing Mix Modeling (MMM) report.
		- postCreate a request for a Marketing Mix Modeling (MMM) report
		- getGet the account analytics report created by the async call
		- postCreate async request for an account analytics report
		- delDelete ads data for ad account in API Sandbox
		- getGet targeting analytics for an ad account
		- getList templates
		- postCreate async request for an analytics report using a template
	+ ad\_groups
		- getList ad groups
		- postCreate ad groups
		- patchUpdate ad groups
		- getGet ad group analytics
		- getGet targeting analytics for ad groups
		- getGet audience sizing
		- getGet ad group
		- postGet bid floors
	+ ads
		- postCreate ad preview with pin or image
		- getList ads
		- postCreate ads
		- patchUpdate ads
		- getGet ad analytics
		- getGet targeting analytics for ads
		- getGet ad
	+ audience\_insights
		- getGet audience insights
		- getGet audience insights scope and type
	+ audiences
		- getList audiences
		- postCreate audience
		- postCreate custom audience
		- getGet audience
		- patchUpdate audience
	+ billing
		- getGet ads credit discounts
		- postRedeem ad credits
		- getGet billing profiles
		- getGet Salesforce account details including bill-to information.
		- postCreate insertion order through SSIO.
		- patchEdit insertion order through SSIO.
		- getGet insertion order status by ad account id.
		- getGet insertion order status by pin order id.
		- getGet Salesforce order lines by ad account id.
	+ boards
		- getList boards
		- postCreate board
		- getGet board
		- patchUpdate board
		- delDelete board
		- getList Pins on board
		- getList board sections
		- postCreate board section
		- patchUpdate board section
		- delDelete board section
		- getList Pins on board section
	+ bulk
		- postGet advertiser entities in bulk
		- postCreate/update ad entities in bulk
		- getDownload advertiser entities in bulk
	+ campaigns
		- getList campaigns
		- postCreate campaigns
		- patchUpdate campaigns
		- getGet campaign analytics
		- getGet targeting analytics for campaigns
		- getGet campaign
	+ catalogs
		- getList catalogs
		- getList feeds
		- postCreate feed
		- getGet feed
		- patchUpdate feed
		- delDelete feed
		- getList processing results for a given feed
		- getGet catalogs items
		- postOperate on item batch
		- getGet catalogs items batch
		- getList item issues for a given processing result
		- getList product groups
		- postCreate product group
		- getGet product group
		- delDelete product group
		- patchUpdate product group
		- getGet product counts for a Product Group
		- getList products for a Product Group
		- postList filtered products
	+ conversion\_events
		- postSend conversions
	+ conversion\_tags
		- getGet conversion tags
		- postCreate conversion tag
		- getGet Ocpm eligible conversion tags
		- getGet page visit conversion tags
		- getGet conversion tag
	+ customer\_lists
		- postCreate customer lists
		- getGet customer lists
		- getGet customer list
		- patchUpdate customer list
	+ integrations
		- postCreate commerce integration
		- getGet commerce integration
		- patchUpdate commerce integration
		- delDelete commerce integration
		- postReceives batched logs from integration applications.
		- getGet integration metadata list
		- getGet integration metadata
	+ keywords
		- getGet keywords
		- postCreate keywords
		- patchUpdate keywords
		- getGet country's keyword metrics
		- getList trending keywords
	+ lead\_ads
		- postCreate lead ads subscription
		- getGet lead ads subscriptions
		- getGet lead ads subscription
		- delDelete lead ads subscription
	+ lead\_forms
		- getGet lead forms
		- getGet lead form by id
		- postCreate lead form test data
	+ media
		- getList media uploads
		- postRegister media upload
		- getGet media upload details
	+ oauth
		- postGenerate OAuth access token
	+ order\_lines
		- getGet order lines
		- getGet order line
	+ pins
		- getList Pins
		- postCreate Pin
		- getGet Pin
		- delDelete Pin
		- patchUpdate Pin
		- getGet Pin analytics
		- postSave Pin
	+ product\_group\_promotions
		- postCreate product group promotions
		- patchUpdate product group promotions
		- getGet product group promotions
		- getGet a product group promotion by id
		- getGet product group analytics
	+ product\_groups
		- getGet catalog product groups
	+ resources
		- getGet ad accounts countries
		- getGet available metrics' definitions
		- getGet lead form questions
		- getGet metrics ready state
		- getGet interest details
		- getGet targeting options
	+ search
		- getSearch user's boards
		- getSearch user's Pins
		- getSearch pins by a given search term
	+ terms
		- getList related terms
		- getList suggested terms
	+ terms\_of\_service
		- getGet terms of service
	+ user\_account
		- getGet user account
		- getGet user account analytics
		- getGet user account top pins analytics
		- getGet user account top video pins analytics
		- getList linked businesses
		- getList followers
		- getList following
		- getList following boards
		- postFollow user
		- postVerify website
		- getGet user websites
		- delUnverify website
		- getGet user verification code for website claiming
		- getList following interests
Documentation Powered by ReDocPinterest REST API (5.12.0)
===========================
 URL: https://developers.pinterest.com/ License: MIT Terms of ServicePinterest's REST API

ad\_accounts
============
View analytical information about advertising.

Note: If the current operation\_user\_account (defined by the access token)
has access to another user's Ad Accounts via
Pinterest Business Access,
you can modify your request to use the current operation\_user\_account's
permissions to those Ad Accounts by including the ad\_account\_id in the path
parameters for the request (e.g. .../?ad\_account\_id=12345&...).

List ad accounts
----------------
Get a list of the ad\_accounts that the "operation user\_account" has access to.

* This includes ad\_accounts they own and ad\_accounts that are owned by others who have granted them Business Access.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| include\_shared\_accounts | boolean Default:  true Include shared ad accounts
 |
### Responses
**200** response

**default** Unexpected error

get/ad\_accountshttps://api.pinterest.com/v5/ad\_accounts###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "string",
		- "name": "string",
		- "owner": {
			* "username": "string",
			* "id": "string"},
		- "country": "US",
		- "currency": "USD",
		- "permissions": [
			* "ADMIN"],
		- "created\_time": 1451431341,
		- "updated\_time": 1451431341}],
* "bookmark": "string"
}`Create ad account
-----------------
Create a new ad account. Different ad accounts can support different currencies, payment methods, etc.
An ad account is needed to create campaigns, ad groups, and ads; other accounts (your employees or partners) can be assigned business access and appropriate roles to access an ad account. 

You can set up up to 50 ad accounts per user. (The user must have a business account to create an ad account.) 

For more, see Create an advertiser account.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### Request Body schema: application/json
Ad account to create.

|  |  |
| --- | --- |
| country | string (Country)  Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more Country ID from ISO 3166-1 alpha-2.
 |
| name | string (name)   <= 256 characters  Ad Account name.
 |
| owner\_user\_id | string (owner\_user\_id) ^\d+$ Advertiser's owning user ID.
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accountshttps://api.pinterest.com/v5/ad\_accounts###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "country": "US",
* "owner\_user\_id": "383791336903426391",
* "name": "ACME Tools"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "string",
* "name": "string",
* "owner": {
	+ "username": "string",
	+ "id": "string"},
* "country": "US",
* "currency": "USD",
* "permissions": [
	+ "ADMIN"],
* "created\_time": 1451431341,
* "updated\_time": 1451431341
}`Get ad account
--------------
Get an ad account

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "string",
* "name": "string",
* "owner": {
	+ "username": "string",
	+ "id": "string"},
* "country": "US",
* "currency": "USD",
* "permissions": [
	+ "ADMIN"],
* "created\_time": 1451431341,
* "updated\_time": 1451431341
}`Get ad account analytics
------------------------
Get analytics for the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
### Responses
**200** Success

**400** Invalid ad account analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/analytics###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "DATE": "2021-04-01",
	+ "AD\_ACCOUNT\_ID": "547602124502",
	+ "SPEND\_IN\_DOLLAR": 30,
	+ "TOTAL\_CLICKTHROUGH": 216}
]`Get advertiser Marketing Mix Modeling (MMM) report.
---------------------------------------------------
Get an mmm report for an ad account. This returns a URL to an mmm metrics report given a token returned from the
create mmm report endpoint.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| token required  | string Token returned from the post request creation call
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/mmm\_reportshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 0,
* "data": {
	+ "report\_status": "DOES\_NOT\_EXIST",
	+ "url": "string",
	+ "size": 0},
* "message": "ok",
* "status": "success"
}`Create a request for a Marketing Mix Modeling (MMM) report
----------------------------------------------------------
This creates an asynchronous mmm report based on the given request. It returns a token that you can use to download
the report when it is ready. NOTE: An additional limit of 5 queries per minute per advertiser applies to this endpoint while it's in beta release.

 ratelimit-category:  ads\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| report\_name required  | string (report\_name)  Name of the Marketing Mix Modeling (MMM) report
 |
| start\_date required  | string^(\d{4})-(\d{2})-(\d{2})$ Metric report start date (UTC). Format: YYYY-MM-DD
 |
| end\_date required  | string^(\d{4})-(\d{2})-(\d{2})$ Metric report end date (UTC). Format: YYYY-MM-DD
 |
| granularity required  | string Enum: "DAY" "WEEK"  DAY - metrics are broken down daily. WEEK - metrics are broken down weekly.
 |
| level required  | string Enum: "CAMPAIGN\_TARGETING" "AD\_GROUP\_TARGETING"  Level of the report
 |
| targeting\_types required  | Array of strings (targeting\_types)   [ 1 .. 5 ] items Items Enum: "APPTYPE" "COUNTRY" "CREATIVE\_TYPE" "GENDER" "LOCATION"  List of targeting types
 |
| columns required  | Array of strings (MMMReportingColumn) Items Enum: "SPEND\_IN\_DOLLAR" "SPEND\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "ECTR" "CAMPAIGN\_NAME" "TOTAL\_ENGAGEMENT" "EENGAGEMENT\_RATE" "ECPM\_IN\_DOLLAR" "CAMPAIGN\_ID" "ADVERTISER\_ID" "AD\_GROUP\_ID" "AD\_GROUP\_NAME" "CLICKTHROUGH\_1" "IMPRESSION\_1" "CLICKTHROUGH\_2" "IMPRESSION\_2" "TOTAL\_CLICKTHROUGH" "TOTAL\_IMPRESSION" "ADVERTISER\_NAME" "SPEND\_ORDER\_LINE\_PAID\_TYPE"  Metric and entity columns
 |
| countries | Array of strings (TargetingAdvertiserCountry) Items Enum: "US" "GB" "CA" "IE" "AU" "NZ" "FR" "SE" "IL" "DE" "AT" "IT" "ES" "NL" "BE" "PT" "CH" "HK" "JP" "KR" … 18 more A List of countries for filtering
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics mmm parameters

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/mmm\_reportshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/mmm\_reports###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "report\_name": "string",
* "start\_date": "2020-12-20",
* "end\_date": "2020-12-20",
* "granularity": "DAY",
* "level": "CAMPAIGN\_TARGETING",
* "targeting\_types": [
	+ "GENDER"],
* "columns": [
	+ "SPEND\_IN\_DOLLAR"],
* "countries": [
	+ "US"]
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 0,
* "data": {
	+ "report\_status": "FINISHED",
	+ "token": "string",
	+ "message": "string",
	+ "status": "success"}
}`Get the account analytics report created by the async call
----------------------------------------------------------
This returns a URL to an analytics report given a token returned from the post request report creation call. You can use the URL to download the report. The link is valid for five minutes and the report is valid for one hour.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.

 ratelimit-category:  ads\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| token required  | string Token returned from the post request creation call
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/reportshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/reports###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "report\_status": "FINISHED",
* "url": "string",
* "size": 0
}`Create async request for an account analytics report
----------------------------------------------------
This returns a token that you can use to download the report when it is ready. Note that this endpoint requires the parameters to be passed as JSON-formatted in the request body. This endpoint does not support URL query parameters.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 914 days before the current date in UTC time and the max time range supported is 186 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.
* If level is PRODUCT\_ITEM, the furthest back you can are allowed to pull data is 92 days before the current date in UTC time and the max time range supported is 31 days.
* If level is PRODUCT\_ITEM, ad\_ids and ad\_statuses parameters are not allowed. Any columns related to pin promotion and ad is not allowed either.

 ratelimit-category:  ads\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| start\_date required  | string^(\d{4})-(\d{2})-(\d{2})$ Metric report start date (UTC). Format: YYYY-MM-DD
 |
| end\_date required  | string^(\d{4})-(\d{2})-(\d{2})$ Metric report end date (UTC). Format: YYYY-MM-DD
 |
| granularity required  | string Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"  TOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"  The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
| attribution\_types | Array of strings (ConversionReportAttributionType) Items Enum: "INDIVIDUAL" "HOUSEHOLD"  List of types of attribution for the conversion report
 |
| campaign\_ids | Array of strings  [ 1 .. 500 ] items  List of campaign ids
 |
| campaign\_statuses | Array of strings (CampaignSummaryStatus)   [ 1 .. 6 ] items Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  List of status values for filtering
 |
| campaign\_objective\_types | Array of strings (ObjectiveType)   [ 1 .. 6 ] items Items Enum: "AWARENESS" "CONSIDERATION" "VIDEO\_VIEW" "WEB\_CONVERSION" "CATALOG\_SALES" "WEB\_SESSIONS"  List of values for filtering. ["WEB\_SESSIONS"] in BETA.
 |
| ad\_group\_ids | Array of strings  [ 1 .. 500 ] items  List of ad group ids
 |
| ad\_group\_statuses | Array of strings (AdGroupSummaryStatus)   [ 1 .. 6 ] items Items Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  List of values for filtering
 |
| ad\_ids | Array of strings  [ 1 .. 500 ] items  List of ad ids [This parameter is no supported for Product Item Level Reports]
 |
| ad\_statuses | Array of strings (PinPromotionSummaryStatus)   [ 1 .. 6 ] items Items Enum: "APPROVED" "PAUSED" "PENDING" "REJECTED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  List of values for filtering [This parameter is not supported for Product Item Level Reports]
 |
| product\_group\_ids | Array of strings  [ 1 .. 500 ] items  List of product group ids
 |
| product\_group\_statuses | Array of strings (ProductGroupSummaryStatus)   [ 1 .. 6 ] items Items Enum: "RUNNING" "PAUSED" "EXCLUDED" "ARCHIVED"  List of values for filtering
 |
| product\_item\_ids | Array of strings  [ 1 .. 500 ] items  List of product item ids
 |
| targeting\_types | Array of strings (AdsAnalyticsTargetingType)   [ 1 .. 5 ] items Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"  List of targeting types. Requires `level` to be a value ending in `_TARGETING`.
 |
| metrics\_filters | Array of objects (AdsAnalyticsMetricsFilter)   non-empty  List of metrics filters
 |
| columns required  | Array of strings (ReportingColumnAsync) Items Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "OUTBOUND\_CTR" "COST\_PER\_OUTBOUND\_CLICK" "CAMPAIGN\_NAME" "CAMPAIGN\_STATUS" "PIN\_PROMOTION\_STATUS" "AD\_STATUS" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" … 541 more Metric and entity columns. Pin promotion and ad related columns are not supported for the Product Item level reports.
 |
| level required  | string Enum: "ADVERTISER" "ADVERTISER\_TARGETING" "CAMPAIGN" "CAMPAIGN\_TARGETING" "AD\_GROUP" "AD\_GROUP\_TARGETING" "PIN\_PROMOTION" "PIN\_PROMOTION\_TARGETING" "KEYWORD" "PRODUCT\_GROUP" "PRODUCT\_GROUP\_TARGETING" "PRODUCT\_ITEM"  Level of the report
 |
| report\_format | string Default:  "JSON" Enum: "JSON" "CSV"  Specification for formatting the report data. Reports in JSON will not zero-fill metrics, whereas reports in CSV will. Both report formats will omit rows where all the columns are equal to 0.
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics parameters.

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/reportshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/reports###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "start\_date": "2020-12-20",
* "end\_date": "2020-12-20",
* "granularity": "TOTAL",
* "click\_window\_days": 0,
* "engagement\_window\_days": 0,
* "view\_window\_days": 0,
* "conversion\_report\_time": "TIME\_OF\_AD\_ACTION",
* "attribution\_types": [
	+ "INDIVIDUAL"],
* "campaign\_ids": [
	+ "12345678"],
* "campaign\_statuses": [
	+ "RUNNING",
	+ "PAUSED"],
* "campaign\_objective\_types": [
	+ "AWARENESS",
	+ "VIDEO\_VIEW"],
* "ad\_group\_ids": [
	+ "12345678"],
* "ad\_group\_statuses": [
	+ "RUNNING",
	+ "PAUSED"],
* "ad\_ids": [
	+ "12345678"],
* "ad\_statuses": [
	+ "APPROVED",
	+ "PAUSED"],
* "product\_group\_ids": [
	+ "12345678"],
* "product\_group\_statuses": [
	+ "RUNNING",
	+ "PAUSED"],
* "product\_item\_ids": [
	+ "12345678"],
* "targeting\_types": [
	+ "APPTYPE"],
* "metrics\_filters": [
	+ {
		- "field": "SPEND\_IN\_DOLLAR",
		- "operator": "LESS\_THAN",
		- "values": [
			* 0]}],
* "columns": [
	+ "SPEND\_IN\_MICRO\_DOLLAR"],
* "level": "CAMPAIGN",
* "report\_format": "JSON"
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "report\_status": "FINISHED",
* "token": "string",
* "message": "string"
}`Delete ads data for ad account in API Sandbox
---------------------------------------------
Delete an ad account and all the ads data associated with that account. 
A string message is returned indicating the status of the delete operation.

Note: This endpoint is only allowed in the Pinterest API Sandbox (https://api-sandbox.pinterest.com/v5). 
Go to https://developers.pinterest.com/docs/dev-tools/sandbox/ for more information.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** OK

**400** Invalid ad account id.

**default** Unexpected error

delete/ad\_accounts/{ad\_account\_id}/sandboxhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/sandbox###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `"Delete Success"`Get targeting analytics for an ad account
-----------------------------------------
Get targeting analytics for an ad account.
For the requested account and metrics, the response will include the requested metric information
(e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49"). 

* The token's user\_account must either be the Owner of the specified ad account, or have one
of the necessary roles granted to them via
Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| targeting\_types required  | Array of strings (AdsAnalyticsTargetingType)   [ 1 .. 15 ] items Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"   Example:  targeting\_types=APPTYPETargeting type breakdowns for the report. The reporting per targeting type  is independent from each other.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
| attribution\_types | string (ConversionReportAttributionType)  Enum: "INDIVIDUAL" "HOUSEHOLD"   Example:  attribution\_types=INDIVIDUALList of types of attribution for the conversion report
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/targeting\_analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/targeting\_analytics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "targeting\_type": "KEYWORD",
		- "targeting\_value": "christmas decor ideas",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "iphone",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "ipad",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_tablet",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GENDER",
		- "targeting\_value": "female",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "LOCATION",
		- "targeting\_value": 500,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PLACEMENT",
		- "targeting\_value": "SEARCH",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "COUNTRY",
		- "targeting\_value": "US",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "TARGETED\_INTEREST",
		- "targeting\_value": "Food and Drinks",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PINNER\_INTEREST",
		- "targeting\_value": "Chocolate Cookies",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AUDIENCE\_INCLUDE",
		- "targeting\_value": 254261234567,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GEO",
		- "targeting\_value": "US:94102",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AGE\_BUCKET",
		- "targeting\_value": "45-49",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "REGION",
		- "targeting\_value": "US-CA",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}}]
}`List templates
--------------
Gets all Templates associated with an ad account ID.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**400** Invalid ad account template parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/templateshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/templates###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "6739202847590",
		- "ad\_account\_id": "547664674848",
		- "ad\_account\_ids": [
			* "547664674848"],
		- "user\_id": "784762938748396",
		- "name": "Week over week spend",
		- "report\_start\_relative\_days\_in\_past": 7,
		- "report\_end\_relative\_days\_in\_past": 7,
		- "date\_range": {
			* "dynamic\_date\_range": {
				+ "range": "YEAR\_TO\_DATE",
				+ "type": "dynamic"},
			* "relative\_date\_range": {
				+ "end\_days\_in\_past": 7,
				+ "type": "relative",
				+ "start\_days\_in\_past": 14},
			* "absolute\_date\_range": {
				+ "end\_date": 6.027456183070403,
				+ "type": "absolute",
				+ "start\_date": 0.8008281904610115}},
		- "report\_level": "CAMPAIGN",
		- "report\_format": "JSON",
		- "columns": [
			* "SPEND\_IN\_DOLLAR"],
		- "granularity": "TOTAL",
		- "view\_window\_days": 7,
		- "click\_window\_days": 7,
		- "engagement\_window\_days": 7,
		- "conversion\_report\_time\_type": "TIME\_OF\_AD\_ACTION",
		- "filters\_json": "[{\"field\": \"SPEND\_IN\_DOLLAR\", \"operator\": \"=\", \"value\": 100}]",
		- "is\_owned\_by\_user": true,
		- "is\_scheduled": true,
		- "creation\_source": "ADS\_MANAGER\_REPORT\_BUILDER",
		- "is\_deleted": false,
		- "updated\_time": 1432744744,
		- "custom\_column\_ids": [
			* "1597252063"],
		- "type": "BULK",
		- "ingestion\_sources": [
			* "CONVERSIONS\_API"]}],
* "bookmark": "string"
}`Create async request for an analytics report using a template
-------------------------------------------------------------
This takes a template ID and an optional custom timeframe and constructs an asynchronous report based on the
template. It returns a token that you can use to download the report when it is ready.

 ratelimit-category:  ads\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| template\_id required  | string  <= 18 characters ^\d+$ Unique identifier of a template.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years back from today.
 |
| end\_date | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 2.5 years past start date.
 |
| granularity | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics template parameters.

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reportshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/templates/{template\_id}/reports###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "report\_status": "FINISHED",
* "token": "string",
* "message": "string"
}`ad\_groups
==========
View, create or update ad groups.

List ad groups
--------------
List ad groups based on provided campaign IDs or ad group IDs.(campaign\_ids or ad\_group\_ids). 

**Note:**

Provide only campaign\_id or ad\_group\_id. Do not provide both.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| campaign\_ids | Array of strings  [ 1 .. 100 ] items  List of Campaign Ids to use to filter the results.
 |
| ad\_group\_ids | Array of strings  [ 1 .. 100 ] items  List of Ad group Ids to use to filter the results.
 |
| entity\_statuses | Array of strings Default:  ["ACTIVE","PAUSED"]Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"   Example:  entity\_statuses=ACTIVEEntity status
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| translate\_interests\_to\_names | boolean Default:  false Return interests as text names (if value is true) rather than topic IDs.
 |
### Responses
**200** Success

**400** Invalid ad account group parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groupshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "name": "Ad Group For Pin: 687195905986",
		- "status": "ACTIVE",
		- "budget\_in\_micro\_currency": 5000000,
		- "bid\_in\_micro\_currency": 5000000,
		- "optimization\_goal\_metadata": {
			* "conversion\_tag\_v3\_goal\_metadata": {
				+ "attribution\_windows": {
					- "click\_window\_days": 0,
					- "engagement\_window\_days": 0,
					- "view\_window\_days": 0},
				+ "conversion\_event": "PAGE\_VISIT",
				+ "conversion\_tag\_id": "string",
				+ "cpa\_goal\_value\_in\_micro\_currency": "string",
				+ "is\_roas\_optimized": true,
				+ "learning\_mode\_type": "ACTIVE"},
			* "frequency\_goal\_metadata": {
				+ "frequency": 0,
				+ "timerange": "DAY"},
			* "scrollup\_goal\_metadata": {
				+ "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
		- "budget\_type": "DAILY",
		- "start\_time": 5686848000,
		- "end\_time": 5705424000,
		- "targeting\_spec": {
			* "AGE\_BUCKET": [
				+ "35-44",
				+ "50-54"],
			* "APPTYPE": [
				+ "ipad",
				+ "iphone"],
			* "AUDIENCE\_EXCLUDE": [
				+ "string"],
			* "AUDIENCE\_INCLUDE'": [
				+ "string"],
			* "GENDER": [
				+ "unknown"],
			* "GEO": [
				+ "string"],
			* "INTEREST": [
				+ "string"],
			* "LOCALE": [
				+ "string"],
			* "LOCATION": [
				+ "string"],
			* "SHOPPING\_RETARGETING": [
				+ {
					- "lookback\_window": 30,
					- "exclusion\_window": 14,
					- "tag\_types": [
						* 0,
						* 6]}],
			* "TARGETING\_STRATEGY": [
				+ "CHOOSE\_YOUR\_OWN"]},
		- "lifetime\_frequency\_cap": 100,
		- "tracking\_urls": {
			* "impression": [
				+ "URL1",
				+ "URL2"],
			* "click": [
				+ "URL1",
				+ "URL2"],
			* "engagement": [
				+ "URL1",
				+ "URL2"],
			* "buyable\_button": [
				+ "URL1",
				+ "URL2"],
			* "audience\_verification": [
				+ "URL1",
				+ "URL2"]},
		- "auto\_targeting\_enabled": true,
		- "placement\_group": "ALL",
		- "pacing\_delivery\_type": "STANDARD",
		- "campaign\_id": "626736533506",
		- "billable\_event": "CLICKTHROUGH",
		- "bid\_strategy\_type": "MAX\_BID",
		- "id": "2680060704746",
		- "ad\_account\_id": "549755885175",
		- "created\_time": 1476477189,
		- "updated\_time": 1476477189,
		- "type": "adgroup",
		- "conversion\_learning\_mode\_type": "ACTIVE",
		- "summary\_status": "RUNNING",
		- "feed\_profile\_id": "626736533506",
		- "dca\_assets": null}],
* "bookmark": "string"
}`Create ad groups
----------------
Create multiple new ad groups. All ads in a given ad group will have the same budget, bid, run dates, targeting, and placement (search, browse, other). For more information, click here.

**Note:**
* 'bid\_in\_micro\_currency' and 'budget\_in\_micro\_currency' should be expressed in microcurrency amounts based on the currency field set in the advertiser's profile.Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.

A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.

**Equivalency equations**, using dollars as an example currency:

	+ $1 = 1,000,000 microdollars
	+ 1 microdollar = $0.000001**To convert between currency and microcurrency**, using dollars as an example currency:

	+ To convert dollars to microdollars, mutiply dollars by 1,000,000
	+ To convert microdollars to dollars, divide microdollars by 1,000,000
* Ad groups belong to ad campaigns. Some types of campaigns (e.g. budget optimization) have limits on the number of ad groups they can hold. If you exceed those limits, you will get an error message.
* Start and end time cannot be set for ad groups that belong to CBO campaigns. Currently, campaigns with the following objective types: TRAFFIC, AWARENESS, WEB\_CONVERSIONS, and CATALOG\_SALES will default to CBO.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of ad groups to create, size limit [1, 30].

 Array ()
|  |  |
| --- | --- |
| name required  | string Ad group name.
 |
| status | string Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Ad group/entity status.
 |
| budget\_in\_micro\_currency | integer Nullable  Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups.
 |
| bid\_in\_micro\_currency | integer Nullable  Bid price in micro currency. This field is **REQUIRED** for the following campaign objective\_type/billable\_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG\_SALES/CLICKTHROUGH, VIDEO\_VIEW/VIDEO\_V\_50\_MRC.
 |
| optimization\_goal\_metadata | object Nullable  Optimization goals for objective-based performance campaigns. **REQUIRED** when campaign's `objective_type` is set to `"WEB_CONVERSION"`.
 |
| budget\_type | string Default:  "DAILY" Enum: "DAILY" "LIFETIME" "CBO\_ADGROUP"  Budget type. If DAILY, an ad group's daily spend will not exceed the budget parameter value. If LIFETIME, the end\_time parameter is **REQUIRED**, and the ad group spend is spread evenly between the ad group `start_time` and `end_time` range. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. For CBO campaigns, only "CBO\_ADGROUP" is allowed. For WEB\_SESSIONS campaigns, only "LIFETIME" is allowed.
 |
| start\_time | integer Nullable  Ad group start time. Unix timestamp in seconds. Defaults to current time.
 |
| end\_time | integer Nullable  Ad group end time. Unix timestamp in seconds.
 |
| targeting\_spec | object (TargetingSpec)  Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":["iphone"], "GENDER":["male"], "LOCALE":["en-US"], "LOCATION":["501"], "AGE\_BUCKET":["25-34"]}
 |
| lifetime\_frequency\_cap | integer Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions)) ad groups. A CPM ad group has an IMPRESSION billable\_event value. This field **REQUIRES** the `end_time` field.
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. JSON object with the format: {"Tracking event enum":[URL string array],...} For example: {"impression": ["URL1", "URL2"], "click": ["URL1", "URL2", "URL3"]}.Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs. For more information, see Third-party and dynamic tracking.
 |
| auto\_targeting\_enabled | boolean Nullable  Enable auto-targeting for ad group. Also known as "expanded targeting".
 |
| placement\_group | string Enum: "ALL" "SEARCH" "BROWSE" "OTHER"  Placement group.
 |
| pacing\_delivery\_type | string Default:  "STANDARD" Enum: "STANDARD" "ACCELERATED"  Ad group pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day. When using CBO, only the STANDARD pacing delivery type is allowed.
 |
| campaign\_id required  | string^[C]?\d+$ Campaign ID of the ad group.
 |
| billable\_event required  | string (ActionType)  Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO\_V\_50\_MRC"  Ad group billable event type.
 |
| bid\_strategy\_type | string (BidStrategyType)  Nullable  Enum: "AUTOMATIC\_BID" "MAX\_BID" "TARGET\_AVG" null  Bid strategy type
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/ad\_groupshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "name": "Ad Group For Pin: 687195905986",
	+ "status": "ACTIVE",
	+ "budget\_in\_micro\_currency": 5000000,
	+ "bid\_in\_micro\_currency": 5000000,
	+ "optimization\_goal\_metadata": {
		- "conversion\_tag\_v3\_goal\_metadata": {
			* "attribution\_windows": {
				+ "click\_window\_days": 0,
				+ "engagement\_window\_days": 0,
				+ "view\_window\_days": 0},
			* "conversion\_event": "PAGE\_VISIT",
			* "conversion\_tag\_id": "string",
			* "cpa\_goal\_value\_in\_micro\_currency": "string",
			* "is\_roas\_optimized": true,
			* "learning\_mode\_type": "ACTIVE"},
		- "frequency\_goal\_metadata": {
			* "frequency": 0,
			* "timerange": "DAY"},
		- "scrollup\_goal\_metadata": {
			* "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
	+ "budget\_type": "DAILY",
	+ "start\_time": 5686848000,
	+ "end\_time": 5705424000,
	+ "targeting\_spec": {
		- "AGE\_BUCKET": [
			* "35-44",
			* "50-54"],
		- "APPTYPE": [
			* "ipad",
			* "iphone"],
		- "AUDIENCE\_EXCLUDE": [
			* "string"],
		- "AUDIENCE\_INCLUDE'": [
			* "string"],
		- "GENDER": [
			* "unknown"],
		- "GEO": [
			* "string"],
		- "INTEREST": [
			* "string"],
		- "LOCALE": [
			* "string"],
		- "LOCATION": [
			* "string"],
		- "SHOPPING\_RETARGETING": [
			* {
				+ "lookback\_window": 30,
				+ "exclusion\_window": 14,
				+ "tag\_types": [
					- 0,
					- 6]}],
		- "TARGETING\_STRATEGY": [
			* "CHOOSE\_YOUR\_OWN"]},
	+ "lifetime\_frequency\_cap": 100,
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "auto\_targeting\_enabled": true,
	+ "placement\_group": "ALL",
	+ "pacing\_delivery\_type": "STANDARD",
	+ "campaign\_id": "626736533506",
	+ "billable\_event": "CLICKTHROUGH",
	+ "bid\_strategy\_type": "MAX\_BID"}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "name": "Ad Group For Pin: 687195905986",
			* "status": "ACTIVE",
			* "budget\_in\_micro\_currency": 5000000,
			* "bid\_in\_micro\_currency": 5000000,
			* "optimization\_goal\_metadata": {
				+ "conversion\_tag\_v3\_goal\_metadata": {
					- "attribution\_windows": {
						* "click\_window\_days": 0,
						* "engagement\_window\_days": 0,
						* "view\_window\_days": 0},
					- "conversion\_event": "PAGE\_VISIT",
					- "conversion\_tag\_id": "string",
					- "cpa\_goal\_value\_in\_micro\_currency": "string",
					- "is\_roas\_optimized": true,
					- "learning\_mode\_type": "ACTIVE"},
				+ "frequency\_goal\_metadata": {
					- "frequency": 0,
					- "timerange": "DAY"},
				+ "scrollup\_goal\_metadata": {
					- "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
			* "budget\_type": "DAILY",
			* "start\_time": 5686848000,
			* "end\_time": 5705424000,
			* "targeting\_spec": {
				+ "AGE\_BUCKET": [
					- "35-44",
					- "50-54"],
				+ "APPTYPE": [
					- "ipad",
					- "iphone"],
				+ "AUDIENCE\_EXCLUDE": [
					- "string"],
				+ "AUDIENCE\_INCLUDE'": [
					- "string"],
				+ "GENDER": [
					- "unknown"],
				+ "GEO": [
					- "string"],
				+ "INTEREST": [
					- "string"],
				+ "LOCALE": [
					- "string"],
				+ "LOCATION": [
					- "string"],
				+ "SHOPPING\_RETARGETING": [
					- {
						* "lookback\_window": 30,
						* "exclusion\_window": 14,
						* "tag\_types": [
							+ 0,
							+ 6]}],
				+ "TARGETING\_STRATEGY": [
					- "CHOOSE\_YOUR\_OWN"]},
			* "lifetime\_frequency\_cap": 100,
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "auto\_targeting\_enabled": true,
			* "placement\_group": "ALL",
			* "pacing\_delivery\_type": "STANDARD",
			* "campaign\_id": "626736533506",
			* "billable\_event": "CLICKTHROUGH",
			* "bid\_strategy\_type": "MAX\_BID",
			* "id": "2680060704746",
			* "ad\_account\_id": "549755885175",
			* "created\_time": 1476477189,
			* "updated\_time": 1476477189,
			* "type": "adgroup",
			* "conversion\_learning\_mode\_type": "ACTIVE",
			* "summary\_status": "RUNNING",
			* "feed\_profile\_id": "626736533506",
			* "dca\_assets": null},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Update ad groups
----------------
Update multiple existing ad groups.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of ad groups to update, size limit [1, 30].

 Array ()
|  |  |
| --- | --- |
| name | string Ad group name.
 |
| status | string Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Ad group/entity status.
 |
| budget\_in\_micro\_currency | integer Nullable  Budget in micro currency. This field is **REQUIRED** for non-CBO (campaign budget optimization) campaigns. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. A CBO campaign is limited to 70 or less ad groups.
 |
| bid\_in\_micro\_currency | integer Nullable  Bid price in micro currency. This field is **REQUIRED** for the following campaign objective\_type/billable\_event combinations: AWARENESS/IMPRESSION, CONSIDERATION/CLICKTHROUGH, CATALOG\_SALES/CLICKTHROUGH, VIDEO\_VIEW/VIDEO\_V\_50\_MRC.
 |
| optimization\_goal\_metadata | object Nullable  Optimization goals for objective-based performance campaigns. **REQUIRED** when campaign's `objective_type` is set to `"WEB_CONVERSION"`.
 |
| budget\_type | string Enum: "DAILY" "LIFETIME" "CBO\_ADGROUP"  Budget type. If DAILY, an ad group's daily spend will not exceed the budget parameter value. If LIFETIME, the end\_time parameter is **REQUIRED**, and the ad group spend is spread evenly between the ad group `start_time` and `end_time` range. A CBO campaign automatically generates ad group budgets from its campaign budget to maximize campaign outcome. For CBO campaigns, only "CBO\_ADGROUP" is allowed. For WEB\_SESSIONS campaigns, only "LIFETIME" is allowed.
 |
| start\_time | integer Nullable  Ad group start time. Unix timestamp in seconds. Defaults to current time.
 |
| end\_time | integer Nullable  Ad group end time. Unix timestamp in seconds.
 |
| targeting\_spec | object (TargetingSpec)  Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":["iphone"], "GENDER":["male"], "LOCALE":["en-US"], "LOCATION":["501"], "AGE\_BUCKET":["25-34"]}
 |
| lifetime\_frequency\_cap | integer Set a limit to the number of times a promoted pin from this campaign can be impressed by a pinner within the past rolling 30 days. Only available for CPM (cost per mille (1000 impressions)) ad groups. A CPM ad group has an IMPRESSION billable\_event value. This field **REQUIRES** the `end_time` field.
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. JSON object with the format: {"Tracking event enum":[URL string array],...} For example: {"impression": ["URL1", "URL2"], "click": ["URL1", "URL2", "URL3"]}.Up to three tracking URLs are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. May be null. Pass in an empty object - {} - to remove tracking URLs. For more information, see Third-party and dynamic tracking.
 |
| auto\_targeting\_enabled | boolean Nullable  Enable auto-targeting for ad group. Also known as "expanded targeting".
 |
| placement\_group | string Enum: "ALL" "SEARCH" "BROWSE" "OTHER"  Placement group.
 |
| pacing\_delivery\_type | string Enum: "STANDARD" "ACCELERATED"  Ad group pacing delivery type. With ACCELERATED, an ad group budget is spent as fast as possible. With STANDARD, an ad group budget is spent smoothly over a day. When using CBO, only the STANDARD pacing delivery type is allowed.
 |
| campaign\_id | string^[C]?\d+$ Campaign ID of the ad group.
 |
| billable\_event | string (ActionType)  Enum: "CLICKTHROUGH" "IMPRESSION" "VIDEO\_V\_50\_MRC"  Ad group billable event type.
 |
| bid\_strategy\_type | string (BidStrategyType)  Nullable  Enum: "AUTOMATIC\_BID" "MAX\_BID" "TARGET\_AVG" null  Bid strategy type
 |
| id required  | string^\d+$ Ad group ID.
 |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/ad\_groupshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "name": "Ad Group For Pin: 687195905986",
	+ "status": "ACTIVE",
	+ "budget\_in\_micro\_currency": 5000000,
	+ "bid\_in\_micro\_currency": 5000000,
	+ "optimization\_goal\_metadata": {
		- "conversion\_tag\_v3\_goal\_metadata": {
			* "attribution\_windows": {
				+ "click\_window\_days": 0,
				+ "engagement\_window\_days": 0,
				+ "view\_window\_days": 0},
			* "conversion\_event": "PAGE\_VISIT",
			* "conversion\_tag\_id": "string",
			* "cpa\_goal\_value\_in\_micro\_currency": "string",
			* "is\_roas\_optimized": true,
			* "learning\_mode\_type": "ACTIVE"},
		- "frequency\_goal\_metadata": {
			* "frequency": 0,
			* "timerange": "DAY"},
		- "scrollup\_goal\_metadata": {
			* "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
	+ "budget\_type": "DAILY",
	+ "start\_time": 5686848000,
	+ "end\_time": 5705424000,
	+ "targeting\_spec": {
		- "AGE\_BUCKET": [
			* "35-44",
			* "50-54"],
		- "APPTYPE": [
			* "ipad",
			* "iphone"],
		- "AUDIENCE\_EXCLUDE": [
			* "string"],
		- "AUDIENCE\_INCLUDE'": [
			* "string"],
		- "GENDER": [
			* "unknown"],
		- "GEO": [
			* "string"],
		- "INTEREST": [
			* "string"],
		- "LOCALE": [
			* "string"],
		- "LOCATION": [
			* "string"],
		- "SHOPPING\_RETARGETING": [
			* {
				+ "lookback\_window": 30,
				+ "exclusion\_window": 14,
				+ "tag\_types": [
					- 0,
					- 6]}],
		- "TARGETING\_STRATEGY": [
			* "CHOOSE\_YOUR\_OWN"]},
	+ "lifetime\_frequency\_cap": 100,
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "auto\_targeting\_enabled": true,
	+ "placement\_group": "ALL",
	+ "pacing\_delivery\_type": "STANDARD",
	+ "campaign\_id": "626736533506",
	+ "billable\_event": "CLICKTHROUGH",
	+ "bid\_strategy\_type": "MAX\_BID",
	+ "id": "2680060704746"}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "name": "Ad Group For Pin: 687195905986",
			* "status": "ACTIVE",
			* "budget\_in\_micro\_currency": 5000000,
			* "bid\_in\_micro\_currency": 5000000,
			* "optimization\_goal\_metadata": {
				+ "conversion\_tag\_v3\_goal\_metadata": {
					- "attribution\_windows": {
						* "click\_window\_days": 0,
						* "engagement\_window\_days": 0,
						* "view\_window\_days": 0},
					- "conversion\_event": "PAGE\_VISIT",
					- "conversion\_tag\_id": "string",
					- "cpa\_goal\_value\_in\_micro\_currency": "string",
					- "is\_roas\_optimized": true,
					- "learning\_mode\_type": "ACTIVE"},
				+ "frequency\_goal\_metadata": {
					- "frequency": 0,
					- "timerange": "DAY"},
				+ "scrollup\_goal\_metadata": {
					- "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
			* "budget\_type": "DAILY",
			* "start\_time": 5686848000,
			* "end\_time": 5705424000,
			* "targeting\_spec": {
				+ "AGE\_BUCKET": [
					- "35-44",
					- "50-54"],
				+ "APPTYPE": [
					- "ipad",
					- "iphone"],
				+ "AUDIENCE\_EXCLUDE": [
					- "string"],
				+ "AUDIENCE\_INCLUDE'": [
					- "string"],
				+ "GENDER": [
					- "unknown"],
				+ "GEO": [
					- "string"],
				+ "INTEREST": [
					- "string"],
				+ "LOCALE": [
					- "string"],
				+ "LOCATION": [
					- "string"],
				+ "SHOPPING\_RETARGETING": [
					- {
						* "lookback\_window": 30,
						* "exclusion\_window": 14,
						* "tag\_types": [
							+ 0,
							+ 6]}],
				+ "TARGETING\_STRATEGY": [
					- "CHOOSE\_YOUR\_OWN"]},
			* "lifetime\_frequency\_cap": 100,
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "auto\_targeting\_enabled": true,
			* "placement\_group": "ALL",
			* "pacing\_delivery\_type": "STANDARD",
			* "campaign\_id": "626736533506",
			* "billable\_event": "CLICKTHROUGH",
			* "bid\_strategy\_type": "MAX\_BID",
			* "id": "2680060704746",
			* "ad\_account\_id": "549755885175",
			* "created\_time": 1476477189,
			* "updated\_time": 1476477189,
			* "type": "adgroup",
			* "conversion\_learning\_mode\_type": "ACTIVE",
			* "summary\_status": "RUNNING",
			* "feed\_profile\_id": "626736533506",
			* "dca\_assets": null},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Get ad group analytics
----------------------
Get analytics for the specified ad groups in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| ad\_group\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Ad group Ids to use to filter the results.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
### Responses
**200** Success

**400** Invalid ad account group analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/analytics###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "DATE": "2021-04-01",
	+ "AD\_GROUP\_ID": "547602124502",
	+ "SPEND\_IN\_DOLLAR": 30,
	+ "TOTAL\_CLICKTHROUGH": 216}
]`Get targeting analytics for ad groups
-------------------------------------
Get targeting analytics for one or more ad groups.
For the requested ad group(s) and metrics, the response will include the requested metric information
(e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49"). 

* The token's user\_account must either be the Owner of the specified ad account, or have one
of the necessary roles granted to them via
Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_group\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Ad group Ids to use to filter the results.
 |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| targeting\_types required  | Array of strings (AdsAnalyticsTargetingType)   [ 1 .. 15 ] items Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"   Example:  targeting\_types=APPTYPETargeting type breakdowns for the report. The reporting per targeting type  is independent from each other.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
| attribution\_types | string (ConversionReportAttributionType)  Enum: "INDIVIDUAL" "HOUSEHOLD"   Example:  attribution\_types=INDIVIDUALList of types of attribution for the conversion report
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/targeting\_analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/targeting\_analytics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "targeting\_type": "KEYWORD",
		- "targeting\_value": "christmas decor ideas",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "iphone",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "ipad",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_tablet",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GENDER",
		- "targeting\_value": "female",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "LOCATION",
		- "targeting\_value": 500,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PLACEMENT",
		- "targeting\_value": "SEARCH",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "COUNTRY",
		- "targeting\_value": "US",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "TARGETED\_INTEREST",
		- "targeting\_value": "Food and Drinks",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PINNER\_INTEREST",
		- "targeting\_value": "Chocolate Cookies",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AUDIENCE\_INCLUDE",
		- "targeting\_value": 254261234567,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GEO",
		- "targeting\_value": "US:94102",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AGE\_BUCKET",
		- "targeting\_value": "45-49",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "REGION",
		- "targeting\_value": "US-CA",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}}]
}`Get audience sizing
-------------------
Get potential audience size for an ad group with given targeting criteria. 
Potential audience size estimates the number of people you may be able to reach per month with your campaign. 
It is based on historical advertising data and the targeting criteria you select.
It does not guarantee results or take into account factors such as bid, budget, schedule, seasonality or product experiments.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| auto\_targeting\_enabled | boolean Default:  true Enable auto-targeting for ad group. Also known as "expanded targeting".
 |
| placement\_group | string Default:  "ALL" Enum: "ALL" "SEARCH" "BROWSE" "OTHER"  Placement group.
 |
| creative\_types | Array of strings Nullable Items Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"  Pin creative types filter. **Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead.
 |
| targeting\_spec | object (TargetingSpec)  Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":["iphone"], "GENDER":["male"], "LOCALE":["en-US"], "LOCATION":["501"], "AGE\_BUCKET":["25-34"]}
 |
| product\_group\_ids | Array of strings Nullable  Targeted product group IDs. **Note:** This can only be combined with shopping/catalog sales campaigns. For more information, click here. SHOPPING\_RETARGETING must be included in targeting\_spec object or this field will be ignored.
 |
| keywords | Array of objects Nullable  Array of keyword objects. If the keywords field is missing, all keywords will be targeted.
 |
### Responses
**200** Success

**400** Invalid ad group audience sizing parameters.

**403** No access to requested audience list or product group.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/audience\_sizinghttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/audience\_sizing###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "auto\_targeting\_enabled": true,
* "placement\_group": "ALL",
* "creative\_types": [
	+ "REGULAR"],
* "targeting\_spec": {
	+ "AGE\_BUCKET": [
		- "35-44",
		- "50-54"],
	+ "APPTYPE": [
		- "ipad",
		- "iphone"],
	+ "AUDIENCE\_EXCLUDE": [
		- "string"],
	+ "AUDIENCE\_INCLUDE'": [
		- "string"],
	+ "GENDER": [
		- "unknown"],
	+ "GEO": [
		- "string"],
	+ "INTEREST": [
		- "string"],
	+ "LOCALE": [
		- "string"],
	+ "LOCATION": [
		- "string"],
	+ "SHOPPING\_RETARGETING": [
		- {
			* "lookback\_window": 30,
			* "exclusion\_window": 14,
			* "tag\_types": [
				+ 0,
				+ 6]}],
	+ "TARGETING\_STRATEGY": [
		- "CHOOSE\_YOUR\_OWN"]},
* "product\_group\_ids": [
	+ "23423422123"],
* "keywords": [
	+ {
		- "match\_type": "BROAD",
		- "value": "string"}]
}`###  Response samples
* 200
* 400
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "audience\_size\_lower\_bound": 100000,
* "audience\_size\_upper\_bound": 150000
}`Get ad group
------------
Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will
contain additional information from the Ad Review process.
For more information about our policies and rejection reasons see the Pinterest advertising standards.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| ad\_group\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad group.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ad\_groups/{ad\_group\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_groups/{ad\_group\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Ad Group For Pin: 687195905986",
* "status": "ACTIVE",
* "budget\_in\_micro\_currency": 5000000,
* "bid\_in\_micro\_currency": 5000000,
* "optimization\_goal\_metadata": {
	+ "conversion\_tag\_v3\_goal\_metadata": {
		- "attribution\_windows": {
			* "click\_window\_days": 0,
			* "engagement\_window\_days": 0,
			* "view\_window\_days": 0},
		- "conversion\_event": "PAGE\_VISIT",
		- "conversion\_tag\_id": "string",
		- "cpa\_goal\_value\_in\_micro\_currency": "string",
		- "is\_roas\_optimized": true,
		- "learning\_mode\_type": "ACTIVE"},
	+ "frequency\_goal\_metadata": {
		- "frequency": 0,
		- "timerange": "DAY"},
	+ "scrollup\_goal\_metadata": {
		- "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
* "budget\_type": "DAILY",
* "start\_time": 5686848000,
* "end\_time": 5705424000,
* "targeting\_spec": {
	+ "AGE\_BUCKET": [
		- "35-44",
		- "50-54"],
	+ "APPTYPE": [
		- "ipad",
		- "iphone"],
	+ "AUDIENCE\_EXCLUDE": [
		- "string"],
	+ "AUDIENCE\_INCLUDE'": [
		- "string"],
	+ "GENDER": [
		- "unknown"],
	+ "GEO": [
		- "string"],
	+ "INTEREST": [
		- "string"],
	+ "LOCALE": [
		- "string"],
	+ "LOCATION": [
		- "string"],
	+ "SHOPPING\_RETARGETING": [
		- {
			* "lookback\_window": 30,
			* "exclusion\_window": 14,
			* "tag\_types": [
				+ 0,
				+ 6]}],
	+ "TARGETING\_STRATEGY": [
		- "CHOOSE\_YOUR\_OWN"]},
* "lifetime\_frequency\_cap": 100,
* "tracking\_urls": {
	+ "impression": [
		- "URL1",
		- "URL2"],
	+ "click": [
		- "URL1",
		- "URL2"],
	+ "engagement": [
		- "URL1",
		- "URL2"],
	+ "buyable\_button": [
		- "URL1",
		- "URL2"],
	+ "audience\_verification": [
		- "URL1",
		- "URL2"]},
* "auto\_targeting\_enabled": true,
* "placement\_group": "ALL",
* "pacing\_delivery\_type": "STANDARD",
* "campaign\_id": "626736533506",
* "billable\_event": "CLICKTHROUGH",
* "bid\_strategy\_type": "MAX\_BID",
* "id": "2680060704746",
* "ad\_account\_id": "549755885175",
* "created\_time": 1476477189,
* "updated\_time": 1476477189,
* "type": "adgroup",
* "conversion\_learning\_mode\_type": "ACTIVE",
* "summary\_status": "RUNNING",
* "feed\_profile\_id": "626736533506",
* "dca\_assets": null
}`Get bid floors
--------------
List bid floors for your campaign configuration. Bid floors are given in microcurrency values based on the currency in the bid floor specification. 

Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.

A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’ s profile.

**Equivalency equations**, using dollars as an example currency:

* $1 = 1,000,000 microdollars
* 1 microdollar = $0.000001

**To convert between currency and microcurrency**, using dollars as an example currency:

* To convert dollars to microdollars, mutiply dollars by 1,000,000
* To convert microdollars to dollars, divide microdollars by 1,000,000

For more on bid floors see Set your bid. ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Parameters to get bid\_floor info

|  |  |
| --- | --- |
| bid\_floor\_specs required  | Array of objects (bid\_floor\_specs)   |
| targeting\_spec | object (TargetingSpec)  Ad group targeting specification defining the ad group target audience. For example, {"APPTYPE":["iphone"], "GENDER":["male"], "LOCALE":["en-US"], "LOCATION":["501"], "AGE\_BUCKET":["25-34"]}
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/bid\_floorhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bid\_floor###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "targeting\_spec": {
	+ "GEO": [
		- "BE-VOV"],
	+ "LOCATION": [
		- "US"],
	+ "LOCALE": [
		- "cs"],
	+ "AGE\_BUCKET": [
		- "25-34"],
	+ "AUDIENCE\_INCLUDE": [
		- "2542620905473"],
	+ "SHOPPING\_RETARGETING": [
		- {
			* "lookback\_window": 30,
			* "exclusion\_window": 14,
			* "tag\_types": [
				+ 0,
				+ 6]},
		- {
			* "lookback\_window": 30,
			* "exclusion\_window": 14,
			* "tag\_types": [
				+ 0,
				+ 6]}],
	+ "GENDER": [
		- "male"],
	+ "TARGETING\_STRATEGY": [
		- "CHOOSE\_YOUR\_OWN"],
	+ "APPTYPE": [
		- "iphone"],
	+ "AUDIENCE\_EXCLUDE": [
		- "2542620905475"],
	+ "INTEREST": [
		- "925056443165"]},
* "bid\_floor\_specs": [
	+ {
		- "billable\_event": "CLICKTHROUGH",
		- "creative\_type": "REGULAR",
		- "currency": "USD",
		- "countries": [
			* "US",
			* "US"],
		- "optimization\_goal\_metadata": {
			* "frequency\_goal\_metadata": {
				+ "timerange": "DAY",
				+ "frequency": 5},
			* "conversion\_tag\_v3\_goal\_metadata": {
				+ "attribution\_windows": {
					- "view\_window\_days": 1,
					- "click\_window\_days": 0,
					- "engagement\_window\_days": 6},
				+ "conversion\_tag\_id": "123456789",
				+ "learning\_mode\_type": "ACTIVE",
				+ "conversion\_event": "PAGE\_VISIT",
				+ "is\_roas\_optimized": true,
				+ "cpa\_goal\_value\_in\_micro\_currency": "123456789"},
			* "scrollup\_goal\_metadata": {
				+ "scrollup\_goal\_value\_in\_micro\_currency": "123456789"}}},
	+ {
		- "billable\_event": "CLICKTHROUGH",
		- "creative\_type": "REGULAR",
		- "currency": "USD",
		- "countries": [
			* "US",
			* "US"],
		- "optimization\_goal\_metadata": {
			* "frequency\_goal\_metadata": {
				+ "timerange": "DAY",
				+ "frequency": 5},
			* "conversion\_tag\_v3\_goal\_metadata": {
				+ "attribution\_windows": {
					- "view\_window\_days": 1,
					- "click\_window\_days": 0,
					- "engagement\_window\_days": 6},
				+ "conversion\_tag\_id": "123456789",
				+ "learning\_mode\_type": "ACTIVE",
				+ "conversion\_event": "PAGE\_VISIT",
				+ "is\_roas\_optimized": true,
				+ "cpa\_goal\_value\_in\_micro\_currency": "123456789"},
			* "scrollup\_goal\_metadata": {
				+ "scrollup\_goal\_value\_in\_micro\_currency": "123456789"}}}]
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "bid\_floors": [
	+ 100000,
	+ 200000],
* "type": "bidfloor"
}`ads
===
View, create or update ads.

Create ad preview with pin or image
-----------------------------------
Create an ad preview given an ad account ID and either an existing organic pin ID or the URL for an image to be used to create the Pin and the ad. 

If you are creating a preview from an existing Pin, that Pin must be promotable: that is, it must have a clickthrough link and meet other requirements. (See Ads Overview.) 

You can view the returned preview URL on a webpage or iframe for 7 days, after which the URL expires.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Create ad preview with pin or image.

 One of AdPreviewCreateFromImageAdPreviewCreateFromPin
|  |  |
| --- | --- |
| image\_url required  | string (image\_url)  Image URL.
 |
| title required  | string (title)  Title displayed below ad.
 |
### Responses
**200** Successful ad preview creation.

**400** Invalid Pin parameters response

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/ad\_previewshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ad\_previews###  Request samples
* Payload
Content typeapplication/jsonExampleAdPreviewCreateFromImageAdPreviewCreateFromImageAdPreviewCreateFromPinCopy Expand all  Collapse all `{* "image\_url": "https://somewebsite.com/someimage.jpg",
* "title": "My Preview Image"
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "url": "https://ads.pinterest.com/ad-preview/58f1a0e9ab0bd0f99462a0e4c5dd7e8297888c8a36331e88f757abe8f0295d31/"
}`List ads
--------
List ads that meet the filters provided:

* Listed campaign ids or ad group ids or ad ids
* Listed entity statuses 
If no filter is provided, all ads in the ad account are returned. 

**Note:**

Provide only campaign\_id or ad\_group\_id or ad\_id. Do not provide more than one type. 

Review status is provided for each ad; if review\_status is REJECTED, the rejected\_reasons field will contain additional information.
For more, see Pinterest advertising standards.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| campaign\_ids | Array of strings  [ 1 .. 100 ] items  List of Campaign Ids to use to filter the results.
 |
| ad\_group\_ids | Array of strings  [ 1 .. 100 ] items  List of Ad group Ids to use to filter the results.
 |
| ad\_ids | Array of strings  [ 1 .. 100 ] items  List of Ad Ids to use to filter the results.
 |
| entity\_statuses | Array of strings Default:  ["ACTIVE","PAUSED"]Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"   Example:  entity\_statuses=ACTIVEEntity status
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**400** Invalid ad account ads parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/adshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "ad\_group\_id": "2680059592705",
		- "android\_deep\_link": "string",
		- "carousel\_android\_deep\_links": [
			* "string"],
		- "carousel\_destination\_urls": [
			* "string"],
		- "carousel\_ios\_deep\_links": [
			* "string"],
		- "click\_tracking\_url": "string",
		- "creative\_type": "REGULAR",
		- "destination\_url": "string",
		- "ios\_deep\_link": "string",
		- "is\_pin\_deleted": false,
		- "is\_removable": false,
		- "name": "string",
		- "status": "ACTIVE",
		- "tracking\_urls": {
			* "impression": [
				+ "URL1",
				+ "URL2"],
			* "click": [
				+ "URL1",
				+ "URL2"],
			* "engagement": [
				+ "URL1",
				+ "URL2"],
			* "buyable\_button": [
				+ "URL1",
				+ "URL2"],
			* "audience\_verification": [
				+ "URL1",
				+ "URL2"]},
		- "view\_tracking\_url": "string",
		- "lead\_form\_id": "string",
		- "grid\_click\_type": "CLOSEUP",
		- "customizable\_cta\_type": "LEARN\_MORE",
		- "quiz\_pin\_data": {
			* "questions": [
				+ {
					- "question\_id": 1,
					- "question\_text": "Where do you thrive?",
					- "options": [
						* {
							+ "text": "Hangout vibes"},
						* {
							+ "text": "Time to party!"},
						* {
							+ "text": "Keeping it lowkey"}]},
				+ {
					- "question\_id": 2,
					- "question\_text": "Where would you nap?",
					- "options": [
						* {
							+ "text": "Hammock in the mountains"},
						* {
							+ "text": "Beach towel in the sand"},
						* {
							+ "text": "Tent under the stars"}]},
				+ {
					- "question\_id": 2,
					- "question\_text": "Who are you taking?",
					- "options": [
						* {
							+ "text": "No one—solo trip!"},
						* {
							+ "text": "My best friend"},
						* {
							+ "text": "The family"}]}],
			* "results": [
				+ {
					- "organicPinId": "1234",
					- "android\_deep\_link": "https://www.pinterest.com/",
					- "iOS\_deep\_link": "https://www.pinterest.com/",
					- "destination\_url": "https://www.pinterest.com/",
					- "result\_id": 1},
				+ {
					- "organicPinId": "1234",
					- "android\_deep\_link": "https://www.pinterest.com/",
					- "iOS\_deep\_link": "https://www.pinterest.com/",
					- "destination\_url": "https://www.pinterest.com/",
					- "result\_id": 2},
				+ {
					- "organicPinId": "1234",
					- "android\_deep\_link": "https://www.pinterest.com/",
					- "iOS\_deep\_link": "https://www.pinterest.com/",
					- "destination\_url": "https://www.pinterest.com/",
					- "result\_id": 3}]},
		- "pin\_id": "394205773611545468",
		- "ad\_account\_id": "549755885175",
		- "campaign\_id": "626735565838",
		- "collection\_items\_destination\_url\_template": "string",
		- "created\_time": 1451431341,
		- "id": "687195134316",
		- "rejected\_reasons": [
			* "HASHTAGS"],
		- "rejection\_labels": [
			* "string"],
		- "review\_status": "PENDING",
		- "type": "pinpromotion",
		- "updated\_time": 1451431341,
		- "summary\_status": "APPROVED"}],
* "bookmark": "string"
}`Create ads
----------
Create multiple new ads. Request must contain ad\_group\_id, creative\_type, and the source Pin pin\_id.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of ads to create, size limit [1, 30].

 Array ()
|  |  |
| --- | --- |
| ad\_group\_id required  | string^(AG)?\d+$ ID of the ad group that contains the ad.
 |
| android\_deep\_link | string Nullable  Deep link URL for Android devices. Not currently available. Using this field will generate an error.
 |
| carousel\_android\_deep\_links | Array of strings Nullable  Comma-separated deep links for the carousel pin on Android.
 |
| carousel\_destination\_urls | Array of strings Nullable  Comma-separated destination URLs for the carousel pin to promote.
 |
| carousel\_ios\_deep\_links | Array of strings Nullable  Comma-separated deep links for the carousel pin on iOS.
 |
| click\_tracking\_url | string Nullable  Tracking url for the ad clicks.
 |
| creative\_type required  | string (CreativeType)  Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA" "SHOWCASE" "QUIZ"  Ad creative type enum. **Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead.
 |
| destination\_url | string Nullable  Destination URL.
 |
| ios\_deep\_link | string Nullable  Deep link URL for iOS devices. Not currently available. Using this field will generate an error.
 |
| is\_pin\_deleted | boolean Is original pin deleted?
 |
| is\_removable | boolean Is pin repinnable?
 |
| name | string Nullable  Name of the ad - 255 chars max.
 |
| status | string (EntityStatus)  Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Entity status
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see Third-party and dynamic tracking.
 |
| view\_tracking\_url | string Nullable  Tracking URL for ad impressions.
 |
| lead\_form\_id | string Nullable ^(AG)?\d+$ Lead form ID for lead ad generation.
 |
| grid\_click\_type | string (GridClickType)  Nullable  Enum: "CLOSEUP" "DIRECT\_TO\_DESTINATION"  Where a user is taken after clicking on an ad in grid.
 |
| customizable\_cta\_type | string Nullable  Enum: "GET\_OFFER" "LEARN\_MORE" "ORDER\_NOW" "SHOP\_NOW" "SIGN\_UP" "SUBSCRIBE" "BUY\_NOW" "CONTACT\_US" "GET\_QUOTE" "VISIT\_WEBSITE" "APPLY\_NOW" "BOOK\_NOW" "REQUEST\_DEMO" "REGISTER\_NOW" "FIND\_A\_DEALER" "ADD\_TO\_CART" "WATCH\_NOW" "READ\_MORE" null  Select a call to action (CTA) to display below your ad. Available only for ads with direct links enabled. CTA options for consideration and conversion campaigns are LEARN\_MORE, SHOP\_NOW, BOOK\_NOW, SIGN\_UP, VISIT\_WEBSITE, BUY\_NOW, GET\_OFFER, ORDER\_NOW, ADD\_TO\_CART (for conversion campaigns with add to cart conversion events only)
 |
| quiz\_pin\_data | object Nullable  Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved.
 |
| pin\_id required  | string^\d+$ Pin ID.
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/adshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "ad\_group\_id": "2680059592705",
	+ "android\_deep\_link": "string",
	+ "carousel\_android\_deep\_links": [
		- "string"],
	+ "carousel\_destination\_urls": [
		- "string"],
	+ "carousel\_ios\_deep\_links": [
		- "string"],
	+ "click\_tracking\_url": "string",
	+ "creative\_type": "REGULAR",
	+ "destination\_url": "string",
	+ "ios\_deep\_link": "string",
	+ "is\_pin\_deleted": false,
	+ "is\_removable": false,
	+ "name": "string",
	+ "status": "ACTIVE",
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "view\_tracking\_url": "string",
	+ "lead\_form\_id": "string",
	+ "grid\_click\_type": "CLOSEUP",
	+ "customizable\_cta\_type": "LEARN\_MORE",
	+ "quiz\_pin\_data": {
		- "questions": [
			* {
				+ "question\_id": 1,
				+ "question\_text": "Where do you thrive?",
				+ "options": [
					- {
						* "text": "Hangout vibes"},
					- {
						* "text": "Time to party!"},
					- {
						* "text": "Keeping it lowkey"}]},
			* {
				+ "question\_id": 2,
				+ "question\_text": "Where would you nap?",
				+ "options": [
					- {
						* "text": "Hammock in the mountains"},
					- {
						* "text": "Beach towel in the sand"},
					- {
						* "text": "Tent under the stars"}]},
			* {
				+ "question\_id": 2,
				+ "question\_text": "Who are you taking?",
				+ "options": [
					- {
						* "text": "No one—solo trip!"},
					- {
						* "text": "My best friend"},
					- {
						* "text": "The family"}]}],
		- "results": [
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 1},
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 2},
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 3}]},
	+ "pin\_id": "394205773611545468"}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "ad\_group\_id": "2680059592705",
			* "android\_deep\_link": "string",
			* "carousel\_android\_deep\_links": [
				+ "string"],
			* "carousel\_destination\_urls": [
				+ "string"],
			* "carousel\_ios\_deep\_links": [
				+ "string"],
			* "click\_tracking\_url": "string",
			* "creative\_type": "REGULAR",
			* "destination\_url": "string",
			* "ios\_deep\_link": "string",
			* "is\_pin\_deleted": false,
			* "is\_removable": false,
			* "name": "string",
			* "status": "ACTIVE",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "view\_tracking\_url": "string",
			* "lead\_form\_id": "string",
			* "grid\_click\_type": "CLOSEUP",
			* "customizable\_cta\_type": "LEARN\_MORE",
			* "quiz\_pin\_data": {
				+ "questions": [
					- {
						* "question\_id": 1,
						* "question\_text": "Where do you thrive?",
						* "options": [
							+ {
								- "text": "Hangout vibes"},
							+ {
								- "text": "Time to party!"},
							+ {
								- "text": "Keeping it lowkey"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Where would you nap?",
						* "options": [
							+ {
								- "text": "Hammock in the mountains"},
							+ {
								- "text": "Beach towel in the sand"},
							+ {
								- "text": "Tent under the stars"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Who are you taking?",
						* "options": [
							+ {
								- "text": "No one—solo trip!"},
							+ {
								- "text": "My best friend"},
							+ {
								- "text": "The family"}]}],
				+ "results": [
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 1},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 2},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 3}]},
			* "pin\_id": "394205773611545468",
			* "ad\_account\_id": "549755885175",
			* "campaign\_id": "626735565838",
			* "collection\_items\_destination\_url\_template": "string",
			* "created\_time": 1451431341,
			* "id": "687195134316",
			* "rejected\_reasons": [
				+ "HASHTAGS"],
			* "rejection\_labels": [
				+ "string"],
			* "review\_status": "PENDING",
			* "type": "pinpromotion",
			* "updated\_time": 1451431341,
			* "summary\_status": "APPROVED"},
		- "exceptions": {
			* "code": 2,
			* "message": "Advertiser not found."}}]
}`Update ads
----------
Update multiple existing ads

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of ads to update, size limit [1, 30]

 Array ()
|  |  |
| --- | --- |
| ad\_group\_id | string^(AG)?\d+$ ID of the ad group that contains the ad.
 |
| android\_deep\_link | string Nullable  Deep link URL for Android devices. Not currently available. Using this field will generate an error.
 |
| carousel\_android\_deep\_links | Array of strings Nullable  Comma-separated deep links for the carousel pin on Android.
 |
| carousel\_destination\_urls | Array of strings Nullable  Comma-separated destination URLs for the carousel pin to promote.
 |
| carousel\_ios\_deep\_links | Array of strings Nullable  Comma-separated deep links for the carousel pin on iOS.
 |
| click\_tracking\_url | string Nullable  Tracking url for the ad clicks.
 |
| creative\_type | string (CreativeType)  Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA" "SHOWCASE" "QUIZ"  Ad creative type enum. **Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead.
 |
| destination\_url | string Nullable  Destination URL.
 |
| ios\_deep\_link | string Nullable  Deep link URL for iOS devices. Not currently available. Using this field will generate an error.
 |
| is\_pin\_deleted | boolean Is original pin deleted?
 |
| is\_removable | boolean Is pin repinnable?
 |
| name | string Nullable  Name of the ad - 255 chars max.
 |
| status | string (EntityStatus)  Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Entity status
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see Third-party and dynamic tracking.
 |
| view\_tracking\_url | string Nullable  Tracking URL for ad impressions.
 |
| lead\_form\_id | string Nullable ^(AG)?\d+$ Lead form ID for lead ad generation.
 |
| grid\_click\_type | string (GridClickType)  Nullable  Enum: "CLOSEUP" "DIRECT\_TO\_DESTINATION"  Where a user is taken after clicking on an ad in grid.
 |
| customizable\_cta\_type | string Nullable  Enum: "GET\_OFFER" "LEARN\_MORE" "ORDER\_NOW" "SHOP\_NOW" "SIGN\_UP" "SUBSCRIBE" "BUY\_NOW" "CONTACT\_US" "GET\_QUOTE" "VISIT\_WEBSITE" "APPLY\_NOW" "BOOK\_NOW" "REQUEST\_DEMO" "REGISTER\_NOW" "FIND\_A\_DEALER" "ADD\_TO\_CART" "WATCH\_NOW" "READ\_MORE" null  Select a call to action (CTA) to display below your ad. Available only for ads with direct links enabled. CTA options for consideration and conversion campaigns are LEARN\_MORE, SHOP\_NOW, BOOK\_NOW, SIGN\_UP, VISIT\_WEBSITE, BUY\_NOW, GET\_OFFER, ORDER\_NOW, ADD\_TO\_CART (for conversion campaigns with add to cart conversion events only)
 |
| quiz\_pin\_data | object Nullable  Before creating a quiz ad, you must create an organic Pin using POST/Create Pin for each result in the quiz. Quiz ads cannot be saved by a Pinner. Quiz ad results can be saved.
 |
| id required  | string (id) ^\d+$ The ID of this ad.
 |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/adshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "ad\_group\_id": "2680059592705",
	+ "android\_deep\_link": "string",
	+ "carousel\_android\_deep\_links": [
		- "string"],
	+ "carousel\_destination\_urls": [
		- "string"],
	+ "carousel\_ios\_deep\_links": [
		- "string"],
	+ "click\_tracking\_url": "string",
	+ "creative\_type": "REGULAR",
	+ "destination\_url": "string",
	+ "ios\_deep\_link": "string",
	+ "is\_pin\_deleted": false,
	+ "is\_removable": false,
	+ "name": "string",
	+ "status": "ACTIVE",
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "view\_tracking\_url": "string",
	+ "lead\_form\_id": "string",
	+ "grid\_click\_type": "CLOSEUP",
	+ "customizable\_cta\_type": "LEARN\_MORE",
	+ "quiz\_pin\_data": {
		- "questions": [
			* {
				+ "question\_id": 1,
				+ "question\_text": "Where do you thrive?",
				+ "options": [
					- {
						* "text": "Hangout vibes"},
					- {
						* "text": "Time to party!"},
					- {
						* "text": "Keeping it lowkey"}]},
			* {
				+ "question\_id": 2,
				+ "question\_text": "Where would you nap?",
				+ "options": [
					- {
						* "text": "Hammock in the mountains"},
					- {
						* "text": "Beach towel in the sand"},
					- {
						* "text": "Tent under the stars"}]},
			* {
				+ "question\_id": 2,
				+ "question\_text": "Who are you taking?",
				+ "options": [
					- {
						* "text": "No one—solo trip!"},
					- {
						* "text": "My best friend"},
					- {
						* "text": "The family"}]}],
		- "results": [
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 1},
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 2},
			* {
				+ "organicPinId": "1234",
				+ "android\_deep\_link": "https://www.pinterest.com/",
				+ "iOS\_deep\_link": "https://www.pinterest.com/",
				+ "destination\_url": "https://www.pinterest.com/",
				+ "result\_id": 3}]},
	+ "id": "687195134316"}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "ad\_group\_id": "2680059592705",
			* "android\_deep\_link": "string",
			* "carousel\_android\_deep\_links": [
				+ "string"],
			* "carousel\_destination\_urls": [
				+ "string"],
			* "carousel\_ios\_deep\_links": [
				+ "string"],
			* "click\_tracking\_url": "string",
			* "creative\_type": "REGULAR",
			* "destination\_url": "string",
			* "ios\_deep\_link": "string",
			* "is\_pin\_deleted": false,
			* "is\_removable": false,
			* "name": "string",
			* "status": "ACTIVE",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "view\_tracking\_url": "string",
			* "lead\_form\_id": "string",
			* "grid\_click\_type": "CLOSEUP",
			* "customizable\_cta\_type": "LEARN\_MORE",
			* "quiz\_pin\_data": {
				+ "questions": [
					- {
						* "question\_id": 1,
						* "question\_text": "Where do you thrive?",
						* "options": [
							+ {
								- "text": "Hangout vibes"},
							+ {
								- "text": "Time to party!"},
							+ {
								- "text": "Keeping it lowkey"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Where would you nap?",
						* "options": [
							+ {
								- "text": "Hammock in the mountains"},
							+ {
								- "text": "Beach towel in the sand"},
							+ {
								- "text": "Tent under the stars"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Who are you taking?",
						* "options": [
							+ {
								- "text": "No one—solo trip!"},
							+ {
								- "text": "My best friend"},
							+ {
								- "text": "The family"}]}],
				+ "results": [
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 1},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 2},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 3}]},
			* "pin\_id": "394205773611545468",
			* "ad\_account\_id": "549755885175",
			* "campaign\_id": "626735565838",
			* "collection\_items\_destination\_url\_template": "string",
			* "created\_time": 1451431341,
			* "id": "687195134316",
			* "rejected\_reasons": [
				+ "HASHTAGS"],
			* "rejection\_labels": [
				+ "string"],
			* "review\_status": "PENDING",
			* "type": "pinpromotion",
			* "updated\_time": 1451431341,
			* "summary\_status": "APPROVED"},
		- "exceptions": {
			* "code": 2,
			* "message": "Advertiser not found."}}]
}`Get ad analytics
----------------
Get analytics for the specified ads in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| ad\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Ad Ids to use to filter the results.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/analytics###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "DATE": "2021-04-01",
	+ "AD\_ID": "547602124502",
	+ "SPEND\_IN\_DOLLAR": 30,
	+ "TOTAL\_CLICKTHROUGH": 216}
]`Get targeting analytics for ads
-------------------------------
Get targeting analytics for one or more ads. For the requested ad(s) and metrics,
the response will include the requested metric information (e.g. SPEND\_IN\_DOLLAR) for the requested target type
(e.g. "age\_bucket") for applicable values (e.g. "45-49"). 

* The token's user\_account must either be the Owner of the specified ad account, or have one
of the necessary roles granted to them via
Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Ad Ids to use to filter the results.
 |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| targeting\_types required  | Array of strings (AdsAnalyticsTargetingType)   [ 1 .. 15 ] items Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"   Example:  targeting\_types=APPTYPETargeting type breakdowns for the report. The reporting per targeting type  is independent from each other.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
| attribution\_types | string (ConversionReportAttributionType)  Enum: "INDIVIDUAL" "HOUSEHOLD"   Example:  attribution\_types=INDIVIDUALList of types of attribution for the conversion report
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/targeting\_analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/targeting\_analytics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "targeting\_type": "KEYWORD",
		- "targeting\_value": "christmas decor ideas",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "iphone",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "ipad",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_tablet",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GENDER",
		- "targeting\_value": "female",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "LOCATION",
		- "targeting\_value": 500,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PLACEMENT",
		- "targeting\_value": "SEARCH",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "COUNTRY",
		- "targeting\_value": "US",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "TARGETED\_INTEREST",
		- "targeting\_value": "Food and Drinks",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PINNER\_INTEREST",
		- "targeting\_value": "Chocolate Cookies",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AUDIENCE\_INCLUDE",
		- "targeting\_value": 254261234567,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GEO",
		- "targeting\_value": "US:94102",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AGE\_BUCKET",
		- "targeting\_value": "45-49",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "REGION",
		- "targeting\_value": "US-CA",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}}]
}`Get ad
------
Get a specific ad given the ad ID. If your pin is rejected, rejected\_reasons will
contain additional information from the Ad Review process.
For more information about our policies and rejection reasons see the Pinterest advertising standards.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| ad\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads/{ad\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_group\_id": "2680059592705",
* "android\_deep\_link": "string",
* "carousel\_android\_deep\_links": [
	+ "string"],
* "carousel\_destination\_urls": [
	+ "string"],
* "carousel\_ios\_deep\_links": [
	+ "string"],
* "click\_tracking\_url": "string",
* "creative\_type": "REGULAR",
* "destination\_url": "string",
* "ios\_deep\_link": "string",
* "is\_pin\_deleted": false,
* "is\_removable": false,
* "name": "string",
* "status": "ACTIVE",
* "tracking\_urls": {
	+ "impression": [
		- "URL1",
		- "URL2"],
	+ "click": [
		- "URL1",
		- "URL2"],
	+ "engagement": [
		- "URL1",
		- "URL2"],
	+ "buyable\_button": [
		- "URL1",
		- "URL2"],
	+ "audience\_verification": [
		- "URL1",
		- "URL2"]},
* "view\_tracking\_url": "string",
* "lead\_form\_id": "string",
* "grid\_click\_type": "CLOSEUP",
* "customizable\_cta\_type": "LEARN\_MORE",
* "quiz\_pin\_data": {
	+ "questions": [
		- {
			* "question\_id": 1,
			* "question\_text": "Where do you thrive?",
			* "options": [
				+ {
					- "text": "Hangout vibes"},
				+ {
					- "text": "Time to party!"},
				+ {
					- "text": "Keeping it lowkey"}]},
		- {
			* "question\_id": 2,
			* "question\_text": "Where would you nap?",
			* "options": [
				+ {
					- "text": "Hammock in the mountains"},
				+ {
					- "text": "Beach towel in the sand"},
				+ {
					- "text": "Tent under the stars"}]},
		- {
			* "question\_id": 2,
			* "question\_text": "Who are you taking?",
			* "options": [
				+ {
					- "text": "No one—solo trip!"},
				+ {
					- "text": "My best friend"},
				+ {
					- "text": "The family"}]}],
	+ "results": [
		- {
			* "organicPinId": "1234",
			* "android\_deep\_link": "https://www.pinterest.com/",
			* "iOS\_deep\_link": "https://www.pinterest.com/",
			* "destination\_url": "https://www.pinterest.com/",
			* "result\_id": 1},
		- {
			* "organicPinId": "1234",
			* "android\_deep\_link": "https://www.pinterest.com/",
			* "iOS\_deep\_link": "https://www.pinterest.com/",
			* "destination\_url": "https://www.pinterest.com/",
			* "result\_id": 2},
		- {
			* "organicPinId": "1234",
			* "android\_deep\_link": "https://www.pinterest.com/",
			* "iOS\_deep\_link": "https://www.pinterest.com/",
			* "destination\_url": "https://www.pinterest.com/",
			* "result\_id": 3}]},
* "pin\_id": "394205773611545468",
* "ad\_account\_id": "549755885175",
* "campaign\_id": "626735565838",
* "collection\_items\_destination\_url\_template": "string",
* "created\_time": 1451431341,
* "id": "687195134316",
* "rejected\_reasons": [
	+ "HASHTAGS"],
* "rejection\_labels": [
	+ "string"],
* "review\_status": "PENDING",
* "type": "pinpromotion",
* "updated\_time": 1451431341,
* "summary\_status": "APPROVED"
}`audience\_insights
==================
View audience insights.

Get audience insights
---------------------
Get Audience Insights for an ad account. The response will return insights for 3 types of audiences: the
ad account's engaged audience on Pinterest, the ad account's total audience on Pinterest and Pinterest's
total audience.

Learn more about Audience Insights.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| audience\_insight\_type required  | string (AudienceInsightType)  Default:  "YOUR\_TOTAL\_AUDIENCE" Enum: "YOUR\_TOTAL\_AUDIENCE" "YOUR\_ENGAGED\_AUDIENCE" "PINTEREST\_TOTAL\_AUDIENCE"   Example:  audience\_insight\_type=YOUR\_TOTAL\_AUDIENCEType of audience insights.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/audience\_insightshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audience\_insights###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "categories": [
	+ {
		- "key": "1234567",
		- "name": "travel",
		- "ratio": 0.551,
		- "index": 1.2,
		- "id": "1234567",
		- "subcategories": [
			* {
				+ "key": "958862518888",
				+ "name": "travel destinations",
				+ "ratio": 0.482,
				+ "index": 1.2,
				+ "id": "958862518888"}]}],
* "demographics": {
	+ "ages": [
		- {
			* "name": "United States",
			* "key": "us",
			* "ratio": 0.551}],
	+ "genders": [
		- {
			* "name": "United States",
			* "key": "us",
			* "ratio": 0.551}],
	+ "devices": [
		- {
			* "name": "United States",
			* "key": "us",
			* "ratio": 0.551}],
	+ "metros": [
		- {
			* "name": "United States",
			* "key": "us",
			* "ratio": 0.551}],
	+ "countries": [
		- {
			* "name": "United States",
			* "key": "us",
			* "ratio": 0.551}]},
* "type": "YOUR\_TOTAL\_AUDIENCE",
* "date": "2022-10-09",
* "size": 10000,
* "size\_is\_upper\_bound": true
}`Get audience insights scope and type
------------------------------------
Get the scope and type of available audiences, which along with a date, is an audience that has recently had an interaction (referred to here as a type) on pins. Interacted pins can belong to at least the most common **partner** or **Pinterest** scopes. This means that user interactions made on advertiser or partner pins will have the **partner** scope. You can also have user interactions performed in general on Pinterest with the **Pinterest** scope. In that case, you can then use the returned type and scope values together on requests to other endpoints to retrieve insight metrics for a desired audience.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/insights/audienceshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/insights/audiences###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "date": "2022-10-09",
		- "scope": "PARTNER",
		- "type": "IMPRESSION\_PLUS\_ENGAGEMENT"}]
}`audiences
=========
View, create, or update audiences.

List audiences
--------------
Get list of audiences for the ad account.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING” by ID.
For received audiences, it is sorted by sharing event time.
Note that higher-value IDs are associated with more-recently added items.
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ownership\_type | string Default:  "OWNED" Enum: "OWNED" "RECEIVED"   Example:  ownership\_type=OWNED**This feature is currently in beta and not available to all apps.**
Filter audiences by ownership type.
 |
### Responses
**200** Success

**400** Invalid ad account audience parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/audienceshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "ad\_account\_id": "549755885175",
		- "id": "1234",
		- "name": "ACME Tools",
		- "audience\_type": "string",
		- "description": "People who love making quilts.",
		- "rule": {
			* "country": "US",
			* "customer\_list\_id": "5497558859876",
			* "engagement\_domain": [
				+ "www.somedomain.com"],
			* "engagement\_type": "click",
			* "event": "checkout",
			* "event\_data": {
				+ "currency": "USD",
				+ "lead\_type": "Newsletter",
				+ "line\_items": {
					- "product\_brand": "Parker",
					- "product\_category": "Shoes",
					- "product\_id": 1414,
					- "product\_name": "Parker Boots",
					- "product\_price": "99.99",
					- "product\_quantity": 2,
					- "product\_variant": "Red",
					- "product\_variant\_id": "1414-34832"},
				+ "order\_id": "X-151481",
				+ "order\_quantity": 1,
				+ "page\_name": "Our Favorite Pins on Pinterest.",
				+ "promo\_code": "WINTER10",
				+ "property": "Athleta",
				+ "search\_query": "boots",
				+ "value": "199.98",
				+ "video\_title": "How to style your Parker Boots"},
			* "percentage": 3,
			* "pin\_id": [
				+ "34567"],
			* "prefill": true,
			* "retention\_days": 30,
			* "seed\_id": [
				+ "2542620639259",
				+ "2542620639261"],
			* "url": [
				+ "string"],
			* "visitor\_source\_id": "549755885175",
			* "event\_source": {
				+ "=": [
					- "web",
					- "mobile"]},
			* "ingestion\_source": {
				+ "=": [
					- "tag"]},
			* "engager\_type": 1,
			* "campaign\_id": [
				+ "626744528398"],
			* "ad\_id": [
				+ "687201361754"],
			* "objective\_type": [
				+ "AWARENESS"],
			* "ad\_account\_id": "549755885175"},
		- "size": 1000,
		- "status": "string",
		- "type": "audience",
		- "created\_timestamp": 1451431341,
		- "updated\_timestamp": 1451431341}],
* "bookmark": "string"
}`Create audience
---------------
Create an audience you can use in targeting for specific ad groups. Targeting combines customer information with
the ways users interact with Pinterest to help you reach specific groups of users; you can include or exclude
specific audience\_ids when you create an ad group. 

For more, see Audience targeting.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of ads to create, size limit [1, 30]

|  |  |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\d+$ Ad account ID.
 |
| name required  | string (name)  Audience name.
 |
| rule required  | object (Rule)  JSON object defining targeted audience users. Example rule formats per audience type:CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}ACTALIKE: { "seed\_id": ["<audience ID>"], "country": "US", "percentage": "10" }(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.The targeted audience should be this % size across Pinterest.)VISITOR: { "visitor\_source\_id": ["<conversion tag ID>"], "retention\_days": "180", "event\_source": {"=": ["web", "mobile"]}, "ingestion\_source": {"=": ["tag"]}}(Retention days should be 1-540. Retention applies to specific customers.)ENGAGEMENT: {"engagement\_domain": ["www.entomi.com"], "engager\_type": 1}For more details on engagement audiences, see November 2021 changelog.
 |
| description | string (description)  Audience description.
 |
| audience\_type required  | string Enum: "CUSTOMER\_LIST" "VISITOR" "ENGAGEMENT" "ACTALIKE" "PERSONA"  Audience type
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/audienceshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "name": "string",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "description": "string",
* "audience\_type": "string"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "id": "1234",
* "name": "ACME Tools",
* "audience\_type": "string",
* "description": "People who love making quilts.",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "size": 1000,
* "status": "string",
* "type": "audience",
* "created\_timestamp": 1451431341,
* "updated\_timestamp": 1451431341
}`Create custom audience
----------------------
Create a custom audience and find the audiences you want your ads to reach.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Custom audience to create.

|  |  |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\d+$ Ad account ID.
 |
| name required  | string (name)  Audience name.
 |
| rule required  | object (Rule)  JSON object defining targeted audience users. Example rule formats per audience type:CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}ACTALIKE: { "seed\_id": ["<audience ID>"], "country": "US", "percentage": "10" }(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.The targeted audience should be this % size across Pinterest.)VISITOR: { "visitor\_source\_id": ["<conversion tag ID>"], "retention\_days": "180", "event\_source": {"=": ["web", "mobile"]}, "ingestion\_source": {"=": ["tag"]}}(Retention days should be 1-540. Retention applies to specific customers.)ENGAGEMENT: {"engagement\_domain": ["www.entomi.com"], "engager\_type": 1}For more details on engagement audiences, see November 2021 changelog.
 |
| sharing\_type required  | string (AudienceSharingType)  Enum: "CUSTOM" "SYNDICATED"  Audience sharing type: ["CUSTOM", "SYNDICATED"]
 |
| data\_party required  | string (AudienceDataParty)  Enum: "1p" "3p"  Whether the data is owned by the partner (1p) or by the data provider (3p)
 |
| category | string  |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/audiences/customhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/custom###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "name": "string",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "sharing\_type": "CUSTOM",
* "data\_party": "1p",
* "category": "DLX Demographics"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "id": "1234",
* "name": "ACME Tools",
* "audience\_type": "string",
* "description": "People who love making quilts.",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "size": 1000,
* "status": "string",
* "type": "audience",
* "created\_timestamp": 1451431341,
* "updated\_timestamp": 1451431341
}`Get audience
------------
Get a specific audience given the audience ID.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| audience\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an audience
 |
### Responses
**200** Success

**404** Audience not found.

**default** Unexpected error.

get/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "id": "1234",
* "name": "ACME Tools",
* "audience\_type": "string",
* "description": "People who love making quilts.",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "size": 1000,
* "status": "string",
* "type": "audience",
* "created\_timestamp": 1451431341,
* "updated\_timestamp": 1451431341
}`Update audience
---------------
Update (edit or remove) an existing targeting audience.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| audience\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an audience
 |
##### Request Body schema: application/json
The audience to be updated.

|  |  |
| --- | --- |
| ad\_account\_id | string (ad\_account\_id) ^\d+$ Ad account ID.
 |
| name | string (name)  Audience name.
 |
| rule | object (Rule)  JSON object defining targeted audience users. Example rule formats per audience type:CUSTOMER\_LIST: { "customer\_list\_id": "<customer list ID>"}ACTALIKE: { "seed\_id": ["<audience ID>"], "country": "US", "percentage": "10" }(Valid countries include: "US", "CA", and "GB". Percentage should be 1-10.The targeted audience should be this % size across Pinterest.)VISITOR: { "visitor\_source\_id": ["<conversion tag ID>"], "retention\_days": "180", "event\_source": {"=": ["web", "mobile"]}, "ingestion\_source": {"=": ["tag"]}}(Retention days should be 1-540. Retention applies to specific customers.)ENGAGEMENT: {"engagement\_domain": ["www.entomi.com"], "engager\_type": 1}For more details on engagement audiences, see November 2021 changelog.
 |
| description | string (description)  Audience description.
 |
| operation\_type | string (operation\_type)  Default:  "UPDATE" Enum: "UPDATE" "REMOVE"  Audience operation type (update or remove).
 |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/audiences/{audience\_id}###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "name": "string",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "description": "string",
* "operation\_type": "UPDATE"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "id": "1234",
* "name": "ACME Tools",
* "audience\_type": "string",
* "description": "People who love making quilts.",
* "rule": {
	+ "country": "US",
	+ "customer\_list\_id": "5497558859876",
	+ "engagement\_domain": [
		- "www.somedomain.com"],
	+ "engagement\_type": "click",
	+ "event": "checkout",
	+ "event\_data": {
		- "currency": "USD",
		- "lead\_type": "Newsletter",
		- "line\_items": {
			* "product\_brand": "Parker",
			* "product\_category": "Shoes",
			* "product\_id": 1414,
			* "product\_name": "Parker Boots",
			* "product\_price": "99.99",
			* "product\_quantity": 2,
			* "product\_variant": "Red",
			* "product\_variant\_id": "1414-34832"},
		- "order\_id": "X-151481",
		- "order\_quantity": 1,
		- "page\_name": "Our Favorite Pins on Pinterest.",
		- "promo\_code": "WINTER10",
		- "property": "Athleta",
		- "search\_query": "boots",
		- "value": "199.98",
		- "video\_title": "How to style your Parker Boots"},
	+ "percentage": 3,
	+ "pin\_id": [
		- "34567"],
	+ "prefill": true,
	+ "retention\_days": 30,
	+ "seed\_id": [
		- "2542620639259",
		- "2542620639261"],
	+ "url": [
		- "string"],
	+ "visitor\_source\_id": "549755885175",
	+ "event\_source": {
		- "=": [
			* "web",
			* "mobile"]},
	+ "ingestion\_source": {
		- "=": [
			* "tag"]},
	+ "engager\_type": 1,
	+ "campaign\_id": [
		- "626744528398"],
	+ "ad\_id": [
		- "687201361754"],
	+ "objective\_type": [
		- "AWARENESS"],
	+ "ad\_account\_id": "549755885175"},
* "size": 1000,
* "status": "string",
* "type": "audience",
* "created\_timestamp": 1451431341,
* "updated\_timestamp": 1451431341
}`billing
=======
View, create, or update information related to billing.

Get ads credit discounts
------------------------
Returns the list of discounts applied to the account.

**This endpoint might not be available to all apps. Learn more.**

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read``billing:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**default** Unexpected error.

get/ad\_accounts/{ad\_account\_id}/ads\_credit/discountshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads\_credit/discounts###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "active": true,
		- "advertiser\_id": "12312451231",
		- "discountType": "COUPON",
		- "discountInMicroCurrency": 125000000,
		- "discountCurrency": "USD",
		- "title": "Ads Credits",
		- "remainingDiscountInMicroCurrency": 125000000}],
* "bookmark": "string"
}`Redeem ad credits
-----------------
Redeem ads credit on behalf of the ad account id and apply it towards billing.

**This endpoint might not be available to all apps. Learn more.**

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write``billing:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Redeem ad credits request.

|  |  |
| --- | --- |
| offerCodeHash required  | string^[a-z0-9]\*$ Takes in a SHA256 hash of the offerCode.
 |
| validateOnly required  | boolean If true, only validate if we can redeem offer code. Otherwise it will actually apply the offer code to the account
 |
### Responses
**200** Successfully redeemed ad credits.

**400** Error thrown when unable to redeem offer code.

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/ads\_credit/redeemhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ads\_credit/redeem###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "offerCodeHash": "138e9e0ff7e38cf511b880975eb574c09aa9d5e1657590ab0431040da68caa67",
* "validateOnly": true
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "success": false,
* "errorCode": 2708,
* "errorMessage": "The offer has already been redeemed by this advertiser"
}`Get billing profiles
--------------------
Get billing profiles in the advertiser account.

**This endpoint might not be available to all apps. Learn more.**

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read``billing:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| is\_active required  | boolean Return active billing profiles, if false return all billing profiles.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**default** Unexpected error.

get/ad\_accounts/{ad\_account\_id}/billing\_profileshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/billing\_profiles###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "12312451231",
		- "card\_type": "VISA",
		- "status": "INVALID",
		- "advertiser\_id": "12312451231",
		- "payment\_method\_brand": "VISA"}],
* "bookmark": "string"
}`Get Salesforce account details including bill-to information.
-------------------------------------------------------------
Get Salesforce account details including bill-to information to be used in insertion orders process for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid request parameter.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/accountshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/accounts###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "eligible": true,
* "can\_edit": true,
* "billto\_infos": [
	+ {
		- "id": "0011N00001LW8kAQAT",
		- "io\_terms\_id": "a2S1N000000bKHgUAM",
		- "io\_terms": "The IO is governed by the terms available at https://business.pinterest.com/en/pinterest-advertising-services-agreement/. If a budget is listed on this IO, the parties agree that Advertiser (or if applicable, its Agency) may apply any of the budget to any auction bid type or ad product. Price will be determined by auction closing price, plus any applicable non-auction fees. The terms of the Agreement supersede any terms on this IO. ANY ADDITIONAL TERMS AND CONDITIONS ON THIS IO ARE NULL AND VOID.",
		- "us\_terms\_id": "a2S1N000000bKIOUA2",
		- "us\_terms": "This Insertion Order (\"IO\") is subject to the Pinterest Addendum To IAB Standard Terms and Conditions for Internet Advertising For Media Buys One Year or Less (Version 3.0), as executed by Pinterest, Inc. and GroupM Worldwide LLC on May 7, 2014 and Amendment No. 1 to Pinterest Addendum to IAB Standard Terms and Conditions for Internet Advertising For Media Buys One Year or Less (Version 3.0) as executed by Pinterest, Inc. and GroupM Worldwide LLC on August 20, 2015. The parties agree that Agency may apply any of the budget listed on this IO to any auction bid type or ad product. Price will be determined by auction closing price, plus any applicable non-auction fees.The terms of the Addendum supersede any terms on this IO. ANY ADDITIONAL TERMS AND CONDITIONS ON THIS IO ARE NULL AND VOID.",
		- "row\_terms\_id": "a2S1N000000bKHhUAM",
		- "row\_terms": "The IO is governed by the terms available at\r\nhttps://business.pinterest.com/en-gb/pinterest-advertising-services-agreement",
		- "io\_type": "Pinterest Paper",
		- "addresses": [
			* {
				+ "display": "475 Brannan Street, San Francisco, CA 94103",
				+ "purpose": "Billing",
				+ "address\_id": "a1C1N000004MUrLUAW",
				+ "order\_legal\_entity": "PIN US OU"}]}],
* "currency": "USD",
* "pmp\_names": [
	+ {
		- "name": "Bidalgo",
		- "id": "0011N00001LW2aSQAT"}],
* "error": "No Error"
}`Create insertion order through SSIO.
------------------------------------
Create insertion order through SSIO for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Order line to create.

|  |  |
| --- | --- |
| start\_date required  | string^(\d{4})-(\d{2})-(\d{2})$ Starting date of time period. Format: YYYY-MM-DD
 |
| end\_date | string^(\d{4})-(\d{2})-(\d{2})$ End date of time period. Format: YYYY-MM-DD
 |
| po\_number required  | string The po number
 |
| budget\_amount | number If Budget order line, the budget amount.
 |
| billing\_contact\_firstname required  | string The billing contact first name
 |
| billing\_contact\_lastname required  | string The billing contact last name
 |
| billing\_contact\_email required  | string The billing contact email
 |
| media\_contact\_firstname required  | string The media contact first name
 |
| media\_contact\_lastname required  | string The media contact last name
 |
| media\_contact\_email required  | string The media contact email
 |
| agency\_link | string URL link for agency
 |
| user\_email | string The email of user submitting the insertion order
 |
| accepted\_terms\_time | integer The UTC timestamp (to the nearest sec) of when terms were accepted
 |
| pmp\_id required  | string The pmp id
 |
| order\_name required  | string The order name
 |
| order\_line\_type required  | string Enum: "BUDGET" "PERPETUALS"  Type can be Budget or Perpetual
 |
| accepted\_terms\_id required  | string The SFDC id for the terms
 |
| billto\_company\_id required  | string The bill-to company id
 |
| billto\_business\_address\_id required  | string The bill-to business address id
 |
| billto\_billing\_address\_id required  | string The bill-to billing address id
 |
| estimated\_monthly\_spend | number If Ongoing (perpetual) order line, the estimated monthly spend
 |
| currency\_info required  | string (Currency)  Enum: "UNK" "USD" "GBP" "CAD" "EUR" "AUD" "NZD" "SEK" "ILS" "CHF" "HKD" "JPY" "SGD" "KRW" "NOK" "DKK" "PLN" "RON" "HUF" "CZK" … 5 more Currency Codes from ISO 4217
 |
### Responses
**200** Success

**400** Invalid request.

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/ssio/insertion\_ordershttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "start\_date": "2020-12-20",
* "end\_date": "2020-12-20",
* "po\_number": "string",
* "budget\_amount": 5000000,
* "billing\_contact\_firstname": "string",
* "billing\_contact\_lastname": "string",
* "billing\_contact\_email": "test@example",
* "media\_contact\_firstname": "string",
* "media\_contact\_lastname": "string",
* "media\_contact\_email": "test@example",
* "agency\_link": "string",
* "user\_email": "test@example",
* "accepted\_terms\_time": 0,
* "pmp\_id": "string",
* "order\_name": "string",
* "order\_line\_type": "BUDGET",
* "accepted\_terms\_id": "string",
* "billto\_company\_id": "string",
* "billto\_business\_address\_id": "string",
* "billto\_billing\_address\_id": "string",
* "estimated\_monthly\_spend": 0,
* "currency\_info": "USD"
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "pin\_order\_id": "string"
}`Edit insertion order through SSIO.
----------------------------------
Edit insertion order through SSIO for `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Order line to create.

|  |  |
| --- | --- |
| start\_date | string^(\d{4})-(\d{2})-(\d{2})$ Starting date of time period. Format: YYYY-MM-DD
 |
| end\_date | string^(\d{4})-(\d{2})-(\d{2})$ End date of time period. Format: YYYY-MM-DD
 |
| po\_number | string The po number
 |
| budget\_amount | number If Budget order line, the budget amount.
 |
| billing\_contact\_firstname | string The billing contact first name
 |
| billing\_contact\_lastname | string The billing contact last name
 |
| billing\_contact\_email | string The billing contact email
 |
| media\_contact\_firstname | string The media contact first name
 |
| media\_contact\_lastname | string The media contact last name
 |
| media\_contact\_email | string The media contact email
 |
| agency\_link | string URL link for agency
 |
| user\_email | string The email of user submitting the insertion order
 |
| oracle\_line\_id | string LineId in the Oracle DB
 |
| salesforce\_order\_id | string OrderId in SFDC
 |
| salesforce\_order\_line\_id | string OrderLineId in SFDC
 |
| ads\_manager\_order\_line\_id | string Ads manager OrderLineId
 |
### Responses
**200** Success

**400** Invalid request.

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/ssio/insertion\_ordershttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "start\_date": "2020-12-20",
* "end\_date": "2020-12-20",
* "po\_number": "string",
* "budget\_amount": 5000000,
* "billing\_contact\_firstname": "string",
* "billing\_contact\_lastname": "string",
* "billing\_contact\_email": "test@example",
* "media\_contact\_firstname": "string",
* "media\_contact\_lastname": "string",
* "media\_contact\_email": "test@example",
* "agency\_link": "string",
* "user\_email": "test@example",
* "oracle\_line\_id": "string",
* "salesforce\_order\_id": "string",
* "salesforce\_order\_line\_id": "string",
* "ads\_manager\_order\_line\_id": "string"
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "pin\_order\_id": "string"
}`Get insertion order status by ad account id.
--------------------------------------------
Get insertion order status for account id `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**400** Invalid request parameter.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/statushttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/status###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "pin\_order\_id": "0Q01N0000015hekSAB",
		- "status": "Approved",
		- "creation\_time": "2017-06-21T23:11:11.000Z"}],
* "bookmark": "string"
}`Get insertion order status by pin order id.
-------------------------------------------
Get insertion order status for pin order id `pin_order_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| pin\_order\_id required  | string  Example:  0Q01N0000015hekSVDFDCThe pin order id associated with the ssio insertion order
 |
### Responses
**200** Success

**400** Invalid request parameter.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/{pin\_order\_id}/statushttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/insertion\_orders/{pin\_order\_id}/status###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "pin\_order\_id": "0Q01N0000015hekSAB",
* "status": "Approved",
* "creation\_time": "2017-06-21T23:11:11.000Z"
}`Get Salesforce order lines by ad account id.
--------------------------------------------
Get Salesforce order lines for account id `ad_account_id`.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Finance, Campaign.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| pin\_order\_id | string  Example:  pin\_order\_id=0Q01N0000015hekSVDFDCThe pin order id associated with the ssio insertino order
 |
### Responses
**200** Success

**400** Invalid request parameter.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/ssio/order\_lineshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/ssio/order\_lines###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "salesforce\_order\_line\_id": "string",
		- "ads\_manager\_order\_line\_id": "string",
		- "pin\_order\_id": "string",
		- "last\_modified\_date\_time": "2020-10-06T13:07:04.000Z",
		- "start\_date": "2018-03-01",
		- "end\_date": "2020-10-05",
		- "bill\_to\_company\_name": "Home Depot Inc.",
		- "billing\_contact\_firstname": "Mary",
		- "billing\_contact\_lastname": "Smith",
		- "billing\_contact\_email": "mail@test.com",
		- "media\_contact\_email": "mail@test.com",
		- "media\_contact\_firstname": "John",
		- "media\_contact\_lastname": "Doe",
		- "currency\_info": "USD",
		- "agency\_link": "",
		- "po\_number": "string",
		- "order\_name": "string",
		- "pmp\_name": "string",
		- "accepted\_terms\_id": "string",
		- "accepted\_terms\_time": "2020-10-06T13:07:04.000Z",
		- "budget\_amount": 5000000,
		- "estimated\_monthly\_spend": 0}],
* "bookmark": "string"
}`boards
======
View, create, update, or delete information about boards.

List boards
-----------
Get a list of the boards owned by the "operation user\_account" + group boards where this account is a collaborator
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
Optional: Specify a privacy type (public, protected, or secret) to indicate which boards to return.

* If no privacy is specified, all boards that can be returned (based on the scopes of the token and ad\_account role if applicable) will be returned.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| privacy | string Enum: "ALL" "PROTECTED" "PUBLIC" "SECRET" "PUBLIC\_AND\_SECRET"  Privacy setting for a board.
 |
### Responses
**200** response

**default** Unexpected error

get/boardshttps://api.pinterest.com/v5/boards###  Request samples
* curl
* curl (Sandbox)
Copy
```
curl --location --request GET 'https://api.pinterest.com/v5/boards' \
--header 'Authorization: Bearer <Add your token here>' \
--header 'Content-Type: application/json'
```
###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "549755885175",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
		- "name": "Summer Recipes",
		- "description": "My favorite summer recipes",
		- "collaborator\_count": 17,
		- "pin\_count": 5,
		- "follower\_count": 13,
		- "media": {
			* "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
			* "pin\_thumbnail\_urls": [
				+ "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
				+ "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
				+ "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
				+ "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
		- "owner": {
			* "username": "string"},
		- "privacy": "PUBLIC"}],
* "bookmark": "string"
}`Create board
------------
Create a board owned by the "operation user\_account".
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Create a board using a single board json object.

|  |  |
| --- | --- |
| name required  | string  |
| description | string Nullable   |
| privacy | string Default:  "PUBLIC" Enum: "PUBLIC" "PROTECTED" "SECRET"  Privacy setting for a board. Learn more about secret boards and protected boards
 |
### Responses
**201** response

**400** The board name is invalid or duplicated.

**default** Unexpected error

post/boardshttps://api.pinterest.com/v5/boards###  Request samples
* Payload
* Python SDK
* curl
* curl (Sandbox)
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Summer Recipes",
* "description": "My favorite summer recipes",
* "privacy": "PUBLIC"
}`###  Response samples
* 201
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
* "name": "Summer Recipes",
* "description": "My favorite summer recipes",
* "collaborator\_count": 17,
* "pin\_count": 5,
* "follower\_count": 13,
* "media": {
	+ "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
	+ "pin\_thumbnail\_urls": [
		- "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
		- "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
		- "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
		- "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
* "owner": {
	+ "username": "string"},
* "privacy": "PUBLIC"
}`Get board
---------
Get a board owned by the operation user\_account - or a group board that has been shared with this account.

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** response

**404** Board not found.

**default** Unexpected error

get/boards/{board\_id}https://api.pinterest.com/v5/boards/{board\_id}###  Request samples
* Python SDK
* curl
* curl (Sandbox)
Copy
```
# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started
from pinterest.organic.boards import Board
# Board information can be fetched from profile page or from create/list board method here:
# https://developers.pinterest.com/docs/api/v5/#operation/boards/list
BOARD_ID="<Add your board id here>"
board_get = Board(board_id=BOARD_ID)
print("Board Id: %s, Board name:%s"%(board_get.id, board_get.name))
```
###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
* "name": "Summer Recipes",
* "description": "My favorite summer recipes",
* "collaborator\_count": 17,
* "pin\_count": 5,
* "follower\_count": 13,
* "media": {
	+ "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
	+ "pin\_thumbnail\_urls": [
		- "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
		- "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
		- "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
		- "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
* "owner": {
	+ "username": "string"},
* "privacy": "PUBLIC"
}`Update board
------------
Update a board owned by the "operating user\_account".

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Update a board.

|  |  |
| --- | --- |
| name | string  |
| description | string Nullable   |
| privacy | string Enum: "PUBLIC" "SECRET"   |
### Responses
**200** response

**400** Invalid board parameters.

**403** Not authorized to update the board.

**429** This request exceeded a rate limit. This can happen if the client exceeds one
of the published rate limits or if multiple write operations are applied to
an object within a short time window.

**default** Unexpected error

patch/boards/{board\_id}https://api.pinterest.com/v5/boards/{board\_id}###  Request samples
* Payload
* Python SDK
* curl
* curl (Sandbox)
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Summer Recipes",
* "description": "My favorite summer recipes",
* "privacy": "PUBLIC"
}`###  Response samples
* 200
* 400
* 403
* 429
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
* "name": "Summer Recipes",
* "description": "My favorite summer recipes",
* "collaborator\_count": 17,
* "pin\_count": 5,
* "follower\_count": 13,
* "media": {
	+ "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
	+ "pin\_thumbnail\_urls": [
		- "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
		- "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
		- "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
		- "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
* "owner": {
	+ "username": "string"},
* "privacy": "PUBLIC"
}`Delete board
------------
Delete a board owned by the "operation user\_account".

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**204** Board deleted successfully

**403** Not authorized to delete the board.

**404** Board not found.

**409** Could not get exclusive access to delete the board.

**429** This request exceeded a rate limit. This can happen if the client exceeds one
of the published rate limits or if multiple write operations are applied to
an object within a short time window.

**default** Unexpected error

delete/boards/{board\_id}https://api.pinterest.com/v5/boards/{board\_id}###  Request samples
* Python SDK
* curl
* curl (Sandbox)
Copy
```
# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started
from pinterest.organic.boards import Board
# Board information can be fetched from profile page or from create/list board method here:
# https://developers.pinterest.com/docs/api/v5/#operation/boards/list
BOARD_ID="<Add your board id here>"
board_delete=Board.delete(board_id=BOARD_ID)
print("Board was deleted? %s" % (board_delete))
```
###  Response samples
* 403
* 404
* 409
* 429
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 403,
* "message": "Not authorized to delete the board."
}`List Pins on board
------------------
Get a list of the Pins on a board owned by the "operation user\_account" - or on a group board that has been shared with this account.

* Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".
* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| creative\_types | Array of stringsItems Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"   Example:  creative\_types=REGULARPin creative types filter. **Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| pin\_metrics | boolean Default:  false Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then.
 |
### Responses
**200** response

**404** Board not found.

**default** Unexpected error

get/boards/{board\_id}/pinshttps://api.pinterest.com/v5/boards/{board\_id}/pins###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "813744226420795884",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "link": "https://www.pinterest.com/",
		- "title": "string",
		- "description": "string",
		- "dominant\_color": "#6E7874",
		- "alt\_text": "string",
		- "creative\_type": "REGULAR",
		- "board\_id": "string",
		- "board\_section\_id": "string",
		- "board\_owner": {
			* "username": "string"},
		- "is\_owner": true,
		- "media": {
			* "media\_type": "string"},
		- "parent\_pin\_id": "string",
		- "is\_standard": true,
		- "has\_been\_promoted": true,
		- "note": "string",
		- "pin\_metrics": {
			* "pin\_metrics": [
				+ {
					- "90d": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3},
					- "all\_time": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3,
						* "reaction": 10,
						* "comment": 2}},
				+ null]}}],
* "bookmark": "string"
}`List board sections
-------------------
Get a list of all board sections from a board owned by the "operation user\_account" - or a group board that has been shared with this account.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** response

**default** Unexpected error

get/boards/{board\_id}/sectionshttps://api.pinterest.com/v5/boards/{board\_id}/sections###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "549755885175",
		- "name": "Salads"}],
* "bookmark": "string"
}`Create board section
--------------------
Create a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Create a board section.

|  |  |
| --- | --- |
| name required  | string  [ 1 .. 180 ] characters   |
### Responses
**201** response

**400** Invalid board section parameters.

**403** Not authorized to create board sections.

**409** Could not get exclusive access to the board to create a new section.

**500** Could not create a new board section.

**default** Unexpected error

post/boards/{board\_id}/sectionshttps://api.pinterest.com/v5/boards/{board\_id}/sections###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Salads"
}`###  Response samples
* 201
* 400
* 403
* 409
* 500
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "name": "Salads"
}`Update board section
--------------------
Update a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
| section\_id required  | string^\d+$ Unique identifier of a board section.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Update a board section.

|  |  |
| --- | --- |
| name required  | string  [ 1 .. 180 ] characters   |
### Responses
**200** response

**400** Invalid board section parameters.

**403** Not authorized to update board section.

**409** Board section conflict.

**default** Unexpected error

patch/boards/{board\_id}/sections/{section\_id}https://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Salads"
}`###  Response samples
* 200
* 400
* 403
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "name": "Salads"
}`Delete board section
--------------------
Delete a board section on a board owned by the "operation user\_account" - or on a group board that has been shared with this account.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
| section\_id required  | string^\d+$ Unique identifier of a board section.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**204** Board section deleted successfully

**403** Not authorized to delete board section.

**404** Board section not found.

**409** Board section conflict.

**default** Unexpected error

delete/boards/{board\_id}/sections/{section\_id}https://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}###  Response samples
* 403
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 403,
* "message": "Not authorized to delete board section."
}`List Pins on board section
--------------------------
Get a list of the Pins on a board section of a board owned by the "operation user\_account" - or on a group board that has been shared with this account.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| board\_id required  | string^\d+$ Unique identifier of a board.
 |
| section\_id required  | string^\d+$ Unique identifier of a board section.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** response

**403** Not authorized to access Pins on board section.

**404** Board or section not found.

**409** Board section conflict.

**default** Unexpected error

get/boards/{board\_id}/sections/{section\_id}/pinshttps://api.pinterest.com/v5/boards/{board\_id}/sections/{section\_id}/pins###  Response samples
* 200
* 403
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "813744226420795884",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "link": "https://www.pinterest.com/",
		- "title": "string",
		- "description": "string",
		- "dominant\_color": "#6E7874",
		- "alt\_text": "string",
		- "creative\_type": "REGULAR",
		- "board\_id": "string",
		- "board\_section\_id": "string",
		- "board\_owner": {
			* "username": "string"},
		- "is\_owner": true,
		- "media": {
			* "media\_type": "string"},
		- "parent\_pin\_id": "string",
		- "is\_standard": true,
		- "has\_been\_promoted": true,
		- "note": "string",
		- "pin\_metrics": {
			* "pin\_metrics": [
				+ {
					- "90d": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3},
					- "all\_time": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3,
						* "reaction": 10,
						* "comment": 2}},
				+ null]}}],
* "bookmark": "string"
}`bulk
====
Create, update, or download ads-related entities in bulk.

Get advertiser entities in bulk
-------------------------------
Create an asynchronous report that may include information on campaigns, ad groups, product groups, ads,
and/or keywords; can filter by campaigns. Though the entities may be active, archived, or paused,
only active entities will return data.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Parameters to get ad entities in bulk

|  |  |
| --- | --- |
| entity\_types | Array of strings  [ 1 .. 5 ] items Items Enum: "CAMPAIGN" "AD\_GROUP" "PRODUCT\_GROUP" "AD" "KEYWORD"  All entity types specified will be downloaded. Fewer types result in faster downloads.
 |
| entity\_ids | Array of strings All entities specified by these IDs as well as their children and grandchildren will be downloaded if the entity type is one of the types requested to be downloaded.
 |
| updated\_since | string^\d+$ Unix UTC timestamp to retrieve all entities that have changed since this time.
 |
| campaign\_filter | object  |
| output\_format | string Default:  "JSON" Enum: "CSV" "JSON"  Bulk file output format
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/bulk/downloadhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/download###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "entity\_types": [
	+ "CAMPAIGN",
	+ "AD\_GROUP"],
* "entity\_ids": [
	+ "string"],
* "updated\_since": "1622848072",
* "campaign\_filter": {
	+ "start\_time": "1622848072",
	+ "end\_time": "1622848072",
	+ "name": "campaign name",
	+ "campaign\_status": [
		- "RUNNING"],
	+ "objective\_type": [
		- "AWARENESS"]},
* "output\_format": "CSV"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "request\_id": "2680059592705"
}`Create/update ad entities in bulk
---------------------------------
Either create or update any combination of campaigns, ad groups, product groups, ads, or keywords.
Note that this request will be processed asynchronously; the response will include a `request_id`
that can be used to obtain the status of the request.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Parameters to get create/update ad entities in bulk

|  |  |
| --- | --- |
| create | object (BulkUpsertRequestCreate)  Request for creation of entities in bulk.
 |
| update | object (BulkUpsertRequestUpdate)  Request for creation of entities in bulk.
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/bulk/upserthttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/upsert###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "create": {
	+ "campaigns": [
		- {
			* "ad\_account\_id": "549755885175",
			* "name": "ACME Tools",
			* "status": "ACTIVE",
			* "lifetime\_spend\_cap": 1432744744,
			* "daily\_spend\_cap": 1432744744,
			* "order\_line\_id": "549755885175",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "start\_time": 1580865126,
			* "end\_time": 1644023526,
			* "summary\_status": "RUNNING",
			* "is\_flexible\_daily\_budgets": true,
			* "default\_ad\_group\_budget\_in\_micro\_currency": 0,
			* "is\_automated\_campaign": true,
			* "objective\_type": "AWARENESS"}],
	+ "ad\_groups": [
		- {
			* "name": "Ad Group For Pin: 687195905986",
			* "status": "ACTIVE",
			* "budget\_in\_micro\_currency": 5000000,
			* "bid\_in\_micro\_currency": 5000000,
			* "optimization\_goal\_metadata": {
				+ "conversion\_tag\_v3\_goal\_metadata": {
					- "attribution\_windows": {
						* "click\_window\_days": 0,
						* "engagement\_window\_days": 0,
						* "view\_window\_days": 0},
					- "conversion\_event": "PAGE\_VISIT",
					- "conversion\_tag\_id": "string",
					- "cpa\_goal\_value\_in\_micro\_currency": "string",
					- "is\_roas\_optimized": true,
					- "learning\_mode\_type": "ACTIVE"},
				+ "frequency\_goal\_metadata": {
					- "frequency": 0,
					- "timerange": "DAY"},
				+ "scrollup\_goal\_metadata": {
					- "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
			* "budget\_type": "DAILY",
			* "start\_time": 5686848000,
			* "end\_time": 5705424000,
			* "targeting\_spec": {
				+ "AGE\_BUCKET": [
					- "35-44",
					- "50-54"],
				+ "APPTYPE": [
					- "ipad",
					- "iphone"],
				+ "AUDIENCE\_EXCLUDE": [
					- "string"],
				+ "AUDIENCE\_INCLUDE'": [
					- "string"],
				+ "GENDER": [
					- "unknown"],
				+ "GEO": [
					- "string"],
				+ "INTEREST": [
					- "string"],
				+ "LOCALE": [
					- "string"],
				+ "LOCATION": [
					- "string"],
				+ "SHOPPING\_RETARGETING": [
					- {
						* "lookback\_window": 30,
						* "exclusion\_window": 14,
						* "tag\_types": [
							+ 0,
							+ 6]}],
				+ "TARGETING\_STRATEGY": [
					- "CHOOSE\_YOUR\_OWN"]},
			* "lifetime\_frequency\_cap": 100,
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "auto\_targeting\_enabled": true,
			* "placement\_group": "ALL",
			* "pacing\_delivery\_type": "STANDARD",
			* "campaign\_id": "626736533506",
			* "billable\_event": "CLICKTHROUGH",
			* "bid\_strategy\_type": "MAX\_BID"}],
	+ "ads": [
		- {
			* "ad\_group\_id": "2680059592705",
			* "android\_deep\_link": "string",
			* "carousel\_android\_deep\_links": [
				+ "string"],
			* "carousel\_destination\_urls": [
				+ "string"],
			* "carousel\_ios\_deep\_links": [
				+ "string"],
			* "click\_tracking\_url": "string",
			* "creative\_type": "REGULAR",
			* "destination\_url": "string",
			* "ios\_deep\_link": "string",
			* "is\_pin\_deleted": false,
			* "is\_removable": false,
			* "name": "string",
			* "status": "ACTIVE",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "view\_tracking\_url": "string",
			* "lead\_form\_id": "string",
			* "grid\_click\_type": "CLOSEUP",
			* "customizable\_cta\_type": "LEARN\_MORE",
			* "quiz\_pin\_data": {
				+ "questions": [
					- {
						* "question\_id": 1,
						* "question\_text": "Where do you thrive?",
						* "options": [
							+ {
								- "text": "Hangout vibes"},
							+ {
								- "text": "Time to party!"},
							+ {
								- "text": "Keeping it lowkey"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Where would you nap?",
						* "options": [
							+ {
								- "text": "Hammock in the mountains"},
							+ {
								- "text": "Beach towel in the sand"},
							+ {
								- "text": "Tent under the stars"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Who are you taking?",
						* "options": [
							+ {
								- "text": "No one—solo trip!"},
							+ {
								- "text": "My best friend"},
							+ {
								- "text": "The family"}]}],
				+ "results": [
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 1},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 2},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 3}]},
			* "pin\_id": "394205773611545468"}],
	+ "product\_groups": [
		- {
			* "product\_group\_promotion": [
				+ {
					- "slideshow\_collections\_description": "Description",
					- "creative\_type": "REGULAR",
					- "collections\_hero\_pin\_id": "123123",
					- "catalog\_product\_group\_name": "catalogProductGroupName",
					- "collections\_hero\_destination\_url": "http://www.pinterest.com",
					- "tracking\_url": "https://www.pinterest.com",
					- "slideshow\_collections\_title": "Title",
					- "is\_mdl": true,
					- "status": "ACTIVE"},
				+ {
					- "slideshow\_collections\_description": "Description",
					- "creative\_type": "REGULAR",
					- "collections\_hero\_pin\_id": "123123",
					- "catalog\_product\_group\_name": "catalogProductGroupName",
					- "collections\_hero\_destination\_url": "http://www.pinterest.com",
					- "tracking\_url": "https://www.pinterest.com",
					- "slideshow\_collections\_title": "Title",
					- "is\_mdl": true,
					- "status": "ACTIVE"}],
			* "ad\_group\_id": "2680059592705"}],
	+ "keywords": [
		- {
			* "keywords": [
				+ {
					- "bid": 200000,
					- "match\_type": "BROAD",
					- "value": "string"}],
			* "parent\_id": "383791336903426391"}]},
* "update": {
	+ "campaigns": [
		- {
			* "id": "549755885175",
			* "ad\_account\_id": "549755885175",
			* "name": "ACME Tools",
			* "status": "ACTIVE",
			* "lifetime\_spend\_cap": 1432744744,
			* "daily\_spend\_cap": 1432744744,
			* "order\_line\_id": "549755885175",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "start\_time": 1580865126,
			* "end\_time": 1644023526,
			* "summary\_status": "RUNNING",
			* "is\_flexible\_daily\_budgets": true,
			* "default\_ad\_group\_budget\_in\_micro\_currency": 0,
			* "is\_automated\_campaign": true,
			* "is\_campaign\_budget\_optimization": true}],
	+ "ad\_groups": [
		- {
			* "name": "Ad Group For Pin: 687195905986",
			* "status": "ACTIVE",
			* "budget\_in\_micro\_currency": 5000000,
			* "bid\_in\_micro\_currency": 5000000,
			* "optimization\_goal\_metadata": {
				+ "conversion\_tag\_v3\_goal\_metadata": {
					- "attribution\_windows": {
						* "click\_window\_days": 0,
						* "engagement\_window\_days": 0,
						* "view\_window\_days": 0},
					- "conversion\_event": "PAGE\_VISIT",
					- "conversion\_tag\_id": "string",
					- "cpa\_goal\_value\_in\_micro\_currency": "string",
					- "is\_roas\_optimized": true,
					- "learning\_mode\_type": "ACTIVE"},
				+ "frequency\_goal\_metadata": {
					- "frequency": 0,
					- "timerange": "DAY"},
				+ "scrollup\_goal\_metadata": {
					- "scrollup\_goal\_value\_in\_micro\_currency": "string"}},
			* "budget\_type": "DAILY",
			* "start\_time": 5686848000,
			* "end\_time": 5705424000,
			* "targeting\_spec": {
				+ "AGE\_BUCKET": [
					- "35-44",
					- "50-54"],
				+ "APPTYPE": [
					- "ipad",
					- "iphone"],
				+ "AUDIENCE\_EXCLUDE": [
					- "string"],
				+ "AUDIENCE\_INCLUDE'": [
					- "string"],
				+ "GENDER": [
					- "unknown"],
				+ "GEO": [
					- "string"],
				+ "INTEREST": [
					- "string"],
				+ "LOCALE": [
					- "string"],
				+ "LOCATION": [
					- "string"],
				+ "SHOPPING\_RETARGETING": [
					- {
						* "lookback\_window": 30,
						* "exclusion\_window": 14,
						* "tag\_types": [
							+ 0,
							+ 6]}],
				+ "TARGETING\_STRATEGY": [
					- "CHOOSE\_YOUR\_OWN"]},
			* "lifetime\_frequency\_cap": 100,
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "auto\_targeting\_enabled": true,
			* "placement\_group": "ALL",
			* "pacing\_delivery\_type": "STANDARD",
			* "campaign\_id": "626736533506",
			* "billable\_event": "CLICKTHROUGH",
			* "bid\_strategy\_type": "MAX\_BID",
			* "id": "2680060704746"}],
	+ "ads": [
		- {
			* "ad\_group\_id": "2680059592705",
			* "android\_deep\_link": "string",
			* "carousel\_android\_deep\_links": [
				+ "string"],
			* "carousel\_destination\_urls": [
				+ "string"],
			* "carousel\_ios\_deep\_links": [
				+ "string"],
			* "click\_tracking\_url": "string",
			* "creative\_type": "REGULAR",
			* "destination\_url": "string",
			* "ios\_deep\_link": "string",
			* "is\_pin\_deleted": false,
			* "is\_removable": false,
			* "name": "string",
			* "status": "ACTIVE",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "view\_tracking\_url": "string",
			* "lead\_form\_id": "string",
			* "grid\_click\_type": "CLOSEUP",
			* "customizable\_cta\_type": "LEARN\_MORE",
			* "quiz\_pin\_data": {
				+ "questions": [
					- {
						* "question\_id": 1,
						* "question\_text": "Where do you thrive?",
						* "options": [
							+ {
								- "text": "Hangout vibes"},
							+ {
								- "text": "Time to party!"},
							+ {
								- "text": "Keeping it lowkey"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Where would you nap?",
						* "options": [
							+ {
								- "text": "Hammock in the mountains"},
							+ {
								- "text": "Beach towel in the sand"},
							+ {
								- "text": "Tent under the stars"}]},
					- {
						* "question\_id": 2,
						* "question\_text": "Who are you taking?",
						* "options": [
							+ {
								- "text": "No one—solo trip!"},
							+ {
								- "text": "My best friend"},
							+ {
								- "text": "The family"}]}],
				+ "results": [
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 1},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 2},
					- {
						* "organicPinId": "1234",
						* "android\_deep\_link": "https://www.pinterest.com/",
						* "iOS\_deep\_link": "https://www.pinterest.com/",
						* "destination\_url": "https://www.pinterest.com/",
						* "result\_id": 3}]},
			* "id": "687195134316"}],
	+ "product\_groups": [
		- {
			* "product\_group\_promotion": [
				+ {
					- "catalog\_product\_group\_id": "1234123",
					- "slideshow\_collections\_description": "Description",
					- "creative\_type": "REGULAR",
					- "collections\_hero\_pin\_id": "123123",
					- "catalog\_product\_group\_name": "ProductGroupName",
					- "collections\_hero\_destination\_url": "http://www.pinterest.com",
					- "tracking\_url": "https://www.pinterest.com",
					- "slideshow\_collections\_title": "Title",
					- "status": "ACTIVE",
					- "id": "2680059592705"},
				+ {
					- "catalog\_product\_group\_id": "1231231",
					- "slideshow\_collections\_description": "Other description",
					- "creative\_type": "REGULAR",
					- "collections\_hero\_pin\_id": "123124",
					- "catalog\_product\_group\_name": "ProductGroupName",
					- "collections\_hero\_destination\_url": "http://www.pinterest.com",
					- "tracking\_url": "https://www.pinterest.com",
					- "slideshow\_collections\_title": "Title",
					- "status": "ACTIVE",
					- "id": "2680059592706"}],
			* "ad\_group\_id": "26823439592705"}],
	+ "keywords": [
		- {
			* "id": "2886364308355",
			* "archived": false,
			* "bid": 200000}]}
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "request\_id": "549763856477-1660864560-1407e16a-c586-4add-94df-d0b160bec0ff, 549763856477-1660864560-d0b160bec0ff"
}`Download advertiser entities in bulk
------------------------------------
Get the status of a bulk request by `request_id`, along with a download URL that will allow you to download the
new or updated entity data (campaigns, ad groups, product groups, ads, or keywords).

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| bulk\_request\_id required  | string Unique identifier of a bulk upsert request.
 |
##### query Parameters

|  |  |
| --- | --- |
| include\_details | boolean Default:  false if set to True then attach the errors/details to all the requests
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/bulk/{bulk\_request\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/bulk/{bulk\_request\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "status": "SUCCEEDED",
* "result\_url": "https://pinterest-waterloo.s3.us-east-1.amazonaws.com/bulk\_framework/AD\_ENTITY\_UPSERT/549763856637-1659122537-0b4d77d3-f620-48ce-bec9-616106afb8d4/(...)"
}`campaigns
=========
View, create or update campaigns.

List campaigns
--------------
Get a list of the campaigns in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| campaign\_ids | Array of strings  [ 1 .. 100 ] items  List of Campaign Ids to use to filter the results.
 |
| entity\_statuses | Array of strings Default:  ["ACTIVE","PAUSED"]Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"   Example:  entity\_statuses=ACTIVEEntity status
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**400** Invalid ad account campaign parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaignshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "549755885175",
		- "ad\_account\_id": "549755885175",
		- "name": "ACME Tools",
		- "status": "ACTIVE",
		- "lifetime\_spend\_cap": 1432744744,
		- "daily\_spend\_cap": 1432744744,
		- "order\_line\_id": "549755885175",
		- "tracking\_urls": {
			* "impression": [
				+ "URL1",
				+ "URL2"],
			* "click": [
				+ "URL1",
				+ "URL2"],
			* "engagement": [
				+ "URL1",
				+ "URL2"],
			* "buyable\_button": [
				+ "URL1",
				+ "URL2"],
			* "audience\_verification": [
				+ "URL1",
				+ "URL2"]},
		- "start\_time": 1580865126,
		- "end\_time": 1644023526,
		- "summary\_status": "RUNNING",
		- "objective\_type": "AWARENESS",
		- "created\_time": 1432744744,
		- "updated\_time": 1432744744,
		- "type": "campaign",
		- "is\_flexible\_daily\_budgets": true,
		- "is\_campaign\_budget\_optimization": true}],
* "bookmark": "string"
}`Create campaigns
----------------
Create multiple new campaigns. Every campaign has its own campaign\_id and houses one or more ad groups, which contain one or more ads.
For more, see Set up your campaign. 

**Note:**

* The values for 'lifetime\_spend\_cap' and 'daily\_spend\_cap' are microcurrency amounts based on the currency field set in the advertiser's profile. (e.g. USD) Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.

A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’s profile.

**Equivalency equations**, using dollars as an example currency:

	+ $1 = 1,000,000 microdollars
	+ 1 microdollar = $0.000001**To convert between currency and microcurrency**, using dollars as an example currency:

	+ To convert dollars to microdollars, mutiply dollars by 1,000,000
	+ To convert microdollars to dollars, divide microdollars by 1,000,000

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Array of campaigns.

 Array ()
|  |  |
| --- | --- |
| ad\_account\_id required  | string^\d+$ Campaign's Advertiser ID. If you want to create a campaign in a Business Account shared account you need to specify the Business Access advertiser ID in both the query path param as well as the request body schema.
 |
| name required  | string Campaign name.
 |
| status | string Default:  "ACTIVE" Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Entity status
 |
| lifetime\_spend\_cap | integer Nullable  Campaign total spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "daily\_spend\_cap" cannot be set at the same time.
 |
| daily\_spend\_cap | integer Nullable  Campaign daily spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "lifetime\_spend\_cap" cannot be set at the same time.
 |
| order\_line\_id | string Nullable ^\d+$ Order line ID that appears on the invoice.
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see Third-party and dynamic tracking.
 |
| start\_time | integer Nullable  Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns.
 |
| end\_time | integer Nullable  Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns.
 |
| summary\_status | string Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Summary status for campaign
 |
| is\_flexible\_daily\_budgets | boolean Default:  false Determine if a campaign has flexible daily budgets setup.
 |
| default\_ad\_group\_budget\_in\_micro\_currency | integer Nullable  When transitioning from campaign budget optimization to non-campaign budget optimization, the default\_ad\_group\_budget\_in\_micro\_currency will propagate to each child ad groups daily budget. Unit is micro currency of the associated advertiser account.
 |
| is\_automated\_campaign | boolean Default:  false Specifies whether the campaign was created in the automated campaign flow
 |
| objective\_type required  | string (ObjectiveType)  Enum: "AWARENESS" "CONSIDERATION" "VIDEO\_VIEW" "WEB\_CONVERSION" "CATALOG\_SALES" "WEB\_SESSIONS"  Campaign objective type. If set as one of ["AWARENESS", "CONSIDERATION", "WEB\_CONVERSION", "CATALOG\_SALES"] the campaign is considered as a Campaign Budget Optimization (CBO) campaign, meaning budget needs to be set at the campaign level rather than at the ad group level. ["WEB\_SESSIONS"] in BETA.
 |
### Responses
**200** response

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/campaignshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "ad\_account\_id": "549755885175",
	+ "name": "ACME Tools",
	+ "status": "ACTIVE",
	+ "lifetime\_spend\_cap": 1432744744,
	+ "daily\_spend\_cap": 1432744744,
	+ "order\_line\_id": "549755885175",
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "start\_time": 1580865126,
	+ "end\_time": 1644023526,
	+ "summary\_status": "RUNNING",
	+ "is\_flexible\_daily\_budgets": true,
	+ "default\_ad\_group\_budget\_in\_micro\_currency": 0,
	+ "is\_automated\_campaign": true,
	+ "objective\_type": "AWARENESS"}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "ad\_account\_id": "549755885175",
			* "name": "ACME Tools",
			* "status": "ACTIVE",
			* "lifetime\_spend\_cap": 1432744744,
			* "daily\_spend\_cap": 1432744744,
			* "order\_line\_id": "549755885175",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "start\_time": 1580865126,
			* "end\_time": 1644023526,
			* "summary\_status": "RUNNING",
			* "is\_flexible\_daily\_budgets": true,
			* "default\_ad\_group\_budget\_in\_micro\_currency": 0,
			* "is\_automated\_campaign": true,
			* "id": "549755885175",
			* "objective\_type": "AWARENESS",
			* "created\_time": 1432744744,
			* "updated\_time": 1432744744,
			* "type": "campaign",
			* "is\_campaign\_budget\_optimization": true},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Update campaigns
----------------
Update multiple ad campaigns based on campaign\_ids. 

**Note:**

* The values for 'lifetime\_spend\_cap' and 'daily\_spend\_cap' are microcurrency amounts based on the currency field set in the advertiser's profile. (e.g. USD) 

Microcurrency is used to track very small transactions, based on the currency set in the advertiser’s profile.

A microcurrency unit is 10^(-6) of the standard unit of currency selected in the advertiser’ s profile.

**Equivalency equations**, using dollars as an example currency:

	+ $1 = 1,000,000 microdollars
	+ 1 microdollar = $0.000001**To convert between currency and microcurrency**, using dollars as an example currency:

	+ To convert dollars to microdollars, mutiply dollars by 1,000,000
	+ To convert microdollars to dollars, divide microdollars by 1,000,000

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Array of campaigns.

 Array ()
|  |  |
| --- | --- |
| id required  | string^\d+$ Campaign ID.
 |
| ad\_account\_id required  | string^\d+$ Campaign's Advertiser ID. If you want to create a campaign in a Business Account shared account you need to specify the Business Access advertiser ID in both the query path param as well as the request body schema.
 |
| name | string Campaign name.
 |
| status | string Nullable  Default:  "ACTIVE" Enum: "ACTIVE" "PAUSED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Entity status
 |
| lifetime\_spend\_cap | integer Nullable  Campaign total spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "daily\_spend\_cap" cannot be set at the same time.
 |
| daily\_spend\_cap | integer Nullable  Campaign daily spending cap. Required for Campaign Budget Optimization (CBO) campaigns. This and "lifetime\_spend\_cap" cannot be set at the same time.
 |
| order\_line\_id | string Nullable ^\d+$ Order line ID that appears on the invoice.
 |
| tracking\_urls | object Nullable  Third-party tracking URLs. Up to three tracking URLs - with a max length of 2,000 - are supported for each event type. Tracking URLs set at the ad group or ad level can override those set at the campaign level. For more information, see Third-party and dynamic tracking.
 |
| start\_time | integer Nullable  Campaign start time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns.
 |
| end\_time | integer Nullable  Campaign end time. Unix timestamp in seconds. Only used for Campaign Budget Optimization (CBO) campaigns.
 |
| summary\_status | string Enum: "RUNNING" "PAUSED" "NOT\_STARTED" "COMPLETED" "ADVERTISER\_DISABLED" "ARCHIVED" "DRAFT" "DELETED\_DRAFT"  Summary status for campaign
 |
| is\_flexible\_daily\_budgets | boolean Nullable  Default:  false Determine if a campaign has flexible daily budgets setup.
 |
| default\_ad\_group\_budget\_in\_micro\_currency | integer Nullable  When transitioning from campaign budget optimization to non-campaign budget optimization, the default\_ad\_group\_budget\_in\_micro\_currency will propagate to each child ad groups daily budget. Unit is micro currency of the associated advertiser account.
 |
| is\_automated\_campaign | boolean Nullable  Default:  false Specifies whether the campaign was created in the automated campaign flow
 |
| is\_campaign\_budget\_optimization | boolean Nullable  Determines if a campaign automatically generate ad-group level budgets given a campaign budget to maximize campaign outcome. When transitioning from non-cbo to cbo, all previous child ad group budget will be cleared.
 |
### Responses
**200** response

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/campaignshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "id": "549755885175",
	+ "ad\_account\_id": "549755885175",
	+ "name": "ACME Tools",
	+ "status": "ACTIVE",
	+ "lifetime\_spend\_cap": 1432744744,
	+ "daily\_spend\_cap": 1432744744,
	+ "order\_line\_id": "549755885175",
	+ "tracking\_urls": {
		- "impression": [
			* "URL1",
			* "URL2"],
		- "click": [
			* "URL1",
			* "URL2"],
		- "engagement": [
			* "URL1",
			* "URL2"],
		- "buyable\_button": [
			* "URL1",
			* "URL2"],
		- "audience\_verification": [
			* "URL1",
			* "URL2"]},
	+ "start\_time": 1580865126,
	+ "end\_time": 1644023526,
	+ "summary\_status": "RUNNING",
	+ "is\_flexible\_daily\_budgets": true,
	+ "default\_ad\_group\_budget\_in\_micro\_currency": 0,
	+ "is\_automated\_campaign": true,
	+ "is\_campaign\_budget\_optimization": true}
]`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "ad\_account\_id": "549755885175",
			* "name": "ACME Tools",
			* "status": "ACTIVE",
			* "lifetime\_spend\_cap": 1432744744,
			* "daily\_spend\_cap": 1432744744,
			* "order\_line\_id": "549755885175",
			* "tracking\_urls": {
				+ "impression": [
					- "URL1",
					- "URL2"],
				+ "click": [
					- "URL1",
					- "URL2"],
				+ "engagement": [
					- "URL1",
					- "URL2"],
				+ "buyable\_button": [
					- "URL1",
					- "URL2"],
				+ "audience\_verification": [
					- "URL1",
					- "URL2"]},
			* "start\_time": 1580865126,
			* "end\_time": 1644023526,
			* "summary\_status": "RUNNING",
			* "is\_flexible\_daily\_budgets": true,
			* "default\_ad\_group\_budget\_in\_micro\_currency": 0,
			* "is\_automated\_campaign": true,
			* "id": "549755885175",
			* "objective\_type": "AWARENESS",
			* "created\_time": 1432744744,
			* "updated\_time": 1432744744,
			* "type": "campaign",
			* "is\_campaign\_budget\_optimization": true},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Get campaign analytics
----------------------
Get analytics for the specified campaigns in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| campaign\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Campaign Ids to use to filter the results.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
### Responses
**200** Success

**400** Invalid ad account campaign analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/analytics###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "DATE": "2021-04-01",
	+ "CAMPAIGN\_ID": "547602124502",
	+ "SPEND\_IN\_DOLLAR": 30,
	+ "TOTAL\_CLICKTHROUGH": 216}
]`Get targeting analytics for campaigns
-------------------------------------
Get targeting analytics for one or more campaigns.
For the requested account and metrics, the response will include the requested metric information
(e.g. SPEND\_IN\_DOLLAR) for the requested target type (e.g. "age\_bucket") for applicable values (e.g. "45-49"). 

* The token's user\_account must either be the Owner of the specified ad account, or have one
of the necessary roles granted to them via
Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| campaign\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Campaign Ids to use to filter the results.
 |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| targeting\_types required  | Array of strings (AdsAnalyticsTargetingType)   [ 1 .. 15 ] items Items Enum: "KEYWORD" "APPTYPE" "GENDER" "LOCATION" "PLACEMENT" "COUNTRY" "TARGETED\_INTEREST" "PINNER\_INTEREST" "AUDIENCE\_INCLUDE" "GEO" "AGE\_BUCKET" "REGION"   Example:  targeting\_types=APPTYPETargeting type breakdowns for the report. The reporting per targeting type  is independent from each other.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
| attribution\_types | string (ConversionReportAttributionType)  Enum: "INDIVIDUAL" "HOUSEHOLD"   Example:  attribution\_types=INDIVIDUALList of types of attribution for the conversion report
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/targeting\_analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/targeting\_analytics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "targeting\_type": "KEYWORD",
		- "targeting\_value": "christmas decor ideas",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "iphone",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "ipad",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "web\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_mobile",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "APPTYPE",
		- "targeting\_value": "android\_tablet",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GENDER",
		- "targeting\_value": "female",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "LOCATION",
		- "targeting\_value": 500,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PLACEMENT",
		- "targeting\_value": "SEARCH",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "COUNTRY",
		- "targeting\_value": "US",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "TARGETED\_INTEREST",
		- "targeting\_value": "Food and Drinks",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "PINNER\_INTEREST",
		- "targeting\_value": "Chocolate Cookies",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AUDIENCE\_INCLUDE",
		- "targeting\_value": 254261234567,
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "GEO",
		- "targeting\_value": "US:94102",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "AGE\_BUCKET",
		- "targeting\_value": "45-49",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}},
	+ {
		- "targeting\_type": "REGION",
		- "targeting\_value": "US-CA",
		- "metrics": {
			* "AD\_GROUP\_ID": 2680067996745,
			* "DATE": "2022-04-26",
			* "SPEND\_IN\_DOLLAR": 240}}]
}`Get campaign
------------
Get a specific campaign given the campaign ID.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| campaign\_id required  | string  <= 18 characters ^\d+$ Campaign ID, must be associated with the ad account ID provided in the path.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/campaigns/{campaign\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/campaigns/{campaign\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "549755885175",
* "ad\_account\_id": "549755885175",
* "name": "ACME Tools",
* "status": "ACTIVE",
* "lifetime\_spend\_cap": 1432744744,
* "daily\_spend\_cap": 1432744744,
* "order\_line\_id": "549755885175",
* "tracking\_urls": {
	+ "impression": [
		- "URL1",
		- "URL2"],
	+ "click": [
		- "URL1",
		- "URL2"],
	+ "engagement": [
		- "URL1",
		- "URL2"],
	+ "buyable\_button": [
		- "URL1",
		- "URL2"],
	+ "audience\_verification": [
		- "URL1",
		- "URL2"]},
* "start\_time": 1580865126,
* "end\_time": 1644023526,
* "summary\_status": "RUNNING",
* "objective\_type": "AWARENESS",
* "created\_time": 1432744744,
* "updated\_time": 1432744744,
* "type": "campaign",
* "is\_flexible\_daily\_budgets": true,
* "is\_campaign\_budget\_optimization": true
}`catalogs
========
Manage information about shopping product catalogs and items.

List catalogs
-------------
Fetch catalogs owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid parameters.

**401** Unauthorized access.

**default** Unexpected error.

get/catalogshttps://api.pinterest.com/v5/catalogs###  Response samples
* 200
* 400
* 401
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "created\_at": "2022-03-14T15:15:22Z",
		- "id": "864344156814050986",
		- "updated\_at": "2022-03-14T15:16:34Z",
		- "name": "string",
		- "catalog\_type": "RETAIL"}],
* "bookmark": "string"
}`List feeds
----------
Fetch feeds owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to Before you get started with Catalogs. For Hotel parterns, refer to Pinterest API for shopping.

 ratelimit-category:  catalogs\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| catalog\_id | string^\d+$ Filter entities for a given catalog\_id. If not given, all catalogs are considered.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid parameters.

**401** Unauthorized access.

**default** Unexpected error.

get/catalogs/feedshttps://api.pinterest.com/v5/catalogs/feeds###  Response samples
* 200
* 400
* 401
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "created\_at": "2022-03-14T15:15:22Z",
		- "id": "string",
		- "updated\_at": "2022-03-14T15:16:34Z",
		- "name": "string",
		- "format": "TSV",
		- "catalog\_type": "RETAIL",
		- "credentials": {
			* "password": "pa$$word",
			* "username": "string"},
		- "location": "string",
		- "preferred\_processing\_schedule": {
			* "time": "02:59",
			* "timezone": "Africa/Abidjan"},
		- "status": "ACTIVE",
		- "default\_currency": "USD",
		- "default\_locale": "en-US",
		- "default\_country": "US",
		- "default\_availability": "IN\_STOCK"}],
* "bookmark": "string"
}`Create feed
-----------
Create a new feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Please, be aware that "default\_country"
and "default\_locale" are not required in the spec for forward compatibility
but for now the API will not accept requests without those fields.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to Before you get started with Catalogs. For Hotel parterns, refer to Pinterest API for shopping.

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read``catalogs:write`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to created a feed.

 One of feeds\_create\_requestlegacy\_retail\_only
|  |  |
| --- | --- |
| default\_currency | string (NullableCurrency)  Nullable  Enum: "AED" "AFN" "ALL" "AMD" "ANG" "AOA" "ARS" "AUD" "AWG" "AZN" "BAM" "BBD" "BDT" "BGN" "BHD" "BIF" "BMD" "BND" "BOB" "BRL" … 144 more Currency Codes from ISO 4217.
 |
| name required  | string A human-friendly name associated to a given feed.
 |
| format required  | string (CatalogsFormat)  Enum: "TSV" "CSV" "XML"  The file format of a feed.
 |
| default\_locale required  | CatalogsLocale (string) or string The locale used within a feed for product descriptions.
 |
| credentials | object (CatalogsFeedCredentials)  Nullable  This field is **OPTIONAL**. Use this if your feed file requires username and password.
 |
| location required  | string^(http|https|ftp|sftp):// The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.
 |
| preferred\_processing\_schedule | object (catalogs\_processing\_schedule)  Nullable  Daily processing schedule. This field is **OPTIONAL**. Use this to configure the preferred time for processing a feed (otherwise random).
 |
| catalog\_type required  | string (CatalogsType)  Type of the catalog entity.
RETAILRETAILHOTEL |
| default\_country required  | string (Country)  Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more Country ID from ISO 3166-1 alpha-2.
 |
| default\_availability | string (ProductAvailabilityType)  Nullable  Enum: "IN\_STOCK" "OUT\_OF\_STOCK" "PREORDER" null  Default availability for products in a feed.
 |
### Responses
**201** Success

**400** Invalid feed parameters.

**401** Unauthorized access.

**403** Business account required.

**409** User website required.

**422** Unique feed name is required.

**501** Not implemented (absent "default\_country" or "default\_locale").

**default** Unexpected error

post/catalogs/feedshttps://api.pinterest.com/v5/catalogs/feeds###  Request samples
* Payload
Content typeapplication/jsonExamplefeeds\_create\_requestfeeds\_create\_requestlegacy\_retail\_onlyCopy Expand all  Collapse all `{* "default\_currency": "USD",
* "name": "string",
* "format": "TSV",
* "default\_locale": "en-US",
* "credentials": {
	+ "password": "pa$$word",
	+ "username": "string"},
* "location": "string",
* "preferred\_processing\_schedule": {
	+ "time": "02:59",
	+ "timezone": "Africa/Abidjan"},
* "catalog\_type": "RETAIL",
* "default\_country": "US",
* "default\_availability": "IN\_STOCK"
}`###  Response samples
* 201
* 400
* 401
* 403
* 409
* 422
* 501
* default
Content typeapplication/jsonExampleRETAILRETAILHOTELCopy Expand all  Collapse all `{* "created\_at": "2022-03-14T15:15:22Z",
* "id": "string",
* "updated\_at": "2022-03-14T15:16:34Z",
* "name": "string",
* "format": "TSV",
* "catalog\_type": "RETAIL",
* "credentials": {
	+ "password": "pa$$word",
	+ "username": "string"},
* "location": "string",
* "preferred\_processing\_schedule": {
	+ "time": "02:59",
	+ "timezone": "Africa/Abidjan"},
* "status": "ACTIVE",
* "default\_currency": "USD",
* "default\_locale": "en-US",
* "default\_country": "US",
* "default\_availability": "IN\_STOCK"
}`Get feed
--------
Get a single feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to Before you get started with Catalogs. For Hotel parterns, refer to Pinterest API for shopping.

 ratelimit-category:  catalogs\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| feed\_id required  | string^\d+$ Unique identifier of a feed
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid feed parameters.

**401** Unauthorized access.

**404** Data feed not found.

**default** Unexpected error.

get/catalogs/feeds/{feed\_id}https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}###  Response samples
* 200
* 400
* 401
* 404
* default
Content typeapplication/jsonExampleRETAILRETAILHOTELCopy Expand all  Collapse all `{* "created\_at": "2022-03-14T15:15:22Z",
* "id": "string",
* "updated\_at": "2022-03-14T15:16:34Z",
* "name": "string",
* "format": "TSV",
* "catalog\_type": "RETAIL",
* "credentials": {
	+ "password": "pa$$word",
	+ "username": "string"},
* "location": "string",
* "preferred\_processing\_schedule": {
	+ "time": "02:59",
	+ "timezone": "Africa/Abidjan"},
* "status": "ACTIVE",
* "default\_currency": "USD",
* "default\_locale": "en-US",
* "default\_country": "US",
* "default\_availability": "IN\_STOCK"
}`Update feed
-----------
Update a feed owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to Before you get started with Catalogs. For Hotel parterns, refer to Pinterest API for shopping.

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read``catalogs:write`) ##### path Parameters

|  |  |
| --- | --- |
| feed\_id required  | string^\d+$ Unique identifier of a feed
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to update a feed.

 One of feeds\_update\_requestlegacy\_retail\_only
|  |  |
| --- | --- |
| default\_currency | string (NullableCurrency)  Nullable  Enum: "AED" "AFN" "ALL" "AMD" "ANG" "AOA" "ARS" "AUD" "AWG" "AZN" "BAM" "BBD" "BDT" "BGN" "BHD" "BIF" "BMD" "BND" "BOB" "BRL" … 144 more Currency Codes from ISO 4217.
 |
| name | string A human-friendly name associated to a given feed.
 |
| format | string (CatalogsFormat)  Enum: "TSV" "CSV" "XML"  The file format of a feed.
 |
| credentials | object (CatalogsFeedCredentials)  Nullable  This field is **OPTIONAL**. Use this if your feed file requires username and password.
 |
| location | string^(http|https|ftp|sftp):// The URL where a feed is available for download. This URL is what Pinterest will use to download a feed for processing.
 |
| preferred\_processing\_schedule | object (catalogs\_processing\_schedule)  Nullable  Daily processing schedule. This field is **OPTIONAL**. Use this to configure the preferred time for processing a feed (otherwise random).
 |
| status | string (CatalogsStatus)  Enum: "ACTIVE" "INACTIVE"  Status for catalogs entities. Present in catalogs\_feed values. When a feed is deleted, the response will inform DELETED as status.
 |
| catalog\_type required  | string (CatalogsType)  Type of the catalog entity.
RETAILRETAILHOTEL |
| default\_availability | string (ProductAvailabilityType)  Nullable  Enum: "IN\_STOCK" "OUT\_OF\_STOCK" "PREORDER" null  Default availability for products in a feed.
 |
### Responses
**200** Success

**400** Invalid feed parameters.

**403** Forbidden. Account not approved for feed mutations yet.

**404** Data feed not found.

**default** Unexpected error

patch/catalogs/feeds/{feed\_id}https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}###  Request samples
* Payload
Content typeapplication/jsonExamplefeeds\_update\_requestfeeds\_update\_requestlegacy\_retail\_onlyCopy Expand all  Collapse all `{* "default\_currency": "USD",
* "name": "string",
* "format": "TSV",
* "credentials": {
	+ "password": "pa$$word",
	+ "username": "string"},
* "location": "string",
* "preferred\_processing\_schedule": {
	+ "time": "02:59",
	+ "timezone": "Africa/Abidjan"},
* "status": "ACTIVE",
* "catalog\_type": "RETAIL",
* "default\_availability": "IN\_STOCK"
}`###  Response samples
* 200
* 400
* 403
* 404
* default
Content typeapplication/jsonExampleRETAILRETAILHOTELCopy Expand all  Collapse all `{* "created\_at": "2022-03-14T15:15:22Z",
* "id": "string",
* "updated\_at": "2022-03-14T15:16:34Z",
* "name": "string",
* "format": "TSV",
* "catalog\_type": "RETAIL",
* "credentials": {
	+ "password": "pa$$word",
	+ "username": "string"},
* "location": "string",
* "preferred\_processing\_schedule": {
	+ "time": "02:59",
	+ "timezone": "Africa/Abidjan"},
* "status": "ACTIVE",
* "default\_currency": "USD",
* "default\_locale": "en-US",
* "default\_country": "US",
* "default\_availability": "IN\_STOCK"
}`Delete feed
-----------
Delete a feed owned by the "operating user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

For Retail partners, refer to Before you get started with Catalogs. For Hotel parterns, refer to Pinterest API for shopping.

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read``catalogs:write`) ##### path Parameters

|  |  |
| --- | --- |
| feed\_id required  | string^\d+$ Unique identifier of a feed
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**204** Feed deleted successfully.

**400** Invalid feed parameters.

**403** Forbidden. Account not approved for feed mutations yet.

**404** Data feed not found.

**409** Conflict. Can't delete a feed with active promotions.

**default** Unexpected error

delete/catalogs/feeds/{feed\_id}https://api.pinterest.com/v5/catalogs/feeds/{feed\_id}###  Response samples
* 400
* 403
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 1,
* "message": "'feed\_id' value '1511851494501\_' must match the pattern: ^\\d+$\"}"
}`List processing results for a given feed
----------------------------------------
Fetch a feed processing results owned by the "operation user\_account". Please note that for now the bookmark parameter is not functional and only the first page will be available until it is implemented in some release in the near future.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| feed\_id required  | string^\d+$ Unique identifier of a feed
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid parameters.

**401** Unauthorized access.

**404** Feed not found.

**default** Unexpected error.

get/catalogs/feeds/{feed\_id}/processing\_resultshttps://api.pinterest.com/v5/catalogs/feeds/{feed\_id}/processing\_results###  Response samples
* 200
* 400
* 401
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "created\_at": "2022-03-14T15:15:22Z",
		- "id": "string",
		- "updated\_at": "2022-03-14T15:16:34Z",
		- "ingestion\_details": {
			* "errors": {
				+ "LINE\_LEVEL\_INTERNAL\_ERROR": 0,
				+ "LARGE\_PRODUCT\_COUNT\_DECREASE": 1,
				+ "ACCOUNT\_FLAGGED": 0,
				+ "IMAGE\_LEVEL\_INTERNAL\_ERROR": 0,
				+ "IMAGE\_FILE\_NOT\_ACCESSIBLE": 0,
				+ "IMAGE\_MALFORMED\_URL": 0,
				+ "IMAGE\_FILE\_NOT\_FOUND": 0,
				+ "IMAGE\_INVALID\_FILE": 0},
			* "info": {
				+ "IN\_STOCK": 0,
				+ "OUT\_OF\_STOCK": 0,
				+ "PREORDER": 0},
			* "warnings": {
				+ "ADDITIONAL\_IMAGE\_LEVEL\_INTERNAL\_ERROR": 0,
				+ "ADDITIONAL\_IMAGE\_FILE\_NOT\_ACCESSIBLE": 0,
				+ "ADDITIONAL\_IMAGE\_MALFORMED\_URL": 0,
				+ "ADDITIONAL\_IMAGE\_FILE\_NOT\_FOUND": 0,
				+ "ADDITIONAL\_IMAGE\_INVALID\_FILE": 0,
				+ "HOTEL\_PRICE\_HEADER\_IS\_PRESENT": 0}},
		- "status": "COMPLETED",
		- "product\_counts": {
			* "original": 0,
			* "ingested": 0},
		- "validation\_details": {
			* "errors": {
				+ "FETCH\_ERROR": 0,
				+ "FETCH\_INACTIVE\_FEED\_ERROR": 0,
				+ "ENCODING\_ERROR": 0,
				+ "DELIMITER\_ERROR": 0,
				+ "REQUIRED\_COLUMNS\_MISSING": 0,
				+ "DUPLICATE\_PRODUCTS": 0,
				+ "IMAGE\_LINK\_INVALID": 0,
				+ "ITEMID\_MISSING": 0,
				+ "TITLE\_MISSING": 0,
				+ "DESCRIPTION\_MISSING": 0,
				+ "PRODUCT\_LINK\_MISSING": 0,
				+ "IMAGE\_LINK\_MISSING": 0,
				+ "AVAILABILITY\_INVALID": 0,
				+ "PRODUCT\_PRICE\_INVALID": 0,
				+ "LINK\_FORMAT\_INVALID": 0,
				+ "PARSE\_LINE\_ERROR": 0,
				+ "ADWORDS\_FORMAT\_INVALID": 0,
				+ "INTERNAL\_SERVICE\_ERROR": 0,
				+ "NO\_VERIFIED\_DOMAIN": 0,
				+ "ADULT\_INVALID": 0,
				+ "IMAGE\_LINK\_LENGTH\_TOO\_LONG": 0,
				+ "INVALID\_DOMAIN": 0,
				+ "FEED\_LENGTH\_TOO\_LONG": 0,
				+ "LINK\_LENGTH\_TOO\_LONG": 0,
				+ "MALFORMED\_XML": 0,
				+ "PRICE\_MISSING": 0,
				+ "FEED\_TOO\_SMALL": 0,
				+ "MAX\_ITEMS\_PER\_ITEM\_GROUP\_EXCEEDED": 0,
				+ "ITEM\_MAIN\_IMAGE\_DOWNLOAD\_FAILURE": 0,
				+ "PINJOIN\_CONTENT\_UNSAFE": 0,
				+ "BLOCKLISTED\_IMAGE\_SIGNATURE": 0,
				+ "LIST\_PRICE\_INVALID": 0,
				+ "PRICE\_CANNOT\_BE\_DETERMINED": 0},
			* "warnings": {
				+ "AD\_LINK\_FORMAT\_WARNING": 0,
				+ "AD\_LINK\_SAME\_AS\_LINK": 0,
				+ "TITLE\_LENGTH\_TOO\_LONG": 0,
				+ "DESCRIPTION\_LENGTH\_TOO\_LONG": 0,
				+ "GENDER\_INVALID": 0,
				+ "AGE\_GROUP\_INVALID": 0,
				+ "SIZE\_TYPE\_INVALID": 0,
				+ "SIZE\_SYSTEM\_INVALID": 0,
				+ "LINK\_FORMAT\_WARNING": 0,
				+ "SALES\_PRICE\_INVALID": 0,
				+ "PRODUCT\_CATEGORY\_DEPTH\_WARNING": 0,
				+ "ADWORDS\_FORMAT\_WARNING": 0,
				+ "ADWORDS\_SAME\_AS\_LINK": 0,
				+ "DUPLICATE\_HEADERS": 0,
				+ "FETCH\_SAME\_SIGNATURE": 1,
				+ "ADDITIONAL\_IMAGE\_LINK\_LENGTH\_TOO\_LONG": 0,
				+ "ADDITIONAL\_IMAGE\_LINK\_WARNING": 0,
				+ "IMAGE\_LINK\_WARNING": 0,
				+ "SHIPPING\_INVALID": 0,
				+ "TAX\_INVALID": 0,
				+ "SHIPPING\_WEIGHT\_INVALID": 0,
				+ "EXPIRATION\_DATE\_INVALID": 0,
				+ "AVAILABILITY\_DATE\_INVALID": 0,
				+ "SALE\_DATE\_INVALID": 0,
				+ "WEIGHT\_UNIT\_INVALID": 0,
				+ "IS\_BUNDLE\_INVALID": 0,
				+ "UPDATED\_TIME\_INVALID": 0,
				+ "CUSTOM\_LABEL\_LENGTH\_TOO\_LONG": 0,
				+ "PRODUCT\_TYPE\_LENGTH\_TOO\_LONG": 0,
				+ "TOO\_MANY\_ADDITIONAL\_IMAGE\_LINKS": 0,
				+ "MULTIPACK\_INVALID": 0,
				+ "INDEXED\_PRODUCT\_COUNT\_LARGE\_DELTA": 0,
				+ "ITEM\_ADDITIONAL\_IMAGE\_DOWNLOAD\_FAILURE": 0,
				+ "OPTIONAL\_PRODUCT\_CATEGORY\_MISSING": 0,
				+ "OPTIONAL\_PRODUCT\_CATEGORY\_INVALID": 0,
				+ "OPTIONAL\_CONDITION\_MISSING": 0,
				+ "OPTIONAL\_CONDITION\_INVALID": 0,
				+ "IOS\_DEEP\_LINK\_INVALID": 0,
				+ "ANDROID\_DEEP\_LINK\_INVALID": 0,
				+ "UTM\_SOURCE\_AUTO\_CORRECTED": 0,
				+ "COUNTRY\_DOES\_NOT\_MAP\_TO\_CURRENCY": 0,
				+ "MIN\_AD\_PRICE\_INVALID": 0,
				+ "GTIN\_INVALID": 0,
				+ "INCONSISTENT\_CURRENCY\_VALUES": 0,
				+ "SALES\_PRICE\_TOO\_LOW": 0,
				+ "SHIPPING\_WIDTH\_INVALID": 0,
				+ "SHIPPING\_HEIGHT\_INVALID": 0,
				+ "SALES\_PRICE\_TOO\_HIGH": 0,
				+ "MPN\_INVALID": 0}}}],
* "bookmark": "string"
}`Get catalogs items
------------------
Get the items of the catalog owned by the "operation user\_account". See detailed documentation here.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| country required  | string  Example:  country=USCountry for the Catalogs Items
 |
| language required  | string  Example:  language=ENLanguage for the Catalogs Items
 |
| item\_ids | Array of strings Deprecated   Example:  item\_ids=CR123This parameter is deprecated. Use filters instead.
 |
| filters | object (CatalogsItemsFilters)  Identifies items to be retrieved. This is a required parameter.
 |
### Responses
**200** Response containing the requested catalogs items

**400** Invalid request parameters.

**401** Not authorized to access catalogs items

**403** Not authorized to access catalogs items

**default** Unexpected error

get/catalogs/itemshttps://api.pinterest.com/v5/catalogs/items###  Response samples
* 200
* 400
* 401
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "catalog\_type": "RETAIL",
		- "item\_id": "DS0294-M",
		- "pins": [
			* {
				+ "id": "813744226420795884",
				+ "created\_at": "2020-01-01T20:10:40-00:00",
				+ "link": "https://www.pinterest.com/",
				+ "title": "string",
				+ "description": "string",
				+ "dominant\_color": "#6E7874",
				+ "alt\_text": "string",
				+ "creative\_type": "REGULAR",
				+ "board\_id": "string",
				+ "board\_section\_id": "string",
				+ "board\_owner": {
					- "username": "string"},
				+ "is\_owner": true,
				+ "media": {
					- "media\_type": "string"},
				+ "parent\_pin\_id": "string",
				+ "is\_standard": true,
				+ "has\_been\_promoted": true,
				+ "note": "string",
				+ "pin\_metrics": {
					- "pin\_metrics": [
						* {
							+ "90d": {
								- "pin\_click": 7,
								- "impression": 2,
								- "clickthrough": 3},
							+ "all\_time": {
								- "pin\_click": 7,
								- "impression": 2,
								- "clickthrough": 3,
								- "reaction": 10,
								- "comment": 2}},
						* null]}}],
		- "attributes": {
			* "additional\_image\_link": [
				+ "https://scene.example.com/image/image\_v2.jpg",
				+ "https://scene.example.com/image/image\_v3.jpg"],
			* "image\_link": [
				+ "https://scene.example.com/image/image.jpg"],
			* "ad\_link": "https://www.example.com/cat/denim-shirt/item012?utm\_source=Pinterest",
			* "adult": true,
			* "age\_group": "newborn",
			* "availability": "in stock",
			* "average\_review\_rating": 5,
			* "brand": "Josie’s Denim",
			* "checkout\_enabled": false,
			* "color": "blue",
			* "condition": "new",
			* "custom\_label\_0": "Best sellers",
			* "custom\_label\_1": "Summer promotion",
			* "custom\_label\_2": "Winter sales",
			* "custom\_label\_3": "Woman dress",
			* "custom\_label\_4": "Man hat",
			* "description": "Casual fit denim shirt made with the finest quality Japanese denim.",
			* "free\_shipping\_label": true,
			* "free\_shipping\_limit": "35 USD",
			* "gender": "unisex",
			* "google\_product\_category": "Apparel & Accessories > Clothing > Shirts & Tops",
			* "gtin": 3234567890126,
			* "id": "DS0294-L",
			* "item\_group\_id": "DS0294",
			* "last\_updated\_time": 1641483432072,
			* "link": "https://www.example.com/cat/womens-clothing/denim-shirt-0294",
			* "material": "cotton",
			* "min\_ad\_price": "19.99 USD",
			* "mobile\_link": "https://m.example.com/cat/womens-clothing/denim-shirt-0294",
			* "mpn": "PI12345NTEREST",
			* "number\_of\_ratings": 10,
			* "number\_of\_reviews": 10,
			* "pattern": "plaid",
			* "price": "24.99 USD",
			* "product\_type": "Clothing > Women’s > Shirts > Denim",
			* "sale\_price": "14.99 USD",
			* "shipping": "US:CA:Ground:0 USD",
			* "shipping\_height": "12 in",
			* "shipping\_weight": "3 kg",
			* "shipping\_width": "16 in",
			* "size": "M",
			* "size\_system": "US",
			* "size\_type": "regular",
			* "tax": "US:1025433:6.00:y",
			* "title": "Women’s denim shirt, large",
			* "variant\_names": [
				+ "Color",
				+ "Size"],
			* "variant\_values": [
				+ "Red",
				+ "Small"]}}]
}`Operate on item batch
---------------------
This endpoint supports multiple operations on a set of one or more catalog items owned by the "operation user\_account". See detailed documentation here.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

 ratelimit-category:  catalogs\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read``catalogs:write`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to create catalogs items in a batch

 One of operate on item batchlegacy\_retail\_only
|  |  |
| --- | --- |
| catalog\_type required  | string (CatalogsType)  Type of the catalog entity.
RETAILRETAILHOTEL |
| country required  | string (Country)  Enum: "AD" "AE" "AF" "AG" "AI" "AL" "AM" "AO" "AQ" "AR" "AS" "AT" "AU" "AW" "AX" "AZ" "BA" "BB" "BD" "BE" … 228 more Country ID from ISO 3166-1 alpha-2.
 |
| language required  | string (Language)  Enum: "AM" "AR" "AZ" "BG" "BN" "BS" "CA" "CS" "DA" "DV" "DZ" "DE" "EL" "EN" "ES" "ET" "FA" "FI" "FR" "HE" … 41 more Language code, which is among the offical ISO 639-1 language list.
 |
| items required  | Array of any  [ 1 .. 1000 ] items  Array with catalogs item operations
 |
### Responses
**200** Response containing the requested catalogs items batch

**400** Invalid request parameters.

**401** Not authenticated to post catalogs items

**403** Not authorized to post catalogs items

**default** Unexpected error

post/catalogs/items/batchhttps://api.pinterest.com/v5/catalogs/items/batch###  Request samples
* Payload
Content typeapplication/jsonExampleoperate on item batchoperate on item batchlegacy\_retail\_onlyCopy Expand all  Collapse all `{* "catalog\_type": "RETAIL",
* "country": "US",
* "language": "EN",
* "items": [
	+ {
		- "item\_id": "DS0294-M",
		- "operation": "CREATE",
		- "attributes": {
			* "additional\_image\_link": [
				+ "https://scene.example.com/image/image\_v2.jpg",
				+ "https://scene.example.com/image/image\_v3.jpg"],
			* "image\_link": [
				+ "https://scene.example.com/image/image.jpg"],
			* "ad\_link": "https://www.example.com/cat/denim-shirt/item012?utm\_source=Pinterest",
			* "adult": true,
			* "age\_group": "newborn",
			* "availability": "in stock",
			* "average\_review\_rating": 5,
			* "brand": "Josie’s Denim",
			* "checkout\_enabled": false,
			* "color": "blue",
			* "condition": "new",
			* "custom\_label\_0": "Best sellers",
			* "custom\_label\_1": "Summer promotion",
			* "custom\_label\_2": "Winter sales",
			* "custom\_label\_3": "Woman dress",
			* "custom\_label\_4": "Man hat",
			* "description": "Casual fit denim shirt made with the finest quality Japanese denim.",
			* "free\_shipping\_label": true,
			* "free\_shipping\_limit": "35 USD",
			* "gender": "unisex",
			* "google\_product\_category": "Apparel & Accessories > Clothing > Shirts & Tops",
			* "gtin": 3234567890126,
			* "id": "DS0294-L",
			* "item\_group\_id": "DS0294",
			* "last\_updated\_time": 1641483432072,
			* "link": "https://www.example.com/cat/womens-clothing/denim-shirt-0294",
			* "material": "cotton",
			* "min\_ad\_price": "19.99 USD",
			* "mobile\_link": "https://m.example.com/cat/womens-clothing/denim-shirt-0294",
			* "mpn": "PI12345NTEREST",
			* "number\_of\_ratings": 10,
			* "number\_of\_reviews": 10,
			* "pattern": "plaid",
			* "price": "24.99 USD",
			* "product\_type": "Clothing > Women’s > Shirts > Denim",
			* "sale\_price": "14.99 USD",
			* "shipping": "US:CA:Ground:0 USD",
			* "shipping\_height": "12 in",
			* "shipping\_weight": "3 kg",
			* "shipping\_width": "16 in",
			* "size": "M",
			* "size\_system": "US",
			* "size\_type": "regular",
			* "tax": "US:1025433:6.00:y",
			* "title": "Women’s denim shirt, large",
			* "variant\_names": [
				+ "Color",
				+ "Size"],
			* "variant\_values": [
				+ "Red",
				+ "Small"]}}]
}`###  Response samples
* 200
* 400
* 401
* 403
* default
Content typeapplication/jsonExampleRETAILRETAILHOTELCopy Expand all  Collapse all `{* "batch\_id": "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e",
* "created\_time": "2020-01-01T20:10:40-00:00",
* "completed\_time": "2022-03-10T15:37:10-00:00",
* "status": "PROCESSING",
* "catalog\_type": "RETAIL",
* "items": [
	+ {
		- "item\_id": "DS0294-M",
		- "errors": [
			* {
				+ "attribute": "title",
				+ "code": 106,
				+ "message": "Title is missing from product metadata."}],
		- "warnings": [
			* {
				+ "attribute": "title",
				+ "code": 106,
				+ "message": "Title is missing from product metadata."}],
		- "status": "SUCCESS"}]
}`Get catalogs items batch
------------------------
Get a single catalogs items batch owned by the "operating user\_account". See detailed documentation here.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| batch\_id required  | string  Example:  595953100599279259-66753b9bb65c46c49bd8503b27fecf9eId of a catalogs items batch to fetch
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Response containing the requested catalogs items batch

**401** Not authenticated to access catalogs items batch

**403** Not authorized to access catalogs items batch

**404** Catalogs items batch not found

**405** Method Not Allowed.

**default** Unexpected error

get/catalogs/items/batch/{batch\_id}https://api.pinterest.com/v5/catalogs/items/batch/{batch\_id}###  Response samples
* 200
* 401
* 403
* 404
* 405
* default
Content typeapplication/jsonExampleRETAILRETAILHOTELCopy Expand all  Collapse all `{* "batch\_id": "595953100599279259-66753b9bb65c46c49bd8503b27fecf9e",
* "created\_time": "2020-01-01T20:10:40-00:00",
* "completed\_time": "2022-03-10T15:37:10-00:00",
* "status": "PROCESSING",
* "catalog\_type": "RETAIL",
* "items": [
	+ {
		- "item\_id": "DS0294-M",
		- "errors": [
			* {
				+ "attribute": "title",
				+ "code": 106,
				+ "message": "Title is missing from product metadata."}],
		- "warnings": [
			* {
				+ "attribute": "title",
				+ "code": 106,
				+ "message": "Title is missing from product metadata."}],
		- "status": "SUCCESS"}]
}`List item issues for a given processing result
----------------------------------------------
List item validation issues for a given feed processing result owned by the "operation user\_account". Please note that for now query parameters 'item\_numbers' and 'item\_validation\_issue' cannot be used simultaneously until it is implemented in some release in the future.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| processing\_result\_id required  | string^\d+$  Example:  5224831246441439241Unique identifier of a feed processing result. It can be acquired from the "id" field of the "items" array within the response of the List processing results for a given feed.
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| item\_numbers | Array of integers  Example:  item\_numbers=1&item\_numbers=5Item number based on order of appearance in the Catalogs Feed. For example, '0' refers to first item found in a feed that was downloaded from a 'location' specified during feed creation.
 |
| item\_validation\_issue | string (CatalogsItemValidationIssue)  Enum: "AD\_LINK\_FORMAT\_WARNING" "AD\_LINK\_SAME\_AS\_LINK" "ADDITIONAL\_IMAGE\_LINK\_LENGTH\_TOO\_LONG" "ADDITIONAL\_IMAGE\_LINK\_WARNING" "ADULT\_INVALID" "ADWORDS\_FORMAT\_INVALID" "ADWORDS\_FORMAT\_WARNING" "ADWORDS\_SAME\_AS\_LINK" "AGE\_GROUP\_INVALID" "ANDROID\_DEEP\_LINK\_INVALID" "AVAILABILITY\_DATE\_INVALID" "AVAILABILITY\_INVALID" "BLOCKLISTED\_IMAGE\_SIGNATURE" "COUNTRY\_DOES\_NOT\_MAP\_TO\_CURRENCY" "CUSTOM\_LABEL\_LENGTH\_TOO\_LONG" "DESCRIPTION\_LENGTH\_TOO\_LONG" "DESCRIPTION\_MISSING" "DUPLICATE\_PRODUCTS" "EXPIRATION\_DATE\_INVALID" "GENDER\_INVALID" … 47 more  Example:  item\_validation\_issue=TITLE\_MISSINGFilter item validation issues that have a given type of item validation issue.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**401** Unauthorized access.

**404** Processing Result not found.

**501** Not implemented.

**default** Unexpected error.

get/catalogs/processing\_results/{processing\_result\_id}/item\_issueshttps://api.pinterest.com/v5/catalogs/processing\_results/{processing\_result\_id}/item\_issues###  Response samples
* 200
* 401
* 404
* 501
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "item\_number": 0,
		- "item\_id": "DS0294-L",
		- "errors": {
			* "ADULT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ADWORDS\_FORMAT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "AVAILABILITY\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "BLOCKLISTED\_IMAGE\_SIGNATURE": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "DESCRIPTION\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "DUPLICATE\_PRODUCTS": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IMAGE\_LINK\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IMAGE\_LINK\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IMAGE\_LINK\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "INVALID\_DOMAIN": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ITEMID\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ITEM\_MAIN\_IMAGE\_DOWNLOAD\_FAILURE": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "LINK\_FORMAT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "LINK\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "LIST\_PRICE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "MAX\_ITEMS\_PER\_ITEM\_GROUP\_EXCEEDED": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PARSE\_LINE\_ERROR": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PINJOIN\_CONTENT\_UNSAFE": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRICE\_CANNOT\_BE\_DETERMINED": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRICE\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRODUCT\_LINK\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRODUCT\_PRICE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "TITLE\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"}},
		- "warnings": {
			* "AD\_LINK\_FORMAT\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "AD\_LINK\_SAME\_AS\_LINK": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ADDITIONAL\_IMAGE\_LINK\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ADDITIONAL\_IMAGE\_LINK\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ADWORDS\_FORMAT\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ADWORDS\_SAME\_AS\_LINK": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "AGE\_GROUP\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SIZE\_SYSTEM\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ANDROID\_DEEP\_LINK\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "AVAILABILITY\_DATE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "COUNTRY\_DOES\_NOT\_MAP\_TO\_CURRENCY": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "CUSTOM\_LABEL\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "DESCRIPTION\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "EXPIRATION\_DATE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "GENDER\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "GTIN\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IMAGE\_LINK\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IOS\_DEEP\_LINK\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "IS\_BUNDLE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "ITEM\_ADDITIONAL\_IMAGE\_DOWNLOAD\_FAILURE": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "LINK\_FORMAT\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "MIN\_AD\_PRICE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "MPN\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "MULTIPACK\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "OPTIONAL\_CONDITION\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "OPTIONAL\_CONDITION\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "OPTIONAL\_PRODUCT\_CATEGORY\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "OPTIONAL\_PRODUCT\_CATEGORY\_MISSING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRODUCT\_CATEGORY\_DEPTH\_WARNING": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "PRODUCT\_TYPE\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SALES\_PRICE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SALES\_PRICE\_TOO\_LOW": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SALES\_PRICE\_TOO\_HIGH": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SALE\_DATE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SHIPPING\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SHIPPING\_HEIGHT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SHIPPING\_WEIGHT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SHIPPING\_WIDTH\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "SIZE\_TYPE\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "TAX\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "TITLE\_LENGTH\_TOO\_LONG": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "TOO\_MANY\_ADDITIONAL\_IMAGE\_LINKS": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "UTM\_SOURCE\_AUTO\_CORRECTED": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"},
			* "WEIGHT\_UNIT\_INVALID": {
				+ "attribute\_name": "TITLE",
				+ "provided\_value": "string"}}}],
* "bookmark": "string"
}`List product groups
-------------------
Get a list of product groups for a given Catalogs Feed Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### query Parameters

|  |  |
| --- | --- |
| feed\_id | string^\d+$ Filter entities for a given feed\_id. If not given, all feeds are considered.
 |
| catalog\_id | string^\d+$ Filter entities for a given catalog\_id. If not given, all catalogs are considered.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid feed parameters.

**401** Unauthorized access.

**403** Forbidden. Account not approved for catalog product group mutations yet.

**404** Data feed not found.

**409** Conflict. Can't create this catalogs product group with this value.

**default** Unexpected error.

get/catalogs/product\_groupshttps://api.pinterest.com/v5/catalogs/product\_groups###  Response samples
* 200
* 400
* 401
* 403
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "443727193917",
		- "name": "Most Popular",
		- "description": "string",
		- "filters": {
			* "any\_of": [
				+ {
					- "MIN\_PRICE": {
						* "inclusion": true,
						* "values": 0,
						* "negated": false}}]},
		- "is\_featured": true,
		- "type": "TOP\_SELLERS",
		- "status": "ACTIVE",
		- "created\_at": 1621350033000,
		- "updated\_at": 1622742155000,
		- "feed\_id": "2680059592705",
		- "catalog\_type": "RETAIL"}],
* "bookmark": "string"
}`Create product group
--------------------
Create product group to use in Catalogs owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:write`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to created a catalogs product group.

 One of retailhotel
|  |  |
| --- | --- |
| name required  | string  |
| description | string Nullable   |
| is\_featured | boolean Default:  false boolean indicator of whether the product group is being featured or not
 |
| filters required  | object or object (catalogs\_product\_group\_filters)  Object holding a group of filters for request on catalog product group. This is a distinct schema It is not possible to create or update a Product Group with empty filters. But some automatically generated Product Groups might have empty filters.
 |
| feed\_id required  | string^\d+$ Catalog Feed id pertaining to the catalog product group.
 |
### Responses
**201** Success

**400** Invalid body.

**401** Unauthorized access.

**403** Forbidden. Account not approved for catalog product group mutations yet.

**409** Conflict. Can't create this catalogs product group with this value.

**default** Unexpected error.

post/catalogs/product\_groupshttps://api.pinterest.com/v5/catalogs/product\_groups###  Request samples
* Payload
Content typeapplication/jsonExampleA simple retail example that applies "all of the following filters".A simple retail example that applies "all of the following filters".A more complete retail example that applies "any of the following filters".A simple hotel example that applies "all of the following filters".The use of "all\_of" creates a Product Group where all of the individual filters
must be satisfied by a product to be included in the Product Group.

Copy Expand all  Collapse all `{* "name": "Few Filters using \"all\_of\"",
* "feed\_id": "2680059592705",
* "featured": false,
* "filters": {
	+ "all\_of": [
		- {
			* "MIN\_PRICE": {
				+ "values": 999.99,
				+ "inclusion": true}},
		- {
			* "CURRENCY": {
				+ "values": "USD"}},
		- {
			* "CUSTOM\_LABEL\_0": {
				+ "values": [
					- "Luxury Items"]}}]}
}`###  Response samples
* 201
* 400
* 401
* 403
* 409
* default
Content typeapplication/jsonExamplefeed\_based\_product\_groupfeed\_based\_product\_groupcatalog\_based\_product\_groupCopy Expand all  Collapse all `{* "id": "443727193917",
* "name": "Most Popular",
* "description": "string",
* "filters": {
	+ "any\_of": [
		- {
			* "MIN\_PRICE": {
				+ "inclusion": true,
				+ "values": 0,
				+ "negated": false}}]},
* "is\_featured": true,
* "type": "TOP\_SELLERS",
* "status": "ACTIVE",
* "created\_at": 1621350033000,
* "updated\_at": 1622742155000,
* "feed\_id": "2680059592705",
* "catalog\_type": "RETAIL"
}`Get product group
-----------------
Get a singe product group for a given Catalogs Product Group Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| product\_group\_id required  | string^\d+$ Unique identifier of a product group
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid catalogs product group id parameters.

**401** Unauthorized access.

**403** Forbidden. Account not approved for catalog product group mutations yet.

**404** Catalogs product group not found.

**409** Conflict. Can't get a catalogs product group without an existing catalog.

**default** Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}###  Response samples
* 200
* 400
* 401
* 403
* 404
* 409
* default
Content typeapplication/jsonExamplefeed\_based\_product\_groupfeed\_based\_product\_groupcatalog\_based\_product\_groupCopy Expand all  Collapse all `{* "id": "443727193917",
* "name": "Most Popular",
* "description": "string",
* "filters": {
	+ "any\_of": [
		- {
			* "MIN\_PRICE": {
				+ "inclusion": true,
				+ "values": 0,
				+ "negated": false}}]},
* "is\_featured": true,
* "type": "TOP\_SELLERS",
* "status": "ACTIVE",
* "created\_at": 1621350033000,
* "updated\_at": 1622742155000,
* "feed\_id": "2680059592705",
* "catalog\_type": "RETAIL"
}`Delete product group
--------------------
Delete a product group owned by the "operation user\_account" from being in use in Catalogs.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:write`) ##### path Parameters

|  |  |
| --- | --- |
| product\_group\_id required  | string^\d+$ Unique identifier of a product group
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**204** Catalogs Product Group deleted successfully.

**400** Invalid catalogs product group id parameters.

**401** Unauthorized access.

**403** Forbidden. Account not approved for catalog product group mutations yet.

**404** Catalogs product group not found.

**409** Conflict. Can't delete this catalogs product group.

**default** Unexpected error.

delete/catalogs/product\_groups/{product\_group\_id}https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}###  Response samples
* 400
* 401
* 403
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 1,
* "message": "'product\_group\_id' value '11851494501\_' must match the pattern: ^\\d+$\"}"
}`Update product group
--------------------
Update product group owned by the "operation user\_account" to use in Catalogs.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`catalogs:write`) ##### path Parameters

|  |  |
| --- | --- |
| product\_group\_id required  | string^\d+$ Unique identifier of a product group
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to Update a catalogs product group.

 One of retailhotel
|  |  |
| --- | --- |
| name | string  |
| description | string Nullable   |
| is\_featured | boolean boolean indicator of whether the product group is being featured or not
 |
| filters | object or object (catalogs\_product\_group\_filters)  Object holding a group of filters for request on catalog product group. This is a distinct schema It is not possible to create or update a Product Group with empty filters. But some automatically generated Product Groups might have empty filters.
 |
### Responses
**200** Success

**400** Invalid parameters.

**401** Unauthorized access.

**403** Forbidden. Account not approved for catalog product group mutations yet.

**404** Catalogs product group not found.

**409** Conflict. Can't update this catalogs product group to this value.

**default** Unexpected error.

patch/catalogs/product\_groups/{product\_group\_id}https://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}###  Request samples
* Payload
Content typeapplication/jsonExampleretailretailhotelCopy Expand all  Collapse all `{* "name": "string",
* "description": "string",
* "is\_featured": true,
* "filters": {
	+ "any\_of": [
		- {
			* "MIN\_PRICE": {
				+ "inclusion": true,
				+ "values": 0,
				+ "negated": false}}]}
}`###  Response samples
* 200
* 400
* 401
* 403
* 404
* 409
* default
Content typeapplication/jsonExamplefeed\_based\_product\_groupfeed\_based\_product\_groupcatalog\_based\_product\_groupCopy Expand all  Collapse all `{* "id": "443727193917",
* "name": "Most Popular",
* "description": "string",
* "filters": {
	+ "any\_of": [
		- {
			* "MIN\_PRICE": {
				+ "inclusion": true,
				+ "values": 0,
				+ "negated": false}}]},
* "is\_featured": true,
* "type": "TOP\_SELLERS",
* "status": "ACTIVE",
* "created\_at": 1621350033000,
* "updated\_at": 1622742155000,
* "feed\_id": "2680059592705",
* "catalog\_type": "RETAIL"
}`Get product counts for a Product Group
--------------------------------------
Get a product counts for a given Catalogs Product Group owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`catalogs:read`) ##### path Parameters

|  |  |
| --- | --- |
| product\_group\_id required  | string^\d+$ Unique identifier of a product group
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**404** Product Group Not Found.

**409** Can't access this feature without an existing catalog.

**default** Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}/product\_countshttps://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}/product\_counts###  Response samples
* 200
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "in\_stock": 0,
* "out\_of\_stock": 0,
* "preorder": 0,
* "total": 0
}`List products for a Product Group
---------------------------------
Get a list of product pins for a given Catalogs Product Group Id owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``catalogs:read``pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| product\_group\_id required  | string^\d+$ Unique identifier of a product group
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid parameters.

**401** Unauthorized access.

**404** Catalogs product group not found.

**default** Unexpected error.

get/catalogs/product\_groups/{product\_group\_id}/productshttps://api.pinterest.com/v5/catalogs/product\_groups/{product\_group\_id}/products###  Response samples
* 200
* 400
* 401
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "metadata": {
			* "item\_id": "DS0294-L",
			* "item\_group\_id": "DS0294",
			* "availability": "IN\_STOCK",
			* "price": 24.99,
			* "sale\_price": 14.99,
			* "currency": "USD"},
		- "pin": {
			* "id": "813744226420795884",
			* "created\_at": "2020-01-01T20:10:40-00:00",
			* "link": "https://www.pinterest.com/",
			* "title": "string",
			* "description": "string",
			* "dominant\_color": "#6E7874",
			* "alt\_text": "string",
			* "creative\_type": "REGULAR",
			* "board\_id": "string",
			* "board\_section\_id": "string",
			* "board\_owner": {
				+ "username": "string"},
			* "is\_owner": true,
			* "media": {
				+ "media\_type": "string"},
			* "parent\_pin\_id": "string",
			* "is\_standard": true,
			* "has\_been\_promoted": true,
			* "note": "string",
			* "pin\_metrics": {
				+ "pin\_metrics": [
					- {
						* "90d": {
							+ "pin\_click": 7,
							+ "impression": 2,
							+ "clickthrough": 3},
						* "all\_time": {
							+ "pin\_click": 7,
							+ "impression": 2,
							+ "clickthrough": 3,
							+ "reaction": 10,
							+ "comment": 2}},
					- null]}}}],
* "bookmark": "string"
}`List filtered products
----------------------
List products Pins owned by the "operation user\_account" that meet the criteria specified in the Catalogs Product Group Filter given in the request.

* This endpoint has been implemented in POST to allow for complex filters. This specific POST endpoint is designed to be idempotent.
* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account: Owner, Admin, Catalogs Manager.

Learn more

 ratelimit-category:  catalogs\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``catalogs:read``pins:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Object holding a group of filters for a catalog product group

 One of object
|  |  |
| --- | --- |
| feed\_id required  | string^\d+$ Catalog Feed id pertaining to the catalog product group filter.
 |
| filters required  | CatalogsProductGroupFiltersAnyOf (object) or CatalogsProductGroupFiltersAllOf (object) (catalogs\_product\_group\_filters)  Object holding a group of filters for a catalog product group
 |
### Responses
**200** Success

**401** Unauthorized access.

**409** Conflict. Can't get products.

**default** Unexpected error.

post/catalogs/products/get\_by\_product\_group\_filtershttps://api.pinterest.com/v5/catalogs/products/get\_by\_product\_group\_filters###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "feed\_id": "2680059592705",
* "filters": {
	+ "any\_of": [
		- {
			* "MIN\_PRICE": {
				+ "inclusion": true,
				+ "values": 0,
				+ "negated": false}}]}
}`###  Response samples
* 200
* 401
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "metadata": {
			* "item\_id": "DS0294-L",
			* "item\_group\_id": "DS0294",
			* "availability": "IN\_STOCK",
			* "price": 24.99,
			* "sale\_price": 14.99,
			* "currency": "USD"},
		- "pin": {
			* "id": "813744226420795884",
			* "created\_at": "2020-01-01T20:10:40-00:00",
			* "link": "https://www.pinterest.com/",
			* "title": "string",
			* "description": "string",
			* "dominant\_color": "#6E7874",
			* "alt\_text": "string",
			* "creative\_type": "REGULAR",
			* "board\_id": "string",
			* "board\_section\_id": "string",
			* "board\_owner": {
				+ "username": "string"},
			* "is\_owner": true,
			* "media": {
				+ "media\_type": "string"},
			* "parent\_pin\_id": "string",
			* "is\_standard": true,
			* "has\_been\_promoted": true,
			* "note": "string",
			* "pin\_metrics": {
				+ "pin\_metrics": [
					- {
						* "90d": {
							+ "pin\_click": 7,
							+ "impression": 2,
							+ "clickthrough": 3},
						* "all\_time": {
							+ "pin\_click": 7,
							+ "impression": 2,
							+ "clickthrough": 3,
							+ "reaction": 10,
							+ "comment": 2}},
					- null]}}}],
* "bookmark": "string"
}`conversion\_events
==================
Submit conversion events via the Pinterest API.

Send conversions
----------------
The Pinterest API offers advertisers a way to send Pinterest their conversion information (including web conversions, in-app conversions, or even offline conversions) based on their `ad_account_id`. The request body should be a JSON object.

* This endpoint requires an `access_token` be generated through Ads Manager. Review the Conversions Guide for more details.
* The token's `user_account` must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Audience, Campaign. (Note that the token can be used across multiple ad accounts under an user ID.)
* This endpoint has a rate limit of 5,000 calls per minute per ad account.
* If the merchant is submitting this information using both Pinterest conversion tags and the Pinterest API, Pinterest will remove duplicate information before reporting. (Note that events that took place offline cannot be deduplicated.)

 ratelimit-category:  ads\_conversions sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) conversion\_token##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| test | boolean Include query param ?test=true to mark the request as a test request. The events will not be recorded but the API will still return the same response messages. Use this mode to verify your requests are working and your events are constructed correctly.
Warning: If you use this query parameter, be certain that it is off (set to false or deleted) before sending a legitimate (non-testing) request.
 |
##### Request Body schema: application/json
Conversion events.

|  |  |
| --- | --- |
| data required  | Array of objects  [ 1 .. 1000 ] items   |
### Responses
**200** Success

**400** The request was invalid.

**401** Not authorized to send conversion events

**403** Unauthorized access.

**422** Not all events were successfully processed.

**429** This request exceeded a rate limit. This can happen if the client exceeds one
of the published rate limits within a short time window.

**503** The endpoint has been ramped down and is currently not accepting any traffic.

**default** Unexpected errors

post/ad\_accounts/{ad\_account\_id}/eventshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/events###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "event\_name": "checkout",
		- "action\_source": "app\_ios",
		- "event\_time": 1451431341,
		- "event\_id": "eventId0001",
		- "event\_source\_url": "https://www.my-clothing-shop.org/",
		- "opt\_out": false,
		- "partner\_name": "ss-partnername",
		- "user\_data": {
			* "em": [
				+ "411e44ce1261728ffd2c0686e44e3fffe413c0e2c5adc498bc7da883d476b9c8",
				+ "09831ea51bd1b7b32a836683a00a9ccaf3d05f59499f42d9883412ed79289969"],
			* "hashed\_maids": [
				+ "0192518eb84137ccfe82c8b6322d29631dae7e28ed9d0f6dd5f245d73a58c5f1",
				+ "837b850ac46d62b2272a71de73c27801ff011ac1e36c5432620c8755cf90db46"],
			* "client\_ip\_address": "216.3.128.12",
			* "client\_user\_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_13\_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"},
		- "custom\_data": {
			* "currency": "USD",
			* "value": "72.39",
			* "content\_ids": [
				+ "red-pinterest-shirt-logo-1",
				+ "purple-pinterest-shirt-logo-3"],
			* "content\_name": "pinterest-themed-clothing",
			* "content\_category": "shirts",
			* "content\_brand": "pinterest-brand",
			* "contents": [
				+ {
					- "id": "red-pinterest-shirt-logo-1",
					- "item\_price": "1325.12",
					- "quantity": 5,
					- "item\_name": "pinterest-clothing-shirt",
					- "item\_category": "pinterest-entertainment",
					- "item\_brand": "pinterest"}],
			* "num\_items": 2,
			* "order\_id": "my\_order\_id",
			* "search\_string": "sample string",
			* "opt\_out\_type": "LDP",
			* "np": "ss-company"},
		- "app\_id": "429047995",
		- "app\_name": "Pinterest",
		- "app\_version": "7.9",
		- "device\_brand": "Apple",
		- "device\_carrier": "T-Mobile",
		- "device\_model": "iPhone X",
		- "device\_type": "iPhone",
		- "os\_version": "12.1.4",
		- "wifi": false,
		- "language": "en"}]
}`###  Response samples
* 200
* 400
* 401
* 403
* 422
* 429
* 503
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "num\_events\_received": 0,
* "num\_events\_processed": 0,
* "events": [
	+ {
		- "status": "processed",
		- "error\_message": "string",
		- "warning\_message": "string"}]
}`conversion\_tags
================
View, create, or update conversion tags.

Get conversion tags
-------------------
List conversion tags associated with an ad account.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| filter\_deleted | boolean Default:  false  Example:  filter\_deleted=trueFilter out deleted tags.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tagshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "ad\_account\_id": "549755885175",
		- "code\_snippet": "<script type=text/javascript> [...]",
		- "enhanced\_match\_status": "VALIDATION\_COMPLETE",
		- "id": "2617998078212",
		- "last\_fired\_time\_ms": 1599030000000,
		- "name": "ACME Checkout Test Tag",
		- "status": "ACTIVE",
		- "version": "3",
		- "configs": {
			* "aem\_enabled": true,
			* "md\_frequency": 0.6,
			* "aem\_fnln\_enabled": true,
			* "aem\_ph\_enabled": true,
			* "aem\_ge\_enabled": true,
			* "aem\_db\_enabled": true,
			* "aem\_loc\_enabled": true}}]
}`Create conversion tag
---------------------
Create a conversion tag, also known as Pinterest tag, with the option to enable enhanced match.

The Pinterest Tag tracks actions people take on the ad account’ s website after they view the ad account's ad on Pinterest. The advertiser needs to customize this tag to track conversions.

For more information, see:

Set up the Pinterest tag

Pinterest Tag

Enhanced match

 sandbox:  disabled ratelimit-category:  ads\_write##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Conversion Tag to create

|  |  |
| --- | --- |
| name required  | string (name)  Conversion tag name.
 |
| aem\_enabled | boolean (aem\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match email is enabled. See Enhanced match for more information.
 |
| md\_frequency | number (md\_frequency)  Nullable  Default:  1 Metadata ingestion frequency.
 |
| aem\_fnln\_enabled | boolean (aem\_fnln\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match name is enabled. See Enhanced match for more information.
 |
| aem\_ph\_enabled | boolean (aem\_ph\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match phone is enabled. See Enhanced match for more information.
 |
| aem\_ge\_enabled | boolean (aem\_ge\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match gender is enabled. See Enhanced match for more information.
 |
| aem\_db\_enabled | boolean (aem\_db\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match birthdate is enabled. See Enhanced match for more information.
 |
| aem\_loc\_enabled | boolean (aem\_loc\_enabled)  Nullable  Default:  false Whether Automatic Enhanced Match location is enabled. See Enhanced match for more information.
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/conversion\_tagshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "ACME Tools Tag"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "code\_snippet": "<script type=text/javascript> [...]",
* "enhanced\_match\_status": "VALIDATION\_COMPLETE",
* "id": "2617998078212",
* "last\_fired\_time\_ms": 1599030000000,
* "name": "ACME Checkout Test Tag",
* "status": "ACTIVE",
* "version": "3",
* "configs": {
	+ "aem\_enabled": true,
	+ "md\_frequency": 0.6,
	+ "aem\_fnln\_enabled": true,
	+ "aem\_ph\_enabled": true,
	+ "aem\_ge\_enabled": true,
	+ "aem\_db\_enabled": true,
	+ "aem\_loc\_enabled": true}
}`Get Ocpm eligible conversion tags
---------------------------------
Get Ocpm eligible conversion tag events for an ad account.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**default** Unexpected errors

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/ocpm\_eligiblehttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/ocpm\_eligible###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "12345": [
	+ {
		- "conversion\_event": "PAGE\_LOAD",
		- "created\_time": 1564768710,
		- "conversion\_tag\_id": "2614324385652",
		- "ad\_account\_id": "549757463328"},
	+ {
		- "conversion\_event": "CHECKOUT",
		- "created\_time": 1564710210,
		- "conversion\_tag\_id": "2614324315793",
		- "ad\_account\_id": "549757463328"}]
}`Get page visit conversion tags
------------------------------
Get all page visit conversion tag events for an ad account.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/page\_visithttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/page\_visit###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "conversion\_event": "PAGE\_LOAD",
		- "conversion\_tag\_id": "2614324385652",
		- "ad\_account\_id": "549757463328",
		- "created\_time": 1564768710}],
* "bookmark": "string"
}`Get conversion tag
------------------
Get information about an existing conversion tag.

 sandbox:  disabled ratelimit-category:  ads\_read##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| conversion\_tag\_id required  | string  <= 18 characters ^\d+$  Example:  2617998078212Id of the conversion tag.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/conversion\_tags/{conversion\_tag\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/conversion\_tags/{conversion\_tag\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549755885175",
* "code\_snippet": "<script type=text/javascript> [...]",
* "enhanced\_match\_status": "VALIDATION\_COMPLETE",
* "id": "2617998078212",
* "last\_fired\_time\_ms": 1599030000000,
* "name": "ACME Checkout Test Tag",
* "status": "ACTIVE",
* "version": "3",
* "configs": {
	+ "aem\_enabled": true,
	+ "md\_frequency": 0.6,
	+ "aem\_fnln\_enabled": true,
	+ "aem\_ph\_enabled": true,
	+ "aem\_ge\_enabled": true,
	+ "aem\_db\_enabled": true,
	+ "aem\_loc\_enabled": true}
}`customer\_lists
===============
View, create, or update customer lists.

Create customer lists
---------------------
Create a customer list from your records(hashed or plain-text email addresses, or hashed MAIDs or IDFAs).

A customer list is one of the four types of Pinterest audiences: for more information, see Audience targeting
or the Audiences section of the ads management guide.

**Please review our requirements for what type of information is allowed when uploading a customer list.**

When you create a customer list, the system scans the list for existing Pinterest accounts;
the list must include at least 100 Pinterest accounts. Your original list will be deleted when the matching process
is complete. The filtered list – containing only the Pinterest accounts that were included in your starting
list – is what will be used to create the audience.

Note that once you have created your customer list, you must convert it into an audience (of the “ CUSTOMER\_LIST” type)
using the create audience endpoint before it can be used.
 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Parameters to get Customer lists info

|  |  |
| --- | --- |
| name required  | string (name)  Customer list name.
 |
| records required  | string (records)  Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5.
 |
| list\_type | string (list\_type)  Default:  "EMAIL" Enum: "EMAIL" "IDFA" "MAID" "LR\_ID" "DLX\_ID" "HASHED\_PINNER\_ID"  User list type
 |
| exceptions | object (exceptions)  Customer list errors.
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/customer\_listshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "The Glengarry Glen Ross leads",
* "records": "email1@pinterest.com,email2@pinterest.com,..<more records>",
* "list\_type": "EMAIL",
* "exceptions": { }
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549756359984",
* "created\_time": 1452208622,
* "id": "643",
* "name": "The Glengarry Glen Ross leads",
* "num\_batches": 2,
* "num\_removed\_user\_records": 0,
* "num\_uploaded\_user\_records": 11,
* "status": "PROCESSING",
* "type": "customerlist",
* "updated\_time": 1461269616,
* "exceptions": { }
}`Get customer lists
------------------
Get a set of customer lists including id and name based on the filters provided.

(Customer lists are a type of audience.) For more information, see
Audience targeting
 or the Audiences
section of the ads management guide.
 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/customer\_listshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "ad\_account\_id": "549756359984",
		- "created\_time": 1452208622,
		- "id": "643",
		- "name": "The Glengarry Glen Ross leads",
		- "num\_batches": 2,
		- "num\_removed\_user\_records": 0,
		- "num\_uploaded\_user\_records": 11,
		- "status": "PROCESSING",
		- "type": "customerlist",
		- "updated\_time": 1461269616,
		- "exceptions": { }}],
* "bookmark": "string"
}`Get customer list
-----------------
Gets a specific customer list given the customer list ID.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| customer\_list\_id required  | string  <= 18 characters ^\d+$ Unique identifier of a customer list
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549756359984",
* "created\_time": 1452208622,
* "id": "643",
* "name": "The Glengarry Glen Ross leads",
* "num\_batches": 2,
* "num\_removed\_user\_records": 0,
* "num\_uploaded\_user\_records": 11,
* "status": "PROCESSING",
* "type": "customerlist",
* "updated\_time": 1461269616,
* "exceptions": { }
}`Update customer list
--------------------
Append or remove records to/from an existing customer list. (A customer list is one of the four types of Pinterest audiences.)

When you add records to an existing customer list, the system scans the additions for existing Pinterest
accounts; those are the records that will be added to your “CUSTOMER\_LIST” audience. Your original list of records
 to add will be deleted when the matching process is complete.

For more information, see Audience targeting
or the Audiences
section of the ads management guide.
 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| customer\_list\_id required  | string  <= 18 characters ^\d+$ Unique identifier of a customer list
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| records required  | string (records)  Records list. Can be any combination of emails, MAIDs, or IDFAs. Emails must be lowercase and can be plain text or hashed using SHA1, SHA256, or MD5. MAIDs and IDFAs must be hashed with SHA1, SHA256, or MD5.
 |
| operation\_type required  | string (operation\_type)  Enum: "ADD" "REMOVE"  User list operation type (add or remove)
 |
| exceptions | object (Generic exception class to be used within schemas)   |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/customer\_lists/{customer\_list\_id}###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "records": "email2@pinterest.com,email6@pinterest.com,",
* "operation\_type": "REMOVE",
* "exceptions": {
	+ "code": 2,
	+ "message": "Advertiser not found."}
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "ad\_account\_id": "549756359984",
* "created\_time": 1452208622,
* "id": "643",
* "name": "The Glengarry Glen Ross leads",
* "num\_batches": 2,
* "num\_removed\_user\_records": 0,
* "num\_uploaded\_user\_records": 11,
* "status": "PROCESSING",
* "type": "customerlist",
* "updated\_time": 1461269616,
* "exceptions": { }
}`integrations
============
View, create, or update commerce integrations.

Create commerce integration
---------------------------
Create commerce integration metadata to link an external business ID with a Pinterest merchant & ad account.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### Request Body schema: application/json
Parameters to get create/update the Integration Metadata

|  |  |
| --- | --- |
| external\_business\_id | string Nullable  External business ID for the integration.
 |
| connected\_merchant\_id | string  |
| connected\_advertiser\_id | string  |
| connected\_lba\_id | string  |
| connected\_tag\_id | string  |
| partner\_access\_token | string  |
| partner\_refresh\_token | string  |
| partner\_primary\_email | string  |
| partner\_access\_token\_expiry | integer  |
| partner\_refresh\_token\_expiry | integer  |
| scopes | string  |
| additional\_id\_1 | string  |
| partner\_metadata | string  |
### Responses
**200** Success

**404** Integration not found.

**409** Can't access this integration metadata.

**default** Unexpected error.

post/integrations/commercehttps://api.pinterest.com/v5/integrations/commerce###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "external\_business\_id": "string",
* "connected\_merchant\_id": "string",
* "connected\_advertiser\_id": "string",
* "connected\_lba\_id": "string",
* "connected\_tag\_id": "string",
* "partner\_access\_token": "string",
* "partner\_refresh\_token": "string",
* "partner\_primary\_email": "string",
* "partner\_access\_token\_expiry": 0,
* "partner\_refresh\_token\_expiry": 0,
* "scopes": "string",
* "additional\_id\_1": "string",
* "partner\_metadata": "string"
}`###  Response samples
* 200
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "7329167449607351372",
* "external\_business\_id": "1238401984",
* "connected\_merchant\_id": "1445572885401",
* "connected\_user\_id": "871939315263957401",
* "connected\_advertiser\_id": "549764738871",
* "connected\_lba\_id": "871939315263957402",
* "connected\_tag\_id": "2412141155151",
* "partner\_access\_token\_expiry": 1621350033000,
* "partner\_refresh\_token\_expiry": 1621350033000,
* "scopes": "accounts:read",
* "created\_timestamp": 1621350033000,
* "updated\_timestamp": 1621350033000,
* "additional\_id\_1": "128464",
* "partner\_metadata": ""
}`Get commerce integration
------------------------
Get commerce integration metadata associated with the given external business ID.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required  | string External business ID for the integration.
 |
### Responses
**200** Success

**404** Integration not found.

**409** Can't access this integration metadata.

**default** Unexpected error.

get/integrations/commerce/{external\_business\_id}https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}###  Response samples
* 200
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "7329167449607351372",
* "external\_business\_id": "1238401984",
* "connected\_merchant\_id": "1445572885401",
* "connected\_user\_id": "871939315263957401",
* "connected\_advertiser\_id": "549764738871",
* "connected\_lba\_id": "871939315263957402",
* "connected\_tag\_id": "2412141155151",
* "partner\_access\_token\_expiry": 1621350033000,
* "partner\_refresh\_token\_expiry": 1621350033000,
* "scopes": "accounts:read",
* "created\_timestamp": 1621350033000,
* "updated\_timestamp": 1621350033000,
* "additional\_id\_1": "128464",
* "partner\_metadata": ""
}`Update commerce integration
---------------------------
Update commerce integration metadata for the given external business ID.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required  | string External business ID for the integration.
 |
##### Request Body schema: application/json
Parameters to get create/update the Integration Metadata

|  |  |
| --- | --- |
| connected\_merchant\_id | string  |
| connected\_advertiser\_id | string  |
| connected\_lba\_id | string  |
| connected\_tag\_id | string  |
| partner\_access\_token | string  |
| partner\_refresh\_token | string  |
| partner\_primary\_email | string  |
| partner\_access\_token\_expiry | number  |
| partner\_refresh\_token\_expiry | number  |
| scopes | string  |
| additional\_id\_1 | string  |
| partner\_metadata | string  |
### Responses
**200** Success

**404** Integration not found.

**409** Can't access this integration metadata.

**default** Unexpected error.

patch/integrations/commerce/{external\_business\_id}https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "connected\_merchant\_id": "string",
* "connected\_advertiser\_id": "string",
* "connected\_lba\_id": "string",
* "connected\_tag\_id": "string",
* "partner\_access\_token": "string",
* "partner\_refresh\_token": "string",
* "partner\_primary\_email": "string",
* "partner\_access\_token\_expiry": 0,
* "partner\_refresh\_token\_expiry": 0,
* "scopes": "string",
* "additional\_id\_1": "string",
* "partner\_metadata": "string"
}`###  Response samples
* 200
* 404
* 409
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "7329167449607351372",
* "external\_business\_id": "1238401984",
* "connected\_merchant\_id": "1445572885401",
* "connected\_user\_id": "871939315263957401",
* "connected\_advertiser\_id": "549764738871",
* "connected\_lba\_id": "871939315263957402",
* "connected\_tag\_id": "2412141155151",
* "partner\_access\_token\_expiry": 1621350033000,
* "partner\_refresh\_token\_expiry": 1621350033000,
* "scopes": "accounts:read",
* "created\_timestamp": 1621350033000,
* "updated\_timestamp": 1621350033000,
* "additional\_id\_1": "128464",
* "partner\_metadata": ""
}`Delete commerce integration
---------------------------
Delete commerce integration metadata for the given external business ID.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| external\_business\_id required  | string External business ID for the integration.
 |
### Responses
**204** Commerce Integration deleted successfully

**default** Unexpected error.

delete/integrations/commerce/{external\_business\_id}https://api.pinterest.com/v5/integrations/commerce/{external\_business\_id}###  Response samples
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 0,
* "message": "string"
}`Receives batched logs from integration applications.
----------------------------------------------------
This endpoint receives batched logs from integration applications on partner platforms.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### Request Body schema: application/json
Ingest log information from external integration application.

|  |  |
| --- | --- |
| logs required  | Array of objects (IntegrationLog)   |
### Responses
**200** Success.

**400** Bad request.

**default** Unexpected error

post/integrations/logshttps://api.pinterest.com/v5/integrations/logs###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "logs": [
	+ {
		- "client\_timestamp": 0,
		- "event\_type": "APP",
		- "log\_level": "INFO",
		- "external\_business\_id": "string",
		- "advertiser\_id": "string",
		- "merchant\_id": "string",
		- "tag\_id": "string",
		- "feed\_profile\_id": "string",
		- "message": "string",
		- "app\_version\_number": "string",
		- "platform\_version\_number": "string",
		- "error": {
			* "cause": "string",
			* "column\_number": 0,
			* "file\_name": "string",
			* "line\_number": 0,
			* "message": "string",
			* "message\_detail": "string",
			* "name": "string",
			* "number": 0,
			* "stack\_trace": "string"},
		- "request": {
			* "method": "GET",
			* "host": "string",
			* "path": "string",
			* "request\_headers": {
				+ "property1": "string",
				+ "property2": "string"},
			* "response\_headers": {
				+ "property1": "string",
				+ "property2": "string"},
			* "response\_status\_code": 0}}]
}`###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "message": "string"
}`Get integration metadata list
-----------------------------
Get integration metadata list.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**default** Unexpected error.

get/integrationshttps://api.pinterest.com/v5/integrations###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "7329123456789012345",
		- "external\_business\_id": "1234567890",
		- "connected\_merchant\_id": "1234567890123",
		- "connected\_user\_id": "123456789012345678",
		- "connected\_advertiser\_id": "123456789012",
		- "connected\_lba\_id": "871234567890123456",
		- "connected\_tag\_id": "2412345678901",
		- "partner\_access\_token": "ABCLUOJS5XDMWDE",
		- "partner\_refresh\_token": "ABCLUOJS5XDMWDE",
		- "partner\_primary\_email": "partner@server.com",
		- "partner\_access\_token\_expiry": 1621350033000,
		- "partner\_refresh\_token\_expiry": 1621350033000,
		- "scopes": "accounts:read",
		- "partner\_metadata": "",
		- "additional\_id\_1": "123456",
		- "created\_time": 1621350033000,
		- "updated\_time": 1621350033000}],
* "bookmark": "string"
}`Get integration metadata
------------------------
Get integration metadata by ID.
Note: If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| id required  | string Integration ID.
 |
### Responses
**200** Success

**404** Integration not found.

**default** Unexpected error.

get/integrations/{id}https://api.pinterest.com/v5/integrations/{id}###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "7329123456789012345",
* "external\_business\_id": "1234567890",
* "connected\_merchant\_id": "1234567890123",
* "connected\_user\_id": "123456789012345678",
* "connected\_advertiser\_id": "123456789012",
* "connected\_lba\_id": "871234567890123456",
* "connected\_tag\_id": "2412345678901",
* "partner\_access\_token": "ABCLUOJS5XDMWDE",
* "partner\_refresh\_token": "ABCLUOJS5XDMWDE",
* "partner\_primary\_email": "partner@server.com",
* "partner\_access\_token\_expiry": 1621350033000,
* "partner\_refresh\_token\_expiry": 1621350033000,
* "scopes": "accounts:read",
* "partner\_metadata": "",
* "additional\_id\_1": "123456",
* "created\_time": 1621350033000,
* "updated\_time": 1621350033000
}`keywords
========
View, create or update keywords.

Get keywords
------------
Get a list of keywords based on the filters provided. If no filter is provided, it will default to the ad\_account\_id filter, which means it will only return keywords that specifically have parent\_id set to the ad\_account\_id. Note: Keywords can have ad\_account\_ids, campaign\_ids, and ad\_group\_ids set as their parent\_ids. Keywords created through Ads Manager will have their parent\_id set to an ad\_group\_id, not ad\_account\_id.

For more information, see Keyword targeting.

**Notes:**
 * Advertisers and campaigns can only be assigned keywords with excluding ('\_NEGATIVE').
* All keyword match types are available for ad groups.
 For more information on match types, see match type enums.

**Returns:**
 * A successful call returns an object containing an array of new keyword objects and an empty "errors" object array.
* An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the "errors" object array:

```
 { "keywords": [], "errors": [ { "data": { "archived": null, "match_type": "EXACT", "parent_type": null, "value": "foobar", "parent_id": null, "type": "keyword", "id": null }, "error_messages": [ "Advertisers and Campaigns only accept excluded targeting attributes." ] } } 
```
 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| campaign\_id | string  <= 18 characters ^\d+$ Campaign Id to use to filter the results.
 |
| ad\_group\_id | string  <= 18 characters ^\d+$  Example:  ad\_group\_id=123123123Ad group Id.
 |
| match\_types | Array of strings (MatchType)   [ 1 .. 5 ] items Items Enum: "BROAD" "PHRASE" "EXACT" "EXACT\_NEGATIVE" "PHRASE\_NEGATIVE"   Example:  match\_types=BROADKeyword match type
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/keywordshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "archived": false,
		- "id": "383791336903426391",
		- "parent\_id": "383791336903426391",
		- "parent\_type": "campaign",
		- "type": "keyword",
		- "bid": 200000,
		- "match\_type": "BROAD",
		- "value": "string"}],
* "bookmark": "string"
}`Create keywords
---------------
Create keywords for following entity types(advertiser, campaign, ad group or ad).
 For more information, see Keyword targeting.

**Notes:**
 * Advertisers and campaigns can only be assigned keywords with excluding ('\_NEGATIVE').
* All keyword match types are available for ad groups.
 For more information on match types, see match type enums.

**Returns:**
 * A successful call returns an object containing an array of new keyword objects and an empty "errors" object array.
* An unsuccessful call returns an empty keywords array, and, instead, inserts the entire object with nulled/negated properties into the "errors" object array:

```
 { "keywords": [], "errors": [ { "data": { "archived": null, "match_type": "EXACT", "parent_type": null, "value": "foobar", "parent_id": null, "type": "keyword", "id": null }, "error_messages": [ "Advertisers and Campaigns only accept excluded targeting attributes." ] } } 
```

**Rate limit**: WRITE.
 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| keywords required  | Array of objects (KeywordsCommon)  Keyword JSON array. Each array element has 3 fields
 |
| parent\_id required  | string (parent\_id) ^((AG)|C)?\d+$ Keyword parent entity ID (advertiser, campaign, ad group).
 |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/keywordshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "keywords": [
	+ {
		- "bid": 200000,
		- "match\_type": "BROAD",
		- "value": "string"}],
* "parent\_id": "383791336903426391"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "errors": [
	+ {
		- "data": {
			* "archived": false,
			* "id": "383791336903426391",
			* "parent\_id": "383791336903426391",
			* "parent\_type": "campaign",
			* "type": "keyword",
			* "bid": 200000,
			* "match\_type": "BROAD",
			* "value": "string"},
		- "error\_messages": [
			* "string"]}],
* "keywords": [
	+ {
		- "archived": false,
		- "id": "383791336903426391",
		- "parent\_id": "383791336903426391",
		- "parent\_type": "campaign",
		- "type": "keyword",
		- "bid": 200000,
		- "match\_type": "BROAD",
		- "value": "string"}]
}`Update keywords
---------------
Update one or more keywords' bid and archived fields.
 Archiving a keyword effectively deletes it - keywords no longer receive metrics and no longer visible within the parent entity's keywords list.
 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| keywords required  | Array of objects (keywords)  Keywords to update. Object array. Each object has 3 possible fields:1. "id": (required) keyword ID2. "archived": boolean. Should keyword be archived?3. "bid": numberFor example: [{"id":"2886610576653", "archived": false, "bid": 20000}, {"id":"2886610576654", "archived": true, "bid": 20000}, ...]
 |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/keywordshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "keywords": [
	+ {
		- "id": "2886364308355",
		- "archived": false,
		- "bid": 200000}]
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "errors": [
	+ {
		- "data": {
			* "archived": false,
			* "id": "383791336903426391",
			* "parent\_id": "383791336903426391",
			* "parent\_type": "campaign",
			* "type": "keyword",
			* "bid": 200000,
			* "match\_type": "BROAD",
			* "value": "string"},
		- "error\_messages": [
			* "string"]}],
* "keywords": [
	+ {
		- "archived": false,
		- "id": "383791336903426391",
		- "parent\_id": "383791336903426391",
		- "parent\_type": "campaign",
		- "type": "keyword",
		- "bid": 200000,
		- "match\_type": "BROAD",
		- "value": "string"}]
}`Get country's keyword metrics
-----------------------------
See keyword metrics for a specified country, aggregated across all of Pinterest.
(Definitions are available from the "Get delivery metrics definitions"
API endpoint).

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| country\_code required  | string  Example:  country\_code=USTwo letter country code (ISO 3166-1 alpha-2)
 |
| keywords required  | Array of strings  [ 1 .. 2000 ] items  Comma-separated keywords
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/keywords/metricshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/keywords/metrics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "data": [
	+ {
		- "keyword": "animals",
		- "metrics": {
			* "avg\_cpc\_in\_micro\_currency": 100000,
			* "keyword\_query\_volume": "5M+"}}]
}`List trending keywords
----------------------
Get the top trending search keywords among the Pinterest user audience.

Trending keywords can be used to inform ad targeting, budget strategy, and creative decisions about which products and Pins will resonate with your audience.

Geographic, demographic and interest-based filters are available to narrow down to the top trends among a specific audience. Multiple trend types are supported that can be used to identify newly-popular, evergreen or seasonal keywords.

For an interactive way to explore this data, please visit trends.pinterest.com.
 ratelimit-category:  trends\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### path Parameters

|  |  |
| --- | --- |
| region required  | string (Region)  Enum: "US" "CA" "DE" "FR" "ES" "IT" "DE+AT+CH" "GB+IE" "IT+ES+PT+GR+MT" "PL+RO+HU+SK+CZ" "SE+DK+FI+NO" "NL+BE+LU" "AR" "BR" "CO" "MX" "MX+AR+CO+CL" "AU+NZ"   Example:  GB+IEThe geographic region of interest. Only top trends within the specified region will be returned.
The `region` parameter is formatted as ISO 3166-2 country codes delimited by `+`, corresponding to the following geographic areas:
* `US` - United States
* `CA` - Canada
* `DE` - Germany
* `FR` - France
* `ES` - Spain
* `IT` - Italy
* `DE+AT+CH` - Germanic countries
* `GB+IE` - Great Britain & Ireland
* `IT+ES+PT+GR+MT` - Southern Europe
* `PL+RO+HU+SK+CZ` - Eastern Europe
* `SE+DK+FI+NO` - Nordic countries
* `NL+BE+LU` - Benelux
* `AR` - Argentina
* `BR` - Brazil
* `CO` - Colombia
* `MX` - Mexico
* `MX+AR+CO+CL` - Hispanic LatAm
* `AU+NZ` - Australasia

 |
| trend\_type required  | string (TrendType)  Enum: "growing" "monthly" "yearly" "seasonal"   Example:  monthlyThe methodology used to rank how trendy a keyword is.
* `growing` trends have high upward growth in search volume over the last quarter
* `monthly` trends have high search volume in the last month
* `yearly` trends have high search volume in the last year
* `seasonal` trends have high upward growth in search volume over the last month and exhibit a seasonal recurring pattern (typically annual)

 |
##### query Parameters

|  |  |
| --- | --- |
| interests | Array of strings (Interest) Items Enum: "animals" "architecture" "art" "beauty" "childrens\_fashion" "design" "diy\_and\_crafts" "education" "electronics" "entertainment" "event\_planning" "finance" "food\_and\_drinks" "gardening" "health" "home\_decor" "mens\_fashion" "parenting" "quotes" "sport" … 4 more  Example:  interests=beauty&interests=womens\_fashionIf set, filters the results to trends associated with the specified interests.
If unset, trends for all interests will be returned.
The list of supported interests is:
* `animals` - Animals
* `architecture` - Architecture
* `art` - Art
* `beauty` - Beauty
* `childrens_fashion` - Children's Fashion
* `design` - Design
* `diy_and_crafts` - DIY & Crafts
* `education` - Education
* `electronics` - Electronics
* `entertainment` - Entertainment
* `event_planning` - Event Planning
* `finance` - Finance
* `food_and_drinks` - Food & Drink
* `gardening` - Gardening
* `health` - Health
* `home_decor` - Home Decor
* `mens_fashion` - Men's Fashion
* `parenting` - Parenting
* `quotes` - Quotes
* `sport` - Sports
* `travel` - Travel
* `vehicles` - Vehicles
* `wedding` - Wedding
* `womens_fashion` - Women's Fashion

 |
| genders | Array of strings (Gender) Items Enum: "female" "male" "unknown"   Example:  genders=female&genders=unknownIf set, filters the results to trends among users who identify with the specified gender(s).
If unset, trends among all genders will be returned.
The `unknown` group includes users with unspecified or customized gender profile settings.
 |
| ages | Array of strings (AgeRange) Items Enum: "18-24" "25-34" "35-44" "45-49" "50-54" "55-64" "65+"   Example:  ages=35-44&ages=50-54If set, filters the results to trends among users in the specified age range(s).
If unset, trends among all age groups will be returned.
 |
| normalize\_against\_group | boolean Default:  false  Example:  normalize\_against\_group=trueGoverns how the resulting time series data will be normalized to a [0-100] scale.
By default (`false`), the data will be normalized independently for each keyword. The peak search volume observation in *each* keyword's time series will be represented by the value 100. This is ideal for analyzing when an individual keyword is expected to peak in interest.
If set to `true`, the data will be normalized as a group. The peak search volume observation across *all* keywords in the response will be represented by the value 100, and all other values scaled accordingly. Use this option when you wish to compare relative search volume between multiple keywords.
 |
| limit | integer  [ 1 .. 50 ]  Default:  50  Example:  limit=25The maximum number of trending keywords that will be returned. Keywords are returned in trend-ranked order, so a `limit` of 50 will return the top 50 trends.
 |
### Responses
**200** Success

**400** Invalid trending keywords request parameters

**default** Unexpected error

get/trends/keywords/{region}/top/{trend\_type}https://api.pinterest.com/v5/trends/keywords/{region}/top/{trend\_type}###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "trends": [
	+ {
		- "keyword": "couples halloween costumes",
		- "pct\_growth\_wow": 50,
		- "pct\_growth\_mom": 400,
		- "pct\_growth\_yoy": -5,
		- "time\_series": {
			* "2023-10-10": 31,
			* "2023-10-17": 54,
			* "2023-10-24": 77,
			* "2023-10-31": 100}}]
}`lead\_ads
=========
View, create, or update lead ads.

Create lead ads subscription
----------------------------
Create a lead ads webhook subscription.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.
* Advertisers can set up multiple integrations using ad\_account\_id + lead\_form\_id but only one integration per unique records.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Subscription to create.

|  |  |
| --- | --- |
| webhook\_url required  | string (webhook\_url)  Standard HTTPS webhook URL.
 |
| lead\_form\_id | string (Lead form ID) ^\d+$ Lead form ID.
 |
| partner\_access\_token | string Partner access token. Only for clients that requires authentication. We recommend to avoid this param.
 |
| partner\_refresh\_token | string Partner refresh token. Only for clients that requires authentication. We recommend to avoid this param.
 |
### Responses
**200** Success

**400** Invalid input parameters.

**403** Can't access this subscription.

**default** Unexpected error.

post/ad\_accounts/{ad\_account\_id}/leads/subscriptionshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "webhook\_url": "https://webhook.example.com/xyz",
* "lead\_form\_id": "383791336903426390"
}`###  Response samples
* 200
* 400
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "8078432025948590686",
* "cryptographic\_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",
* "cryptographic\_algorithm": "AES-256-GCM",
* "created\_time": 1699209842000
}`Get lead ads subscriptions
--------------------------
Get the advertiser's list of lead ads subscriptions.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**403** Can't access this subscription.

**default** Unexpected error.

get/ad\_accounts/{ad\_account\_id}/leads/subscriptionshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "lead\_form\_id": "383791336903426390",
		- "webhook\_url": "https://webhook.example.com/xyz",
		- "id": "8078432025948590686",
		- "user\_account\_id": "549755885175",
		- "ad\_account\_id": "549755885176",
		- "api\_version": "v5",
		- "cryptographic\_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",
		- "cryptographic\_algorithm": "AES-256-GCM",
		- "created\_time": 1699209842000}],
* "bookmark": "string"
}`Get lead ads subscription
-------------------------
Get a specific lead ads subscription record.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| subscription\_id required  | string^\d+$ Unique identifier of a subscription.
 |
### Responses
**200** Success

**400** Invalid input parameters.

**403** Can't access this subscription.

**404** Subscription not found.

**default** Unexpected error.

get/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}###  Response samples
* 200
* 400
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "lead\_form\_id": "383791336903426390",
* "webhook\_url": "https://webhook.example.com/xyz",
* "id": "8078432025948590686",
* "user\_account\_id": "549755885175",
* "ad\_account\_id": "549755885176",
* "api\_version": "v5",
* "cryptographic\_key": "ucvxbV2Tdss0vNeYsdh4Qfa/1Khm2b0PqXvXeTTZh54",
* "cryptographic\_algorithm": "AES-256-GCM",
* "created\_time": 1699209842000
}`Delete lead ads subscription
----------------------------
Delete an existing lead ads webhook subscription by ID.

* Only requests for the OWNER or ADMIN of the ad\_account will be allowed.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| subscription\_id required  | string^\d+$ Unique identifier of a subscription.
 |
### Responses
**204** Subscription deleted successfully

**400** Invalid input parameters.

**403** You are not authorized to delete this subscription.

**404** Subscription not found.

**default** Unexpected error.

delete/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/leads/subscriptions/{subscription\_id}###  Response samples
* 400
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 1,
* "message": "Advertiser ID must be numeric."
}`lead\_forms
===========
View lead forms.

Get lead forms
--------------
Gets all Lead Forms associated with an ad account ID.
Retrieving an advertiser's list of lead forms will only contain results if you're a part of the Lead ads beta. If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**400** Invalid ad account lead forms parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/lead\_formshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "name": "Lead Form 3/14/2023",
		- "privacy\_policy\_link": "https://www.advertisername.com/privacy-policy",
		- "has\_accepted\_terms": false,
		- "completion\_message": "Thank you for submitting. We will contact you soon.",
		- "status": "DRAFT",
		- "disclosure\_language": "By entering your personal information, you agree that your data will be collected and used.",
		- "questions": [
			* {
				+ "question\_type": "CUSTOM",
				+ "custom\_question\_field\_type": "CHECKBOX",
				+ "custom\_question\_label": "What is your favorite animal?",
				+ "custom\_question\_options": [
					- "Dog",
					- "Cat",
					- "Bird",
					- "Turtle"]}],
		- "id": "7765300871171",
		- "ad\_account\_id": "549755885175",
		- "created\_time": 1451431341,
		- "updated\_time": 1451431341}],
* "bookmark": "string"
}`Get lead form by id
-------------------
Gets a lead form given it's ID. It must also be associated with the provided ad account ID.
Retrieving an advertiser's lead form will only contain results if you're a part of the Lead ads beta. If you're interested in joining the beta, please reach out to your Pinterest account manager.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| lead\_form\_id required  | string^\d+$  Example:  1234567890123Unique identifier of a lead form.
 |
### Responses
**200** Success

**400** Invalid ad account lead forms parameters.

**404** The lead form ID for the given ad account ID does not exist.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}###  Response samples
* 200
* 400
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "name": "Lead Form 3/14/2023",
* "privacy\_policy\_link": "https://www.advertisername.com/privacy-policy",
* "has\_accepted\_terms": false,
* "completion\_message": "Thank you for submitting. We will contact you soon.",
* "status": "DRAFT",
* "disclosure\_language": "By entering your personal information, you agree that your data will be collected and used.",
* "questions": [
	+ {
		- "question\_type": "CUSTOM",
		- "custom\_question\_field\_type": "CHECKBOX",
		- "custom\_question\_label": "What is your favorite animal?",
		- "custom\_question\_options": [
			* "Dog",
			* "Cat",
			* "Bird",
			* "Turtle"]}],
* "id": "7765300871171",
* "ad\_account\_id": "549755885175",
* "created\_time": 1451431341,
* "updated\_time": 1451431341
}`Create lead form test data
--------------------------
Create lead form test data based on the list of answers provided as part of the body.

* List of answers should follow the questions creation order.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| lead\_form\_id required  | string^\d+$  Example:  1234567890123Unique identifier of a lead form.
 |
##### Request Body schema: application/json
Subscription to create.

|  |  |
| --- | --- |
| answers required  | Array of strings Test lead answers. Should follow the creation order.
 |
### Responses
**200** Success

**400** Invalid parameters.

**404** Lead not found.

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}/testhttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/lead\_forms/{lead\_form\_id}/test###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "answers": [
	+ "John",
	+ "Doe",
	+ "abc@email.com",
	+ "987654321"]
}`###  Response samples
* 200
* 400
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "subscription\_id": "8078432025948590686"
}`media
=====
Register and manage media uploads.

List media uploads
------------------
List media uploads filtered by given parameters.

**Learn more** about video Pin creation.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`pins:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** response

**default** Unexpected error

get/mediahttps://api.pinterest.com/v5/media###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "media\_id": "12345",
		- "media\_type": "video",
		- "status": "succeeded"}],
* "bookmark": "string"
}`Register media upload
---------------------
Register your intent to upload media

The response includes all of the information needed to upload the media
to Pinterest.

To upload the media, make an HTTP POST request (using curl, for
example) to upload\_url using the Content-Type header
value. Send the media file's contents as the request's file
parameter and also include all of the parameters from
upload\_parameters.

**Learn more** about video Pin creation.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`pins:read``pins:write`) ##### Request Body schema: application/json
Create a media upload request

|  |  |
| --- | --- |
| media\_type required  | string Value: "video"   |
### Responses
**201** response

**default** Unexpected error

post/mediahttps://api.pinterest.com/v5/media###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "media\_type": "video"
}`###  Response samples
* 201
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "media\_id": "12345",
* "media\_type": "video",
* "upload\_url": "https://pinterest-media-upload.s3-accelerate.amazonaws.com/",
* "upload\_parameters": {
	+ "x-amz-data": "20220127T185143Z",
	+ "x-amz-signature": "fcd6309a6aaee213348666a72abed8b44552a43acb6b340e8e1b288d21a5fe92",
	+ "key": "uploads/11/aa/22/3:video:203014033110991560:5212123920968240771",
	+ "policy": "eyJleHBpcmF0aW9uIjoiMj..==",
	+ "x-amz-credential": "ASIA6QZJ64OPIKV7FRVX/20220127/us-east-1/s3/aws4\_request",
	+ "x-amz-security-token": "IQoJb3JpZ2luX2VjEJr...==",
	+ "x-amz-algorithm": "AWS4-HMAC-SHA256",
	+ "Content-Type": "multipart/form-data"}
}`Get media upload details
------------------------
Get details for a registered media upload, including its current status.

**Learn more** about video Pin creation.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| media\_id required  | string^\d+$ Media identifier
 |
### Responses
**200** response

**404** Media upload not found

**default** Unexpected error

get/media/{media\_id}https://api.pinterest.com/v5/media/{media\_id}###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "media\_id": "12345",
* "media\_type": "video",
* "status": "succeeded"
}`oauth
=====
Generate and refresh OAuth access tokens.

Generate OAuth access token
---------------------------
Generate an OAuth access token by using an authorization code or a refresh token.

IMPORTANT: You need to start the OAuth flow via www.pinterest.com/oauth before calling this endpoint (or have an existing refresh token).

See Authentication for more.

**Parameter *refresh\_on* and its corresponding response type *everlasting\_refresh* are currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
basic##### Request Body schema: application/x-www-form-urlencoded
Generate an OAuth access token.

|  |  |
| --- | --- |
| grant\_type required  | string authorization\_codeauthorization\_coderefresh\_token |
| code required  | string  |
| redirect\_uri required  | string  |
### Responses
**200** response

**default** Unexpected error

post/oauth/tokenhttps://api.pinterest.com/v5/oauth/token###  Response samples
* 200
* default
Content typeapplication/jsonExampleauthorization\_codeauthorization\_coderefresh\_tokenintegration\_refresheverlasting\_refreshCopy Expand all  Collapse all `{* "response\_type": "authorization\_code",
* "access\_token": "string",
* "token\_type": "bearer",
* "expires\_in": 0,
* "scope": "string",
* "refresh\_token": "string",
* "refresh\_token\_expires\_in": 0
}`order\_lines
============
View order lines.

Get order lines
---------------
List existing order lines associated with an ad account.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/order\_lineshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/order\_lines###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "2680059592705",
		- "type": "orderline",
		- "ad\_account\_id": "549755885175",
		- "purchase\_order\_id": "PO12345",
		- "start\_time": 1452208622,
		- "end\_time": 1461269616,
		- "budget": 5000000,
		- "paid\_budget": 5000000,
		- "status": "ACTIVE",
		- "name": "Order Line Name 1",
		- "paid\_type": "PAID",
		- "campaign\_ids": [
			* "626735565838"]}],
* "bookmark": "string"
}`Get order line
--------------
Get a specific existing order line associated with an ad account.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| order\_line\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an order line.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/order\_lines/{order\_line\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/order\_lines/{order\_line\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "2680059592705",
* "type": "orderline",
* "ad\_account\_id": "549755885175",
* "purchase\_order\_id": "PO12345",
* "start\_time": 1452208622,
* "end\_time": 1461269616,
* "budget": 5000000,
* "paid\_budget": 5000000,
* "status": "ACTIVE",
* "name": "Order Line Name 1",
* "paid\_type": "PAID",
* "campaign\_ids": [
	+ "626735565838"]
}`pins
====
View, create, update, or delete information about Pins.

List Pins
---------
Get a list of the Pins owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.
* All Pins owned by the "operation user\_account" are included, regardless of who owns the board they are on.
Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| pin\_filter | string Enum: "exclude\_native" "exclude\_repins" "has\_been\_promoted"  Pin filter.
 |
| include\_protected\_pins | boolean Default:  false Specify if return pins from protected boards
 |
| pin\_type | string Value: "PRIVATE"  The type of pins to return, currently only enabled for private pins
 |
| creative\_types | Array of stringsItems Enum: "REGULAR" "VIDEO" "SHOPPING" "CAROUSEL" "MAX\_VIDEO" "SHOP\_THE\_PIN" "COLLECTION" "IDEA"   Example:  creative\_types=REGULARPin creative types filter. **Note:** SHOP\_THE\_PIN has been deprecated. Please use COLLECTION instead.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| pin\_metrics | boolean Default:  false Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then.
 |
### Responses
**200** Success

**400** Invalid pin filter value

**default** Unexpected error

get/pinshttps://api.pinterest.com/v5/pins###  Request samples
* curl
* curl (Sandbox)
Copy
```
curl --location --request GET 'https://api.pinterest.com/v5/pins' \
--header 'Authorization: Bearer <Add your token here>' \
--header 'Content-Type: application/json'
```
###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "813744226420795884",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "link": "https://www.pinterest.com/",
		- "title": "string",
		- "description": "string",
		- "dominant\_color": "#6E7874",
		- "alt\_text": "string",
		- "creative\_type": "REGULAR",
		- "board\_id": "string",
		- "board\_section\_id": "string",
		- "board\_owner": {
			* "username": "string"},
		- "is\_owner": true,
		- "media": {
			* "media\_type": "string"},
		- "parent\_pin\_id": "string",
		- "is\_standard": true,
		- "has\_been\_promoted": true,
		- "note": "string",
		- "pin\_metrics": {
			* "pin\_metrics": [
				+ {
					- "90d": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3},
					- "all\_time": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3,
						* "reaction": 10,
						* "comment": 2}},
				+ null]}}],
* "bookmark": "string"
}`Create Pin
----------
Create a Pin on a board or board section owned by the "operation user\_account".

Note: If the current "operation user\_account" (defined by the access token) has access to another user's Ad Accounts via Pinterest Business Access, you can modify your request to make use of the current operation\_user\_account's permissions to those Ad Accounts by including the ad\_account\_id in the path parameters for the request (e.g. .../?ad\_account\_id=12345&...).

* This function is intended solely for publishing new content created by the user. If you are interested in saving content created by others to your Pinterest boards, sometimes called 'curated content', please use our Save button instead. For more tips on creating fresh content for Pinterest, review our Content App Solutions Guide.

**Learn more** about video Pin creation.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write``pins:read``pins:write`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Create a new Pin.

|  |  |
| --- | --- |
| link | string  <= 2048 characters  Nullable   |
| title | string  <= 100 characters  Nullable   |
| description | string  <= 800 characters  Nullable   |
| dominant\_color | string Nullable  Dominant pin color. Hex number, e.g. "#6E7874".
 |
| alt\_text | string  <= 500 characters  Nullable   |
| board\_id | string^\d+$ The board to which this Pin belongs.
 |
| board\_section\_id | string Nullable ^\d+$ The board section to which this Pin belongs.
 |
| media\_source | object Pin media source.
 |
| parent\_pin\_id | string Nullable ^\d+$ The source pin id if this pin was saved from another pin. Learn more.
 |
| note | string Nullable  Private note for this Pin. Learn more.
 |
### Responses
**201** Successful pin creation.

**400** Invalid Pin parameters response

**403** The Pin's image is too small, too large or is broken

**404** Board or section not found

**429** This request exceeded a rate limit. This can happen if the client exceeds one
of the published rate limits or if multiple write operations are applied to
an object within a short time window.

**default** Unexpected error

post/pinshttps://api.pinterest.com/v5/pins###  Request samples
* Payload
* Python SDK
* curl
* curl (Sandbox)
Content typeapplication/jsonCopy Expand all  Collapse all `{* "link": "https://www.pinterest.com/",
* "title": "string",
* "description": "string",
* "dominant\_color": "#6E7874",
* "alt\_text": "string",
* "board\_id": "string",
* "board\_section\_id": "string",
* "media\_source": {
	+ "source\_type": "image\_base64",
	+ "content\_type": "image/jpeg",
	+ "data": "string",
	+ "is\_standard": true},
* "parent\_pin\_id": "string",
* "note": "string"
}`###  Response samples
* 201
* 400
* 403
* 404
* 429
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "813744226420795884",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "link": "https://www.pinterest.com/",
* "title": "string",
* "description": "string",
* "dominant\_color": "#6E7874",
* "alt\_text": "string",
* "creative\_type": "REGULAR",
* "board\_id": "string",
* "board\_section\_id": "string",
* "board\_owner": {
	+ "username": "string"},
* "is\_owner": true,
* "media": {
	+ "media\_type": "string"},
* "parent\_pin\_id": "string",
* "is\_standard": true,
* "has\_been\_promoted": true,
* "note": "string",
* "pin\_metrics": {
	+ "pin\_metrics": [
		- {
			* "90d": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3},
			* "all\_time": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3,
				+ "reaction": 10,
				+ "comment": 2}},
		- null]}
}`Get Pin
-------
Get a Pin owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| pin\_id required  | string Unique identifier of a Pin.
 |
##### query Parameters

|  |  |
| --- | --- |
| pin\_metrics | boolean Default:  false Specify whether to return 90d and lifetime Pin metrics. Total comments and total reactions are only available with lifetime Pin metrics. If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** response

**403** Not authorized to access board or Pin.

**404** Pin not found.

**default** Unexpected error

get/pins/{pin\_id}https://api.pinterest.com/v5/pins/{pin\_id}###  Request samples
* Python SDK
* curl
* curl (Sandbox)
Copy
```
# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started
from pinterest.organic.pins import Pin
# Pin information can be fetched from profile page or from list pin method here:
# https://developers.pinterest.com/docs/api/v5/#operation/pins/list
PIN_ID="<Add your pin id here>"
pin_get = Pin(pin_id=PIN_ID)
print("Pin Id: %s, Pin Title:%s" %(pin_get.id, pin_get.title))
```
###  Response samples
* 200
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "813744226420795884",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "link": "https://www.pinterest.com/",
* "title": "string",
* "description": "string",
* "dominant\_color": "#6E7874",
* "alt\_text": "string",
* "creative\_type": "REGULAR",
* "board\_id": "string",
* "board\_section\_id": "string",
* "board\_owner": {
	+ "username": "string"},
* "is\_owner": true,
* "media": {
	+ "media\_type": "string"},
* "parent\_pin\_id": "string",
* "is\_standard": true,
* "has\_been\_promoted": true,
* "note": "string",
* "pin\_metrics": {
	+ "pin\_metrics": [
		- {
			* "90d": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3},
			* "all\_time": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3,
				+ "reaction": 10,
				+ "comment": 2}},
		- null]}
}`Delete Pin
----------
Delete a Pins owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write``pins:read``pins:write`) ##### path Parameters

|  |  |
| --- | --- |
| pin\_id required  | string Unique identifier of a Pin.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**204** Successfully deleted Pin

**403** Not authorized to access board or Pin.

**404** Pin not found.

**default** Unexpected error

delete/pins/{pin\_id}https://api.pinterest.com/v5/pins/{pin\_id}###  Request samples
* Python SDK
* curl
* curl (Sandbox)
Copy
```
# Follow this link for initial setup: https://github.com/pinterest/pinterest-python-sdk#getting-started
from pinterest.organic.pins import Pin
# Pin information can be fetched from profile page or from create/list pin method here:
# https://developers.pinterest.com/docs/api/v5/#operation/pins/list
PIN_ID="<Add your pin id here>"
pin_delete=Pin.delete(pin_id=PIN_ID)
print("Pin was deleted? %s" % (pin_delete))
```
###  Response samples
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 403,
* "message": "Not authorized to access board or Pin."
}`Update Pin
----------
Update a pin owned by the "operating user\_account".

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account:

* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write``pins:read``pins:write`) ##### path Parameters

|  |  |
| --- | --- |
| pin\_id required  | string Unique identifier of a Pin.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json

|  |  |
| --- | --- |
| alt\_text | string  <= 500 characters  Nullable  Pin's alternative text.
 |
| board\_id | string Nullable ^\d+$ The id of the board to move the Pin onto.
 |
| board\_section\_id | string Nullable ^\d+$ Board section ID.
 |
| description | string  <= 800 characters  Nullable  Pin description - 800 characters maximum.
 |
| link | string  <= 2048 characters  Nullable  URL viewer is taken to when they click pin.
 |
| title | string  <= 100 characters  Nullable  The native pin title that creators explicitly prefer to display.
 |
| carousel\_slots | Array of objects Carousel Pin slots data.
 |
| note | string Nullable  Private note for this Pin. Learn more.
 |
### Responses
**200** response

**403** Not authorized to update Pin.

**404** Pin not found.

**429** This request exceeded a rate limit. This can happen if the client exceeds one
of the published rate limits or if multiple write operations are applied to
an object within a short time window.

**default** Unexpected error

patch/pins/{pin\_id}https://api.pinterest.com/v5/pins/{pin\_id}###  Request samples
* Payload
* curl
* curl (Sandbox)
Content typeapplication/jsonCopy Expand all  Collapse all `{* "alt\_text": "string",
* "board\_id": "string",
* "board\_section\_id": "string",
* "description": "string",
* "link": "https://www.pinterest.com/",
* "title": "string",
* "carousel\_slots": [
	+ {
		- "title": "string",
		- "description": "string",
		- "link": "string"}],
* "note": "string"
}`###  Response samples
* 200
* 403
* 404
* 429
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "813744226420795884",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "link": "https://www.pinterest.com/",
* "title": "string",
* "description": "string",
* "dominant\_color": "#6E7874",
* "alt\_text": "string",
* "creative\_type": "REGULAR",
* "board\_id": "string",
* "board\_section\_id": "string",
* "board\_owner": {
	+ "username": "string"},
* "is\_owner": true,
* "media": {
	+ "media\_type": "string"},
* "parent\_pin\_id": "string",
* "is\_standard": true,
* "has\_been\_promoted": true,
* "note": "string",
* "pin\_metrics": {
	+ "pin\_metrics": [
		- {
			* "90d": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3},
			* "all\_time": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3,
				+ "reaction": 10,
				+ "comment": 2}},
		- null]}
}`Get Pin analytics
-----------------
Get analytics for a Pin owned by the "operation user\_account" - or on a group board that has been shared with this account.

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account:

* For Pins on public or protected boards: Admin, Analyst.
* For Pins on secret boards: Admin.

If Pin was created before `2023-03-20` lifetime metrics will only be available for Video and Idea Pin formats. Lifetime metrics are available for all Pin formats since then.

 ratelimit-category:  org\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### path Parameters

|  |  |
| --- | --- |
| pin\_id required  | string Unique identifier of a Pin.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| app\_types | string Default:  "ALL" Enum: "ALL" "MOBILE" "TABLET" "WEB"  Apps or devices to get data for, default is all.
 |
| metric\_types required  | Array of strings or strings Pin metric types to get data for, default is all.
 |
| split\_field | string Default:  "NO\_SPLIT" Enum: "NO\_SPLIT" "APP\_TYPE"  How to split the data into groups. Not including this param means data won't be split.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** response

**400** Invalid pins analytics parameters.

**403** Not authorized to access board or Pin.

**404** Pin not found.

**default** Unexpected error

get/pins/{pin\_id}/analyticshttps://api.pinterest.com/v5/pins/{pin\_id}/analytics###  Response samples
* 200
* 400
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "property1": {
	+ "lifetime\_metrics": {
		- "TOTAL\_COMMENTS": 10,
		- "TOTAL\_REACTIONS": 12},
	+ "daily\_metrics": [
		- {
			* "data\_status": "READY",
			* "date": "2019-12-01",
			* "metrics": {
				+ "IMPRESSION": 240,
				+ "OUTBOUND\_CLICK": 20,
				+ "PIN\_CLICK": 37,
				+ "QUARTILE\_95\_PERCENT\_VIEW": 8,
				+ "SAVE": 20,
				+ "SAVE\_RATE": 0.18,
				+ "VIDEO\_10S\_VIEW": 2,
				+ "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
				+ "VIDEO\_MRC\_VIEW": 20,
				+ "VIDEO\_START": 29,
				+ "VIDEO\_V50\_WATCH\_TIME": 10031}}],
	+ "summary\_metrics": {
		- "IMPRESSION": 240,
		- "OUTBOUND\_CLICK": 20,
		- "PIN\_CLICK": 37,
		- "QUARTILE\_95\_PERCENT\_VIEW": 8,
		- "SAVE": 20,
		- "SAVE\_RATE": 0.18,
		- "VIDEO\_10S\_VIEW": 2,
		- "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
		- "VIDEO\_MRC\_VIEW": 20,
		- "VIDEO\_START": 29,
		- "VIDEO\_V50\_WATCH\_TIME": 10031}},
* "property2": {
	+ "lifetime\_metrics": {
		- "TOTAL\_COMMENTS": 10,
		- "TOTAL\_REACTIONS": 12},
	+ "daily\_metrics": [
		- {
			* "data\_status": "READY",
			* "date": "2019-12-01",
			* "metrics": {
				+ "IMPRESSION": 240,
				+ "OUTBOUND\_CLICK": 20,
				+ "PIN\_CLICK": 37,
				+ "QUARTILE\_95\_PERCENT\_VIEW": 8,
				+ "SAVE": 20,
				+ "SAVE\_RATE": 0.18,
				+ "VIDEO\_10S\_VIEW": 2,
				+ "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
				+ "VIDEO\_MRC\_VIEW": 20,
				+ "VIDEO\_START": 29,
				+ "VIDEO\_V50\_WATCH\_TIME": 10031}}],
	+ "summary\_metrics": {
		- "IMPRESSION": 240,
		- "OUTBOUND\_CLICK": 20,
		- "PIN\_CLICK": 37,
		- "QUARTILE\_95\_PERCENT\_VIEW": 8,
		- "SAVE": 20,
		- "SAVE\_RATE": 0.18,
		- "VIDEO\_10S\_VIEW": 2,
		- "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
		- "VIDEO\_MRC\_VIEW": 20,
		- "VIDEO\_START": 29,
		- "VIDEO\_V50\_WATCH\_TIME": 10031}}
}`Save Pin
--------
Save a Pin on a board or board section owned by the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.
Optional: Business Access: Specify an `ad_account_id` (obtained via List ad accounts) to use the owner of that ad\_account as the "operation user\_account". In order to do this, the token user\_account must have one of the following Business Access roles on the ad\_account:
* For Pins on public or protected boards: Owner, Admin, Analyst, Campaign Manager.
* For Pins on secret boards: Owner, Admin.
* Any Pin type can be saved: image Pin, video Pin, Idea Pin, product Pin, etc.
* Any public Pin can be saved given a pin ID.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:write``pins:read``pins:write`) ##### path Parameters

|  |  |
| --- | --- |
| pin\_id required  | string Unique identifier of a Pin.
 |
##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Request object used to save an existing pin

|  |  |
| --- | --- |
| board\_id | string Nullable ^\d+$ Unique identifier of the board to which the pin will be saved.
 |
| board\_section\_id | string Nullable ^\d+$ Unique identifier of the board section to which the pin will be saved.
 |
### Responses
**201** Successfully saved pin.

**403** Not authorized to access Board or Pin.

**404** Board or Pin not found.

**default** Unexpected error

post/pins/{pin\_id}/savehttps://api.pinterest.com/v5/pins/{pin\_id}/save###  Request samples
* Payload
* Python SDK
* curl
* curl (Sandbox)
Content typeapplication/jsonCopy Expand all  Collapse all `{* "board\_id": "string",
* "board\_section\_id": "string"
}`###  Response samples
* 201
* 403
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "813744226420795884",
* "created\_at": "2020-01-01T20:10:40-00:00",
* "link": "https://www.pinterest.com/",
* "title": "string",
* "description": "string",
* "dominant\_color": "#6E7874",
* "alt\_text": "string",
* "creative\_type": "REGULAR",
* "board\_id": "string",
* "board\_section\_id": "string",
* "board\_owner": {
	+ "username": "string"},
* "is\_owner": true,
* "media": {
	+ "media\_type": "string"},
* "parent\_pin\_id": "string",
* "is\_standard": true,
* "has\_been\_promoted": true,
* "note": "string",
* "pin\_metrics": {
	+ "pin\_metrics": [
		- {
			* "90d": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3},
			* "all\_time": {
				+ "pin\_click": 7,
				+ "impression": 2,
				+ "clickthrough": 3,
				+ "reaction": 10,
				+ "comment": 2}},
		- null]}
}`product\_group\_promotions
==========================
View, create, update, or delete information about promoted product groups.

Create product group promotions
-------------------------------
Add one or more product groups from your catalog to an existing ad group. (Product groups added to an ad group are a 'product group promotion.')

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
List of Product Group Promotions to create, size limit [1, 30].

|  |  |
| --- | --- |
| ad\_group\_id required  | string (ad\_group\_id) ^(AG)?\d+$ ID of the Ad Group the Product Group Promotion belongs to.
 |
| product\_group\_promotion required  | Array of objects (product\_group\_promotion)   |
### Responses
**200** Success

**default** Unexpected error

post/ad\_accounts/{ad\_account\_id}/product\_group\_promotionshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "product\_group\_promotion": [
	+ {
		- "slideshow\_collections\_description": "Description",
		- "creative\_type": "REGULAR",
		- "collections\_hero\_pin\_id": "123123",
		- "catalog\_product\_group\_name": "catalogProductGroupName",
		- "collections\_hero\_destination\_url": "http://www.pinterest.com",
		- "tracking\_url": "https://www.pinterest.com",
		- "slideshow\_collections\_title": "Title",
		- "is\_mdl": true,
		- "status": "ACTIVE"},
	+ {
		- "slideshow\_collections\_description": "Description",
		- "creative\_type": "REGULAR",
		- "collections\_hero\_pin\_id": "123123",
		- "catalog\_product\_group\_name": "catalogProductGroupName",
		- "collections\_hero\_destination\_url": "http://www.pinterest.com",
		- "tracking\_url": "https://www.pinterest.com",
		- "slideshow\_collections\_title": "Title",
		- "is\_mdl": true,
		- "status": "ACTIVE"}],
* "ad\_group\_id": "2680059592705"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "id": "2680059592705",
			* "ad\_group\_id": "2680059592705",
			* "bid\_in\_micro\_currency": 14000000,
			* "included": true,
			* "definition": "\*/product\_type\_0='kitchen'/product\_type\_1='beverage appliances'",
			* "relative\_definition": "product\_type\_1='beverage appliances'",
			* "parent\_id": "1231234",
			* "slideshow\_collections\_title": "slideshow title",
			* "slideshow\_collections\_description": "slideshow description",
			* "is\_mdl": true,
			* "status": "ACTIVE",
			* "tracking\_url": "https://www.pinterest.com",
			* "catalog\_product\_group\_id": "1231235",
			* "catalog\_product\_group\_name": "catalogProductGroupName",
			* "creative\_type": "REGULAR",
			* "collections\_hero\_pin\_id": "123123",
			* "collections\_hero\_destination\_url": "http://www.pinterest.com",
			* "grid\_click\_type": "CLOSEUP"},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Update product group promotions
-------------------------------
Update multiple existing Product Group Promotions (by product\_group\_id)

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### Request Body schema: application/json
Parameters to update Product group promotions

|  |  |
| --- | --- |
| ad\_group\_id required  | string (ad\_group\_id) ^(AG)?\d+$ ID of the ad group the product group belongs to.
 |
| product\_group\_promotion required  | Array of objects (product\_group\_promotion)   |
### Responses
**200** Success

**default** Unexpected error

patch/ad\_accounts/{ad\_account\_id}/product\_group\_promotionshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "product\_group\_promotion": [
	+ {
		- "catalog\_product\_group\_id": "1234123",
		- "slideshow\_collections\_description": "Description",
		- "creative\_type": "REGULAR",
		- "collections\_hero\_pin\_id": "123123",
		- "catalog\_product\_group\_name": "ProductGroupName",
		- "collections\_hero\_destination\_url": "http://www.pinterest.com",
		- "tracking\_url": "https://www.pinterest.com",
		- "slideshow\_collections\_title": "Title",
		- "status": "ACTIVE",
		- "id": "2680059592705"},
	+ {
		- "catalog\_product\_group\_id": "1231231",
		- "slideshow\_collections\_description": "Other description",
		- "creative\_type": "REGULAR",
		- "collections\_hero\_pin\_id": "123124",
		- "catalog\_product\_group\_name": "ProductGroupName",
		- "collections\_hero\_destination\_url": "http://www.pinterest.com",
		- "tracking\_url": "https://www.pinterest.com",
		- "slideshow\_collections\_title": "Title",
		- "status": "ACTIVE",
		- "id": "2680059592706"}],
* "ad\_group\_id": "26823439592705"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "id": "2680059592705",
			* "ad\_group\_id": "2680059592705",
			* "bid\_in\_micro\_currency": 14000000,
			* "included": true,
			* "definition": "\*/product\_type\_0='kitchen'/product\_type\_1='beverage appliances'",
			* "relative\_definition": "product\_type\_1='beverage appliances'",
			* "parent\_id": "1231234",
			* "slideshow\_collections\_title": "slideshow title",
			* "slideshow\_collections\_description": "slideshow description",
			* "is\_mdl": true,
			* "status": "ACTIVE",
			* "tracking\_url": "https://www.pinterest.com",
			* "catalog\_product\_group\_id": "1231235",
			* "catalog\_product\_group\_name": "catalogProductGroupName",
			* "creative\_type": "REGULAR",
			* "collections\_hero\_pin\_id": "123123",
			* "collections\_hero\_destination\_url": "http://www.pinterest.com",
			* "grid\_click\_type": "CLOSEUP"},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Get product group promotions
----------------------------
List existing product group promotions associated with an ad account.

Include either ad\_group\_id or product\_group\_promotion\_ids in your request.

**Note:** ad\_group\_ids and product\_group\_promotion\_ids are mutually exclusive parameters.
Only provide one. If multiple options are provided, product\_group\_promotion\_ids takes precedence over ad\_group\_ids. If none are provided, the endpoint returns an error.

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| product\_group\_promotion\_ids | Array of strings  [ 1 .. 100 ] items  List of Product group promotion Ids.
 |
| entity\_statuses | Array of strings Default:  ["ACTIVE","PAUSED"]Items Enum: "ACTIVE" "PAUSED" "ARCHIVED"   Example:  entity\_statuses=ACTIVEEntity status
 |
| ad\_group\_id | string  <= 18 characters ^\d+$  Example:  ad\_group\_id=123123123Ad group Id.
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| order | string Enum: "ASCENDING" "DESCENDING"   Example:  order=ASCENDINGThe order in which to sort the items returned: “ASCENDING” or “DESCENDING”
by ID. Note that higher-value IDs are associated with more-recently added
items.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_group\_promotionshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "id": "2680059592705",
			* "ad\_group\_id": "2680059592705",
			* "bid\_in\_micro\_currency": 14000000,
			* "included": true,
			* "definition": "\*/product\_type\_0='kitchen'/product\_type\_1='beverage appliances'",
			* "relative\_definition": "product\_type\_1='beverage appliances'",
			* "parent\_id": "1231234",
			* "slideshow\_collections\_title": "slideshow title",
			* "slideshow\_collections\_description": "slideshow description",
			* "is\_mdl": true,
			* "status": "ACTIVE",
			* "tracking\_url": "https://www.pinterest.com",
			* "catalog\_product\_group\_id": "1231235",
			* "catalog\_product\_group\_name": "catalogProductGroupName",
			* "creative\_type": "REGULAR",
			* "collections\_hero\_pin\_id": "123123",
			* "collections\_hero\_destination\_url": "http://www.pinterest.com",
			* "grid\_click\_type": "CLOSEUP"},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}],
* "bookmark": "string"
}`Get a product group promotion by id
-----------------------------------
Get a product group promotion by id

 ratelimit-category:  ads\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| product\_group\_promotion\_id required  | string  <= 18 characters ^\d+$ Unique identifier of a product group promotion
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_group\_promotions/{product\_group\_promotion\_id}https://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_group\_promotions/{product\_group\_promotion\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "data": {
			* "id": "2680059592705",
			* "ad\_group\_id": "2680059592705",
			* "bid\_in\_micro\_currency": 14000000,
			* "included": true,
			* "definition": "\*/product\_type\_0='kitchen'/product\_type\_1='beverage appliances'",
			* "relative\_definition": "product\_type\_1='beverage appliances'",
			* "parent\_id": "1231234",
			* "slideshow\_collections\_title": "slideshow title",
			* "slideshow\_collections\_description": "slideshow description",
			* "is\_mdl": true,
			* "status": "ACTIVE",
			* "tracking\_url": "https://www.pinterest.com",
			* "catalog\_product\_group\_id": "1231235",
			* "catalog\_product\_group\_name": "catalogProductGroupName",
			* "creative\_type": "REGULAR",
			* "collections\_hero\_pin\_id": "123123",
			* "collections\_hero\_destination\_url": "http://www.pinterest.com",
			* "grid\_click\_type": "CLOSEUP"},
		- "exceptions": [
			* {
				+ "code": 2,
				+ "message": "Advertiser not found."}]}]
}`Get product group analytics
---------------------------
Get analytics for the specified product groups in the specified `ad_account_id`, filtered by the specified options.

* The token's user\_account must either be the Owner of the specified ad account, or have one of the necessary roles granted to them via Business Access: Admin, Analyst, Campaign Manager.
* If granularity is not HOUR, the furthest back you can are allowed to pull data is 90 days before the current date in UTC time and the max time range supported is 90 days.
* If granularity is HOUR, the furthest back you can are allowed to pull data is 8 days before the current date in UTC time and the max time range supported is 3 days.

 ratelimit-category:  ads\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| product\_group\_ids required  | Array of strings  [ 1 .. 100 ] items  List of Product group Ids to use to filter the results.
 |
| columns required  | Array of stringsItems Enum: "SPEND\_IN\_MICRO\_DOLLAR" "PAID\_IMPRESSION" "SPEND\_IN\_DOLLAR" "CPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_MICRO\_DOLLAR" "ECPC\_IN\_DOLLAR" "CTR" "ECTR" "CAMPAIGN\_NAME" "PIN\_ID" "TOTAL\_ENGAGEMENT" "ENGAGEMENT\_1" "ENGAGEMENT\_2" "ECPE\_IN\_DOLLAR" "ENGAGEMENT\_RATE" "EENGAGEMENT\_RATE" "ECPM\_IN\_MICRO\_DOLLAR" "REPIN\_RATE" "CTR\_2" "CAMPAIGN\_ID" … 129 more  Example:  columns=TOTAL\_CONVERSIONSColumns to retrieve, encoded as a comma-separated string. **NOTE**: Any metrics defined as MICRO\_DOLLARS returns a value based on the advertiser profile's currency field. For USD,($1/1,000,000, or $0.000001 - one one-ten-thousandth of a cent). it's microdollars. Otherwise, it's in microunits of the advertiser's currency.For example, if the advertiser's currency is GBP (British pound sterling), all MICRO\_DOLLARS fields will be in GBP microunits (1/1,000,000 British pound).If a column has no value, it may not be returned
 |
| granularity required  | string (Granularity)  Enum: "TOTAL" "DAY" "HOUR" "WEEK" "MONTH"   Example:  granularity=DAYTOTAL - metrics are aggregated over the specified date range. DAY - metrics are broken down daily. HOUR - metrics are broken down hourly.WEEKLY - metrics are broken down weekly.MONTHLY - metrics are broken down monthly
 |
| click\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60   Example:  click\_window\_days=1Number of days to use as the conversion attribution window for a pin click action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| engagement\_window\_days | integer Default:  30 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for an engagement action. Engagements include saves, closeups, link clicks, and carousel card swipes. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `30` days.
 |
| view\_window\_days | integer Default:  1 Enum: 0 1 7 14 30 60  Number of days to use as the conversion attribution window for a view action. Applies to Pinterest Tag conversion metrics. Prior conversion tags use their defined attribution windows. If not specified, defaults to `1` day.
 |
| conversion\_report\_time | string Default:  "TIME\_OF\_AD\_ACTION" Enum: "TIME\_OF\_AD\_ACTION" "TIME\_OF\_CONVERSION"   Example:  conversion\_report\_time=TIME\_OF\_AD\_ACTIONThe date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.
 |
### Responses
**200** Success

**400** Invalid ad account ads analytics parameters.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_groups/analyticshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_groups/analytics###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "DATE": "2021-04-01",
	+ "PRODUCT\_GROUP\_ID": "74629351736530",
	+ "SPEND\_IN\_DOLLAR": 30,
	+ "TOTAL\_CLICKTHROUGH": 216}
]`product\_groups
===============
View, create, update, or delete information about product groups.

Get catalog product groups  Deprecated
--------------------------------------
This endpoint is completely deprecated. Please use List product groups from Catalogs API instead.

 ratelimit-category:  ads\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`ads:write`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| feed\_profile\_id | string  <= 18 characters ^\d+$ The feed profile id whose catalog product groups we want to return.
 |
### Responses
**200** Success

**400** Invalid ad account ads parameters.

**401** Access Denied. This can happen if account is not yet approved to operate as Merchant on Pinterest.

**404** Merchant data not found.

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/product\_groups/catalogshttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/product\_groups/catalogs###  Response samples
* 200
* 400
* 401
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "2680059592705",
		- "merchant\_id": "2680059592705",
		- "name": "Most Popular",
		- "filters": {
			* "1": [
				+ "123chars\_title"]},
		- "filter\_v2": {
			* "1": [
				+ "123chars\_title"]},
		- "type": {
			* "id": "549755885175",
			* "created\_at": "2020-01-01T20:10:40-00:00",
			* "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
			* "name": "Summer Recipes",
			* "description": "My favorite summer recipes",
			* "collaborator\_count": 17,
			* "pin\_count": 5,
			* "follower\_count": 13,
			* "media": {
				+ "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
				+ "pin\_thumbnail\_urls": [
					- "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
					- "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
					- "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
					- "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
			* "owner": {
				+ "username": "string"},
			* "privacy": "PUBLIC"},
		- "status": "ACTIVE",
		- "feed\_profile\_id": "string",
		- "created\_at": 1621350033000,
		- "last\_update": 1622742155000,
		- "product\_count": 6,
		- "featured\_position": 2}],
* "bookmark": "string"
}`resources
=========
View metadata about available metrics and targeting options in the Pinterest API.

Get ad accounts countries
-------------------------
Get Ad Accounts countries

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ### Responses
**200** Success

**default** Unexpected error

get/resources/ad\_account\_countrieshttps://api.pinterest.com/v5/resources/ad\_account\_countries###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "code": "US",
		- "currency": "Dollars",
		- "index": 1,
		- "name": "United States of America"}]
}`Get available metrics' definitions
----------------------------------
Get the definitions for ads and organic metrics available across both synchronous and asynchronous report endpoints.
The `display_name` attribute will match how the metric is named in our native tools like Ads Manager.
See Organic Analytics and Ads Analytics for more information.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read``pins:read``user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| report\_type | string Enum: "SYNC" "ASYNC"  Report type.
 |
### Responses
**200** Success

**default** Unexpected error

get/resources/delivery\_metricshttps://api.pinterest.com/v5/resources/delivery\_metrics###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "name": "AD\_GROUP\_ID",
		- "category": "ADS",
		- "definition": "Unique ID for your ad group",
		- "display\_name": "Ad group ID"}]
}`Get lead form questions
-----------------------
Get a list of all lead form question type names. Some questions might not be used.

**This endpoint is currently in beta and not available to all apps. Learn more.**

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ### Responses
**200** Success

**default** Unexpected error

get/resources/lead\_form\_questionshttps://api.pinterest.com/v5/resources/lead\_form\_questions###  Response samples
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 0,
* "message": "string"
}`Get metrics ready state
-----------------------
Learn whether conversion or non-conversion metrics are finalized and ready to query.

 ratelimit-category:  ads\_analytics sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### query Parameters

|  |  |
| --- | --- |
| date required  | string^(\d{4})-(\d{2})-(\d{2})$  Example:  date=2022-07-13Analytics reports request date (UTC). Format: YYYY-MM-DD
 |
### Responses
**200** Success

**default** Unexpected error

get/resources/metrics\_ready\_statehttps://api.pinterest.com/v5/resources/metrics\_ready\_state###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "conversion\_metrics\_ready": false,
* "non\_conversion\_metrics\_ready": false
}`Get interest details
--------------------
Get details of a specific interest given interest ID.
 Click here for a spreadsheet listing interests and their IDs.
 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| interest\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an interest.
 |
### Responses
**200** Success

**default** Unexpected error

get/resources/targeting/interests/{interest\_id}https://api.pinterest.com/v5/resources/targeting/interests/{interest\_id}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "945391946569",
* "name": "Dress",
* "child\_interests": [
	+ "string"],
* "level": 2
}`Get targeting options
---------------------
You can use targeting values in ads placement to define your intended audience. 
 Targeting metrics are organized around targeting specifications.
 For more information on ads targeting, see Audience targeting.

**Sample return:**

```
 [{"36313": "Australia: Moreton Bay - North", "124735": "Canada: North Battleford", "36109": "Australia: Murray", "36108": "Australia: Mid North Coast", "36101": "Australia: Capital Region", "811": "U.S.: Reno", "36103": "Australia: Central West", "36102": "Australia: Central Coast", "36105": "Australia: Far West and Orana", "36104": "Australia: Coffs Harbour - Grafton", "36107": "Australia: Illawarra", "36106": "Australia: Hunter Valley Exc Newcastle", "554017": "New Zealand: Wanganui", "554016": "New Zealand: Marlborough", "554015": "New Zealand: Gisborne", "554014": "New Zealand: Tararua", "554013": "New Zealand: Invercargill", "GR": "Greece", "554011": "New Zealand: Whangarei", "554010": "New Zealand: Far North", "717": "U.S.: Quincy-Hannibal-Keokuk", "716": "U.S.: Baton Rouge",...}] 
```
 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| targeting\_type required  | string (PublicTargetingType)  Enum: "APPTYPE" "GENDER" "LOCALE" "AGE\_BUCKET" "LOCATION" "GEO" "INTEREST" "KEYWORD" "AUDIENCE\_INCLUDE" "AUDIENCE\_EXCLUDE"   Example:  APPTYPEPublic targeting type.
 |
##### query Parameters

|  |  |
| --- | --- |
| client\_id | string  <= 18 characters ^\d+$  Example:  client\_id=1094834Client ID.
 |
| oauth\_signature | string  Example:  oauth\_signature=8209fOauth signature
 |
| timestamp | string\d+  Example:  timestamp=1618338184277Timestamp
 |
### Responses
**200** Success

**default** Unexpected error

get/resources/targeting/{targeting\_type}https://api.pinterest.com/v5/resources/targeting/{targeting\_type}###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "36313": "Australia: Moreton Bay - North",
	+ "124735": "Canada: North Battleford"}
]`search
======
Search for Pins and boards owned by the current user.

Search user's boards
--------------------
Search for boards for the "operation user\_account". This includes boards of all board types.

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See Understanding Business Access for more information.

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:read_secret`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| query | string Search query. Can contain pin description keywords or comma-separated pin IDs.
 |
### Responses
**200** response

**default** Unexpected error

get/search/boardshttps://api.pinterest.com/v5/search/boards###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "549755885175",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
		- "name": "Summer Recipes",
		- "description": "My favorite summer recipes",
		- "collaborator\_count": 17,
		- "pin\_count": 5,
		- "follower\_count": 13,
		- "media": {
			* "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
			* "pin\_thumbnail\_urls": [
				+ "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
				+ "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
				+ "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
				+ "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
		- "owner": {
			* "username": "string"},
		- "privacy": "PUBLIC"}],
* "bookmark": "string"
}`Search user's Pins
------------------
Search for pins for the "operation user\_account".

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See Understanding Business Access for more information.

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`boards:read``boards:read_secret``pins:read``pins:read_secret`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
| query required  | string  Example:  query=PlantsSearch query. Can contain pin description keywords or comma-separated pin IDs.
 |
| bookmark | string Cursor used to fetch the next page of items
 |
### Responses
**200** Success

**404** User not found

**default** Unexpected error

get/search/pinshttps://api.pinterest.com/v5/search/pins###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "813744226420795884",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "link": "https://www.pinterest.com/",
		- "title": "string",
		- "description": "string",
		- "dominant\_color": "#6E7874",
		- "alt\_text": "string",
		- "creative\_type": "REGULAR",
		- "board\_id": "string",
		- "board\_section\_id": "string",
		- "board\_owner": {
			* "username": "string"},
		- "is\_owner": true,
		- "media": {
			* "media\_type": "string"},
		- "parent\_pin\_id": "string",
		- "is\_standard": true,
		- "has\_been\_promoted": true,
		- "note": "string",
		- "pin\_metrics": {
			* "pin\_metrics": [
				+ {
					- "90d": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3},
					- "all\_time": {
						* "pin\_click": 7,
						* "impression": 2,
						* "clickthrough": 3,
						* "reaction": 10,
						* "comment": 2}},
				+ null]}}],
* "bookmark": "string"
}`Search pins by a given search term
----------------------------------
**This endpoint is currently in beta and not available to all apps. Learn more.**

Get the top 10 Pins by a given search term.

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`boards:read``pins:read`) ##### query Parameters

|  |  |
| --- | --- |
| term required  | string Search term to look up pins.
 |
| country\_code required  | string  Example:  country\_code=USTwo letter country code (ISO 3166-1 alpha-2)
 |
| bookmark | string Cursor used to fetch the next page of items
 |
| locale | string Search locale.
 |
| limit | integer  [ 1 .. 50 ]  Default:  10  Example:  limit=4Max search result size
 |
### Responses
**200** Success

**400** Invalid pins

**default** Unexpected error

get/search/partner/pinshttps://api.pinterest.com/v5/search/partner/pins###  Request samples
* curl
Copy
```
curl --location --request GET 'https://api.pinterest.com/v5/search/partner/pins' \
--header 'Authorization: Bearer <Add your token here>' \
--header 'Content-Type: application/json'
```
###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "media": {
			* "media\_type": "string"},
		- "alt\_text": "string",
		- "link": "https://www.pinterest.com/",
		- "title": "string",
		- "description": "string"}],
* "bookmark": "string"
}`terms
=====
View related and suggested terms for ads targeting.

List related terms
------------------
Get a list of terms logically related to each input term. 

Example: the term 'workout' would list related terms like 'one song workout', 'yoga workout', 'workout motivation', etc.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### query Parameters

|  |  |
| --- | --- |
| terms required  | Array of strings  Example:  terms=workoutList of input terms.
 |
### Responses
**200** Success

**400** Invalid terms related parameters.

**default** Unexpected error

get/terms/relatedhttps://api.pinterest.com/v5/terms/related###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "id": "clothes",
* "related\_term\_count": 2,
* "related\_terms\_list": [
	+ {
		- "term": "clothes",
		- "related\_terms": [
			* "shoes",
			* "cute clothes"]}]
}`List suggested terms
--------------------
Get popular search terms that begin with your input term. 

Example: 'sport' would return popular terms like 'sports bar' and 'sportswear', but not 'motor sports' since the phrase does not begin with the given term.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### query Parameters

|  |  |
| --- | --- |
| term required  | string  Example:  term=sportsInput term.
 |
| limit | integer  [ 1 .. 10 ]  Default:  4  Example:  limit=4Max suggested terms to return.
 |
### Responses
**200** Success

**400** Invalid terms suggested parameters.

**default** Unexpected error

get/terms/suggestedhttps://api.pinterest.com/v5/terms/suggested###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* "string"
]`terms\_of\_service
==================
View Advertising Terms Of Service.

Get terms of service
--------------------
Get the text of the terms of service and see whether the advertiser has accepted the terms of service.

 sandbox:  enabled ratelimit-category:  ads\_read##### Authorizations:
pinterest\_oauth2 (`ads:read`) ##### path Parameters

|  |  |
| --- | --- |
| ad\_account\_id required  | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
##### query Parameters

|  |  |
| --- | --- |
| include\_html | boolean Default:  false Return HTML in TOS text.
 |
| tos\_type | string Request type.
 |
### Responses
**200** Success

**default** Unexpected error

get/ad\_accounts/{ad\_account\_id}/terms\_of\_servicehttps://api.pinterest.com/v5/ad\_accounts/{ad\_account\_id}/terms\_of\_service###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "has\_accepted": true,
* "html": "example test",
* "id": "2650449554526",
* "ad\_account\_id": "549755885175"
}`user\_account
=============
View user accounts associated with a given access token.

Get user account
----------------
Get account information for the "operation user\_account"

* By default, the "operation user\_account" is the token user\_account.

If using Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account". See Understanding Business Access for more information.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** response

**403** Not authorized to access the user account.

**default** Unexpected error

get/user\_accounthttps://api.pinterest.com/v5/user\_account###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "account\_type": "PINNER",
* "id": "2783136121146311751",
* "profile\_image": "string",
* "website\_url": "string",
* "username": "string",
* "about": "string",
* "business\_name": "string",
* "board\_count": 14,
* "pin\_count": 339,
* "follower\_count": 10,
* "following\_count": 347,
* "monthly\_views": 163
}`Get user account analytics
--------------------------
Get analytics for the "operation user\_account"

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

 ratelimit-category:  org\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| from\_claimed\_content | string Default:  "BOTH" Enum: "OTHER" "CLAIMED" "BOTH"  Filter on Pins that match your claimed domain.
 |
| pin\_format | string Default:  "ALL" Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"  Pin formats to get data for, default is all.
 |
| app\_types | string Default:  "ALL" Enum: "ALL" "MOBILE" "TABLET" "WEB"  Apps or devices to get data for, default is all.
 |
| content\_type | string Default:  "ALL" Enum: "ALL" "PAID" "ORGANIC"  Filter to paid or organic data. Default is all.
 |
| source | string Default:  "ALL" Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"  Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts
 |
| metric\_types | Array of stringsItems Enum: "ENGAGEMENT" "ENGAGEMENT\_RATE" "IMPRESSION" "OUTBOUND\_CLICK" "OUTBOUND\_CLICK\_RATE" "PIN\_CLICK" "PIN\_CLICK\_RATE" "SAVE" "SAVE\_RATE"  Metric types to get data for, default is all. 
 |
| split\_field | string Default:  "NO\_SPLIT" Enum: "NO\_SPLIT" "APP\_TYPE" "OWNED\_CONTENT" "SOURCE" "PIN\_FORMAT"  How to split the data into groups. Not including this param means data won't be split.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid user accounts analytics parameters.

**403** Not authorized to access the user account analytics.

**default** Unexpected error

get/user\_account/analyticshttps://api.pinterest.com/v5/user\_account/analytics###  Response samples
* 200
* 400
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "property1": {
	+ "summary\_metrics": {
		- "CLOSEUP": 1,
		- "CLOSEUP\_RATE": 0,
		- "ENGAGEMENT": 1,
		- "ENGAGEMENT\_RATE": 0,
		- "IMPRESSION": 240,
		- "OUTBOUND\_CLICK": 20,
		- "OUTBOUND\_CLICK\_RATE": 0.08,
		- "PIN\_CLICK": 37,
		- "PIN\_CLICK\_RATE": 0.15,
		- "PROFILE\_VISIT": 0,
		- "QUARTILE\_95\_PERCENT\_VIEW": 8,
		- "SAVE": 20,
		- "SAVE\_RATE": 0.18,
		- "VIDEO\_10S\_VIEW": 2,
		- "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
		- "VIDEO\_MRC\_VIEW": 20,
		- "VIDEO\_START": 29,
		- "VIDEO\_V50\_WATCH\_TIME": 10031},
	+ "daily\_metrics": [
		- {
			* "data\_status": "READY",
			* "date": "2019-12-01",
			* "metrics": {
				+ "CLOSEUP": 1,
				+ "CLOSEUP\_RATE": 0,
				+ "ENGAGEMENT": 1,
				+ "ENGAGEMENT\_RATE": 0,
				+ "IMPRESSION": 240,
				+ "OUTBOUND\_CLICK": 20,
				+ "OUTBOUND\_CLICK\_RATE": 0.08,
				+ "PIN\_CLICK": 37,
				+ "PIN\_CLICK\_RATE": 0.15,
				+ "QUARTILE\_95\_PERCENT\_VIEW": 8,
				+ "SAVE": 20,
				+ "SAVE\_RATE": 0.18,
				+ "VIDEO\_10S\_VIEW": 2,
				+ "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
				+ "VIDEO\_MRC\_VIEW": 20,
				+ "VIDEO\_START": 29,
				+ "VIDEO\_V50\_WATCH\_TIME": 10031}}]},
* "property2": {
	+ "summary\_metrics": {
		- "CLOSEUP": 1,
		- "CLOSEUP\_RATE": 0,
		- "ENGAGEMENT": 1,
		- "ENGAGEMENT\_RATE": 0,
		- "IMPRESSION": 240,
		- "OUTBOUND\_CLICK": 20,
		- "OUTBOUND\_CLICK\_RATE": 0.08,
		- "PIN\_CLICK": 37,
		- "PIN\_CLICK\_RATE": 0.15,
		- "PROFILE\_VISIT": 0,
		- "QUARTILE\_95\_PERCENT\_VIEW": 8,
		- "SAVE": 20,
		- "SAVE\_RATE": 0.18,
		- "VIDEO\_10S\_VIEW": 2,
		- "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
		- "VIDEO\_MRC\_VIEW": 20,
		- "VIDEO\_START": 29,
		- "VIDEO\_V50\_WATCH\_TIME": 10031},
	+ "daily\_metrics": [
		- {
			* "data\_status": "READY",
			* "date": "2019-12-01",
			* "metrics": {
				+ "CLOSEUP": 1,
				+ "CLOSEUP\_RATE": 0,
				+ "ENGAGEMENT": 1,
				+ "ENGAGEMENT\_RATE": 0,
				+ "IMPRESSION": 240,
				+ "OUTBOUND\_CLICK": 20,
				+ "OUTBOUND\_CLICK\_RATE": 0.08,
				+ "PIN\_CLICK": 37,
				+ "PIN\_CLICK\_RATE": 0.15,
				+ "QUARTILE\_95\_PERCENT\_VIEW": 8,
				+ "SAVE": 20,
				+ "SAVE\_RATE": 0.18,
				+ "VIDEO\_10S\_VIEW": 2,
				+ "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
				+ "VIDEO\_MRC\_VIEW": 20,
				+ "VIDEO\_START": 29,
				+ "VIDEO\_V50\_WATCH\_TIME": 10031}}]}
}`Get user account top pins analytics
-----------------------------------
Gets analytics data about a user's top pins (limited to the top 50).

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

 ratelimit-category:  org\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`pins:read``user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| sort\_by required  | string Enum: "ENGAGEMENT" "IMPRESSION" "OUTBOUND\_CLICK" "PIN\_CLICK" "SAVE"  Specify sorting order for metrics
 |
| from\_claimed\_content | string Default:  "BOTH" Enum: "OTHER" "CLAIMED" "BOTH"  Filter on Pins that match your claimed domain.
 |
| pin\_format | string Default:  "ALL" Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"  Pin formats to get data for, default is all.
 |
| app\_types | string Default:  "ALL" Enum: "ALL" "MOBILE" "TABLET" "WEB"  Apps or devices to get data for, default is all.
 |
| content\_type | string Default:  "ALL" Enum: "ALL" "PAID" "ORGANIC"  Filter to paid or organic data. Default is all.
 |
| source | string Default:  "ALL" Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"  Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts
 |
| metric\_types | Array of stringsItems Enum: "ENGAGEMENT" "ENGAGEMENT\_RATE" "IMPRESSION" "OUTBOUND\_CLICK" "OUTBOUND\_CLICK\_RATE" "PIN\_CLICK" "PIN\_CLICK\_RATE" "SAVE" "SAVE\_RATE"  Metric types to get data for, default is all. 
 |
| num\_of\_pins | integer  [ 1 .. 50 ]  Default:  10  Example:  num\_of\_pins=25Number of pins to include, default is 10. Max is 50.
 |
| created\_in\_last\_n\_days | integer Value: 30   Example:  created\_in\_last\_n\_days=30Get metrics for pins created in the last "n" days.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**403** Not authorized to access the user account analytics.

**default** Unexpected error

get/user\_account/analytics/top\_pinshttps://api.pinterest.com/v5/user\_account/analytics/top\_pins###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "date\_availability": {
	+ "latest\_available\_timestamp": 1649116799000,
	+ "is\_realtime": false},
* "pins": [
	+ {
		- "metrics": {
			* "CLOSEUP": 1,
			* "CLOSEUP\_RATE": 0,
			* "ENGAGEMENT": 1,
			* "ENGAGEMENT\_RATE": 0,
			* "IMPRESSION": 240,
			* "OUTBOUND\_CLICK": 20,
			* "OUTBOUND\_CLICK\_RATE": 0.08,
			* "PIN\_CLICK": 37,
			* "PIN\_CLICK\_RATE": 0.15,
			* "QUARTILE\_95\_PERCENT\_VIEW": 8,
			* "SAVE": 20,
			* "SAVE\_RATE": 0.18,
			* "VIDEO\_10S\_VIEW": 2,
			* "VIDEO\_AVG\_WATCH\_TIME": 2507.75,
			* "VIDEO\_MRC\_VIEW": 20,
			* "VIDEO\_START": 29,
			* "VIDEO\_V50\_WATCH\_TIME": 10031},
		- "data\_status": {
			* "property1": "READY",
			* "property2": "READY"},
		- "pin\_id": "642396334344813594"}],
* "sort\_by": "IMPRESSION"
}`Get user account top video pins analytics
-----------------------------------------
Gets analytics data about a user's top video pins (limited to the top 50).

* By default, the "operation user\_account" is the token user\_account.

Optional: Business Access: Specify an ad\_account\_id to use the owner of that ad\_account as the "operation user\_account".

 ratelimit-category:  org\_analytics sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`pins:read``user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| start\_date required  | string <date>  Metric report start date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days back from today.
 |
| end\_date required  | string <date>  Metric report end date (UTC). Format: YYYY-MM-DD. Cannot be more than 90 days past start\_date.
 |
| sort\_by required  | string Enum: "IMPRESSION" "SAVE" "OUTBOUND\_CLICK" "VIDEO\_MRC\_VIEW" "VIDEO\_AVG\_WATCH\_TIME" "VIDEO\_V50\_WATCH\_TIME" "QUARTILE\_95\_PERCENT\_VIEW" "VIDEO\_10S\_VIEW" "VIDEO\_START"  Specify sorting order for video metrics
 |
| from\_claimed\_content | string Default:  "BOTH" Enum: "OTHER" "CLAIMED" "BOTH"  Filter on Pins that match your claimed domain.
 |
| pin\_format | string Default:  "ALL" Enum: "ALL" "ORGANIC\_IMAGE" "ORGANIC\_PRODUCT" "ORGANIC\_VIDEO" "ADS\_STANDARD" "ADS\_PRODUCT" "ADS\_VIDEO" "ADS\_IDEA" "PRODUCT" "REGULAR" "VIDEO"  Pin formats to get data for, default is all.
 |
| app\_types | string Default:  "ALL" Enum: "ALL" "MOBILE" "TABLET" "WEB"  Apps or devices to get data for, default is all.
 |
| content\_type | string Default:  "ALL" Enum: "ALL" "PAID" "ORGANIC"  Filter to paid or organic data. Default is all.
 |
| source | string Default:  "ALL" Enum: "ALL" "YOUR\_PINS" "OTHER\_PINS"  Filter to activity from Pins created and saved by your, or activity created and saved by others from your claimed accounts
 |
| metric\_types | Array of stringsItems Enum: "IMPRESSION" "SAVE" "VIDEO\_MRC\_VIEW" "VIDEO\_AVG\_WATCH\_TIME" "VIDEO\_V50\_WATCH\_TIME" "QUARTILE\_95\_PERCENT\_VIEW" "VIDEO\_10S\_VIEW" "VIDEO\_START" "OUTBOUND\_CLICK"  Metric types to get video data for, default is all. 
 |
| num\_of\_pins | integer  [ 1 .. 50 ]  Default:  10  Example:  num\_of\_pins=25Number of pins to include, default is 10. Max is 50.
 |
| created\_in\_last\_n\_days | integer Value: 30   Example:  created\_in\_last\_n\_days=30Get metrics for pins created in the last "n" days.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**403** Not authorized to access the user account analytics.

**default** Unexpected error

get/user\_account/analytics/top\_video\_pinshttps://api.pinterest.com/v5/user\_account/analytics/top\_video\_pins###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "date\_availability": {
	+ "latest\_available\_timestamp": 1649116799000,
	+ "is\_realtime": false},
* "pins": [
	+ {
		- "metrics": {
			* "IMPRESSION": 7,
			* "QUARTILE\_95\_PERCENT\_VIEW": 2,
			* "SAVE": 1,
			* "VIDEO\_10S\_VIEW": 5,
			* "VIDEO\_AVG\_WATCH\_TIME": 86989,
			* "VIDEO\_MRC\_VIEW": 2,
			* "VIDEO\_START": 2,
			* "VIDEO\_V50\_WATCH\_TIME": 173979,
			* "OUTBOUND\_CLICK": 2},
		- "data\_status": {
			* "property1": "READY",
			* "property2": "READY"},
		- "pin\_id": "642396334344813594"}],
* "sort\_by": "IMPRESSION"
}`List linked businesses
----------------------
Get a list of your linked business accounts.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ### Responses
**200** Success

**default** Unexpected error

get/user\_account/businesseshttps://api.pinterest.com/v5/user\_account/businesses###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `[* {
	+ "username": "username",
	+ "image\_small\_url": "https://www.example.com/dj23454f53dfk2324.jpg",
	+ "image\_medium\_url": "https://www.example.com/dj23454f53dfk2324.jpg",
	+ "image\_large\_url": "https://www.example.com/dj23454f53dfk2324.jpg",
	+ "image\_xlarge\_url": "https://www.example.com/dj23454f53dfk2324.jpg"}
]`List followers
--------------
Get a list of your followers.

 ratelimit-category:  ads\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**400** Invalid user id

**default** Unexpected error

get/user\_account/followershttps://api.pinterest.com/v5/user\_account/followers###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "username": "username",
		- "type": "user"}],
* "bookmark": "string"
}`List following
--------------
Get a list of who a certain user follows.

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| feed\_type | string (UserFollowingFeedType)  Default:  "ALL" Enum: "ALL" "RANKED" "CREATOR\_ONLY" "RANKED\_CREATOR\_ONLY"   Example:  feed\_type=CREATOR\_ONLYThrift param specifying what type of followees will be kept. Default to include all followees.
 |
| explicit\_following | boolean Default:  false Whether or not to include implicit user follows, which means followees with board follows. When explicit\_following is True, it means we only want explicit user follows.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** response

**default** Unexpected error

get/user\_account/followinghttps://api.pinterest.com/v5/user\_account/following###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "username": "username",
		- "type": "user"}],
* "bookmark": "string"
}`List following boards
---------------------
Get a list of the boards a user follows. The request returns a board summary object array.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
| explicit\_following | boolean Default:  false Whether or not to include implicit user follows, which means followees with board follows. When explicit\_following is True, it means we only want explicit user follows.
 |
| ad\_account\_id | string  <= 18 characters ^\d+$ Unique identifier of an ad account.
 |
### Responses
**200** Success

**400** Invalid user id

**default** Unexpected error

get/user\_account/following/boardshttps://api.pinterest.com/v5/user\_account/following/boards###  Response samples
* 200
* 400
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "id": "549755885175",
		- "created\_at": "2020-01-01T20:10:40-00:00",
		- "board\_pins\_modified\_at": "2020-01-01T20:10:40-00:00",
		- "name": "Summer Recipes",
		- "description": "My favorite summer recipes",
		- "collaborator\_count": 17,
		- "pin\_count": 5,
		- "follower\_count": 13,
		- "media": {
			* "image\_cover\_url": "https://i.pinimg.com/400x300/fd/cd/d5/fdcdd5a6d8a80824add0d054125cd957.jpg",
			* "pin\_thumbnail\_urls": [
				+ "https://i.pinimg.com/150x150/b4/57/10/b45710f1ede96af55230f4b43935c4af.jpg",
				+ "https://i.pinimg.com/150x150/dd/ff/46/ddff4616e39c1935cd05738794fa860e.jpg",
				+ "https://i.pinimg.com/150x150/84/ac/59/84ac59b670ccb5b903dace480a98930c.jpg",
				+ "https://i.pinimg.com/150x150/4c/54/6f/4c546f521be85e30838fb742bfff6936.jpg"]},
		- "owner": {
			* "username": "string"},
		- "privacy": "PUBLIC"}],
* "bookmark": "string"
}`Follow user
-----------
**This endpoint is currently in beta and not available to all apps. Learn more.**

Use this request, as a signed-in user, to follow another user.

 ratelimit-category:  org\_write sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:write`) ##### path Parameters

|  |  |
| --- | --- |
| username required  | string(?!^\d+$)^.+$  Example:  usernameA valid username
 |
##### Request Body schema: application/json
Follow a user.

|  |  |
| --- | --- |
| auto\_follow | boolean (auto\_follow)  Default:  false Whether this request comes as result of auto-follow after clicking on a link. Follow links can be used by partners on their site or in emails. Only selected partners can be followed this way. We verify that partner can be auto-followed.
 |
### Responses
**200** Success

**404** User not found

**default** Unexpected error

post/user\_account/following/{username}https://api.pinterest.com/v5/user\_account/following/{username}###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "auto\_follow": false
}`###  Response samples
* 200
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "username": "username",
* "type": "user"
}`Verify website
--------------
Verify a website as a signed-in user.

 ratelimit-category:  org\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:write`) ##### Request Body schema: application/json
Verify a website.

|  |  |
| --- | --- |
| website | string  |
| verification\_method | string Default:  "METATAG" Enum: "FILENAME" "METATAG" "DNSTXT"   |
### Responses
**200** Success

**default** Unexpected error

post/user\_account/websiteshttps://api.pinterest.com/v5/user\_account/websites###  Request samples
* Payload
Content typeapplication/jsonCopy Expand all  Collapse all `{* "website": "pintest-website-12345678.test/test\_1",
* "verification\_method": "METATAG"
}`###  Response samples
* 200
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "website": "mysite.test",
* "status": "success",
* "verified\_at": "2022-12-14T21:03:01.602000"
}`Get user websites
-----------------
Get user websites, claimed or not

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**403** Not authorized to access the user website list.

**default** Unexpected error

get/user\_account/websiteshttps://api.pinterest.com/v5/user\_account/websites###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "website": "mysite.test",
		- "status": "success",
		- "verified\_at": "2022-12-14T21:03:01.602000"}],
* "bookmark": "string"
}`Unverify website
----------------
Unverifu a website verified by the signed-in user.

 ratelimit-category:  org\_write sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:write`) ##### query Parameters

|  |  |
| --- | --- |
| website required  | string  Example:  website=mysite.testWebsite with path or domain only
 |
### Responses
**204** Successfully unverified website

**404** Website not in user list.

**default** Unexpected error

delete/user\_account/websiteshttps://api.pinterest.com/v5/user\_account/websites###  Response samples
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "code": 404,
* "message": "Website not in user list."
}`Get user verification code for website claiming
-----------------------------------------------
Get verification code for user to install on the website to claim it.

 ratelimit-category:  org\_read sandbox:  disabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ### Responses
**200** Success

**403** Not authorized to access the user verification code for website claiming.

**default** Unexpected error

get/user\_account/websites/verificationhttps://api.pinterest.com/v5/user\_account/websites/verification###  Response samples
* 200
* 403
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "verification\_code": "e1edcc1a43976c646367e9c6c9a9b7b6",
* "dns\_txt\_record": "pinterest-site-verification=e1edcc1a43976c646367e9c6c9a9b7b6",
* "metatag": "<meta name=\"p:domain\_verify\" content=\"e1edcc1a43976c646367e9c6c9a9b7b6\"/>",
* "filename": "pinterest-e1edc.html",
* "file\_content": "string"
}`List following interests
------------------------
Get a list of a user's following interests in one place.

 ratelimit-category:  org\_read sandbox:  enabled##### Authorizations:
pinterest\_oauth2 (`user_accounts:read`) ##### path Parameters

|  |  |
| --- | --- |
| username required  | string(?!^\d+$)^.+$  Example:  usernameA valid username
 |
##### query Parameters

|  |  |
| --- | --- |
| bookmark | string Cursor used to fetch the next page of items
 |
| page\_size | integer  [ 1 .. 250 ]  Default:  25 Maximum number of items to include in a single page of the response. See documentation on Pagination for more information.
 |
### Responses
**200** Success

**400** Invalid parameters

**401** Authorization failed

**404** User not found

**default** Unexpected error

get/users/{username}/interests/followhttps://api.pinterest.com/v5/users/{username}/interests/follow###  Response samples
* 200
* 400
* 401
* 404
* default
Content typeapplication/jsonCopy Expand all  Collapse all `{* "items": [
	+ {
		- "canonical\_url": "string",
		- "id": "903972677830",
		- "key": "man cave",
		- "name": "Man cave"}],
* "bookmark": "string"
}`