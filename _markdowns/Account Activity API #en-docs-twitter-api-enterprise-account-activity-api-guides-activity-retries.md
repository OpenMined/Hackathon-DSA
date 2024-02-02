::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}

One of the benefits of the enterprise tier of the Account Activity API
is a retry mechanism for webhook events. If a \'success\' 200 HTTP
response code is not received, the Twitter server will initiate a retry
mechanism, resending the webhook event up to three times over a
five-minute period. This webhook event retry service helps provide
reliability and event recovery when network problems occur and during
client-side service interruptions and deploys.\

### What are retries?

The Account Activity API provides a retry feature when the client\'s web
app does not return a \'success\' 200 response for an account activity
webhook event. When the client-side does not confirm the successful
receipt of an event, Twitter assumes the event was not received. If
a non-200 response is received, a response isn\'t received within three
seconds, or we don\'t receive a response at all, we retry the request
and leave that open for three seconds. This means that you have roughly
five seconds over two attempts to respond to receive the activity that
we are trying to send to your webhook URL. In the event that your server
doesn\'t response or returns a transient error, we will retry for five
minutes. There will be a total of three retry attempts to confirm
validation. This allows redundancy and insurance that you receive all
webhook events. Note that subscriptions with retries will get retried
events for any/all activities for all subscribed users on their webhook.

If you do not confirm validation within these eight attempts, the
activity will no longer be available via the Account Activity API.

### Retry timeline

The Account Activity API will retry up to three times over a five-minute
period until a 200 response is received.  Refer to the table below for
more details. After around five minutes, the activity cannot be resent
through the Account Activity API. You will need to use other Twitter
endpoints to collect missed data. For example, the [search
APIs](/en/docs/twitter-api/enterprise/search-api/overview) can be used
to retrieve relevant Tweets, Retweets, Quote Tweets, Mentions, and
Replies. Missed Direct Messages can be retrieved with [this
endpoint](/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)
.

#### Retries timeline

  -----------------------------------------------------------------------
  Activity created, POST to the webhook URL from Account Activity API and
  times out in three seconds.

  Wait three seconds after previous timeout finishes, then POST to the
  webhook URL from Account Activity API and times out in three seconds.\

  Wait 27 seconds after previous timeout finishes, then POST to the
  webhook URL from Account Activity API and times out in three seconds.\

  Wait 242 seconds after previous timeout finishes, then POST to the
  webhook URL from Account Activity API and times out in three seconds\

  The Account Activity API will stop attempting to POST after this.
  Client must use other Twitter endpoints to recover data.
  -----------------------------------------------------------------------

## Next steps
:::
:::
:::
:::
:::
:::
:::
:::
