::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Create a new saved search for the authenticated user. A user may only
have 25 saved searches.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/saved_searches/create.json `

  -------------------------- -------------------------
  Response formats           JSON
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------- ---------- ------------------------------------------------------ --------------- ---------
  Name    Required   Description                                            Default Value   Example
  query   required   The query of the search the user would like to save.                   
  ------- ---------- ------------------------------------------------------ --------------- ---------

## Example Request [¶](#example-request){.headerlink}

` POST https://api.twitter.com/1.1/saved_searches/create.json?query=sandwiches `

## Example Response [¶](#example-response){.headerlink}

    {
      "created_at": "Fri Aug 24 22:08:58 +0000 2012", 
      "id": 158598597, 
      "id_str": "158598597", 
      "name": "sandwiches", 
      "position": null, 
      "query": "sandwiches"
    }
:::
:::
:::
:::
:::
:::
:::
