::: is-table-default
### Anticipating disconnects and reconnecting

When streaming Tweets, the goal is to stay connected for as long as
possible, recognizing that disconnects may occur. The endpoint provides
a 20-second keep alive heartbeat (it will look like a new line
character). Use this signal to detect if you're being disconnected.

1.  Your code should detect when fresh content and the heartbeat stop
    arriving.
2.  If that happens, your code should trigger a reconnection logic. Some
    clients and languages allow you to specify a read timeout, which you
    can set to 20 seconds.
3.  Your service should detect these disconnections and reconnect as
    soon as possible.

The code samples on the API reference page provide an example of this
reconnect logic.

Once an established connection drops, attempt to reconnect immediately.
If the reconnect fails, slow down your reconnect attempts according to
the type of error experienced:

-   Back off linearly for TCP/IP level network errors. These problems
    are generally temporary and tend to clear quickly. Increase the
    delay in reconnects by 250ms each attempt, up to 16 seconds.
-   Back off exponentially for HTTP errors for which reconnecting would
    be appropriate. Start with a 5 second wait, doubling each attempt,
    up to 320 seconds.
-   Back off exponentially for HTTP 429 errors [ Rate limit exceeded
    ]{.code-inline} . Start with a 1 minute wait and double each
    attempt. Note that every HTTP 429 received increases the time you
    must wait until rate limiting will no longer be in effect for your
    account.\

### Rate limits and usage

To check connection limits response will return three headers. This is
useful to understand how many reconnections attempts are allowed for the
streaming endpoint.

-   [ x-rate-limit-limit ]{.code-inline} indicates the number of
    allotted requests your client is allowed to make during the
    15-minute window.

-   [ x-rate-limit-remaining ]{.code-inline} indicates the number of
    requests made so far in the 15-minute window.

-   [ x-rate-limit-reset ]{.code-inline} is a UNIX timestamp indicating
    when the 15-minute window will restart, [ resetting
    x-rate-limit-remaining ]{.code-inline} to 0.

The sampled stream endpoint does not currently report usage data. To
check how many Tweets have been delivered, your code can implement a
metering logic, so that consumption can be measured and paused if
needed.

Your code that hosts the client side of the stream simply inserts
incoming Tweets into a first in, first out (FIFO) queue, or a similar
memory structure; a separate process/thread should consume Tweets from
that queue to parse and prepare content for storage. With this design,
you can implement a service that can scale efficiently in case incoming
Tweet volumes changes dramatically. Conceptually, you can think of it as
downloading an infinitely long file over HTTP.

### Reconnection best practices

#### Test backoff strategies

A good way to test a backoff implementation is to use invalid
authorization credentials and examine the reconnect attempts. A good
implementation will not get any 429 responses.

#### Issue alerts for multiple reconnects

If a client reaches its upper threshold of its time between reconnects,
it should send you notifications so you can triage the issues affecting
your connection.

#### Handle DNS changes

Test that your client process honors the DNS Time To live (TTL). Some
stacks will cache a resolved address for the duration of the process and
will not pick up DNS changes within the prescribed TTL. Such aggressive
caching will lead to service disruptions on your client as Twitter
shifts load between IP addresses.

#### User Agent

Ensure your user-agent HTTP header includes the client's version. This
will be critical in diagnosing issues on Twitter's end. If your
environment precludes setting the user-agent field, then set an
x-user-agent header.
:::
