::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
**We retired the Site Streams, User Streams, and standard beta version
of the Account Activity API - DM Only products in 2018. If you had been
using those products, please make sure to migrate over to the premium or
enterprise version of the Account Activity API.**

**We have also retired the legacy Direct Message endpoints. If you had
been using those endpoints, please make sure to migrate over to either
the new DM endpoints, or to the premium or enterprise version of the
Account Activity API.**

**Please review [this
announcment](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746)
to learn more.**

Here are the endpoints that will be affected by these changes:\

-   User Streams
-   Site Streams
-   GET direct_messages
-   GET direct_messages/sent
-   GET direct_messages/show
-   POST direct_messages/new
-   POST direct_messages/destroy\

We have new endpoints and services available that provide similar access
and, for Direct Messages, some additional functionality:

To help you make a smooth migration to these new endpoints and services
we have two migration guides:

Additionally, we have a [series of
videos](https://www.youtube.com/playlist?list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg)
about the Account Activity API and how to get started.

And, finally, we have code samples to further your understanding and
help you get started quickly:

-   The [Account Activity
    Dashboard](https://github.com/twitterdev/Account-Activity-dashboard)
    is a sample Node.js web app with helper scripts to get started with
    the Account Activity API.
-   [SnowBot](https://github.com/twitterdev/SnowBotDev) is a sample
    chatbot using the Account Activity API and REST Direct Message
    endpoints. It's written in Ruby, uses the Sinatra web app framework,
    and is deployed on Heroku.\

If you are building solutions that ingest data and respond in Direct
Messages we also have a [Building a Customer Engagement Application on
Twitter
playbook](/en/docs/tutorials/customer-engagement-application-playbook) .

## Next steps

Review our [User Streams and Site Streams migration
guide](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/us-ss-migration-guide)

Review our [Direct Message API migration
guide](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/migration/direct-message-migration)

Learn more about the [Account Activity
API](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/overview)
:::
:::
:::
:::
:::
:::
:::
:::
