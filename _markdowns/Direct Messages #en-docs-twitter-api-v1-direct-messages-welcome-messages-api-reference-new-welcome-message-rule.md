::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
Creates a new Welcome Message Rule that determines which Welcome Message
will be shown in a given conversation. Returns the created rule if
successful.

Requires a JSON POST body and ` Content-Type ` header to be set to
` application/json ` . Setting ` Content-Length ` may also be required
if it is not automatically.

Additional rule configurations are forthcoming. For the initial beta
release, the most recently created Rule will always take precedence, and
the assigned Welcome Message will be displayed in the conversation.

See the [Welcome Messages
overview](/en/docs/direct-messages/welcome-messages/overview) to learn
how to work with Welcome Messages.

## Resource URL [¶](#resource-url){.headerlink}

` https://api.twitter.com/1.1/direct_messages/welcome_messages/rules/new.json `

  -------------------------- -------------------------
  Response formats           JSON
  Content-Type               application/json
  Requires authentication?   Yes (user context only)
  Rate limited?              Yes
  -------------------------- -------------------------

## Welcome Message Rule Object [¶](#welcome-message-rule-object){.headerlink}

  ----------------------------------- ------------------------------------------------------------------------------
  **welcome_message_id** (required)   The ID of the Welcome Message that will be sent when this Rule is triggered.
  ----------------------------------- ------------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

    {
      "welcome_message_rule": {
        "welcome_message_id": "844385345234"
      }
    }

### Example request using [Twurl](https://github.com/twitter/twurl) [¶](#example-request-using-twurl){.headerlink}

    twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/welcome_messages/rules/new.json -d '{"welcome_message_rule": {"welcome_message_id": "844385345234"}}'

## Example Response [¶](#example-response){.headerlink}

    {
      "welcome_message_rule" : {
        "id": "9910934913490319",
        "created_timestamp": "1470182394258",
        "welcome_message_id": "844385345234"
      }
    }
:::
:::
:::
:::
:::
:::
:::
