::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Uploads a profile banner on behalf of the authenticating user. More
information about sizing variations can be found in [User Profile Images
and
Banners](/en/docs/accounts-and-users/user-profile-images-and-banners)
and [GET users /
profile_banner](/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner)
.

Profile banner images are processed asynchronously. The
profile_banner_url and its variant sizes will not necessary be available
directly after upload.

## HTTP Response Codes [¶](#http-response-codes){.headerlink}

  --------------- ----------------------------------------------------------------------------
  Code(s)         Meaning
  200, 201, 202   Profile banner image successfully uploaded
  400             Either an image was not provided, or the image data could not be processed
  422             The image could not be resized, or is too large.
  --------------- ----------------------------------------------------------------------------

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/account/update_profile_banner.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------
  Name          Required   Description                                                                                                                                                                        Default Value   Example
  banner        required   The Base64-encoded or raw image data being uploaded as the user\'s new profile banner.                                                                                                             
  width         optional   The width of the preferred section of the image being uploaded in pixels. Use with *height* , *offset_left* , and *offset_top* to select the desired region of the image to use.                   
  height        optional   The height of the preferred section of the image being uploaded in pixels. Use with *width* , *offset_left* , and *offset_top* to select the desired region of the image to use.                   
  offset_left   optional   The number of pixels by which to offset the uploaded image from the left. Use with *height* , *width* , and *offset_top* to select the desired region of the image to use.                         
  offset_top    optional   The number of pixels by which to offset the uploaded image from the top. Use with *height* , *width* , and *offset_left* to select the desired region of the image to use.                         
  ------------- ---------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/account/update_profile_banner.json?width=1500&height=500&offset_top=0&offset_left=0&banner=FILE_DATA `
:::
:::
:::
:::
:::
:::
:::
