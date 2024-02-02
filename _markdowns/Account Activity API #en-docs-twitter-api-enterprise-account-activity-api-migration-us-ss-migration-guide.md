::: is-table-default
**As of August 23rd, 2018, we retired both Site Streams and User
Streams. Please make sure to migrate over to the Account Activity API.**

**Please review [this
announcement](https://twittercommunity.com/t/details-and-what-to-expect-from-the-api-deprecations-this-week-on-august-16-2018/110746)
to learn more.**

This guide is designed to help you migrate from legacy User Streams and
Site Streams APIs to their replacement, the Account Activity API. Below
you will find a summary of the changes, new features list, as well as
key differences and considerations to help with the transition. For
guidance in migrating from basic DM endpoints, please refer to the
[Direct Message migration
guide](/content/developer-twitter/en/docs/direct-messages/sending-and-receiving/guides/direct-message-migration)
.\

### Summary of changes

The Account Activity API will deliver you events for authenticated and
subscribed accounts via webhooks as opposed to a streaming connection
like with User Streams and Site Streams.

#### Deprecated APIs

GET user

GET site  (including control streams: GET site/c/:stream_id, 
GET site/c/:stream_id/info.json,  GET
site/c/:stream_id/friends/ids.json,  POST
site/c/:stream_id/add_user.json,  POST
/site/c/:stream_id/remove_user.json)

#### Replacement APIs

[Enterprise Account Activity API - All
Activities](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/api-reference/aaa-enterprise)

[Premium Account Activity API - All Activities\
](/en/docs/twitter-api/premium/account-activity-api/api-reference/aaa-premium)

### Differences & migration considerations

**API format:** The new Account Activity API operates differently than
User Streams and Site Streams. You will need to alter your web app to
receive data with webhooks. You can find more information on webhooks
[here](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks)
.

**Data Available:** Another key difference you will notice is in regards
to the data being delivered. Twitter will no longer send events from
people that you follow on Twitter (aka your home timeline). This was an
intentional change and is not something we plan to alter going forward.

**Reliability:** Unlike streaming, webhooks enable confirmation of
delivery and options to retry POSTed activities that do not make it to
the webhook URL.  This gives more assurance that the app is receiving
all applicable activities, even if there are brief disconnections or
periods of downtime.

### New features

The Account Activity API offers many new features, most notably that
data is now delivered via webhooks as opposed to streaming. Webhooks
offer many benefits compared to streaming, but the most prominent are
speed and reliability. The API will send you data in the form of JSON
events as they become available and you will no longer need to maintain
an active connection or poll the endpoint. This limits the need for
redundancy features and increases efficiency overall. More information
on webhooks can be found in the [technical
documentation](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/getting-started-with-webhooks)
.

### Managing user subscriptions

The Account Activity API allows multiple subscriptions for a single
registered webhook.  This allows multiple user subscriptions activities
to be delivered to the same location, similar to the Site Streams
architecture, with webhooks.  This means you can track subscriptions, as
they pertain to your subscription limits, independently from the webhook
connection.  This also allows scalability from only one or a few
subscriptions to thousands of subscriptions for a single webhook.

### **How to Migrate**

### **Follow the steps below to easily migrate from the Site Streams API to the Account Activity API**

**Step 1: Decide on a Package**

Depending on how you are currently operating with User Streams or Site
Streams, you should consider moving to either the enterprise or premium
version of the Account Activity API.  Consider the number of
applications or authorized users you are currently supporting and scale
appropriately to the volume and reliability needed.  When deciding on
the package that best suits your needs, some things worth considering
are:

-   Number of webhooks needed
-   Current/projected subscriptions/authorized users managed on your
    application
-   Current number of Twitter client applications
-   The level of support you\'d prefer from Twitter (forum support or
    managed enterprise level 1:1 support)
-   Price of each package

**Step 2:** **Check the Setup of your Twitter app in the developer
portal**

The [Twitter
app](/content/developer-twitter/en/docs/basics/developer-portal/guides/apps)
currently used for User Streams or Site Streams will be listed for the
owning user within the [developer
portal](/content/developer-twitter/en/docs/basics/developer-portal/overview)
. This Twitter app can also be used for Account Activity API to retain
authorized users for that application.  A new app can also be created,
and users can be re-authorized for this new app if desired.  If you are
creating a new app on behalf of a business, it is recommended that you
create the app with a corporate Twitter \@handle account.

-   Enable "Read, Write and Access direct messages" on the
    [permissions](/content/developer-twitter/en/docs/basics/authentication/overview/application-permission-model)
    tab of your Twitter app page.\
    \*Note that changing these settings is not retroactive, any
    authorized users will keep the authorization settings from the time
    at which they were authorized. If a user has not already given you
    read, write and direct message access, you will need to have that
    user re-authorize your application.
-   If you are unfamiliar with [Twitter
    Sign-in](/content/developer-twitter/en/docs/authentication/guides/log-in-with-twitter)
    and how user contexts work with the Twitter API review [Obtaining
    Access Tokens](https://dev.twitter.com/webhooks/access-tokens) .
-   Generate access tokens for the Twitter app owner at the bottom of
    the "Keys and Tokens" tab. On this same tab take note of your
    Consumer Key, Consumer Secret, Access Token and Access Token Secret.
    You will need these to use the API.
-   Generate a bearer token using your Consumer Key and Consumer Secret
    for
    [application-only](/content/developer-twitter/en/docs/basics/authentication/overview/application-only)
    API methods.

**Step 3: Setup & Configure Your Webhooks**

-   Create a web app with an endpoint to use as your webhook to receive
    events (e.g. https://your_domain.com/webhook/twitter or
    https://webhooks.your_domain.com).
-   Use your Consumer Key, Consumer Secret, Access Token and Access
    Token Secret when creating your webhook, Note that your endpoint
    must return a JSON response with a response_token that is a base64
    encoded HMAC SHA-256 hash created from the crc_token and your app
    Consumer Secret.\
-   Review [Securing
    Webhooks](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/securing-webhooks)
    documentation taking special note of the Challenge Response Check
    (CRC) requirements.
-   Make sure your webhook supports POST requests for incoming events
    and GET requests for the CRC.
-   Make sure your webhook has low latency (\<3 seconds to respond to
    POST requests)

**Step 4: Validate Your Webhook Setup**

-   Webhook APIs will secure your webhooks in two ways:

\- Require challenge response checks to validate that the webhook owner
is the web app owner.

\- A signature header in each POST request for your web app to validate
the source.

-   In order to verify that you are both the owner of the web app and
    the webhook URL, Twitter will perform a Challenge Response Check
    (CRC), which is not to be confused with a cyclic redundancy check.
-   A GET request with a parameter named crc_token will be sent to your
    webhook URL. Your endpoint must return a JSON response with a
    response_token that is a base64 encoded HMAC SHA-256 hash created
    from the crc_token and your app Consumer Secret.
-   The crc_token should be expected to change for each incoming CRC
    request. The crc_token should be used as the message in the
    calculation, where your Consumer Secret is the key.
-   In the event that the response is invalid, events will cease to be
    sent to the registered webhook.

**Step 5: Create Subscriptions for Each User Stream or Site Streams
Authorized User**

Converting to the Account Activity API from User Streams:

-   Generate a list of your current user subscriptions on User Streams
-   Set up your new Account Activity API subscriptions using the
    request: *POST account_activity/all/:env_name/subscriptions*
-   Confirm your Account Activity API subscriptions using the request:
    *GET account_activity/all/:env_name/subscriptions/list\
    *

Converting to the Account Activity API from Site Streams: (using control
streams):

-   Generate a list of your current subscriptions on Site Streams using
    the request: *GET /1.1/site/c/:stream_id/info.json*
-   Set up your new Account Activity API subscriptions using the
    request: *POST account_activity/all/:env_name/subscriptions*
-   Confirm your Account Activity API subscriptions using the request:
    *GET account_activity/all/:env_name/subscriptions/list\
    *

Registering a Webhook and Creating Subscriptions (not migrating from
Site Streams or User Streams)

### The Account Activity dashboard (sample Account Activity API application)

We\'ve created a sample app to make testing the Account Activity API a
little quicker:

-   Download the Account Activity Dashboard sample application
    [here](https://github.com/twitterdev/Account-Activity-dashboard) (it
    uses Node.js)
-   Follow the instructions on the README to install and launch the app
-   Once the application has been launched, you can use the UI to easily
    set up your webhook and create a new subscription

### Available Activities

### Deprecated streaming message types

  --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Blank lines           Blank lines will no longer be delivered in the Account Activity API as they were used as keep-alive messages in User Streams and Site Streams.
  Limit notices         Limit notices will no longer be sent to a given webhook.  Instead, users can call the API to get current usage of available handles. This will be included in the developer portal at some time in the future.
  Disconnect messages   Disconnect notices will no longer be necessary as webhooks do not rely on an active connection.
  Stall warnings        Stall warnings will no longer be necessary as webhooks do not rely on an active connection being able to handle large numbers of incoming messages.
  Friends list          Friends lists will no longer be sent proactively. There will now be a REST endpoint to get this information.
  --------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Deprecated event types

+-------------+-------------+-------------+-------------+-------------+
| **De        | **Event     | **Source**  | **Target**  | **Target    |
| scription** | Name**      |             |             | Object**    |
+-------------+-------------+-------------+-------------+-------------+
| User        | delete      | Current     | Current     | Tweet       |
| deletes a   |             | user        | User        |             |
| Tweet       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Followed    | delete      | Followed    | Followed    | Tweet       |
| user        |             | user        | user        |             |
| deletes a   |             |             |             |             |
| Tweet       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | unfavorite  | Current     | Tweet       | Tweet       |
| unfavorites |             | user        | author      |             |
| a Tweet     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User's      | unfavorite  | U           | Current     | Tweet       |
| Tweet is    |             | nfavoriting | user        |             |
| unfavorited |             | user        |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | unfollow    | Current     | Followed    | Null        |
| unfollows   |             | user        | user        |             |
| someone     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | l           | Current     | Current     | List        |
| creates a   | ist_created | user        | user        |             |
| list        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | lis         | Current     | Current     | List        |
| deletes a   | t_destroyed | user        | user        |             |
| list        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User edits  | l           | Current     | Current     | List        |
| a list      | ist_updated | user        | user        |             |
+-------------+-------------+-------------+-------------+-------------+
| User adds   | list_m      | Current     | Added user  | List        |
| someone to  | ember_added | user        |             |             |
| a list      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User is     | list_m      | Adding user | Current     | List        |
| added to a  | ember_added |             | user        |             |
| list        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | list_mem    | Current     | Removed     | List        |
| removes     | ber_removed | user        | user        |             |
| someone     |             |             |             |             |
| from a list |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User is     | list_mem    | Removing    | Current     | List        |
| removed     | ber_removed | user        | user        |             |
| from a list |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | list_user   | Current     | List owner  | List        |
| subscribes  | _subscribed | user        |             |             |
| to a list   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User's list | list_user   | Subscribing | Current     | List        |
| is          | _subscribed | user        | user        |             |
| subscribed  |             |             |             |             |
| to          |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | list_user_u | Current     | List owner  | List        |
| u           | nsubscribed | user        |             |             |
| nsubscribes |             |             |             |             |
| from a list |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User's list | list_user_u | Un          | Current     | List        |
| is          | nsubscribed | subscribing | user        |             |
| u           |             | user        |             |             |
| nsubscribed |             |             |             |             |
| from        |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | user_update | Current     | Current     | Null        |
| updates     |             | user        | user        |             |
| their       |             |             |             |             |
| profile     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| User        | user_update | Current     | Current     | Null        |
| updates     |             | user        | user        |             |
| their       |             |             |             | \           |
| protected   |             |             |             |             |
| status      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

## 
:::
