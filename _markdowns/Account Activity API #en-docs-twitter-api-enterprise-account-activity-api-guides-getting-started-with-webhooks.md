::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
**[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}**

The Account Activity API is a webhook-based API that sends account
events to a web app you develop, deploy and host.

There are several \'plumbing\' details that need attention before you
can start receiving webhook events in your event consumer application.
As described below, you will need to create a Twitter app, obtain
Account Activity API access, and develop a web app that consumes webhook
events.

### 1. Create a Twitter app.

-   Create a [Twitter app](/content/developer-twitter/en/docs/apps) with
    an approved developer account from the [developer
    portal](/content/developer-twitter/en/docs/developer-portal/overview)
    . If you are creating the app on behalf of your company, it is
    recommended you create the app with a corporate Twitter account. To
    apply for a developer account, [click
    here](/content/developer-twitter/en/apply) .
-   Enable "Read, Write and Access direct messages" on the
    [permissions](/content/developer-twitter/en/docs/authentication/overview/application-permission-model)
    tab of your app page.
-   On the \"Keys and Access Tokens\" tab, take note of your app\'s
    Consumer Key (API Key) and Consumer Token (API Secret).
-   On the same tab, generate your app\'s [Access Token and Access Token
    Secret](/content/developer-twitter/en/docs/authentication/guides/access-tokens)
    . You will need these Access Tokens to register your webhook URL,
    which is where Twitter will send account events.
-   If you are unfamiliar with [Twitter
    Sign-in](/content/developer-twitter/en/docs/basics/authentication/overview/sign-in-with-twitter)
    and how user contexts work with the Twitter API review [Obtaining
    Access Tokens](https://dev.twitter.com/webhooks/access-tokens) . As
    you add accounts for which to receive events, you will subscribe
    them using that account\'s access tokens.
-   Take note of your app\'s numeric ID, as seen in the
    [\"Apps\"](/content/developer-twitter/en/docs/apps) page of the
    [developer
    portal](/content/developer-twitter/en/docs/developer-portal/overview)
    . When you apply for Account Activity API access, you\'ll need this
    app ID.\

### 2. Get Account Activity API access

After creating a Twitter app, the next step is applying for Account
Activity API access.

Those needing enterprise level access to more than 250 account
subscriptions and 3+ webhooks will need to submit an application at the
following link. If you can satisfy your use case with less access than
this, you may want to check out [Account Activity API
premium](/en/docs/twitter-api/premium/account-activity-api/overview) .
:::
:::

::: b03-button-v3
[](https://developer.twitter.com/en/enterprise-application.html){.chirp-btn
.twtr-spacing--mb-500 .chirp-btn--primary .chirp-btn--icon
.chirp-btn--icon-end .twtr-scribe-clicks}

::: chirp-btn__icon
![](https://cdn.cms-twdigitalassets.com/content/dam/developer-twitter/icons/chevron_right.svg){.chirp-btn__icon--img}
:::

Apply for Enterprise access
:::

::: c01-rich-text-editor
::: is-table-default
### []{#webhook-url} 3. Develop webhook consumer app

Once you have received Account Activity API access, you need to develop,
deploy and host a web app that will receive Twitter webhook events.

-   Create a web app with a URL to use as your webhook to receive
    events. This is the endpoint deployed on your server to listen for
    incoming Twitter webhook events.
    -   The URI *path* is completely up to you. This example would be
        valid: https://mydomain.com */service/listen*\
    -   If you are listening for webhooks from a variety of sources, a
        common pattern is: https://mydomain.com/webhook/twitter
    -   Note that the specified URL can not include a port specification
        (https://mydomain.com:5000/NoWorkie).
-   As described in our [Securing
    Webhooks](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks)
    guide, a first step is writing code that receives a Twitter
    Challenge Response Check (CRC) GET request and responds with a
    properly formatted JSON response.
-   Register your webhook URL. You will make a POST request to a [
    /webhooks.json?url= ]{.theme-color--dark} endpoint. When you make
    this request Twitter will issue a CRC request to your web app. When
    a webhook is successfully registered, the response will include a
    webhook [ id ]{.code-inline} . This webhook [ id ]{.code-inline} is
    needed later when making some requests to the Account Activity API.\
-   Twitter will send account webhook events to the URL you registered.
    Make sure your web app supports POST requests for incoming events.
    These events will be encoded in JSON. See
    [HERE](/en/docs/twitter-api/enterprise/account-activity-api/guides/account-activity-data-objects)
    for example webhook JSON payloads.
-   Once your web app is ready, the next step is adding accounts to
    receive activities for. When adding (or deleting) accounts you will
    make POST requests referencing the account id. See our [guide on
    adding
    subscriptions](/en/docs/twitter-api/enterprise/account-activity-api/guides/managing-webhooks-and-subscriptions)
    for more information.

### 4. Validate setup

-   To validate your app and webhook are configured correctly, favorite
    a Tweet posted by one of the Twitter accounts your app is subscribed
    to. You should receive a ` favorite_events ` via a POST request to
    your webhook URL for each Favorite your subscribers receive.
-   Note that it may take up to 10 seconds for events to start being
    delivered after a subscription has been added.

## Important Notes

-   When registering your webhook URL, your web app must authenticate
    with its consumer token and secret *and the app owner\'s user access
    token and secret* .
-   All incoming Direct Messages will be delivered via webhooks. All
    Direct Messages sent via [POST direct_messages/events/new
    (message_create)](/en/docs/direct-messages/sending-and-receiving/api-reference/new-event)
    will also be delivered via webhooks. This is so your web app can be
    aware of Direct Messages sent via a different client.
-   Note that every webhook event includes a [ for_user_id
    ]{.code-inline} user ID that indicates which subscription the event
    was delivered for.
-   If you have two users using your web app for Direct Messages in the
    same conversation, your webhook will receive two duplicate events
    (one for each user). Your web app should account for this.\
-   If you have more than one web app sharing the same webhook URL and
    the same user mapped to each app, the same event will be sent to
    your webhook multiple times (once per web app).
-   In some cases, your webhook may receive duplicate events. Your
    webhook app should be tolerant of this and dedupe by event ID.
-   Do not expect Quick Reply response to directly follow a request. A
    user has the ability to ignore a Quick Reply request and may respond
    via traditional Direct Message. The user may also provide a Quick
    Reply response to a request they have not replied to earlier in the
    message thread.

## Next steps
:::
:::
:::
:::
:::
:::
:::
:::
