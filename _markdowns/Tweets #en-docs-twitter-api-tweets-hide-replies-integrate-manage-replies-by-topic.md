::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Through the hide replies endpoint, you can build integrations to help
people and brands keep their conversation on topic. This page shows how
to manage a conversation using the hide replies and [recent
search](/en/docs/twitter-api/tweets/search/introduction.html) endpoints.

Recent search has functionality to a conversation and its replies, and
the Tweet payload returns [Tweet
annotations](/en/docs/twitter-api/annotations.html) to help you
understand the context and topic of each Tweet, regardless of language.

The app\'s flow will have controls to display and manage a conversation:

1.  It asks the user's permission to read their Tweets and manage their
    replies.
2.  It pulls a recent conversation from a Tweet URL, and checks that the
    conversation is from the authenticating user.
3.  It will call the recent search endpoint to display each Tweet in the
    conversation. The request will include a conversation ID search
    query and the annotation expansion to determine if the Tweet is
    sports-related or not, according to Twitter\'s interpretation of the
    Tweet.
4.  It calls Hide replies to hide a reply when the user chooses to do
    so. It will also provide a way to undo this action in case, so that
    the user is always in control.\
5.  For longer conversations, it will provide controls to [paginate
    through search
    results](/en/docs/twitter-api/tweets/search/integrate/paginate.html)
    .\
:::
:::

::: c01-rich-text-editor
::: is-table-default
You can design a flow in a way that puts the user in control of any
action they intend to make. Keeping this principle in mind also helps
you build an integration that can optimize for Tweet consumption.

1.  Because the authenticated user can only manage conversations they
    started, your flow should terminate early when that\'s not the case.
    -   Make an initial Tweet lookup request. Terminate the flow early
        if the Tweet URL is not valid or the conversation was not
        started by the authenticating user.
    -   This way, your app doesn\'t have to make a recent search request
        if the conversation cannot be moderated by the authenticated
        user.
2.  Request [user and Tweet fields](/en/docs/twitter-api/fields.html) in
    the same request to avoid making separate requests. This approach
    can also improve your app\'s performance.
3.  Avoid making requests when needed. This app caches a reply\'s hidden
    status in the user\'s browser. This is useful for larger
    conversations, where the user may want to pick up their moderation
    efforts at a later stage, and it helps your app optimize requests to
    hide or unhide replies.
:::
:::
:::
:::
:::
:::
:::
:::
