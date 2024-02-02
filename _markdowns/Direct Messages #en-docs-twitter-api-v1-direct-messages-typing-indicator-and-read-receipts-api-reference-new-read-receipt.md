::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Marks a message as read in the recipient's Direct Message conversation
view with the sender.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/mark_read.json `

  -------------------------------------- -------------------------
  Response formats                       JSON
  Content-Type                           application/json
  Requires authentication?               Yes (user context only)
  Rate limited?                          Yes
  Requests / 15-min window (user auth)   1000 / 15 minutes
  -------------------------------------- -------------------------

## Parameters [¶](#parameters){.headerlink}

  ----------------------------------- ------------------------------------------------------------------------------------------------------------------
  **last_read_event_id** (required)   The message ID of the most recent message to be marked read. All messages before it will be marked read as well.
  **recipient_id** (required)         The user ID of the user the message is from.
  ----------------------------------- ------------------------------------------------------------------------------------------------------------------

## Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -X POST /1.1/direct_messages/mark_read.json -d "last_read_event_id=8754578330382663743" -d "recipient_id=3805104374" 

## HTTP Response Codes [¶](#http-response-codes){.headerlink}

Response contains no body.

  ----- ------------------------------------------------------
  204   Read receipt successfully sent.
  400   Missing or invalid parameter(s) included in request.
  ----- ------------------------------------------------------

## Webhook Event [¶](#webhook-event){.headerlink}

If using the [Account Activity
API](/en/docs/accounts-and-users/subscribe-account-activity/overview) ,
the following JSON payload will be sent to your webhook for all
subscribed users.

    {
      "direct_message_mark_read_events": [
        {
          "created_timestamp": "1288834974657",
          "sender_id": "2244994945",
          "last_read_event_id": "877260925346103299",
          "target": {
            "recipient_id": "3805104374"
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
