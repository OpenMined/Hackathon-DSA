::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: dtc09-callout-text
::: dtc09-callout-text
::: dtc09__item
::: dtc09__text
::: c01-rich-text-editor
::: is-table-default
**Please note**

We have released a new compliance tool to Twitter API v2 called [batch
compliance](/en/docs/twitter-api/compliance/batch-compliance) . This new
tool allows you to upload large datasets of Tweet or user IDs to
retrieve their compliance status in order to determine what data
requires action in order to bring your datasets into compliance.

In addtion, both the batch compliance and the compliance firehose have
been updated to support Tweet edits. For the compliance firehose, a new
\'tweet_edit\' event was added. See the [Compliance Data
Objects](/en/docs/twitter-api/enterprise/compliance-firehose-api/guides/compliance-data-objects)
documentation for more details. Learn more about how Edit Tweet metadata
works on the [Edit Tweets
fundamentals](/en/docs/twitter-api/edit-tweets) page.
:::
:::
:::
:::
:::
:::

::: c01-rich-text-editor
::: is-table-default
[ Enterprise ]{.subscription-tag .subscription-tag--enterprise}

One of Twitter's core values is to defend and respect the user's voice.
This includes respecting their expectations and intent when they delete,
modify, or edit the content they choose to share on Twitter. We believe
that this is critically important to the long term health of one of the
largest public, real-time information platforms in the world. Twitter
puts controls in the hands of its users, giving individuals the ability
to control their own Twitter experience. We believe that business
consumers that receive Twitter data have a responsibility to honor the
expectations and intent of end users.

For more information on the types of compliance events that are possible
on the Twitter platform, reference our article, [Honoring User Intent on
Twitter](/content/developer-twitter/en/docs/tweets/compliance/guides/honoring-user-intent)
.\

Any developer or company consuming Twitter data via an API holds an
obligation to use all reasonable efforts to honor changes to user
content. This obligation extends to user events such as deletions,
modifications, and changes to sharing options (e.g., content becoming
protected or withheld). This also includes when users edit their Tweets.
Please reference the specific language in the [Developer
Policy](/en/developer-terms/policy.html) and/or your Twitter Data
Agreement to understand how this obligation affects your use of Twitter
data.\

Twitter offers the following solutions that deliver information about
these user compliance events and whether a specific Tweet or User is
publicly available or not. A brief overview of the solutions and their
general integration patterns is detailed below:

#### GET statuses/lookup and GET users/lookup 

-   Format: REST API's See: [GET
    statuses/lookup](/en/docs/tweets/post-and-engage/api-reference/get-statuses-lookup.html)
    and [GET
    users/lookup](/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup.html)
    .
-   These endpoints always return the latest version of any Tweet
    edits. All Tweet objects describing Tweets created after the edit
    feature was introduced will include Tweet edit metadata. This is
    true even for Tweets that were not edited.
-    For all Tweets, requests for Tweets more than 30 minutes after they
    were created will represent the final state of all Tweets. \
-   Deliver availability information for specific Tweets or Users as
    defined by the caller as part of the API request.
-   May be used for ad-hoc spot-checking on the current availability
    state of a specific group of Tweets / Users.
-   Ideal for customers who need a way to check the current state of a
    specific Tweet or User at a given moment in time.
-   These API's provide a helpful mechanism that may be used by
    customers who need to check the availability of a piece of Content,
    for instance when:
    1.  Displaying Tweets
    2.  Engaging with a Tweet(s) or User(s) in a 1:1 way
    3.  Distributing Twitter Content to a 3rd party through an allowed
        file download
    4.  Storing Tweets for extended periods of time

#### Compliance Firehose (enterprise only) 

-   Format: Streaming API See: [Compliance
    Firehose](/en/docs/tweets/compliance/api-reference.html) .
-   Delivers realtime stream of [Compliance
    activities](/en/docs/tweets/compliance/guides/compliance-data-objects)
    on Twitter. These activities include when Tweets are edited.
-   May be used to maintain compliance state across a set of stored data
    as new compliance events happen on the platform.
-   Ideal for customers consuming and storing large quantities of
    Twitter data for extended periods of time.
:::
:::
:::
:::
:::
:::
:::
:::
