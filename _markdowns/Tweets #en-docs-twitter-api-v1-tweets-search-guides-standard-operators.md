::: is-table-default
[ Standard ]{.subscription-tag .subscription-tag--standard}

One way to start testing searches for Tweets, is to first use the
twitter.com/search UI, and build a query there.  There is not complete
parity or completeness between the web interface and the standard search
API, but this can help to get started.

Using the operators below and the search/tweets API, you can iterate on
the result by adding more specificity, or negations to get the desired
results.  As you get a satisfactory result set, the URL loaded in the
browser will contain the proper query syntax that can be reused in the
API endpoint.

Here's an example:\

-   We want to search for Tweets referencing *TwitterDev* , the word
    *new* and the word *premium* . First, we run the search on
    twitter.com/search:
    https://twitter.com/search?q=twitterdev%20new%20premium
-   Replace "https://twitter.com/search" with
    "https://api.twitter.com/1.1/search/tweets.json" and you will get:
    https://api.twitter.com/1.1/search/tweets.json?q=twitterdev%20new%20premium
-   Execute this URL to do the search in the API.

Here\'s an example twurl command:
` twurl /1.1/search/tweets.json?q=twitterdev%20new%20premium `

And the result:

    {
        "statuses": [{
                    "created_at": "Thu Feb 01 16:40:07 +0000 2018",
                    "id": 959104084845453312,
                    "id_str": "959104084845453312",
                    "text": "RT @TwitterAPI: New year, new access for our developer community! \ud83c\udf89\n\nToday, we\u2019re launching our premium Search Tweets: Full-archive endpoin\u2026",
                    "truncated": false,
                    "entities": {
                        "hashtags": [],
                        "symbols": [],
                        "user_mentions": [{
                            "screen_name": "TwitterAPI",
                            "name": "Twitter API",
                            "id": 6253282,
                            "id_str": "6253282",
                            "indices": [3, 14]
                        }],
                        "urls": []
                    },
                    "metadata": {
                        "iso_language_code": "en",
                        "result_type": "recent"
                    },
                    "source": "\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e",
                    "in_reply_to_status_id": null,
                    "in_reply_to_status_id_str": null,
                    "in_reply_to_user_id": null,
                    "in_reply_to_user_id_str": null,
                    "in_reply_to_screen_name": null,
                    "user": {
                        "id": 2244994945,
                        "id_str": "2244994945",
                        "name": "Twitter Dev",
                        "screen_name": "TwitterDev",
                        "location": "Internet",
                        "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/t.co\/mGHnxZU8c1 \u2328\ufe0f #TapIntoTwitter",
                        "url": "https:\/\/t.co\/FGl7VOULyL",
                        "entities": {
                            "u.......

### Important Practices

-    Ensure all parameters are properly URL encoded.
-   Limit your searches to 10 keywords and operators.
-   Queries can be limited due to complexity. If this happens, the
    Search API will respond with the error: {\"error\":\"Sorry, your
    query is too complex. Please reduce complexity and try again.\"}.
-   The Search API is not a complete index of all Tweets, but instead an
    index of recent Tweets. The index includes between 6-9 days of
    Tweets.

**Example searches:**

When you are following an event that's currently happening, you would be
interested in search for recent Tweets using the event hashtag\

You want recent Tweets that contain the hashtag #superbowl

Your search URL is:
https://api.twitter.com/1.1/search/tweets.json?q=%23superbowl&result_type=recent

` twurl /1.1/search/tweets.json?q=%23superbowl&result_type=recent `\

When you want to know what Tweets are coming from a specific location,
with a specific language:

You want: all recent Tweets in Portuguese, near Maracanã soccer stadium
in Rio de Janeiro

Your search URL is:
https://api.twitter.com/1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent

` twurl /1.1/search/tweets.json?q=geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent `\

When you want the most popular tweets of a specific user using a
hashtag:

You want: popular Tweets from \@Cmdr_Hadfield mentioning the hashtag
#nasa

Your search URL is:
https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular

` twurl /1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa&result_type=popular `\

**Standard search operators**\

The query can have operators that modify its behavior.  Below are
examples that illustrate the available operators in standard search:

  ----------------------------------- -----------------------------------------------------------------------------------------------
  Operator                            Finds Tweets\...
  watching now                        containing both "watching" and "now". This is the default operator.
  "happy hour"                        containing the exact phrase "happy hour".
  love OR hate                        containing either "love" or "hate" (or both).
  beer -root                          containing "beer" but not "root".
  #haiku                              containing the hashtag "haiku".
  from:interior                       sent from Twitter account "interior".
  list:NASA/astronauts-in-space-now   sent from a Twitter account in the NASA list astronauts-in-space-now
  to:NASA                             a Tweet authored in reply to Twitter account "NASA".
  \@NASA                              mentioning Twitter account "NASA".
  politics filter:safe                containing "politics" with Tweets marked as potentially sensitive removed.
  puppy filter:media                  containing "puppy" and an image or video.
  puppy -filter:retweets              containing "puppy", filtering out retweets
  puppy filter:native_video           containing "puppy" and an uploaded video, Amplify video, Periscope, or Vine.
  puppy filter:periscope              containing "puppy" and a Periscope video URL.
  puppy filter:vine                   containing "puppy" and a Vine.
  puppy filter:images                 containing "puppy" and links identified as photos, including third parties such as Instagram.
  puppy filter:twimg                  containing "puppy" and a pic.twitter.com link representing one or more photos.
  hilarious filter:links              containing "hilarious" and linking to URL.
  puppy url:amazon                    containing "puppy" and a URL with the word "amazon" anywhere within it.
  superhero since:2015-12-21          containing "superhero" and sent since date "2015-12-21" (year-month-day).
  puppy until:2015-12-21              containing "puppy" and sent before the date "2015-12-21".
  movie -scary :)                     containing "movie", but not "scary", and with a positive attitude.
  flight :(                           containing "flight" and with a negative attitude.
  traffic ?                           containing "traffic" and asking a question.
  ----------------------------------- -----------------------------------------------------------------------------------------------

Please, make sure to [URL
encode](http://en.wikipedia.org/wiki/URL_encoding) these queries before
making the request. There are several online tools to help you to do
that, or you can search at twitter.com/search and copy the encoded URL
from the browser's address bar. The table below shows some example
mappings from search queries to URL encoded queries:

  ----------------- -----------------------------
  Search query      URL encoded query
  #haiku #poetry    %23haiku+%23poetry
  "happy hour" :)   %22happy%20hour%22%20%3A%29
  ----------------- -----------------------------

Note that the space character can be represented by "%20" or "+" sign.\

## Additional parameters

There is a set of additional parameters that allows a better control of
the search results. The [standard search API
reference](/content/developer-twitter/en/docs/tweets/search/api-reference/get-search-tweets)
documentation has detailed information about the usage of the
parameters, this section will only give a brief description of their
capabilities:

-   **Result Type** : just like twitter.com/search results,
    the result_type parameter selects whether the result set will be
    represented by recent or popular Tweets, or even a mix of both.
-   **Geolocalization** : the search operator "near" isn't available in
    the API, but there is a more precise way to restrict your query by a
    given location using the geocode parameter specified with the
    template "latitude,longitude,radius", for example,
    "37.781157,-122.398720,1mi". When conducting geo searches, the
    search API will first attempt to find Tweets which have lat/long
    within the queried geocode, and in case of not having success, it
    will attempt to find Tweets created by users whose profile location
    can be reverse geocoded into a lat/long within the queried geocode,
    meaning that is possible to receive Tweets which do not include
    lat/long information.
-   **Language** : the lang parameter restricts Tweets to the given
    language.
-   **Iterating in a result set** : parameters
    such count, until, since_id, max_id control iteration through search
    results, since it could be a large set of Tweets. The [Working with
    Timelines](/en/docs/tweets/timelines/guides/working-with-timelines.html)
    documentation is a rich and illustrative tutorial to learn how to
    use these parameters to achieve the best efficiency and reliability
    when processing result sets.
:::
