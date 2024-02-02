<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
ThreatExchange supports creating connections (also known as **edges** or
**relations** ) between
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator)
objects to express relationships. Examples of when this can be useful
are for describing URL redirect chains or domain-to-IP-address
relationships.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
When you connect one descriptor to another, you must own one or the
other.

1.  Within the **View** / **Edit** popup for a given descriptor, you
    need the IDs of the descriptors to connect to. Start with any search
    results. In this case, ` testing-relation-editing ` .
2.  Connect the first one to the next 2.
3.  Select the IDs of the next 2 descriptors and click **Copy IDs to
    clipboard** .
4.  Click **View** / **Edit** on the first descriptor, paste the IDs,
    and then click **Add Relation** \> **OK** .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Just as in the [Use the UI](#using-ui) topic, you can assume that
multiple descriptors are related to another one.

1.  In the next example, do a query for a particular tag (can be any set
    of descriptors).
2.  Click **Bulk relate** .
3.  Supply the ID of the related-to indicator and click **OK** .
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
These are optional columns you can use to bulk-relate (see also [Submit
Data](/docs/threat-exchange/reference/submitting) :

-   The descriptors you want to relate your new one to must already
    exist.
-   You can specify the relate-to descriptors by ID using the
    ` td_related_ids_for_upload ` column.
-   Alternatively, you can specify the related-to descriptors using the
    ` td_related_triples_for_upload ` column. Provide the owner-app ID,
    indicator type, and indicator text, which will uniquely identify the
    linked-to descriptors.

#### CSV Example (written vertically for convenience):

` `

    td_description                Testing bulk upload
    td_status                     NON_MALICIOUS
    td_confidence                 100
    td_severity                   INFO
    td_share_level                AMBER
    td_indicator_type             HASH_MD5
    td_raw_indicator              e8b19da37825a3056e84c522f05eb000
    td_visibility                 HAS_WHITELIST
    td_subjective_tags            testing
    td_whitelist_apps             494491891138576:Media Hash Sharing RF Test
    td_privacy_groups             
    td_review_status              REVIEWED_MANUALLY
    td_related_ids_for_upload     2515798535123892,2376386079125415
    td_related_triples_for_upload 

    td_description                Testing bulk upload
    td_status                     NON_MALICIOUS
    td_confidence                 100
    td_severity                   INFO
    td_share_level                AMBER
    td_indicator_type             HASH_MD5
    td_raw_indicator              e8b19da37825a3056e84c522f05eb001
    td_visibility                 HAS_WHITELIST
    td_subjective_tags            pwny;testing
    td_whitelist_apps             494491891138576:Media Hash Sharing RF Test
    td_privacy_groups             
    td_review_status              REVIEWED_MANUALLY
    td_related_ids_for_upload     
    td_related_triples_for_upload 494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb000,494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb002

#### JSON Example:

` `

    [
      {
        "td_description": "Testing bulk upload/relate",
        "td_status": "NON_MALICIOUS",
        "td_confidence": 100,
        "td_severity": "INFO",
        "td_share_level": "AMBER",
        "td_indicator_type": "HASH_MD5",
        "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000",
        "td_visibility": "HAS_WHITELIST",
        "td_subjective_tags": ["testing"],
        "td_whitelist_apps": [
          {
            "id": "494491891138576",
            "name": "Media Hash Sharing RF Test"
          }
        ],
        "td_privacy_groups": [],
        "td_review_status": "REVIEWED_MANUALLY",
        "td_related_ids_for_upload": ["2515798535123892","2376386079125415"]
      },
      {
        "td_description": "Testing bulk upload/relate",
        "td_status": "NON_MALICIOUS",
        "td_confidence": 100,
        "td_severity": "INFO",
        "td_share_level": "AMBER",
        "td_indicator_type": "HASH_MD5",
        "td_raw_indicator": "e8b19da37825a3056e84c522f05eb001",
        "td_visibility": "HAS_WHITELIST",
        "td_subjective_tags": ["pwny", "testing"],
        "td_whitelist_apps": [
          {
            "id": "494491891138576",
            "name": "Media Hash Sharing RF Test"
          }
        ],
        "td_privacy_groups": [],
        "td_review_status": "REVIEWED_MANUALLY",
        "td_related_triples_for_upload": [
          {
            "owner_app_id": "494491891138576",
            "td_indicator_type": "HASH_MD5",
            "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000"
          },
          {
            "owner_app_id": "494491891138576",
            "td_indicator_type": "HASH_MD5",
            "td_raw_indicator": "e8b19da37825a3056e84c522f05eb002"
          }
        ]
      }
    ]
          
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Using the API, you can create connections via an ` HTTP POST ` request
to the ` /related ` URI for a specific object:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.8/<object_id>/related
```

In this example, create a connection between the ` facebook.com ` domain
object ( ` 788497497903212 ` ) and the 173.252.120.6 IP address object (
` 1061383593887032 ` ), which ` facebook.com ` can resolve to via DNS.

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v2.8/788497497903212/related

POST DATA:
related_id=1061383593887032
&amp;access_token=<access_token>
```

Data returned:

``` {._5s-8 .prettyprint .lang-code}
{
"success": true
}
```
:::
:::

</div>

</div>
