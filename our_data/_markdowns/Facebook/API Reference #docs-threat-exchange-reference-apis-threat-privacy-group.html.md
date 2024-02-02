ThreatPrivacyGroup Object - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0ThreatPrivacyGroup
==================
A list of ThreatExchangeMembers to which data can be shared. Only available in versions 2.4+ of the Graph API.
Fields
------

Parameter
 | 
Description
 | 
Type
 || `id` | Unique identifier of the threat privacy group | `number` |
| `name` | The name of the threat privacy group | `string` |
| `description` | A human readable description of the group | `string` |
| `members_can_see` | If true, group members can view this group, including its name, description, and list of members | `boolean` |
| `members_can_use` | If true, members are allowed to use this group to protect their own threat data | `boolean` |
### Sample Usage
To create a privacy group, one could POST to:

```
https://graph.facebook.com/v2.4/threat_privacy_groups?name=GROUP1&amp;description=MYFIRSTGROUP&amp;access_token=555|asdF123
```
Data returned:

```
{
  "id": "123456789101112"
}
```
Connections
-----------

Name
 | 
Description
 | 
Type
 || `members` | Members of the privacy group | `ThreatExchangeMember` |
### Sample Usage
Example query for a specific privacy group: 123456789101112

```
https://graph.facebook.com/v2.4/123456789101112/members/?access_token=555|aSdF123GhK
```
Data returned:

```
{
  "data": [
    {
      "id": "999999999999",
      "email": "threatexchange@domain.com",
      "name": "Facebook Administrator"
    }
    ...
  ]
}
```