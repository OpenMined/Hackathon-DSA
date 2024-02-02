
Graph API Reference v19.0: Post - Documentation - Meta for Developers












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
Graph API Versionv19.0Post
====

An individual post in a profile's feed. The profile could be a user, page, app, or group.

Reading
-------

A Facebook Feed story


### New Page Experience

This endpoint is supported for New Page Experience.### Feature Permissions



| Name | Description |
| --- | --- |
| Page Public Content Access | This feature permission may be required. |

### Permissions

* A page access token can read all posts posted to or posted by that Page.
* A page access token with the `pages_manage_posts` permission and Page Public Content Access Feature are required to read publicly shared Page posts. The person requesting the access token must be an admin of the Page.
* A user access token can read any post your application created on behalf of that user.
* A user's post can be read if the owner has granted the `user_posts` permission.
* A user access token may read a post that user is tagged in if they have granted the `user_posts` permission. However, in some cases the post's owner's privacy settings may not allow your application to access it.
### Limitations


The following fields for `/page/feed`, `/page/posts`, `/pageposts`, and `/page/published_posts` were deprecated in v3.3:


* `caption`
* `description`
* `link`
* `name`
* `object_id`
* `source`
* `type`


### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{post-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{post-id}',
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
    "/{post-id}",
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
    "/{post-id}",
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
                               initWithGraphPath:@"/{post-id}"
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
| `id`token with structure: Post ID | The post ID.
 |
| `actions`list | Action links
 |
| `admin_creator`BusinessUser|User|Application | The admin creator of a Page Post. Only available if there exists more than one admin for the page.
 |
| `allowed_advertising_objectives`list<string> | The only objectives under which this post can be advertised
 |
| `application`Application | Information about the app this post was published by.
 |
| `backdated_time`datetime | The backdated time for backdate post. For regular post, this field will be set to null.
 |
| `call_to_action`struct with keys: type, value | The call to action type used in any Page posts for mobile app engagement ads.
 |
| `can_reply_privately`bool | Whether the page viewer can send a private reply to this post
 |
| `caption`string | The caption of a link in the post (appears beneath the name).
 |
| `child_attachments`list | Sub-shares of a multi-link share post
 |
| `comments_mirroring_domain`string | If comments are being mirrored to an external site, this function returns the domain of that external site.
 |
| `coordinates`struct with keys: checkin\_id, author\_uid, page\_id, target\_id, target\_href, coords, tagged\_uids, timestamp, message, target\_type | An array of information about the attachment to the post
 |
| `created_time`datetime | The time the post was published, expressed as UNIX timestamp
Default |
| `description`string | A description of a link in the post (appears beneath the caption).
 |
| `event`Event | If this Post has a place, the event associated with the place
 |
| `expanded_height`unsigned int32 | An array of information about the attachment to the post
 |
| `expanded_width`unsigned int32 | An array of information about the attachment to the post
 |
| `feed_targeting`struct with keys: country, cities, regions, genders, age\_min, age\_max, education\_statuses, college\_years, relationship\_statuses, interests, interested\_in, user\_adclusters, locales, countries, geo\_locations, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, industries, politics, ethnic\_affinity, generation, fan\_of, relevant\_until\_ts | Object that controls news feed targeting for this post. Anyone in these groups will be more likely to see this post, others will be less likely, but may still see it anyway. Any of the targeting fields shown here can be used, none are required (applies to Pages only).
 |
| `from`User|Page | The ID of the user, page, group, or event that published the post
 |
| `full_picture`string | If the photo's largest dimension exceeds 720 pixels, it is resized, with the largest dimension set to 720.
 |
| `height`unsigned int32 | An array of information about the attachment to the post
 |
| `icon`string | A link to an icon representing the type of this post.
 |
| `is_app_share`bool | Whether or not the post references an app
 |
| `is_eligible_for_promotion`bool | Whether the post is eligible for promotion.
 |
| `is_expired`bool | Whether the post has expiration time that has passed
 |
| `is_hidden`bool | Whether a post has been set to hidden
 |
| `is_inline_created`bool | Returns True if the post was created inline when creating ads.
 |
| `is_popular`bool | Whether the post is currently popular. Based on whether the total actions as a percentage of reach exceeds a certain threshold
 |
| `is_published`bool | Indicates whether a scheduled post was published (applies to scheduled Page Post only, for users post and instanlty published posts this value is always true)
 |
| `is_spherical`bool | Whether the post is a spherical video post
 |
| `link`uri | A description of a link in the post (appears beneath the caption).
 |
| `message`string | The message written in the post
Default |
| `message_tags`list | Profiles mentioned or tagged in a message. This is an object with a unique key for each mention or tag in the message.
 |
| `multi_share_end_card`bool | Whether display the end card for a multi-link share post
 |
| `multi_share_optimized`bool | Whether automatically select the order of the links in multi-link share post when used in an ad
 |
| `name`string | The name of the link.
 |
| `object_id`string | The ID of any uploaded photo or video attached to the post.
 |
| `parent_id`token with structure: Post ID | The ID of a parent post for this post, if it exists. For example, if this story is a 'Your Page was mentioned in a post' story, the parent\_id will be the original post where the mention happened
 |
| `permalink_url`uri | The permanent static URL to the post on www.facebook.com. Example: https://www.facebook.com/FacebookforDevelopers/posts/10153449196353553
 |
| `place`Place | ID of the place associated with the post
 |
| `privacy`Privacy | The privacy settings for a post
 |
| `promotable_id`token with structure: Post ID | ID of post to use for promotion for stories that cannot be promoted directly
 |
| `properties`list | A list of properties for any attached video, for example, the length of the video.
 |
| `scheduled_publish_time`float | UNIX timestamp of the scheduled publish time for the post
 |
| `shares`struct with keys: count | Number of times the post has been shared
 |
| `source`string | A URL to any Flash movie or video file attached to the post.
 |
| `status_type`string | Description of the type of a status update.
 |
| `story`string | Text of stories not intentionally generated by users, such as those generated when two users become friends. You must have the "Include recent activity stories" migration enabled in your app to retrieve this field
Default |
| `story_tags`list | The list of tags in the post description
 |
| `subscribed`bool | Whether user is subscribed to the post
 |
| `target`Profile | The profile this was posted on if different from the author
 |
| `targeting`struct with keys: country, cities, regions, zips, genders, college\_networks, work\_networks, age\_min, age\_max, education\_statuses, college\_years, college\_majors, political\_views, relationship\_statuses, interests, keywords, interested\_in, user\_clusters, user\_clusters2, user\_clusters3, user\_adclusters, excluded\_user\_adclusters, custom\_audiences, excluded\_custom\_audiences, locales, radius, connections, excluded\_connections, friends\_of\_connections, countries, excluded\_user\_clusters, adgroup\_id, user\_event, qrt\_versions, page\_types, user\_os, user\_device, action\_spec, action\_spec\_friend, action\_spec\_excluded, geo\_locations, excluded\_geo\_locations, targeted\_entities, conjunctive\_user\_adclusters, wireless\_carrier, site\_category, work\_positions, work\_employers, education\_majors, education\_schools, family\_statuses, life\_events, behaviors, travel\_status, industries, politics, markets, income, net\_worth, home\_type, home\_ownership, home\_value, ethnic\_affinity, generation, household\_composition, moms, office\_type, interest\_clusters\_expansion, dynamic\_audience\_ids, product\_audience\_specs, excluded\_product\_audience\_specs, exclusions, flexible\_spec, engagement\_specs, excluded\_engagement\_specs | Object that limited the audience for this content. Anyone not in these demographics will not be able to view this content. This will not override any Page-level demographic restrictions that may be in place.
 |
| `timeline_visibility`string | Timeline visibility information of the post
 |
| `type`string | A string indicating the object type of this post.
 |
| `updated_time`datetime | The time the post was last updated, which occurs when a user comments on the post.
 |
| `via`User|Page | ID of the user or Page the post was shared from
 |
| `width`unsigned int32 | An array of information about the attachment to the post
 |

### Edges



| Edge | Description |
| --- | --- |
| `attachments` | Any attachments that are associated with the story
 |
| `comments` | Comments made on this
 |
| `dynamic_posts` | All dynamic ad creatives
 |
| `insights` | Insights for this post (only for Pages).
 |
| `reactions` | People who reacted on this
 |
| `sharedposts` | Shared posts
 |
| `sponsor_tags` | An array sponsor pages tagged in the post
 |
| `to` | Profiles mentioned or targeted in this post.
 |

### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 2500 | Error parsing graph query |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 459 | The session is invalid because the user has been checkpointed |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can publish posts by using the `/{user-id}/feed`, `/{page-id}/feed`, `/{event-id}/feed`, or `/{group-id}/feed` edges.

When creating a Post for a Page if you use a user access token the post will be in the voice of the user that posted it. If you use a page access token, the post will be in the voice of the page.

You can't perform this operation on this endpoint.Deleting
--------

You can't perform this operation on this endpoint.

































