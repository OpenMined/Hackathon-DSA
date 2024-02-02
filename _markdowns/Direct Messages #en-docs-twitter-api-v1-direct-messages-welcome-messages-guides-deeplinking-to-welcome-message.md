::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Every Welcome Message can be deeplinked to. When a user follows the
deeplink, the Direct Message compose view will be opened with the
specified Welcome Message presented. Deeplinks can be used anywhere from
a website, an app, a Tweet or even another Direct Message conversation.

To create a Welcome Message deeplink:

1.  Create a new Welcome Message with [POST
    direct_messages/welcome_messages/new](/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message)
    . Take note of the returned Welcome Message ID.\
2.  Construct a Direct Message deeplink with the recipient_id and
    welcome_message_id query string parameters defined.\

Example Direct Message Deeplink:\

[ https://twitter.com/messages/compose?recipient_id=
3805104374&welcome_message_id=12345 ]{.payload}

**Note:** You can create as many Welcome Messages as you require and all
Welcome Messages can be deeplinked to.

## Deeplinking from a Tweet 

By simply including the Direct Message deeplink URL at the end of a
Tweet, your can append a \"Send a private message\" button to the bottom
of the Tweet. Read more about using Direct Message deeplinks in Tweets
in [this blog
post](https://blog.twitter.com/marketing/en_us/a/2016/best-practices-using-direct-messages-for-customer-service-0.html)
.

Using a [Direct Message
Card](https://blog.twitter.com/2017/drive-discovery-of-bots-other-personalized-customer-experiences-in-direct-messages)
, businesses can capture people's attention with engaging image or video
creatives, and include up to four fully customizable call-to-action
buttons. Each call-to-action button can deeplink to a unique Welcome
Message. The Direct Message Card is currently available in limited beta
to Twitter advertisers. Contact your Twitter representative for more
information.\

## Deeplinking from a Website 

Direct Message deeplinks may also be used to deeplink from a website or
other external source like a mobile app. For more details on deeplinking
to Welcome Messages from a website, see [Message
Button](https://dev.twitter.com/web/message-button) documentation.\
:::
:::
:::
:::
:::
:::
:::
:::
