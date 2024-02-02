
/<app-id>/threat\_privacy\_groups\_member - ThreatExchange - Documentation - Meta for Developers












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
Graph API Versionv18.0/<app-id>/threat\_privacy\_groups\_member
=========================================

Returns a list of the ThreatPrivacyGroups of which your app is a member.

Parameters
----------

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".

The following query parameters are optional:

* `name` - Allows filtering by privacy group name
* `description` - Allows filtering by privacy group description

Example query:


```
https://graph.facebook.com/v2.4/<your-app-id>/threat_privacy_groups_member?access_token=555|aSdF123GhK
```
Data returned:


```
{
  "data": [
    {
      "name": "MYNAMEISBOB",
      "description": "MALWARESIGNATURES",
      "group_id": "7777777777"
    },
    ...
  ]
}
```

































 
