::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Permanently delete a Collection owned by the currently authenticated
user.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/destroy.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------ ---------- ---------------------------------------------- --------------- -----------------------------
  Name   Required   Description                                    Default Value   Example
  id     required   The identifier of the Collection to destroy.                   *custom-388061495298244609*
  ------ ---------- ---------------------------------------------- --------------- -----------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/collections/destroy.json?id=custom-390882285743898624 `

## Example Response [¶](#example-response){.headerlink}

    {
      "destroyed": true
    }
:::
:::
:::
:::
:::
:::
:::
