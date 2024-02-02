::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Profile images (also known as avatars) are an important component of a
Twitter account's expression of identity. Use [POST
account/update_profile_image](/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_image){.reference
.external} to upload a profile image on behalf of a user.\

### Alternative image sizes for user profile images [¶](#alternative-image-sizes-for-user-profile-images){.headerlink}

Obtain a user's most recent profile image, along with the other
components comprising their identity on Twitter, from [GET
users/show](/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show){.reference
.external} . The [user
object](/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object){.reference
.external} contains the ` `{.docutils
.literal}[` profile_image_url `{.docutils .literal}]{.pre}` `{.docutils
.literal} and ` `{.docutils
.literal}[` profile_image_url_https `{.docutils
.literal}]{.pre}` `{.docutils .literal} fields. These fields will
contain the resized "normal" variant of the user's uploaded image. This
"normal" variant is typically 48px by 48px.

By modifying the URL, it is possible to retrieve other variant sizings
such as "bigger", "mini", and "original". Consult the table below for
more examples:

  ---------- ------------ ---------------------------------------------------------------------------------
  Variant    Dimensions   Example URL

  normal     48x48        [ http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png
                          https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_normal.png
                          ]{.code-inline}

  bigger     73x73        [ http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_bigger.png
                          https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_bigger.png
                          ]{.code-inline}

  mini       24x24        [ http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_mini.png
                          https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3_mini.png
                          ]{.code-inline}

  original   original     [ http://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3.png
                          https://pbs.twimg.com/profile_images/2284174872/7df3h38zabcvjylnyfe3.png\
                          ]{.code-inline} *Omit the underscore and variant to retrieve the original image.
                          The images can be very large.*
  ---------- ------------ ---------------------------------------------------------------------------------

### Default profile images [¶](#default-profile-images){.headerlink}

Some users may not have uploaded a profile image. Users who have not
uploaded a profile image can be identified by the ` `{.docutils
.literal}[` default_profile_image `{.docutils
.literal}]{.pre}` `{.docutils .literal} field of their user object
having a ` `{.docutils .literal}[` true `{.docutils
.literal}]{.pre}` `{.docutils .literal} value.

The ` `{.docutils .literal}[` profile_image_url `{.docutils
.literal}]{.pre}` `{.docutils .literal} and ` `{.docutils
.literal}[` profile_image_url_https `{.docutils
.literal}]{.pre}` `{.docutils .literal} URLs provided for users in this
case will indicate Twitter's default profile photo, which is
[https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png](https://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png){.reference
.external} .

The table above can be used to determine how to retrieve different size
variants of the default image.\

### Outdated profile images [¶](#outdated-profile-images){.headerlink}

If a 403 or 404 error is returned when trying to access a profile image,
refresh the [user
object](/content/developer-twitter/en/docs/tweets/data-dictionary/overview/user-object){.reference
.external} using [GET
users/show](/content/developer-twitter/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-show){.reference
.external} to retrieve the most recent ` `{.docutils
.literal}[` profile_image_url `{.docutils .literal}]{.pre}` `{.docutils
.literal} or ` `{.docutils
.literal}[` profile_image_url_https `{.docutils
.literal}]{.pre}` `{.docutils .literal} . The URL may have changed,
which happens for instance when the user updates their profile image.\

## Profile banners [¶](#profile-banners){.headerlink}

Profile banners allow users to further customize the expressiveness of
their profiles. Use [POST
account/update_profile_banner](/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/post-account-update_profile_banner){.reference
.external} to upload a profile banner on behalf of a user.

Profile banners come in a variety of display-enhanced sizes. The variant
sizes are available through a request to [GET
users/profile_banner](/content/developer-twitter/en/docs/accounts-and-users/manage-account-settings/api-reference/get-users-profile_banner){.reference
.external} or by modifying the final path component of the ` `{.docutils
.literal}[` profile_banner_url `{.docutils .literal}]{.pre}` `{.docutils
.literal} found in a user object according to the table below.

The profile banner data available at each size variant's URL is in PNG
format.

The following sizes are available:

  ------------- -------------------------------------------------------------------
  Dimensions\   Example URL

  1500x500      [ https://pbs.twimg.com/profile_banners/6253282/1431474710/1500x500
                ]{.code-inline}

  600x200       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/600x200
                ]{.code-inline}

  300x100       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/300x100
                ]{.code-inline}
  ------------- -------------------------------------------------------------------

The following sizes are available for the certain screen types:

  --------------- ------------- ------------------------------------------------------------------------
  Screen Type     Dimensions\   Example URL

  web             520x260       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/web
                                ]{.code-inline}

  web_retina      1040x520      [ https://pbs.twimg.com/profile_banners/6253282/1431474710/web_retina
                                ]{.code-inline}

  ipad            626x313       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/ipad
                                ]{.code-inline}

  ipad_retina     1252x626      [ https://pbs.twimg.com/profile_banners/6253282/1431474710/ipad_retina
                                ]{.code-inline}

  mobile          320x160       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/mobile
                                ]{.code-inline}

  mobile_retina   640x320       [ https://pbs.twimg.com/profile_banners/6253282/1431474710/mobile_retina
                                ]{.code-inline}
  --------------- ------------- ------------------------------------------------------------------------
:::
:::
:::
:::
:::
:::
:::
:::
