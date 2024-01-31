Facebook App


================

[](#)

A Facebook app.

[](#)

Reading
-------

Get information about a Facebook app.

### Permissions

* An app access token can be used to view all fields for an app.
    

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D&version=v18.0)

    GET /v18.0/{application-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The app ID<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `aam_rules`<br><br>string | Rules of Auto Advanced Matching in FB SDKs |
| `an_ad_space_limit`<br><br>unsigned int32 | The maximum number of Ad Spaces allowed for each Audience Network supported platform |
| `an_platforms`<br><br>list<enum> | The platforms associated with the app in the Audience Network product. Not enforced, but when present, it can be used to provide the user with platform specific information for the app and its placements |
| `app_domains`<br><br>list<string> | Domains and subdomains this app can use |
| `app_events_config`<br><br>ApplicationAppEventsConfig | Configuration for app events |
| `app_install_tracked`<br><br>bool | Whether the app install is trackable or not |
| `app_name`<br><br>string | App name |
| `app_signals_binding_ios`<br><br>list<Binding> | List of app event bindings for iOS app |
| `app_type`<br><br>unsigned int32 | App type |
| `auth_dialog_data_help_url`<br><br>string | The URL of a special landing page that helps people who are using an app begin publishing Open Graph activity |
| `auth_dialog_headline`<br><br>string | One line description of an app that appears in the Login Dialog |
| `auth_dialog_perms_explanation`<br><br>string | The text to explain why an app needs additional permissions. This appears in the Login Dialog |
| `auth_referral_default_activity_privacy`<br><br>string | The default privacy setting selected for Open Graph activities in the Auth Dialog |
| `auth_referral_enabled`<br><br>unsigned int32 | Indicates whether Authenticated Referrals are enabled |
| `auth_referral_extended_perms`<br><br>list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled |
| `auth_referral_friend_perms`<br><br>list<string> | Basic friends permissions that a user must grant when Authenticated Referrals are enabled |
| `auth_referral_response_type`<br><br>string | The format that an app receives for the authentication token from the Login Dialog |
| `auth_referral_user_perms`<br><br>list<string> | Basic user permissions that a user must grant when Authenticated Referrals are enabled |
| `canvas_fluid_height`<br><br>bool | Indicates whether the app uses fluid or settable height values for Canvas |
| `canvas_fluid_width`<br><br>unsigned int32 | Indicates whether the app uses fluid or fixed width values for Canvas |
| `canvas_url`<br><br>string | The non-secure URL from which Canvas app content is loaded |
| `category`<br><br>string | The category of the app<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `client_config`<br><br>map | Config data for the client |
| `company`<br><br>string | The company the app belongs to |
| `configured_ios_sso`<br><br>bool | True if the app has configured Single Sign On on iOS |
| `contact_email`<br><br>string | Email address listed for people using the app to contact developers |
| `created_time`<br><br>datetime | Timestamp that indicates when the app was created |
| `creator_uid`<br><br>id | User ID of the creator of this app |
| `daily_active_users`<br><br>numeric string | The number of daily active users the app has |
| `daily_active_users_rank`<br><br>unsigned int32 | Ranking of this app vs other apps comparing daily active users |
| `deauth_callback_url`<br><br>string | URL that is pinged whenever a person removes the app |
| `default_share_mode`<br><br>string | The platform that should be used to share content |
| `description`<br><br>string | The description of the app, as provided by the developer<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `financial_id`<br><br>string | The ID for the corresponding audience network financial entity. |
| `hosting_url`<br><br>string | Webspace created with one of our hosting partners for this app |
| `icon_url`<br><br>string | The URL of this app's icon |
| `ios_bundle_id`<br><br>list<string> | Bundle ID of the associated iOS app |
| `ios_supports_native_proxy_auth_flow`<br><br>bool | Whether to support the native proxy login flow |
| `ios_supports_system_auth`<br><br>bool | Whether to support the iOS integrated Login Dialog |
| `ipad_app_store_id`<br><br>string | ID of the app in the iPad App Store |
| `iphone_app_store_id`<br><br>string | ID of the app in the iPhone App Store |
| `latest_sdk_version`<br><br>ApplicationSDKInfo | App latest sdk version |
| `link`<br><br>string | A link to the app on Facebook<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `logging_token`<br><br>string | To use for logging purposes |
| `logo_url`<br><br>string | The URL of the app's logo |
| `migrations`<br><br>map<string, bool> | Status of migrations for this app |
| `mobile_profile_section_url`<br><br>string | Mobile URL of the app section on a person's profile |
| `mobile_web_url`<br><br>string | URL to which Mobile users will be directed when using the app |
| `monthly_active_users`<br><br>numeric string | The number of monthly active users the app has |
| `monthly_active_users_rank`<br><br>unsigned int32 | Ranking of this app vs other apps comparing monthly active users |
| `name`<br><br>string | The name of the app<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `namespace`<br><br>string | The string appended to `apps.facebook.com/` to navigate to the app's canvas page<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `object_store_urls`<br><br>[ApplicationObjectStoreURLs](https://developers.facebook.com/docs/graph-api/reference/application-object-store-urls/) | Mobile store URLs for the app |
| `page_tab_default_name`<br><br>string | The title of the app when used in a Page Tab |
| `page_tab_url`<br><br>string | The non-secure URL from which Page Tab app content is loaded |
| `photo_url`<br><br>string | The URL of the app photo |
| `privacy_policy_url`<br><br>string | The URL that links to a Privacy Policy for the app |
| `profile_section_url`<br><br>string | URL of the app section on a user's profile for the desktop site |
| `property_id`<br><br>string | The monetization property which owns this app |
| `protected_mode_rules`<br><br>ApplicationProtectedModeRules | protected\_mode\_rules |
| `real_time_mode_devices`<br><br>list<string> | List of real time hashed device |
| `restrictions`<br><br>[ApplicationRestrictionInfo](https://developers.facebook.com/docs/graph-api/reference/application-restriction-info/) | Demographic restrictions for the app |
| `restrictive_data_filter_params`<br><br>string | Params used to filter out restrictive data |
| `secure_canvas_url`<br><br>string | The secure URL from which Canvas app content is loaded |
| `secure_page_tab_url`<br><br>string | The secure URL from which Page Tab app content is loaded |
| `server_ip_whitelist`<br><br>string | App requests must originate from this comma-separated list of IP addresses |
| `social_discovery`<br><br>unsigned int32 | Indicates whether app usage stories show up in the Ticker or Feed |
| `subcategory`<br><br>string | The subcategory the app can be found under |
| `suggested_events_setting`<br><br>string | Settings for suggested events |
| `supported_platforms`<br><br>list<enum {WEB, CANVAS, MOBILE\_WEB, IPHONE, IPAD, ANDROID, WINDOWS, AMAZON, SUPPLEMENTARY\_IMAGES, GAMEROOM, INSTANT\_GAME, OCULUS, SAMSUNG, XIAOMI}> | All the platform the app supports |
| `terms_of_service_url`<br><br>string | URL to Terms of Service that appears in the Login Dialog |
| `url_scheme_suffix`<br><br>string | URL scheme suffix |
| `user_support_email`<br><br>string | Main contact email for this app where people can receive support |
| `user_support_url`<br><br>string | URL shown in the Canvas footer that people can visit to get support for the app |
| `website_url`<br><br>string | URL of a website that integrates with this app |
| `weekly_active_users`<br><br>numeric string | The number of weekly active users the app has |

### Edges

| Edge | Description |
| --- | --- |
| [`accounts`](https://developers.facebook.com/docs/graph-api/reference/application/accounts/) | Test User accounts associated with the app |
| [`ad_placement_groups`](https://developers.facebook.com/docs/graph-api/reference/application/ad_placement_groups/) | Ad placement groups for publishing ads on this app |
| [`adnetworkanalytics_results`](https://developers.facebook.com/docs/graph-api/reference/application/adnetworkanalytics_results/) | Obtain the results of an async Audience Network query for this publisher entity |
| [`aem_attribution`](https://developers.facebook.com/docs/graph-api/reference/application/aem_attribution/) | aem\_attribution |
| [`aem_conversion_configs`](https://developers.facebook.com/docs/graph-api/reference/application/aem_conversion_configs/) | The aggregated event measurement conversion value configs for this app |
| [`aem_conversion_filter`](https://developers.facebook.com/docs/graph-api/reference/application/aem_conversion_filter/) | Boolean for if product\_set\_id \[fb\_content\_id\] belongs to a certain catalog \[catalog\_id\] |
| [`agencies`](https://developers.facebook.com/docs/graph-api/reference/application/agencies/) | The businesses which are not owner but can advertise for this app |
| [`app_event_types`](https://developers.facebook.com/docs/graph-api/reference/application/app_event_types/) | Info about App Events logged for the app |
| [`app_installed_groups`](https://developers.facebook.com/docs/graph-api/reference/application/app_installed_groups/) | List of facebook groups the app is installed in |
| [`appassets`](https://developers.facebook.com/docs/graph-api/reference/application/appassets/) | appassets |
| [`button_auto_detection_device_selection`](https://developers.facebook.com/docs/graph-api/reference/application/button_auto_detection_device_selection/) | Whether to turn on auto device sampling. |
| [`cloudbridge_settings`](https://developers.facebook.com/docs/graph-api/reference/application/cloudbridge_settings/) | cloudbridge\_settings |
| [`da_checks`](https://developers.facebook.com/docs/graph-api/reference/application/da_checks/) | A list of results after running Dynamic Ads checks on this app. |
| [`events`](https://developers.facebook.com/docs/graph-api/reference/application/events/) | Events |
| [`ios_skadnetwork_conversion_config`](https://developers.facebook.com/docs/graph-api/reference/application/ios_skadnetwork_conversion_config/) | ios\_skadnetwork\_conversion\_config |
| [`mobile_sdk_gk`](https://developers.facebook.com/docs/graph-api/reference/application/mobile_sdk_gk/) | Gatekeeper for Mobile SDK |
| [`model_asset`](https://developers.facebook.com/docs/graph-api/reference/application/model_asset/) | model\_asset |
| [`monetized_digital_store_objects`](https://developers.facebook.com/docs/graph-api/reference/application/monetized_digital_store_objects/) | List of digital store objects for this app monetized via Audience Network |
| [`object_types`](https://developers.facebook.com/docs/graph-api/reference/application/object_types/) | Open Graph Object types associated with this app |
| [`objects`](https://developers.facebook.com/docs/graph-api/reference/application/objects/) | Open Graph objects |
| [`permissions`](https://developers.facebook.com/docs/graph-api/reference/application/permissions/) | The status of permissions that are have been submitted for Login Review |
| [`products`](https://developers.facebook.com/docs/graph-api/reference/application/products/) | In-app-purchaseable products associated with this app |
| [`purchases`](https://developers.facebook.com/docs/graph-api/reference/application/purchases/) | In-app-purchaseable products of this app owned by the user |
| [`roles`](https://developers.facebook.com/docs/graph-api/reference/app/roles/) | The developer roles defined for this app |
| [`subscribed_domains`](https://developers.facebook.com/docs/graph-api/reference/application/subscribed_domains/) | subscribed\_domains |
| [`subscribed_domains_phishing`](https://developers.facebook.com/docs/graph-api/reference/application/subscribed_domains_phishing/) | subscribed\_domains\_phishing |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 278 | Reading advertisements requires an access token with the extended permission ads\_read |

[](#)

Creating
--------

You can make a POST request to `owned_apps` edge from the following paths:

* [`/{business_id}/owned_apps`](https://developers.facebook.com/docs/marketing-api/reference/business/owned_apps/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

This endpoint doesn't have any parameters.

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`access_status`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `app_indexing` edge from the following paths:

* [`/{application_id}/app_indexing`](https://developers.facebook.com/docs/graph-api/reference/application/app_indexing/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `app_version`<br><br>string | The version of the app being indexed<br><br>Required |
| `device_session_id`<br><br>string | Device session id of the uploading device |
| `extra_info`<br><br>string | Extra information about the app index |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `request_type`<br><br>enum {APP\_INDEXING, PLUGIN, BUTTON\_SAMPLING} | Default value: `"APP_INDEXING"`<br><br>Type of the app indexing request |
| `tree`<br><br>JSON object | The UI component tree of the app<br><br>Required |
| `screenname`<br><br>string |     |
| `screenshot`<br><br>string |     |
| `view`<br><br>list<JSON encoded app UI component> | Required |

### Return Type

Struct {

`success`: bool,

`is_app_indexing_enabled`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `codeless_event_mappings` edge from the following paths:

* [`/{application_id}/codeless_event_mappings`](https://developers.facebook.com/docs/graph-api/reference/application/codeless_event_mappings/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `mappings`<br><br>array<JSON object> | The event to UI component mappings of the app<br><br>Required |
| `method`<br><br>enum {INFERENCE, MANUAL, CONFIRMED\_INFERENCE, BUTTON\_INDEXING, UNKNOWN} | method<br><br>Required |
| `event_name`<br><br>string | event\_name<br><br>Required |
| `event_type`<br><br>enum {CLICK, SELECTED, TEXT\_CHANGED} | event\_type<br><br>Required |
| `app_version`<br><br>string | app\_version<br><br>Required |
| `parameters`<br><br>array<JSON object> | parameters |
| `name`<br><br>string | name<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `screenshot_handle`<br><br>string | screenshot\_handle |
| `dimensions`<br><br>array<JSON object> | dimensions |
| `top`<br><br>int64 | top<br><br>Required |
| `left`<br><br>int64 | left<br><br>Required |
| `width`<br><br>int64 | width<br><br>Required |
| `height`<br><br>int64 | height<br><br>Required |
| `activity_name`<br><br>string | activity\_name |
| `mutation_method`<br><br>enum {REPLACE, ADD, DELETE} | Detailed mutation type like replace, add<br><br>Required |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `post_method`<br><br>enum {EYMT, CODELESS} | Default value: `"CODELESS"`<br><br>Whether the api is called by codeless or EYMT |

### Return Type

Struct {

`num_updated`: int32,

`num_invalid`: int32,

}

### Error Codes

| Error | Description |
| --- | --- |
| 105 | The number of parameters exceeded the maximum for this operation |

You can make a POST request to `page_activities` edge from the following paths:

* [`/{application_id}/page_activities`](https://developers.facebook.com/docs/graph-api/reference/application/page_activities/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on iOS 6+, and that choice is stored within the phone. You should fetch that and return it to Facebook so we know not to use the data for optimization. We will, however, use the data to report on a conversion. See [here](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT2Mvg13ugopSWUbYa4G142e1A5uCFxolC9n0YZDeX1Mf3jzuurj6t-uzXxmlz-q8IpkWA8suUnWGzUNgh7vqa_byW_ASDgXbaGlE9Qg3e5XQILxEC0eYEHgwYgw1lNpre__2QyKa0AyWI5mw2lu5w) for an example of how Facebook fetches that variable. For devices running less than iOS 6, this query parameter can default to 1. Use 0 for disabled, 1 for enabled |
| `application_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled |
| `custom_events`<br><br>list<CustomEvent> | Custom events reported |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `logging_source`<br><br>enum {MESSENGER\_BOT, DETECTION} | Specifies the event source |
| `logging_target`<br><br>enum {APP, APP\_AND\_PAGE, PAGE} | Default value: `"APP"`<br><br>whether the event is logged to app level or page level or both |
| `page_id`<br><br>int64 | Specifies the Page ID associated with the messenger bot that logs the event |
| `page_scoped_user_id`<br><br>int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `client_apps` edge from the following paths:

* [`/{business_id}/client_apps`](https://developers.facebook.com/docs/marketing-api/reference/business/client_apps/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id` | App ID.<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`access_status`: enum,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

You can make a POST request to `mmp_auditing` edge from the following paths:

* [`/{application_id}/mmp_auditing`](https://developers.facebook.com/docs/graph-api/reference/application/mmp_auditing/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`<br><br>string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on [iOS](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT29gerJcyYU9YHbU9jW-QDpbRFcRNj6v0RrI2zMGfr1fEeGxHiE2nD2xXLCqMa2N2oY9HsvyOnZxpNGHS_yDZrstKqTjnxmBkuE20G-z_GaHPMIPu4_-3akGrnoSTu7UMT9qvmnchOrV8quqM-cSA) or on [Android](https://developers.facebook.com/docs/reference/ads-api/mobile-conversions-endpoint/v2.2#android) |
| `attribution`<br><br>string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3` |
| `attribution_model`<br><br>string | attribution model that clients selected to be respected by MMP |
| `auditing_token`<br><br>string | Token provided in claim response sent to MMP |
| `click_attr_window`<br><br>int64 | Time window of click attribution |
| `custom_events`<br><br>list<CustomEvent> | Custom app events that MMP are sending auditing events for |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `decline_reason`<br><br>string | Reason that MMP rejected Facebook ads claim |
| `engagement_type`<br><br>string | Engagement type that MMP explicitly reports |
| `event`<br><br>string | Event type that Facebook claimed for<br><br>Required |
| `event_reported_time`<br><br>int64 | Time that event reported to MMP |
| `fb_ad_id`<br><br>int64 | FBID of the ads in Facebook claim<br><br>Required |
| `fb_click_time`<br><br>int64 | Ad click time in Facebook claim |
| `fb_view_time`<br><br>int64 | Ad view time in Facebook claim |
| `is_fb`<br><br>boolean | Result that whether MMP attribute the event to Facebook ads<br><br>Required |
| `used_install_referrer`<br><br>boolean | Identifies whether MMP used the install referrer |
| `view_attr_window`<br><br>int64 | Time window of view attribution |

### Return Type

Struct {

`success`: bool,

} Or Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

Update application information such as demographic restrictions.

### Permissions

* An app access token is required to update fields on an app.

### Example

To update an app restrictions, such as `age`, send a `POST` request to `/{app-id}`:

`curl -i -X POST "https://graph.facebook.com/{app-id}?restrictions={'age':'21+'}&access_token={app-access-token}"`

On success your app receives this response:

`{ "success": true }`

You can update an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a POST request to [`/{application_id}`](https://developers.facebook.com/docs/graph-api/reference/application/).

### Parameters

| Parameter | Description |
| --- | --- |
| `allow_cycle_app_secret`<br><br>boolean | Default value: `false`<br><br>Allows for the application to cycle the secret |
| `an_platforms`<br><br>list<enum {ANDROID, DESKTOP, GALAXY, INSTANT\_ARTICLES, IOS, MOBILE\_WEB, OCULUS, UNKNOWN, XIAOMI}> | The platforms associated with the app in the AudienceNetwork product |
| `app_domains`<br><br>list<string> | Specifies a list of domains that correspond to this app. Subdomains of domains in this array are also considered to belong to this app |
| `app_name`<br><br>string | App name |
| `app_type`<br><br>boolean | App type |
| `auth_dialog_headline`<br><br>string | One line description of this app that appears in the Login Dialog |
| `auth_dialog_perms_explanation`<br><br>string | The text to explain why an app needs additional permissions. This appears in the Login Dialog |
| `auth_referral_default_activity_privacy`<br><br>string | The default privacy setting selected for Open Graph activities in the Auth Dialog |
| `auth_referral_enabled`<br><br>boolean | Enables or disables Authenticated Referrals |
| `auth_referral_extended_perms`<br><br>list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled |
| `auth_referral_friend_perms`<br><br>list<string> | Basic friends permissions that a person must grant when Authenticated Referrals are enabled |
| `auth_referral_response_type`<br><br>string | The format of the authentication token this app receives from the Login Dialog |
| `auth_referral_user_perms`<br><br>list<string> | Basic permissions that a person must grant when Authenticated Referrals are enabled |
| `canvas_fluid_height`<br><br>boolean | Indicates whether this app uses fluid or settable height values for Canvas |
| `canvas_fluid_width`<br><br>boolean | Indicates whether this app uses fluid or fixed width values for Canvas |
| `canvas_url`<br><br>URL | The non-secure URL from which Canvas app content is loaded |
| `contact_email`<br><br>string | Email address users can use to contact developers |
| `deauth_callback_url`<br><br>URL | URL that is pinged whenever a person removes this app |
| `mobile_web_url`<br><br>URL | URL that mobile users will be directed to when using this app |
| `namespace`<br><br>string | The string appended to `apps.facebook.com/` to navigate to this app's Canvas page |
| `page_tab_default_name`<br><br>string | The title of this app as it appears in a Page Tab |
| `privacy_policy_url`<br><br>URL | The URL that links to a privacy policy for this app |
| `restrictions`<br><br>JSON-encoded string | Update demographic restrictions for this app. Can be one or more of the following parameters: `age`, `location`, or `type`. `age` can be one of the following values: `13+`, `16+`, `17+`, `18+`, `19+`, or `21+`. `location` can be one or more country represented by the [2 letter country code](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FISO_3166-1_alpha-2&h=AT3_oE2glJjrM3bVoxBkGsndvGHGZxo_Q2PjuoEjMr3PLtEugyHue-EpoCysBJd-LpGAOXgCtKAEBEcmtFhsMs5d_7lgxHxdTNfnrUStOsB436mMVhClBU3S14NB8HL7yZJ7Ac8chPcJQtSqpbs0qw). `type` can only be `alcohol`. |
| `secure_canvas_url`<br><br>URL | The secure URL from which Canvas app content is loaded |
| `secure_page_tab_url`<br><br>URL | The secure URL from which Page Tab app content is loaded |
| `server_ip_whitelist`<br><br>list<string> | App requests must originate from this comma-separated list of IP addresses |
| `terms_of_service_url`<br><br>URL | URL to Terms of Service that appears in the Login Dialog |
| `url_scheme_suffix`<br><br>string | URL scheme suffix |
| `user_support_email`<br><br>string | Main contact email for this app where people can receive support |
| `user_support_url`<br><br>URL | URL shown in the Canvas footer that people can visit to get support for this app |
| `website_url`<br><br>URL | URL of a website that integrates with this app |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

You can update an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a POST request to [`/act_{ad_account_id}/subscribed_apps`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/subscribed_apps/).

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id`<br><br>string | Default value:<br><br>the id of app to be subscribed from ad account |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Deleting
--------

You can dissociate an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) from a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a DELETE request to [`/{page_id}/subscribed_apps`](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

`messaging_success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 210 | User not visible |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

You can dissociate an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) from an [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/subscribed_apps`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/subscribed_apps/).

### Parameters

| Parameter | Description |
| --- | --- |
| `app_id`<br><br>string | Default value:<br><br>the id of app to be unsubscribed from ad account |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Application Accounts
====================

[](#)

Represents a collection of [test users](https://developers.facebook.com/docs/development/build-and-test/test-users) on an app.

[](#)

Reading
-------

Get a list of [test users](https://developers.facebook.com/docs/development/build-and-test/test-users) on an app.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [App](https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Faccounts&version=v18.0)

    GET /v18.0/{application-id}/accounts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/accounts',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/accounts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/accounts",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/accounts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum{test-users} | The type of user requested |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `access_token`<br><br>string | An access token that can be used to make API calls on behalf of this user<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can make a POST request to `accounts` edge from the following paths:

* [`/{application_id}/accounts`](https://developers.facebook.com/docs/graph-api/reference/application/accounts/)

When posting to this edge, a [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) will be created.

  

Upon successful creation, a `login_url` and `access_token` will be returned. You can use the login URL to log in as the test user. Login URLs expire once they are used, or after one hour if they are unused. An access token will only be returned if the `installed` parameter was set to `true` at the time of the query.

You can also use this edge to associate an existing test user with a different app by using the `owner_acces_token` parameter.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [App](https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None |

### Parameters

| Parameter | Description |
| --- | --- |
| `installed`<br><br>boolean | Automatically installs the app for the test user once it is created or associated |
| `minor`<br><br>boolean | Is this test user a minor |
| `name`<br><br>string | The name for the test user. When left blank, a random name will be automatically generated |
| `owner_access_token`<br><br>string | When associating existing test users with other apps, this is the app access token of any app that is already associated with the test user. The `{app-id}` in the publishing request in this case should be the app that will is the target to associate with the test user. The API request should also be signed with the app access token of that target app. Required when associating test users, but should not be used when creating new test users |
| `permissions`<br><br>List<Permission> | Default value: `Set`<br><br>List of permissions that are automatically granted for the app when it is created or associated |
| `type`<br><br>enum{test-users} | Type |
| `uid`<br><br>int | ID of an existing test user to associate with another app. Required when associating test users, but should not be used when creating new test users |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`access_token`: string,

`login_url`: string,

`email`: string,

`password`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 2900 | Too many test accounts |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can dissociate a [TestAccount](https://developers.facebook.com/docs/graph-api/reference/test-account/) from an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) by making a DELETE request to [`/{application_id}/accounts`](https://developers.facebook.com/docs/graph-api/reference/application/accounts/).

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/) | [App](https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None |

### Limitations

At least one test user must be associated with an app. Attempting to perform this operation on an app's sole test user will result in error code `2902`.

### Parameters

| Parameter | Description |
| --- | --- |
| `type`<br><br>enum {TEST\_USERS} | Account type |
| `uid`<br><br>UID | Account UID<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 2902 | Cannot remove test account from this app |

[](#)

Application Activities
======================

[](#)

Application activities are events from your app.

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can use a user access token or app access token to log events to this endpoint.

You can make a POST request to `activities` edge from the following paths:

* [`/{application_id}/activities`](https://developers.facebook.com/docs/graph-api/reference/application/activities/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`<br><br>string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on [iOS](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT2XFqAlT43G1WhBHzdKjIdRvFo9x7HCE5yZTRiTcI39UYVXJeB6zYE-9F2dhmnxnAl5Fem8JwUyvp9pUxElR71ko1Qx3p3SjsGFnsKXV6Afs3cFlTdcyT6km2mD2ZqdsYlNYaZAQ88SvdyA2DFwWmasN9CeJ6OVJRg) or on [Android](https://developers.facebook.com/docs/reference/ads-api/mobile-conversions-endpoint/v2.2#android) |
| `advertiser_tracking_enabled`<br><br>boolean | Specifies whether a person has enabled advertising tracking on their device. Set to 0 for disabled or 1 for enabled. You should fetch this data and return it to Meta will use the event data (from partners about user activities off Meta) pursuant to its Data Policy, including for ad reporting, fraud detection and to build and improve our products (including our ads delivery products), but will restrict use of data about that individual to personalize that user’s ads. For devices running earlier versions than iOS 6, this parameter should default to 1. |
| `anon_id`<br><br>string | The ID of a person who has installed the app anonymously |
| `app_user_id`<br><br>string | Specifies [user id](https://developers.facebook.com/docs/analytics/properties#user-id) of an app user. Used internally by the iOS and Android SDKs for `MOBILE_APP_INSTALL` event |
| `application_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled |
| `attribution`<br><br>string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3` |
| `auto_publish`<br><br>boolean | This field is not longer being used. Used to be used internally by Facebook's SDK |
| `bundle_id`<br><br>string | Used internally by Facebook's SDK |
| `bundle_short_version`<br><br>string | Used internally by Facebook's SDK |
| `bundle_version`<br><br>string | Used internally by Facebook's SDK |
| `campaign_ids`<br><br>string | Parameter passed via the deep link for Mobile App Engagement campaigns. |
| `click_id`<br><br>string | click\_id |
| `consider_views`<br><br>boolean | Specifies that view through data should be considered when determining the ad to attribute this install to. Clicks will always be considered first before views and views will only be returned if there was not a click on an ad for the app |
| `custom_events`<br><br>list<CustomEvent> | Custom events reported, required with `CUSTOM_APP_EVENTS` events. Please see our [App Events API](https://developers.facebook.com/docs/marketing-api/app-event-api), [App Events for iOS](https://developers.facebook.com/docs/app-events/ios) and [App Events for Android](https://developers.facebook.com/docs/app-events/android) for more information |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `custom_events_file`<br><br>file | Custom file, encoded as JSON that describes the event. Please encode as UTF-8 and attach with the mime type `application/json` or `content/unknown` |
| `device_token`<br><br>string | A token used to identify the device on push networks |
| `event`<br><br>enum {MOBILE\_APP\_INSTALL, CUSTOM\_APP\_EVENTS, DEFERRED\_APP\_LINK} | Event type, one of `MOBILE_APP_INSTALL`, `CUSTOM_APP_EVENTS` or `DEFERRED_APP_LINK`. If you are reporting a `MOBILE_APP_INSTALL` event, you must include either `attribution` or `advertiser_id` in the request<br><br>Required |
| `extinfo`<br><br>Object | Extended device and source information array, used by Facebook's SDKs, MMPs and Bots for Messenger. This parameter is an array and must be in a specific format. Please see our [App Events API](https://developers.facebook.com/docs/marketing-api/app-event-api) for more information |
| `0`<br><br>string | extinfo version<br><br>Required |
| `1`<br><br>string | app package name |
| `2`<br><br>string | short version (int or string) |
| `3`<br><br>string | long version |
| `4`<br><br>string | OS version |
| `5`<br><br>string | device model name |
| `6`<br><br>string | locale |
| `7`<br><br>string | timezone abbreviation |
| `8`<br><br>string | carrier |
| `9`<br><br>int64 | screen width |
| `10`<br><br>int64 | screen height |
| `11`<br><br>string | screen density (float decimal , or .) |
| `12`<br><br>int64 | CPU cores |
| `13`<br><br>int64 | external storage size in GB |
| `14`<br><br>int64 | free space on external storage in GB |
| `15`<br><br>string | device timezone |
| `include_dwell_data`<br><br>boolean | Specifies that view dwell ms should be returned as part of view through data |
| `include_video_data`<br><br>boolean | Specifies that video view completion percentages should be returned as part of view through data |
| `install_referrer`<br><br>string | 3rd party install referrer, currently available for Android only, see https://developers.google.com/analytics/devguides/collection/android/v4/campaigns |
| `installer_package`<br><br>string | Used internally by the Android SDKs |
| `migration_bundle`<br><br>string | Used internally by the iOS and Android SDKs |
| `page_id`<br><br>int64 | Specifies the Page ID associated with the messenger bot that logs the event |
| `page_scoped_user_id`<br><br>int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event |
| `receipt_data`<br><br>string | The receipts of in-app purchase |
| `ud`<br><br>JSON object | Optional user data parameters for advanced matchingProvide hashed fields as key/value pairs similar to the Pixel |
| `em`<br><br>string | em  |
| `fn`<br><br>string | fn  |
| `ln`<br><br>string | ln  |
| `ph`<br><br>string | ph  |
| `ge`<br><br>string | ge  |
| `dob`<br><br>string | dob |
| `ct`<br><br>string | ct  |
| `st`<br><br>string | st  |
| `zp`<br><br>string | zp  |
| `extern_id`<br><br>string | extern\_id |
| `db`<br><br>string | db  |
| `r1`<br><br>string | r1  |
| `r2`<br><br>string | r2  |
| `cn`<br><br>string | cn  |
| `r3`<br><br>string | r3  |
| `r4`<br><br>string | r4  |
| `r5`<br><br>string | r5  |
| `r6`<br><br>string | r6  |
| `r7`<br><br>string | r7  |
| `r8`<br><br>string | r8  |
| `country`<br><br>string | country |
| `external_id`<br><br>string | external\_id |
| `url_schemes`<br><br>list<string> | Used internally by the iOS and Android SDKs |
| `user_id`<br><br>string | user\_id |
| `user_id_type`<br><br>enum {INSTANT\_GAMES\_PLAYER\_ID} | user\_id\_type |
| `vendor_id`<br><br>string | vendor\_id |
| `windows_attribution_id`<br><br>string | Attribution token used for Windows 10 |

### Return Type

Struct {

`success`: bool,

} Or Struct {

`applink_class`: string,

`applink_url`: string,

`applink_args`: string,

`is_fb`: bool,

`is_paid`: bool,

`account_id`: ad account id,

`ad_id`: numeric string,

`ad_objective_name`: string,

`adgroup_id`: numeric string,

`adgroup_name`: string,

`campaign_id`: numeric string,

`campaign_name`: string,

`campaign_group_id`: numeric string,

`campaign_group_name`: string,

`click_time`: timestamp,

`is_mobile_data_terms_signed`: bool,

`is_external`: bool,

`is_instagram`: bool,

`is_view_through`: bool,

`view_time`: timestamp,

`is_playable_ad`: bool,

`is_aaa_campaign`: bool,

`creative_id`: numeric string,

`engagement_type`: enum,

} Or Struct {

`success`: bool,

`drop_reason`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Ad Placement Groups
===============================

[](#)

Reading
-------

Graph Edge from App to Placement Group

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fad_placement_groups&version=v18.0)

    GET /v18.0/{application-id}/ad_placement_groups HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/ad_placement_groups',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/ad_placement_groups",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/ad_placement_groups",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/ad_placement_groups"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AdPlacementGroup nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Adnetworkanalytics Results
======================================

[](#)

Reading
-------

Query insights data for this publisher entity

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fadnetworkanalytics_results&version=v18.0)

    GET /v18.0/{application-id}/adnetworkanalytics_results HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/adnetworkanalytics_results',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/adnetworkanalytics_results",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/adnetworkanalytics_results",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/adnetworkanalytics_results"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `query_ids`<br><br>list<string> | Default value: `Vec`<br><br>Set of query ids to get result for |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AdNetworkAnalyticsAsyncQueryResult nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Aem Attribution
===========================

[](#)

Reading
-------

ApplicationAEMAttribution

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Faem_attribution&version=v18.0)

    GET /v18.0/{application-id}/aem_attribution HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/aem_attribution',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/aem_attribution",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/aem_attribution",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/aem_attribution"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AEMAttribution nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Aem Conversion Configs
==================================

[](#)

Reading
-------

Application aggregated event measurement conversion configs

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Faem_conversion_configs&version=v18.0)

    GET /v18.0/{application-id}/aem_conversion_configs HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/aem_conversion_configs',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/aem_conversion_configs",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/aem_conversion_configs",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/aem_conversion_configs"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AEMConversionConfig nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Aem Conversion Filter
=================================

[](#)

Reading
-------

ApplicationAEMConversionFilter

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Faem_conversion_filter&version=v18.0)

    GET /v18.0/{application-id}/aem_conversion_filter HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/aem_conversion_filter',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/aem_conversion_filter",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/aem_conversion_filter",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/aem_conversion_filter"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `catalog_id`<br><br>string | catalog\_id. Check the product\_ids are in this catalog. |
| `fb_content_ids`<br><br>string | product\_set\_ids, or fb\_content\_ids. Check these are in catalog\_id |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of AEMConversionFilter nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Agencies
====================

[](#)

Reading
-------

ApplicationAgencies

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fagencies&version=v18.0)

    GET /v18.0/{application-id}/agencies HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/agencies',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/agencies",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/agencies",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/agencies"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Business](https://developers.facebook.com/docs/marketing-api/reference/business/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

App Event Types for an App


==============================

[](#)

App Event types for an app

[](#)

Reading
-------

App Event types for an app

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fapp_event_types&version=v18.0)

    GET /v18.0/{application-id}/app_event_types HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/app_event_types',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/app_event_types",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/app_event_types",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/app_event_types"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ApplicationAppEventTypes](https://developers.facebook.com/docs/graph-api/reference/application-app-event-types/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 3000 | Reading insights of a Page, business, app, domain or event source group not owned by the querying user or application |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application App Indexing
========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `app_indexing` edge from the following paths:

* [`/{application_id}/app_indexing`](https://developers.facebook.com/docs/graph-api/reference/application/app_indexing/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `app_version`<br><br>string | The version of the app being indexed<br><br>Required |
| `device_session_id`<br><br>string | Device session id of the uploading device |
| `extra_info`<br><br>string | Extra information about the app index |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `request_type`<br><br>enum {APP\_INDEXING, PLUGIN, BUTTON\_SAMPLING} | Default value: `"APP_INDEXING"`<br><br>Type of the app indexing request |
| `tree`<br><br>JSON object | The UI component tree of the app<br><br>Required |
| `screenname`<br><br>string |     |
| `screenshot`<br><br>string |     |
| `view`<br><br>list<JSON encoded app UI component> | Required |

### Return Type

Struct {

`success`: bool,

`is_app_indexing_enabled`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application App Installed Groups
================================

[](#)

Reading
-------

List of groups the application is installed in

### Feature Permissions

| Name | Description |
| --- | --- |
| Groups API | This [feature permission](https://developers.facebook.com/docs/graph-api/reference/group/) may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fapp_installed_groups&version=v18.0)

    GET /v18.0/{application-id}/app_installed_groups HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/app_installed_groups',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/app_installed_groups",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/app_installed_groups",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/app_installed_groups"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [App Review](https://developers.facebook.com/docs/apps/review) | Your app must be approved for the [Groups API](https://developers.facebook.com/docs/groups-api/) feature. |
| [App Installation](https://developers.facebook.com/docs/groups-api#app-installation) | The app must be installed on the Group. |
| [Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | An AppToken access token. See [App Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens). |

### Parameters

| Parameter | Description |
| --- | --- |
| `group_id`<br><br>group\_id ID | Id of the group to check if app is installed in it or not |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Group](https://developers.facebook.com/docs/graph-api/reference/group/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Appassets
=====================

[](#)

Reading
-------

An Edge to the CanvasAppAsset

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fappassets&version=v18.0)

    GET /v18.0/{application-id}/appassets HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/appassets',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/appassets",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/appassets",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/appassets"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CanvasAppAsset nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Assets
==================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `assets` edge from the following paths:

* [`/{application_id}/assets`](https://developers.facebook.com/docs/graph-api/reference/application/assets/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `asset`<br><br>file | The asset file to upload<br><br>Required |
| `comment`<br><br>string | Optional comment describing the asset |
| `type`<br><br>string | Type of the asset, e.g. SWF, JS, BUNDLE, UNITY\_WEBGL, GAMES\_DESKTOP, PRIVACY\_POLICY, TOS<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Button Auto Detection Device Selection
==================================================

[](#)

Reading
-------

ApplicationButtonAutoDetectionDeviceSelection

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fbutton_auto_detection_device_selection&version=v18.0)

    GET /v18.0/{application-id}/button_auto_detection_device_selection HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/button_auto_detection_device_selection',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/button_auto_detection_device_selection",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/button_auto_detection_device_selection",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/button_auto_detection_device_selection"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `device_id`<br><br>string | Device id of the given app. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of ButtonAutoDetectionDeviceSelection nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 43003 | App auto button detection is disabled. |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Cloudbridge Settings
================================

[](#)

Reading
-------

ApplicationCloudbridgeSettings

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fcloudbridge_settings&version=v18.0)

    GET /v18.0/{application-id}/cloudbridge_settings HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/cloudbridge_settings',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/cloudbridge_settings",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/cloudbridge_settings",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/cloudbridge_settings"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CloudbridgeSetting nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Codeless Event Mappings
===================================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `codeless_event_mappings` edge from the following paths:

* [`/{application_id}/codeless_event_mappings`](https://developers.facebook.com/docs/graph-api/reference/application/codeless_event_mappings/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `mappings`<br><br>array<JSON object> | The event to UI component mappings of the app<br><br>Required |
| `method`<br><br>enum {INFERENCE, MANUAL, CONFIRMED\_INFERENCE, BUTTON\_INDEXING, UNKNOWN} | method<br><br>Required |
| `event_name`<br><br>string | event\_name<br><br>Required |
| `event_type`<br><br>enum {CLICK, SELECTED, TEXT\_CHANGED} | event\_type<br><br>Required |
| `app_version`<br><br>string | app\_version<br><br>Required |
| `parameters`<br><br>array<JSON object> | parameters |
| `name`<br><br>string | name<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path`<br><br>array<JSON object> | path<br><br>Required |
| `class_name`<br><br>string | class\_name<br><br>Required |
| `index`<br><br>int64 | index<br><br>Required |
| `id`<br><br>int64 | id  |
| `text`<br><br>string | text |
| `tag`<br><br>string | tag |
| `description`<br><br>string | description |
| `hint`<br><br>string | hint |
| `match_bitmask`<br><br>int64 | match\_bitmask |
| `component_id`<br><br>string | component\_id<br><br>Required |
| `path_type`<br><br>enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`<br><br>path\_type |
| `screenshot_handle`<br><br>string | screenshot\_handle |
| `dimensions`<br><br>array<JSON object> | dimensions |
| `top`<br><br>int64 | top<br><br>Required |
| `left`<br><br>int64 | left<br><br>Required |
| `width`<br><br>int64 | width<br><br>Required |
| `height`<br><br>int64 | height<br><br>Required |
| `activity_name`<br><br>string | activity\_name |
| `mutation_method`<br><br>enum {REPLACE, ADD, DELETE} | Detailed mutation type like replace, add<br><br>Required |
| `platform`<br><br>enum {ANDROID, IOS} | The platform of the app being indexed<br><br>Required |
| `post_method`<br><br>enum {EYMT, CODELESS} | Default value: `"CODELESS"`<br><br>Whether the api is called by codeless or EYMT |

### Return Type

Struct {

`num_updated`: int32,

`num_invalid`: int32,

}

### Error Codes

| Error | Description |
| --- | --- |
| 105 | The number of parameters exceeded the maximum for this operation |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Da Checks
=====================

[](#)

Reading
-------

Runs Dynamic Ads checks and returns their results.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fda_checks&version=v18.0)

    GET /v18.0/{application-id}/da_checks HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/da_checks',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/da_checks",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/da_checks",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/da_checks"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `checks`<br><br>list<string> | Default value: `Vector`<br><br>A list of Dynamic Ads checks that will be run. If not specified, all checks will be run. Valid values are: `app_missing_param_in_events` |
| `connection_method`<br><br>enum{ALL, APP, BROWSER, SERVER} | Connection method of pixel/app event to check. This is optional |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [DACheck](https://developers.facebook.com/docs/marketing-api/reference/da-check/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 278 | Reading advertisements requires an access token with the extended permission ads\_read |
| 100 | Invalid parameter |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Events
==================

[](#)

Reading
-------

Retrieves events created on your page on behalf of your app

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fevents&version=v18.0)

    GET /v18.0/{application-id}/events HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/events',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/events",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/events",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/events"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `include_canceled`<br><br>boolean | Whether include canceled events. |
| `type`<br><br>enum{attending, created, declined, maybe, not\_replied} | Query events for which the user has this particular rsvp\_status set |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Event](https://developers.facebook.com/docs/graph-api/reference/event/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

iOS SKAdNetwork Conversion Config
=================================

[](#)

Reading
-------

ApplicationiosSkadnetworkConversionConfig

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fios_skadnetwork_conversion_config&version=v18.0)

    GET /v18.0/{application-id}/ios_skadnetwork_conversion_config HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/ios_skadnetwork_conversion_config',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/ios_skadnetwork_conversion_config",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/ios_skadnetwork_conversion_config",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/ios_skadnetwork_conversion_config"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `dataset_id`<br><br>int64 | used for capi-g to fetch the skan config for dataset |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ConversionConfig](https://developers.facebook.com/docs/graph-api/reference/conversion-config/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Mmp Auditing
========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `mmp_auditing` edge from the following paths:

* [`/{application_id}/mmp_auditing`](https://developers.facebook.com/docs/graph-api/reference/application/mmp_auditing/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_id`<br><br>string | Apple's Advertising Identifier (IDFA) or Google Android's advertising ID. You can see how Facebook fetches this on [iOS](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT0N8x7Od9YakjJLEevOi6KpKvloXQN3JJIyg3sVDf9ZDsIq_t-ljirh8beyRj-B22CdXXmFRLvsDpgFGN6g-3dE3oMOCzT0wv82UWBL_WZ31eykDgngMwU4yR33wVNg4E3ALdhy5Pg2hLIDWUWFUA) or on [Android](https://developers.facebook.com/docs/reference/ads-api/mobile-conversions-endpoint/v2.2#android) |
| `attribution`<br><br>string | mobile\_cookie from the person's device. Use this only on Android or iOS devices before iOS 6. The format for this should look something like `DDDECD0A-C076-4050-8CE8-C20EC3FC2BD3` |
| `attribution_model`<br><br>string | attribution model that clients selected to be respected by MMP |
| `auditing_token`<br><br>string | Token provided in claim response sent to MMP |
| `click_attr_window`<br><br>int64 | Time window of click attribution |
| `custom_events`<br><br>list<CustomEvent> | Custom app events that MMP are sending auditing events for |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `decline_reason`<br><br>string | Reason that MMP rejected Facebook ads claim |
| `engagement_type`<br><br>string | Engagement type that MMP explicitly reports |
| `event`<br><br>string | Event type that Facebook claimed for<br><br>Required |
| `event_reported_time`<br><br>int64 | Time that event reported to MMP |
| `fb_ad_id`<br><br>int64 | FBID of the ads in Facebook claim<br><br>Required |
| `fb_click_time`<br><br>int64 | Ad click time in Facebook claim |
| `fb_view_time`<br><br>int64 | Ad view time in Facebook claim |
| `is_fb`<br><br>boolean | Result that whether MMP attribute the event to Facebook ads<br><br>Required |
| `used_install_referrer`<br><br>boolean | Identifies whether MMP used the install referrer |
| `view_attr_window`<br><br>int64 | Time window of view attribution |

### Return Type

Struct {

`success`: bool,

} Or Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Mobile Sdk Gk
=========================

[](#)

Reading
-------

ApplicationMobileSdkGk

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fmobile_sdk_gk&version=v18.0)

    GET /v18.0/{application-id}/mobile_sdk_gk HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/mobile_sdk_gk',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/mobile_sdk_gk",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/mobile_sdk_gk",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/mobile_sdk_gk"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `device_id`<br><br>string | Device ID |
| `extinfo`<br><br>Object | Extra Information |
| `0`<br><br>string | extinfo version<br><br>Required |
| `1`<br><br>string | app package name |
| `2`<br><br>string | short version (int or string) |
| `3`<br><br>string | long version |
| `4`<br><br>string | OS version |
| `5`<br><br>string | device model name |
| `6`<br><br>string | locale |
| `7`<br><br>string | timezone abbreviation |
| `8`<br><br>string | carrier |
| `9`<br><br>int64 | screen width |
| `10`<br><br>int64 | screen height |
| `11`<br><br>string | screen density (float decimal , or .) |
| `12`<br><br>int64 | CPU cores |
| `13`<br><br>int64 | external storage size in GB |
| `14`<br><br>int64 | free space on external storage in GB |
| `15`<br><br>string | device timezone |
| `platform`<br><br>enum {ANDROID, IOS} | SDK Platform<br><br>Required |
| `sdk_version`<br><br>string | SDK version<br><br>Required |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of MobileSdkGk nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Model Asset
=======================

[](#)

Reading
-------

ApplicationmodelAsset

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fmodel_asset&version=v18.0)

    GET /v18.0/{application-id}/model_asset HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/model_asset',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/model_asset",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/model_asset",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/model_asset"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of SDKMLModel nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Monetized Digital Store Objects
===========================================

[](#)

Reading
-------

ApplicationMonetizedDigitalStoreObjects

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fmonetized_digital_store_objects&version=v18.0)

    GET /v18.0/{application-id}/monetized_digital_store_objects HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/monetized_digital_store_objects',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/monetized_digital_store_objects",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/monetized_digital_store_objects",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/monetized_digital_store_objects"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of MonetizedDigitalStoreObject nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Object Types
========================

[](#)

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Objects
===================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Page Activities
===========================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `page_activities` edge from the following paths:

* [`/{application_id}/page_activities`](https://developers.facebook.com/docs/graph-api/reference/application/page_activities/)

When posting to this edge, an [Application](https://developers.facebook.com/docs/graph-api/reference/application/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `advertiser_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on iOS 6+, and that choice is stored within the phone. You should fetch that and return it to Facebook so we know not to use the data for optimization. We will, however, use the data to report on a conversion. See [here](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2Ffacebook-ios-sdk%2Fblob%2F7fe08877ea773dc35a5e4d6d9d305fae57c513b6%2Fsrc%2FCore%2FFBUtility.m%23L334-L357&h=AT3ZwqF507lEumFuGACDXhagBzUNXtKUBt-LjMlU3KzHawOtGy1Y_wJUN2h_j_6cHxTpL_LmJmp5HyiXNkSchDQJah6PUEnpBXD6brJ6DnVEaRb8qQ2vgTRX13iBa6IpdFw-FvkEc3Ogtk06tYMI8g) for an example of how Facebook fetches that variable. For devices running less than iOS 6, this query parameter can default to 1. Use 0 for disabled, 1 for enabled |
| `application_tracking_enabled`<br><br>boolean | A person can choose to enable ad tracking on an app level. Your SDK should allow an app developer to put an opt-out setting into their app. Use this field to specify the person's choice. Use 0 for disabled, 1 for enabled |
| `custom_events`<br><br>list<CustomEvent> | Custom events reported |
| `_eventName`<br><br>RegexParam | Event name, must match the regular expression /^\[0-9a-zA-Z\_\]\[0-9a-zA-Z \_-\]{0,39}$/<br><br>Required |
| `_eventName_md5`<br><br>RegexParam | MD5 hash of the event name, must match the regular expression /^\[A-Fa-f0-9\]{32}$/ |
| `_valueToSum`<br><br>float | Values to Sum |
| `_logTime`<br><br>int64 | Time to Log |
| `_implicitlyLogged`<br><br>int64 | Whether this is implicitly logged |
| `_isTimedEvent`<br><br>boolean | Whether this is a timed event |
| `_session_id`<br><br>string |     |
| `_app_user_id`<br><br>string |     |
| `logging_source`<br><br>enum {MESSENGER\_BOT, DETECTION} | Specifies the event source |
| `logging_target`<br><br>enum {APP, APP\_AND\_PAGE, PAGE} | Default value: `"APP"`<br><br>whether the event is logged to app level or page level or both |
| `page_id`<br><br>int64 | Specifies the Page ID associated with the messenger bot that logs the event |
| `page_scoped_user_id`<br><br>int64 | Specifies the page scoped User ID associated with the messenger bot that logs the event<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Payment Currencies
==============================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `payment_currencies` edge from the following paths:

* [`/{application_id}/payment_currencies`](https://developers.facebook.com/docs/graph-api/reference/application/payment_currencies/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `currency_url`<br><br>URL | SELF\_EXPLANATORY<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Permissions
=======================

[](#)

Reading
-------

Permissions that have been approved via Login Review

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fpermissions&version=v18.0)

    GET /v18.0/{application-id}/permissions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/permissions',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/permissions",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/permissions",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/permissions"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `android_key_hash`<br><br>string | The app key hash for the Android app |
| `ios_bundle_id`<br><br>string | Bundle ID of the iOS app |
| `permission`<br><br>List<Permission> | Name of permission |
| `proxied_app_id`<br><br>int | App ID of the original app. The main Facebook apps act as a proxy and pass this ID along with their call |
| `status`<br><br>list<enum{live, unapproved}> | Default value: `Vec`<br><br>Status of permission |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ApplicationPermission](https://developers.facebook.com/docs/graph-api/reference/application-permission/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

[`/{app-id}`](https://developers.facebook.com/docs/graph-api/reference/app/)`/picture`
======================================================================================

An app's profile picture.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapp-id%7D%2Fpicture&version=v18.0)

    GET /v18.0/{app-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/picture',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{app-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/picture",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

Because profile pictures are always public on Facebook, this call does not require any access token.

#### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `redirect` | The `picture` edge is a special case that returns the picture itself by default and not a JSON response. To return a JSON response, you need to set `redirect=false` as a request attribute. This is how you can return the [fields below](#readfields). | `bool` |
| `type` | You can use this to get a pre-specified size of picture. | `enum{small,large}` |

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    GET /v18.0/{app-id}/picture?redirect=0&height=200&type=normal&width=200 HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/picture?redirect=0&height=200&type=normal&width=200',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{app-id}/picture",
        {
            "redirect": false,
            "height": "200",
            "type": "normal",
            "width": "200"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putBoolean("redirect", false);
    params.putString("height", "200");
    params.putString("type", "normal");
    params.putString("width", "200");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/picture",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"redirect": @NO,
      @"height": @"200",
      @"type": @"normal",
      @"width": @"200",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/picture"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Fields

| Parameter | Description | Type |
| --- | --- | --- |
| `url` | The URL of the profile photo. Only returned when `redirect` is `false`. | `string` |

[](#)

Publishing
----------

You can't publish using this edge.

[](#)

Deleting
--------

You can't delete using this edge.

[](#)

Updating
--------

You can't update using this edge.

[](#)

[](#)

Application Products
====================

[](#)

Reading
-------

Get information on products associated with this app

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fproducts&version=v18.0)

    GET /v18.0/{application-id}/products HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/products',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/products",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/products",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/products"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `product_ids`<br><br>list<string> | List of product ids (e.g. 'golden\_gem') to retrieve info about |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [GamesIAPProduct](https://developers.facebook.com/docs/graph-api/reference/games-iap-product/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Purchases
=====================

[](#)

Reading
-------

Get information on purchases associated with this user-app pair

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fpurchases&version=v18.0)

    GET /v18.0/{application-id}/purchases HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/purchases',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/purchases",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/purchases",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/purchases"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of GamesIAPOrder nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

[`/{app-id}`](https://developers.facebook.com/docs/graph-api/reference/app/)`/roles`
====================================================================================

The developer roles defined for a Facebook app.

[](#)

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapp-id%7D%2Froles&version=v18.0)

    GET /v18.0/{app-id}/roles HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/roles',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/roles",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/roles"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Requirements

* An app access token for the app is required.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `app_id` | The ID of the app being requested. | `string` |
| `user` | The ID of the user who has a role in the app. | `string` |
| `role` | The name of the role that this person has. | `enum{administrators, developers, testers, insights users}` |

[](#)

Publishing
----------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

[](#)

[`/{app-id}`](https://developers.facebook.com/docs/graph-api/reference/app/)`/scores`
=====================================================================================

Scores from this Facebook game for a user and their friends.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapp-id%7D%2Fscores&version=v18.0)

    GET /v18.0/{app-id}/scores HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/scores',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{app-id}/scores",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/scores",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/scores"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token is required to view scores by that user and their friends, from the app that generated the token.

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `user` | The user who reached the score. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `application` | The app in which the score was reached. | [`App`](https://developers.facebook.com/docs/graph-api/reference/app/) |
| `score` | The score itself. | `int` |

[](#)

Publishing
----------

Use the [`/{user-id}/scores` edge](https://developers.facebook.com/docs/graph-api/reference/user/scores/) in order to create scores.

[](#)

Deleting
--------

You can delete all scores from your app using this edge. To delete individual scores, use the [`/{user-id}/scores` edge](https://developers.facebook.com/docs/graph-api/reference/user/scores/).

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    DELETE /v18.0/{app-id}/scores HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/{app-id}/scores',
        array (),
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{app-id}/scores",
        "DELETE",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/scores",
        null,
        HttpMethod.DELETE,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/scores"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token for the app is required.

### Fields

No fields are required.

### Response

`true` if successful, otherwise an error message.

[](#)

[](#)

This endpoint is deprecated as of April 4, 2018. Please see the [changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes/#4-4-2018) for more information.

[`/{app-id}`](https://developers.facebook.com/docs/graph-api/reference/app/)`/staticresources`
==============================================================================================

Usage statistics for any static resources used by a Facebook Canvas app.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapp-id%7D%2Fstaticresources&version=v18.0)

    GET /v18.0/{app-id}/staticresources HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/staticresources',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{app-id}/staticresources",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/staticresources",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/staticresources"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token for an admin of the app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `usage_stats` | Static resource URLs with the fractions of page loads that used each resource. | `array` |
| `prefetched_resources` | Static resource URLs that are currently being flushed early for users who are using the app. | `array` |
| `https` | An object containing `usage_stats` and `prefetched_resources` again, only showing resources accessed via HTTPS. | `object` |

[](#)

Publishing
----------

You can't publish using this edge.

[](#)

Deleting
--------

You can't delete using this edge.

[](#)

Related Topics
--------------

* [Resource Prefetching via Facebook SDK for JavaScript](https://developers.facebook.com/docs/reference/javascript/FB.Canvas.Prefetcher.addStaticResource)
    

[](#)

[](#)

Application Subscribed Domains
==============================

[](#)

Reading
-------

GETGraphApplicationSubscribedDomainsEdge

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fsubscribed_domains&version=v18.0)

    GET /v18.0/{application-id}/subscribed_domains HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/subscribed_domains',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/subscribed_domains",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/subscribed_domains",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/subscribed_domains"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [CTCertDomain](https://developers.facebook.com/docs/graph-api/reference/ct-cert-domain/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Application Subscribed Domains Phishing
=======================================

[](#)

Reading
-------

GETGraphApplicationSubscribedDomainsPhishingEdge

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapplication-id%7D%2Fsubscribed_domains_phishing&version=v18.0)

    GET /v18.0/{application-id}/subscribed_domains_phishing HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{application-id}/subscribed_domains_phishing',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/{application-id}/subscribed_domains_phishing",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{application-id}/subscribed_domains_phishing",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{application-id}/subscribed_domains_phishing"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [CTCertDomain](https://developers.facebook.com/docs/graph-api/reference/ct-cert-domain/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

[`/{app-id}`](https://developers.facebook.com/docs/reference/api/application/)`/subscriptions`
==============================================================================================

This edge allows you to read, create, update, and delete [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks/) subscriptions.

[Webhooks for Instagram](https://developers.facebook.com/docs/instagram-api/guides/webhooks) subscriptions are not supported and must be configured in your app's dashboard.

[](#)

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bapp-id%7D%2Fsubscriptions&version=v18.0)

    GET /v18.0/{app-id}/subscriptions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/subscriptions',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/subscriptions",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/subscriptions"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to return subscriptions for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered. | `string` |
| `fields` | The set of [fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` that are subscribed to. | `string[]` |
| `active` | Indicates whether or not the subscription is active. | `bool` |

[](#)

Publishing
----------

You can create new Webhooks subscriptions using this edge:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v18.0/{app-id}/subscriptions HTTP/1.1
    Host: graph.facebook.com
    
    object=page&callback_url=http%3A%2F%2Fexample.com%2Fcallback%2F&fields=about%2C+picture&include_values=true&verify_token=thisisaverifystring

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{app-id}/subscriptions',
        array (
          'object' => 'page',
          'callback_url' => 'http://example.com/callback/',
          'fields' => 'about, picture',
          'include_values' => 'true',
          'verify_token' => 'thisisaverifystring',
        ),
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    Bundle params = new Bundle();
    params.putString("object", "page");
    params.putString("callback_url", "http://example.com/callback/");
    params.putString("fields", "about, picture");
    params.putString("include_values", "true");
    params.putString("verify_token", "thisisaverifystring");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/subscriptions",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"object": @"page",
      @"callback_url": @"http://example.com/callback/",
      @"fields": @"about, picture",
      @"include_values": @"true",
      @"verify_token": @"thisisaverifystring",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/subscriptions"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

Making a POST request with the `callback_url`, `verify_token`, and `object` fields will reactivate the subscription.

### Permissions

* An app access token is required to add new subscriptions for that app.
    
* Subscriptions for the object type `user` will only be valid for users who have installed the app.
    
* Subscriptions for the object type `page` will only be valid for Pages that have installed the app. You can install the app for a Page using the [/{page-id}/subscribed\_apps edge](https://developers.facebook.com/docs/graph-api/reference/page/subscribed_apps).
    
* The app used to subscribe should be [set up to receive Webhooks updates](https://developers.facebook.com/docs/graph-api/webhooks/).
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | Indicates the object type that this subscription applies to. | `enum{user, page, permissions, payments}` |
| `callback_url` | The URL that will receive the `POST` request when an update is triggered, and a `GET` request when attempting this publish operation. See our [guide to constructing a callback URL page](https://developers.facebook.com/docs/graph-api/webhooks/#setup). | `string` |
| `fields` | One or more of the [set of valid fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` to subscribe to. | `string[]` |
| `include_values` | Indicates if change notifications should include the new values. | `bool` |
| `verify_token` | An arbitrary string that [can be used to confirm](https://developers.facebook.com/docs/graph-api/webhooks/) to your server that the request is valid. | `string` |

### Response

If your [callback URL is valid](https://developers.facebook.com/docs/graph-api/webhooks/) and the subscription is successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

[](#)

Deleting
--------

You can delete all or per-object subscriptions using this operation:

HTTPPHP SDKAndroid SDKiOS SDK

    DELETE /v18.0/{app-id}/subscriptions HTTP/1.1
    Host: graph.facebook.com
    
    object=page

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/{app-id}/subscriptions',
        array (
          'object' => 'page',
        ),
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    Bundle params = new Bundle();
    params.putString("object", "page");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/subscriptions",
        params,
        HttpMethod.DELETE,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"object": @"page",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/subscriptions"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

You can delete specific fields from your subscription by including a `fields` param.

### Permissions

* An app access token is required to delete subscriptions for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `object` | A specific object type to remove subscriptions for. If this optional field is not included, all subscriptions for this app will be removed. | `enum{user, page, permissions, payments}` |
| `fields` | One or more of the [set of valid fields](https://developers.facebook.com/docs/graph-api/webhooks/) in this `object` to subscribe to. | `string[]` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

[](#)

Updating
--------

You can perform updates on this edge by performing [a publish operation](#publish) with new values. This will amend the susbcription for the given topic without overwriting existing fields.

[](#)

[](#)

[`/{app-id}`](https://developers.facebook.com/docs/reference/api/application/)`/translations`
=============================================================================================

The strings from this app that were translated using our [translations tools](https://developers.facebook.com/docs/internationalization).

[](#)

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDK

    GET /v18.0/{app-id}/translations?locale=fr_FR HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{app-id}/translations?locale=fr_FR',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    Bundle params = new Bundle();
    params.putString("locale", "fr_FR");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/translations",
        params,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"locale": @"fr_FR",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/translations"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to return translations for that app.
    

### Modifiers

| Name | Description | Type |
| --- | --- | --- |
| `locale` | Specifies which locale of language to request. This is a required parameter when reading this edge. | `enum{`[locale](https://www.facebook.com/translations/FacebookLocales.xml)`}` |

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | A unique ID for each individual string. | `string` |
| `translation` | The translated string. | `string` |
| `approval_status` | The approval status of the string. | `enum{auto-approved, approved, unapproved}` |
| `native_string` | The original string that was translated. | `string` |
| `description` | The provided description of the string. | `string` |

[](#)

Publishing
----------

You can specify new strings to be translated for your app using this edge:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v18.0/{app-id}/translations HTTP/1.1
    Host: graph.facebook.com
    
    native_strings=%5B%7B%22text%22%3A%22Test+String%22%2C+%22description%22%3A+%22This+is+a+test+string+for+an+app.%22%7D%5D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{app-id}/translations',
        array (
          'native_strings' => '[{"text":"Test String", "description": "This is a test string for an app."}]',
        ),
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    Bundle params = new Bundle();
    params.putString("native_strings", "[{\"text\":\"Test String\", \"description\": \"This is a test string for an app.\"}]");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/translations",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"native_strings": @"[{\"text\":\"Test String\", \"description\": \"This is a test string for an app.\"}]",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/translations"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to add new translation strings for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| Vector | Vector | Vector |

#### Response

If successful, you will receive a plain response of the number of strings that were added, otherwise an error message.

[](#)

Deleting
--------

You can delete translation strings using this operation:

HTTPPHP SDKAndroid SDKiOS SDK

    DELETE /v18.0/{app-id}/translations HTTP/1.1
    Host: graph.facebook.com
    
    native_hashes=%5B%27hash1%27%2C+%27hash2%27%5D

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/{app-id}/translations',
        array (
          'native_hashes' => '[\'hash1\', \'hash2\']',
        ),
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    Bundle params = new Bundle();
    params.putString("native_hashes", "['hash1', 'hash2']");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{app-id}/translations",
        params,
        HttpMethod.DELETE,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"native_hashes": @"['hash1', 'hash2']",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{app-id}/translations"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to delete translation strings from that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `native_hashes` | An array of hashes for each translation string. The hash is a unique identifier for each string, and can be retrieved using the [`translation` FQL table](https://developers.facebook.com/docs/reference/fql/translation/). | `string[]` |

#### Response

If successful, you will receive a plain response of the number of strings that were deleted, otherwise an error message.

[](#)

[](#)

Application Uploads
===================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

Create an upload session.

Upload session IDs returned by this endpoint can be used to upload large files, get the status of an upload session, or resume an interrupted session. See the [Resumable Upload API](https://developers.facebook.com/docs/graph-api/guides/upload) document for complete usage instructions.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) or [System User](https://developers.facebook.com/docs/marketing-api/system-users/overview#system-user-access-token). The app user who granted the token must have an Administrator or Developer [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on the app. |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None. |

You can make a POST request to `uploads` edge from the following paths:

* [`/{application_id}/uploads`](https://developers.facebook.com/docs/graph-api/reference/application/uploads/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `file_length`<br><br>int64 | The file length in bytes |
| `file_name`<br><br>RegexParam | The name of the file to be uploaded |
| `file_type`<br><br>RegexParam | The MIME type of the file to be uploaded |
| `session_type`<br><br>enum {attachment} | Default value: `attachment`<br><br>The type of upload session that is being requested by the app |

### Return Type

Struct {

`id`: string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)