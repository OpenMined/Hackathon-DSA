Privacy Controls - ThreatExchange - Documentation - Meta for Developers

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
ThreatExchange Privacy Controls
===============================
All submissions to the ThreatExchange API allow for limiting the visibility of any ThreatDescriptor objects. Currently, ThreatExchange supports three levels of visibility:
* allow all members;
* allow a ThreatPrivacyGroup; and
* allow a whitelist of specific members.
The desired privacy setting on an object is specified by the values at the time of a create or edit submission to the API. Privacy settings can also be changed retroactively for data you've already submitted.
Privacy settings are propagated as follows: Threat Exchange members can see an indicator if and only if they can see at least one associated descriptor.
Privacy Fields
--------------
There are two fields that combine to define the privacy on an object within ThreatExchange: `privacy_type` and `privacy_members`.
The `privacy_type` field can have one of the following values:

 Name
  | 
 Description
  || `HAS_PRIVACY_GROUP` | The privacy group IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `HAS_WHITELIST` | The App IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `VISIBLE` | All members of ThreatExchange can see the object. *This is the default, if no value is specified.* |
The `privacy_members` field is a comma-delimited list of App IDs of ThreatExchangeMembers or ThreatPrivacyGroups that are either given or not given access to the data, based on the value in `privacy_type`.
Setting Privacy: Examples
-------------------------
The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which members of ThreatExchange are allowed to see the data.
### Controlling visibility using the UI
### Allowing all members access using the API

```
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
```
### Limiting privacy to a privacy group using the API

```
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_PRIVACY_GROUP
&amp;privacy_members=123456789
```
### Limiting privacy To select members using the API

```
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_WHITELIST
&amp;privacy_members=123456789,9012345678
```
### Limiting privacy to only your app using the API

```
POST https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat_type=MALICIOUS_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=HAS_WHITELIST
&amp;privacy_members=555
```