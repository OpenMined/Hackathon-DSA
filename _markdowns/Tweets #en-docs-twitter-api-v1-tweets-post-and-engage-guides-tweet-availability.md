::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
**Tweets, Retweets, Quote Tweets** : A Twitter user can delete a status
at any point in time. Deleted statuses cannot be reversed and are
permanently deleted.  When the original Tweet is deleted, all Retweets
are also deleted. When the original quoted Tweet is deleted, the Quote
Tweet remains.

**Protected accounts** : A Twitter user can protect or unprotect their
account at any time. Protected accounts require manual user approval of
every person who is allowed to view their account\'s Tweets. For more
information, see [About Public and Protected
Tweets](https://help.twitter.com/en/safety-and-security/public-and-protected-tweets)
.

**Nullcasted Tweets** : A type of Tweet that is created through the Ads
API Platform or at ads.twitter.com. Nullcasted Tweets do not appear in
the public timeline and are not served to followers, but they do come
through the firehose when they are created. In the case of a nullcasted
Tweet, the below object will be seen in your enriched native payload. If
a Tweet payload includes this object, it was created on the ads
platform; however, not all promoted Tweets include this metadata.
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 "scopes": {
  "followers": false
}
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
