::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
With the hide replies endpoint, you can build a workflow to helps your
users hide replies that have a very high-probability of being
irrelevant.

Useful apps often combine technologies so that they can be valuable to
their users. This page shows how to hide replies by using the
[Perspective API](https://www.perspectiveapi.com/) . This API is an
artificial intelligence trained by [Jigsaw](https://jigsaw.google.com/)
, a unit within Google, to detect toxic comments. The application logic
will work in the following way:

1.  It asks the user's permission to read their Tweets and hide or
    unhide their replies.
2.  It uses the [Account Activity
    API](/en/docs/accounts-and-users/subscribe-account-activity/overview.html)
    to detect incoming replies.
3.  It asks the Perspective API to give a "score" (a number between 0
    and 1) that indicates how confident their algorithm is that a
    comment is similar to toxic comments it's seen in the past.
    (Perspective does not store the text sent to the service).
4.  It calls hide replies if the algorithm's score is very high.

### Strive for transparency

Because Perspective is not trained on actual Tweets, certain language
nuances may cause this app to hide a reply that a user wants to remain
unhidden. Regardless of the technology or the approach you use when
designing your app, always make the best possible effort to ensure that
your users understand what your app has hidden and can make changes.

-   The best option is to always trust the user and to give them full
    control over their decisions. This means your user experience should
    include controls to undo any action taken by your app on behalf of
    the user.
-   When using an artificial intelligence, your app should use a very
    high confidence threshold to detect and hide Tweets.
-   Not everybody uses the same words, and your app should be designed
    to avoid any bias. Be mindful of reclaimed words and slang that may
    lead to false positives.
-   If you are training an artificial intelligence, consider adopting a
    model that closely reflects language often used on Twitter.
:::
:::
:::
:::
:::
:::
:::
:::
