<div>

When posting to this edge, no Graph object will be created.

<div>

::: _57-c
+-----------------------------------+-----------------------------------+
| Parameter                         | Description                       |
+===================================+===================================+
| ` advertiser_id `                 | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Apple\'s Advertising Identifier   |
|                                   | (IDFA) or Google Android\'s       |
|                                   | advertising ID. You can see how   |
|                                   | Facebook fetches this on          |
|                                   | [iOS](https://l.f                 |
|                                   | acebook.com/l.php?u=https%3A%2F%2 |
|                                   | Fgithub.com%2Ffacebook%2Ffacebook |
|                                   | -ios-sdk%2Fblob%2F7fe08877ea773dc |
|                                   | 35a5e4d6d9d305fae57c513b6%2Fsrc%2 |
|                                   | FCore%2FFBUtility.m%23L334-L357&h |
|                                   | =AT2XFqAlT43G1WhBHzdKjIdRvFo9x7HC |
|                                   | E5yZTRiTcI39UYVXJeB6zYE-9F2dhmnxn |
|                                   | Al5Fem8JwUyvp9pUxElR71ko1Qx3p3Sjs |
|                                   | GFnsKXV6Afs3cFlTdcyT6km2mD2ZqdsYl |
|                                   | NYaZAQ88SvdyA2DFwWmasN9CeJ6OVJRg) |
|                                   | or on                             |
|                                   | [Android]                         |
|                                   | (/docs/reference/ads-api/mobile-c |
|                                   | onversions-endpoint/v2.2#android) |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` advertiser_tracking_enabled `   | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | Specifies whether a person has    |
|                                   | enabled advertising tracking on   |
|                                   | their device. Set to 0 for        |
|                                   | disabled or 1 for enabled. You    |
|                                   | should fetch this data and return |
|                                   | it to Meta will use the event     |
|                                   | data (from partners about user    |
|                                   | activities off Meta) pursuant to  |
|                                   | its Data Policy, including for ad |
|                                   | reporting, fraud detection and to |
|                                   | build and improve our products    |
|                                   | (including our ads delivery       |
|                                   | products), but will restrict use  |
|                                   | of data about that individual to  |
|                                   | personalize that user's ads. For  |
|                                   | devices running earlier versions  |
|                                   | than iOS 6, this parameter should |
|                                   | default to 1.                     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` anon_id `                       | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | The ID of a person who has        |
|                                   | installed the app anonymously     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` app_user_id `                   | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Specifies [user                   |
|                                   | id](/d                            |
|                                   | ocs/analytics/properties#user-id) |
|                                   | of an app user. Used internally   |
|                                   | by the iOS and Android SDKs for   |
|                                   | ` MOBILE_APP_INSTALL ` event      |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` application_tracking_enabled `  | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | A person can choose to enable ad  |
|                                   | tracking on an app level. Your    |
|                                   | SDK should allow an app developer |
|                                   | to put an opt-out setting into    |
|                                   | their app. Use this field to      |
|                                   | specify the person\'s choice. Use |
|                                   | 0 for disabled, 1 for enabled     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` attribution `                   | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | mobile_cookie from the person\'s  |
|                                   | device. Use this only on Android  |
|                                   | or iOS devices before iOS 6. The  |
|                                   | format for this should look       |
|                                   | something like                    |
|                                   | ` DDDEC                           |
|                                   | D0A-C076-4050-8CE8-C20EC3FC2BD3 ` |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` auto_publish `                  | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | This field is not longer being    |
|                                   | used. Used to be used internally  |
|                                   | by Facebook\'s SDK                |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` bundle_id `                     | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Used internally by Facebook\'s    |
|                                   | SDK                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` bundle_short_version `          | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Used internally by Facebook\'s    |
|                                   | SDK                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` bundle_version `                | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Used internally by Facebook\'s    |
|                                   | SDK                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` campaign_ids `                  | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Parameter passed via the deep     |
|                                   | link for Mobile App Engagement    |
|                                   | campaigns.                        |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` click_id `                      |                                   |
|                                   |                                   |
| string                            |                                   |
+-----------------------------------+-----------------------------------+
| ` consider_views `                | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | Specifies that view through data  |
|                                   | should be considered when         |
|                                   | determining the ad to attribute   |
|                                   | this install to. Clicks will      |
|                                   | always be considered first before |
|                                   | views and views will only be      |
|                                   | returned if there was not a click |
|                                   | on an ad for the app              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` custom_events `                 |                                   |
|                                   |                                   |
| list\<CustomEvent\>               |                                   |
+-----------------------------------+-----------------------------------+
| ` custom_events_file `            | <div>                             |
|                                   |                                   |
| file                              | <div>                             |
|                                   |                                   |
|                                   | Custom file, encoded as JSON that |
|                                   | describes the event. Please       |
|                                   | encode as UTF-8 and attach with   |
|                                   | the mime type                     |
|                                   | ` application/json ` or           |
|                                   | ` content/unknown `               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` device_token `                  | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | A token used to identify the      |
|                                   | device on push networks           |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` event `                         | <div>                             |
|                                   |                                   |
| enum {MOBILE_APP_INSTALL,         | <div>                             |
| CUSTOM_APP_EVENTS,                |                                   |
| DEFERRED_APP_LINK}                | Event type, one of                |
|                                   | ` MOBILE_APP_INSTALL ` ,          |
|                                   | ` CUSTOM_APP_EVENTS ` or          |
|                                   | ` DEFERRED_APP_LINK ` . If you    |
|                                   | are reporting a                   |
|                                   | ` MOBILE_APP_INSTALL ` event, you |
|                                   | must include either               |
|                                   | ` attribution ` or                |
|                                   | ` advertiser_id ` in the request  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | [ Required ]{._1vet}              |
+-----------------------------------+-----------------------------------+
| ` extinfo `                       | <div>                             |
|                                   |                                   |
| Object                            | <div>                             |
|                                   |                                   |
|                                   | Extended device and source        |
|                                   | information array, used by        |
|                                   | Facebook\'s SDKs, MMPs and Bots   |
|                                   | for Messenger. This parameter is  |
|                                   | an array and must be in a         |
|                                   | specific format. Please see our   |
|                                   | [App Events                       |
|                                   | API](/                            |
|                                   | docs/marketing-api/app-event-api) |
|                                   | for more information              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` include_dwell_data `            | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | Specifies that view dwell ms      |
|                                   | should be returned as part of     |
|                                   | view through data                 |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` include_video_data `            | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | Specifies that video view         |
|                                   | completion percentages should be  |
|                                   | returned as part of view through  |
|                                   | data                              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` install_referrer `              | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | 3rd party install referrer,       |
|                                   | currently available for Android   |
|                                   | only, see                         |
|                                   | https://develop                   |
|                                   | ers.google.com/analytics/devguide |
|                                   | s/collection/android/v4/campaigns |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` installer_package `             | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Used internally by the Android    |
|                                   | SDKs                              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` migration_bundle `              | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Used internally by the iOS and    |
|                                   | Android SDKs                      |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` page_id `                       | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | Specifies the Page ID associated  |
|                                   | with the messenger bot that logs  |
|                                   | the event                         |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` page_scoped_user_id `           | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | Specifies the page scoped User ID |
|                                   | associated with the messenger bot |
|                                   | that logs the event               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` receipt_data `                  | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | The receipts of in-app purchase   |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` ud `                            | <div>                             |
|                                   |                                   |
| JSON object                       | <div>                             |
|                                   |                                   |
|                                   | Optional user data parameters for |
|                                   | advanced matchingProvide hashed   |
|                                   | fields as key/value pairs similar |
|                                   | to the Pixel                      |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` url_schemes `                   | <div>                             |
|                                   |                                   |
| list\<string\>                    | <div>                             |
|                                   |                                   |
|                                   | Used internally by the iOS and    |
|                                   | Android SDKs                      |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` user_id `                       |                                   |
|                                   |                                   |
| string                            |                                   |
+-----------------------------------+-----------------------------------+
| ` user_id_type `                  |                                   |
|                                   |                                   |
| enum {INSTANT_GAMES_PLAYER_ID}    |                                   |
+-----------------------------------+-----------------------------------+
| ` vendor_id `                     |                                   |
|                                   |                                   |
| string                            |                                   |
+-----------------------------------+-----------------------------------+
| ` windows_attribution_id `        | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Attribution token used for        |
|                                   | Windows 10                        |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
:::

</div>

::: _367u
Struct {

` success ` : bool,

} Or Struct {

` applink_class ` : string,

` applink_url ` : string,

` applink_args ` : string,

` is_fb ` : bool,

` is_paid ` : bool,

` account_id ` : ad account id,

` ad_id ` : numeric string,

` ad_objective_name ` : string,

` adgroup_id ` : numeric string,

` adgroup_name ` : string,

` campaign_id ` : numeric string,

` campaign_name ` : string,

` campaign_group_id ` : numeric string,

` campaign_group_name ` : string,

` click_time ` : timestamp,

` is_mobile_data_terms_signed ` : bool,

` is_external ` : bool,

` is_instagram ` : bool,

` is_view_through ` : bool,

` view_time ` : timestamp,

` is_playable_ad ` : bool,

` is_aaa_campaign ` : bool,

` creative_id ` : numeric string,

` engagement_type ` : enum,

} Or Struct {

` success ` : bool,

` drop_reason ` : string,

}
:::

</div>
