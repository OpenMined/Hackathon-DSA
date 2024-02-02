<div>

<div>

::: _57-c
+-----------------------------------+-----------------------------------+
| Parameter                         | Description                       |
+===================================+===================================+
|                                   | <div>                             |
| ` au                              |                                   |
| dio_story_wave_animation_handle ` | <div>                             |
|                                   |                                   |
| string                            | Everstore handle of wave          |
|                                   | animation used to burn audio      |
|                                   | story video                       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| enum {BEAUTY_FASHION, BUSINESS,   | <div>                             |
| CARS_TRUCKS, COMEDY,              |                                   |
| CUTE_ANIMALS, ENTERTAINMENT,      | <div>                             |
| FAMILY, FOOD_HEALTH, HOME,        |                                   |
| LIFESTYLE, MUSIC, NEWS, POLITICS, | Content category of this video.   |
| SCIENCE, SPORTS, TECHNOLOGY,      |                                   |
| VIDEO_GAMING, OTHER}              | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` description `                   | <div>                             |
|                                   |                                   |
| UTF-8 string                      | <div>                             |
|                                   |                                   |
|                                   | ``` {.prettyprint .prettyprinted} |
|                                   |                                   |
|                                   | The text describing a post that m |
|                                   | ay be shown in a story about it.  |
|                                   | It may include rich text informat |
|                                   | ion, such as entities and emojis. |
|                                   | ```                               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | [ Supports Emoji ]{._1vet}        |
+-----------------------------------+-----------------------------------+
| ` direct_share_status `           | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | The status to allow sponsor       |
|                                   | directly boost the post.          |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Whether the video is embeddable.  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| int64                             |                                   |
+-----------------------------------+-----------------------------------+
| int64                             | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | The size of the entire video file |
|                                   | in bytes.                         |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` file_url `                      | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | Accessible URL of a video file.   |
|                                   | Cannot be used with               |
|                                   | ` upload_phase ` .                |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` fisheye_video_cropped `         | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | Whether the single fisheye video  |
|                                   | is cropped or not                 |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` fov `                           | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | 360 video only: Vertical field of |
|                                   | view                              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` front_z_rotation `              | <div>                             |
|                                   |                                   |
| float                             | <div>                             |
|                                   |                                   |
|                                   | The front z rotation in degrees   |
|                                   | on the single fisheye video       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` guide `                         | <div>                             |
|                                   |                                   |
| list\<list\<int64\>\>             | <div>                             |
|                                   |                                   |
|                                   | 360 video only: Guide keyframes   |
|                                   | data. An array of keyframes, each |
|                                   | of which is an array of 3 or 4    |
|                                   | elements in the following order:  |
|                                   | \[video timestamp (seconds),      |
|                                   | pitch (degrees, -90 \~ 90), yaw   |
|                                   | (degrees, -180 \~ 180), field of  |
|                                   | view (degrees, 40 \~ 90,          |
|                                   | optional)\], ordered by video     |
|                                   | timestamp in strictly ascending   |
|                                   | order.                            |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` guide_enabled `                 | <div>                             |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | 360 video only: Whether Guide is  |
|                                   | active.                           |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` initial_heading `               | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | 360 video only: Horizontal camera |
|                                   | perspective to display when the   |
|                                   | video begins.                     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` initial_pitch `                 | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | 360 video only: Vertical camera   |
|                                   | perspective to display when the   |
|                                   | video begins.                     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | is_voice_clip, used to indicate   |
|                                   | that if a video is used as audio  |
|                                   | record                            |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` no_story `                      | Default value: ` false `          |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | If set to ` true ` , this will    |
|                                   | suppress feed and timeline story. |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` original_fov `                  | <div>                             |
|                                   |                                   |
| int64                             | <div>                             |
|                                   |                                   |
|                                   | Original field of view of the     |
|                                   | source camera                     |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| enum {equirectangular, cubemap,   | <div>                             |
| half_equirectangular}             |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | 360 video only: The original      |
|                                   | projection type of the 360 video  |
|                                   | being uploaded.                   |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| enum {enabled, disabled}          | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Whether the post should appear in |
|                                   | RedSpace.                         |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` privacy `                       | <div>                             |
|                                   |                                   |
| Privacy Parameter                 | <div>                             |
|                                   |                                   |
|                                   | Determines the [privacy           |
|                                   | settings](/docs/graph-ap          |
|                                   | i/common-scenarios#privacy-param) |
|                                   | of the video. If not supplied,    |
|                                   | this defaults to the privacy      |
|                                   | level granted to the app in the   |
|                                   | Login Dialog. This field cannot   |
|                                   | be used to set a more open        |
|                                   | privacy setting than the one      |
|                                   | granted.                          |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| string                            | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | The prompt id in prompts or       |
|                                   | purple rain that generated this   |
|                                   | post                              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| string                            | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | The prompt tracking string        |
|                                   | associated with this video post   |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` react_mode_metadata `           | <div>                             |
|                                   |                                   |
| JSON-encoded string               | <div>                             |
|                                   |                                   |
|                                   | This metadata is required for     |
|                                   | clip reacts feature               |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` referenced_sticker_id `         | <div>                             |
|                                   |                                   |
| numeric string or integer         | <div>                             |
|                                   |                                   |
|                                   | Sticker id of the sticker in the  |
|                                   | post                              |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| numeric string or integer         | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | The video id your uploaded video  |
|                                   | about to replace                  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` slideshow_spec `                | <div>                             |
|                                   |                                   |
| JSON object                       | <div>                             |
|                                   |                                   |
|                                   | Specification of a list of images |
|                                   | that are used to generate video.  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` source `                        | <div>                             |
|                                   |                                   |
| string                            | <div>                             |
|                                   |                                   |
|                                   | The video, [encoded as form       |
|                                   | data](https://l.f                 |
|                                   | acebook.com/l.php?u=https%3A%2F%2 |
|                                   | Fwww.w3.org%2FTR%2Fhtml401%2Finte |
|                                   | ract%2Fforms.html%23h-17.13.4.2&h |
|                                   | =AT31t8y9-Q1OyG4fYalnFhJFF4O7L85J |
|                                   | 5u8xPqaFpzpV24egt6NhkYll45cU2e6D9 |
|                                   | qgv9SfT-cstTpC2OW2arR_T8NDOlRy0-0 |
|                                   | wpPhNp-IFurcHXqhJNQH7rsg9bZq-vSBk |
|                                   | HlQ7zr0KqmPkeq8cblGs5DLkNG6su5Ec) |
|                                   | . This field is required.         |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` spherical `                     | Default value: ` false `          |
|                                   |                                   |
| boolean                           | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Set if the video was recorded in  |
|                                   | 360 format.                       |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` sponsor_id `                    | <div>                             |
|                                   |                                   |
| numeric string or integer         | <div>                             |
|                                   |                                   |
|                                   | Facebook Page id that is tagged   |
|                                   | as sponsor in the video post      |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| int64                             | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Start byte position of the file   |
|                                   | chunk.                            |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| enum {replace}                    | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Type of replacing video request   |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` title `                         | [ Supports Emoji ]{._1vet}        |
|                                   |                                   |
| UTF-8 string                      |                                   |
+-----------------------------------+-----------------------------------+
| ::: _yc                           | <div>                             |
| ` transcode_setting_properties `  |                                   |
| [](#){#u_0_u_SY ._2pir}           | <div>                             |
| :::                               |                                   |
|                                   | Properties used in computing      |
| string                            | transcode settings for the video  |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| ` unpublished_content_type `      | <div>                             |
|                                   |                                   |
| enum {SCHEDULED,                  | <div>                             |
| SCHEDULED_RECURRING, DRAFT,       |                                   |
| ADS_POST, INLINE_CREATED,         | Type of unpublished content, such |
| PUBLISHED,                        | as scheduled, draft or ads_post.  |
| REVIEWABLE_BRANDED_CONTENT}       |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| enum {start, transfer, finish,    | <div>                             |
| cancel}                           |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | Type of chunked upload request.   |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| numeric string or integer         | <div>                             |
|                                   |                                   |
|                                   | <div>                             |
|                                   |                                   |
|                                   | ID of the chunked upload session. |
|                                   |                                   |
|                                   | </div>                            |
|                                   |                                   |
|                                   | </div>                            |
+-----------------------------------+-----------------------------------+
| string                            |                                   |
+-----------------------------------+-----------------------------------+
| string                            |                                   |
+-----------------------------------+-----------------------------------+
:::

</div>

::: _367u
Struct {

` id ` : numeric string,

` upload_session_id ` : numeric string,

` video_id ` : numeric string,

` start_offset ` : numeric string,

` end_offset ` : numeric string,

` success ` : bool,

` skip_upload ` : bool,

` upload_domain ` : string,

` region_hint ` : string,

` xpv_asset_id ` : numeric string,

` is_xpv_single_prod ` : bool,

` transcode_bit_rate_bps ` : numeric string,

` transcode_dimension ` : numeric string,

` should_expand_to_transcode_dimension ` : bool,

` action_id ` : string,

` gop_size_seconds ` : numeric string,

` target_video_codec ` : string,

` target_hdr ` : string,

` maximum_frame_rate ` : numeric string,

}
:::

</div>
