
ThreatDescriptor Object - ThreatExchange - Documentation - Meta for Developers











ThreatExchange* Get Started
* Get Access
* Best Practices
* UI Overview
* UI Reference
* API Overview
* API Examples
* API Structure
* API Reference
* Privacy Controls
* Submitting Data
* Editing Existing Data
* Delete Data
* Re-sharing
* React to Data
* Submit Connections
* Integrations
* Webhooks
* FAQ
* Webinar
* Changelog
Graph API Versionv18.0ThreatDescriptor
================

A subjective opinion about a ThreatIndicator that was submitted by a ThreatExchangeMember.

Fields
------



 
Parameter
 | 
Description
 | 
Type
 || `id` | Unique identifier of the threat descriptor. Automatically assigned at create time, and non-editable. | `number` |
| `added_on` | The datetime this descriptor was first uploaded. Automatically computed; not directly editable. | `string` |
| `confidence` | A rating, from 0-100, on how confident the publisher is of the threat indicator's status. 0 is meant to be least confident, with 100 being most confident. | `number` |
| `description` | A short summary of the indicator and threat. | `string` |
| `expired_on` | Datetime the indicator is no longer considered a threat, as subjectively determined by the owner of the descriptor. | `number` |
| `first_active` | The datetime when this opinion first became valid, as subjectively determined by the owner of the descriptor. | `string` |
| `last_active` | The datetime when this opinion stopped being valid, as subjectively determined by the owner of the descriptor. | `string` |
| `indicator` | The ThreatIndicator described by the descriptor: for example, a URL or a hash string. Non-editable after the descriptor is created. | `ThreatIndicator` |
| `last_updated` | Datetime the threat descriptor was last updated. Automatically computed; not directly editable. | `string` |
| `my_reactions` | A list of reactions that you have added to this descriptor. | `ReactionType` |
| `owner` | The ThreatExchangeMember that submitted the descriptor. Non-editable. | `ThreatExchangeMember` |
| `precision` | The degree of accuracy of the descriptor. | `PrecisionType` |
| `privacy_type` | The level of privacy applied to the descriptor. Also known as "visibility". | `PrivacyType` |
| `raw_indicator` | A raw, unsanitized string of the indicator being described. | `string` |
| `reactions` | A list of reactions to reacting application. | `ReactionType` |
| `review_status` | Describes how the indicator was vetted. | `ReviewStatusType` |
| `severity` | Dangerousness of threat associated with the indicator. | `SeverityType` |
| `share_level` | A designation of how the indicator may be shared, based on the US-CERT's Traffic Light Protocol. | `ShareLevelType` |
| `source_uri` | A publicly accessible URL containing further context or details about the descriptor. | `string` |
| `status` | If the indicator is known to be malicious or not. | `StatusType` |
| `type` | The type of indicator. | `IndicatorType` |

### Connections



 
Parameter
 | 
Description
 | 
Type
 || `tags` | The tags applied to this descriptor. | `string` |

For additional documentation on ThreatTags, see ThreatTag Object

### Sample Usage

Example query for a specific descriptor: 777900478994849


```
https://graph.facebook.com/777900478994849?access_token=555|asdF123
```
Data returned:


```
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
































 
