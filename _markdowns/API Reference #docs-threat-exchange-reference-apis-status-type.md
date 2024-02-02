
StatusType - ThreatExchange - Documentation - Meta for Developers











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
Graph API Versionv18.0StatusType
==========

StatusType is an important field in ThreatExchange, as it corresponds to whether the upload is referring to malicious or harmful content. This help you determine what the original uploader's intent was in uploading signals, and therefore what you should do when you find matching or corresponding data on your platform.

Values
------



 
 Name
  | 
 Cybersecurity Description
  | 
 Content Safety Description
  || `MALICIOUS` | The object is consistently malicious | Corresponds to harmful content or behavior. |
| `SUSPICIOUS` | The object can be malicious, dependent on the context in which it is found | Helps discover harmful content or requires additional investigation to discover harmful content. |
| `NON_MALICIOUS` | The object is not known to be malicious | Informational or trend information that does not lead to the discovery of harmful content. |
| `UNKNOWN` | No maliciousness information available | Do not use this StatusType for content safety. |

































 
