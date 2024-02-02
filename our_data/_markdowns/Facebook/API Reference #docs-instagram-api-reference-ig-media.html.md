IG Media - Instagram Platform - Documentation - Meta for Developers

Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG Media
========

Represents an Instagram album, photo, or video (uploaded video, live video, video created with the Instagram TV app, reel, or story).

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-media-id}`**

Gets fields and edges on IG media.

### Limitations

* Fields that return aggregated values don't include ads-driven data. For example, `comments_count` counts comments on a photo, but not comments on ads that contain that photo.
* Captions don't include the `@` symbol unless the app user is also able to perform Admin-equivalent tasks on the app.
* Some fields, such as `permalink`, cannot be used on photos within albums (children).
* Instagram TV media must be shared to Instagram at the time of publish (**Post a Preview** or **Share Preview to Feed** enabled) in order to be accessible via the API.
* Live video IG Media can only be read while they are being broadcast.

### Requirements

 Type | Description || Access Tokens | User. |
| Permissions | `instagram_basic`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you also need one of the following:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-media-id}
  ?fields={fields}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's user access token. |
| `fields` | `{fields}` | Comma-separated list of fields you want returned. |
### Fields

Public fields can be read via field expansion.

 Field | Description || `caption`
Public | Caption. Excludes album children. The `@` symbol is excluded, unless the app user can perform admin-equivalent tasks on the Facebook Page connected to the Instagram account used to create the caption. |
| `comments_count`
Public | Count of comments on the media. Excludes comments on album child media and the media's caption. Includes replies on comments. |
| `copyright_check_information.status` | Returns `status` and `matches_found` objects

 status objects | Description || `status` | * `completed` – the detection process has finished
* `error` – an error occurred during the detection process
* `in_progress` – the detection process is ongoing
* `not_started` – the detection process has not started
 |
| `matches_found` | Set to one of the following:* `false` if the video **does not violate** copyright,
* `true` if the video **does violate** copyright
 |
If a video **is violating copyright**, the `copyright_matches` is returned with an array of objects about the copyrighted material, when the violation is occurring in the video, and the actions take to mitigate the violation.

 copyright\_matches objects | Description || `author` | the author of the copyrighted video |
| `content_title` | the name of the copyrighted video |
| `matched_segments` | An array of objects with the following key-value pairs:
\* `duration_in_seconds` – the number of seconds the content violates copyright
\* `segment_type` – either `AUDIO` or `VIDEO`
\* `start_time_in_seconds` – set to the start time of the video |
| `owner_copyright_policy` | Objects returned include:* `name` – The name for the copyright owners' policy
* `actions` – An array of `action` objects with the mitigations steps taken defined by the copyright owner's policy. May include different mitigations steps for different locations.
	+ `action` – The mitigation action taken against the video violating copyright. Different mitigation steps can be taken for different countries. Can be one of the following values:
		- `BLOCK` – The video is blocked from the audiences listed in the `geos` array
		- `MUTE` - The video is muted for audiences listed in the `geos` array
 |
 |
| `id`
Public | Media ID. |
| `ig_id`
Public | Instagram media ID. Used with Legacy Instagram API, now deprecated. Use `id` instead. |
| `is_comment_enabled` | Indicates if comments are enabled or disabled. Excludes album children. |
| `is_shared_to_feed`
Public | For Reels only. When `true`, indicates that the reel can appear in both the **Feed** and **Reels** tabs. When `false`, indicates that the reel can only appear in the **Reels** tab.
Neither value determines whether the reel actually appears in the **Reels** tab because the reel may not meet eligibilty requirements or may not be selected by our algorithm. See reel specifications for eligibility critera.
 |
| `like_count` | Count of likes on the media, including replies on comments. Excludes likes on album child media and likes on promoted posts created from the media.
If queried indirectly through another endpoint or field expansion:
* **v10.0 and older calls:** The value is `0` if the media owner has hidden like counts.
* **v11.0+ calls:** The `like_count` field is omitted if the media owner has hidden like counts.
 |
| `media_product_type`
Public | Surface where the media is published. Can be `AD`, `FEED`, `STORY` or `REELS`. |
| `media_type`
Public | Media type. Can be `CAROUSEL_ALBUM`, `IMAGE`, or `VIDEO`. |
| `media_url`
Public | The URL for the media.
The `media_url` field is omitted from responses if the media contains copyrighted material or has been flagged for a copyright violation. Examples of copyrighted material can include audio on reels.
 |
| `owner`
Public | Instagram user ID who created the media. Only returned if the app user making the query also created the media; otherwise, `username` field is returned instead. |
| `permalink`
Public | Permanent URL to the media. |
| `shortcode`
Public | Shortcode to the media. |
| `thumbnail_url`
Public | Media thumbnail URL. Only available on `VIDEO` media. |
| `timestamp`
Public | ISO 8601-formatted creation date in UTC (default is UTC ±00:00). |
| `username`
Public | Username of user who created the media. |
| `video_title`
Public | Deprecated. Omitted from response. |
### Edges

Public edges can be returned through field expansion.

 Edge | Description || `children`
Public. | Represents a collection of IG Media objects on an album IG Media. |
| `collaborators` | Represents a list of users who are added as collaborators on an IG Media object. |
| `comments` | Represents a collection of IG Comments on an IG Media object. |
| `insights` | Represents social interaction metrics on an IG Media object. |
### cURL Example

#### Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17895695668004550?fields=id,media_type,media_url,owner,timestamp&access_token=IGQVJ...'
```
#### Response

```
{
  "id": "17918920912340654",
  "media_type": "IMAGE",
  "media_url": "https://sconten...",
  "owner": {
    "id": "17841405309211844"
  },
  "timestamp": "2019-09-26T22:36:43+0000"
}
```
Updating
--------

**`POST /{ig-media-id}`**

Enable or disable comments on an IG Media.

### Limitations

Live video IG Media not supported.

### Requirements

 Type | Description || Access Tokens | User. |
| Permissions | `instagram_basic`
`instagram_manage_comments`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you also need one of the following:
`ads_management`
`business_management` |
### Request Syntax

```
POST https://graph.facebook.com/{api-version}/{ig-media-id}
  ?comment_enabled={comment-enabled}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's user access token. |
| `comment_enabled` | `{comment-enabled}` | **Required.** Set to `true` to enable comments or `false` to disable comments. |
### cURL Example

#### Request

```
curl -i -X POST \
 "https://graph.facebook.com/v19.0/17918920912340654?comment_enabled=true&access_token=EAAOc..."
```
#### Response

```
{
  "success": true
}
```
Deleting
--------

This operation is not supported.