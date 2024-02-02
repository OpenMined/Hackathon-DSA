Graph API Photo Node














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
		- Object Comments
		- Insights
		- Likes
		- Picture
		- Sponsor Tags
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
On This PagePhotoReadingPermissionsNew Page ExperienceFeature PermissionsExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingDeletingPermissionsParametersReturn TypeError CodesGraph API Versionv18.0Photo
=====

Represents an individual photo on Facebook.

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

This endpoint is supported for New Page Experience.### Feature Permissions



| Name | Description |
| --- | --- |
| Page Public Content Access | This feature permission may be required. |

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v18.0/{photo-id} HTTP/1.1
Host: graph.facebook.com
```

```
/\* PHP SDK v5.0.0 \*/
/\* make the API call \*/
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
/\* handle the result \*/
```

```
/\* make the API call \*/
FB.api(
 "/{photo-id}",
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
 "/{photo-id}",
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
 initWithGraphPath:@"/{photo-id}"
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
| `id`numeric string | The photo ID
 |
| `album`Album | The album this photo is in
 |
| `alt_text`string | Accessible alternative description for an image
 |
| `alt_text_custom`string | User provided accessible alternative description for an image
 |
| `backdated_time`datetime | A user-specified time for when this object was created
 |
| `backdated_time_granularity`enum | How accurate the backdated time is
 |
| `can_backdate`bool | Indicates whether the viewer can backdate the photo
 |
| `can_delete`bool | Indicates whether the viewer can delete the photo
 |
| `can_tag`bool | Indicates whether the viewer can tag the photo
 |
| `created_time`datetime | The time this photo was published
Default |
| `event`Event | If this object has a place, the event associated with the place
 |
| `from`User|Page | The profile (user or page) that uploaded this photo
 |
| `height`unsigned int32 | The height of this photo in pixels
 |
| `icon`string | The icon that Facebook displays when photos are published to News Feed
 |
| `images`list<PlatformImageSource> | The different stored representations of the photo. Can vary in number based upon the size of the original photo.
 |
| `link`string | A link to the photo on Facebook
 |
| `name`string | The user-provided caption given to this photo. Corresponds to `caption` when creating photos
Default |
| `name_tags`list<EntityAtTextRange> | An array containing an array of objects mentioned in the name field which contain the id, name, and type of each object as well as the offset and length which can be used to match it up with its corresponding string in the name field
 |
| `page_story_id`string | ID of the page story this corresponds to. May not be on all photos. Applies only to published photos
 |
| `place`Place | Place info
 |
| `position`unsigned int32 | Deprecated. Returns 0
Deprecated |
| `source`string | Deprecated. Use `images` instead
Deprecated |
| `target`Profile | The target this photo is published to
 |
| `updated_time`datetime | The last time the photo was updated
 |
| `webp_images`list<PlatformImageSource> | The different stored representations of the photo in webp format. Can vary in number based upon the size of the original photo.
 |
| `width`unsigned int32 | The width of this photo in pixels
 |

### Edges



| Edge | Description |
| --- | --- |
| `insights` | Insights data
 |
| `likes` | People who like this
 |
| `picture` | Link to the 100px wide representation of this photo
 |
| `sponsor_tags` | Sponsor pages tagged in the photo.
 |

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

Creating
--------

Animated photos are not supported, and a photo must be less than 10MB in size.


Note: the `post_id` value is not returned for photos added to Albums.

You can make a POST request to `photos` edge from the following paths: * `/{album_id}/photos`

When posting to this edge, a Photo will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `aid`string | Legacy album ID. Deprecated
Deprecated |
| `allow_spherical_photo`boolean | Default value: `false`Indicates that we should allow this photo to be treated as a spherical photo. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true.
 |
| `alt_text_custom`string | Accessible alternative description for an image
 |
| `android_key_hash`string | Android key hash
 |
| `application_id`non-empty string | iTunes App ID. This is used by the native Share dialog that's part of iOS
 |
| `attempt`int64 | Default value: `0`Number of attempts that have been made to upload this photo
 |
| `audience_exp`boolean | Default value: `false`Audience exp
 |
| `backdated_time`datetime | A user-specified creation time for this photo
 |
| `backdated_time_granularity`enum{year, month, day, hour, min, none} | Default value: `none`Use only the part of the `backdated_time` parameter to the specified granularity
 |
| `caption`UTF-8 string | The description of the photo
Supports Emoji |
| `composer_session_id`string | Composer session ID
 |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post.
 |
| `feed_targeting`feed target | Object that controls News Feed targeting for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only.
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> | Values for targeted locales. Use `type` of `adlocale` to find Targeting Options and use the returned key to specify.
 |
| `age_min`int64 | Must be `13` or higher. Default is 0.
 |
| `age_max`int64 | Maximum age.
 |
| `genders`list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both.
 |
| `college_years`list<int64> | Array of integers. Represent graduation years from college.
 |
| `education_statuses`list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents).
 |
| `interested_in`list<int64> | Deprecated. Please see the Graph API Changelog for more information.
Deprecated |
| `relationship_statuses`list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types.
 |
| `interests`list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as find Targeting Options and use the returned id to specify.
 |
| `filter_type`int64 | Default value: `-1`Unused?
 |
| `full_res_is_coming_later`boolean | Default value: `false`Full res is coming later
 |
| `initial_view_heading_override_degrees`int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `initial_view_pitch_override_degrees`int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `initial_view_vertical_fov_override_degrees`int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `ios_bundle_id`string | iOS Bundle ID
 |
| `is_explicit_location`boolean | Is this an explicit location?
 |
| `is_explicit_place`boolean | If set to `true`, the tag is a place, not a person
 |
| `manual_privacy`boolean | Default value: `false`Manual privacy
 |
| `message`UTF-8 string | Deprecated. Please use the caption param instead.
DeprecatedSupports Emoji |
| `name`UTF-8 string | Deprecated. Please use the caption param instead.
DeprecatedSupports Emoji |
| `no_story`boolean | If set to `true`, this will suppress the News Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story
 |
| `offline_id`int64 | Default value: `0`Offline ID
 |
| `og_action_type_id`numeric string or integer | The Open Graph action type
 |
| `og_icon_id`numeric string or integer | The Open Graph icon
 |
| `og_object_id`OG object ID or URL string | The Open Graph object ID
 |
| `og_phrase`string | The Open Graph phrase
 |
| `og_set_profile_badge`boolean | Default value: `false`Flag to set if the post should create a profile badge
 |
| `og_suggestion_mechanism`string | The Open Graph suggestion
 |
| `place`place tag | Page ID of a place associated with the photo
 |
| `privacy`Privacy Parameter | Determines the privacy settings of the photo. If not supplied, this defaults to the privacy level granted to the app in the Login dialog. This field cannot be used to set a more open privacy setting than the one granted
 |
| `profile_id`int | Deprecated. Use `target_id` instead
Deprecated |
| `proxied_app_id`numeric string or integer | Proxied app ID
 |
| `published`boolean | Default value: `true`Set to `false` if you don't want the photo to be published immediately
 |
| `qn`string | Photos waterfall ID
 |
| `scheduled_publish_time`int64 | Time at which an unpublished post should be published (Unix ISO-8601 format). Applies to Pages only
 |
| `spherical_metadata`JSON object | A set of params describing an uploaded spherical photo. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata
 |
| `ProjectionType`string | Accepted values include equirectangular (full spherical photo),
 cylindrical (panorama), and cubestrip (also known as cubemap, e.g.
 for synthetic or rendered content; stacked vertically with 6 faces).
Required |
| `CroppedAreaImageWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to equirectangular.
 This value should be equal to the actual width of the image, and
 together with FullPanoWidthPixels, it describes the horizontal FOV
 of content of the image: HorizontalFOV = 360 \*
 CroppedAreaImageWidthPixels / FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 horizontal FOV of the content of the image.
 HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `CroppedAreaImageHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value will NOT be equal to
 the actual height of the image. Instead, together with
 FullPanoHeightPixels, it describes the vertical FOV of the image:
 VerticalFOV = 180 \* CroppedAreaImageHeightPixels /
 FullPanoHeightPixels. In other words, this value is equal to the
 CroppedAreaImageHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 vertical FOV of the content of the image.
 VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `FullPanoWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to
 equirectangular. This value defines a ratio of horizontal pixels to
 degrees in the space of the image, and in general the pixel to degree
 ratio in the scope of the metadata object. Concretely, PixelsPerDegree =
 FullPanoWidthPixels / 360. This is also equivalent to the
 circumference of the cylinder used to model this projection.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It only defines
 the pixel to degree ratio in the scope of the metadata object. It
 represents the number of pixels in 360 degrees, so pixels per degree
 is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an
 example, if FullPanoWidthPixels were chosen to be 3600, we would have
 PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of
 view of 65 degrees would then have a CroppedAreaImageHeightPixels value
 of 65 \* 10 = 650.
Required |
| `FullPanoHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the FullPanoHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is always equal to
 FullPanoWidthPixels / 2.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is a second,
 redundant representation of PixelsPerDegree.
 FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent
 with FullPanoWidthPixels:
 FullPanoHeightPixels = FullPanoWidthPixels / 2.
Required |
| `CroppedAreaLeftPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaLeftPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `CroppedAreaTopPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaTopPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `PoseHeadingDegrees`float |  |
| `PosePitchDegrees`float |  |
| `PoseRollDegrees`float |  |
| `InitialViewHeadingDegrees`float |  |
| `InitialViewPitchDegrees`float |  |
| `InitialViewRollDegrees`float | This is not currently supported
 |
| `InitialViewVerticalFOVDegrees`float | This is deprecated. Please use InitialVerticalFOVDegrees.
 |
| `InitialVerticalFOVDegrees`float | You can set the intial vertical FOV of the image. You can set either
 this field or InitialHorizontalFOVDegrees.
 |
| `InitialHorizontalFOVDegrees`float | You can set the intial horizontal FOV of the image. You can set either
 this field or InitialVerticalFOVDegrees.
 |
| `PreProcessCropLeftPixels`int64 |  |
| `PreProcessCropRightPixels`int64 |  |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the photo post
 |
| `sponsor_relationship`int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith
 |
| `tags`list<Object> | Tags on this photo
 |
| `x`float | The x-axis offset for the tag
 |
| `y`float | The y-axis offset for the tag
 |
| `tag_uid`int | The user\_id of the tagged person
 |
| `tag_text`string | Text associated with the tag
 |
| `target_id`int | Don't use this. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos`.
 |
| `targeting`target | Allows you to target posts to specific audiences. Applies to Pages only
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> |  |
| `excluded_countries`list<string> |  |
| `excluded_regions`list<int64> |  |
| `excluded_cities`list<int64> |  |
| `excluded_zipcodes`list<string> |  |
| `timezones`list<int64> |  |
| `age_min`enum {13, 15, 18, 21, 25} |  |
| `time_since_original_post`int64 | Same as `backdated_time` but with a time delta instead of absolute time
 |
| `uid`int | Deprecated
 |
| `unpublished_content_type`enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Content type of the unpublished content type
 |
| `url`string | The URL of a photo that is already uploaded to the Internet. You must specify this or a file attachment
 |
| `user_selected_tags`boolean | Default value: `false`User selected tags
 |
| `vault_image_id`numeric string or integer | A vault image ID to use for a photo. You can use only one of `url`, a file attachment, `vault_image_id`, or `sync_object_uuid`
 |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `post_id`: token with structure: Post ID, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 321 | Album is full |
| 100 | Invalid parameter |
| 220 | Album or albums not visible |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 120 | Invalid album id |

You can make a POST request to `photos` edge from the following paths: * `/{group_id}/photos`

When posting to this edge, a Photo will be created.### Parameters



| Parameter | Description |
| --- | --- |
| `aid`string | Legacy album ID. Deprecated
Deprecated |
| `allow_spherical_photo`boolean | Default value: `false`Indicates that we should allow this photo to be treated as a spherical photo. This will not change the behavior unless the server is able to interpret the photo as spherical, such as via Photosphere XMP metadata. Regular non-spherical photos will still be treated as regular photos even if this parameter is true.
 |
| `alt_text_custom`string | Accessible alternative description for an image
 |
| `android_key_hash`string | Android key hash
 |
| `application_id`non-empty string | iTunes App ID. This is used by the native Share dialog that's part of iOS
 |
| `attempt`int64 | Default value: `0`Number of attempts that have been made to upload this photo
 |
| `audience_exp`boolean | Default value: `false`Audience exp
 |
| `backdated_time`datetime | A user-specified creation time for this photo
 |
| `backdated_time_granularity`enum{year, month, day, hour, min, none} | Default value: `none`Use only the part of the `backdated_time` parameter to the specified granularity
 |
| `caption`UTF-8 string | The description of the photo
Supports Emoji |
| `composer_session_id`string | Composer session ID
 |
| `direct_share_status`int64 | The status to allow sponsor directly boost the post
 |
| `feed_targeting`feed target | Object that controls Feed targeting for this post. Anyone in these groups will be more likely to see this post. People not in these groups will be less likely to see this post, but may still see it anyway. Any of the targeting fields shown here can be used, but none are required. `feed_targeting` applies to Pages only
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> | Values for targeted locales. Use `type` of `adlocale` to find Targeting Options and use the returned key to specify.
 |
| `age_min`int64 | Must be `13` or higher. Default is 0.
 |
| `age_max`int64 | Maximum age.
 |
| `genders`list<int64> | Target specific genders. `1` targets all male viewers and `2` females. Default is to target both.
 |
| `college_years`list<int64> | Array of integers. Represent graduation years from college.
 |
| `education_statuses`list<int64> | Array of integers which represent current educational status. Use `1` for high school, `2` for undergraduate, and `3` for alum (or localized equivalents).
 |
| `interested_in`list<int64> | Deprecated. Please see the Graph API Changelog for more information.
Deprecated |
| `relationship_statuses`list<int64> | Array of integers for targeting based on relationship status. Use `1` for single, `2` for 'in a relationship', `3` for married, and `4` for engaged. Default is all types.
 |
| `interests`list<int64> | One or more IDs of pages to target fans of pages.Use `type` of `page` to get possible IDs as find Targeting Options and use the returned id to specify.
 |
| `filter_type`int64 | Default value: `-1`Filter type
 |
| `full_res_is_coming_later`boolean | Default value: `false`Full res is coming later
 |
| `initial_view_heading_override_degrees`int64 | Manually specify the initial view heading in degrees from 0 to 360. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `initial_view_pitch_override_degrees`int64 | Manually specify the initial view pitch in degrees from -90 to 90. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `initial_view_vertical_fov_override_degrees`int64 | Manually specify the initial view vertical FOV in degrees from 60 to 120. This overrides any value present in the photo embedded metadata or provided in the spherical\_metadata parameter
 |
| `ios_bundle_id`string | iOS Bundle ID
 |
| `is_explicit_location`boolean | Is an explicit location
 |
| `is_explicit_place`boolean | If set to `true`, the tag is a place, not a person
 |
| `manual_privacy`boolean | Default value: `false`Manual privacy
 |
| `message`UTF-8 string | Deprecated. Please use the caption param instead
DeprecatedSupports Emoji |
| `name`UTF-8 string | Deprecated. Please use the caption param instead
DeprecatedSupports Emoji |
| `no_story`boolean | If set to `true`, this will suppress the Feed story that is automatically generated on a profile when people upload a photo using your app. Useful for adding old photos where you may not want to generate a story
 |
| `offline_id`int64 | Default value: `0`Offline ID
 |
| `og_action_type_id`numeric string or integer | The Open Graph action type
 |
| `og_icon_id`numeric string or integer | The Open Graph icon
 |
| `og_object_id`OG object ID or URL string | The Open Graph object ID
 |
| `og_phrase`string | The Open Graph phrase
 |
| `og_set_profile_badge`boolean | Default value: `false`Flag to set if the post should create a profile badge
 |
| `og_suggestion_mechanism`string | The Open Graph suggestion
 |
| `place`place tag | Page ID of a place associated with the photo
 |
| `privacy`Privacy Parameter | Determines the privacy settings of the photo. If not supplied, this defaults to the privacy level granted to the app in the Login dialog. This field cannot be used to set a more open privacy setting than the one granted
 |
| `profile_id`int | Deprecated. Use `target_id` instead
Deprecated |
| `proxied_app_id`numeric string or integer | Proxied app ID
 |
| `published`boolean | Default value: `true`Set to `false` if you don't want the photo to be published immediately
 |
| `qn`string | Photos waterfall ID
 |
| `scheduled_publish_time`int64 | Time at which an unpublished post should be published (Unix ISO-8601 format). Applies to Pages only
 |
| `spherical_metadata`JSON object | A set of params describing an uploaded spherical photo. This field is not required; if it is not present we will try to generate spherical metadata from the metadata embedded in the image. If it is present, it takes precedence over any embedded metadata. Please click to the left to expand this list and see more information on each parameter. See also the Google Photo Sphere spec for more info on the meaning of the params: https://developers.google.com/streetview/spherical-metadata
 |
| `ProjectionType`string | Accepted values include equirectangular (full spherical photo),
 cylindrical (panorama), and cubestrip (also known as cubemap, e.g.
 for synthetic or rendered content; stacked vertically with 6 faces).
Required |
| `CroppedAreaImageWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to equirectangular.
 This value should be equal to the actual width of the image, and
 together with FullPanoWidthPixels, it describes the horizontal FOV
 of content of the image: HorizontalFOV = 360 \*
 CroppedAreaImageWidthPixels / FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 horizontal FOV of the content of the image.
 HorizontalFOV = CroppedAreaImageWidthPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `CroppedAreaImageHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value will NOT be equal to
 the actual height of the image. Instead, together with
 FullPanoHeightPixels, it describes the vertical FOV of the image:
 VerticalFOV = 180 \* CroppedAreaImageHeightPixels /
 FullPanoHeightPixels. In other words, this value is equal to the
 CroppedAreaImageHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels.
--- In cubestrip projection: This has no relationship to the pixel
 dimensions of the image. It is simply a representation of the
 vertical FOV of the content of the image.
 VerticalFOV = CroppedAreaImageHeightPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
Required |
| `FullPanoWidthPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: Very similar to
 equirectangular. This value defines a ratio of horizontal pixels to
 degrees in the space of the image, and in general the pixel to degree
 ratio in the scope of the metadata object. Concretely, PixelsPerDegree =
 FullPanoWidthPixels / 360. This is also equivalent to the
 circumference of the cylinder used to model this projection.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It only defines
 the pixel to degree ratio in the scope of the metadata object. It
 represents the number of pixels in 360 degrees, so pixels per degree
 is then given by: PixelsPerDegree = FullPanoWidthPixels / 360. As an
 example, if FullPanoWidthPixels were chosen to be 3600, we would have
 PixelsPerDegree = 3600 / 360 = 10. An image with a vertical field of
 view of 65 degrees would then have a CroppedAreaImageHeightPixels value
 of 65 \* 10 = 650.
Required |
| `FullPanoHeightPixels`int64 | --- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the FullPanoHeightPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is always equal to
 FullPanoWidthPixels / 2.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is a second,
 redundant representation of PixelsPerDegree.
 FullPanoHeightPixels = 180 \* PixelsPerDegree. It must be consistent
 with FullPanoWidthPixels:
 FullPanoHeightPixels = FullPanoWidthPixels / 2.
Required |
| `CroppedAreaLeftPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaLeftPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromLeftDegrees = CroppedAreaLeftPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `CroppedAreaTopPixels`int64 | Default value: `0`--- In equirectangular projection: As described in Google Photo Sphere
 XMP Metadata spec.
--- In cylindrical projection: This value is equal
 to the CroppedAreaTopPixels value that this image would have, if it
 were projected into equirectangular format while maintaining the
 same FullPanoWidthPixels. It is just a representation of the same
 angular offset that it represents in equirectangular projection in the
 Google Photo Sphere spec.
 Concretely, AngularOffsetFromTopDegrees = CroppedAreaTopPixels /
 PixelsPerDegree, where PixelsPerDegree is defined by
 FullPanoWidthPixels.
--- In cubestrip projection: This value has
 no relationship to the pixel dimensions of the image. It is just a
 representation of the same angular offset that it represents in
 equirectangular projection in the Google Photo Sphere spec.
 AngularOffsetFromTopDegrees = CroppedAreaTopPixels / PixelsPerDegree,
 where PixelsPerDegree is defined by FullPanoWidthPixels.
 |
| `PoseHeadingDegrees`float |  |
| `PosePitchDegrees`float |  |
| `PoseRollDegrees`float |  |
| `InitialViewHeadingDegrees`float |  |
| `InitialViewPitchDegrees`float |  |
| `InitialViewRollDegrees`float | This is not currently supported
 |
| `InitialViewVerticalFOVDegrees`float | This is deprecated. Please use InitialVerticalFOVDegrees.
 |
| `InitialVerticalFOVDegrees`float | You can set the intial vertical FOV of the image. You can set either
 this field or InitialHorizontalFOVDegrees.
 |
| `InitialHorizontalFOVDegrees`float | You can set the intial horizontal FOV of the image. You can set either
 this field or InitialVerticalFOVDegrees.
 |
| `PreProcessCropLeftPixels`int64 |  |
| `PreProcessCropRightPixels`int64 |  |
| `sponsor_id`numeric string or integer | Facebook Page id that is tagged as sponsor in the photo post
 |
| `sponsor_relationship`int64 | Sponsor Relationship, such as Presented By or Paid PartnershipWith
 |
| `tags`list<Object> | Tags on this photo
 |
| `x`float | The x-axis offset for the tag
 |
| `y`float | The y-axis offset for the tag
 |
| `tag_uid`int | The user\_id of the tagged person
 |
| `tag_text`string | Text associated with the tag
 |
| `target_id`int | Do not use. Specifying a `target_id` allows you to post the photo to an object that's not the user in the access token. It only works when posting directly to the `/photos` endpoint. Instead of using this parameter you should be using the edge on an object directly, like `/page/photos`
 |
| `targeting`target | Allows you to target posts to specific audiences. Applies to Pages only
 |
| `geo_locations`Object |  |
| `countries`list<string> |  |
| `regions`list<Object> |  |
| `key`int64 |  |
| `cities`list<Object> |  |
| `key`int64 |  |
| `zips`list<Object> |  |
| `key`string |  |
| `locales`list<string> |  |
| `excluded_countries`list<string> |  |
| `excluded_regions`list<int64> |  |
| `excluded_cities`list<int64> |  |
| `excluded_zipcodes`list<string> |  |
| `timezones`list<int64> |  |
| `age_min`enum {13, 15, 18, 21, 25} |  |
| `time_since_original_post`int64 | Same as `backdated_time` but with a time delta instead of absolute time
 |
| `uid`int | Deprecated
 |
| `unpublished_content_type`enum {SCHEDULED, SCHEDULED\_RECURRING, DRAFT, ADS\_POST, INLINE\_CREATED, PUBLISHED, REVIEWABLE\_BRANDED\_CONTENT} | Content type of the unpublished content type
 |
| `url`string | The URL of a photo that is already uploaded to the Internet. You must specify this or a file attachment
 |
| `user_selected_tags`boolean | Default value: `false`User selected tags
 |
| `vault_image_id`numeric string or integer | A vault image ID to use for a photo. You can use only one of `url`, a file attachment, `vault_image_id`, or `sync_object_uuid`
 |

### Return Type

This endpoint supports read-after-write and will read the node represented by `id` in the return type. Struct {`id`: numeric string, `post_id`: token with structure: Post ID, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |
| 368 | The action attempted has been deemed abusive or is otherwise disallowed |
| 190 | Invalid OAuth 2.0 Access Token |
| 120 | Invalid album id |
| 324 | Missing or invalid image file |

Updating
--------

You can't perform this operation on this endpoint.Deleting
--------

An app can delete any photos it published, or a page-management app can delete a Photo published to a page that the app manages.

### Permissions

* To delete a User's photo, a User access token with `publish_actions`permission is required.
* To delete a Page's photo a Page access token and `publish_pages`permission is required.
* To delete a User's photo on a Page a Page access token is required.
You can delete a Photo by making a DELETE request to `/{photo_id}`.### Parameters

This endpoint doesn't have any parameters.### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
| 190 | Invalid OAuth 2.0 Access Token |

On This PagePhotoReadingPermissionsNew Page ExperienceFeature PermissionsExampleParametersFieldsEdgesError CodesCreatingParametersReturn TypeError CodesUpdatingDeletingPermissionsParametersReturn TypeError CodesFollow Us* 
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