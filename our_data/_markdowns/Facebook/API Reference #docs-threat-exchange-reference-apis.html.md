API Reference - ThreatExchange - Documentation - Meta for Developers

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
ThreatExchange API Reference
============================

The comprehensive list of the ThreatExchange APIs and the related endpoints.

Objects
-------

 Parameter | 
 Description
  || ThreatDescriptor | Subjective context provided by a ThreatExchangeMember for a ThreatIndicator. |
| ThreatExchangeMember | Participant within ThreatExchange. |
| ThreatExchangeImpactReport | Freeform record of outcomes as a result of participating in ThreatExchange. |
| ThreatIndicator | Indicator of compromise. |
| ThreatPrivacyGroup | Label to group threat objects together. |
| ThreatTags | Label to group threat objects together. |
Types
-----

 Parameter
  | 
 Description
  || IndicatorType | Type of indicator being described by a ThreatIndicator object. |
| PrecisionType | Defines how accurately the threat intelligence detects its intended target, victim or actor. |
| PrivacyType | Defines who can access the threat intelligence. |
| ReviewStatusType | Description of how the threat intelligence was vetted. |
| SeverityType | Description of the threat dangerousness associated with a ThreatIndicator object. The order of the values below are ordered from least severe to most severe. |
| SignatureType | Type of signature format described by a ThreatIndicator object. |
| ShareLevelType (aka Traffic Light Protocol or TLP) | Designation of how any object in ThreatExchange may be re-shared both within and outside of ThreatExchange, based on the US-CERT's Traffic Light Protocol. |
| StatusType | Description of the maliciousness of any object within ThreatExchange. |
Search Endpoints
----------------

 Parameter
  | 
 Description
  || /threat\_updates | Prefered way of downloading all the data for a collaboration and staying in sync with updates. Not enabled for all privacy groups. See page for details. |
| /threat\_descriptors | Enables searching for descriptors (opinions on content or indicators). |
| /threat\_indicators | Enables searching for indicators. |
| /threat\_tags | Enables searching for threat tags. |
Miscellaneous Endpoints
-----------------------

 Parameter
  | 
 Description
  || /threat\_exchange\_members | Returns a list of current members of the ThreatExchange. |