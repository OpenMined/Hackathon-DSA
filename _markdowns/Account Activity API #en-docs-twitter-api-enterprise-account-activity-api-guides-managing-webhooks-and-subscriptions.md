::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
In order to change webhook URLs, you must delete your existing webhook
and then create a new one. Note that when you do this, you will be
required to re-add user subscriptions to the new webhook.

#### Webhook configuration management endpoints:

#### Why can't I just update the webhook URL?

Why are webhook configurations immutable? Twitter takes security very
seriously. If your webhook URL is changed, there is a possibility that
your application consumer key and consumer secret have been compromised.
By requiring you to create a new webhook configuration, you are also
required to re-subscribe to your user's events. This requires the use of
access tokens that a malicious party is less likely to possess. As a
result, the likelihood that another party will receive your user's
private information is reduced.\

### Adding & removing User subscriptions

Support for thousands of subscriptions is available with the enterprise
tier. If you already have an account manager, please reach out to them
with questions.  To apply for access to the enterprise APIs, [click
here](/content/developer-twitter/en/enterprise) .\

#### Subscription management endpoints 

### 

### Next steps

#### 
:::
:::
:::
:::
:::
:::
:::
:::
