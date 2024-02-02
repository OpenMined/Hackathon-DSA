
Re-sharing - ThreatExchange - Documentation - Meta for Developers











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
ThreatExchange re-sharing controls
==================================

All submissions to the ThreatExchange API allow for defining how the data can be re-shared by its recipients. The level of re-sharing is applied via the `share_level` attribute.

The desired re-share setting on an object can be specified at the time of a create or edit submission to the API. While re-sharing settings can be changed retroactively, those changes will not be pushed as updates to members that have already accessed the data.

Re-sharing options via `share_level`
------------------------------------

The re-sharing definitions adopted by ThreatExchange are derived from those definied in the US-CERT's Traffic Light Protocol. They have been adapted to accomodate the realities of re-sharing within large corporations with complex subsidiary relationships.

The exact definitions of the permitted values in the `share_level` attribute are defined in the ShareLevelType.

Setting re-sharing: examples
----------------------------

The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which re-sharing level is permitted.

### Specifying re-sharing using the UI

### Allowing re-sharing to anyone, including public channels, using the API


```
POST https://graph.facebook.com/v2.8/threat_indicators?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
&amp;share_level=WHITE
```
### Limiting re-sharing to established, non-public channels, using the API


```
POST https://graph.facebook.com/v2.8/threat_indicators?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
&amp;share_level=GREEN
```
### Limiting re-sharing to select members and their related entities with a need to know, using the API


```
POST https://graph.facebook.com/v2.8/threat_indicators?access_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_WHITELIST
&amp;privacy_members=555
&amp;share_level=AMBER
```


































 
