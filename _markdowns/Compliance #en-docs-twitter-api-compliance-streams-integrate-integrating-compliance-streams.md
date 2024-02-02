::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The Tweet and User compliance streams are realtime streaming endpoints
that delivers compliance events that occur on the Twitter platform. For
an understanding of compliance events and how they are generated on
Twitter, please reference our article, [Honoring User Intent on
Twitter](/en/docs/twitter-api/compliance/streams/integrate/honoring-user-intent.html)
.

It is important to note that Tweet and User events are delivered
independently and that each should be processed independently (i.e. a
Tweet delete doesn't imply a User event, and vice versa.) Several User
events are not necessarily permanent and can toggle between states
infinitely. These include: user_delete,user_undelete, user_protect,
user_unprotect and user_suspend, user_unsuspend.

User_deletes are followed by Tweet deletes 30 days later only if the
user has not selected to user_undelete their account. It is possible
that a user_delete is reversed by the user and deletes for all of their
Tweets 30 days later do not occur.

User_suspend is an action that remains true unless the user is subject
to an user_unsuspend event. These are not subject to any changes on a 30
day time period.

It is never suitable to display compliance events directly to users of
your software or to otherwise incorporate them into your products or
customer experiences. They are intended solely for maintaining
compliance and honoring the actions of Twitter users.

## Integrating the compliance streams 

To integrate the compliance streams into your system, you will need to
build an integration that can do the following:

1.  Establish a streaming connection to each streaming endpoint
    partition of the compliance streams. The Tweet and User streams are
    both split into 4 partitions, and a connect must be established for
    each partition.
2.  Handle high data volumes -- de-couple stream ingestion from
    additional processing using asynchronous processes
3.  Reconnect to the stream partitions automatically when disconnected
    for any reason. After a disconnection, reconnect using the
    \'backfill_minutes\' request parameter to avoid missing any events.
    Your system needs to be tolerant of duplicate events.
4.  Process compliance events that are relevant to Tweet and User data
    you have stored in accordance with the guidance presented above
:::
:::
:::
:::
:::
:::
:::
:::
