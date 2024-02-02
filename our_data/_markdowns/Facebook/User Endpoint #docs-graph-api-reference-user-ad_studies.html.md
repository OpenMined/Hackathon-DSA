Graph API Reference v19.0: User Ad Studies - Documentation - Meta for Developers

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
Graph API Versionv19.0User Ad Studies
===============
Reading
-------
UserAdStudies

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{user-id}/ad_studies HTTP/1.1
Host: graph.facebook.com
```
```
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
```
```
/* make the API call */
FB.api(
    "/{user-id}/ad_studies",
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
    "/{user-id}/ad_studies",
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
                               initWithGraphPath:@"/{user-id}/ad_studies"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters
This endpoint doesn't have any parameters.### Fields
Reading from this edge will return a JSON formatted result:

```
{
 "`data`": [],
 "`paging`": {},
 "`summary`": {}
}

```
#### `data`
A list of AdStudy nodes.#### `paging`
For more details about pagination, see the Graph API guide.#### `summary`
Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`unsigned int32 | Total number of lift studies for this person
 |
### Error Codes

| Error | Description |
| --- | --- |
| 270 | This Ads API request is not allowed for apps with development access level (Development access is by default for all apps, please request for upgrade). Make sure that the access token belongs to a user that is both admin of the app and admin of the ad account |
| 100 | Invalid parameter |
Creating
--------
You can make a POST request to `ad_studies` edge from the following paths: * `/{user_id}/ad_studies`
When posting to this edge, an AdStudy will be created.### Parameters

| Parameter | Description |
| --- | --- |
| `cells`list<Object> | A shape to describe the cells of the study
 |
| `description`string |  |
| `id`int64 |  |
| `name`string |  |
| `creation_template`enum {AUTOMATIC\_PLACEMENTS, BRAND\_AWARENESS, FACEBOOK, FACEBOOK\_AUDIENCE\_NETWORK, FACEBOOK\_INSTAGRAM, FACEBOOK\_NEWS\_FEED, FACEBOOK\_NEWS\_FEED\_IN\_STREAM\_VIDEO, IN\_STREAM\_VIDEO, INSTAGRAM, MOBILE\_OPTIMIZED\_VIDEO, PAGE\_POST\_ENGAGEMENT, REACH, TV\_COMMERCIAL, TV\_FACEBOOK, VIDEO\_VIEW\_OPTIMIZATION, LOW\_FREQUENCY, MEDIUM\_FREQUENCY, HIGH\_FREQUENCY} |  |
| `adaccounts`list<int64> |  |
| `adsets`list<numeric string or integer> |  |
| `campaigns`list<numeric string or integer> |  |
| `control_percentage`float with at most two digits after decimal point |  |
| `treatment_percentage`float with at most two digits after decimal point |  |
| `client_business`numeric string or integer | Business associated with study
 |
| `confidence_level`float | Confidence level used in power calculation and final report
 |
| `cooldown_start_time`integer | The beginning of the pre measurement cooldown period. This period ends when the study period starts.
 |
| `description`string | A brief description about the purpose of the study.
 |
| `end_time`integer | The time when the study period ends.
 |
| `name`string | The name of the study.
 |
| `objectives`list<Object> | A vector of objects describing the objectives assigned to this study
 |
| `id`numeric string or integer |  |
| `is_primary`boolean |  |
| `name`string |  |
| `type`enum {SALES, NONSALES, MAE, TELCO, FTL, MAI, PARTNER, BRANDLIFT, BRAND, MPC\_CONVERSION, CONVERSIONS} |  |
| `offsite_datasets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `adspixels`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `customconversions`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `applications`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `offline_conversion_data_sets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `product_sets`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `product_catalogs`list<JSON or object-like arrays> |  |
| `id`numeric string or integer | Required |
| `event_names`list<string> |  |
| `observation_end_time`integer | The end of the observation period for this study, this period starts when the study period ends.
 |
| `start_time`integer | The time when the study period starts.
 |
| `type`enum {LIFT, SPLIT\_TEST, CONTINUOUS\_LIFT\_CONFIG, GEO\_LIFT} | The type of ad study, either SPLIT\_TEST or LIFT.
 |
| `viewers`list<int> | The list of people who this study has been shared with.
 |
### Return Type
This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `cell_ids`: List [numeric string], `objective_ids`: List [numeric string], }### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.