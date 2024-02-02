Event - Graph API Reference - Documentation - Meta for Developers

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
Graph API Versionv19.0Event
=====
Represents an Event.

### Limitations

Access to Events on Users and Pages is only available to Facebook Marketing Partners.

Reading
-------
Get fields and edges on an Event.

### Requirements

For Events on an App:

* An App access token of an App that created the Event.

For Events on a Group:

* A User access token of an Admin of the Event.
* The Groups API feature.

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{event-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{event-id}',
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
    "/{event-id}",
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
    "/{event-id}",
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
                               initWithGraphPath:@"/{event-id}"
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

| Field | Description |
| --- | --- |
| `id`numeric string | The event ID
 |
| `attending_count`int32 | Number of people attending the event
 |
| `can_guests_invite`bool | Can guests invite friends. Requires an access token of an Admin of the Event
 |
| `category`enum {CLASSIC\_LITERATURE, COMEDY, CRAFTS, DANCE, DRINKS, FITNESS\_AND\_WORKOUTS, FOODS, GAMES, GARDENING, HEALTH\_AND\_MEDICAL, HEALTHY\_LIVING\_AND\_SELF\_CARE, HOME\_AND\_GARDEN, MUSIC\_AND\_AUDIO, PARTIES, PROFESSIONAL\_NETWORKING, RELIGIONS, SHOPPING\_EVENT, SOCIAL\_ISSUES, SPORTS, THEATER, TV\_AND\_MOVIES, VISUAL\_ARTS} | The category of the event
 |
| `cover`CoverPhoto | Cover picture
 |
| `created_time`datetime | created\_time
 |
| `declined_count`int32 | Number of people who declined the event
 |
| `description`string | Long-form description
Default |
| `discount_code_enabled`bool | Is discount code enabled for this event
 |
| `end_time`string | End time, if one has been set
Default |
| `event_times`list<ChildEvent> | Array of times of a multi-instance event
Default |
| `guest_list_enabled`bool | Can see guest list. Requires an access token of an Admin of the Event
 |
| `interested_count`int32 | Number of people interested in the event
 |
| `is_canceled`bool | Whether or not the event has been marked as canceled
 |
| `is_draft`bool | Whether the event is in draft mode or published. Requires an access token of an Admin of the Event
 |
| `is_online`bool | Whether the event is online or not. Required to pass the 'address' (city name) parameter for online events.
 |
| `is_page_owned`bool | Whether the event is created by page or not
 |
| `maybe_count`int32 | Number of people who maybe going to the event
 |
| `name`string | Event name
Default |
| `noreply_count`int32 | Number of people who did not reply to the event
 |
| `online_event_format`enum {messenger\_room, third\_party, fb\_live, other, none} | Type of online event - Live, Link or Other
 |
| `online_event_third_party_url`string | Third party streaming url associated with Link events
 |
| `owner` | The profile that created the event
 |
| `place`Place | Event Place information
Default |
| `scheduled_publish_time`string | Time when event is scheduled to be published
 |
| `start_time`string | Start time
Default |
| `ticket_uri`string | The link users can visit to buy a ticket to this event
 |
| `ticket_uri_start_sales_time`string | Time when tickets go on sale
 |
| `ticketing_privacy_uri`string | URI to seller's privacy policy for ticket purchases
 |
| `ticketing_terms_uri`string | URI to seller's terms of service for ticket purchases
 |
| `timezone`enum | Timezone
 |
| `type`enum {private, public, group, community, friends, work\_company} | The type of the event
 |
| `updated_time`datetime | Last update time (ISO 8601 formatted)
 |
### Edges

| Edge | Description |
| --- | --- |
| `roles` | List of profiles having roles on the event. Requires an access token of an Admin of the Event
 |
| `ticket_tiers` | List of ticket tiers. Requires an access token of an Admin of the Event
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 458 | The session is invalid because the application is not installed |
| 190 | Invalid OAuth 2.0 Access Token |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.