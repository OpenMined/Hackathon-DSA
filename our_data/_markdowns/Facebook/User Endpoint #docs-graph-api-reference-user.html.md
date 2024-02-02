Graph API User - Documentation - Meta for Developers

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
Graph API Versionv19.0User
====
Represents a Facebook user.

Reading
-------
Get fields and edges on a User.

### Requirements

 Type | Description || Access Tokens | User |
| Permissions | public\_profile |
### New Page Experience
This endpoint is supported for New Page Experience.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
GET /v19.0/{person-id}/ HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{person-id}/',
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
```
```
/* make the API call */
FB.api(
    "/{person-id}/",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{person-id}/",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{person-id}/"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
```
curl -X GET -G \
  -d 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/{person-id}/
```
If you want to learn how to use the Graph API, read our Using Graph API guide.  
### Default Public Profile Fields

The `public_profile` permission allows apps to read the following fields:

* `id`
* `first_name`
* `last_name`
* `middle_name`
* `name`
* `name_format`
* `picture`
* `short_name`

### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | The app user's App-Scoped User ID. This ID is unique to the app and cannot be used by other apps.
Core |
| `about`string | *Returns no data as of April 4, 2018.*
 |
| `age_range`AgeRange | The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21.
Core |
| `birthday`string | The person's birthday. This is a fixed format string, like `MM/DD/YYYY`. However, people can control who can see the year they were born separately from the month and day so this string can be only the year (YYYY) or the month + day (MM/DD)
Core |
| `education`list<EducationExperience> | *Returns no data as of April 4, 2018.*
 |
| `email`string | The User's primary email address listed on their profile. This field will not be returned if no valid email address is available.
Core |
| `favorite_athletes`list<Experience> | Athletes the User likes.
 |
| `favorite_teams`list<Experience> | Sports teams the User likes.
 |
| `first_name`string | The person's first name
Core |
| `gender`string | The gender selected by this person, `male` or `female`. If the gender is set to a custom value, this value will be based off of the selected pronoun; it will be omitted if the pronoun is neutral.
Core |
| `hometown`Page | The person's hometown
 |
| `id_for_avatars`numeric string | A profile based app scoped ID. It is used to query avatars
 |
| `inspirational_people`list<Experience> | The person's inspirational people
 |
| `installed`bool | Is the app making the request installed
 |
| `is_guest_user`bool | if the current user is a guest user. should always return false.
 |
| `languages`list<Experience> | Facebook Pages representing the languages this person knows
 |
| `last_name`string | The person's last name
Core |
| `link`string | A link to the person's Timeline. The link will only resolve if the person clicking the link is logged into Facebook and is a friend of the person whose profile is being viewed.
Core |
| `local_news_megaphone_dismiss_status`bool | Display megaphone for local news bookmark
Deprecated |
| `local_news_subscription_status`bool | Daily local news notification
Deprecated |
| `locale`string | The person's locale
CoreDeprecated |
| `location`Page | The person's current location as entered by them on their profile. This field requires the `user_location` permission.
Core |
| `meeting_for`list<string> | What the person is interested in meeting for
 |
| `middle_name`string | The person's middle name
Core |
| `name`string | The person's full name
CoreDefault |
| `name_format`string | The person's name formatted to correctly handle Chinese, Japanese, or Korean ordering
 |
| `political`string | *Returns no data as of April 4, 2018.*
 |
| `quotes`string | The person's favorite quotes
 |
| `relationship_status`string | *Returns no data as of April 4, 2018.*
 |
| `shared_login_upgrade_required_by`timestamp | The time that the shared login needs to be upgraded to Business Manager by
 |
| `significant_other`User | The person's significant other
 |
| `sports`list<Experience> | Sports played by the person
 |
| `supports_donate_button_in_live_video`bool | Whether the user can add a Donate Button to their Live Videos
 |
| `third_party_id`string | A string containing an anonymous, unique identifier for the User, for use with third-parties. Deprecated for versions 3.0+. Apps using older versions of the API can get this field until January 8, 2019. Apps installed by the User on or after May 1st, 2018, cannot get this field.
Deprecated |
| `timezone`float (min: -24) (max: 24) | The person's current timezone offset from UTC
CoreDeprecated |
| `token_for_business`string | A token that is the same across a business's apps. Access to this token requires that the person be logged into your app or have a role on your app. This token will change if the business owning the app changes
 |
| `updated_time`datetime | Updated time
Deprecated |
| `verified`bool | Indicates whether the account has been verified. This is distinct from the `is_verified` field. Someone is considered verified if they take any of the following actions:
```
                                                                                                                                                                    * Register for mobile
                                                                                                                                                                    * Confirm their account via SMS
                                                                                                                                                                    * Enter a valid credit card
```
Deprecated |
| `video_upload_limits`VideoUploadLimits | Video upload limits
 |
| `website`string | *Returns no data as of April 4, 2018.*
 |
### Edges

| Edge | Description |
| --- | --- |
| `accounts` | Pages the User has a role on.
 |
| `ad_studies` | Ad studies that this User's can view.
 |
| `albums` | The photo albums this person has created
 |
| `apprequestformerrecipients` | App requests
 |
| `apprequests` | This person's pending requests from an app
Core |
| `assigned_business_asset_groups` | Business asset groups that are assign to this business scoped user
 |
| `assigned_pages` | Pages that are assigned to this business scoped user
 |
| `assigned_product_catalogs` | Product catalogs that are assigned to this business scoped user
 |
| `business_users` | Business users corresponding to the user
 |
| `businesses` | Businesses associated with the user
 |
| `conversations` | Facebook Messenger conversation
 |
| `custom_labels` | custom\_labels
 |
| `feed` | The posts and links published by this person or others on their profile
 |
| `ids_for_apps` | Businesses can claim ownership of multiple apps using Business Manager. This edge returns the list of IDs that this user has in any of those other apps
 |
| `ids_for_business` | Businesses can claim ownership of multiple apps using Business Manager. This edge returns the list of IDs that this user has in any of those other apps
 |
| `ids_for_pages` | Businesses can claim ownership of apps and pages using Business Manager. This edge returns the list of IDs that this user has in any of the pages owned by this business
 |
| `likes` | All the Pages this person has liked
 |
| `live_videos` | Live videos from this person
 |
| `music` | Music this person likes
 |
| `payment.subscriptions` | Payment subscriptions
 |
| `permissions` | The permissions that the person has granted this app
Core |
| `photos` | Photos the person is tagged in or has uploaded
 |
| `picture` | The person's profile picture
Core |
| `rich_media_documents` | A list of rich media documents belonging to Pages that the user has advertiser permissions on
 |
| `videos` | Videos the person is tagged in or uploaded
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 80004 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#ads-management. |
| 613 | Calls to this api have exceeded the rate limit. |
| 210 | User not visible |
| 80006 | There have been too many messenger api calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 110 | Invalid user id |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can update a User by making a POST request to `/{user_id}`.### Parameters

| Parameter | Description |
| --- | --- |
| `emoji_color_pref`int64 | emoji color preference.
 |
| `firstname`string | This person's first name
 |
| `lastname`string | This person's last name
 |
| `local_news_megaphone_dismiss_status`enum {YES, NO} | Dismisses local news megaphone
 |
| `local_news_subscription_status`enum {STATUS\_ON, STATUS\_OFF} | Preference for setting local news notifications
 |
| `name`string | Used for test accounts only. Name for this account
 |
| `password`string | Used for test accounts only. Password for this account
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 240 | Desktop applications cannot call this function for other users |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 210 | User not visible |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
You can update a User by making a POST request to `/{custom_audience_id}/users`.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURLGraph API Explorer
```
POST /v19.0/<CUSTOM_AUDIENCE_ID>/users HTTP/1.1
Host: graph.facebook.com
payload=%7B%22schema%22%3A%5B%22EMAIL%22%2C%22LOOKALIKE_VALUE%22%5D%2C%22data%22%3A%5B%5B%229b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254%22%2C44.5%5D%2C%5B%228cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee%22%2C140%5D%2C%5B%224eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a%22%2C0%5D%2C%5B%2298df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56%22%2C0.9%5D%5D%7D
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->post(
    '/<CUSTOM_AUDIENCE_ID>/users',
    array (
      'payload' => '{"schema":["EMAIL","LOOKALIKE_VALUE"],"data":[["9b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254",44.5],["8cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee",140],["4eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a",0],["98df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56",0.9]]}',
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
```
```
/* make the API call */
FB.api(
    "/<CUSTOM_AUDIENCE_ID>/users",
    "POST",
    {
        "payload": "{\"schema\":[\"EMAIL\",\"LOOKALIKE_VALUE\"],\"data\":[[\"9b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254\",44.5],[\"8cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee\",140],[\"4eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a\",0],[\"98df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56\",0.9]]}"
    },
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```
```
Bundle params = new Bundle();
params.putString("payload", "{\"schema\":[\"EMAIL\",\"LOOKALIKE_VALUE\"],\"data\":[[\"9b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254\",44.5],[\"8cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee\",140],[\"4eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a\",0],[\"98df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56\",0.9]]}");
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/<CUSTOM_AUDIENCE_ID>/users",
    params,
    HttpMethod.POST,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```
```
NSDictionary *params = @{
  @"payload": @"{\"schema\":[\"EMAIL\",\"LOOKALIKE_VALUE\"],\"data\":[[\"9b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254\",44.5],[\"8cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee\",140],[\"4eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a\",0],[\"98df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56\",0.9]]}",
};
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/<CUSTOM_AUDIENCE_ID>/users"
                                      parameters:params
                                      HTTPMethod:@"POST"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
```
curl -X POST \
  -F 'payload={
       "schema": [
         "EMAIL",
         "LOOKALIKE_VALUE"
       ],
       "data": [
         [
           "9b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254",
           44.5
         ],
         [
           "8cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee",
           140
         ],
         [
           "4eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a",
           0
         ],
         [
           "98df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56",
           0.9
         ]
       ]
     }' \
  -F 'access_token=<ACCESS_TOKEN>' \
  https://graph.facebook.com/v19.0/<CUSTOM_AUDIENCE_ID>/users
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters

| Parameter | Description |
| --- | --- |
| `payload`Object | Payload representing users to add
 |
| `schema`string | `EMAIL_SHA256`, `PHONE_SHA256`, `MOBILE_ADVERTISER_ID`. One can also pass an array of multiple keys for multi-key match. Supported key types includes:  `EXTERN_ID``EMAIL``PHONE``GEN``DOBY``DOBM``DOBD``LN``FN``FI``CT``ST``ZIP``MADID``COUNTRY`The multi-key array is of the form `["EMAIL", "LN", "FN", "ZIP"]`
 |
| `is_raw`boolean | Is the key raw? If the keys are combinational keys like "LN\_FN\_ZIP", set this to `false`, otherwise set this to `true`. Default to false
 |
| `data`list<JSON array> | Array with users data. If the multi-key feature is used, a two-dimensional array of the form `[["<HASHED_EMAIL>", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"], ["", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"]]` should be passed.In case a key is unknown, it should be left blank.
 |
| `app_ids`list<int> | App ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by an App integration. e.g. `[1234,5678]`
 |
| `page_ids`list<Page ID> | Page ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by a Page webhook integration. e.g. `[1234,5678]`
 |
| `data_source`Object | Indicates by which method the custom audience was created, defined by the `type` and `subtype` of the `data_source`
 |
| `type`enum {UNKNOWN, FILE\_IMPORTED, EVENT\_BASED, SEED\_BASED, THIRD\_PARTY\_IMPORTED, COPY\_PASTE, CONTACT\_IMPORTER, HOUSEHOLD\_AUDIENCE} | Type of the custom audience
 |
| `sub_type`enum {ANYTHING, NOTHING, HASHES, USER\_IDS, HASHES\_OR\_USER\_IDS, MOBILE\_ADVERTISER\_IDS, EXTERNAL\_IDS, MULTI\_HASHES, TOKENS, EXTERNAL\_IDS\_MIX, HOUSEHOLD\_EXPANSION, SUBSCRIBER\_LIST, WEB\_PIXEL\_HITS, MOBILE\_APP\_EVENTS, MOBILE\_APP\_COMBINATION\_EVENTS, VIDEO\_EVENTS, WEB\_PIXEL\_COMBINATION\_EVENTS, PLATFORM, MULTI\_DATA\_EVENTS, IG\_BUSINESS\_EVENTS, STORE\_VISIT\_EVENTS, INSTANT\_ARTICLE\_EVENTS, FB\_EVENT\_SIGNALS, ENGAGEMENT\_EVENT\_USERS, FACEBOOK\_WIFI\_EVENTS, AR\_EXPERIENCE\_EVENTS, AR\_EFFECTS\_EVENTS, MESSENGER\_ONSITE\_SUBSCRIPTION, CUSTOM\_AUDIENCE\_USERS, PAGE\_FANS, CONVERSION\_PIXEL\_HITS, APP\_USERS, S\_EXPR, DYNAMIC\_RULE, CAMPAIGN\_CONVERSIONS, WEB\_PIXEL\_HITS\_CUSTOM\_AUDIENCE\_USERS, MOBILE\_APP\_CUSTOM\_AUDIENCE\_USERS, COMBINATION\_CUSTOM\_AUDIENCE\_USERS, VIDEO\_EVENT\_USERS, FB\_PIXEL\_HITS, IG\_PROMOTED\_POST, PLACE\_VISITS, OFFLINE\_EVENT\_USERS, EXPANDED\_AUDIENCE, SEED\_LIST, PARTNER\_CATEGORY\_USERS, PAGE\_SMART\_AUDIENCE, MULTICOUNTRY\_COMBINATION, PLATFORM\_USERS, MULTI\_EVENT\_SOURCE, SMART\_AUDIENCE, LOOKALIKE\_PLATFORM, SIGNAL\_SOURCE, MAIL\_CHIMP\_EMAIL\_HASHES, CONSTANT\_CONTACTS\_EMAIL\_HASHES, COPY\_PASTE\_EMAIL\_HASHES, CUSTOM\_DATA\_TARGETING, CONTACT\_IMPORTER, DATA\_FILE} | Subtype of the custom audience
 |
| `metadata`Object |  |
| `calculated_date`datetime |  |
| `schema_version`string |  |
| `session`Object | Information about the session. Sessions are used when you
 have a lot of users to upload. For example, if you have 1 million users
 to upload, you need to split them into at least 100 requests because
 each request can only take 10k users. Specify the session info so that
 you can track if the session has finished or not.
 |
| `session_id`int64 | Advertiser generated session identifier, used to track the session. Needs to be unique in the same ad account.
 |
| `estimated_num_total`int64 | Estimated total num of users to be uploaded in this session, used by Facebook systems to better process this session.
 |
| `batch_seq`int64 | A 1 based sequence number to identify the request in the session.
 |
| `last_batch_flag`boolean | `true` mean this request is the last request in this session. You must mark the last request otherwise Facebook doesn't know the session has ended
 |
### Return Type
This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`audience_id`: numeric string, `session_id`: numeric string, `num_received`: int32, `num_invalid_entries`: int32, `invalid_entry_samples`: Map {string: string}, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 2650 | Failed to update the custom audience |
| 190 | Invalid OAuth 2.0 Access Token |
| 105 | The number of parameters exceeded the maximum for this operation |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
Deleting
--------
Delete a test user
You can delete a User by making a DELETE request to `/{user_id}`.### Parameters
This endpoint doesn't have any parameters.### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 2903 | Cannot delete this test account |
| 100 | Invalid parameter |
| 2904 | Cannot delete the OG Test User |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |
You can dissociate a User from a Page by making a DELETE request to `/{page_id}/blocked`.### Parameters

| Parameter | Description |
| --- | --- |
| `asid`user/page ID | App Scoped User ID to unblock
 |
| `psid`UID | Page Scoped User ID to unblock
 |
| `uid`UID | Deprecated. Same as `user`
 |
| `user`UID | List of User or Page IDs to unblock. This or `uid` is required
 |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
You can dissociate a User from an AdAccount by making a DELETE request to `/act_{ad_account_id}/assigned_users`.### Parameters

| Parameter | Description |
| --- | --- |
| `user`UID | Business user id or system user id
Required |
### Return Type
 Struct {`success`: bool, }### Error Codes

| Error | Description |
| --- | --- |
| 3919 | There was an unexpected technical issue. Please try again. |
| 100 | Invalid parameter |
| 457 | The session has an invalid origin |
You can dissociate a User from a CustomAudience by making a DELETE request to `/{custom_audience_id}/users`.### Parameters

| Parameter | Description |
| --- | --- |
| `payload`Object | Payload representing users to delete
 |
| `schema`string | `EMAIL_SHA256`, `PHONE_SHA256`, `MOBILE_ADVERTISER_ID`. One can also pass an array of multiple keys for multi-key match. Supported key types includes:  `EXTERN_ID``EMAIL``PHONE``GEN``DOBY``DOBM``DOBD``LN``FN``FI``CT``ST``ZIP``MADID``COUNTRY`The multi-key array is of the form `["EMAIL", "LN", "FN", "ZIP"]`
 |
| `is_raw`boolean | Is the key raw? If the keys are combinational keys like "LN\_FN\_ZIP", set this to `false`, otherwise set this to `true`. Default to false
 |
| `data`list<JSON array> | Array with users data. If the multi-key feature is used, a two-dimensional array of the form `[["<HASHED_EMAIL>", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"], ["", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"]]` should be passed.In case a key is unknown, it should be left blank.
 |
| `app_ids`list<int> | App ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by an App integration. e.g. `[1234,5678]`
 |
| `page_ids`list<Page ID> | Page ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by a Page webhook integration. e.g. `[1234,5678]`
 |
| `data_source`Object | Indicates by which method the custom audience was created, defined by the `type` and `subtype` of the `data_source`
 |
| `type`enum {UNKNOWN, FILE\_IMPORTED, EVENT\_BASED, SEED\_BASED, THIRD\_PARTY\_IMPORTED, COPY\_PASTE, CONTACT\_IMPORTER, HOUSEHOLD\_AUDIENCE} | Type of the custom audience
 |
| `sub_type`enum {ANYTHING, NOTHING, HASHES, USER\_IDS, HASHES\_OR\_USER\_IDS, MOBILE\_ADVERTISER\_IDS, EXTERNAL\_IDS, MULTI\_HASHES, TOKENS, EXTERNAL\_IDS\_MIX, HOUSEHOLD\_EXPANSION, SUBSCRIBER\_LIST, WEB\_PIXEL\_HITS, MOBILE\_APP\_EVENTS, MOBILE\_APP\_COMBINATION\_EVENTS, VIDEO\_EVENTS, WEB\_PIXEL\_COMBINATION\_EVENTS, PLATFORM, MULTI\_DATA\_EVENTS, IG\_BUSINESS\_EVENTS, STORE\_VISIT\_EVENTS, INSTANT\_ARTICLE\_EVENTS, FB\_EVENT\_SIGNALS, ENGAGEMENT\_EVENT\_USERS, FACEBOOK\_WIFI\_EVENTS, AR\_EXPERIENCE\_EVENTS, AR\_EFFECTS\_EVENTS, MESSENGER\_ONSITE\_SUBSCRIPTION, CUSTOM\_AUDIENCE\_USERS, PAGE\_FANS, CONVERSION\_PIXEL\_HITS, APP\_USERS, S\_EXPR, DYNAMIC\_RULE, CAMPAIGN\_CONVERSIONS, WEB\_PIXEL\_HITS\_CUSTOM\_AUDIENCE\_USERS, MOBILE\_APP\_CUSTOM\_AUDIENCE\_USERS, COMBINATION\_CUSTOM\_AUDIENCE\_USERS, VIDEO\_EVENT\_USERS, FB\_PIXEL\_HITS, IG\_PROMOTED\_POST, PLACE\_VISITS, OFFLINE\_EVENT\_USERS, EXPANDED\_AUDIENCE, SEED\_LIST, PARTNER\_CATEGORY\_USERS, PAGE\_SMART\_AUDIENCE, MULTICOUNTRY\_COMBINATION, PLATFORM\_USERS, MULTI\_EVENT\_SOURCE, SMART\_AUDIENCE, LOOKALIKE\_PLATFORM, SIGNAL\_SOURCE, MAIL\_CHIMP\_EMAIL\_HASHES, CONSTANT\_CONTACTS\_EMAIL\_HASHES, COPY\_PASTE\_EMAIL\_HASHES, CUSTOM\_DATA\_TARGETING, CONTACT\_IMPORTER, DATA\_FILE} | Subtype of the custom audience
 |
| `metadata`Object |  |
| `calculated_date`datetime |  |
| `schema_version`string |  |
| `session`Object | Information about the session. Sessions are used when you
 have a lot of users to upload. For example, if you have 1 million users
 to upload, you need to split them into at least 100 requests because
 each request can only take 10k users. Specify the session info so that
 you can track if the session has finished or not.
 |
| `session_id`int64 | Advertiser generated session identifier, used to track the session. Needs to be unique in the same ad account.
 |
| `estimated_num_total`int64 | Estimated total num of users to be uploaded in this session, used by Facebook systems to better process this session.
 |
| `batch_seq`int64 | A 1 based sequence number to identify the request in the session.
 |
| `last_batch_flag`boolean | `true` mean this request is the last request in this session. You must mark the last request otherwise Facebook doesn't know the session has ended
 |
### Return Type
 Struct {`audience_id`: numeric string, `session_id`: numeric string, `num_received`: int32, `num_invalid_entries`: int32, `invalid_entry_samples`: Map {string: string}, }### Error Codes

| Error | Description |
| --- | --- |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#custom-audience. |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 2650 | Failed to update the custom audience |