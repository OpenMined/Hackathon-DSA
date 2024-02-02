::: is-table-default
The Twitter API v2 has three timelines endpoints - reverse chronological
home timeline, user Tweet timeline, and user mention timeline. See below
for more details.

These three timelines endpoints support edited Tweets. These endpoints
will always return the most recent edit, along with the edit history.
Any Tweet collected after its 30-minute edit window will represent its
final version. Edit metadata includes an array of IDs for all Tweets in
its history. For Tweets with no edit history, this array will hold a
single ID. For Tweets that have been edited, this array contains
multiple IDs, arranged in ascending order reflecting the order of edits,
with the most recent version in the last position of the array. To learn
more about how Tweet edits work, see the [Edit Tweets
fundamentals](/en/docs/twitter-api/edit-tweets) page. \

### Reverse chronological home timeline

This endpoint enables you to retrieve the most recent Tweets, Retweets,
and replies posted by the authenticated user and the accounts they
follow.

Since you are making requests on behalf of a user, you must authenticate
these endpoints using an [OAuth 2.0 Authorization Code Flow with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
or [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
. This endpoint has a per-user rate limit of 180 requests per 15-minute
window. This endpoint can return every Tweet created on a timeline over
the last 7 days as well as the most recent 800 regardless of creation
date.

### User Tweet timeline

The user Tweet timeline endpoint provides access to Tweets published by
a specific Twitter account.  Retrieving a user\'s Tweets allows you to
build experiences such as showcasing a timeline in a user interface,
analyzing a user\'s Tweets to better understand their content, or
creating engagement workflows with their Tweets programmatically. This
endpoint gives you access to a single Twitter account\'s most recent
Tweets, Retweets, replies, and Quote Tweets, similar to what may be seen
on a user\'s profile timeline.

Here is a user timeline for \@XDevelopers:

[Tweets by
XDevelopers](https://twitter.com/XDevelopers?ref_src=twsrc%5Etfw){.twitter-timeline}

The user Tweet timeline endpoint is a REST endpoint that receives a
single path parameter to indicate the desired user (by user ID). The
endpoint can return the 3,200 most recent Tweets, Retweets, replies, and
Quote Tweets posted by the user.

Tweets are delivered in reverse-chronological order, starting with the
most recent. Results are
[paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html)
up to 100 Tweets per page. Pagination tokens are provided for paging
through large sets of Tweets. The Tweet IDs of the newest and the oldest
Tweets included in the given page are also provided as metadata, which
can also be used for polling timelines for recent Tweets. The user Tweet
timeline also supports the ability to specify start_time and end_time
parameters to receive Tweets that were created within a certain window
of time.

The user Tweet timeline endpoint supports
[fields](https://developer.twitter.com/en/docs/twitter-api/fields) and
[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions)
parameters, and returns the [new JSON data
format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction)
.

To successfully make a request to this endpoint, you will need to
authorize your request with the [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
, or [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
authentication methods. You must use OAuth 1.0a User Context or OAuth
2.0 Authorization Code with PKCE when requesting nonpublic metrics,
promoted metrics or a protected user\'s timeline.

The user Tweet timeline endpoint is designed to support two common usage
patterns:

-   \"Get a user's historical Tweets\": Requests made to user Tweet
    timeline in order to receive Tweets authored by the user of interest
    in chronological order over a specific recent timeframe. The
    timeframe can be set using the start_time and end_time and
    paginating through the full results.  In some cases, a user's entire
    history of Tweets can be retrieved if the user has only authored up
    to 3,200 Tweets in their account. Tweets included will depend on the
    public availability and the authentication that is used for the
    requests.

-   \"Polling for new Tweets\": Requests made to user Tweet timeline on
    a continual basis, to retrieve new Tweets authored by a specific
    user. The last Tweet ID received can be set as a parameter for any
    new requests since the last Tweet.

### User mention timeline

The user mention timeline endpoint allows you to request Tweets
mentioning a specific Twitter user, for example, if a Twitter account
mentioned \@TwitterDev within a Tweet. This will also include replies to
Tweets by the user requested. Retrieving a user\'s mentions allows you
to build experiences such as quickly discovering who is replying to a
users\' Tweets, mentioning or to create engagement workflows with their
Tweets programmatically. The endpoint allows you to request to a single
user\'s most recent mentions and replies, similar to what may be seen in
a user\'s [notifications for
mentions](https://twitter.com/notifications/mentions) on Twitter.

The user mention timeline is a REST endpoint that receives a single path
parameter to indicate the desired user (by user ID). The endpoint can
return the 800 most recent mentions for that user.

Tweets are delivered in reverse-chronological order, starting with the
most recent. Results are
[paginated](https://developer.twitter.com/en/docs/twitter-api/pagination.html)
in up to 100 Tweets per page. Pagination tokens are provided for paging
through large sets of Tweets. The Tweet IDs of the newest and the oldest
Tweets included in the given page are also provided as metadata, which
can also be used for polling timelines for recent Tweets, or for
navigating through the timeline similar to the v1.1
[mentions_timeline](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-mentions_timeline)
endpoint. The endpoint also supports the ability to specify start_time
and end_time parameters to receive Tweets that were created within a
certain window of time.

To successfully make a request to this endpoint, you will need to
authorize your request with the [OAuth 1.0a User
Context](https://developer.twitter.com/en/docs/authentication/oauth-1-0a)
, [OAuth 2.0 Authorization Code with
PKCE](https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code)
, or [OAuth 2.0
App-Only](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)
authentication methods. You must use OAuth 1.0a User Context or OAuth
2.0 Authorization Code with PKCE when requesting non public metrics,
promoted metrics or a protected user\'s timeline.

The user mention timeline endpoint supports
[fields](https://developer.twitter.com/en/docs/twitter-api/fields) and
[expansions](https://developer.twitter.com/en/docs/twitter-api/expansions)
parameters, and returns the [new JSON data
format](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction)
.
:::
