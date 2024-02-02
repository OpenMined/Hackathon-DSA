Graph API Reference v19.0: Application Activities - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Graph API Versionv19.0Application Activities
======================
Application activities are events from your app.
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can use a user access token or app access token to log events to this endpoint.
You can make a POST request to `activities` edge from the following paths: * `/{application_id}/activities`
When posting to this edge, no Graph object will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on iOS or on Android
 |
| `advertiser_tracking_enabled`boolean | Specifies whether a person has enabled advertising tracking on their device. Set to 0 for disabled or 1 for enabled. You should fetch this data and return it to Meta will use the event data (from partners about user activities off Meta) pursuant to its Data Policy, including for ad reporting, fraud detection and to build and improve our products (including our ads delivery products), but will restrict use of data about that individual to personalize that user’s ads. For devices running earlier versions than iOS 6, this parameter should default to 1.
 |
| `anon_id`string | The ID of a person who has installed the app anonymously
 |
| `app_user_id`string | Specifies user id of an app user. Used internally by the iOS and Android SDKs for `MOBILE_APP_INSTALL` event
 |
| `application_tracking_enabled`boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled
 |
| `attribution`string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3`
 |
| `auto_publish`boolean | This field is not longer being used. Used to be used internally by Facebook's SDK
 |
| `bundle_id`string | Used internally by Facebook's SDK
 |
| `bundle_short_version`string | Used internally by Facebook's SDK
 |
| `bundle_version`string | Used internally by Facebook's SDK
 |
| `campaign_ids`string | Parameter passed via the deep link for Mobile App Engagement campaigns.
 |
| `click_id`string | click\_id
 |
| `consider_views`boolean | Specifies that view through data should be considered when determining the ad to attribute this install to. Clicks will always be considered first before views and views will only be returned if there was not a click on an ad for the app
 |
| `custom_events`list<CustomEvent> | Custom events reported, required with `CUSTOM_APP_EVENTS` events. Please see our App Events API, App Events for iOS and App Events for Android for more information
 |
| `_eventName`RegexParam | Event name, must match the regular expression /^[0-9a-zA-Z\_][0-9a-zA-Z \_-]{0,39}$/
Required |
| `_eventName_md5`RegexParam | MD5 hash of the event name, must match the regular expression /^[A-Fa-f0-9]{32}$/
 |
| `_valueToSum`float | Values to Sum
 |
| `_logTime`int64 | Time to Log
 |
| `_implicitlyLogged`int64 | Whether this is implicitly logged
 |
| `_isTimedEvent`boolean | Whether this is a timed event
 |
| `_session_id`string |  |
| `_app_user_id`string |  |
| `custom_events_file`file | Custom file, encoded as JSON that describes the event. Please encode as UTF-8 and attach with the mime type `application/json` or `content/unknown`
 |
| `device_token`string | A token used to identify the device on push networks
 |
| `event`enum {MOBILE\_APP\_INSTALL, CUSTOM\_APP\_EVENTS, DEFERRED\_APP\_LINK} | Event type, one of `MOBILE_APP_INSTALL`, `CUSTOM_APP_EVENTS` or `DEFERRED_APP_LINK`. If you are reporting a `MOBILE_APP_INSTALL` event, you must include either `attribution` or `advertiser_id` in the request
Required |
| `extinfo`Object | Extended device and source information array, used by Facebook's SDKs, MMPs and Bots for Messenger. This parameter is an array and must be in a specific format. Please see our App Events API for more information
 |
| `0`string | extinfo version
Required |
| `1`string | app package name
 |
| `2`string | short version (int or string)
 |
| `3`string | long version
 |
| `4`string | OS version
 |
| `5`string | device model name
 |
| `6`string | locale
 |
| `7`string | timezone abbreviation
 |
| `8`string | carrier
 |
| `9`int64 | screen width
 |
| `10`int64 | screen height
 |
| `11`string | screen density (float decimal , or .)
 |
| `12`int64 | CPU cores
 |
| `13`int64 | external storage size in GB
 |
| `14`int64 | free space on external storage in GB
 |
| `15`string | device timezone
 |
| `include_dwell_data`boolean | Specifies that view dwell ms should be returned as part of view through data
 |
| `include_video_data`boolean | Specifies that video view completion percentages should be returned as part of view through data
 |
| `install_referrer`string | 3rd party install referrer, currently available for Android only, see https://developers.google.com/analytics/devguides/collection/android/v4/campaigns
 |
| `installer_package`string | Used internally by the Android SDKs
 |
| `migration_bundle`string | Used internally by the iOS and Android SDKs
 |
| `page_id`int64 | Specifies the Page ID associated with the messenger bot that logs the event
 |
| `page_scoped_user_id`int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event
 |
| `receipt_data`string | The receipts of in-app purchase
 |
| `ud`JSON object | Optional user data parameters for advanced matchingProvide hashed fields as key/value pairs similar to the Pixel
 |
| `em`string | em
 |
| `fn`string | fn
 |
| `ln`string | ln
 |
| `ph`string | ph
 |
| `ge`string | ge
 |
| `dob`string | dob
 |
| `ct`string | ct
 |
| `st`string | st
 |
| `zp`string | zp
 |
| `extern_id`string | extern\_id
 |
| `db`string | db
 |
| `r1`string | r1
 |
| `r2`string | r2
 |
| `cn`string | cn
 |
| `r3`string | r3
 |
| `r4`string | r4
 |
| `r5`string | r5
 |
| `r6`string | r6
 |
| `r7`string | r7
 |
| `r8`string | r8
 |
| `country`string | country
 |
| `external_id`string | external\_id
 |
| `url_schemes`list<string> | Used internally by the iOS and Android SDKs
 |
| `user_id`string | user\_id
 |
| `user_id_type`enum {INSTANT\_GAMES\_PLAYER\_ID} | user\_id\_type
 |
| `vendor_id`string | vendor\_id
 |
| `windows_attribution_id`string | Attribution token used for Windows 10
 |
### Return Type
 Struct {`success`: bool, } Or Struct {`applink_class`: string, `applink_url`: string, `applink_args`: string, `is_fb`: bool, `is_paid`: bool, `account_id`: ad account id, `ad_id`: numeric string, `ad_objective_name`: string, `adgroup_id`: numeric string, `adgroup_name`: string, `campaign_id`: numeric string, `campaign_name`: string, `campaign_group_id`: numeric string, `campaign_group_name`: string, `click_time`: timestamp, `is_mobile_data_terms_signed`: bool, `is_external`: bool, `is_instagram`: bool, `is_view_through`: bool, `view_time`: timestamp, `is_playable_ad`: bool, `is_aaa_campaign`: bool, `creative_id`: numeric string, `engagement_type`: enum, } Or Struct {`success`: bool, `drop_reason`: string, }### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.