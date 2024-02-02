::: is-table-default
**The number of Tweets I receive with the data endpoint doesn\'t match
the number of Tweets identified by the counts endpoint. Why is this the
case?**

There is a known difference between results provided by the counts
endpoint and the data endpoint. You may see a discrepancy in your
results because the counts endpoint is pre-compliance (meaning that it
does not account for things like deleted Tweets, scrub geo, etc.)
whereas the data endpoint is compliant at the time of delivery and
accounts for all compliance events. For further reference, please go to
[this
document](/content/developer-twitter/en/docs/tweets/search/api-reference/premium-search#CountsEndpoint)
on our support site.

**\
I didn\'t receive a Tweet that should match my query. Why?**

There are a few different reasons why this might have happened,
including

1.  the Tweet you expected to see is from a protected account
2.  because the data endpoint accounts for all compliance events
    (meaning that deleted Tweets, scrubbed geos, etc. will not be
    included in the response).

**\
My query matched a Tweet but includes a keyword that I negated. Why is
this happening?**

This is likely due to a wrong usage of our premium rules & filtering.
Please review our documentation
[here](/en/docs/tweets/rules-and-filtering/guides/using-premium-operators)
and ensure you understand the restrictions around building rules.

**\
Are there any libraries that I can use to get started using the Search
Tweet APIs?**

Yes, there are, including:

-   [Tweepy](http://www.tweepy.org/) - good for using the standard
    search/tweets product (Python)
-   [Twitter API](https://github.com/geduldig/TwitterAPI) - good for
    using both the standard and premium Search Tweet APIs (Python)
-   [Search Tweets
    Python](https://github.com/twitterdev/search-tweets-python) and
    [Search Tweets
    Ruby](https://github.com/twitterdev/search-tweets-ruby) - two good
    tools that can be used for both premium and enterprise (and v2!)
    Search Tweet APIs

All of the libraries that we directly support can be found on our
TwitterDev GitHub page: <https://github.com/twitterdev> .

There are [other third-party
libraries](/en/docs/developer-utilities/twitter-libraries) that may also
be helpful; however, please note that some of these may not work with
our premium and enterprise products.

**\
Will I ever receive less volume of Tweets than the value I set as the
` maxResults ` in my request to the data endpoint?**

Yes. Our data endpoint paginates at either the specified ` maxResults `
or after 30 days.

For example, if you have 800 Tweets in a given 30 day period, you will
have to make two requests to pull the complete results; because the
maximum number of Tweets that can be returned per request is 500 (
` maxResults ` ). And if you just have 400 Tweets in month one, and then
100 Tweets in month two, you will also have to use two requests to pull
the full results; because pagination takes place after a period of 30
days even if the first request returns less than the specified
` maxResults ` Tweets.

**\
In what order are the matching Tweets returned?**

Tweets are returned in reverse chronological order. For example, the
first page of results will show the most recent Tweets that match the
query, pagination will continue until the results posted dates get to
the ` fromDate ` initially requested.

** How do Edit Tweets impact my usage and billing?**

Only the original Tweet will count for billing purposes. Any subsequent
edits will be ignored and not contribute to your overall activity count.

[]{#enterprise} [ Enterprise ]{.subscription-tag
.subscription-tag--enterprise}

**I\'m interested in learning more about the pricing of the enterprise
Search Tweet API and in applying for this offering. How can I do this?**

Our enterprise solutions are customized with predictable pricing to meet
the needs of your business. Please apply
[here](/content/developer-twitter/en/enterprise-application) for more
information.

**\
How do I build a rule set that matches my use case?**

-   Please refer to our enterprise Search Tweet APIs documentation
    [here](/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search)
-   Useful information on rules and filering can be found
    [here](/content/developer-twitter/en/docs/twitter-api/enterprise/rules-and-filtering/guides/using-enterprise-operators)
-   Useful information for using the data endpoint can be found
    [here](/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search#DataEndpoint)
-   Useful information for using the counts endpoint can be found
    [here](/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/api-reference/enterprise-search#CountsEndpoint)
-   A list of available operators can be found
    [here](/content/developer-twitter/en/docs/twitter-api/enterprise/search-api/overview#AvailableOperators)

**\
I have exceeded my request caps/limits for the month, but I need to
access more data - what can I do?**

Please get in touch with your Account Manager at Twitter who will be
able to help you with this.

### []{#troubleshooting} Error troubleshooting guide

**Code 404 - Not Found**

1.  Please ensure you are using the right parameters for each endpoint
    (e.g. the ` buckets ` field can only be used with the counts
    endpoint, not the data endpoint)
2.  Please double check the ` :product ` ` :account_name ` and
    ` :label ` fields are correct. You can find your ` :label ` field in
    the GNIP Console (enterprise customers only).

l
:::
