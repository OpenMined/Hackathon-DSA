::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Returns a single Feedback response for the specified ID in the URL.

  -------------------------------------- -------------------------
  Response formats                       JSON
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15 min window (user auth)   180
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ---------------------------- -------------------
  **feedback_id** (required)   Required in path.
  ---------------------------- -------------------

## Response Values [¶](#response-values){.headerlink}

  ----------- ---------------------------------------------------------------------------
  **score**   The user provided score response. 1­5 if type is CSAT. 0­10 if type is NPS.
  **text**    The user provided text response.
  ----------- ---------------------------------------------------------------------------

## Example Result [¶](#example-result){.headerlink}

    {
      "created_at": "SatDec1517:58:20+00002015",
      "updated_at": "SatDec1517:59:22+00002015",
      "id": "123456789"
      "text": "Thankyouforbeingaloyalcustomer!",
      "media_id_str": 12345,
      "response": {
        "score": {
          "created_at": "SatDec1518:59:22+00002015",
          "value": 1
        },
        "text": {
          "created_at": "SatDec1518:59:52+00002015",
          "value": "I<3thisbiz"
        }
      }
    }

::: note
Response object will only be present if data is available.
:::
:::
:::
:::
:::
:::
:::
:::
