Graph API Reference v19.0: Application Page Activities - Documentation - Meta for Developers

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
Graph API Versionv19.0Application Page Activities
===========================
Reading
-------
You can't perform this operation on this endpoint.Creating
--------
You can make a POST request to `page_activities` edge from the following paths: * `/{application_id}/page_activities`
When posting to this edge, an Application will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_tracking_enabled`boolean | A person can choose to enable ad tracking on iOS 6+, and that choice is stored within the phone. You should fetch that and return it to Facebook so we know not to use the data for optimization. We will, however, use the data to report on a conversion. See here for an example of how Facebook fetches that variable. For devices running less than iOS 6, this query parameter can default to 1. Use 0 for disabled, 1 for enabled
 |
| `application_tracking_enabled`boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled
 |
| `custom_events`list<CustomEvent> | Custom events reported
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
| `logging_source`enum {MESSENGER\_BOT, DETECTION} | Specifies the event source
 |
| `logging_target`enum {APP, APP\_AND\_PAGE, PAGE} | Default value: `"APP"`whether the event is logged to app level or page level or both
 |
| `page_id`int64 | Specifies the Page ID associated with the messenger bot that logs the event
 |
| `page_scoped_user_id`int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.