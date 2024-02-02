::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Add a specified Tweet to a Collection.

A collection will store up to a few thousand Tweets. Adding a Tweet to a
collection beyond its allowed capacity will remove the oldest Tweet in
the collection based on the time it was added to the collection.

Use [POST collections / entries /
curate](/en/docs/tweets/curate-a-collection/api-reference/post-collections-entries-curate)
to add Tweets to a Collection in bulk.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/collections/entries/add.json `

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
  relative_to   optional   The identifier of the Tweet used for relative positioning in a *curation_reverse_chron* ordered collection.                          *614929127313965056*
  above         optional   Set to *false* to insert the specified *tweet_id* below the *relative_to* Tweet in the collection. Default: *true*                   *false*
  ------------- ---------- -------------------------------------------------------------------------------------------------------------------- --------------- -----------------------------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/collections/entries/add.json?tweet_id=390890231215292416&id=custom-388061495298244609 `

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
              "op": "add",
              "tweet_id": "390890231215292416"
            },
            "reason": "duplicate"
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
