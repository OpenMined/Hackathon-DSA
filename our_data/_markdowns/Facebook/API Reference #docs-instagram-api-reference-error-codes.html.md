Error Codes - Instagram Platform - Documentation - Meta for Developers

Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
Error Codes
===========

This page describes the error messages that can be returned by the Instragram Graph API. The sample response below shows an example of code `3600` and subcode `2207004` with the subsequent error codes defined.

### Sample Response

```
{
  "error": 
    {
      "message": "The image size is too large.",
      "type": "OAuthException",
      "code": 36000,
      "error_subcode": 2207004,
      "is_transient": false,
      "error_user_title": "Image size too large",
      "error_user_msg": "The image is too large to download. It should be less than 8 MiB.",
      "fbtrace_id": "A6LJylpZRKw2xKLFsAP-cJh"
   }
 }
```
### Error Codes Defined

 HTTP Status Code | Code | Subcode | User Message | Recommended Solution || `400` | `-2` | `2207003` | `It takes too long to download the media.` | A timeout occured while downloading the media. Try again. |
| `400` | `-2` | `2207020` | `The media you are trying to access has expired. Please try to upload again.` | Generate a new container ID and use it to try again. |
| `400` | `-1` | `2207001` |  | Instagram server error. Try again. |
| `400` | `-1` | `2207032` | `Create media fail, please try to re-create media` | Failed to create a media container. Try again. |
| `400` | `-1` | `2207053` | `unknown upload error` | An unknown error occured during upload. Generate a new container and use it to try again. This should only affect video uploads. |
| `400` | `1` | `2207057` | `Thumbnail offset must be greater than or equal to 0 and less than video duration, i.e.` {video-length} | The thumbnail offset you entered is out of bounds for the video duration. Add the right offset in milliseconds. |
| `400` | `4` | `2207051` | `We restrict certain activity to protect our community. Tell us if you think we made a mistake.` | The publishing action is suspected to be spam. We restrict certain activity to protect our community. Let us know if you can determine that the publishing actions is not spam. |
| `400` | `9` | `2207042` | `You reached maximum number of posts that is allowed to be published by Content Publishing API.` | The app user has reached their daily publishing limit. Advise the app's user to try again the following day. |
| `400` | `24` | `2207006` | `The media with` {media-id} `cannot be found` | Possible permission error due to missing permission or expired token. Generate a new container and use it to try again. |
| `400` | `24` | `2207008` | `The media builder with creation id =` {creation-id} `does not exist or has been expired.` | Temporary error publishing a container. Try again 1–2 times in the next 30 seconds to 2 minutes. If unsuccessful, generate a new container ID and use it to try again. |
| `400` | `25` | `2207050` | `The Instagram account is restricted.` | The app user's Instagram Professional account is inactive, checkpointed, or restricted. Advise the app user to sign in to the Instagram app and complete any actions the app requires to re-enable their account. |
| `400` | `100` | `2207023` | `The media type` {media-type} `is unknown.` | The media type entered is not one of the expected media types. Please enter the correct one. |
| `400` | `100` | `2207028` | `Your post won't work as a carousel. Carousels need at least 2 photos/videos and no more than 10 photos/videos.` | Try again using an acceptable number of photos/videos. |
| `400` | `100` | `2207035` | `Product tag positions should not be specified for video media.` | Videos do not support X/Y coordinates. Disallow X/Y coordinates with videos. |
| `400` | `100` | `2207036` | `Product tag positions are required for photo media.` | Image product tags must include X/Y coordinates. Require X/Y coordinates for images. |
| `400` | `100` | `2207037` | `We couldn't add all of your product tags. The product ID may be incorrect, the product may be deleted, or you may not have permission to tag the product.` | One or more of the products being used to tag the item is invalid (deleted, rejected, app user lacks permission, product ID is invalid, etc.). Get the app user's catalogs and eligible products again and allow the app user to only use those product IDs when tagging. |
| `400` | `100` | `2207040` | `Cannot use more than` {max-tag-count} `tags per created media.` | The app user exceeded the maximum number (20) of @ tags. Advise user to use fewer @ tags. |
| `400` | `352` | `2207026` | `The video format is not supported. Please check spec for supported` {video} `format` | Unsupported video format. Advise the app user to upload an MOV or MP4 (MPEG-4 Part 14). See Video Specifications. |
| `400` | `9004` | `2207052` | `The media could not be fetched from this uri:` {uri} | The media could not be fetched from the supplied URI. Advise the app user to make sure the URI is valid and publicly available. |
| `400` | `9007` | `2207027` | `The media is not ready for publishing, please wait for a moment` | Check the container status and publish when its status is `FINISHED`. |
| `400` | `36000` | `2207004` | `The image is too large to download. It should be less than` {size}`.` | Image exceeded maximum file size of 8MiB. Advise the user to try again with a smaller image. |
| `400` | `36001` | `2207005` | `The image format` {current-image-format} `is not supported. Supported formats are:` {format}`.` | Possible permission error due to missing permission or expired token. Generate a new container and use it to try again. |
| `400` | `36003` | `2207009` | `The submitted image with aspect ratio` {submitted-ratio} `cannot be published. Please submit an image with a valid aspect ratio.` | The image's aspect ratio does not fall within our acceptable range. Advise the app user to try again with an image that falls withing a 4:5 to 1.91:1 range. |
| `400` | `36004` | `2207010` | `The submitted image's caption was` {submitted-caption-length} `characters long. The maximum number of characters permitted for a caption is` {maximum-caption-length}. `Please submit media with a shorter caption.` | The user exceeded the maximum amount of characters for a caption. Advise user to use a shorter caption. Maximum 2,200 characters, 30 hashtags, and 20 @ tags. |