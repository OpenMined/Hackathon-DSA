
Delete Data - ThreatExchange - Documentation - Meta for Developers









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
Delete Data
===========


ThreatExchange currently supports deletion for ThreatDescriptor objects and relationships between ThreatIndicator objects. Some objects may also be given an expiration time, which will cause data to be deleted automatically within 90 days of the expiration.
 

You can delete a ThreatDescriptor using the API with a `DELETE HTTP` request:



```
DELETE https://graph.facebook.com/v2.11/<object_id>
```
After a subjective ThreatDescriptor is deleted, the objective ThreatIndicator may still exist.


To delete a relationship between ThreatIndicators using the API:



```
DELETE https://graph.facebook.com/v2.11/<object_id>/related?related_id=<object_id_2>
```
We do not support deletes for Tags.


































 
