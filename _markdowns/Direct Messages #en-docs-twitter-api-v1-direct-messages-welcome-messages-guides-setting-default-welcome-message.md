::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Without a default Welcome Message, users are presented with an empty
Direct Message conversation view or the state of the previous
conversation.  A Welcome Message may be set to default so that it is
presented to the user when a Welcome Message deeplink is not used. Use a
default Welcome Message to provide context to users including what
services are provided, when they can receive response or provide Quick
Reply options to start an automated conversation flow. All features
available to Direct Messages can be used in a default Welcome Message.

When a Welcome Message is set as default, it will be presented to the
user in the following scenarios:

-   Direct Message compose view opened for the first time.
-   Direct Message compose view opened for the first time since leaving
    a conversation.
-   Direct Message compose view opened after no message activity for 7
    days.

**Note:** Specifying a Welcome Message in a
[deeplink](/en/docs/direct-messages/welcome-messages/guides/deeplinking-to-welcome-message)
will always override the default Welcome Message. Deeplinking without a
defined Welcome Message will follow default Welcome Message behavior
defined above.

To set a default Welcome Message:

**Note:** Although an account can have many Welcome Messages, an account
may only have a single "default" Welcome Message and only a single rule.
If you have previously created a rule, you must
[delete](/en/docs/direct-messages/welcome-messages/api-reference/delete-welcome-message-rule)
the current rule before creating a new one. See [POST
direct_messages/welcome_messages/rules/new](/en/docs/direct-messages/welcome-messages/api-reference/new-welcome-message-rule)
documentation for more information regarding the future of rules.\
:::
:::
:::
:::
:::
:::
:::
:::
