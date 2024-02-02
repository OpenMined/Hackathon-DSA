<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Visit the [**descriptors-tab
page**](/docs/threat-exchange/reference/ui/descriptors) to see more
things you can do with threat descriptors within the ThreatExchange UI
including searching, bulk download, and more.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Using the Create button you can upload a new descriptor, with tooltips
to provide context. Here\'s an example of submitting a malicious domain
using the UI:

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/73006337_1206961936162108_561223273489104896_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=nVzV9GDyZbgAX-RTaWH&_nc_ht=scontent-cdg4-2.xx&oh=00_AfAtfTwqVzhbwFnxXhYMR6WkJRQofpMUR3yFuAxDAPN8YQ&oe=65A8F4F7){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/73006337_1206961936162108_561223273489104896_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=nVzV9GDyZbgAX-RTaWH&_nc_ht=scontent-cdg4-2.xx&oh=00_AfAtfTwqVzhbwFnxXhYMR6WkJRQofpMUR3yFuAxDAPN8YQ&oe=65A8F4F7"}
:::

Note : If you set a descriptor\'s privacy to has-whitelist and include
no whitelist apps, the owner\'s app is automatically included. This is a
\"visible to self\" or \"storage mode\" option.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/80034984_2401774043262367_1180505347949854720_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=B7gTkYoJzc4AX9bio_5&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCQrzujN7RFIZIEHRFsjonaMnvgDP25snneI4ndtvaRnA&oe=65A9E4AF){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/80034984_2401774043262367_1180505347949854720_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=B7gTkYoJzc4AX9bio_5&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCQrzujN7RFIZIEHRFsjonaMnvgDP25snneI4ndtvaRnA&oe=65A9E4AF"}
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Using the Create button is fine for sharing a single threat descriptor
\-- but what if you have a hundred or a thousand? As we\'ll see
immediately below, bulk-upload from CSV or JSON files solves this
problem in a very general way.

But there\'s a common case that\'s simpler \-- when you don\'t really
need a CSV file. ThreatExchange users often find they\'re submitting a
number of threat descriptors which have all the same metadata except for
the indicator value. The **create-with-templates** feature fits the
bill.

To use templates, simply proceed as above by selecting the Create button
\-- then select the .

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/101225047_2667055900207086_6753427763304071168_n.png?_nc_cat=106&ccb=1-7&_nc_sid=f537c7&_nc_ohc=C8gB5UAcB_4AX_Krx7_&_nc_ht=scontent-cdg4-3.xx&oh=00_AfB8f4CIocSef1cWCCQyP02clKkNAJXGoAAmWw3Tymv_kg&oe=65A9F89E){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/101225047_2667055900207086_6753427763304071168_n.png?_nc_cat=106&ccb=1-7&_nc_sid=f537c7&_nc_ohc=C8gB5UAcB_4AX_Krx7_&_nc_ht=scontent-cdg4-3.xx&oh=00_AfB8f4CIocSef1cWCCQyP02clKkNAJXGoAAmWw3Tymv_kg&oe=65A9F89E"}
:::

Since template mode is selected, once you hit OK you\'ll be taken to a
commit screen (the same as for upload from file) where you can make any
revisions, if any, then commit.

The same works for the Copy button as for the Create button \-- this way
you can easily make \"more of the same\" as your organization has more
data to share on a given topic.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Both CSV and JSON formats are supported.

Start by selecting the Bulk Upload button:

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/77990078_2481255295487862_2619752805849628672_n.png?_nc_cat=108&ccb=1-7&_nc_sid=f537c7&_nc_ohc=1fLfy5wdLVEAX98Orjs&_nc_ht=scontent-cdg4-1.xx&oh=00_AfB2k9G7m6qvzr5cHakC7qOWeHSzB_da2q3u-Y8yIsPveQ&oe=65AA70B0){.img
srcset="https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/77990078_2481255295487862_2619752805849628672_n.png?_nc_cat=108&ccb=1-7&_nc_sid=f537c7&_nc_ohc=1fLfy5wdLVEAX98Orjs&_nc_ht=scontent-cdg4-1.xx&oh=00_AfB2k9G7m6qvzr5cHakC7qOWeHSzB_da2q3u-Y8yIsPveQ&oe=65AA70B0"}
:::

Select your file:

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78303202_766146167142680_4726873051281489920_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=XRb3MpvAR60AX8LnEJB&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDnpGP3VPQOHbTM3oZ1BtsxXGa_3Z07mlXIb3uk_m3-VQ&oe=65AA1632){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78303202_766146167142680_4726873051281489920_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=XRb3MpvAR60AX8LnEJB&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDnpGP3VPQOHbTM3oZ1BtsxXGa_3Z07mlXIb3uk_m3-VQ&oe=65AA1632"}
:::

If you wish to revise your data before committing you can do so:

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/78480767_451147705531527_8385306995510476800_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=aC4-2mjnCisAX_zgB6t&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBAn8dEVcMEWLqAtEmW9ZExN6GUDWzWdQrUxkBsYyXRxA&oe=65A9E1D4){.img
srcset="https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/78480767_451147705531527_8385306995510476800_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=aC4-2mjnCisAX_zgB6t&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBAn8dEVcMEWLqAtEmW9ZExN6GUDWzWdQrUxkBsYyXRxA&oe=65A9E1D4"}
:::

If there are errors detected before committing you\'ll be notified, and
you can revise them. (Note that not all possible errors are surfaced
here.)

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78056540_469384567026002_5213986844466741248_n.png?_nc_cat=100&ccb=1-7&_nc_sid=f537c7&_nc_ohc=fZZdosBfxlIAX_ODnUy&_nc_ht=scontent-cdg4-2.xx&oh=00_AfC-wupwExm_LGN-Bo1jWuE3iKy1KqknddqfjHF-CKlHrA&oe=65A9BF46){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78056540_469384567026002_5213986844466741248_n.png?_nc_cat=100&ccb=1-7&_nc_sid=f537c7&_nc_ohc=fZZdosBfxlIAX_ODnUy&_nc_ht=scontent-cdg4-2.xx&oh=00_AfC-wupwExm_LGN-Bo1jWuE3iKy1KqknddqfjHF-CKlHrA&oe=65A9BF46"}
:::

Within the revision dialog you can fix the errors and hit OK to
continue:

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/77994167_547816799330232_5192561550434500608_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=KGwpepwM6UsAX9R-CBI&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDks8zyPqEJy0zBT1VmhD7MDhuMPRRzzosGqxmD1ZR-Qg&oe=65AAA7EA){.img
srcset="https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/77994167_547816799330232_5192561550434500608_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=KGwpepwM6UsAX9R-CBI&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDks8zyPqEJy0zBT1VmhD7MDhuMPRRzzosGqxmD1ZR-Qg&oe=65AAA7EA"}
:::

Once you hit the Confirm Upload button, your new descriptors are saved
and their IDs are entered into the search bar. At that point, you can
further revise them if you like.

::: {.pam .uiBoxGray}
![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78202259_2530979643657489_6334042808353030144_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=GjmCtioTlA8AX8pjr31&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDnyUIvdaeaDNc6IeJ7-CRAImx5Ug8FUaWmRuxarXEwuA&oe=65A8D839){.img
srcset="https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/78202259_2530979643657489_6334042808353030144_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=GjmCtioTlA8AX8pjr31&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDnyUIvdaeaDNc6IeJ7-CRAImx5Ug8FUaWmRuxarXEwuA&oe=65A8D839"}
:::

The following screen recording shows the revise-before-upload feature in
more detail:

::: {.pam .uiBoxGray}
::: {#u_0_3_3R ._1c_u}
::: {#u_0_4_cl ._53j5}
::: {#u_0_7_PF ._m54 ._1jto ._3htz}
![](https://static.xx.fbcdn.net/rsrc.php/v3/y4/r/-PAXP-deijE.gif){#u_0_8_G8
._1445 ._2sy9 .img}
:::

::: {._4ctp ._1jto ._3htz}
::: _4ctq
Something Went Wrong

We\'re having trouble playing this video.
:::
:::
:::
:::
:::
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
You may submit data using the ThreatExchange API via an HTTP POST to the
following URL:

-   https://graph.facebook.com/v4.0/threat_descriptors

NOTE: The call to /threat_indicators is deprecated as of v2.4 of the
ThreatExchange API. If you attempt to access this endpoint in v2.4+, it
will create a threat descriptor and the associated threat indicator
behind the scenes.

Example submission of a malicious domain using the API:

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

POST DATA:
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;tags=testingtags
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
```

Data returned:

``` {._5s-8 .prettyprint .lang-code}
{
"id": "853037291373757",
"success": true
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
Bold parameters are required.

::: _57-c
API Name and Example
:::
:::
:::

</div>

</div>

UI CSV Name and Example

Description

**` access_token `**\
` 555|aSdF123GhK `

*Not used for the UI*

The key for authenticating to the API, in the format

` your-app-id|your-app-secret `

Please visit the

[Access Token Tool](https://developers.facebook.com/tools/accesstoken)

to find values for your app(s).

**` description `**\
` This%20domain%20was%20hosting%20malware `

**` td_description `**\
` This domain was hosting malware `

A short summary of the indicator and threat.

**` indicator `**\
` evil-domain.biz `

**` td_raw_indicator `**\
` evil-domain.biz `

The indicator data being submitted.

**` type `**\
` URI `

**` td_indicator_type `**\
` URI `

The kind of indicator being described. See

[IndicatorType](/docs/threat-exchange/reference/apis/indicator-type)

for the list of allowed values.

**` privacy_type `**\
` HAS_PRIVACY_GROUP `

**` td_visibility `**\
` HAS_PRIVACY_GROUP `

The kind of privacy for the indicator. See

[PrivacyType](/docs/threat-exchange/reference/apis/privacy-type)

for the list of allowed values.

` privacy_members `\
` 1064060413755420,494491891138576 `

` td_whitelist_apps `\
` 1064060413755420,494491891138576 `

` td_privacy_groups `

\
` 438835087026293,468692780520730 `

Or, for compatibility, you can use a column name of

` td_privacy_members `

for upload if you like. If visibility is HAS_WHITELIST, we will proceed
as if your td_privacy_members column were named td_whitelist_apps; if
visibility is HAS_PRIVACY_GROUP, we will proceed as if your
td_privacy_members column were named td_privacy_groups.

See [CSV examples](#csv_examples) and [JSON examples
below.](#json_examples)

A list of

[ThreatExchangeMembers](/docs/threat-exchange/reference/apis/threat-exchange-member)

allowed to see the indicator, and only applies when

` privacy_type `

is set to

` HAS_WHITELIST `

or

` HAS_PRIVACY_GROUP `

. Delimiters are comma for the API and semicolon for the UI.

**` share_level `**\
` AMBER `

**` td_share_level `**\
` AMBER `

A designation of how the indicator may be shared based on the

[US-CERT\'s Traffic Light
Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT0-Twuvtto2WjqCfjHt-WNS6E2ck_niJsoaGF5dEJ_x-ejReS131L45xCx5kchrZB_UhU-IgHLief1N-4EYM5fK-JxCU7f-8PNCywXOEP1Soi3oCj_9ilIkRZmN_l22D1RAAl99jM_bn6Hm)

. See

[ShareLevelType](/docs/threat-exchange/reference/apis/share-level-type)

for the list of allowed values. Note: GREEN/WHITE requires VISIBLE, and
AMBER/RED requires HAS_WHITELIST or HAS_PRIVACY_GROUP.

**` status `**\
` MALICIOUS `

**` td_status `**\
` MALICIOUS `

Indicates if the indicator is labeled as malicious. See

[StatusType](/docs/threat-exchange/reference/apis/status-type)

for the list of allowed values.

` tags `\
` testing,pwny `

` td_subjective_tags `\
` testing;pwny `

API: a comma-separated list of tags you want to publish. UI: a
semicolon-separated list of tags you want to publish. This will replace
any existing tags.\
Tags are not strictly required but do note that they are essential for
your collaborators to discover data you contribute.

` add_tags `\
` pwny,testing `

*Not used for the UI*

To add tags to an object without overwriting existing tags.

` remove_tags `\
` pwny,testing `

*Not used for the UI*

Remove tags associated with an object.

` confidence `\
` 100 `

` td_confidence `\
` 100 `

A score for how likely the indicator\'s

` status `

is accurate, ranging from 0 to 100.

` expired_on `

` td_expire_time `\
` 2019-11-07T22:25:00-05:00 `

Time the indicator is no longer considered a threat, in ISO 8601 date
format.

` first_active `

` td_first_active `\
` 2019-11-07T22:25:00-05:00 `

Time when the opinion first became valid.

` last_active `

` td_last_active `\
` 2019-11-07T22:25:00-05:00 `

Time when the opinion stopped being valid.

` review_status `\
` PENDING `

` td_review_status `\
` PENDING `

Describes how the indicator was vetted. See

[ReviewStatusType](/docs/threat-exchange/reference/apis/review-status-type)

for the list of allowed values.

` severity `\
` SEVERE `

` td_severity `\
` SEVERE `

A rating of how severe the indicator is when found in an incident. See

[SeverityType](/docs/threat-exchange/reference/apis/severity-type)

for the list of allowed values.

N/A

` td_related_ids_for_upload `

For submitting relations in bulk. Please see the

[Submitting Connections
page](/docs/threat-exchange/reference/submitting-connections)

for more information.

N/A

` td_related_triples_for_upload `

For submitting relations in bulk. Please see the

[Submitting Connections
page](/docs/threat-exchange/reference/submitting-connections)

for more information.

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
When you download as CSV, we put whitelist apps and privacy groups in
the format ` id1:name1;id2:name2 ` . Tags are always text-only,
delimited by semicolons:

` `

    id                 2494923897281868
    td_description     This is an example descriptor
    td_status          UNKNOWN
    td_confidence      0
    td_severity        SEVERE
    td_share_level     AMBER
    td_indicator_type  URI
    td_raw_indicator   https://evilevillabs.com/evil.php
    td_visibility      HAS_WHITELIST
    td_creation_time   2019-11-07T22:25:00-05:00
    td_update_time     2019-11-07T22:25:01-05:00
    td_expire_time
    td_owner_id        494491891138576
    td_owner_name      Media Hash Sharing RF Test
    td_subjective_tags testing;pwny
    td_whitelist_apps  1064060413755420:Media Hash Sharing Test;494491891138576:Media Hash Sharing RF Test
            

When upload from CSV, you may specify whitelist apps and privacy groups
in the format ` id1;id2 ` if you prefer:

` `

    td_description     This is an example descriptor
    td_status          UNKNOWN
    td_confidence      0
    td_severity        SEVERE
    td_share_level     AMBER
    td_indicator_type  URI
    td_raw_indicator   https://evilevillabs.com/evil.php
    td_visibility      HAS_WHITELIST
    td_creation_time   2019-11-07T22:25:00-05:00
    td_update_time     2019-11-07T22:25:01-05:00
    td_expire_time
    td_owner_id        494491891138576
    td_owner_name      Media Hash Sharing RF Test
    td_subjective_tags testing;pwny
    td_whitelist_apps  1064060413755420;494491891138576
            
:::
:::
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8}
::: {._4-u3 ._588p}
When you download as JSON, we put whitelist app, privacy groups, and
tags in nested ID/name pairs:

` `

    {
      "id": "2699570156799349",
      "td_description": "Testing bulk upload",
      "td_status": "NON_MALICIOUS",
      "td_confidence": 100,
      "td_severity": "UNKNOWN",
      "td_share_level": "AMBER",
      "td_creation_time": 1575824153,
      "td_update_time": 1575824154,
      "td_expire_time": 0,
      "td_indicator_type": "HASH_MD5",
      "td_raw_indicator": "e8b19da37825a3056e84c522f05ed0c0",
      "td_owner": {
        "id": "1064060413755420",
        "name": "Media Hash Sharing Test"
      },
      "td_subjective_tags": [
        {
          "id": "2055943881194599",
          "td_name": "pwny"
        },
        {
          "id": "1977957082312815",
          "td_name": "testing"
        }
      ],
      "td_visibility": "HAS_WHITELIST",
      "td_whitelist_apps": [
        {
          "id": "1064060413755420",
          "name": "Media Hash Sharing Test"
        },
        {
          "id": "494491891138576",
          "name": "Media Hash Sharing RF Test"
        }
      ],
      "td_privacy_groups": []
    }
            

When you upload from JSON, if you prefer, you can write whitelist apps
and privacy groups as simply arrays of IDs, and tags as arrays of text:

` `

    {
      "td_description": "This is an example descriptor",
      "td_status": "UNKNOWN",
      "td_confidence": 0,
      "td_severity": "SEVERE",
      "td_share_level": "AMBER",
      "td_creation_time": 1573183500,
      "td_update_time": 1573183501,
      "td_expire_time": 0,
      "td_indicator_type": "URI",
      "td_raw_indicator": "https://evilevillabs.com/evil.php",
      "td_subjective_tags": ["testing", "pwny"],
      "td_visibility": "HAS_WHITELIST",
      "td_whitelist_apps": ["1064060413755420", "494491891138576"]
    }
            

See also the [Submitting Connections
page](/docs/threat-exchange/reference/submitting-connections) for how to
do related descriptors at bulk-upload.
:::
:::
:::
:::
