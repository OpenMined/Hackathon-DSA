::: {._4-u3 ._588p}
::: _57-c
Parameter
:::
:::

Description

Type

` id `

Unique identifier of the threat descriptor. Automatically assigned at
create time, and non-editable.

` number `

` added_on `

The datetime this descriptor was first uploaded. Automatically computed;
not directly editable.

` string `

` confidence `

A rating, from 0-100, on how confident the publisher is of the threat
indicator\'s status. 0 is meant to be least confident, with 100 being
most confident.

` number `

` description `

A short summary of the indicator and threat.

` string `

` expired_on `

Datetime the indicator is no longer considered a threat, as subjectively
determined by the owner of the descriptor.

` number `

` first_active `

The datetime when this opinion first became valid, as subjectively
determined by the owner of the descriptor.

` string `

` last_active `

The datetime when this opinion stopped being valid, as subjectively
determined by the owner of the descriptor.

` string `

` indicator `

The
[ThreatIndicator](/docs/threat-exchange/reference/apis/threat-indicator)
described by the descriptor: for example, a URL or a hash string.
Non-editable after the descriptor is created.

[` ThreatIndicator `](/docs/threat-exchange/reference/apis/threat-indicator)

` last_updated `

Datetime the threat descriptor was last updated. Automatically computed;
not directly editable.

` string `

` my_reactions `

A list of reactions that you have added to this descriptor.

[` ReactionType `](/docs/threat-exchange/reference/apis/reaction-type)

` owner `

The
[ThreatExchangeMember](/docs/threat-exchange/reference/apis/threat-exchange-member)
that submitted the descriptor. Non-editable.

[` ThreatExchangeMember `](/docs/threat-exchange/reference/apis/threat-exchange-member)

` precision `

The degree of accuracy of the descriptor.

[` PrecisionType `](/docs/threat-exchange/reference/apis/precision-type)

` privacy_type `

The level of privacy applied to the descriptor. Also known as
\"visibility\".

[` PrivacyType `](/docs/threat-exchange/reference/apis/privacy-type)

` raw_indicator `

A raw, unsanitized string of the indicator being described.

` string `

` reactions `

A list of reactions to reacting application.

[` ReactionType `](/docs/threat-exchange/reference/apis/reaction-type)

` review_status `

Describes how the indicator was vetted.

[` ReviewStatusType `](/docs/threat-exchange/reference/apis/review-status-type)

` severity `

Dangerousness of threat associated with the indicator.

[` SeverityType `](/docs/threat-exchange/reference/apis/severity-type)

` share_level `

A designation of how the indicator may be shared, based on the
[US-CERT\'s Traffic Light
Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT2eCTR9dXrDWiJAPyyuVXoFcxtTBpbFmLnAJFY6k8sFkQIZWmXEfc0yo4pmPp5qfxnZGArc3FWsT3Tfihr844pcszP-SERtRYvdY7e6fwbLN67m3rIwLU79o--qOJRSAWGy1lkNm1tsjSNl)
.

[` ShareLevelType `](/docs/threat-exchange/reference/apis/share-level-type)

` source_uri `

A publicly accessible URL containing further context or details about
the descriptor.

` string `

` status `

If the indicator is known to be malicious or not.

[` StatusType `](/docs/threat-exchange/reference/apis/status-type)

` type `

The type of indicator.

[` IndicatorType `](/docs/threat-exchange/reference/apis/indicator-type)

::: _57-c
Parameter
:::

Description

Type

` tags `

The tags applied to this descriptor.

` string `

For additional documentation on ThreatTags, see [ThreatTag
Object](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/v2.8)

### Sample Usage

Example query for a specific descriptor: 777900478994849

``` {._5s-8 .prettyprint .lang-code}
https://graph.facebook.com/777900478994849?access_token=555|asdF123
```

Data returned:

``` {._5s-8 .prettyprint .lang-code}
{
  "id": "777900478994849",
  "indicator": {
    "indicator": "http://test1435342443.evilevillabs.com/test.php",
    "type": "URI",
    "id": "841478115929947"
  },
  "owner": {
    "id": "682796275165036",
    "name": "Facebook Site Integrity ThreatExchange"
  },
  "type": "URI",
  "raw_indicator": "http://test1435342443.evilevillabs.com/test.php",
  "description": "Test Description",
  "tags": {
    "data": [
      {
        "id": "908180082612873",
        "text": "evilevil"
      },
      {
        "id": "884078131700721",
        "text": "testing"
      }
    ]
  },
  "status": "UNKNOWN"
}
```
