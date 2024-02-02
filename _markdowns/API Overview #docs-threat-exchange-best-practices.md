<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
This guide explains some ways to use ThreatExchange that will help
improve throughput and usage.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
When you get access to new data in ThreatExchange (such as by being
added to a PrivacyGroup), we recommend you get a sample or complete copy
of the data to evaluate it.

You can use these APIs and UI:

::: {._57yz ._57z1 ._3-8p}
::: _57y-
Only some of them should be used for automated integration into your own
systems, and the others should be used only for sampled evaluation and
testing.
:::
:::

### Sample CSVs from the UI {#sample-csvs}

Some privacy groups have a feature where samples of indicators can be
downloaded from the UI, which is the fastest way to evaluate potential
data. Learn more at [ThreatExchange
UI.](/docs/threat-exchange/reference/ui/collaborations)

### Sampling from /threat_descriptors API {#threat-descriptors-api}

[The /threat_descriptors
API](/docs/threat-exchange/reference/apis/threat-descriptors) allows you
to do complex searches on ThreatDescriptors. This can be useful to
generate your own narrow samples, but the API is not guaranteed to be
contain all data that matches the filters.

**Recommended** --- [The
/threat_updates](/docs/threat-exchange/reference/apis/threat-updates)
API allows you to exactly reproduce a
[ThreatPrivacyGroup](/docs/threat-exchange/reference/apis/threat-privacy-group/)
\'s contents. It also allows you to get deletion events as long as you
poll within 30 days of the object being deleted. Tailing /threat_updates
gives you the lowest latency, complete data, and is the only API that
notifies of deletes.

Not all PrivacyGroups have this API enabled, reach out to
threatexchange@meta.com for questions about enabling it.

### /\<TAG_ID\>/tagged_objects API {#tagged-objects-api}

The
[/\<TAG_ID\>/tagged_objects](/docs/threat-exchange/reference/apis/threattags)
API allows you to reliably download all ThreatDescriptors tagged with
those tags. Because most data is tagged, this is a reliable way to get
data. However, you must do client-side filtering to remove unwanted
data, but with the same tags (for example, in the wrong privacy group,
wrong type, etc). Additionally, because you don\'t learn of deletions or
updates, you must start over from ` tagged_since=0 ` at some interval
(for example, 30 days) in order get updates and discard data that has
been deleted.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
By [tagging your data](/docs/threat-exchange/reference/apis/threattags/)
, it makes it easier for yourself and others to find the indicators they
care most about. For example, by tagging descriptors with ` evil ` ,
this allows others to filter descriptors searches by data with that tag.
Another option is that you can then search the ` threat_tags ` endpoint
by that tag and see all the tagged objects visible to you. The tagging
endpoint also supports partial matches on tags, so a query for ` evil `
will surface any tags visible to you which are like ` evil* ` .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
ThreatTags (also known as \"subjective tags\") contain metadata fields
describing what they are. If you create the tag ` foo ` , others can
inspect the metadata to see what means or why the data was tagged. But
it\'s helpful to be more descriptive instead; for example,
` campaign_zeusbotnet ` or ` malicious_ssl_cert ` .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
ThreatTags are visible based on the
[PrivacyType](/docs/threat-exchange/reference/apis/privacy-type/) of the
tagged data. For example, if the tag ` public_tag ` is on ANY descriptor
that is publically visible (privacy type of VISIBLE), then the tag is
visible to all members. Conversely, if the tag ` nonpublic_tag ` is ONLY
on tagged objects shared to specific members (privacy types
\`HAS_WHITELIST\` or \`HAS_PRIVACY_GROUP\`), then the tag is only
visible to those members. Tag your data accordingly. Learn more about
[PrivacyType tag](/docs/threat-exchange/reference/apis/privacy-type/) .

For more uses cases with ThreatTags, see the [ThreatTag
reference](/docs/threat-exchange/reference/apis/threattags/) .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Batch requests allow you to make multiple requests to the Graph API
using a single HTTP call. For more information on Graph API Batch
Requests, review the following:

-   ::: fcb
    [Making multiple API
    requests](/docs/graph-api/making-multiple-requests)
    :::

-   ::: fcb
    [Batch requests
    documentation](/docs/reference/ads-api/batch-requests)
    :::

You can also query for multiple objects by ID using the following
syntax:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.8/?ids=[id1,id2]&amp;access_token=<access_token>
```

If you need to query for a specific field:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.8/?ids=[id1,id2]&amp;fields=field1,field2&amp;access_token=<access_token>
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
It can sometimes be more efficient to include various nested fields or
related objects in your search results. The following syntax shows how,
for the ` facebook.com ` indicator object, to pull all of its
descriptors without issuing additional API calls:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.8/788497497903212?fields=descriptors{owner,description,status,share_level},indicator,type&amp;access_token=<access_token>

RESULT:
{
  "descriptors": {
    "data": [
      {
        "owner": {
          "id": "820763734618599",
          "name": "Facebook Administrator"
        },
        "description": "Facebook",
        "status": "NON_MALICIOUS",
        "share_level": "GREEN",
        "id": "834469179976904"
      },
      {
        "owner": {
          "id": "588498724619612",
          "name": "Facebook CERT ThreatExchange"
        },
        "description": "Non malicious",
        "status": "NON_MALICIOUS",
        "share_level": "GREEN",
        "id": "1202389109786630"
      }
    ],
    "paging": {
      "cursors": {
        "before": "ODM0NDY5MTc5OTc2OTA0",
        "after": "MTIwMjM4OTEwOTc4NjYzMAZDZD"
      }
    }
  },
  "indicator": "facebook.com",
  "type": "DOMAIN",
  "id": "788497497903212"
}
```
:::
:::

</div>

</div>
