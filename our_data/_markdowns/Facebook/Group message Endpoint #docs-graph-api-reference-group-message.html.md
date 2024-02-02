Graph API Reference v19.0: Group Message - Documentation - Meta for Developers

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
Graph API Versionv19.0Group Message
=============
Reading
-------
GroupMessage

### New Page Experience
This endpoint is supported for New Page Experience.### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{group-message-id} HTTP/1.1
Host: graph.facebook.com
```
```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{group-message-id}',
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
    "/{group-message-id}",
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
    "/{group-message-id}",
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
                               initWithGraphPath:@"/{group-message-id}"
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
| `id`token with structure: Post ID | id
 |
| `actions`list | actions
 |
| `admin_creator`BusinessUser|User|Application | admin\_creator
 |
| `allowed_advertising_objectives`list<string> | allowed\_advertising\_objectives
 |
| `application`Application | application
 |
| `backdated_time`datetime | backdated\_time
 |
| `call_to_action`struct with keys: type, value | call\_to\_action
 |
| `can_reply_privately`bool | can\_reply\_privately
 |
| `caption`string | caption
 |
| `child_attachments`list | child\_attachments
 |
| `comments_mirroring_domain`string | comments\_mirroring\_domain
 |
| `coordinates`struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | coordinates
 |
| `created_time`datetime | created\_time
Default |
| `description`string | description
 |
| `event`Event | event
 |
| `expanded_height`unsigned int32 | expanded\_height
 |
| `expanded_width`unsigned int32 | expanded\_width
 |
| `feed_targeting`struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | feed\_targeting
 |
| `from`User|Page | from
 |
| `full_picture`string | full\_picture
 |
| `height`unsigned int32 | height
 |
| `icon`string | icon
 |
| `is_app_share`bool | is\_app\_share
 |
| `is_eligible_for_promotion`bool | is\_eligible\_for\_promotion
 |
| `is_expired`bool | is\_expired
 |
| `is_hidden`bool | is\_hidden
 |
| `is_inline_created`bool | is\_inline\_created
 |
| `is_popular`bool | is\_popular
 |
| `is_published`bool | is\_published
 |
| `is_spherical`bool | is\_spherical
 |
| `link`uri | link
 |
| `message`string | message
Default |
| `message_tags`list | message\_tags
 |
| `multi_share_end_card`bool | multi\_share\_end\_card
 |
| `multi_share_optimized`bool | multi\_share\_optimized
 |
| `name`string | name
 |
| `object_id`string | object\_id
 |
| `parent_id`token with structure: Post ID | parent\_id
 |
| `permalink_url`uri | permalink\_url
 |
| `place`Place | place
 |
| `privacy`Privacy | privacy
 |
| `promotable_id`token with structure: Post ID | promotable\_id
 |
| `properties`list | properties
 |
| `scheduled_publish_time`float | scheduled\_publish\_time
 |
| `shares`struct with keys: count | shares
 |
| `source`string | source
 |
| `status_type`string | status\_type
 |
| `story`string | story
Default |
| `story_tags`list | story\_tags
 |
| `subscribed`bool | subscribed
 |
| `target`Profile | target
 |
| `targeting`struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | targeting
 |
| `timeline_visibility`string | timeline\_visibility
 |
| `type`string | type
 |
| `updated_time`datetime | updated\_time
 |
| `via`User|Page | via
 |
| `width`unsigned int32 | width
 |
### Edges

| Edge | Description |
| --- | --- |
| `attachments` | attachments
 |
| `comments` | comments
 |
| `dynamic_posts` | dynamic\_posts
 |
| `insights` | insights
 |
| `reactions` | reactions
 |
| `sharedposts` | sharedposts
 |
| `sponsor_tags` | sponsor\_tags
 |
| `to` | to
 |
### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.