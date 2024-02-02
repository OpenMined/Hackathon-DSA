Graph API App













DocsToolsSupportLog InGraph API* Overview
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
	+ Ads Archive
	+ Album
	+ App Link Host
	+ Application
		- Accounts
		- Application Achievements
		- Activities
		- Ad Placement Groups
		- Adnetworkanalytics Results
		- Aem Attribution
		- Aem Conversion Configs
		- Aem Conversion Filter
		- Agencies
		- App Event Types
		- App Indexing
		- App Installed Groups
		- Appassets
		- Assets
		- Button Auto Detection Device Selection
		- Cloudbridge Settings
		- Codeless Event Mappings
		- Da Checks
		- Events
		- Page/insights
		- Ios Skadnetwork Conversion Config
		- Mmp Auditing
		- Mobile Sdk Gk
		- Model Asset
		- Monetized Digital Store Objects
		- Object Types
		- Objects
		- Page Activities
		- Payment Currencies
		- Permissions
		- Picture
		- Products
		- Purchases
		- Roles
		- Scores
		- Static Resources
		- Subscribed Domains
		- Subscribed Domains Phishing
		- Subscriptions
		- Translations
		- Uploads
	+ Branded Content Search
	+ CPASAdvertiser Partnership Recommendation
	+ Canvas
	+ Canvas Button
	+ Canvas Carousel
	+ Canvas Footer
	+ Canvas Header
	+ Canvas Photo
	+ Canvas Product List
	+ Canvas Product Set
	+ Canvas Text
	+ Canvas Video
	+ Collaborative Ads Directory
	+ Comment
	+ Commerce Merchant Settings
	+ Conversation
	+ Debug Token
	+ Event
	+ Games IAPProduct
	+ Group
	+ Group Doc
	+ Group Message
	+ Image Copyright
	+ Instagram Oembed
	+ Link
	+ Live Video
	+ Live Video Input Stream
	+ Mailing Address
	+ Media Fingerprint
	+ Message
	+ Milestone
	+ Object Comments
	+ Object Likes
	+ Object Private Replies
	+ Object Reactions
	+ Object Sharedposts
	+ Oembed Page
	+ Oembed Post
	+ Oembed Video
	+ Offline Conversion Data Set Upload
	+ Page
	+ Page Call To Action
	+ Page Post
	+ Page Upcoming Change
	+ Page/insights
	+ Payment
	+ Photo
	+ Place
	+ Place Tag
	+ Place Topic
	+ Post
	+ Profile
	+ Request
	+ Test User
	+ Thread
	+ URL
	+ User
	+ Video
	+ Video Copyright
	+ Video List
	+ Video Poll
	+ Video Poll Option
	+ Whats App Business Account
	+ Whats App Message Template
On This PageFacebook AppReadingPermissionsExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingPermissionsExampleParametersReturn TypeError CodesDeletingParametersReturn TypeError CodesGraph API Versionv18.0Facebook App

A Facebook app.

Reading
-------


 Get information about a Facebook app.
 ### Permissions

* An app access token can be used to view all fields for an app.
### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{application-id} HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
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
/\* handle the result \*/
```

```
/\* make the API call \*/
FB.api(
 "/{application-id}",
 function (response) {
 if (response && !response.error) {
 /\* handle the result \*/
 }
 }
);
```

```
/\* make the API call \*/
new GraphRequest(
 AccessToken.getCurrentAccessToken(),
 "/{application-id}",
 null,
 HttpMethod.GET,
 new GraphRequest.Callback() {
 public void onCompleted(GraphResponse response) {
 /\* handle the result \*/
 }
 }
).executeAsync();
```

```
/\* make the API call \*/
FBSDKGraphRequest \*request = [[FBSDKGraphRequest alloc]
 initWithGraphPath:@"/{application-id}"
 parameters:params
 HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection,
 id result,
 NSError \*error) {
 // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

This endpoint doesn't have any parameters.### Fields



| Field | Description |
| --- | --- |
| `id`numeric string | The app ID
Core |
| `aam_rules`string | Rules of Auto Advanced Matching in FB SDKs
 |
| `an_ad_space_limit`unsigned int32 | The maximum number of Ad Spaces allowed for each Audience Network supported platform
 |
| `an_platforms`list<enum> | The platforms associated with the app in the Audience Network product. Not enforced, but when present, it can be used to provide the user with platform specific information for the app and its placements
 |
| `app_domains`list<string> | Domains and subdomains this app can use
 |
| `app_events_config`ApplicationAppEventsConfig | Configuration for app events
 |
| `app_install_tracked`bool | Whether the app install is trackable or not
 |
| `app_name`string | App name
 |
| `app_signals_binding_ios`list<Binding> | List of app event bindings for iOS app
 |
| `app_type`unsigned int32 | App type
 |
| `auth_dialog_data_help_url`string | The URL of a special landing page that helps people who are using an app begin publishing Open Graph activity
 |
| `auth_dialog_headline`string | One line description of an app that appears in the Login Dialog
 |
| `auth_dialog_perms_explanation`string | The text to explain why an app needs additional permissions. This appears in the Login Dialog
 |
| `auth_referral_default_activity_privacy`string | The default privacy setting selected for Open Graph activities in the Auth Dialog
 |
| `auth_referral_enabled`unsigned int32 | Indicates whether Authenticated Referrals are enabled
 |
| `auth_referral_extended_perms`list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled
 |
| `auth_referral_friend_perms`list<string> | Basic friends permissions that a user must grant when Authenticated Referrals are enabled
 |
| `auth_referral_response_type`string | The format that an app receives for the authentication token from the Login Dialog
 |
| `auth_referral_user_perms`list<string> | Basic user permissions that a user must grant when Authenticated Referrals are enabled
 |
| `canvas_fluid_height`bool | Indicates whether the app uses fluid or settable height values for Canvas
 |
| `canvas_fluid_width`unsigned int32 | Indicates whether the app uses fluid or fixed width values for Canvas
 |
| `canvas_url`string | The non-secure URL from which Canvas app content is loaded
 |
| `category`string | The category of the app
Default |
| `client_config`map | Config data for the client
 |
| `company`string | The company the app belongs to
 |
| `configured_ios_sso`bool | True if the app has configured Single Sign On on iOS
 |
| `contact_email`string | Email address listed for people using the app to contact developers
 |
| `created_time`datetime | Timestamp that indicates when the app was created
 |
| `creator_uid`id | User ID of the creator of this app
 |
| `daily_active_users`numeric string | The number of daily active users the app has
 |
| `daily_active_users_rank`unsigned int32 | Ranking of this app vs other apps comparing daily active users
 |
| `deauth_callback_url`string | URL that is pinged whenever a person removes the app
 |
| `default_share_mode`string | The platform that should be used to share content
 |
| `description`string | The description of the app, as provided by the developer
Core |
| `financial_id`string | The ID for the corresponding audience network financial entity.
 |
| `hosting_url`string | Webspace created with one of our hosting partners for this app
 |
| `icon_url`string | The URL of this app's icon
 |
| `ios_bundle_id`list<string> | Bundle ID of the associated iOS app
 |
| `ios_supports_native_proxy_auth_flow`bool | Whether to support the native proxy login flow
 |
| `ios_supports_system_auth`bool | Whether to support the iOS integrated Login Dialog
 |
| `ipad_app_store_id`string | ID of the app in the iPad App Store
 |
| `iphone_app_store_id`string | ID of the app in the iPhone App Store
 |
| `latest_sdk_version`ApplicationSDKInfo | App latest sdk version
 |
| `link`string | A link to the app on Facebook
CoreDefault |
| `logging_token`string | To use for logging purposes
 |
| `logo_url`string | The URL of the app's logo
 |
| `migrations`map<string, bool> | Status of migrations for this app
 |
| `mobile_profile_section_url`string | Mobile URL of the app section on a person's profile
 |
| `mobile_web_url`string | URL to which Mobile users will be directed when using the app
 |
| `monthly_active_users`numeric string | The number of monthly active users the app has
 |
| `monthly_active_users_rank`unsigned int32 | Ranking of this app vs other apps comparing monthly active users
 |
| `name`string | The name of the app
CoreDefault |
| `namespace`string | The string appended to `apps.facebook.com/` to navigate to the app's canvas page
CoreDefault |
| `object_store_urls`ApplicationObjectStoreURLs | Mobile store URLs for the app
 |
| `page_tab_default_name`string | The title of the app when used in a Page Tab
 |
| `page_tab_url`string | The non-secure URL from which Page Tab app content is loaded
 |
| `photo_url`string | The URL of the app photo
 |
| `privacy_policy_url`string | The URL that links to a Privacy Policy for the app
 |
| `profile_section_url`string | URL of the app section on a user's profile for the desktop site
 |
| `property_id`string | The monetization property which owns this app
 |
| `protected_mode_rules`ApplicationProtectedModeRules | protected\_mode\_rules
 |
| `real_time_mode_devices`list<string> | List of real time hashed device
 |
| `restrictions`ApplicationRestrictionInfo | Demographic restrictions for the app
 |
| `restrictive_data_filter_params`string | Params used to filter out restrictive data
 |
| `secure_canvas_url`string | The secure URL from which Canvas app content is loaded
 |
| `secure_page_tab_url`string | The secure URL from which Page Tab app content is loaded
 |
| `server_ip_whitelist`string | App requests must originate from this comma-separated list of IP addresses
 |
| `social_discovery`unsigned int32 | Indicates whether app usage stories show up in the Ticker or Feed
 |
| `subcategory`string | The subcategory the app can be found under
 |
| `suggested_events_setting`string | Settings for suggested events
 |
| `supported_platforms`list<enum {WEB, CANVAS, MOBILE\_WEB, IPHONE, IPAD, ANDROID, WINDOWS, AMAZON, SUPPLEMENTARY\_IMAGES, GAMEROOM, INSTANT\_GAME, OCULUS, SAMSUNG, XIAOMI}> | All the platform the app supports
 |
| `terms_of_service_url`string | URL to Terms of Service that appears in the Login Dialog
 |
| `url_scheme_suffix`string | URL scheme suffix
 |
| `user_support_email`string | Main contact email for this app where people can receive support
 |
| `user_support_url`string | URL shown in the Canvas footer that people can visit to get support for the app
 |
| `website_url`string | URL of a website that integrates with this app
 |
| `weekly_active_users`numeric string | The number of weekly active users the app has
 |

### Edges



| Edge | Description |
| --- | --- |
| `accounts` | Test User accounts associated with the app
 |
| `ad_placement_groups` | Ad placement groups for publishing ads on this app
 |
| `adnetworkanalytics_results` | Obtain the results of an async Audience Network query for this publisher entity
 |
| `aem_attribution` | aem\_attribution
 |
| `aem_conversion_configs` | The aggregated event measurement conversion value configs for this app
 |
| `aem_conversion_filter` | Boolean for if product\_set\_id [fb\_content\_id] belongs to a certain catalog [catalog\_id]
 |
| `agencies` | The businesses which are not owner but can advertise for this app
 |
| `app_event_types` | Info about App Events logged for the app
 |
| `app_installed_groups` | List of facebook groups the app is installed in
 |
| `appassets` | appassets
 |
| `button_auto_detection_device_selection` | Whether to turn on auto device sampling.
 |
| `cloudbridge_settings` | cloudbridge\_settings
 |
| `da_checks` | A list of results after running Dynamic Ads checks on this app.
 |
| `events` | Events
 |
| `ios_skadnetwork_conversion_config` | ios\_skadnetwork\_conversion\_config
 |
| `mobile_sdk_gk` | Gatekeeper for Mobile SDK
 |
| `model_asset` | model\_asset
 |
| `monetized_digital_store_objects` | List of digital store objects for this app monetized via Audience Network
 |
| `object_types` | Open Graph Object types associated with this app
 |
| `objects` | Open Graph objects
 |
| `permissions` | The status of permissions that are have been submitted for Login Review
 |
| `products` | In-app-purchaseable products associated with this app
 |
| `purchases` | In-app-purchaseable products of this app owned by the user
 |
| `roles` | The developer roles defined for this app
 |
| `subscribed_domains` | subscribed\_domains
 |
| `subscribed_domains_phishing` | subscribed\_domains\_phishing
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 278 | Reading advertisements requires an access token with the extended permission ads\_read |

Creating
--------

You can make a POST request to `owned_apps` edge from the following paths: * `/{business_id}/owned_apps`

When posting to this edge, an Application will be created.### Parameters

This endpoint doesn't have any parameters.### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`access_status`: string, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `app_indexing` edge from the following paths: * `/{application_id}/app_indexing`

When posting to this edge, an Application will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `app_version`string | The version of the app being indexed
Required |
| `device_session_id`string | Device session id of the uploading device
 |
| `extra_info`string | Extra information about the app index
 |
| `platform`enum {ANDROID, IOS} | The platform of the app being indexed
Required |
| `request_type`enum {APP\_INDEXING, PLUGIN, BUTTON\_SAMPLING} | Default value: `"APP_INDEXING"`Type of the app indexing request
 |
| `tree`JSON object | The UI component tree of the app
Required |
| `screenname`string |  |
| `screenshot`string |  |
| `view`list<JSON encoded app UI component> | Required |

### Return Type

 Struct {`success`: bool, `is_app_indexing_enabled`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can make a POST request to `codeless_event_mappings` edge from the following paths: * `/{application_id}/codeless_event_mappings`

When posting to this edge, an Application will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `mappings`array<JSON object> | The event to UI component mappings of the app
Required |
| `method`enum {INFERENCE, MANUAL, CONFIRMED\_INFERENCE, BUTTON\_INDEXING, UNKNOWN} | method
Required |
| `event_name`string | event\_name
Required |
| `event_type`enum {CLICK, SELECTED, TEXT\_CHANGED} | event\_type
Required |
| `app_version`string | app\_version
Required |
| `parameters`array<JSON object> | parameters
 |
| `name`string | name
Required |
| `path`array<JSON object> | path
Required |
| `class_name`string | class\_name
Required |
| `index`int64 | index
Required |
| `id`int64 | id
 |
| `text`string | text
 |
| `tag`string | tag
 |
| `description`string | description
 |
| `hint`string | hint
 |
| `match_bitmask`int64 | match\_bitmask
 |
| `path_type`enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`path\_type
 |
| `component_id`string | component\_id
Required |
| `path`array<JSON object> | path
Required |
| `class_name`string | class\_name
Required |
| `index`int64 | index
Required |
| `id`int64 | id
 |
| `text`string | text
 |
| `tag`string | tag
 |
| `description`string | description
 |
| `hint`string | hint
 |
| `match_bitmask`int64 | match\_bitmask
 |
| `component_id`string | component\_id
Required |
| `path_type`enum {ABSOLUTE, RELATIVE} | Default value: `"ABSOLUTE"`path\_type
 |
| `screenshot_handle`string | screenshot\_handle
 |
| `dimensions`array<JSON object> | dimensions
 |
| `top`int64 | top
Required |
| `left`int64 | left
Required |
| `width`int64 | width
Required |
| `height`int64 | height
Required |
| `activity_name`string | activity\_name
 |
| `mutation_method`enum {REPLACE, ADD, DELETE} | Detailed mutation type like replace, add
Required |
| `platform`enum {ANDROID, IOS} | The platform of the app being indexed
Required |
| `post_method`enum {EYMT, CODELESS} | Default value: `"CODELESS"`Whether the api is called by codeless or EYMT
 |

### Return Type

 Struct {`num_updated`: int32, `num_invalid`: int32, }### Error Codes



| Error | Description |
| --- | --- |
| 105 | The number of parameters exceeded the maximum for this operation |

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

You can make a POST request to `client_apps` edge from the following paths: * `/{business_id}/client_apps`

When posting to this edge, an Application will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `app_id` | App ID.
Required |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`access_status`: enum, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

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

Update application information such as demographic restrictions.


### Permissions


* An app access token is required to update fields on an app.


### Example


To update an app restrictions, such as `age`, send a `POST` request to `/{app-id}`:


`curl -i -X POST "https://graph.facebook.com/{app-id}?restrictions={'age':'21+'}&access_token={app-access-token}"`


On success your app receives this response:


`{
"success": true
}`


You can update an Application by making a POST request to `/{application_id}`.### Parameters



| Parameter | Description |
| --- | --- |
| `allow_cycle_app_secret`boolean | Default value: `false`Allows for the application to cycle the secret
 |
| `an_platforms`list<enum {ANDROID, DESKTOP, GALAXY, INSTANT\_ARTICLES, IOS, MOBILE\_WEB, OCULUS, UNKNOWN, XIAOMI}> | The platforms associated with the app in the AudienceNetwork product
 |
| `app_domains`list<string> | Specifies a list of domains that correspond to this app. Subdomains of domains in this array are also considered to belong to this app
 |
| `app_name`string | App name
 |
| `app_type`boolean | App type
 |
| `auth_dialog_headline`string | One line description of this app that appears in the Login Dialog
 |
| `auth_dialog_perms_explanation`string | The text to explain why an app needs additional permissions. This appears in the Login Dialog
 |
| `auth_referral_default_activity_privacy`string | The default privacy setting selected for Open Graph activities in the Auth Dialog
 |
| `auth_referral_enabled`boolean | Enables or disables Authenticated Referrals
 |
| `auth_referral_extended_perms`list<string> | Extended permissions that a person can choose to grant when Authenticated Referrals are enabled
 |
| `auth_referral_friend_perms`list<string> | Basic friends permissions that a person must grant when Authenticated Referrals are enabled
 |
| `auth_referral_response_type`string | The format of the authentication token this app receives from the Login Dialog
 |
| `auth_referral_user_perms`list<string> | Basic permissions that a person must grant when Authenticated Referrals are enabled
 |
| `canvas_fluid_height`boolean | Indicates whether this app uses fluid or settable height values for Canvas
 |
| `canvas_fluid_width`boolean | Indicates whether this app uses fluid or fixed width values for Canvas
 |
| `canvas_url`URL | The non-secure URL from which Canvas app content is loaded
 |
| `contact_email`string | Email address users can use to contact developers
 |
| `deauth_callback_url`URL | URL that is pinged whenever a person removes this app
 |
| `mobile_web_url`URL | URL that mobile users will be directed to when using this app
 |
| `namespace`string | The string appended to `apps.facebook.com/` to navigate to this app's Canvas page
 |
| `page_tab_default_name`string | The title of this app as it appears in a Page Tab
 |
| `privacy_policy_url`URL | The URL that links to a privacy policy for this app
 |
| `restrictions`JSON-encoded string | Update demographic restrictions for this app. Can be one or more of the following parameters: `age`, `location`, or `type`. `age` can be one of the following values: `13+`, `16+`, `17+`, `18+`, `19+`, or `21+`. `location` can be one or more country represented by the 2 letter country code. `type` can only be `alcohol`.
 |
| `secure_canvas_url`URL | The secure URL from which Canvas app content is loaded
 |
| `secure_page_tab_url`URL | The secure URL from which Page Tab app content is loaded
 |
| `server_ip_whitelist`list<string> | App requests must originate from this comma-separated list of IP addresses
 |
| `terms_of_service_url`URL | URL to Terms of Service that appears in the Login Dialog
 |
| `url_scheme_suffix`string | URL scheme suffix
 |
| `user_support_email`string | Main contact email for this app where people can receive support
 |
| `user_support_url`URL | URL shown in the Canvas footer that people can visit to get support for this app
 |
| `website_url`URL | URL of a website that integrates with this app
 |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

You can update an Application by making a POST request to `/act_{ad_account_id}/subscribed_apps`.### Parameters



| Parameter | Description |
| --- | --- |
| `app_id`string | Default value: the id of app to be subscribed from ad account
 |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

Deleting
--------

You can dissociate an Application from a Page by making a DELETE request to `/{page_id}/subscribed_apps`.### Parameters

This endpoint doesn't have any parameters.### Return Type

 Struct {`success`: bool, `messaging_success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 210 | User not visible |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

You can dissociate an Application from an AdAccount by making a DELETE request to `/act_{ad_account_id}/subscribed_apps`.### Parameters



| Parameter | Description |
| --- | --- |
| `app_id`string | Default value: the id of app to be unsubscribed from ad account
 |

### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

On This PageFacebook AppReadingPermissionsExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingPermissionsExampleParametersReturn TypeError CodesDeletingParametersReturn TypeError CodesFollow Us* 
#### Products

* Artificial Intelligence
* AR/VR
* Business Tools
* Gaming
* Open Source
* Publishing
* Social Integrations
* Social Presence
#### Programs

* ThreatExchange
#### Support

* Developer Support
* Bugs
* Platform Status
* Report a Platform Data Incident
* Facebook for Developers Community Group
* Sitemap
#### News

* Blog
* Success Stories
* Videos
* Meta for Developers Page
#### Terms and Policies

* Platform Initiatives Hub
* Platform Terms
* Developer Policies
* European Commission Commitments
Follow Us* 
 © 2024 Meta * About
* Create Ad
* Careers
* Privacy Policy
* Cookies
* Terms
English (US)Bahasa IndonesiaDeutschEspañolEspañol (España)Français (France)ItalianoPortuguês (Brasil)Tiếng ViệtРусскийالعربيةภาษาไทย한국어中文(香港)中文(台灣)中文(简体)日本語English (US)





































Allow the use of cookies from Facebook on this browser?We use cookies and similar technologies to help:Provide and improve content on Meta ProductsProvide a safer experience by using information we receive from cookies on and off FacebookProvide and improve Meta Products for people who have an accountFor advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you, we use tools from other companies on Facebook. These companies also use cookies.You can allow the use of all cookies, just essential cookies or you can choose more options below. You can learn more about cookies and how we use them, and review or change your choice at any time in our Cookie Policy.Essential cookiesThese cookies are required to use Meta Products. They’re necessary for these sites to work as intended.Optional cookies

Cookies from other companiesWe use tools from other companies for advertising and measurement services off of Meta Products, analytics, and to provide certain features and improve our services for you. These companies also use cookies.More informationIf you allow these cookies:

* We’ll be able to better personalize ads for you off of Meta Products, and measure their performance
* Features on our products will not be affected
* Other companies will receive information about you by using cookies

If you don’t allow these cookies:

* We won’t use cookies from other companies to help personalize ads for you off of Meta Products, or to measure their performance
* Some features on our products may not work

Other ways you can control your information

Manage your ad experience in Accounts CenterIf you have a Facebook account, you can manage how different data is used to personalize ads with these tools.

Ad settings

To show you better ads, we use data that advertisers and other partners provide us about your activity off Meta Company Products, including websites and apps. You can control whether we use this data to show you ads in your ad settings.

The Meta Audience Network is a way for advertisers to show you ads in apps and websites off the Meta Company Products. One of the ways Audience Network shows relevant ads is by using your ad preferences to determine which ads you may be interested in seeing. You can control this in your ad settings.

Ad preferences

In Ad preferences, you can choose whether we show you ads and make choices about the information used to show you ads.

Off-Facebook activity

You can review your off-Facebook activity, which is a summary of activity that businesses and organizations share with us about your interactions with them, such as visiting their apps or websites. They use our Business Tools, such as Facebook Login or Meta Pixel, to share this information with us. This helps us do things such as give you a more personalized experience on Meta Products. Learn more about off-Facebook activity, how we use it, and how you can manage it.

More information about online advertisingYou can opt out of seeing online interest-based ads from Meta and other participating companies through the Digital Advertising Alliance in the US, the Digital Advertising Alliance of Canada in Canada or the European Interactive Digital Advertising Alliance in Europe, or through your mobile device settings, if you are using Android, iOS 13 or an earlier version of iOS. Please note that ad blockers and tools that restrict our cookie use may interfere with these controls.

The advertising companies we work with generally use cookies and similar technologies as part of their services. To learn more about how advertisers generally use cookies and the choices they offer, you can review the following resources:

* Digital Advertising Alliance
* Digital Advertising Alliance of Canada
* European Interactive Digital Advertising Alliance
Controlling cookies with browser settingsYour browser or device may offer settings that allow you to choose whether browser cookies are set and to delete them. These controls vary by browser, and manufacturers may change both the settings they make available and how they work at any time. As of 5 October 2020, you may find additional information about the controls offered by popular browsers at the links below. Certain parts of Meta Products may not work properly if you have disabled browser cookies. Please be aware that these controls are distinct from the controls that Facebook offers.

* Google Chrome
* Internet Explorer
* Firefox
* Safari
* Safari Mobile
* Opera
Only allow essential cookiesAllow essential and optional cookies