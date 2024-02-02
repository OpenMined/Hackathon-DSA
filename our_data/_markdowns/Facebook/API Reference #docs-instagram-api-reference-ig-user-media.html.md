Media - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Media
=============

Represents a collection of IG Media objects on an IG User.

Beginning November 9, 2023, the `VIDEO` value for `media_type` will no longer be supported. Use the `REELS` media type to publish a video to your feed.

Creating
--------

**`POST /{ig-user-id}/media`**

* Create an image, carousel, story or reel IG Container for use in the post publishing process. See the Content Publishing guide for complete publishing steps.

### Limitations

#### General Limitations

* Containers expire after 24 hours.
* If the Page connected to the targeted Instagram Professional account requires Page Publishing Authorization (PPA), PPA must be completed or the request will fail.
* If the Page connected to the targeted Instagram Professional account requires two-factor authentication, the Facebook User must also have performed two-factor authentication or the request will fail.
* Publishing to Instagram TV is not supported.

#### Reels Limitations

* Reels cannot appear in album carousels.
* Account privacy settings are respected upon publish. For example, if **Allow remixing** is enabled, published reels will have remixing enabled upon publish but remixing can be disabled on published reels manually through the Instagram app.
* Music tagging is only available for original audio.

#### Story Limitations

* Stories expire after 24 hours.
* Support either video URL or Reels URL but not both.
* Publishing stickers (i.e., link, poll, location) is not supported.

### Requirements

 Type | Description || Access Tokens | User |
| Business Roles | If creating containers for product tagging, the app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | If creating containers for product tagging, the IG User must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `instagram_basic`
`instagram_content_publish`
`pages_read_engagement` or `pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you will also need one of:
`ads_management`
`business_management`
If creating containers for product tagging, you will also need:
`catalog_management`
`instagram_shopping_tag_products` |
| Tasks | The app user whose token is used in the request must be able to perform `MANAGE` or `CREATE_CONTENT` tasks on the Page connected to the targeted Instagram account. |
### Image Specifications

* Format: JPEG
* File size: 8 MB maximum.
* Aspect ratio: Must be within a 4:5 to 1.91:1 range
* Minimum width: 320 (will be scaled up to the minimum if necessary)
* Maximum width: 1440 (will be scaled down to the maximum if necessary)
* Height: Varies, depending on width and aspect ratio
* Color Space: sRGB. Images using other color spaces will have their color spaces converted to sRGB.

### Reel Specifications

The following are the specifications for Reels:

* Container: MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
* Audio codec: AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
* Video codec: HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
* Frame rate: 23-60 FPS.
* Picture size:
	+ Maximum columns (horizontal pixels): 1920
	+ Required aspect ratio is between 0.01:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space.
* Video bitrate: VBR, 25Mbps maximum
* Audio bitrate: 128kbps
* Duration: 15 mins maximum, 3 seconds minimum
* File size: 1GB maximum
The following are the specifications for a Reels cover photo:

* Format: JPEG
* File size: 8MB maximum
* Color Space: sRGB. Images that use other color spaces will be converted to sRGB.
* Aspect ratio: We recommend 9:16 to avoid cropping or blank space. If the aspect ratio of the original image is not 9:16, we crop the image and use the middle most 9:16 rectangle as the cover photo for the reel. If you share a reel to your feed, we crop the image and use the middle most 1:1 square as the cover photo for your feed post.
### Story Image Specifications

* Format: JPEG
* File size: 8 MB maximum.
* Aspect ratio: We recommended 9:16 to avoid cropping or blank space
* Color Space: sRGB. Images using other color spaces will have their color spaces converted to sRGB

### Story Video Specifications

* Container: MOV or MP4 (MPEG-4 Part 14), no edit lists, moov atom at the front of the file.
* Audio codec: AAC, 48khz sample rate maximum, 1 or 2 channels (mono or stereo).
* Video codec: HEVC or H264, progressive scan, closed GOP, 4:2:0 chroma subsampling.
* Frame rate: 23-60 FPS.
* Picture size:
	+ Maximum columns (horizontal pixels): 1920
	+ Required aspect ratio is between 0.1:1 and 10:1 but we recommend 9:16 to avoid cropping or blank space
* Video bitrate: VBR, 25Mbps maximum
* Audio bitrate: 128kbps
* Duration: 60 seconds maximum, 3 seconds minimum
* File size: 100MB maximum
### Request Syntax

#### Image Containers

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image_url={image-url}
  &is_carousel_item={is-carousel-item}
  &caption={caption}
  &location_id={location-id}
  &user_tags={user-tags}
  &product_tags={product-tags}
  &access_token={access-token}
```
#### Reel Containers

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media_type=REELS
&video_url={reel-url}
&caption={caption}
&share_to_feed={share-to-feed}
&collaborators={collaborator-usernames}
&cover_url={cover-url}
&audio_name={audio-name}
&user_tags={user-tags}
&location_id={location-id}
&thumb_offset={thumb-offset}
&share_to_feed={share-to-feed}
&access_token={access-token}
```
#### Carousel Containers

Carousel containers only. To create carousel item containers, create image or video containers instead (reels are not supported). See Carousel Posts for complete publishing steps.

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
?media_type=CAROUSEL
&caption={caption}
&share_to_feed={share-to-feed}
&collaborators={collaborator-usernames}
&location_id={location-id}
&product_tags={product-tags}
&children={children}
&access_token={access-token}
```
### Image Story Containers

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?image_url={image-url}
  &media_type=STORIES
  &access_token={access-token}
```
### Video Story Containers

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media
  ?video_url={video-url}
  &media_type=STORIES
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}`
Required | App user's app-scoped user ID. |
### Query String Parameters

 Key | Placeholder | Description || `access_token` | `{access-token}` | Required. App user's User access token. |
| `audio_name` | `{audio-name}` | **For Reels only.** Name of the audio of your Reels media. You can only rename once, either while creating a reel or after from the audio page. |
| `caption` | `{caption}` | A caption for the image, video, or carousel. Can include hashtags (example: `#crazywildebeest`) and usernames of Instagram users (example: `@natgeo`). @Mentioned Instagram users receive a notification when the container is published. Maximum 2200 characters, 30 hashtags, and 20 @ tags.
**Not supported on images or videos in carousels**. |
| `collaborators` | `{caption}` | For Feed image, Reels and Carousels only. A list of up to 3 instagram usernames as collaborators on an ig media.
**Not supported for Stories.** |
| `children` | `{children}` | **Required for carousels. Applies only to carousels**. An array of up to 10 container IDs of each image and video that should appear in the published carousel. Carousels can have up to 10 total images, vidoes, or a mix of the two. |
| `cover_url` | `{cover-url}` | For Reels only. The path to an image to use as the cover image for the Reels tab. We will cURL the image using the URL that you specify so the image must be on a public server. If you specify both `cover_url` and `thumb_offset`, we use `cover_url` and ignore `thumb_offset`. The image must conform to the specifications for a Reels cover photo. |
| `image_url` | `{image-url}` | For images only and required for images. The path to the image. We will cURL the image using the URL that you specify so the image must be on a public server. |
| `is_carousel_item` | `{is-carousel-item}` | **Applies only to images and video**. Set to `true`. Indicates image or video appears in a carousel. |
| `location_id` | `{location-id}` | The ID of a Page associated with a location that you want to tag the image or video with.
Use the Pages Search API to search for Pages whose names match a search string, then parse the results to identify any Pages that have been created for a physical location. Include the `location` field in your query and verify that the Page you want to use has location data. Attempting to create a container using a Page that has no location data will fail with coded exception `INSTAGRAM_PLATFORM_API__INVALID_LOCATION_ID`.
**Not supported on images or videos in carousels**. |
| `media_type` | `{media-type}` | **Required for carousels, stories, and reels.** Indicates container is for a carousel, story or reel. Value can be:* `CAROUSEL`
* `REELS`
* `STORIES`
 |
| `product_tags` | `{product-tags}` | **Required for product tagging. Applies only to images and videos**. An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:
* `product_id` — **Required.** Product ID.
* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.
For example:
`[{product_id:'3231775643511089',x: 0.5,y: 0.8}]` |
| `share_to_feed` | `{share-to-feed}` | For Reels only. When `true`, indicates that the reel can appear in both the **Feed** and **Reels** tabs. When `false`, indicates the reel can only appear in the **Reels** tab.
Neither value determines whether the reel actually appears in the **Reels** tab because the reel may not meet eligibilty requirements or may not be selected by our algorithm. See reel specifications for eligibility critera.
 |
| `thumb_offset` | `{thumb-offset}` | For videos and reels. Location, in milliseconds, of the video or reel frame to be used as the cover thumbnail image. The default value is `0`, which is the first frame of the video or reel. For reels, if you specify both `cover_url` and `thumb_offset`, we use `cover_url` and ignore `thumb_offset`. |
| `user_tags` | `{user-tags}` | **Required for user tagging. Applies to images and videos.** An array of public usernames and `x`/`y` coordinates for any public Instagram users who you want to tag in the image. Each object should have the following information:* `usernames` — **Required.** Public usernames.
* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.
 |
| `video_url` | `{video-url}` | **Required for videos and reels. Applies only to videos and reels.** Path to the video. We cURL the video using the passed-in URL, so it must be on a public server. |
### Response

A JSON-formatted object containing an IG Container ID which you can use to publish the container.

Video uploads are asynchronous, so receiving a container ID does not guarantee that the upload was successful. To verify that a video has been uploaded, request the `status_code` field on the IG Container. If its value is `FINISHED`, the video was uploaded successfully.

```
{
  "id":"{ig-container-id}"
}
```
### Sample Request

```
POST graph.facebook.com/17841400008460056/media
  ?image_url=https//www.example.com/images/bronzed-fonzes.jpg
  &caption=#BronzedFonzes!
  &collaborators= [‘username1’,’username2’]
  &user_tags=[
    {
      username:'kevinhart4real',
      x: 0.5,
      y: 0.8
    },
    {
      username:'therock',
      x: 0.3,
      y: 0.2
    }
  ]
```
### Sample Response

```
{
  "id": "17889455560051444"
}
```
Reading
-------

**`GET /{ig-user-id}/media`**

Get all IG Media on an IG User.

### Limitations

* Returns a maximum of 10K of the most recently created media.
* Story IG Media not supported, use the `GET /{ig-user-id}/stories` endpoint instead.

### Requirements

 Type | Description || Access Tokens | User |
| Permissions | `instagram_basic`
`pages_read_engagement` or `pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you will also need one of:
`ads_management`
`business_management` |
### Time-based Pagination

This endpoint supports time-based pagination. Include `since` and `until` query-string parameters with Unix timestamp or `strtotime` data values to define a time range.

### Sample Request

```
GET graph.facebook.com/17841405822304914/media
```
### Sample Response

```
{
  "data": [
    {
      "id": "17895695668004550"
    },
    {
      "id": "17899305451014820"
    },
    {
      "id": "17896450804038745"
    },
    {
      "id": "17881042411086627"
    },
    {
      "id": "17869102915168123"
    }
  ]
}
```
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.