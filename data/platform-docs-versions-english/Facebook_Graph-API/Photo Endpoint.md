Photo
=====

[](#)

Represents an individual photo on Facebook.

[](#)

Reading
-------

This represents a Photo on Facebook.

### Permissions

* Any valid access token can read photos on a public Page.
    
* A page access token can read all photos posted to or posted by that Page.
    
* The current user's photos can be read if the user has granted the `user_photos` or `user_posts` permission.
    
* A user access token may read a photo that the current user is tagged in if they have granted the `user_photos` or `user_posts` permission. However, in some cases the photo's owner's privacy settings may not allow your application to access it.
    
* A User access token for an Admin of a Group can read Group-owned Photos.
    
* A User access token for an Admin of an Event can read Event-owned Photos if required after April 30, 2018.
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Feature Permissions

| Name | Description |
| --- | --- |
| Page Public Content Access | This [feature permission](https://developers.facebook.com/docs/apps/review/feature/) may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bphoto-id%7D&version=v18.0)

    GET /v18.0/{photo-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{photo-id}',
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
        "/{photo-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{photo-id}",
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
                                   initWithGraphPath:@"/{photo-id}"
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
| `id`<br><br>numeric string | The photo ID |
| `album`<br><br>[Album](https://developers.facebook.com/docs/graph-api/reference/album/) | The album this photo is in |
| `alt_text`<br><br>string | Accessible alternative description for an image |
| `alt_text_custom`<br><br>string | User provided accessible alternative description for an image |
| `backdated_time`<br><br>datetime | A user-specified time for when this object was created |
| `backdated_time_granularity`<br><br>enum | How accurate the backdated time is |
| `can_backdate`<br><br>bool | Indicates whether the viewer can backdate the photo |
| `can_delete`<br><br>bool | Indicates whether the viewer can delete the photo |
| `can_tag`<br><br>bool | Indicates whether the viewer can tag the photo |
| `created_time`<br><br>datetime | The time this photo was published<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `event`[](#)<br><br>[Event](https://developers.facebook.com/docs/graph-api/reference/event/) | If this object has a place, the event associated with the place |
| `from`<br><br>User\|Page | The profile (user or page) that uploaded this photo |
| `height`<br><br>unsigned int32 | The height of this photo in pixels |
| `icon`<br><br>string | The icon that Facebook displays when photos are published to News Feed |
| `images`<br><br>[list<PlatformImageSource>](https://developers.facebook.com/docs/graph-api/reference/platform-image-source/) | The different stored representations of the photo. Can vary in number based upon the size of the original photo. |
| `link`<br><br>string | A link to the photo on Facebook |
| `name`<br><br>string | The user-provided caption given to this photo. Corresponds to `caption` when creating photos<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `name_tags`<br><br>[list<EntityAtTextRange>](https://developers.facebook.com/docs/graph-api/reference/entity-at-text-range/) | An array containing an array of objects mentioned in the name field which contain the id, name, and type of each object as well as the offset and length which can be used to match it up with its corresponding string in the name field |
| `page_story_id`<br><br>string | ID of the page story this corresponds to. May not be on all photos. Applies only to published photos |
| `place`<br><br>[Place](https://developers.facebook.com/docs/graph-api/reference/place/) | Place info |
| `position`<br><br>unsigned int32 | Deprecated. Returns 0<br><br>Deprecated |
| `source`<br><br>string | Deprecated. Use `images` instead<br><br>Deprecated |
| `target`<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | The target this photo is published to |
| `updated_time`<br><br>datetime | The last time the photo was updated |
| `webp_images`<br><br>[list<PlatformImageSource>](https://developers.facebook.com/docs/graph-api/reference/platform-image-source/) | The different stored representations of the photo in webp format. Can vary in number based upon the size of the original photo. |
| `width`<br><br>unsigned int32 | The width of this photo in pixels |

### Edges

| Edge | Description |
| --- | --- |
| [`insights`](https://developers.facebook.com/docs/graph-api/reference/photo/insights/) | Insights data |
| [`likes`](https://developers.facebook.com/docs/graph-api/reference/photo/likes/) | People who like this |
| [`picture`](https://developers.facebook.com/docs/graph-api/reference/photo/picture/) | Link to the 100px wide representation of this photo |
| [`sponsor_tags`](https://developers.facebook.com/docs/graph-api/reference/photo/sponsor_tags/) | Sponsor pages tagged in the photo. |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 190 | Invalid OAuth 2.0 Access Token |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 459 | The session is invalid because the user has been checkpointed |
| 3001 | Invalid query |
| 2500 | Error parsing graph query |

[](#)

Creating
--------

Animated photos are not supported, and a photo must be less than 10MB in size.

Note: the `post_id` value is not returned for photos added to Albums.

You can make a POST request to `photos` edge from the following paths:

* [`/{album_id}/photos`](https://developers.facebook.com/docs/graph-api/reference/album/photos/)

When posting to this edge, a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `aid`<br><br>string | Legacy album ID. Deprecated<br><br>Deprecated |
| `allow_spherical_photo`<br><br>boolean | Default value: `false`<br><br>Indicates that we should allow this photo to be treated as a spherical photo. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true. |
| `alt_text_custom`<br><br>string | Accessible alternative description for an image |
| `android_key_hash`<br><br>string | Android key hash |
| `application_id`<br><br>non-empty string | iTunes App ID. This is used by the native Share dialog that's part of iOS |
| `attempt`<br><br>int64 | Default value: `0`<br><br>Number of attempts that have been made to upload this photo |
| `audience_exp`<br><br>boolean | Default value: `false`<br><br>Audience exp |
| `backdated_time`<br><br>datetime | A user-specified creation time for this photo |
| `backdated_time_granularity`<br><br>enum{year, month, day, hour, min, none} | Default value: `none`<br><br>Use only the part of the `backdated_time` parameter to the specified granularity |
| `caption`<br><br>UTF-8 string | The description of the photo<br><br>Supports Emoji |
| `composer_session_id`<br><br>string | Composer session ID |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post. |
| `feed_targeting`<br><br>feed target | Object that controls [News Feed targeting](https://www.facebook.com/help/352402648173466) for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only. |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> | Values for targeted locales. Use `type` of `adlocale` to [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned key to specify. |
| `age_min`<br><br>int64 | Must be `13` or higher. Default is 0. |
| `age_max`<br><br>int64 | Maximum age. |
| `genders`<br><br>list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both. |
| `college_years`<br><br>list<int64> | Array of integers. Represent graduation years from college. |
| `education_statuses`<br><br>list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents). |
| `interested_in`<br><br>list<int64> | Deprecated. Please see the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#2-7-2018) for more information.<br><br>Deprecated |
| `relationship_statuses`<br><br>list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types. |
| `interests`<br><br>list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned id to specify. |
| `filter_type`<br><br>int64 | Default value: `-1`<br><br>Unused? |
| `full_res_is_coming_later`<br><br>boolean | Default value: `false`<br><br>Full res is coming later |
| `initial_view_heading_override_degrees`<br><br>int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_pitch_override_degrees`<br><br>int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_vertical_fov_override_degrees`<br><br>int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `ios_bundle_id`<br><br>string | iOS Bundle ID |
| `is_explicit_location`<br><br>boolean | Is this an explicit location? |
| `is_explicit_place`<br><br>boolean | If set to `true`, the tag is a place, not a person |
| `manual_privacy`<br><br>boolean | Default value: `false`<br><br>Manual privacy |
| `message`<br><br>UTF-8 string | Deprecated. Please use the caption param instead.<br><br>DeprecatedSupports Emoji |
| `name`<br><br>UTF-8 string | Deprecated. Please use the caption param instead.<br><br>DeprecatedSupports Emoji |
| `no_story`<br><br>boolean | If set to `true`, this will suppress the News Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story |
| `offline_id`<br><br>int64 | Default value: `0`<br><br>Offline ID |
| `og_action_type_id`<br><br>numeric string or integer | The Open Graph action type |
| `og_icon_id`<br><br>numeric string or integer | The Open Graph icon |
| `og_object_id`<br><br>OG object ID or URL string | The Open Graph object ID |
| `og_phrase`<br><br>string | The Open Graph phrase |
| `og_set_profile_badge`<br><br>boolean | Default value: `false`<br><br>Flag to set if the post should create a profile badge |
| `og_suggestion_mechanism`<br><br>string | The Open Graph suggestion |
| `place`<br><br>place tag | Page ID of a place associated with the photo |
| `privacy`<br><br>Privacy Parameter | Determines the privacy settings of the photo. If not supplied, this defaults to the privacy level granted to the app in the Login dialog. This field cannot be used to set a more open privacy setting than the one granted |
| `profile_id`<br><br>int | Deprecated. Use `target_id` instead<br><br>Deprecated |
| `proxied_app_id`<br><br>numeric string or integer | Proxied app ID |
| `published`<br><br>boolean | Default value: `true`<br><br>Set to `false` if you don't want the photo to be published immediately |
| `qn`<br><br>string | Photos waterfall ID |
| `scheduled_publish_time`<br><br>int64 | Time at which an unpublished post should be published (Unix ISO-8601 format). Applies to Pages only |
| `spherical_metadata`<br><br>JSON object | A set of params describing an uploaded spherical photo. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata |
| `ProjectionType`<br><br>string | Accepted values include equirectangular (full spherical photo), cylindrical (panorama), and cubestrip (also known as cubemap, e.g. for synthetic or rendered content; stacked vertically with 6 faces).<br><br>Required |
| `CroppedAreaImageWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value should be equal to the actual width of the image, and together with FullPanoWidthPixels, it describes the horizontal FOV of content of the image: HorizontalFOV = 360 \* CroppedAreaImageWidthPixels / FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the horizontal FOV of the content of the image. HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `CroppedAreaImageHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value will NOT be equal to the actual height of the image. Instead, together with FullPanoHeightPixels, it describes the vertical FOV of the image: VerticalFOV = 180 \* CroppedAreaImageHeightPixels / FullPanoHeightPixels. In other words, this value is equal to the CroppedAreaImageHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the vertical FOV of the content of the image. VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `FullPanoWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value defines a ratio of horizontal pixels to degrees in the space of the image, and in general the pixel to degree ratio in the scope of the metadata object. Concretely, PixelsPerDegree = FullPanoWidthPixels / 360. This is also equivalent to the circumference of the cylinder used to model this projection.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It only defines the pixel to degree ratio in the scope of the metadata object. It represents the number of pixels in 360 degrees, so pixels per degree is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an example, if FullPanoWidthPixels were chosen to be 3600, we would have PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of view of 65 degrees would then have a CroppedAreaImageHeightPixels value of 65 \* 10 = 650.<br><br>Required |
| `FullPanoHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the FullPanoHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is always equal to FullPanoWidthPixels / 2.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is a second, redundant representation of PixelsPerDegree. FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent with FullPanoWidthPixels: FullPanoHeightPixels = FullPanoWidthPixels / 2.<br><br>Required |
| `CroppedAreaLeftPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaLeftPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `CroppedAreaTopPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaTopPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `PoseHeadingDegrees`<br><br>float |     |
| `PosePitchDegrees`<br><br>float |     |
| `PoseRollDegrees`<br><br>float |     |
| `InitialViewHeadingDegrees`<br><br>float |     |
| `InitialViewPitchDegrees`<br><br>float |     |
| `InitialViewRollDegrees`<br><br>float | This is not currently supported |
| `InitialViewVerticalFOVDegrees`<br><br>float | This is deprecated. Please use InitialVerticalFOVDegrees. |
| `InitialVerticalFOVDegrees`<br><br>float | You can set the intial vertical FOV of the image. You can set either this field or InitialHorizontalFOVDegrees. |
| `InitialHorizontalFOVDegrees`<br><br>float | You can set the intial horizontal FOV of the image. You can set either this field or InitialVerticalFOVDegrees. |
| `PreProcessCropLeftPixels`<br><br>int64 |     |
| `PreProcessCropRightPixels`<br><br>int64 |     |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the photo post |
| `sponsor_relationship`<br><br>int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith |
| `tags`<br><br>list<Object> | Tags on this photo |
| `x`<br><br>float | The x-axis offset for the tag |
| `y`<br><br>float | The y-axis offset for the tag |
| `tag_uid`<br><br>int | The user\_id of the tagged person |
| `tag_text`<br><br>string | Text associated with the tag |
| `target_id`<br><br>int | Don't use this. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos`. |
| `targeting`<br><br>target | Allows you to target posts to specific audiences. Applies to Pages only |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `time_since_original_post`<br><br>int64 | Same as `backdated_time` but with a time delta instead of absolute time |
| `uid`<br><br>int | Deprecated |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Content type of the unpublished content type |
| `url`<br><br>string | The URL of a photo that is already uploaded to the Internet. You must specify this or a file attachment |
| `user_selected_tags`<br><br>boolean | Default value: `false`<br><br>User selected tags |
| `vault_image_id`<br><br>numeric string or integer | A vault image ID to use for a photo. You can use only one of `url`, a file attachment, `vault_image_id`, or `sync_object_uuid` |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`post_id`: token with structure: Post ID,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 321 | Album is full |
| 100 | Invalid parameter |
| 220 | Album or albums not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 120 | Invalid album id |

You can make a POST request to `photos` edge from the following paths:

* [`/{group_id}/photos`](https://developers.facebook.com/docs/graph-api/reference/group/photos/)

When posting to this edge, a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) will be created.

### Parameters

| Parameter | Description |
| --- | --- |
| `aid`<br><br>string | Legacy album ID. Deprecated<br><br>Deprecated |
| `allow_spherical_photo`<br><br>boolean | Default value: `false`<br><br>Indicates that we should allow this photo to be treated as a spherical photo. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true. |
| `alt_text_custom`<br><br>string | Accessible alternative description for an image |
| `android_key_hash`<br><br>string | Android key hash |
| `application_id`<br><br>non-empty string | iTunes App ID. This is used by the native Share dialog that's part of iOS |
| `attempt`<br><br>int64 | Default value: `0`<br><br>Number of attempts that have been made to upload this photo |
| `audience_exp`<br><br>boolean | Default value: `false`<br><br>Audience exp |
| `backdated_time`<br><br>datetime | A user-specified creation time for this photo |
| `backdated_time_granularity`<br><br>enum{year, month, day, hour, min, none} | Default value: `none`<br><br>Use only the part of the `backdated_time` parameter to the specified granularity |
| `caption`<br><br>UTF-8 string | The description of the photo<br><br>Supports Emoji |
| `composer_session_id`<br><br>string | Composer session ID |
| `direct_share_status`<br><br>int64 | The status to allow sponsor directly boost the post |
| `feed_targeting`<br><br>feed target | Object that controls [Feed targeting](https://www.facebook.com/help/352402648173466) for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> | Values for targeted locales. Use `type` of `adlocale` to [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned key to specify. |
| `age_min`<br><br>int64 | Must be `13` or higher. Default is 0. |
| `age_max`<br><br>int64 | Maximum age. |
| `genders`<br><br>list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both. |
| `college_years`<br><br>list<int64> | Array of integers. Represent graduation years from college. |
| `education_statuses`<br><br>list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents). |
| `interested_in`<br><br>list<int64> | Deprecated. Please see the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog/breaking-changes#2-7-2018) for more information.<br><br>Deprecated |
| `relationship_statuses`<br><br>list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types. |
| `interests`<br><br>list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as [find Targeting Options](https://developers.facebook.com/docs/marketing-api/targeting-search) and use the returned id to specify. |
| `filter_type`<br><br>int64 | Default value: `-1`<br><br>Filter type |
| `full_res_is_coming_later`<br><br>boolean | Default value: `false`<br><br>Full res is coming later |
| `initial_view_heading_override_degrees`<br><br>int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_pitch_override_degrees`<br><br>int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `initial_view_vertical_fov_override_degrees`<br><br>int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter |
| `ios_bundle_id`<br><br>string | iOS Bundle ID |
| `is_explicit_location`<br><br>boolean | Is an explicit location |
| `is_explicit_place`<br><br>boolean | If set to `true`, the tag is a place, not a person |
| `manual_privacy`<br><br>boolean | Default value: `false`<br><br>Manual privacy |
| `message`<br><br>UTF-8 string | Deprecated. Please use the caption param instead<br><br>DeprecatedSupports Emoji |
| `name`<br><br>UTF-8 string | Deprecated. Please use the caption param instead<br><br>DeprecatedSupports Emoji |
| `no_story`<br><br>boolean | If set to `true`, this will suppress the Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story |
| `offline_id`<br><br>int64 | Default value: `0`<br><br>Offline ID |
| `og_action_type_id`<br><br>numeric string or integer | The Open Graph action type |
| `og_icon_id`<br><br>numeric string or integer | The Open Graph icon |
| `og_object_id`<br><br>OG object ID or URL string | The Open Graph object ID |
| `og_phrase`<br><br>string | The Open Graph phrase |
| `og_set_profile_badge`<br><br>boolean | Default value: `false`<br><br>Flag to set if the post should create a profile badge |
| `og_suggestion_mechanism`<br><br>string | The Open Graph suggestion |
| `place`<br><br>place tag | Page ID of a place associated with the photo |
| `privacy`<br><br>Privacy Parameter | Determines the privacy settings of the photo. If not supplied, this defaults to the privacy level granted to the app in the Login dialog. This field cannot be used to set a more open privacy setting than the one granted |
| `profile_id`<br><br>int | Deprecated. Use `target_id` instead<br><br>Deprecated |
| `proxied_app_id`<br><br>numeric string or integer | Proxied app ID |
| `published`<br><br>boolean | Default value: `true`<br><br>Set to `false` if you don't want the photo to be published immediately |
| `qn`<br><br>string | Photos waterfall ID |
| `scheduled_publish_time`<br><br>int64 | Time at which an unpublished post should be published (Unix ISO-8601 format). Applies to Pages only |
| `spherical_metadata`<br><br>JSON object | A set of params describing an uploaded spherical photo. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata |
| `ProjectionType`<br><br>string | Accepted values include equirectangular (full spherical photo), cylindrical (panorama), and cubestrip (also known as cubemap, e.g. for synthetic or rendered content; stacked vertically with 6 faces).<br><br>Required |
| `CroppedAreaImageWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value should be equal to the actual width of the image, and together with FullPanoWidthPixels, it describes the horizontal FOV of content of the image: HorizontalFOV = 360 \* CroppedAreaImageWidthPixels / FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the horizontal FOV of the content of the image. HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `CroppedAreaImageHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value will NOT be equal to the actual height of the image. Instead, together with FullPanoHeightPixels, it describes the vertical FOV of the image: VerticalFOV = 180 \* CroppedAreaImageHeightPixels / FullPanoHeightPixels. In other words, this value is equal to the CroppedAreaImageHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This has no relationship to the pixel dimensions of the image. It is simply a representation of the vertical FOV of the content of the image. VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>Required |
| `FullPanoWidthPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: Very similar to equirectangular. This value defines a ratio of horizontal pixels to degrees in the space of the image, and in general the pixel to degree ratio in the scope of the metadata object. Concretely, PixelsPerDegree = FullPanoWidthPixels / 360. This is also equivalent to the circumference of the cylinder used to model this projection.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It only defines the pixel to degree ratio in the scope of the metadata object. It represents the number of pixels in 360 degrees, so pixels per degree is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an example, if FullPanoWidthPixels were chosen to be 3600, we would have PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of view of 65 degrees would then have a CroppedAreaImageHeightPixels value of 65 \* 10 = 650.<br><br>Required |
| `FullPanoHeightPixels`<br><br>int64 | \--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the FullPanoHeightPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is always equal to FullPanoWidthPixels / 2.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is a second, redundant representation of PixelsPerDegree. FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent with FullPanoWidthPixels: FullPanoHeightPixels = FullPanoWidthPixels / 2.<br><br>Required |
| `CroppedAreaLeftPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaLeftPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `CroppedAreaTopPixels`<br><br>int64 | Default value: `0`<br><br>\--- In equirectangular projection: As described in Google Photo Sphere XMP Metadata spec.<br><br>\--- In cylindrical projection: This value is equal to the CroppedAreaTopPixels value that this image would have, if it were projected into equirectangular format while maintaining the same FullPanoWidthPixels. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels.<br><br>\--- In cubestrip projection: This value has no relationship to the pixel dimensions of the image. It is just a representation of the same angular offset that it represents in equirectangular projection in the Google Photo Sphere spec. AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree, where PixelsPerDegree is defined by FullPanoWidthPixels. |
| `PoseHeadingDegrees`<br><br>float |     |
| `PosePitchDegrees`<br><br>float |     |
| `PoseRollDegrees`<br><br>float |     |
| `InitialViewHeadingDegrees`<br><br>float |     |
| `InitialViewPitchDegrees`<br><br>float |     |
| `InitialViewRollDegrees`<br><br>float | This is not currently supported |
| `InitialViewVerticalFOVDegrees`<br><br>float | This is deprecated. Please use InitialVerticalFOVDegrees. |
| `InitialVerticalFOVDegrees`<br><br>float | You can set the intial vertical FOV of the image. You can set either this field or InitialHorizontalFOVDegrees. |
| `InitialHorizontalFOVDegrees`<br><br>float | You can set the intial horizontal FOV of the image. You can set either this field or InitialVerticalFOVDegrees. |
| `PreProcessCropLeftPixels`<br><br>int64 |     |
| `PreProcessCropRightPixels`<br><br>int64 |     |
| `sponsor_id`<br><br>numeric string or integer | Facebook Page id that is tagged as sponsor in the photo post |
| `sponsor_relationship`<br><br>int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith |
| `tags`<br><br>list<Object> | Tags on this photo |
| `x`<br><br>float | The x-axis offset for the tag |
| `y`<br><br>float | The y-axis offset for the tag |
| `tag_uid`<br><br>int | The user\_id of the tagged person |
| `tag_text`<br><br>string | Text associated with the tag |
| `target_id`<br><br>int | Do not use. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos` |
| `targeting`<br><br>target | Allows you to target posts to specific audiences. Applies to Pages only |
| `geo_locations`<br><br>Object |     |
| `countries`<br><br>list<string> |     |
| `regions`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `cities`<br><br>list<Object> |     |
| `key`<br><br>int64 |     |
| `zips`<br><br>list<Object> |     |
| `key`<br><br>string |     |
| `locales`<br><br>list<string> |     |
| `excluded_countries`[](#)<br><br>list<string> |     |
| `excluded_regions`[](#)<br><br>list<int64> |     |
| `excluded_cities`[](#)<br><br>list<int64> |     |
| `excluded_zipcodes`[](#)<br><br>list<string> |     |
| `timezones`[](#)<br><br>list<int64> |     |
| `age_min`<br><br>enum {13, 15, 18, 21, 25} |     |
| `time_since_original_post`<br><br>int64 | Same as `backdated_time` but with a time delta instead of absolute time |
| `uid`<br><br>int | Deprecated |
| `unpublished_content_type`<br><br>enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Content type of the unpublished content type |
| `url`<br><br>string | The URL of a photo that is already uploaded to the Internet. You must specify this or a file attachment |
| `user_selected_tags`<br><br>boolean | Default value: `false`<br><br>User selected tags |
| `vault_image_id`<br><br>numeric string or integer | A vault image ID to use for a photo. You can use only one of `url`, a file attachment, `vault_image_id`, or `sync_object_uuid` |

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node represented by `id` in the return type.

Struct {

`id`: numeric string,

`post_id`: token with structure: Post ID,

}

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 120 | Invalid album id |
| 324 | Missing or invalid image file |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

An app can delete any photos it published, or a page-management app can delete a Photo published to a page that the app manages.

### Permissions

* To delete a User's photo, a User access token with `publish_actions`[permission](https://developers.facebook.com/docs/authentication/permissions/) is required.
    
* To delete a Page's photo a Page access token and `publish_pages`[permission](https://developers.facebook.com/docs/authentication/permissions/) is required.
    
* To delete a User's photo on a Page a Page access token is required.
    

You can delete a [Photo](https://developers.facebook.com/docs/graph-api/reference/photo/) by making a DELETE request to [`/{photo_id}`](https://developers.facebook.com/docs/graph-api/reference/photo/).

### Parameters

This endpoint doesn't have any parameters.

### Return Type

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Photo Likes
===========

[](#)

Likes on a Photo

[](#)

Reading
-------

Likes for this object

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bphoto-id%7D%2Flikes&version=v18.0)

    GET /v18.0/{photo-id}/likes HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{photo-id}/likes',
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
        "/{photo-id}/likes",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{photo-id}/likes",
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
                                   initWithGraphPath:@"/{photo-id}/likes"
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

A list of [Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

#### `summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

| Field | Description |
| --- | --- |
| `total_count`<br><br>unsigned int32 | Total number of likes |
| `can_like`<br><br>bool | Can the viewer like |
| `has_liked`<br><br>bool | Has the viewer liked |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

[](#)

Creating
--------

You can make a POST request to `likes` edge from the following paths:

* [`/{photo_id}/likes`](https://developers.facebook.com/docs/graph-api/reference/photo/likes/)

When posting to this edge, no Graph object will be created.

### Parameters

This endpoint doesn't have any parameters.

### Return Type

This endpoint supports [read-after-write](https://developers.facebook.com/docs/graph-api/advanced/#read-after-write) and will read the node to which you POSTed.

Struct {

`success`: bool,

}

### Error Codes

| Error | Description |
| --- | --- |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 190 | Invalid OAuth 2.0 Access Token |
| 459 | The session is invalid because the user has been checkpointed |

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Photo Insights
==============

[](#)

Reading
-------

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bphoto-id%7D%2Finsights&version=v18.0)

    GET /v18.0/{photo-id}/insights HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{photo-id}/insights',
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
        "/{photo-id}/insights",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{photo-id}/insights",
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
                                   initWithGraphPath:@"/{photo-id}/insights"
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
| `date_preset`<br><br>enum{today, yesterday, this\_month, last\_month, this\_quarter, maximum, data\_maximum, last\_3d, last\_7d, last\_14d, last\_28d, last\_30d, last\_90d, last\_week\_mon\_sun, last\_week\_sun\_sat, last\_quarter, last\_year, this\_week\_mon\_today, this\_week\_sun\_today, this\_year} | Preset a date range, like lastweek, yesterday. If since or until presents, it does not work. |
| `metric`<br><br>list<A valid metric for an insights endpoint> | The list of metrics that needs to be fetched |
| `period`<br><br>enum{day, week, days\_28, month, lifetime, total\_over\_range} | The aggregation period |
| `since`<br><br>datetime | Lower bound of the time range to consider |
| `until`<br><br>datetime | Upper bound of the time range to consider |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [InsightsResult](https://developers.facebook.com/docs/graph-api/reference/insights-result/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 3001 | Invalid query |

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

Photo Picture
=============

[](#)

Reading
-------

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bphoto-id%7D%2Fpicture&version=v18.0)

    GET /v18.0/{photo-id}/picture HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{photo-id}/picture',
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
        "/{photo-id}/picture",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{photo-id}/picture",
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
                                   initWithGraphPath:@"/{photo-id}/picture"
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
| `redirect`<br><br>boolean | Default value: `true`<br><br>By default the picture edge will return a picture instead of a JSON response. If you want the picture edge to return JSON that describes the image set `redirect=0` when you make the request. |
| `type`<br><br>enum{thumbnail, album, normal} | The size of this picture. |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProfilePictureSource](https://developers.facebook.com/docs/graph-api/reference/profile-picture-source/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 80001 | There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting. |

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

Photo Sponsor Tags
==================

[](#)

Reading
-------

PhotoSponsorTags

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bphoto-id%7D%2Fsponsor_tags&version=v18.0)

    GET /v18.0/{photo-id}/sponsor_tags HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{photo-id}/sponsor_tags',
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
        "/{photo-id}/sponsor_tags",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{photo-id}/sponsor_tags",
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
                                   initWithGraphPath:@"/{photo-id}/sponsor_tags"
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

A list of [Page](https://developers.facebook.com/docs/graph-api/reference/page/) nodes.

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