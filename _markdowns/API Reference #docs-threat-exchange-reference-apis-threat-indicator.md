
ThreatIndicator Object - ThreatExchange - Documentation - Meta for Developers











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
Graph API Versionv18.0ThreatIndicator
===============

An indicator of compromise.

Fields
------



 
Parameter
 | 
Description
 | 
Type
 || `id` | Unique identifier of the threat indicator. Automatically assigned at create time, and non-editable. | `number` |
| `indicator` | The value of the indicator. Non-editable after initial creation of the indicator. | `string` |
| `type` | The type of indicator. Non-editable after initial creation of the indicator. | List of `IndicatorType` |

### Sample Usage

Example query for a specific indicator: 788497497903212:


```

https://graph.facebook.com/v18.0/788497497903212/?access_token=555|aSdF123GhK

```
Data returned:


```
{
   "indicator": "facebook.com",
   "type": "DOMAIN",
   "id": "788497497903212"
}
```
Connections
-----------



 
Name
 | 
Description
 | 
Type
 || `descriptors` | Subjective opinions about the indicator | `ThreatDescriptor` |
| `related` | Other threat indicators that have been associated | `ThreatIndicator` |

### Sample Usage

Example query for descriptors related to a specific indicator: 852121234856016


```

https://graph.facebook.com/v18.0/852121234856016/descriptors/?access_token=555|aSdF123GhK

```
Data returned:


```
 {
   "data": [
  {
    "id": "811927545529339",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "588498724619612",
      "name": "Facebook CERT ThreatExchange"
    },
    "type": "DOMAIN",
    "raw_indicator": "test1434227164.evilevillabs.com",
    "description": "This is our test domain. It's harmless",
    "status": "NON_MALICIOUS"
  },
  {
    "id": "799906626794304",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "682796275165036",
      "name": "Facebook Site Integrity ThreatExchange"
    },
    "type": "DOMAIN",
    "raw_indicator": "test1434227164.evilevillabs.com",
    "description": "Malware command and control",
    "status": "MALICIOUS"
  }
],
"paging": {
  "cursors": {
    "before": "ODExOTI3NTQ1NTI5MzM5",
    "after": "Nzk5OTA2NjI2Nzk0MzA0"
  }
}
```
































 
