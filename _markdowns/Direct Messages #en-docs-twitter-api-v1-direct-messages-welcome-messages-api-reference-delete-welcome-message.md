::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Deletes a Welcome Message by the given id.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/destroy.json `

  -------------------------- -------------------------
  Response formats           204 - No Content
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------------- -------------------------------------------------------
  **id** (required)   The id of the Welcome Message that should be deleted.
  ------------------- -------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X DELETE /1.1/direct_messages/welcome_messages/destroy.json?id=844385345234
:::
:::
:::
:::
:::
:::
:::
