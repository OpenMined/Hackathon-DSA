::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns the authenticated user\'s saved search queries.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/saved_searches/list.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

None

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/saved_searches/list.json `

## Example Response [¶](#example-response){.headerlink}

    [
      {
        "created_at": "Tue Jun 15 09:37:24 +0000 2010",
        "id": 9569704,
        "id_str": "9569704",
        "name": "@twitterapi",
        "position": null,
        "query": "@twitterapi"
      },
      {
        "created_at": "Tue Jun 15 09:38:04 +0000 2010",
        "id": 9569730,
        "id_str": "9569730",
        "name": "@twitter OR twitterapi OR "twitter api" OR "@anywhere"",
        "position": null,
        "query": "@twitter OR twitterapi OR "twitter api" OR "@anywhere""
      }
    ]
:::
:::
:::
:::
:::
:::
:::
