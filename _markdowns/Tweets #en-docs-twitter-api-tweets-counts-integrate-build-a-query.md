::: is-table-default
When you start to build your query, it is important to keep a few things
in mind.

-   Using broad, standalone operators for your query such as a single
    keyword or #hashtag is generally not recommended since it will
    likely match on a massive volume of Tweets. Creating a more robust
    query will result in a more specific set of matching Tweets, and
    will hopefully increase the accuracy of your Tweet counts to help
    you find more valuable insights.
    -   For example, if your query was just the keyword [ happy
        ]{.code-inline} you will likely get anywhere from 200,000 -
        300,000 Tweets per day.
    -   Adding more conditional operators narrows your results, for
        example [ (happy OR happiness) place_country:GB -birthday
        -is:retweet ]{.code-inline}
-   Writing efficient queries is also beneficial for staying within the
    characters query length restriction. The character count includes
    the entire query string including spaces and operators.
    -   For example, the following query is 59 characters long: [ (happy
        OR happiness) place_country:GB -birthday -is:retweet\
        ]{.code-inline}

####  Quote Tweet matching behavior []{#quote-tweets}

When using the Tweet counts endpoints, operators will not match on the
content from the original Tweet that was quoted, but will match on the
content included in the Quote Tweet.

However, please note that [filtered
stream](/en/docs/twitter-api/tweets/filtered-stream) will match on both
the content from the original Tweet that was quoted and the Quote
Tweet\'s content.\

#### Iteratively building a query []{#iterative}

##### Test your query early and often

Getting a query to return the \"right\" results the first time is rare.
There is so much on Twitter that may or may not be obvious at first and
the query syntax described above may be hard to match to your desired
query.

As you build a query, it is important for you to periodically test it
out using one of the [Search Tweet](/en/docs/twitter-api/tweets/search)
endpoints to ensure that the Tweets that are matching your query are
relevant to your use case.

For this section, we are going to start with the following query and
adjust it based on the results that we receive during our test:

[ happy OR happiness ]{.code-inline}

##### Use results to narrow the query

As you test the query with Search Tweets, you should scan the returned
Tweets to see if they include the data that you are expecting and hoping
to receive. Starting with a broad query and a superset of Tweet matches
allows you to review the result and narrow the query to filter out
undesired results.

When we tested the example query, we noticed that we were getting Tweets
in a variety of different languages. In this situation, we want to only
receive Tweets that are in english, so we're going to add the [ lang:
]{.code-inline} operator:

[ (happy OR happiness) lang:en ]{.code-inline}

The test delivered a number of Tweets wishing people a happy birthday,
so we are going to add [ -birthday ]{.code-inline} as a negated keyword
operator. We also want to only receive original Tweets, so we've added
the negated [ -is:retweet ]{.code-inline} operator:

[ (happy OR happiness) lang:en -birthday -is:retweet ]{.code-inline}

##### Adjust for inclusion where needed

If you notice that you are not receiving data via Search Tweets that you
expect and know that there are existing Tweets that should return, you
may need to broaden your query by removing operators that may be
filtering out the desired data.

For our example, we noticed that there were other Tweets in our personal
timeline that expressed the emotion that we are looking for and weren't
included in the test results. To ensure we have greater coverage, we are
going to add the keywords, [ excited ]{.code-inline} and [ elated
]{.code-inline} .

[ (happy OR happiness OR excited OR elated) lang:en -birthday
-is:retweet ]{.code-inline}

##### Adjust for popular trends/bursts over the time period

Trends come and go on Twitter quickly. Maintaining your query should be
an active process. If you plan to use a query for a while, we suggest
that you periodically check in on the data that you are receiving to see
if you need to make any adjustments.

In our example, we notice that we started to receive some Tweets that
are wishing people a "happy holidays". Since we don't want these Tweets
included in our results, we are going to add a negated [ -holidays
]{.code-inline} keyword.

[ (happy OR happiness OR excited OR elated) lang:en -birthday
-is:retweet -holidays ]{.code-inline}

Once you\'ve properly tested and iterated upon your query, you can start
sending it with the Tweet counts endpoints to start to receive just the
volume of Tweets rather than the full Tweet payloads.

### []{#adding-a-query} Adding a query to your request

To add your query to your request, you must use the [ query
]{.code-inline} parameter. As with any query parameters, you must make
sure to HTTP encode the query that you developed.

Here is an example of what this might look like using a cURL command. If
you would like to use this command, please make sure to replace [
\$BEARER_TOKEN ]{.code-inline} with your own [Bearer
Token](/en/docs/authentication/oauth-2-0) :
:::
