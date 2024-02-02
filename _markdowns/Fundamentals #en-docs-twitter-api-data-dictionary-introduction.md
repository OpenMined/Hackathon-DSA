::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Across the Twitter API endpoints, there are a variety of objects
available to request such as Tweets and users. Each GET endpoint will
have a top-level resource and object, such as Tweets in [recent
search](/en/docs/twitter-api/tweets/search/introduction.html) and
[filtered
stream](/en/docs/twitter-api/tweets/filtered-stream/introduction.html) ,
and users in [users
lookup](/en/docs/twitter-api/users/lookup/introduction.html) .

To see each object and it\'s included fields, please visit the
following:

-   [Tweets](/en/docs/twitter-api/data-dictionary/object-model/tweet)
-   [Users](/en/docs/twitter-api/data-dictionary/object-model/user)
-   [Spaces](/en/docs/twitter-api/data-dictionary/object-model/space)
-   [Lists](/en/docs/twitter-api/data-dictionary/object-model/list)
-   [Media](/en/docs/twitter-api/data-dictionary/object-model/media)
-   [Polls](/en/docs/twitter-api/data-dictionary/object-model/poll)
-   [Places](/en/docs/twitter-api/data-dictionary/object-model/place)

### Expanded objects

Additional objects related to the top-level object, such as media,
place, poll, author (user) of the Tweet, and user\'s pinned-Tweet are
available as expansions, which you can request using the [[ expansions
]{.code-inline}](/en/docs/twitter-api/expansions.html) query parameter.\

### Fields: defaults and requesting additional fields

If you make a request without any [[ fields
]{.code-inline}](/en/docs/twitter-api/fields.html) parameters, you will
receive just a few default fields for your top-level object and any
expansion objects. For example, Tweets will return just the [ id
]{.code-inline} and [ text ]{.code-inline} of a Tweet by default. If you
would like to request additional fields, such as the Tweet [ created_at
]{.code-inline} or [ lang ]{.code-inline} fields, you will have to use
the [ fields ]{.code-inline} parameters.\

### Key fields

Other useful fields that you should expect in the Twitter API v2 data
format:

-   [Metrics](/en/docs/twitter-api/metrics.html) available in the Tweet,
    user, Spaces, lists objects
-   [Annotation](/en/docs/twitter-api/annotations.html) topics available
    in the Tweet payload \
-   A new [ [conversation_id](/en/docs/twitter-api/conversation-id)
    ]{.code-inline} field to help you track Tweets included in a
    conversation
-   A new [ reply_settings ]{.code-inline} field to help you understand
    who has the ability to reply to specific Tweets\

### Migrating to the Twitter API v2 data format

Interested in learning more about how the Twitter API v2 data format
compares to standard, premium, or enterprises\' formats? Check out our
data format comparison guides:
:::
:::
:::
:::
:::
:::
:::
:::
