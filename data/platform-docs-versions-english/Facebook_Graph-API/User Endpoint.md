User
====

[](#)

Represents a Facebook user.

[](#)

Reading
-------

Get fields and edges on a User.

### Requirements

| Type | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/guides/access-tokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | [public\_profile](https://developers.facebook.com/docs/permissions/reference/public_profile) |

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bperson-id%7D%2F&version=v18.0)

    GET /v18.0/{person-id}/ HTTP/1.1
    Host: graph.facebook.com

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

    /* make the API call */
    FB.api(
        "/{person-id}/",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

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

    curl -X GET -G \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v18.0/{person-id}/

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

  

### Default Public Profile Fields

The [`public_profile`](https://developers.facebook.com/docs/permissions/reference/public_profile) permission allows apps to read the following fields:

* `id`
* `first_name`
* `last_name`
* `middle_name`
* `name`
* `name_format`
* `picture`
* `short_name`

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | The app user's App-Scoped User ID. This ID is unique to the app and cannot be used by other apps.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `about`<br><br>string | _Returns no data as of April 4, 2018._ |
| `age_range`<br><br>[AgeRange](https://developers.facebook.com/docs/graph-api/reference/age-range/) | The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `birthday`<br><br>string | The person's birthday. This is a fixed format string, like `MM/DD/YYYY`. However, people can control who can see the year they were born separately from the month and day so this string can be only the year (YYYY) or the month + day (MM/DD)<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `education`<br><br>[list<EducationExperience>](https://developers.facebook.com/docs/graph-api/reference/education-experience/) | _Returns no data as of April 4, 2018._ |
| `email`<br><br>string | The User's primary email address listed on their profile. This field will not be returned if no valid email address is available.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `favorite_athletes`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Athletes the User likes. |
| `favorite_teams`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Sports teams the User likes. |
| `first_name`<br><br>string | The person's first name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `gender`<br><br>string | The gender selected by this person, `male` or `female`. If the gender is set to a custom value, this value will be based off of the selected pronoun; it will be omitted if the pronoun is neutral.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `hometown`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The person's hometown |
| `id_for_avatars`<br><br>numeric string | A profile based app scoped ID. It is used to query avatars |
| `inspirational_people`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | The person's inspirational people |
| `installed`<br><br>bool | Is the app making the request installed |
| `is_guest_user`<br><br>bool | if the current user is a guest user. should always return false. |
| `languages`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Facebook Pages representing the languages this person knows |
| `last_name`<br><br>string | The person's last name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `link`<br><br>string | A link to the person's Timeline. The link will only resolve if the person clicking the link is logged into Facebook and is a friend of the person whose profile is being viewed.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `local_news_megaphone_dismiss_status`<br><br>bool | Display megaphone for local news bookmark<br><br>Deprecated |
| `local_news_subscription_status`<br><br>bool | Daily local news notification<br><br>Deprecated |
| `locale`<br><br>string | The person's locale<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)Deprecated |
| `location`<br><br>[Page](https://developers.facebook.com/docs/graph-api/reference/page/) | The person's current location as entered by them on their profile. This field requires the `user_location` permission.<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `meeting_for`<br><br>list<string> | What the person is interested in meeting for |
| `middle_name`<br><br>string | The person's middle name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| `name`<br><br>string | The person's full name<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name_format`<br><br>string | The person's name formatted to correctly handle Chinese, Japanese, or Korean ordering |
| `political`<br><br>string | _Returns no data as of April 4, 2018._ |
| `quotes`<br><br>string | The person's favorite quotes |
| `relationship_status`<br><br>string | _Returns no data as of April 4, 2018._ |
| `shared_login_upgrade_required_by`[](#)<br><br>timestamp | The time that the shared login needs to be upgraded to Business Manager by |
| `significant_other`<br><br>[User](https://developers.facebook.com/docs/graph-api/reference/user/) | The person's significant other |
| `sports`<br><br>[list<Experience>](https://developers.facebook.com/docs/graph-api/reference/experience/) | Sports played by the person |
| `supports_donate_button_in_live_video`<br><br>bool | Whether the user can add a Donate Button to their Live Videos |
| `third_party_id`<br><br>string | A string containing an anonymous, unique identifier for the User, for use with third-parties. Deprecated for versions 3.0+. Apps using older versions of the API can get this field until January 8, 2019. Apps installed by the User on or after May 1st, 2018, cannot get this field.<br><br>Deprecated |
| `timezone`<br><br>float (min: -24) (max: 24) | The person's current timezone offset from UTC<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended)Deprecated |
| `token_for_business`<br><br>string | A token that is the same across a business's apps. Access to this token requires that the person be logged into your app or have a role on your app. This token will change if the business owning the app changes |
| `updated_time`<br><br>datetime | Updated time<br><br>Deprecated |
| `verified`<br><br>bool | Indicates whether the account has been verified. This is distinct from the `is_verified` field. Someone is considered verified if they take any of the following actions:<br><br>                                                                                                                                                                        * Register for mobile<br>                                                                                                                                                                        * Confirm their account via SMS<br>                                                                                                                                                                        * Enter a valid credit card<br><br>Deprecated |
| `video_upload_limits`<br><br>[VideoUploadLimits](https://developers.facebook.com/docs/graph-api/reference/video-upload-limits/) | Video upload limits |
| `website`<br><br>string | _Returns no data as of April 4, 2018._ |

### Edges

| Edge | Description |
| --- | --- |
| [`accounts`](https://developers.facebook.com/docs/graph-api/reference/user/accounts/) | Pages the User has a role on. |
| [`ad_studies`](https://developers.facebook.com/docs/graph-api/reference/user/ad_studies/) | Ad studies that this User's can view. |
| [`albums`](https://developers.facebook.com/docs/graph-api/reference/user/albums/) | The photo albums this person has created |
| [`apprequestformerrecipients`](https://developers.facebook.com/docs/graph-api/reference/user/apprequestformerrecipients/) | App requests |
| [`apprequests`](https://developers.facebook.com/docs/graph-api/reference/user/apprequests/) | This person's pending requests from an app<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| [`assigned_business_asset_groups`](https://developers.facebook.com/docs/graph-api/reference/user/assigned_business_asset_groups/) | Business asset groups that are assign to this business scoped user |
| [`assigned_pages`](https://developers.facebook.com/docs/graph-api/reference/user/assigned_pages/) | Pages that are assigned to this business scoped user |
| [`assigned_product_catalogs`](https://developers.facebook.com/docs/graph-api/reference/user/assigned_product_catalogs/) | Product catalogs that are assigned to this business scoped user |
| [`business_users`](https://developers.facebook.com/docs/graph-api/reference/user/business_users/) | Business users corresponding to the user |
| [`businesses`](https://developers.facebook.com/docs/graph-api/reference/user/businesses/) | Businesses associated with the user |
| [`conversations`](https://developers.facebook.com/docs/graph-api/reference/user/conversations/) | Facebook Messenger conversation |
| [`custom_labels`](https://developers.facebook.com/docs/graph-api/reference/user/custom_labels/)[](#) | custom\_labels |
| [`feed`](https://developers.facebook.com/docs/graph-api/reference/user/feed/) | The posts and links published by this person or others on their profile |
| [`ids_for_apps`](https://developers.facebook.com/docs/graph-api/reference/user/ids_for_apps/)[](#) | Businesses can claim ownership of multiple apps using Business Manager. This edge returns the list of IDs that this user has in any of those other apps |
| [`ids_for_business`](https://developers.facebook.com/docs/graph-api/reference/user/ids_for_business/)[](#) | Businesses can claim ownership of multiple apps using Business Manager. This edge returns the list of IDs that this user has in any of those other apps |
| [`ids_for_pages`](https://developers.facebook.com/docs/graph-api/reference/user/ids_for_pages/)[](#) | Businesses can claim ownership of apps and pages using Business Manager. This edge returns the list of IDs that this user has in any of the pages owned by this business |
| [`likes`](https://developers.facebook.com/docs/graph-api/reference/user/likes/) | All the Pages this person has liked |
| [`live_videos`](https://developers.facebook.com/docs/graph-api/reference/user/live_videos/) | Live videos from this person |
| [`music`](https://developers.facebook.com/docs/graph-api/reference/user/music/) | Music this person likes |
| [`payment.subscriptions`](https://developers.facebook.com/docs/graph-api/reference/user/payment.subscriptions/) | Payment subscriptions |
| [`permissions`](https://developers.facebook.com/docs/graph-api/reference/user/permissions/) | The permissions that the person has granted this app<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| [`photos`](https://developers.facebook.com/docs/graph-api/reference/user/photos/) | Photos the person is tagged in or has uploaded |
| [`picture`](https://developers.facebook.com/docs/graph-api/reference/user/picture/) | The person's profile picture<br><br>[Core](https://developers.facebook.com/docs/apps/versions/#coreextended) |
| [`rich_media_documents`](https://developers.facebook.com/docs/graph-api/reference/user/rich_media_documents/) | A list of rich media documents belonging to Pages that the user has advertiser permissions on |
| [`videos`](https://developers.facebook.com/docs/graph-api/reference/user/videos/) | Videos the person is tagged in or uploaded |

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

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can update a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a POST request to [`/{user_id}`](https://developers.facebook.com/docs/graph-api/reference/user/).

### Parameters

| Parameter | Description |
| --- | --- |
| `emoji_color_pref`<br><br>int64 | emoji color preference. |
| `firstname`<br><br>string | This person's first name |
| `lastname`<br><br>string | This person's last name |
| `local_news_megaphone_dismiss_status`<br><br>enum {YES, NO} | Dismisses local news megaphone |
| `local_news_subscription_status`<br><br>enum {STATUS\_ON, STATUS\_OFF} | Preference for setting local news notifications |
| `name`<br><br>string | Used for test accounts only. Name for this account |
| `password`<br><br>string | Used for test accounts only. Password for this account |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

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

You can update a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a POST request to [`/{custom_audience_id}/users`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=POST&path=%3CCUSTOM_AUDIENCE_ID%3E%2Fusers%3Fpayload%3D%257B%2522schema%2522%253A%255B%2522EMAIL%2522%252C%2522LOOKALIKE_VALUE%2522%255D%252C%2522data%2522%253A%255B%255B%25229b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254%2522%252C44.5%255D%252C%255B%25228cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee%2522%252C140%255D%252C%255B%25224eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a%2522%252C0%255D%252C%255B%252298df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56%2522%252C0.9%255D%255D%257D&version=v18.0)

    POST /v18.0/<CUSTOM_AUDIENCE_ID>/users HTTP/1.1
    Host: graph.facebook.com
    
    payload=%7B%22schema%22%3A%5B%22EMAIL%22%2C%22LOOKALIKE_VALUE%22%5D%2C%22data%22%3A%5B%5B%229b431636bd164765d63c573c346708846af4f68fe3701a77a3bdd7e7e5166254%22%2C44.5%5D%2C%5B%228cc62c145cd0c6dc444168eaeb1b61b351f9b1809a579cc9b4c9e9d7213a39ee%22%2C140%5D%2C%5B%224eaf70b1f7a797962b9d2a533f122c8039012b31e0a52b34a426729319cb792a%22%2C0%5D%2C%5B%2298df8d46f118f8bef552b0ec0a3d729466a912577830212a844b73960777ac56%22%2C0.9%5D%5D%7D

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
      https://graph.facebook.com/v18.0/<CUSTOM_AUDIENCE_ID>/users

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `payload`<br><br>Object | Payload representing users to add |
| `schema`<br><br>string | `EMAIL_SHA256`, `PHONE_SHA256`, `MOBILE_ADVERTISER_ID`. One can also pass an array of multiple keys for multi-key match. Supported key types includes:  <br>`EXTERN_ID`  <br>`EMAIL`  <br>`PHONE`  <br>`GEN`  <br>`DOBY`  <br>`DOBM`  <br>`DOBD`  <br>`LN`  <br>`FN`  <br>`FI`  <br>`CT`  <br>`ST`  <br>`ZIP`  <br>`MADID`  <br>`COUNTRY`  <br>The multi-key array is of the form `["EMAIL", "LN", "FN", "ZIP"]` |
| `is_raw`<br><br>boolean | Is the key raw? If the keys are combinational keys like "LN\_FN\_ZIP", set this to `false`, otherwise set this to `true`. Default to false |
| `data`<br><br>list<JSON array> | Array with users data. If the multi-key feature is used, a two-dimensional array of the form `[["<HASHED_EMAIL>", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"], ["", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"]]` should be passed.In case a key is unknown, it should be left blank. |
| `app_ids`<br><br>list<int> | App ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by an App integration. e.g. `[1234,5678]` |
| `page_ids`<br><br>list<Page ID> | Page ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by a Page webhook integration. e.g. `[1234,5678]` |
| `data_source`<br><br>Object | Indicates by which method the custom audience was created, defined by the `type` and `subtype` of the `data_source` |
| `type`<br><br>enum {UNKNOWN, FILE\_IMPORTED, EVENT\_BASED, SEED\_BASED, THIRD\_PARTY\_IMPORTED, COPY\_PASTE, CONTACT\_IMPORTER, HOUSEHOLD\_AUDIENCE} | Type of the custom audience |
| `sub_type`<br><br>enum {ANYTHING, NOTHING, HASHES, USER\_IDS, HASHES\_OR\_USER\_IDS, MOBILE\_ADVERTISER\_IDS, EXTERNAL\_IDS, MULTI\_HASHES, TOKENS, EXTERNAL\_IDS\_MIX, HOUSEHOLD\_EXPANSION, SUBSCRIBER\_LIST, WEB\_PIXEL\_HITS, MOBILE\_APP\_EVENTS, MOBILE\_APP\_COMBINATION\_EVENTS, VIDEO\_EVENTS, WEB\_PIXEL\_COMBINATION\_EVENTS, PLATFORM, MULTI\_DATA\_EVENTS, IG\_BUSINESS\_EVENTS, STORE\_VISIT\_EVENTS, INSTANT\_ARTICLE\_EVENTS, FB\_EVENT\_SIGNALS, ENGAGEMENT\_EVENT\_USERS, FACEBOOK\_WIFI\_EVENTS, AR\_EXPERIENCE\_EVENTS, AR\_EFFECTS\_EVENTS, MESSENGER\_ONSITE\_SUBSCRIPTION, CUSTOM\_AUDIENCE\_USERS, PAGE\_FANS, CONVERSION\_PIXEL\_HITS, APP\_USERS, S\_EXPR, DYNAMIC\_RULE, CAMPAIGN\_CONVERSIONS, WEB\_PIXEL\_HITS\_CUSTOM\_AUDIENCE\_USERS, MOBILE\_APP\_CUSTOM\_AUDIENCE\_USERS, COMBINATION\_CUSTOM\_AUDIENCE\_USERS, VIDEO\_EVENT\_USERS, FB\_PIXEL\_HITS, IG\_PROMOTED\_POST, PLACE\_VISITS, OFFLINE\_EVENT\_USERS, EXPANDED\_AUDIENCE, SEED\_LIST, PARTNER\_CATEGORY\_USERS, PAGE\_SMART\_AUDIENCE, MULTICOUNTRY\_COMBINATION, PLATFORM\_USERS, MULTI\_EVENT\_SOURCE, SMART\_AUDIENCE, LOOKALIKE\_PLATFORM, SIGNAL\_SOURCE, MAIL\_CHIMP\_EMAIL\_HASHES, CONSTANT\_CONTACTS\_EMAIL\_HASHES, COPY\_PASTE\_EMAIL\_HASHES, CUSTOM\_DATA\_TARGETING, CONTACT\_IMPORTER, DATA\_FILE} | Subtype of the custom audience |
| `metadata`<br><br>Object |     |
| `calculated_date`<br><br>datetime |     |
| `schema_version`<br><br>string |     |
| `session`<br><br>Object | Information about the session. Sessions are used when you have a lot of users to upload. For example, if you have 1 million users to upload, you need to split them into at least 100 requests because each request can only take 10k users. Specify the session info so that you can track if the session has finished or not. |
| `session_id`<br><br>int64 | Advertiser generated session identifier, used to track the session. Needs to be unique in the same ad account. |
| `estimated_num_total`<br><br>int64 | Estimated total num of users to be uploaded in this session, used by Facebook systems to better process this session. |
| `batch_seq`<br><br>int64 | A 1 based sequence number to identify the request in the session. |
| `last_batch_flag`<br><br>boolean | `true` mean this request is the last request in this session. You must mark the last request otherwise Facebook doesn't know the session has ended |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`audience_id`: numeric string,

`session_id`: numeric string,

`num_received`: int32,

`num_invalid_entries`: int32,

`invalid_entry_samples`: Map {

string: string

},

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 2650 | Failed to update the custom audience |
| 190 | Invalid OAuth 2.0 Access Token |
| 105 | The number of parameters exceeded the maximum for this operation |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[](#)

Deleting
--------

Delete a test user

You can delete a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}`](https://developers.facebook.com/docs/graph-api/reference/user/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 2903 | Cannot delete this test account |
| 100 | Invalid parameter |
| 2904 | Cannot delete the OG Test User |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |

You can dissociate a [User](https://developers.facebook.com/docs/graph-api/reference/user/) from a [Page](https://developers.facebook.com/docs/graph-api/reference/page/) by making a DELETE request to [`/{page_id}/blocked`](https://developers.facebook.com/docs/graph-api/reference/page/blocked/).

### Parameters

| Parameter | Description |
| --- | --- |
| `asid`<br><br>user/page ID | App Scoped User ID to unblock |
| `psid`<br><br>UID | Page Scoped User ID to unblock |
| `uid`<br><br>UID | Deprecated. Same as `user` |
| `user`<br><br>UID | List of User or Page IDs to unblock. This or `uid` is required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

You can dissociate a [User](https://developers.facebook.com/docs/graph-api/reference/user/) from an [AdAccount](https://developers.facebook.com/docs/marketing-api/reference/ad-account/) by making a DELETE request to [`/act_{ad_account_id}/assigned_users`](https://developers.facebook.com/docs/marketing-api/reference/ad-account/assigned_users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `user`<br><br>UID | Business user id or system user id<br><br>Required |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 3919 | There was an unexpected technical issue. Please try again. |
| 100 | Invalid parameter |
| 457 | The session has an invalid origin |

You can dissociate a [User](https://developers.facebook.com/docs/graph-api/reference/user/) from a [CustomAudience](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/) by making a DELETE request to [`/{custom_audience_id}/users`](https://developers.facebook.com/docs/marketing-api/reference/custom-audience/users/).

### Parameters

| Parameter | Description |
| --- | --- |
| `payload`<br><br>Object | Payload representing users to delete |
| `schema`<br><br>string | `EMAIL_SHA256`, `PHONE_SHA256`, `MOBILE_ADVERTISER_ID`. One can also pass an array of multiple keys for multi-key match. Supported key types includes:  <br>`EXTERN_ID`  <br>`EMAIL`  <br>`PHONE`  <br>`GEN`  <br>`DOBY`  <br>`DOBM`  <br>`DOBD`  <br>`LN`  <br>`FN`  <br>`FI`  <br>`CT`  <br>`ST`  <br>`ZIP`  <br>`MADID`  <br>`COUNTRY`  <br>The multi-key array is of the form `["EMAIL", "LN", "FN", "ZIP"]` |
| `is_raw`<br><br>boolean | Is the key raw? If the keys are combinational keys like "LN\_FN\_ZIP", set this to `false`, otherwise set this to `true`. Default to false |
| `data`<br><br>list<JSON array> | Array with users data. If the multi-key feature is used, a two-dimensional array of the form `[["<HASHED_EMAIL>", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"], ["", "<HASHED_FN>", "<HASHED_LN>", "<HASHED_ZIP>"]]` should be passed.In case a key is unknown, it should be left blank. |
| `app_ids`<br><br>list<int> | App ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by an App integration. e.g. `[1234,5678]` |
| `page_ids`<br><br>list<Page ID> | Page ids used by the users being uploaded. This field is required when `schema` is a Facebook UID and the IDs were collected by a Page webhook integration. e.g. `[1234,5678]` |
| `data_source`<br><br>Object | Indicates by which method the custom audience was created, defined by the `type` and `subtype` of the `data_source` |
| `type`<br><br>enum {UNKNOWN, FILE\_IMPORTED, EVENT\_BASED, SEED\_BASED, THIRD\_PARTY\_IMPORTED, COPY\_PASTE, CONTACT\_IMPORTER, HOUSEHOLD\_AUDIENCE} | Type of the custom audience |
| `sub_type`<br><br>enum {ANYTHING, NOTHING, HASHES, USER\_IDS, HASHES\_OR\_USER\_IDS, MOBILE\_ADVERTISER\_IDS, EXTERNAL\_IDS, MULTI\_HASHES, TOKENS, EXTERNAL\_IDS\_MIX, HOUSEHOLD\_EXPANSION, SUBSCRIBER\_LIST, WEB\_PIXEL\_HITS, MOBILE\_APP\_EVENTS, MOBILE\_APP\_COMBINATION\_EVENTS, VIDEO\_EVENTS, WEB\_PIXEL\_COMBINATION\_EVENTS, PLATFORM, MULTI\_DATA\_EVENTS, IG\_BUSINESS\_EVENTS, STORE\_VISIT\_EVENTS, INSTANT\_ARTICLE\_EVENTS, FB\_EVENT\_SIGNALS, ENGAGEMENT\_EVENT\_USERS, FACEBOOK\_WIFI\_EVENTS, AR\_EXPERIENCE\_EVENTS, AR\_EFFECTS\_EVENTS, MESSENGER\_ONSITE\_SUBSCRIPTION, CUSTOM\_AUDIENCE\_USERS, PAGE\_FANS, CONVERSION\_PIXEL\_HITS, APP\_USERS, S\_EXPR, DYNAMIC\_RULE, CAMPAIGN\_CONVERSIONS, WEB\_PIXEL\_HITS\_CUSTOM\_AUDIENCE\_USERS, MOBILE\_APP\_CUSTOM\_AUDIENCE\_USERS, COMBINATION\_CUSTOM\_AUDIENCE\_USERS, VIDEO\_EVENT\_USERS, FB\_PIXEL\_HITS, IG\_PROMOTED\_POST, PLACE\_VISITS, OFFLINE\_EVENT\_USERS, EXPANDED\_AUDIENCE, SEED\_LIST, PARTNER\_CATEGORY\_USERS, PAGE\_SMART\_AUDIENCE, MULTICOUNTRY\_COMBINATION, PLATFORM\_USERS, MULTI\_EVENT\_SOURCE, SMART\_AUDIENCE, LOOKALIKE\_PLATFORM, SIGNAL\_SOURCE, MAIL\_CHIMP\_EMAIL\_HASHES, CONSTANT\_CONTACTS\_EMAIL\_HASHES, COPY\_PASTE\_EMAIL\_HASHES, CUSTOM\_DATA\_TARGETING, CONTACT\_IMPORTER, DATA\_FILE} | Subtype of the custom audience |
| `metadata`<br><br>Object |     |
| `calculated_date`<br><br>datetime |     |
| `schema_version`<br><br>string |     |
| `session`<br><br>Object | Information about the session. Sessions are used when you have a lot of users to upload. For example, if you have 1 million users to upload, you need to split them into at least 100 requests because each request can only take 10k users. Specify the session info so that you can track if the session has finished or not. |
| `session_id`<br><br>int64 | Advertiser generated session identifier, used to track the session. Needs to be unique in the same ad account. |
| `estimated_num_total`<br><br>int64 | Estimated total num of users to be uploaded in this session, used by Facebook systems to better process this session. |
| `batch_seq`<br><br>int64 | A 1 based sequence number to identify the request in the session. |
| `last_batch_flag`<br><br>boolean | `true` mean this request is the last request in this session. You must mark the last request otherwise Facebook doesn't know the session has ended |

### Return Type

Struct {

`audience_id`: numeric string,

`session_id`: numeric string,

`num_received`: int32,

`num_invalid_entries`: int32,

`invalid_entry_samples`: Map {

string: string

},

}

### Error Codes

| Error | Description |
| --- | --- |
| 80003 | There have been too many calls to this ad-account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting#custom-audience. |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 2650 | Failed to update the custom audience |

[](#)

User Accounts
=============

[](#)

The Facebook Pages that a person owns or is able to perform tasks on.

[](#)

Reading
-------

Pages the User has a role on

### Permissions

A Page access token for a User with a role (other than Live Contributor) on the Page and the following permissions:

* The `pages_show_list` permission
    
* To access accounts using a `business_id` or for a user who owns any business Pages, the app must be approved for the [`business_management` permission](https://developers.facebook.com/docs/apps/review/login-permissions#business-management).
    

**Note:** In order for a Page to be returned, the User must also grant the app running the query the `pages_show_list` permissions for that Page.

### Limitations

* **It does not return pages that you are connected with through a business. To retrieve pages that you are connected with via businesses, the `business_management` permission is required**
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKcURL[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Faccounts&version=v18.0)

    GET /v18.0/{user-id}/accounts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/accounts',
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
        "/{user-id}/accounts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/accounts",
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
                                   initWithGraphPath:@"/{user-id}/accounts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

    curl -X GET -G \
      -d 'access_token=<ACCESS_TOKEN>' \
      https://graph.facebook.com/v18.0/{user-id}/accounts

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `is_place`[](#)<br><br>boolean | If specified,filter pages based on whetherthey are places or not |
| `is_promotable`[](#)<br><br>boolean | If specified, filter pages based on whether they can be promoted or not |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `tasks`<br><br>list<enum> | The User's tasks assigned to the Page.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 80002 | There have been too many calls to this Instagram account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 110 | Invalid user id |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 210 | User not visible |

[](#)

Creating
--------

This API lets you create Facebook pages.

### Permissions

* A User access token with `pages_manage_metadata` and `pages_show_list` permissions.
    
* The `category_enum` parameter with a Page Category.
    
* Other requirements vary depending on the type of page you are creating but may require the following parameters: `name`, `about`, `picture`, and `cover_photo`.
    

**Note:** When setting the locale, at least one, `city_id`, `location`, or `coordinates`, is required. Caveats:

* `city_id` and `location` can not be used together
    
* `city_id` and `coordinates` can be used together however the coordinates must be within the city selected
    
* `location` and `coordinates` can be used together however the coordinates must be within the location selected
    

### Limitations

* You can only create a Page as a [test user](https://developers.facebook.com/docs/apps/test-users) or if your app has been allowlisted by your Facebook representative.
    

* * *

You can make a POST request to `accounts` edge from the following paths:

* [`/{user_id}/accounts`](https://developers.facebook.com/docs/graph-api/reference/user/accounts/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `about`<br><br>UTF-8 encoded string | Short description |
| `address`<br><br>UTF-8 encoded string | Address |
| `category_enum`<br><br>string | Page category (enum). See [Pages Categories API](https://developers.facebook.com/docs/graph-api/reference/page-category/) docs. |
| `category_list`<br><br>list<numeric string> | List of categories |
| `city_id`<br><br>city id | City ID |
| `coordinates`<br><br>JSON-encoded coordinate list | Coordinates |
| `cover_photo`<br><br>Object | Cover photo |
| `url`<br><br>URL | Required |
| `offset_y`<br><br>integer | Default value: `50` |
| `offset_x`<br><br>integer | Default value: `50` |
| `focus_y`<br><br>float |     |
| `focus_x`<br><br>float |     |
| `zoom_scale_x`<br><br>float |     |
| `zoom_scale_y`<br><br>float |     |
| `no_feed_story`<br><br>boolean | Default value: `false` |
| `no_notification`<br><br>boolean | Default value: `false` |
| `description`<br><br>UTF-8 encoded string | Description |
| `ignore_coordinate_warnings`<br><br>boolean | If ignore warnings generated in coordination validation (bool) |
| `location`<br><br>Object | This defines the location for this page. This is required if `location_page_id` is not specified, or if the Page referenced by the `location_page_id` doesn't have a valid value for the field. The dictionary must include the keys either `city_id` or all of `city`, `state`, and `country` (but `state` is optional if the address is not in the U.S.). |
| `city`<br><br>string |     |
| `state`<br><br>string |     |
| `country`<br><br>string |     |
| `name`<br><br>UTF-8 encoded string | Page name<br><br>Required |
| `phone`<br><br>UTF-8 encoded string | Phone |
| `picture`<br><br>URL | Profile picture |
| `website`<br><br>URL | Website |
| `zip`<br><br>string | Zipcode |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 152 | Invalid page type |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 3950 | The system creation is throttled. |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

User Ad Studies
===============

[](#)

Reading
-------

UserAdStudies

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fad_studies&version=v18.0)

    GET /v18.0/{user-id}/ad_studies HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/ad_studies',
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
        "/{user-id}/ad_studies",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/ad_studies",
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
                                   initWithGraphPath:@"/{user-id}/ad_studies"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [AdStudy](https://developers.facebook.com/docs/marketing-api/reference/ad-study/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of lift studies for this person |

### Error Codes

| Error | Description |
| --- | --- |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can make a POST request to `ad_studies` edge from the following paths:

* [`/{user_id}/ad_studies`](https://developers.facebook.com/docs/graph-api/reference/user/ad_studies/)

When posting to this edge, an [AdStudy](https://developers.facebook.com/docs/marketing-api/reference/ad-study/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `cells`<br><br>list<Object> | A shape to describe the cells of the study |
| `description`<br><br>string |     |
| `id`<br><br>int64 |     |
| `name`<br><br>string |     |
| `creation_template`<br><br>enum {AUTOMATIC\_PLACEMENTS, BRAND\_AWARENESS, FACEBOOK, FACEBOOK\_AUDIENCE\_NETWORK, FACEBOOK\_INSTAGRAM, FACEBOOK\_NEWS\_FEED, FACEBOOK\_NEWS\_FEED\_IN\_STREAM\_VIDEO, IN\_STREAM\_VIDEO, INSTAGRAM, MOBILE\_OPTIMIZED\_VIDEO, PAGE\_POST\_ENGAGEMENT, REACH, TV\_COMMERCIAL, TV\_FACEBOOK, VIDEO\_VIEW\_OPTIMIZATION, LOW\_FREQUENCY, MEDIUM\_FREQUENCY, HIGH\_FREQUENCY} |     |
| `adaccounts`<br><br>list<int64> |     |
| `adsets`<br><br>list<numeric string or integer> |     |
| `campaigns`<br><br>list<numeric string or integer> |     |
| `control_percentage`<br><br>float with at most two digits after decimal point |     |
| `treatment_percentage`<br><br>float with at most two digits after decimal point |     |
| `client_business`<br><br>numeric string or integer | Business associated with study |
| `confidence_level`<br><br>float | Confidence level used in power calculation and final report |
| `cooldown_start_time`<br><br>integer | The beginning of the pre measurement cooldown period. This period ends when the study period starts. |
| `description`<br><br>string | A brief description about the purpose of the study. |
| `end_time`<br><br>integer | The time when the study period ends. |
| `name`<br><br>string | The name of the study. |
| `objectives`<br><br>list<Object> | A vector of objects describing the objectives assigned to this study |
| `id`<br><br>numeric string or integer |     |
| `is_primary`<br><br>boolean |     |
| `name`<br><br>string |     |
| `type`<br><br>enum {SALES, NONSALES, MAE, TELCO, FTL, MAI, PARTNER, BRANDLIFT, BRAND, MPC\_CONVERSION, CONVERSIONS} |     |
| `offsite_datasets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `adspixels`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `customconversions`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `applications`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `offline_conversion_data_sets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `product_sets`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `product_catalogs`<br><br>list<JSON or object-like arrays> |     |
| `id`<br><br>numeric string or integer | Required |
| `event_names`<br><br>list<string> |     |
| `observation_end_time`<br><br>integer | The end of the observation period for this study, this period starts when the study period ends. |
| `start_time`<br><br>integer | The time when the study period starts. |
| `type`<br><br>enum {LIFT, SPLIT\_TEST, CONTINUOUS\_LIFT\_CONFIG, GEO\_LIFT} | The type of ad study, either SPLIT\_TEST or LIFT. |
| `viewers`<br><br>list<int> | The list of people who this study has been shared with. |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`cell_ids`: List \[

numeric string

\],

`objective_ids`: List \[

numeric string

\],

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

User Albums
===========

[](#)

Albums for a Facebook User.

[](#)

Reading
-------

UserAlbums

### Permissions

* A user access token is required with the `user_photos` permission to view a person's albums.
    

This API can only be used to read albums of the person who created the access token. It can't be used to read the albums of friends or non-friends.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Falbums&version=v18.0)

    GET /v18.0/{user-id}/albums HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/albums',
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
        "/{user-id}/albums",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/albums",
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
                                   initWithGraphPath:@"/{user-id}/albums"
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

A list of [Album](https://developers.facebook.com/docs/graph-api/reference/album/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |
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

User Apprequestformerrecipients
===============================

[](#)

Reading
-------

UserAppRequestFormerRecipients

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fapprequestformerrecipients&version=v18.0)

    GET /v18.0/{user-id}/apprequestformerrecipients HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/apprequestformerrecipients',
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
        "/{user-id}/apprequestformerrecipients",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/apprequestformerrecipients",
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
                                   initWithGraphPath:@"/{user-id}/apprequestformerrecipients"
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

A list of [AppRequestFormerRecipient](https://developers.facebook.com/docs/graph-api/reference/app-request-former-recipient/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 110 | Invalid user id |

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

User Apprequests
================

[](#)

Reading
-------

UserAppRequests

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fapprequests&version=v18.0)

    GET /v18.0/{user-id}/apprequests HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/apprequests',
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
        "/{user-id}/apprequests",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/apprequests",
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
                                   initWithGraphPath:@"/{user-id}/apprequests"
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

A list of [AppRequest](https://developers.facebook.com/docs/graph-api/reference/app-request/) nodes.

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

When you create an apprequest, use {user-id} to indicate the recipient.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=post&path=%7Buser-id%7D%2Fapprequests)

    post /{user-id}/apprequests HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{user-id}/apprequests',
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
        "/{user-id}/apprequests",
        "post",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/apprequests",
        null,
        HttpMethod.post,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{user-id}/apprequests"
                                          parameters:params
                                          HTTPMethod:@"post"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

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

User Assigned Business Asset Groups
===================================

[](#)

Reading
-------

Get list of business asset groups for user

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fassigned_business_asset_groups&version=v18.0)

    GET /v18.0/{user-id}/assigned_business_asset_groups HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/assigned_business_asset_groups',
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
        "/{user-id}/assigned_business_asset_groups",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/assigned_business_asset_groups",
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
                                   initWithGraphPath:@"/{user-id}/assigned_business_asset_groups"
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
| `contained_asset_id`<br><br>numeric string or integer | contained\_asset\_id |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of BusinessAssetGroup nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `adaccount_tasks`<br><br>list<string> | Permission tasks for ad accounts contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `offline_conversion_data_set_tasks`<br><br>list<string> | Permission tasks for offline conversion datasets contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `page_tasks`<br><br>list<string> | Permission tasks fo pages contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `pixel_tasks`<br><br>list<string> | Permission tasks for ads pixels contained in business asset group.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total count of business asset groups<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

User Assigned Pages
===================

[](#)

Reading
-------

Pages that are assigned to this business scoped user.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fassigned_pages&version=v18.0)

    GET /v18.0/{user-id}/assigned_pages HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/assigned_pages',
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
        "/{user-id}/assigned_pages",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/assigned_pages",
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
                                   initWithGraphPath:@"/{user-id}/assigned_pages"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `permitted_tasks`<br><br>list<string> | Tasks that are assignable on this object |
| `tasks`<br><br>list<string> | All unpacked roles/tasks of this particular user on this object<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

User Assigned Product Catalogs
==============================

[](#)

Reading
-------

Product catalogs that is assigned to this business scoped user.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fassigned_product_catalogs&version=v18.0)

    GET /v18.0/{user-id}/assigned_product_catalogs HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/assigned_product_catalogs',
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
        "/{user-id}/assigned_product_catalogs",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/assigned_product_catalogs",
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
                                   initWithGraphPath:@"/{user-id}/assigned_product_catalogs"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [ProductCatalog](https://developers.facebook.com/docs/marketing-api/reference/product-catalog/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `access_type`<br><br>string | Checks if business has owner or agency access on the asset |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

User Business Users
===================

[](#)

Represents a collection of Business Manager accounts associated with a User.

[](#)

Reading
-------

Get a list of Business Manager accounts associated with the User.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fbusiness_users&version=v18.0)

    GET /v18.0/{user-id}/business_users HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/business_users',
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
        "/{user-id}/business_users",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/business_users",
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
                                   initWithGraphPath:@"/{user-id}/business_users"
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
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [BusinessUser](https://developers.facebook.com/docs/marketing-api/reference/business-user/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | total\_count |

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

User Businesses
===============

[](#)

Reading
-------

UserBusinesses

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fbusinesses&version=v18.0)

    GET /v18.0/{user-id}/businesses HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/businesses',
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
        "/{user-id}/businesses",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/businesses",
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
                                   initWithGraphPath:@"/{user-id}/businesses"
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

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `permitted_roles`<br><br>list<string> | Roles the user has on the business |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 110 | Invalid user id |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |

[](#)

Creating
--------

You can make a POST request to `businesses` edge from the following paths:

* [`/{user_id}/businesses`](https://developers.facebook.com/docs/graph-api/reference/user/businesses/)

When posting to this edge, a [Business](https://developers.facebook.com/docs/marketing-api/reference/business/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `child_business_external_id`<br><br>string | child\_business\_external\_id |
| `email`<br><br>string | The business email of the business admin |
| `name`<br><br>string | Username<br><br>Required |
| `primary_page`<br><br>page ID | Primary Page ID |
| `sales_rep_email`<br><br>string | Sales Rep email address |
| `survey_business_type`<br><br>enum {AGENCY, ADVERTISER, APP\_DEVELOPER, PUBLISHER} | Business Type |
| `survey_num_assets`<br><br>int64 | Number of Assets in the business |
| `survey_num_people`<br><br>int64 | Number of People that will work on the business |
| `timezone_id`<br><br>int64 | Timezone ID |
| `vertical`<br><br>enum {NOT\_SET, ADVERTISING, AUTOMOTIVE, CONSUMER\_PACKAGED\_GOODS, ECOMMERCE, EDUCATION, ENERGY\_AND\_UTILITIES, ENTERTAINMENT\_AND\_MEDIA, FINANCIAL\_SERVICES, GAMING, GOVERNMENT\_AND\_POLITICS, MARKETING, ORGANIZATIONS\_AND\_ASSOCIATIONS, PROFESSIONAL\_SERVICES, RETAIL, TECHNOLOGY, TELECOM, TRAVEL, NON\_PROFIT, RESTAURANT, HEALTH, LUXURY, OTHER} | Vertical ID<br><br>Required |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 42000 | This Page can't be added because it's already linked to an Instagram business profile. To add this Page to Business Manager, go to Instagram and convert to a personal account or change the Page linked to your business profile. |
| 3918 | The Facebook Page you've tried to add is already owned by another Business Manager. You can still request access to this Page, but your request will need to be approved by the Business Manager that owns it. |
| 3974 | The name you chose for this Business Manager is not valid. Try a different name. |
| 3947 | You are trying to create a Business Manager with the same name as one you are already a part of. Please pick a different name. |
| 3913 | It doesn't look like you have permission to create a new Business Manager. |
| 3912 | There was a technical issue and the changes you made to your Business Manager weren't saved. Please try again. |
| 3973 | The name you chose for this Business Manager is not valid. Please choose another. |
| 3998 | You must be an admin of the primary Page to create a business using that page. |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can dissociate a [Business](https://developers.facebook.com/docs/marketing-api/reference/business/) from a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}/businesses`](https://developers.facebook.com/docs/graph-api/reference/user/businesses/).

### Parameters

| Parameter | Description |
| --- | --- |
| `business`<br><br>numeric string or integer | Business ID |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 3914 | It looks like you're trying to remove the last admin from this Business Manager. At least one admin is required in Business Manager. |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

User Custom Labels
==================

[](#)

Reading
-------

custom\_labels

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fcustom_labels&version=v18.0)

    GET /v18.0/{user-id}/custom_labels HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/custom_labels',
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
        "/{user-id}/custom_labels",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/custom_labels",
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
                                   initWithGraphPath:@"/{user-id}/custom_labels"
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

A list of PageUserMessageThreadLabel nodes.

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

User Feed
=========

[](#)

Reading
-------

The posts and links published by this person or others on their profile

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Ffeed&version=v18.0)

    GET /v18.0/{user-id}/feed HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/feed',
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
        "/{user-id}/feed",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/feed",
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
                                   initWithGraphPath:@"/{user-id}/feed"
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

A list of [Post](https://developers.facebook.com/docs/graph-api/reference/post/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
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

User Ids For Apps
=================

[](#)

Reading
-------

The IDs that apps owned by the business know the user as

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fids_for_apps&version=v18.0)

    GET /v18.0/{user-id}/ids_for_apps HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/ids_for_apps',
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
        "/{user-id}/ids_for_apps",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/ids_for_apps",
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
                                   initWithGraphPath:@"/{user-id}/ids_for_apps"
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
| `app`<br><br>int | A specific app to fetch the User's ID for |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [UserIDForApp](https://developers.facebook.com/docs/graph-api/reference/user-id-for-app/) nodes.

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

User Ids For Business
=====================

[](#)

Reading
-------

The IDs that apps owned by the business know the user as

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fids_for_business&version=v18.0)

    GET /v18.0/{user-id}/ids_for_business HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/ids_for_business',
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
        "/{user-id}/ids_for_business",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/ids_for_business",
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
                                   initWithGraphPath:@"/{user-id}/ids_for_business"
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
| `app`<br><br>int | A specific app to fetch the User's ID for |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [UserIDForApp](https://developers.facebook.com/docs/graph-api/reference/user-id-for-app/) nodes.

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

User Ids For Pages
==================

[](#)

Reading
-------

The IDs that pages owned by the business know the viewer as

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fids_for_pages&version=v18.0)

    GET /v18.0/{user-id}/ids_for_pages HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/ids_for_pages',
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
        "/{user-id}/ids_for_pages",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/ids_for_pages",
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
                                   initWithGraphPath:@"/{user-id}/ids_for_pages"
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
| `page`<br><br>Page ID | A specific page to fetch the User's ID for |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of UserIDForPage nodes.

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

User Likes
==========

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Flikes&version=v18.0)

    GET /v18.0/{user-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/likes',
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
        "/{user-id}/likes",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/likes",
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
                                   initWithGraphPath:@"/{user-id}/likes"
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
| `target_id`<br><br>numeric string | Target node |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `created_time`<br><br>datetime | Time the object liked the page<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |

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

User Live Videos
================

[](#)

Represents a collection of [LiveVideos](https://developers.facebook.com/docs/graph-api/reference/live-video/) on a [User](https://developers.facebook.com/docs/graph-api/reference/user/).

[](#)

Reading
-------

Get a collection of [LiveVideos](https://developers.facebook.com/docs/graph-api/reference/live-video/) on a [User](https://developers.facebook.com/docs/graph-api/reference/user/).

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Flive_videos&version=v18.0)

    GET /v18.0/{user-id}/live_videos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/live_videos',
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
        "/{user-id}/live_videos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/live_videos",
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
                                   initWithGraphPath:@"/{user-id}/live_videos"
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
| `broadcast_status`<br><br>list<enum {UNPUBLISHED, LIVE, LIVE\_STOPPED, PROCESSING, VOD, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_EXPIRED, SCHEDULED\_CANCELED}> | Allows you to specify what kind of live videos return. No value returns all status types |
| `source`[](#)<br><br>enum{target, owner} | Default value: `target`<br><br>Specifies what the source of the videos should be. 'target' gets videos broadcasted onto the user's timeline, 'owner' gets videos made by the user |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 190 | Invalid OAuth 2.0 Access Token |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can make a POST request to `live_videos` edge from the following paths:

* [`/{user_id}/live_videos`](https://developers.facebook.com/docs/graph-api/reference/user/live_videos/)

When posting to this edge, a [LiveVideo](https://developers.facebook.com/docs/graph-api/reference/live-video/) will be created.

Scheduling is deprecated. Calls to the `POST /ID/live-video` endpoint with the `planned_start_time` parameter will return an error. To schedule a live video, use the `event_params` parameter.

[](#)

### Parameters

| Parameter | Description |
| --- | --- |
| `content_tags`<br><br>list<numeric string> | Tags that describe the contents of the video. Use search endpoint with `type=adinterest` to get possible IDs.<br><br>                        Example:<br>                        ~~~~<br>                        /search?type=adinterest&q=couscous<br>                        ~~~~ |
| `description`<br><br>UTF-8 string | The description of the live video.<br><br>Supports Emoji |
| `donate_button_charity_id`<br><br>numeric string or integer | Specifies the ID of the charity for which a donate button will be added to the live video. |
| `enable_backup_ingest`<br><br>boolean | Set this to true to enable a backup ingest url. stop\_on\_delete\_stream defaults to false when set |
| `encoding_settings`<br><br>string | Identifier of the encoding settings group the broadcaster is using for this stream. This parameter is currently only in use for live-360 broadcasts. The value to be passed to this parameter is the value of the `identifier` key of the encoding settings preset. Encoding presets can be found by querying the `/broadcaster_encoding_settings` Graph API endpoint (`GET` query). |
| `event_params`<br><br>Live Video Event Parameter | Parameters specific to Live Online Event broadcast. If `start_time` (unix timecode) is set, LOE's start time will be updated. Also, `cover` (url) uploads an image to use as the cover photo for the event.<br><br>Example: { start\_time: 1641013200, cover: 'https://your.url/image.jpg', } |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `is_spherical`<br><br>boolean | Flag that denotes the broadcast is a 360 live broadcast. |
| `original_fov`<br><br>int64 | Original field of view of the camera |
| `privacy`<br><br>Privacy Parameter | Privacy for this live video. |
| `projection`<br><br>enum {EQUIRECTANGULAR, CUBEMAP, HALF\_EQUIRECTANGULAR} | Flag that denotes expected projection for 360 live streams. The default value is EQUIRECTANGULAR. |
| `published`<br><br>boolean | Set this to false to preview the stream before going live.<br><br>                        Deprecated. Prefer setting the status instead. |
| `schedule_custom_profile_image`<br><br>image | Custom image that will appear in the scheduled live story and lobby. |
| `spatial_audio_format`<br><br>enum {ambiX\_4} | Denotes the format of the spatial audio stream. When unspecified audio is presumed to be mono or stereo. |
| `status`<br><br>enum {UNPUBLISHED, LIVE\_NOW, SCHEDULED\_UNPUBLISHED, SCHEDULED\_LIVE, SCHEDULED\_CANCELED} | The status of the broadcast. A `LIVE_NOW` broadcast is currently live and visible to users. An `UNPUBLISHED` broadcast is in preparation; it's not visible to other users, and it may be automatically deleted after several hours in this state. (Consider using the `SCHEDULED` states to create a planned, future broadcast.) |
| `stereoscopic_mode`<br><br>enum {MONO, LEFT\_RIGHT, TOP\_BOTTOM} | Set this parameter to the stereoscopic mode for this video. |
| `stop_on_delete_stream`<br><br>boolean | Set this to true if stream should be stopped when deleteStream RTMP command received. |
| `title`<br><br>UTF-8 string | The title of the live video. Maximum 254 characters.<br><br>Supports Emoji |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`stream_url`: string,

`secure_stream_url`: string,

`stream_secondary_urls`: List \[

string

\],

`secure_stream_secondary_urls`: List \[

string

\],

`dash_ingest_url`: string,

`dash_ingest_secondary_urls`: List \[

string

\],

`event_id`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 1005 | Fail to upload cover photo. |
| 1000 | Invalid time for an event. |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

User Music
==========

[](#)

Music this person likes.

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fmusic&version=v18.0)

    GET /v18.0/{user-id}/music HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/music',
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
        "/{user-id}/music",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/music",
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
                                   initWithGraphPath:@"/{user-id}/music"
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
| `target_id`<br><br>numeric string | Target node |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {},
    "`summary`": {}
}

#### `data`

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

The following fields will be added to each node that is returned:

| Field | Description |
| --- | --- |
| `created_time`<br><br>datetime | Time the object liked the page<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>int32 | Total number of objects on this edge<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

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

User Notifications
==================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can make a POST request to `notifications` edge from the following paths:

* [`/{user_id}/notifications`](https://developers.facebook.com/docs/graph-api/reference/user/notifications/)

When posting to this edge, no Graph object will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `bot_message_payload_elements`<br><br>string | Optional bot message payload used for sending a customizable generic template XMA to the recipient if a bot message is sent. If not specified, then a standard generic template XMA will be sent using just the message title and body. |
| `filtering`<br><br>list<enum{groups, groups\_social, ema}> | Notification filters to apply. |
| `href` | The relative path and GET params used in the a2u target url. |
| `label`<br><br>string | Optional label to group similar updates. |
| `message`<br><br>JSON object | Contains the title, main message body, and media image for the notification. |
| `title`<br><br>string | title<br><br>Required |
| `body`<br><br>string | body<br><br>Required |
| `media_url`<br><br>URI | media\_url |
| `notif_ids`<br><br>list<string> | The notification ids to act on. |
| `payload`<br><br>string | Optional custom payload that will be added to the URL encoding of the game that is generated when the notification is clicked. |
| `read`<br><br>boolean | Indicates that the provided notification ids should be marked as read |
| `ref`<br><br>string | A reference param used for logging |
| `schedule_interval`<br><br>int64 | Time from now (in seconds) that the notification will be sent |
| `seen`<br><br>boolean | Indicates that the provided notification ids should be marked as seen |
| `template` | Used for creating a2u notifications.<br><br>Supports Emoji |
| `type`<br><br>enum{generic, content\_update} | Notification type |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

`notification_id`: int32,

}

### Error Codes

| Error | Description |
| --- | --- |
| 288 | Sending notificatons to user requires the extended permission app\_notifications |
| 100 | Invalid parameter |
| 613 | Calls to this api have exceeded the rate limit. |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

[`/{user-id}`](https://developers.facebook.com/docs/graph-api/reference/user/)`/payment_transactions`
=====================================================================================================

The Facebook Payments orders this person placed with an app.

[](#)

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Fpayment_transactions&version=v18.0)

    GET /v18.0/me/payment_transactions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/me/payment_transactions',
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
        "/me/payment_transactions",
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
                                   initWithGraphPath:@"/me/payment_transactions"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to view any transactions made using that app.
    

### Fields

An array of [Payment objects](https://developers.facebook.com/docs/reference/api/payment/).

[](#)

Publishing
----------

You can't publish using this edge. Please see the [Payments docs for details on how to integrate this into your ap](https://developers.facebook.com/docs/payments/).

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

Graph API Reference [`/{user-id}`](https://developers.facebook.com/docs/graph-api/reference/user/)`/outbox`
===========================================================================================================

A person's Facebook Messages outbox.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Foutbox&version=v18.0)

    GET /v18.0/me/outbox HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/me/outbox',
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
        "/me/outbox",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/me/outbox",
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
                                   initWithGraphPath:@"/me/outbox"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* A user access token with `read_mailbox` permission is required to view that person's outbox.

### Fields

An array of [Thread objects](https://developers.facebook.com/docs/reference/api/thread/).

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

User permissions


====================

[](#)

Returns a list of granted and declined permissions.

* * *

### Revoking Permissions

Apps can let people revoke permissions that were previously granted. For example, your app could have a settings page that lets someone disable publishing to Facebook. That settings page could also revoke the `publish_actions` permission at the same time.

You can revoke a specific permission by making a call to a Graph API endpoint:

DELETE /{user\-id}/permissions/{permission\-name}

This request must be made with a user access token or an app access token for the current app. If the request is successful, you will receive a response of `true`.

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fpermissions&version=v18.0)

    GET /v18.0/{user-id}/permissions HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/permissions',
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
        "/{user-id}/permissions",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/permissions",
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
                                   initWithGraphPath:@"/{user-id}/permissions"
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
| `permission`<br><br>string | Permission name |
| `status`<br><br>enum{granted, declined, expired} | Permission status |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Permission](https://developers.facebook.com/docs/graph-api/reference/permission/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 459 | The session is invalid because the user has been checkpointed |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
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

You can dissociate a [Permission](https://developers.facebook.com/docs/graph-api/reference/permission/) from a [User](https://developers.facebook.com/docs/graph-api/reference/user/) by making a DELETE request to [`/{user_id}/permissions`](https://developers.facebook.com/docs/graph-api/reference/user/permissions/).

### Parameters

| Parameter | Description |
| --- | --- |
| `permission`<br><br>string | permission which wanted to be remove |

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 240 | Desktop applications cannot call this function for other users |

[](#)

User Photos
===========

[](#)

Photos for a person.

[](#)

Reading
-------

Query photos that the user tagged in / uploaded

### Uploaded Photos

By default reading from the `photos` edge includes all photos a person has been tagged in.

When you read a person's Photos you can also include an optional `type` parameter with the value `uploaded` to get only the list of photos that a person has uploaded:

GET /{user\-id}/photos?type\=uploaded

You can also use this form to add the type, but the `type=uploaded` form is preferred:

GET /{user\-id}/photos/uploaded

### Permissions

* For any photos uploaded by someone, and any photos in which they have been tagged - A user access token for that person with `user_photos` permission.
    

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fphotos&version=v18.0)

    GET /v18.0/{user-id}/photos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/photos',
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
        "/{user-id}/photos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/photos",
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
                                   initWithGraphPath:@"/{user-id}/photos"
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
| `type`<br><br>enum{tagged, uploaded} | Default value: `tagged`<br><br>Allows you to query which type of photos to return |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) nodes.

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

User Picture
============

[](#)

A User's profile image.

Querying a User ID (UID) now requires an access token. Refer to the [requirements](#requirements) table to determine which token type to include in UID-based requests.

[](#)

Reading
-------

Get the app user's profile image.

### Requirements

| Type | Requirement |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | If querying an App-Scoped User ID:<br><br>* None<br><br>If querying a User ID:<br><br>* [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) or [Page](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) access token for Facebook Login authenticated requests<br>* [App](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) access token for server-side requests<br>* [Client](https://developers.facebook.com/docs/facebook-login/access-tokens#clienttokens) access token for mobile or web client-side requests<br><br>If querying a Page-Scoped User ID:<br><br>* [Page](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference) | None |

### Notes

* Supports App-Scoped User IDs (ASID), User IDs (UID), and Page-Scoped User IDs (PSID).
* By default this edge will return a `302` redirect to the image. To get data about the image, include the `redirect=false` query string parameter.
* Profile picture URLs returned by this edge will expire.
* Tokenless requests on ASIDs made by apps that are [inactive](https://developers.facebook.com/docs/apps/#inactive-apps) or that have not completed [Data Use Checkup](https://developers.facebook.com/docs/apps/certifying_data_use) will receive an error code in response.

### Limitations

* Apps in [Development mode](https://developers.facebook.com/docs/apps#development-mode) that make tokenless requests on ASIDs will receive a silhouette image in response.
* Apps in Development mode that make requests with a [Client token](https://developers.facebook.com/docs/facebook-login/access-tokens/#clienttokens) will receive a silhouette image in response.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fpicture&version=v18.0)

    GET /v18.0/{user-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/picture',
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
        "/{user-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/picture",
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
                                   initWithGraphPath:@"/{user-id}/picture"
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
| `height`<br><br>integer | The height of this picture in pixels. |
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |
| `type`<br><br>enum{small, normal, album, large, square} | The size of this picture. It can be one of the following values: small, normal, large, square. |
| `width`<br><br>integer | The width of this picture in pixels. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A single [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) node.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |

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

User Posts
==========

Represents a collection of [Posts](https://developers.facebook.com/docs/graph-api/reference/post) on a [User](https://developers.facebook.com/docs/graph-api/reference/user).

[](#)

Reading
-------

Get a list of [Posts](https://developers.facebook.com/docs/graph-api/reference/post) on a [User](https://developers.facebook.com/docs/graph-api/reference/user).

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fposts&version=v18.0)

    GET /v18.0/{user-id}/posts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/posts',
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
        "/{user-id}/posts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/posts",
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
                                   initWithGraphPath:@"/{user-id}/posts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Limitations

This endpoint will only returns Posts created on the app user's Timeline and Posts in which the app user has been tagged.

### Requirements

| Type of Requirement | Description |
| --- | --- |
| [Access Tokens](https://developers.facebook.com/docs/facebook-login/access-tokens) | [User](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) |
| [Permissions](https://developers.facebook.com/docs/permissions/reference/) | [`user_posts`](https://developers.facebook.com/docs/permissions/reference/user_posts) |

### Query String Parameters

| Name | Description |
| --- | --- |
| `include_hidden`  <br>boolean | Set to `true` to have results include hidden Posts. |
| `show_expired`  <br>boolean | Set to `true` to have results include expired Posts. |
| `with`  <br>enum {LOCATION} | Only return Posts that have set a location. |

### Response

Reading from this edge will return a JSON formatted result:

{
    "data": \[\],
    "paging": {}
}

`data`  
A list of [Post](https://developers.facebook.com/docs/graph-api/reference/post) nodes.

`paging`  
For more details about [pagination](https://developers.facebook.com/docs/graph-api/using-graph-api#paging), see the [Graph API guide](https://developers.facebook.com/docs/graph-api/).

[](#)

Creating
--------

This operation is not supported.

[](#)

Updating
--------

This operation is not supported.

[](#)

Deleting
--------

This operation is not supported.

[](#)

[](#)

User Rich Media Documents
=========================

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Frich_media_documents&version=v18.0)

    GET /v18.0/{user-id}/rich_media_documents HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/rich_media_documents',
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
        "/{user-id}/rich_media_documents",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/rich_media_documents",
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
                                   initWithGraphPath:@"/{user-id}/rich_media_documents"
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
| `query`<br><br>string | The text entered in the typeahead used to retrieve a list of matching rich media documents based on Name or ID. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Canvas](https://developers.facebook.com/docs/graph-api/reference/canvas/) nodes.

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

As of April 4, 2018, this endpoint only returns an empty data set. Please see the [changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes/#4-4-2018) for more information.

[`/{user-id}`](https://developers.facebook.com/docs/graph-api/reference/user/)`/scores`
=======================================================================================

The [scores](https://developers.facebook.com/docs/score/) this person has received from Facebook Games that they've played.

[](#)

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Fscores&version=v18.0)

    GET /v18.0/me/scores HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/me/scores',
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
        "/me/scores",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/me/scores",
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
                                   initWithGraphPath:@"/me/scores"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token can be used to see the scores that a person has received in that app.
    
* A user access token with `user_games_activity` permission is required to see all scores that person has received from other apps.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `user` | The person associated with the scores. | [`User`](https://developers.facebook.com/docs/graph-api/reference/user/) |
| `score` | The actual score. | `int` |
| `application` | The app in which the score was achieved. | [`App`](https://developers.facebook.com/docs/reference/api/application/). |

[](#)

Publishing
----------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    POST /v18.0/me/scores HTTP/1.1
    Host: graph.facebook.com
    
    score=3444

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/me/scores',
        array (
          'score' => '3444',
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

    /* make the API call */
    FB.api(
        "/me/scores",
        "POST",
        {
            "score": "3444"
        },
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    Bundle params = new Bundle();
    params.putString("score", "3444");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/me/scores",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"score": @"3444",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/me/scores"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

As of April 24,2018, the `pubish_actions` permission has been removed. Please see the [Breaking Changes Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#login-4-24) for more details. To provide a way for your app users to share content to Facebook, we encourage you to use our [Sharing products](https://developers.facebook.com/docs/sharing) instead.

The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.

Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing this API.

* A user access token with `publish_actions` permission can be used to publish scores for that person.
    
* An app access token can be used if `publish_actions` permission was previously granted.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `score` | The score that you want to set for this person. | `int` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

[](#)

Deleting
--------

You can delete the score this person has received from your app only.

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK

    DELETE /v18.0/me/scores HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->delete(
        '/me/scores',
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
        "/me/scores",
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
        "/me/scores",
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
                                   initWithGraphPath:@"/me/scores"
                                          parameters:params
                                          HTTPMethod:@"DELETE"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

As of April 24,2018, the `pubish_actions` permission has been removed. Please see the [Breaking Changes Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#login-4-24) for more details.

The **Scores API** is available only for apps that are categorized as Games and have already been granted the `publish_actions` permission in the past.

Please note that `publish_actions` will not be granted for new apps with the sole purpose of accessing these APIs.

* A user access token with `publish_actions` permission can be used to delete scores (from this app) for that person.
    
* An app access token can be used if `publish_actions` permission was previously granted.
    

### Fields

No fields are required to delete.

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

[](#)

Updating
--------

You can update a person's score for your app by [publishing a new score](#publish).

[](#)

[](#)

User Videos
===========

[](#)

Reading
-------

GET GraphUserVideosEdge

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Buser-id%7D%2Fvideos&version=v18.0)

    GET /v18.0/{user-id}/videos HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{user-id}/videos',
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
        "/{user-id}/videos",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{user-id}/videos",
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
                                   initWithGraphPath:@"/{user-id}/videos"
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
| `type`<br><br>enum {TAGGED, UPLOADED} | Default value: `"TAGGED"`<br><br>Allows you to query which type of videos to return |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Video](https://developers.facebook.com/docs/graph-api/reference/video/) nodes.

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

You can make a POST request to `videos` edge from the following paths:

* [`/{user_id}/videos`](https://developers.facebook.com/docs/graph-api/reference/user/videos/)

When posting to this edge, a [Video](https://developers.facebook.com/docs/graph-api/reference/video/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `audio_story_wave_animation_handle`<br><br>string | Everstore handle of wave animation used to burn audio story video |
| `content_category`[](#)<br><br>enum {BEAUTY\_FASHION, BUSINESS, CARS\_TRUCKS, COMEDY, CUTE\_ANIMALS, ENTERTAINMENT, FAMILY, FOOD\_HEALTH, HOME, LIFESTYLE, MUSIC, NEWS, POLITICS, SCIENCE, SPORTS, TECHNOLOGY, VIDEO\_GAMING, OTHER} | Content category of this video. |
| `description`<br><br>UTF-8 string | The text describing a post that may be shown in a story about it.<br>                                                                  It may include rich text information, such as entities and emojis.<br><br>Supports Emoji |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `embeddable`[](#)<br><br>boolean | Whether the video is embeddable. |
| `end_offset`[](#)<br><br>int64 | end\_offset |
| `file_size`[](#)<br><br>int64 | The size of the entire video file in bytes. |
| `file_url`<br><br>string | Accessible URL of a video file. Cannot be used with `upload_phase`. |
| `fisheye_video_cropped`<br><br>boolean | Whether the single fisheye video is cropped or not |
| `fov`<br><br>int64 | 360 video only: Vertical field of view |
| `front_z_rotation`<br><br>float | The front z rotation in degrees on the single fisheye video |
| `guide`<br><br>list<list<int64>> | 360 video only: Guide keyframes data. An array of keyframes, each of which is an array of 3 or 4 elements in the following order: \[video timestamp (seconds), pitch (degrees, -90 ~ 90), yaw (degrees, -180 ~ 180), field of view (degrees, 40 ~ 90, optional)\], ordered by video timestamp in strictly ascending order. |
| `guide_enabled`<br><br>boolean | 360 video only: Whether Guide is active. |
| `initial_heading`<br><br>int64 | 360 video only: Horizontal camera perspective to display when the video begins. |
| `initial_pitch`<br><br>int64 | 360 video only: Vertical camera perspective to display when the video begins. |
| `is_voice_clip`[](#)<br><br>boolean | is\_voice\_clip, used to indicate that if a video is used as audio record |
| `no_story`<br><br>boolean | Default value: `false`<br><br>If set to `true`, this will suppress feed and timeline story. |
| `original_fov`<br><br>int64 | Original field of view of the source camera |
| `original_projection_type`[](#)<br><br>enum {equirectangular, cubemap, half\_equirectangular} | 360 video only: The original projection type of the 360 video being uploaded. |
| `posting_to_redspace`[](#)<br><br>enum {enabled, disabled} | Whether the post should appear in RedSpace. |
| `privacy`<br><br>Privacy Parameter | Determines the [privacy settings](https://developers.facebook.com/docs/graph-api/common-scenarios#privacy-param) of the video. If not supplied, this defaults to the privacy level granted to the app in the Login Dialog. This field cannot be used to set a more open privacy setting than the one granted. |
| `prompt_id`[](#)<br><br>string | The prompt id in prompts or purple rain that generated this post |
| `prompt_tracking_string`[](#)<br><br>string | The prompt tracking string associated with this video post |
| `react_mode_metadata`<br><br>JSON-encoded string | This metadata is required for clip reacts feature |
| `referenced_sticker_id`<br><br>numeric string or integer | Sticker id of the sticker in the post |
| `replace_video_id`[](#)<br><br>numeric string or integer | The video id your uploaded video about to replace |
| `slideshow_spec`<br><br>JSON object | Specification of a list of images that are used to generate video. |
| `images_urls`<br><br>list<URL> | A 3-7 element array of the URLs of the images. Required.<br><br>Required |
| `duration_ms`<br><br>integer | The duration in milliseconds of each image. Default value is 1000. |
| `transition_ms`<br><br>integer | The duration in milliseconds of the crossfade transition between images. Default value is 1000. |
| `reordering_opt_in`<br><br>boolean | Default value: `false` |
| `music_variations_opt_in`<br><br>boolean | Default value: `false` |
| `source`<br><br>string | The video, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT31t8y9-Q1OyG4fYalnFhJFF4O7L85J5u8xPqaFpzpV24egt6NhkYll45cU2e6D9qgv9SfT-cstTpC2OW2arR_T8NDOlRy0-0wpPhNp-IFurcHXqhJNQH7rsg9bZq-vSBkHlQ7zr0KqmPkeq8cblGs5DLkNG6su5Ec). This field is required. |
| `spherical`<br><br>boolean | Default value: `false`<br><br>Set if the video was recorded in 360 format. |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the video post |
| `start_offset`[](#)<br><br>int64 | Start byte position of the file chunk. |
| `swap_mode`[](#)<br><br>enum {replace} | Type of replacing video request |
| `title`<br><br>UTF-8 string | The title of the video<br><br>Supports Emoji |
| `transcode_setting_properties`[](#)<br><br>string | Properties used in computing transcode settings for the video |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Type of unpublished content, such as scheduled, draft or ads\_post. |
| `upload_phase`[](#)<br><br>enum {start, transfer, finish, cancel} | Type of chunked upload request. |
| `upload_session_id`[](#)<br><br>numeric string or integer | ID of the chunked upload session. |
| `video_file_chunk`[](#)<br><br>string | The video file chunk, [encoded as form data](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.w3.org%2FTR%2Fhtml401%2Finteract%2Fforms.html%23h-17.13.4.2&h=AT0kcBWnq-K3khnhOVk4PXKsC2FR_b8YaN5c-G5s0K6l1co5ymzT3sw3z-DzfnXtQ5DC6b32kf-noKMNLG_hkDYRShk5LUJ6tAHn8N1Ne74lHXoyCu-CBsDYhAOR3bYEad5g8eb6XwSLyyt5afUoeQ). This field is required during `transfer` upload phase. |
| `video_id_original`[](#)<br><br>string | video\_id\_original |

### Return Type

Struct {

`id`: numeric string,

`upload_session_id`: numeric string,

`video_id`: numeric string,

`start_offset`: numeric string,

`end_offset`: numeric string,

`success`: bool,

`skip_upload`: bool,

`upload_domain`: string,

`region_hint`: string,

`xpv_asset_id`: numeric string,

`is_xpv_single_prod`: bool,

`transcode_bit_rate_bps`: numeric string,

`transcode_dimension`: numeric string,

`should_expand_to_transcode_dimension`: bool,

`action_id`: string,

`gop_size_seconds`: numeric string,

`target_video_codec`: string,

`target_hdr`: string,

`maximum_frame_rate`: numeric string,

}

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 6000 | There was a problem uploading your video file. Please try again with another file. |
| 6001 | There was a problem uploading your video. Please try again. |
| 459 | The session is invalid because the user has been checkpointed |
| 190 | Invalid OAuth 2.0 Access Token |
| 194 | Missing at least one required parameter |
| 210 | User not visible |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)