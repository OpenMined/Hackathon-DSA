::: is-table-default
The Tweet is one of the primary resources on Twitter. In its simplest
form, a Tweet can contain up to 280 characters and can be posted either
publicly or privately, depending on an account's settings. However, a
variety of different objects can also be attached to Tweet, including
media, a place, polls, and URLs. In addition, most Tweets can be edited
for up to 30 minutes after being created.

While there are a variety of different HTTP, selection, and delivery
methods that can deliver, publish, and act upon Tweets, this group of
REST endpoints simply returns a Tweet or group of Tweets, specified by a
[Tweet ID](/content/developer-twitter/en/docs/twitter-ids) . While
simple, these endpoints can be used to receive up-to-date details on a
Tweet, verify that a Tweet is available, and examine its edit history.
These endpoints are also important tools for managing [compliance
events](/content/developer-twitter/content/developer-twitter/en/docs/twitter-api/enterprise/compliance-firehose-api/overview)
.

The Tweet lookup endpoint provides edited Tweet metadata. All objects
for Tweets created since September 29, 2022, include Tweet edit
metadata, even if the Tweet was never edited. Each time a Tweet is
edited, a new Tweet ID is created. A Tweet\'s edit history is documented
by an array of Tweet IDs, starting with the original ID.

This endpoint will always return the most recent edit, along with any
edit history. Any Tweet collected after its 30-minute edit window has
expired will represent its final version. To learn more about Edit Tweet
metadata, check out the [Edit Tweets
fundamentals](https://developer.twitter.com/content/developer-twitter/en/docs/twitter-api/edit-tweets)
page.

These endpoints utilize the GET HTTP method and return one or many
[Tweet
objects](/content/developer-twitter/en/docs/twitter-api/data-dictionary/object-model/tweet)
, which include fields such as the Tweet text, a timestamp from when it
was created, and lists and metadata of hashtags, mentions, and photos,
and more.\
:::
