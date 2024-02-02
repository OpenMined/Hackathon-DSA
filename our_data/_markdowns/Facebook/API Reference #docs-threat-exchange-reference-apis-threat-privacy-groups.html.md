/threat\_privacy\_groups - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0/threat\_privacy\_groups
========================
This API call enables the creation of a ThreatPrivacyGroup via an HTTP POST request. Privacy groups can be used to protect uploaded data. This feature is only available in versions 2.4+ of the Graph API.
Parameters
----------
The following query parameters are available (bold parameters are required):
* **`access_token`** - The key for authenticating to the API. It is a concatenation of [your-app-id|your-app-secret]. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
* **`name`** - The name of the threat privacy group.
* **`description`** - A human readable description of the group.
* `members` - A list of ThreatExchangeMembers to be added to the group. Can be modified later.
* `members_can_see` - If true, group members can view this group, including its name, description, and list of members. Defaults to FALSE.
* `members_can_use` - If true, members are allowed to use this group to protect their own threat data. Defaults to FALSE.
### Sample Usage
To create a privacy group:

```
curl -s -X POST \
'https://graph.facebook.com/v14.0/threat_privacy_groups'\
'?access_token=REDACTED'\
'&name=Testing+curl+post'\
'&description=Testing+curl+post'\
'&members_can_see=TRUE'
```
Data returned:

```
{"id":"1200716590320515"}
```
To edit:

```
curl -s -X POST \
'https://graph.facebook.com/v14.0/1200716590320515'\
'?access_token=REDACTED'\
'&name=Testing+curl+post'\
'&description=Testing+curl+post+update'
```
Data returned:

```
{"success":true}
```