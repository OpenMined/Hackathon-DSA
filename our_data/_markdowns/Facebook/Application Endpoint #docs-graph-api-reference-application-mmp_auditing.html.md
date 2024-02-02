Graph API Reference v19.0: Application Mmp Auditing - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Mmp Auditing
========================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `mmp_auditing` edge from the following paths: * `/{application_id}/mmp_auditing`
When posting to this edge, an Application will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on iOS or on Android
 |
| `attribution`string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3`
 |
| `attribution_model`string | attribution model that clients selected to be respected by MMP
 |
| `auditing_token`string | Token provided in claim response sent to MMP
 |
| `click_attr_window`int64 | Time window of click attribution
 |
| `custom_events`list<CustomEvent> | Custom app events that MMP are sending auditing events for
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
| `decline_reason`string | Reason that MMP rejected Facebook ads claim
 |
| `engagement_type`string | Engagement type that MMP explicitly reports
 |
| `event`string | Event type that Facebook claimed for
Required |
| `event_reported_time`int64 | Time that event reported to MMP
 |
| `fb_ad_id`int64 | FBID of the ads in Facebook claim
Required |
| `fb_click_time`int64 | Ad click time in Facebook claim
 |
| `fb_view_time`int64 | Ad view time in Facebook claim
 |
| `is_fb`boolean | Result that whether MMP attribute the event to Facebook ads
Required |
| `used_install_referrer`boolean | Identifies whether MMP used the install referrer
 |
| `view_attr_window`int64 | Time window of view attribution
 |
### Return Type
 Struct {`success`: bool, } Or Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.