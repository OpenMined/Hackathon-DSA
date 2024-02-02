::: {._4-u3 ._588p}
::: {._57yz ._57z1 ._3-8p}
::: _57y-
This call is not currently enabled for all PrivacyGroups. A 500 error
will be returned if this call is used with PrivacyGroup that doesn\'t
have \`/threat_updates\` enabled. If you would like to enable this call
for your PrivacyGroup please [contact the ThreatExchange
team](mailto:threatexchange@fb.com) .
:::
:::

ThreatExchange provides [multiple
APIs](/docs/threat-exchange/reference/apis/) for querying data. Most of
these APIs will only allow you to know the current state of the object,
and if it is later updated or removed, you can only learn of changes by
polling the objects again. ThreatExchange API integration works best
when you can keep an up-to-date copy of the information that you are
interested in, and re-polling all data would be cumbersome.

` /threat_updates ` provides a solution to keeping a copy of data within
a PrivacyGroup, specifically for the data that users tell us they most
need kept up to date. ` /threat_updates ` allows for a specific
projection of the ThreatExchange graph database to turn it into a list
of signals with opinions. By tailing ` /threat_updates ` , you can learn
of updates to that projection within seconds, and so the liveness of the
data is only limited by how frequently you poll.

When data in the PrivacyGroup is updated, an event is moved to the
\"end\" of the update list. All updates are ordered by ` update_time ` ,
and you can save this time to resume fetching from where you left off.

## Update Events

` /threat_updates ` entries represent one of two events, which can be
differentiated using the ` should_delete ` flag.

::: _57-c
Event
:::
:::

` should_delete `

Meaning

Update

false

An opinion connected to the ThreatIndicator has been created or updated.
Fetch connected data to get updates.

Delete

true

A ThreatIndicator has been removed from the PrivacyGroup or deleted.

Otherwise, entries returned by this API behave as [ThreatIndicator
Objects](/docs/threat-exchange/reference/apis/threat-indicator/) , with
additional fields described below.

## Delete Event TTL, Polling Frequency, and Checkpointing

Deletion events **are only stored for 90 days** , and so you must poll
more frequently than that, or your copy of the database will become
invalid. We generally recommend polling daily to prevent a large backlog
of updates from accruing, and many platforms will want to poll more
frequently than that to have a lower latency between sharing and
ingestion. We don\'t recommend polling more frequently than 1/minute.

To resume from where you last left off, set the ` start_time ` to the
largest ` update_time ` you have previously seen. It is important that
you not attempt to use the time you completed your last fetch as the
checkpoint, as there may be a small delay between when updates are
written and when they appear in ` /threat_updates ` .

` start_time ` is inclusive, so you may see updates you have already
seen when there is not much activity in a PrivacyGroup.

::: {._57yz ._57z1 ._3-8p}
::: _57y-
This call may reveal indicators that have been removed from the privacy
group. When you recieve notice of a deletion, you should remove it from
your copy of ThreatExchange data, as it may have been previously shared
in error. See [Terms and
Conditions](https://www.facebook.com/legal/threatexchange_terms) for
more.
:::
:::

## Maintaining a copy of data in a PrivacyGroup using ` threat_updates `

The object emitted by ` threat_updates ` is
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator/)
, and has the same fields and connections. However, the connections are
modified such that only data in the given PrivacyGroup are returned.

This allows you to use ` /threat_updates ` as an update stream to keep a
copy of the data, keyed by the ` id ` of the
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator/)
. The simplest way to do this is use the ` fields= ` parameter to fetch
all the data you are interested in connected data, and store the
resultant data.

### Example Table Schema

Here\'s is a sample database table schema you could use (for a single
PrivacyGroup):

::: _57-c
Column
:::

Type

Note

indicator_id

64 bit integer (Primary Key)

An opinion connected to the ThreatIndicator has been created or updated.
Fetch connected data to get updates.

indicator_type

string

The type of the signal (e.g. HASH_MD5). Each type usually needs
type-specific handling, so you could provide a secondary index on (type,
update_time) to checkpoint your own internal processing. This column is
an example of parsing specific data out of the payload for the purposes
of indexing - you may find you are interested in other fields as well.

json_payload

JSON

The raw JSON, including connections fetched by ` fields= ` returned by
the API.

### Updating the Table

In order to build your copy of the database, begin polling at
` start_time=0 ` .

For each entry seen:

-   Update:
    ` UPSERT INTO MyTableForPrivacyGroup VALUES ($response[id], $response[type], $response) `
-   Delete:
    ` DELETE FROM MyTableForPrivacyGroup WHERE indicator_id = $response[id] `

When you completely exhaust ` /threat_updates ` , you should have a
complete and up-to-date copy of the data stored in ThreatExchange.

Store the largest ` update_time ` that you have seen to use as a the
` start_time ` for the next time you fetch, as described above.

## What changes constitute an Update

` /threat_updates ` will generate an update to changes to
[ThreatDescriptor
objects](/docs/threat-exchange/reference/apis/threat-descriptor/) that
have been shared to the PrivacyGroup. Changes to the fields or connected
data will generate an update.

At a minimum, this is:

Note that not every update will appear to have changed data -
` /threat_updates ` only stores the last update to an object, and so
changes that are rapidly undone may not appear to change your copy of
the data. Additionally, if you select only some fields, you will see
updates that don\'t change the fields you selected.

## Open Source Fetching Implementation

Instead of building an implementation from scratch, you can start with
our [Python open source
library](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmain%2Fpython-threatexchange&h=AT1ITz-ZEbJi1WbWUNJ0hDz-h5WZxS0jW5go7YWUoWByFPDSm4nxuDzIftJoQbwd2vbuGT9PHcjb-MJdKTRWf1UbDONoSwQfDFMHPUjVwllXBcCf7PfWlZADTYGtgjMLQBLqBAiDofEW_oun)
which can also be used as a reference implementation.
