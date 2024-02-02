::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Displays a visual typing indicator in the recipient's Direct Message
conversation view with the sender. Each request triggers a typing
indicator animation with a duration of \~3 seconds.

## Usage [¶](#usage){.headerlink}

A rudimentary approach would be to invoke an API request on every
keypress or input event, however the application may quickly hit rate
limits. A more sophisticated approach is to capture input events, but
limit API requests to a specified interval based on the behavior of your
users and the rate limit specified below.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/indicate_typing.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Content-Type                           application/json
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   1000 / 15 minutes
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------------- ----------------------------------------------------------
  **recipient_id** (required)   The user ID of the user to receive the typing indicator.
  ----------------------------- ----------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X POST /1.1/direct_messages/indicate_typing.json -d "recipient_id=3805104374"

## HTTP Response Codes [¶](#http-response-codes){.headerlink}

Response contains no body.

  ----- ------------------------------------------------------
  204   Typing indicator successfully sent.
  400   Missing or invalid parameter(s) included in request.
  ----- ------------------------------------------------------

## Webhook Event [¶](#webhook-event){.headerlink}

**Coming Soon:** If using the [Account Activity
API](/en/docs/accounts-and-users/subscribe-account-activity/overview) ,
the following JSON payload will be sent to your webhook for all
subscribed users.

    {
      "direct_message_indicate_typing_events": [
        {
          "created_timestamp":"1288834974657",
          "sender_id":"2244994945",
          "target":{
            "recipient_id":"3805104374"
          }
        }
      ],
      "users": {
        // hydrated user objects
      }
    }
:::
:::
:::
:::
:::
:::
:::
