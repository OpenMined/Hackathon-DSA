::: is-table-default
[ Standard ]{.subscription-tag .subscription-tag--standard}

## Standard stream messages

In addition to [standard Tweet
payloads](/en/docs/tweets/data-dictionary/overview/tweet-object.html) ,
the following kinds of messages may be delivered on a stream. Note that
this list may not be comprehensive---additional objects may be
introduced into streams. Ensure that your parser is tolerant of
unexpected message formats.

When parsing Tweets, keep in mind that Retweets are streamed as a status
with another status nested inside it. If you are matching Tweet fields
using regular expressions, it is possible that you will match fields in
the nested Tweet instead of the wrapper. As a rule of thumb it is better
to use a JSON parser to extract information from message payloads.

### [Maintenance Messages]{.underline}

### Blank lines

On slow streams, some messages may be blank lines (\\r\\n or similar)
which serve as "keep-alive" signals to prevent clients and other network
infrastructure from assuming the stream has stalled and closing the
connection.

### Limit notices (limit)

These messages indicate that a filtered stream has matched more Tweets
than its current rate limit allows to be delivered. Limit notices
contain a total count of the number of undelivered Tweets since the
connection was opened, making them useful for tracking counts of track
terms, for example. Note that the counts do not specify which filter
predicates undelivered messages matched.

::: payload
{ \"limit\":{ \"track\":1234 }

}
:::

### Disconnect messages (disconnect)

Streams may be shut down for a variety of reasons. The streaming API
will attempt to deliver a message indicating why a stream was closed.
Note that if the disconnect was due to network issues or a client
reading too slowly, it is possible that this message will not be
received.

::: payload
{ \"disconnect\":{ \"code\": 4, \"stream_name\":\"\", \"reason\":\"\" }

}
:::

The following table lists possible status codes and their meanings.
Additional codes may be used without warning.

  ------ ------------------- ---------------------------------------------------------------------------------------------------------------------------
  Code   Name                Description
  1      Shutdown            The feed was shutdown (possibly a machine restart)
  2      Duplicate stream    The same endpoint was connected too many times.
  4      Stall               The client was reading too slowly and was disconnected by the server.
  5      Normal              The client appeared to have initiated a disconnect.
  7      Admin logout        The same credentials were used to connect a new stream and the oldest was disconnected.
  9      Max message limit   The stream connected with a negative count parameter and was disconnected after all backfill was delivered.
  10     Stream exception    An internal issue disconnected the stream.
  11     Broker stall        An internal issue disconnected the stream.
  12     Shed load           The host the stream was connected to became overloaded and streams were disconnected to balance load. Reconnect as usual.
  ------ ------------------- ---------------------------------------------------------------------------------------------------------------------------

###  Stall warnings (warning)

When connected to a stream using the stall_warnings parameter, you may
receive status notices indicating the current health of the connection.
See the
[stall_warnings](/en/docs/tweets/rules-and-filtering/overview/basic-operators.html)
documentation for more information.

::: payload
{ \"warning\":{ \"code\":\"FALLING_BEHIND\", \"message\":\"Your
connection is falling behind and messages are being queued for delivery
to you. Your queue is now over 60% full. You will be disconnected when
the queue is full.\", \"percent_full\": 60 }

}
:::

### [Compliance Messages]{.underline}

### Status deletion notices (delete)

These messages indicate that a given Tweet has been deleted. Client code
***must honor these messages*** by clearing the referenced Tweet from
memory and any storage or archive, even in the rare case where a
deletion message arrives earlier in the stream than the Tweet it
references.

::: payload
{ \"delete\":{ \"status\":{ \"id\":1234, \"id_str\":\"1234\",
\"user_id\":3, \"user_id_str\":\"3\" } }

}
:::

### Location deletion notices (scrub_geo)

These messages indicate that geolocated data must be stripped from a
range of Tweets. Clients ***must honor these messages*** by deleting
geocoded data from Tweets which fall before the given status ID and
belong to the specified user. These messages may also arrive before a
Tweet which falls into the specified range, although this is rare.

::: payload
{ \"scrub_geo\":{ \"user_id\":14090452, \"user_id_str\":\"14090452\",
\"up_to_status_id\":23260136625, \"up_to_status_id_str\":\"23260136625\"
}

}
:::

### Withheld content notices (status_withheld, user_withheld) [](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#withheld-content-notices-status-withheld-user-withheld)

These messages indicate that either the indicated Tweet or indicated
user has had their content withheld.

#### status_withheld [](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#status-withheld)

These events contain an id field indicating the status ID,
a user_id indicating the user, and a collection
of withheld_in_countries uppercase two-letter country codes. This
example illustrates a hypothetical Tweet that has been withheld in
Germany and Argentina.

::: payload
{ \"status_withheld\":{ \"id\":1234567890, \"user_id\":123456,
\"withheld_in_countries\":\[\"DE\", \"AR\"\] }

}
:::

#### user_withheld [](https://aem-author-staging.twitter.biz/editor.html/content/developer-twitter/en_US/docs/imported/developer-twitter-com/streaming/overview/messages-types.html#user-withheld)

These events contain an id field indicating the user ID and a collection
of withheld_in_countries uppercase two-letter country codes. This
example illustrates a hypothetical user who has been withheld in Germany
and Argentina.

::: payload
{ \"user_withheld\":{ \"id\":123456,
\"withheld_in_countries\":\[\"DE\",\"AR\"\] }

}
:::

### 
:::
