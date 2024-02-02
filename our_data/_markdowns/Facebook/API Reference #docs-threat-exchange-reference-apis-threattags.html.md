ThreatTag Object - ThreatExchange - Documentation - Meta for Developers

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
Graph API Versionv19.0ThreatTag
=========
A label which groups Malware, ThreatDescriptor, and/or MalwareFamily objects. Once objects are tagged, you can use tags to narrow your search queries in TE.
Fields
------

Parameter
 | 
Description
 | 
Type
 || `id` | Unique identifier of the threat tag | `number` |
| `text` | The text for this tag | `string` |
### Legal Tags
The text of tags is case insensitive, restricted to letters, numbers, underscores, and colons, and must be UTF-8 friendly. So "שלום" is a valid text, but "#example-tag" is not.
### Sample Usage
Example query for a specific ThreatTag: 908180082612873
Data returned:

```
{
  "id": "908180082612873",
  "text": "evilevil"
}
```
Example of searching for a tag by text 'evilevil'. Note that partial tag search is supported.

```
https://graph.facebook.com/v2.7/threat_tags/?access_token=555|aSdF123GhK&amp;text=evilevil
```
Data returned:

```
{
  "data": [
    {
      "id": "908180082612873",
      "text": "evilevil"
    }
    ...
  ]
}
```
Connections
-----------

Name
 | 
Description
 | 
Type
 || `tagged_objects` | The objects tagged with this text. | `Malware`, `ThreatDescriptor`, `MalwareFamily` |
#### Parameters
The following query parameters are available:
* `tagged_since` - Fetches all objects that have been tagged since this time (inclusive).
* `tagged_until` - Fetches all objects that have been tagged until this time (inclusive).
Tagged objects are returned in the order based on when the tag was applied, ascending. This timestamp is currently not exposed by the API, but is the same one used by `tagged_since` and `tagged_until`. While this API can be used to create a copy of data in ThreatExchange, the threat\_updates API may be better suited for your usecase.
### Sample Usage
Example of tagged objects for a specific ThreatTag: 908180082612873

```
https://graph.facebook.com/v2.7/908180082612873/tagged_objects/?access_token=555|aSdF123GhK
```
Data returned:

```
{
  "data": [
    {
      "id": "1039423046092869",
      "type": "THREAT_DESCRIPTOR",
      "name": "test1464195852.evilevillabs.com"
    },
    ...
  ]
}
```
Example of tagged objects for a ThreatTag with the text 'ducks'

```
https://graph.facebook.com/v2.7/threat_tags/?access_token=555|aSdF123GhK&amp;text=ducks&amp;fields=id,text,tagged_objects
```
Data returned:

```
{
  "data": [
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged_objects": {
        "data": [
          {
            "id": "1162586023812794",
            "type": "THREAT_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        ]
      },
    }
  ]
}
```
Creating a New Tag
------------------
You can create a ThreatTag on-the-fly while creating a ThreatDescriptor. If the ThreatTag does not exist, a new one will be created and applied to the new ThreatDescriptor.

```
https://graph.facebook.com/v2.7/threat_descriptors?access_token=555|aSdF123GhK
POST DATA:
  tags=cows,bar
  &amp;type=DOMAIN
  &amp;indicator=test1466722733.evilevillabs.com
  &amp;description=this is an example with tags
  &amp;privacy_type=VISIBLE
  &amp;share_level=GREEN
  &amp;status=UKNOWN
```
Data returned:

```
{
  "success": true,
  "id": "1162586023812794"
}
```
To create a ThreatTag without labeling any objects, you can post to the /threat\_tags endpoint explicitly:

```
https://graph.facebook.com/v2.7/threat_tags?access_token=555|aSdF123GhK
POST DATA:
  text=superlongtagfortestingcreation
  &amp;objects=973966502652751,898684593584287
```
Data returned:

```
{
  "success": true,
  "id": "1373232162693002"
}
```
Example of updating a ThreatDescriptor with more tags. If the tag does not exist, a new one will be created and applied to this ThreatDescriptor.

```
https://graph.facebook.com/v2.7/1162586023812794?access_token=555|aSdF123GhK
POST DATA:
  tags=ducks,chicken
```
Data returned:

```
{
  "success": true
}
```
Popular Tags
------------
Here is a list of the most popular tags categorizing data related to attacks:

Name
 | 
Description
 || `access_token_theft` | Theft of an OAuth style or similar access token |
| `bogon` | A bogus IP address |
| `bot` | A bot |
| `brute_force` | Repeated attempts to access an authenticated resource |
| `clickjacking` | Any UI redressing or similar type of attack redirecting a person's clicks |
| `compromised` | The associated party has been compromised |
| `creeper` | A party which stalks another online |
| `drugs` | Associated with drugs |
| `email_spam` | Sending of unsolicited email |
| `explicit_content` | Pornographic or otherwise explicit content |
| `exploit_kit` | A set of tools used to take advantage of vulnerabilities |
| `fake_account` | An account associated with no real entity, often used for abuse |
| `financial` | Associated with financials, perhaps fraud |
| `ip_infringement` | Infringement on the rights of an intellectual property holder |
| `malicious_app` | A malicious web app |
| `malicious_nameserver` | A malicious name server |
| `malicious_webserver` | A malicious web server |
| `malvertising` | The use of online advertising to spread malware |
| `malware` | A malware-based attack |
| `passive_dns` | Interserver DNS messages are being captured, recorded, and potentially exfiltrated |
| `phishing` | An attempt to obtain credentials via a deceptive lure |
| `piracy` | Illegal replication of protected property |
| `prox` | A proxy host |
| `scam` | A generic type of scam |
| `scanning` | Port scanning to map a network |
| `scraping` | Systematic traversal of a network and recording of data |
| `self_xss` | Attack where a person is social engineered into pasting malicious code into their brower's address bar or developer console |
| `share_baiting` | A person is convinced to share spammy content in exchange for a fictitious product or content |
| `targeted` | An attack conducted by a sophisticated actor and directed at a specific target |
| `terrorism` | Associated with terrorist attacks or groups |
| `weapons` | Related to the illegal trade of arms |
| `web_app` | A malicious web app |
Here is a list of the most popular tags categorizing data by type:

Name
 | 
Description
 || `bad_actor` | Details on a presumed bad actor (e.g. botherder, spammer) |
| `compromised_credential` | The credential compromised by an attack (must be already publicly accessible) |
| `ht_victim` | For high-value victim targeting |
| `malicious_ad` | A malicious advertisement |
| `malicious_api_key` | An API key which is being abused |
| `malicious_content` | A malicious post, image, or document |
| `malicious_domain` | A malicious Internet domain |
| `malicious_inject` | A malicious piece of code that injected into a another file, process, or DOM |
| `malicious_ip` | A malicious IP address |
| `malicious_subnet` | A malicious IP address range |
| `malicious_ssl_cert` | A malicious SSL certificate |
| `malware_sample` | A specific piece of Malware |
| `malware_victim` | A victim of Malware |
| `proxy_ip` | An IP address known to be a proxy or VPN |
| `signature` | Represents some means or pattern for detecting a threat |
| `web_request` | A full web request, optionally with GET query parameters |
| `whitelist_domain` | An Internet domain that should be treated as non-malicious |
| `whitelist_ip` | An IP address that should be treated as non-malicious |
| `whitelist_url` | An URI that should be treated as non-malicious |