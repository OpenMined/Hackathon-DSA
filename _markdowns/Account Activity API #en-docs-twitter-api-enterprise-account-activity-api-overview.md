::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: {.b02-rich-text .twtr-rte .twtr-component-space--md}
::: {.b02__rich-text .twtr-scribe-clicks-within .b02__type--large}
This endpoint has been updated to include Tweet edit metadata. Learn
more about these metadata on the [\"Edit Tweets\" fundamentals
page](/en/docs/twitter-api/enterprise/edit-tweets) .

This endpoint is often used with the Direct Messages endpoints. We have
launched new [v2 Direct Messages
endpoints](/en/docs/twitter-api/direct-messages/manage/introduction) .
Note that the Enterprise and Premium Account Activity APIs support v2
one-to-one messages, but do not yet support group conversations.\
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
<div>

[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}

The Account Activity API provides you the ability to subscribe to
realtime activities related to a user account via webhooks. This means
that you can receive realtime Tweets, Direct Messages, and other account
events from one or more of your owned or subscribed accounts through a
single connection.

You will receive all related activities below for each user subscription
on your webhook registration:

+-----------------------------------+-----------------------------------+
| Activity types                    |                                   |
+-----------------------------------+-----------------------------------+
| -   Tweets (by user)\             | -   Blocks (by user)              |
| -   Tweet deletes (by user)       | -   Unblocks (by user)            |
| -   \@mentions (of user)          | -   Mutes (by user)               |
| -   Replies (to or from user)     | -   Unmutes (by user)             |
| -   Retweets (by user or of user) | -   Direct Messages sent (by      |
| -   Quote Tweets (by user or of   |     user)                         |
|     user)                         | -   Direct Messages received (by  |
| -   Retweets of Quoted Tweets (by |     user)                         |
|     user or of user)              | -   Typing indicators (to user)   |
| -   Likes (by user or of user)    | -   Read receipts (to user)       |
| -   Follows (by user or of user)\ | -   Subscription revokes (by      |
| -   Unfollows (by user)           |     user)\                        |
+-----------------------------------+-----------------------------------+

**Please note** - We do not deliver home timeline data via the Account
Activity API. Please use the [GET
statuses/home_timeline](/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline)
to pull this data.\

#### Video Series

Check out our [four-part video
series](https://www.youtube.com/watch?v=otPxejFhyy8&index=0&list=PLFKjcMIU2WshGG6Yj940XM7Z6BFs1zfBg)
on the Account Activity API to get up to speed!

</div>
:::

::: c01-rich-text-editor
<div>

### []{#comparison} Feature summary

  ----------------------------------------------------------------- ----------------------------------------------------------------------- -------------------------------- -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Tier                                                              Pricing                                                                 Number of unique subscriptions   Number of webhooks   Reliability and Activity Recovery
  [ Enterprise ]{.subscription-tag .subscription-tag--enterprise}   [Contact sales](/content/developer-twitter/en/enterprise-application)   Up to 500+                       3+                   [Retries](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-retries) and [Replay](/content/developer-twitter/en/docs/twitter-api/enterprise/account-activity-api/guides/activity-replay-api)
  ----------------------------------------------------------------- ----------------------------------------------------------------------- -------------------------------- -------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

</div>
:::

::: c01-rich-text-editor
## Next steps
:::
:::
