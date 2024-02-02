<div>

::: c01-rich-text-editor
Buttons enable developers to add up to three call-to-action (CTA)
buttons to any Direct Message or Welcome Message. These buttons can be
used to open any URL from the Direct Message compose view. The text
labels displayed on the buttons can be fully customized.

![image](/_static/direct-messages/buttons.jpg)

This feature is intended to make it easier for users to complete actions
outside of Direct Messages, whether in a webview or in another part of
the Twitter app. For instance, buttons can be used to:

-   **Open a webview** to interact with a mobile web page that is better
    suited for completing an action than completing that action in
    messaging. For example, completing a credit card purchase or
    interacting with a side-by-side comparison of different products.

-   **Compose a Tweet** at the end of a Direct Message interaction. For
    example, to tell others about a bot or share a coupon publicly. This
    can be accomplished by using the Tweet [web intents URL
    scheme](https://dev.twitter.com/web/intents) .

-   **Follow a user** account at the end of a Direct Message
    interaction. For example, as a final request from a business at the
    end of a customer service interaction. This can be accomplished
    using the Follow [web intents URL
    scheme](https://dev.twitter.com/web/intents) .

-   **Send a Direct Message** to a different account. For example, to
    direct a user from a marketing-related bot to a separate dedicated
    customer service \@username to get help from a person. This can be
    accomplished using the Direct Message URL deep link scheme. Example
    below.

        https://twitter.com/messages/compose?recipient_id=3805104374

## CTAs Object [¶](#ctas-object){.headerlink}

Buttons can be added to a Direct Message by defining a ` ctas ` array of
1-3 objects.

  ------------------------- -----------------------------------------------------------------------------------------------------------
  **type** (required)       Defines the type of button to display. Currently must be set to ` web_url ` .
  **label** (required)      The text that will be displayed to the user on each button. Max string length of 36 characters.
  **url** (required)        A valid http or https target URL of the button.
  **tco_url** (read only)   The t.co version of the URL will be returned in a POST response and on the read path (GET requests) only.
  ------------------------- -----------------------------------------------------------------------------------------------------------

## Example Request [¶](#example-request){.headerlink}

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Flight SF8020 from San Francisco to Montreal is ahead of schedule and will land in approximately 15 minutes. Can we help with anything else?",
            "ctas": [
              {
                "type": "web_url",
                "label": "See flight details",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }

## Example Read Response [¶](#example-read-response){.headerlink}

The following JSON payload is an example of what will be received using
an [Account Activity
webhook](/en/docs/accounts-and-users/subscribe-account-activity/overview.html)
or GET request like [GET
direct_messages/events/list](/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)
. Notice the addition of the t.co short URL representation of the full
URLs.

    {
      "event": {
        "type": "message_create",
        "message_create": {
          "target": {
            "recipient_id": "844385345234"
          },
          "message_data": {
            "text": "Flight SF8020 from San Francisco to Montreal is ahead of schedule and will land in approximately 15 minutes. Can we help with anything else?",
            "ctas": [
              {
                "type": "web_url",
                "label": "See flight details",
                "tco_url": "https://t.co/foo1",
                "url": "https://www.myairline.domain/see-flight-details"
              },
              {
                "type": "web_url",
                "label": "Map it",
                "tco_url": "https://t.co/foo2",
                "url": "https://www.myairline.domain/map-it"
              },
              {
                "type": "web_url",
                "label": "Visit MyAirline.domain",
                "tco_url": "https://t.co/foo3",
                "url": "https://www.myairline.domain/"
              }
            ]
          }
        }
      }
    }
:::

</div>
