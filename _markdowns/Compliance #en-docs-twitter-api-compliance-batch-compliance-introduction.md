::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
Twitter is committed to our community of developers who build with the
Twitter API. As part of this commitment, we aim to make our API open and
fair to developers, safe for people on Twitter, and beneficial for the
Twitter platform as a whole. It is crucial that any developer who stores
Twitter content offline, ensures the data reflects user intent and the
current state of content on Twitter. For example,when someone on Twitter
deletes a Tweet or their account, protects their Tweets, or scrubs the
geo information from their Tweets, it is critical for both Twitter and
our developers to honor that person's expectations and intent. The batch
compliance endpoints provide developers an easy tool to help maintain
Twitter data in compliance with the [Twitter Developer Agreement and
Policy](https://developer.twitter.com/en/developer-terms/policy) .

These batch compliance endpoints allow you to upload large datasets of
Tweet or user IDs to retrieve their compliance status in order to
determine what data requires action in order to bring your datasets into
compliance. Please note, use of the batch compliance endpoints is
restricted to aforementioned use cases, and any other purpose is
prohibited and may result in enforcement action.
:::
:::

::: c01-rich-text-editor
::: is-table-default
Typically, there are 4 steps involved in working with this endpoint:

1.  **Create a compliance job**\
    You can specify the job type (with the value [ tweets
    ]{.code-inline} or [ users ]{.code-inline} to indicate whether the
    dataset you want to upload has Tweet IDs or user IDs. You can have
    one concurrent job per job type at any time.

2.  **Upload your dataset to the [ upload_url ]{.code-inline}**\
    Next, you upload your dataset as a plain text file to the provided [
    upload_url ]{.code-inline} , with each line of the file containing a
    single Tweet ID or user ID. The [ upload_url ]{.code-inline} expires
    after 15 minutes.

3.  **(Optional) Check the job status**\
    You can check the status of your compliance job to see whether it is
    [ created ]{.code-inline} , [ in_progress ]{.code-inline} , [ failed
    ]{.code-inline} or [ complete ]{.code-inline} .

4.  **Download the results**\
    When your job is complete, you can download the results using the [
    download_url ]{.code-inline} . The [ download_url ]{.code-inline}
    expires after one week (from when the job was created).

    This result will contain a set of JSON objects (one object per
    line). Each object will contain a Tweet ID, the Tweet's creation
    date (useful to locate Tweets organized by date), required action,
    the reason for the compliance action, and the date the user was
    suspended.

You will receive the following compliance event types in your results:

-   [ deleted ]{.code-inline} - indicates that the Tweet or User account
    was deleted
-   [ deactivated ]{.code-inline} - indicates that the Tweet or User
    account has been deactivated
-   [ scrub_geo ]{.code-inline} - indicates that the geo information
    associated with the Tweet or User was removed
-   [ protected ]{.code-inline} - indicates the account that made the
    Tweet became private
-   [ suspended ]{.code-inline} - indicates the account that made the
    Tweet was suspended
:::
:::

::: dtc09-callout-text
::: dtc09-callout-text
:::
:::
:::
