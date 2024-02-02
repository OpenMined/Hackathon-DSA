ReviewStatusType - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0ReviewStatusType
================
Indicates if the data was reviewed and, if via automation or a human.
Values
------

Name
 | 
Description
 || `UNKNOWN` | No review data available. |
| `UNREVIEWED` | The data has not been reviewed. |
| `PENDING` | The data is currently under review. |
| `REVIEWED_MANUALLY` | The data was reviewed manually. |
| `REVIEWED_AUTOMATICALLY` | The data was reviewed by an automated system. Note that you cannot set this value if the current value is REVIEWED\_MANUALLY. This restriction was added to prevent automated systems from clobbering the work of human reviewers. To get around this, you must first change the review status to another value, e.g. PENDING, and then change it to REVIEWED\_AUTOMATICALLY. |