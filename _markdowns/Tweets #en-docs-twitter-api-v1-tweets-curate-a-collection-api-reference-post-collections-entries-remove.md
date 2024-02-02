::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Remove the specified Tweet from a Collection.

Use [POST collections / entries /
curate](/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-curate)
to remove Tweets from a Collection in bulk.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/entries/remove.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ---------- ---------- ------------------------------------------ --------------- -----------------------------
  Name       Required   Description                                Default Value   Example
  id         required   The identifier of the target Collection.                   *custom-388061495298244609*
  tweet_id   required   The identifier of the Tweet to remove.                     *390839888012382208*
  ---------- ---------- ------------------------------------------ --------------- -----------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/collections/entries/remove.json?id=custom-388061495298244609&tweet_id=390890231215292416 `

## Example Response [¶](#example-response){.headerlink}

Success:

    {
      "response": {
        "errors": [

        ]
      },
      "objects": {
      }
    }

Failure:

    {
      "response": {
        "errors": [
          {
            "change": {
              "tweet_id": "390890231215292416",
              "op": "remove"
            },
            "reason": "not_found"
          }
        ]
      },
      "objects": {
      }
    }
:::
:::
:::
:::
:::
:::
:::
