::: is-table-default
The Twitter API has several methods, such as [GET statuses /
user_timeline](/en/docs/tweets/timelines/api-reference/get-statuses-user_timeline.html)
and [GET statuses /
home_timeline](/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline.html)
, which return a timeline of Tweet data. Such timelines can grow very
large, so there are limits to how much of a timeline a client
application may fetch in a single request. Applications must therefore
iterate through timeline results in order to build a more complete list.

Because of Twitter's realtime nature and the volume of data which is
constantly being added to timelines, standard paging approaches are not
always effective. The goal of this page is to demonstrate the issues
Twitter developers may face when paging through result sets and to give
best practices for processing a timeline.

### The problem with "pages"

In an ideal world, paging would be very easy to implement. Consider the
case where a timeline has 10 reverse-chronologically sorted Tweets. An
application might attempt to read the entire timeline in two requests by
setting a page size of 5 elements and requesting the first page, then
the second page.

The problem with this method is that Twitter timelines are constantly
having new Tweets added to their front. Consider the previous example.
If two new Tweets are added to the timeline between the first and second
calls, the second fetch retrieves two Tweets which were returned in the
previous call.

In fact, if 5 or more Tweets were added between calls, subsequent calls
would eventually retrieve all the Tweets returned from the first
request - making an entire API request completely redundant.

### The max_id parameter

The solution to the issue described above is to use a technique for
working with streams of data called cursoring. Instead of reading a
timeline relative to the top of the list (which changes frequently), an
application should read the timeline relative to the IDs of Tweets it
has already processed. This is achieved through the use of
the max_id request parameter.

To use max_id correctly, an application's first request to a timeline
endpoint should only specify a count. When processing this and
subsequent responses, keep track of the lowest ID received. This ID
should be passed as the value of the max_id parameter for the next
request, which will only return Tweets with IDs lower than or equal to
the value of the max_id parameter. Note that since the max_id parameter
is inclusive, the Tweet with the matching ID will actually be returned
again.

### Optimizing max_id for environments with 64-bit integers

While one redundant Tweet is not inefficient, it is still possible to
optimize max_id requests to address this problem if your platform is
capable of working with 64-bit integers. **Environments where a Tweet ID
cannot be represented as an integer with 64 bits of precision (such as
JavaScript) should skip this step.** Subtract 1 from the lowest Tweet ID
returned from the previous request and use this for the value of max_id.
It does not matter if this adjusted max_id is a valid Tweet ID, or if it
corresponds with a Tweet posted by a different user - the value is just
used to decide which Tweets to filter. When adjusted in this manner, it
is possible to page through a timeline without receiving redundant
Tweets.

### Using since_id for the greatest efficiency

Applications which process a timeline, wait some quantity of time, and
then need to process new Tweets which have been added since the last
time the timeline was processed can make one more optimization using
the since_id parameter.

Consider the previous example where Tweets 1 through 10 were processed.
Now imagine that Tweets 11 through 18 were added to the timeline since
the processing in the previous example began. An inefficient approach to
process the new Tweets would be to iterate from the start of the list
until Tweet 10 appeared. This causes two Tweets which have already been
processed to be returned again.

This problem is avoided by setting the since_id parameter to the
greatest ID of all the Tweets your application has already processed.
Unlike max_id the since_id parameter is not inclusive, so it is not
necessary to adjust the ID in any way. As shown in the following image,
Twitter will only return Tweets with IDs higher than the value passed
for since_id.

Applications which use both the max_id and since_id parameters correctly
minimize the amount of redundant data they fetch and process, while
retaining the ability to iterate over the entire available contents of a
timeline.
:::
