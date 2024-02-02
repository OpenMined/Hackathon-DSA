::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Twitter is committed to our community of developers who build with the
Twitter API. As part of this commitment, we aim to make our API open and
fair to developers, safe for people on Twitter, and beneficial for the
Twitter platform as a whole. It is crucial that any developer who stores
Twitter content offline, ensures the data reflects user intent and the
current state of content on Twitter. For example, when someone on
Twitter deletes a Tweet or their account, protects their Tweets, edits a
Tweet, or scrubs the geo information from their Tweets, it is critical
for both Twitter and our developers to honor that person's expectations
and intent.

Real-time streams of compliance events provide developers the tools to
maintain Twitter data in compliance with the [Twitter Developer
Agreement and
Policy](https://developer.twitter.com/en/developer-terms/policy) .

There are two c *ompliance event* streams, one for *Tweet compliance*
events, and one for *User compliance* events. These streams are
available with Enterprise access and are designed to help partners that
ingest high volumes of data \'listen\' for compliance events such as
Tweet edit events.

These streams provide the following events:

**Tweet compliance stream:**

-   [ delete ]{.code-inline} - indicates that the Tweet was deleted.

-   [ tweet_edit ]{.code-inline} - indicates a Tweet has been edited and
    provides the ID of the updated Tweet.

-   [ withheld ]{.code-inline} - indicates that the Tweet has been
    withheld from one or more countries.

-   [ drop ]{.code-inline} - indicates that the Tweet should be removed
    from public view.\

-   [ undrop ]{.code-inline} - indicates that the Tweet may be displayed
    again and treated as public.

**User compliance stream:**\

-   [ user_delete ]{.code-inline} - indicates that the User account was
    deleted

-   [ user_undelete ]{.code-inline} - indicates that the User account
    was undeleted

-   [ user_protect ]{.code-inline} - indicates that the User account
    became private

-   [ user_unprotect ]{.code-inline} - indicates that the User account
    became public

-   [ user_withheld ]{.code-inline} - indicates that the User account
    has been withheld from one or more countries.

-   [ user_suspend ]{.code-inline} - indicates that the User account was
    suspended

-   [ user_unsuspend ]{.code-inline}  - indicates that the User account
    was unsuspended

-   [ user_profile_modification ]{.code-inline} - indicates that the
    User profile has been updated. This includes an updated description,
    name, location, and URL.

```{=html}
<!-- -->
```
-   ****[ scrub_geo ]{.code-inline}**** - indicates that the location
    information associated with the User was removed
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::
:::
