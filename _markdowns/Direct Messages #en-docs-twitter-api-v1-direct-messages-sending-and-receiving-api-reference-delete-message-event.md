::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Deletes the direct message specified in the required ID parameter. The
authenticating user must be the recipient of the specified direct
message. Direct Messages are only removed from the interface of the user
context provided. Other members of the conversation can still access the
Direct Messages. A successful delete will return a 204 http response
code with no body content.

**Important** : This method requires an access token with RWD (read,
write & direct message) permissions.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/events/destroy.json `

  -------------------------- -------------------------
  Response formats           204 - No Content
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- ------------------------------------------------------------
  **id** (required)   The id of the Direct Message event that should be deleted.
  ------------------- ------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X DELETE "/1.1/direct_messages/events/destroy.json?id=938178981337088004"
:::
:::
:::
:::
:::
:::
:::
