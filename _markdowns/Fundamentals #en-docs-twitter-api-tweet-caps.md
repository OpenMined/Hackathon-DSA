::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Twitter API v2 has a Tweet consumption cap that limits the number of
Tweets that you can receive from a set of endpoints on a monthly basis.
Tweet caps apply at the [Project](/en/docs/projects) -level, meaning
that any requests to the endpoints listed below using the keys and
tokens from [developer Apps](/en/docs/apps) within that Project will
count towards the Project Tweet cap.\

### Limited v2 endpoints

Tweets you receive from any of the following endpoints count towards
this monthly Tweet cap:

### Note:

If the same Tweet is returned from multiple queries during the billing
cycle, then the Tweet is only counted once against the monthly cap -
i.e, the Tweets are deduplicated.

**Dedupe** Counter gets reset on a monthly basis  (at the end of the
billing cycle).

### Tweet cap volumes

The Tweet cap volume depends on your access level:

  --------------------- ------------------------------
  **Free** tier         1,500 Tweets per month
  **Basic** tier        10,000 Tweets per month
  **Pro** tier          1,000,000 Tweets per month
  **Enterprise** tier   50+ million Tweets per month
  --------------------- ------------------------------

\
You can check your usage towards the monthly Tweet cap by viewing the
[main dashboard page](/content/developer-twitter/en/portal/dashboard) in
the [developer portal](/en/docs/developer-portal) . Under the name of
your Project, you\'ll see a status bar that illustrates your current
month's usage in relation to the Tweet cap. You will also see the number
of Tweets you pulled this month, the percentage of Tweets used in
relation to the cap, and the date your Tweet cap usage resets.
:::
:::
:::
:::
:::
:::
:::
:::
