::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Move a specified Tweet to a new position in a ` curation_reverse_chron `
ordered collection.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/entries/move.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------------- ---------- -------------------------------------------------------------------------------------------------------------------- --------------- -----------------------------
  Name          Required   Description                                                                                                          Default Value   Example
  id            required   The identifier of the Collection receiving the Tweet.                                                                                *custom-388061495298244609*
  tweet_id      required   The identifier of the Tweet to add to the Collection.                                                                                *390839888012382208*
  relative_to   required   The identifier of the Tweet used for relative positioning.                                                                           *614929127313965056*
  above         optional   Set to *false* to insert the specified *tweet_id* below the *relative_to* Tweet in the collection. Default: *true*                   *false*
  ------------- ---------- -------------------------------------------------------------------------------------------------------------------- --------------- -----------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/collections/entries/move.json?id=custom-388061495298244609&tweet_id=390839888012382208&relative_to=614929127313965056 `

## Example Response [¶](#example-response){.headerlink}

## Success: [¶](#success-){.headerlink} {#success-}

    {
      "objects": {},
      "response": {
        "errors": []
      }
    }

## Failure: [¶](#failure-){.headerlink} {#failure-}

    {
      "objects": {},
      "response": {
        "errors": [
          {
            "change": {
              "op": "move",
              "tweet_id": "610990849493762050"
            },
            "reason": "not_found"
          }
        ]
      }
    }
:::
:::
:::
:::
:::
:::
:::
