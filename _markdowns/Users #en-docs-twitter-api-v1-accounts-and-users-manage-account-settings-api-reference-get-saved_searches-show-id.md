::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Retrieve the information for the saved search represented by the given
id. The authenticating user must be the owner of saved search ID being
requested.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/saved_searches/show/:id.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   15
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ------ ---------- ----------------------------- --------------- ----------
  Name   Required   Description                   Default Value   Example
  id     required   The ID of the saved search.                   *313006*
  ------ ---------- ----------------------------- --------------- ----------

## Example Request [¶](#example-request){.headerlink}

` GET https://api.twitter.com/1.1/saved_searches/show/9569704.json `

## Example Response [¶](#example-response){.headerlink}

    {
      "created_at": "Fri Nov 04 18:46:41 +0000 2011", 
      "id": 62353170, 
      "id_str": "62353170", 
      "name": "@anywhere", 
      "position": null, 
      "query": "@anywhere"
    }
:::
:::
:::
:::
:::
:::
:::
