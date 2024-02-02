ThreatExchange API Reference
============================

The comprehensive list of the ThreatExchange APIs and the related endpoints.

Objects
-------

| Parameter | Description |
| --- | --- |
| [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) | Subjective context provided by a [ThreatExchangeMember](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) for a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator). |
| [ThreatExchangeMember](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) | Participant within ThreatExchange. |
| [ThreatExchangeImpactReport](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-impact-report) | Freeform record of outcomes as a result of participating in ThreatExchange. |
| [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) | Indicator of compromise. |
| [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group) | Label to group threat objects together. |
| [ThreatTags](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags) | Label to group threat objects together. |

Types
-----

| Parameter | Description |
| --- | --- |
| [IndicatorType](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) | Type of indicator being described by a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. |
| [PrecisionType](https://developers.facebook.com/docs/threat-exchange/reference/apis/precision-type) | Defines how accurately the threat intelligence detects its intended target, victim or actor. |
| [PrivacyType](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type) | Defines who can access the threat intelligence. |
| [ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) | Description of how the threat intelligence was vetted. |
| [SeverityType](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type) | Description of the threat dangerousness associated with a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. The order of the values below are ordered from least severe to most severe. |
| [SignatureType](https://developers.facebook.com/docs/threat-exchange/reference/apis/signature-type) | Type of signature format described by a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. |
| [ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type) (aka Traffic Light Protocol or TLP) | Designation of how any object in ThreatExchange may be re-shared both within and outside of ThreatExchange, based on the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT2dGOJSPCwEcnKNDv7zuu-oTz5LqwobLUrMrhjtk7rjpGKAbfOccY1Umpgz-2dJRAAVy4Izqp5M2XSisQgd7kmfxu2oDh_mTmZigiXCdXNCoNGVobLrJOwGOvM_DkwFGbRARqkiRESKIk7v). |
| [StatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) | Description of the maliciousness of any object within ThreatExchange. |

Search Endpoints
----------------

| Parameter | Description |
| --- | --- |
| [/threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates/v9.0) | Prefered way of downloading all the data for a collaboration and staying in sync with updates. Not enabled for all privacy groups. See page for details. |
| [/threat\_descriptors](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors) | Enables searching for descriptors (opinions on content or indicators). |
| [/threat\_indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators) | Enables searching for indicators. |
| [/threat\_tags](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-tags) | Enables searching for threat tags. |

Miscellaneous Endpoints
-----------------------

| Parameter | Description |
| --- | --- |
| [/threat\_exchange\_members](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-members) | Returns a list of current members of the ThreatExchange. |

Threat Exchange Member
======================

Reading
-------

You can't perform this operation on this endpoint.

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

ThreatDescriptor
================

A subjective opinion about a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/) that was submitted by a [ThreatExchangeMember](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member).

Fields
------

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat descriptor. Automatically assigned at create time, and non-editable. | `number` |
| `added_on` | The datetime this descriptor was first uploaded. Automatically computed; not directly editable. | `string` |
| `confidence` | A rating, from 0-100, on how confident the publisher is of the threat indicator's status. 0 is meant to be least confident, with 100 being most confident. | `number` |
| `description` | A short summary of the indicator and threat. | `string` |
| `expired_on` | Datetime the indicator is no longer considered a threat, as subjectively determined by the owner of the descriptor. | `number` |
| `first_active` | The datetime when this opinion first became valid, as subjectively determined by the owner of the descriptor. | `string` |
| `last_active` | The datetime when this opinion stopped being valid, as subjectively determined by the owner of the descriptor. | `string` |
| `indicator` | The [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) described by the descriptor: for example, a URL or a hash string. Non-editable after the descriptor is created. | [`ThreatIndicator`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) |
| `last_updated` | Datetime the threat descriptor was last updated. Automatically computed; not directly editable. | `string` |
| `my_reactions` | A list of reactions that you have added to this descriptor. | [`ReactionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) |
| `owner` | The [ThreatExchangeMember](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) that submitted the descriptor. Non-editable. | [`ThreatExchangeMember`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) |
| `precision` | The degree of accuracy of the descriptor. | [`PrecisionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/precision-type) |
| `privacy_type` | The level of privacy applied to the descriptor. Also known as "visibility". | [`PrivacyType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type) |
| `raw_indicator` | A raw, unsanitized string of the indicator being described. | `string` |
| `reactions` | A list of reactions to reacting application. | [`ReactionType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) |
| `review_status` | Describes how the indicator was vetted. | [`ReviewStatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) |
| `severity` | Dangerousness of threat associated with the indicator. | [`SeverityType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type) |
| `share_level` | A designation of how the indicator may be shared, based on the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT2eCTR9dXrDWiJAPyyuVXoFcxtTBpbFmLnAJFY6k8sFkQIZWmXEfc0yo4pmPp5qfxnZGArc3FWsT3Tfihr844pcszP-SERtRYvdY7e6fwbLN67m3rIwLU79o--qOJRSAWGy1lkNm1tsjSNl). | [`ShareLevelType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type) |
| `source_uri` | A publicly accessible URL containing further context or details about the descriptor. | `string` |
| `status` | If the indicator is known to be malicious or not. | [`StatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) |
| `type` | The type of indicator. | [`IndicatorType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) |

### Connections

| Parameter | Description | Type |
| --- | --- | --- |
| `tags` | The tags applied to this descriptor. | `string` |

For additional documentation on ThreatTags, see [ThreatTag Object](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/v2.8)

### Sample Usage

Example query for a specific descriptor: 777900478994849

https://graph.facebook.com/777900478994849?access\_token=555|asdF123

Data returned:

{
  "id": "777900478994849",
  "indicator": {
    "indicator": "http://test1435342443.evilevillabs.com/test.php",
    "type": "URI",
    "id": "841478115929947"
  },
  "owner": {
    "id": "682796275165036",
    "name": "Facebook Site Integrity ThreatExchange"
  },
  "type": "URI",
  "raw\_indicator": "http://test1435342443.evilevillabs.com/test.php",
  "description": "Test Description",
  "tags": {
    "data": \[
      {
        "id": "908180082612873",
        "text": "evilevil"
      },
      {
        "id": "884078131700721",
        "text": "testing"
      }
    \]
  },
  "status": "UNKNOWN"
}

ThreatIndicator
===============

An indicator of compromise.

Fields
------

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat indicator. Automatically assigned at create time, and non-editable. | `number` |
| `indicator` | The value of the indicator. Non-editable after initial creation of the indicator. | `string` |
| `type` | The type of indicator. Non-editable after initial creation of the indicator. | List of [`IndicatorType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type) |

### Sample Usage

Example query for a specific indicator: 788497497903212:

https://graph.facebook.com/`v18.0`/788497497903212/?access\_token=555|aSdF123GhK

Data returned:

{
   "indicator": "facebook.com",
   "type": "DOMAIN",
   "id": "788497497903212"
}

Connections
-----------

| Name | Description | Type |
| --- | --- | --- |
| `descriptors` | Subjective opinions about the indicator | [`ThreatDescriptor`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) |
| `related` | Other threat indicators that have been associated | [`ThreatIndicator`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) |

### Sample Usage

Example query for descriptors related to a specific indicator: 852121234856016

https://graph.facebook.com/`v18.0`/852121234856016/descriptors/?access\_token=555|aSdF123GhK

Data returned:

 {
   "data": \[
  {
    "id": "811927545529339",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "588498724619612",
      "name": "Facebook CERT ThreatExchange"
    },
    "type": "DOMAIN",
    "raw\_indicator": "test1434227164.evilevillabs.com",
    "description": "This is our test domain. It's harmless",
    "status": "NON\_MALICIOUS"
  },
  {
    "id": "799906626794304",
    "indicator": {
      "indicator": "test1434227164.evilevillabs.com",
      "type": "DOMAIN",
      "id": "852121234856016"
    },
    "owner": {
      "id": "682796275165036",
      "name": "Facebook Site Integrity ThreatExchange"
    },
    "type": "DOMAIN",
    "raw\_indicator": "test1434227164.evilevillabs.com",
    "description": "Malware command and control",
    "status": "MALICIOUS"
  }
\],
"paging": {
  "cursors": {
    "before": "ODExOTI3NTQ1NTI5MzM5",
    "after": "Nzk5OTA2NjI2Nzk0MzA0"
  }
}

ThreatPrivacyGroup
==================

A list of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) to which data can be shared. Only available in versions 2.4+ of the Graph API.

Fields
------

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat privacy group | `number` |
| `name` | The name of the threat privacy group | `string` |
| `description` | A human readable description of the group | `string` |
| `members_can_see` | If true, group members can view this group, including its name, description, and list of members | `boolean` |
| `members_can_use` | If true, members are allowed to use this group to protect their own threat data | `boolean` |

### Sample Usage

To create a privacy group, one could POST to:

https://graph.facebook.com/v2.4/threat\_privacy\_groups?name=GROUP1&amp;description=MYFIRSTGROUP&amp;access\_token=555|asdF123

Data returned:

{
  "id": "123456789101112"
}

Connections
-----------

| Name | Description | Type |
| --- | --- | --- |
| `members` | Members of the privacy group | [`ThreatExchangeMember`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) |

### Sample Usage

Example query for a specific privacy group: 123456789101112

https://graph.facebook.com/v2.4/123456789101112/members/?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "999999999999",
      "email": "threatexchange@domain.com",
      "name": "Facebook Administrator"
    }
    ...
  \]
}

ThreatTag
=========

A label which groups [Malware](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware), [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor), and/or [MalwareFamily](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware-family) objects. Once objects are tagged, you can use tags to narrow your search queries in TE.

Fields
------

| Parameter | Description | Type |
| --- | --- | --- |
| `id` | Unique identifier of the threat tag | `number` |
| `text` | The text for this tag | `string` |

### Legal Tags

The text of tags is case insensitive, restricted to letters, numbers, underscores, and colons, and must be UTF-8 friendly. So "שלום" is a valid text, but "#example-tag" is not.

### Sample Usage

Example query for a specific ThreatTag: 908180082612873

Data returned:

{
  "id": "908180082612873",
  "text": "evilevil"
}

Example of searching for a tag by text 'evilevil'. Note that partial tag search is supported.

https://graph.facebook.com/v2.7/threat\_tags/?access\_token=555|aSdF123GhK&amp;text=evilevil

Data returned:

{
  "data": \[
    {
      "id": "908180082612873",
      "text": "evilevil"
    }
    ...
  \]
}

Connections
-----------

| Name | Description | Type |
| --- | --- | --- |
| `tagged_objects` | The objects tagged with this text. | `Malware`, `ThreatDescriptor`, `MalwareFamily` |

#### Parameters

The following query parameters are available:

* `tagged_since` - Fetches all objects that have been tagged since this time (inclusive).
    
* `tagged_until` - Fetches all objects that have been tagged until this time (inclusive).
    

Tagged objects are returned in the order based on when the tag was applied, ascending. This timestamp is currently not exposed by the API, but is the same one used by `tagged_since` and `tagged_until`. While this API can be used to create a copy of data in ThreatExchange, the [threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates/v10.0) API may be better suited for your usecase.

### Sample Usage

Example of tagged objects for a specific ThreatTag: 908180082612873

https://graph.facebook.com/v2.7/908180082612873/tagged\_objects/?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "1039423046092869",
      "type": "THREAT\_DESCRIPTOR",
      "name": "test1464195852.evilevillabs.com"
    },
    ...
  \]
}

Example of tagged objects for a ThreatTag with the text 'ducks'

https://graph.facebook.com/v2.7/threat\_tags/?access\_token=555|aSdF123GhK&amp;text=ducks&amp;fields=id,text,tagged\_objects

Data returned:

{
  "data": \[
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged\_objects": {
        "data": \[
          {
            "id": "1162586023812794",
            "type": "THREAT\_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        \]
      },
    }
  \]
}

Creating a New Tag
------------------

You can create a ThreatTag on-the-fly while creating a ThreatDescriptor. If the ThreatTag does not exist, a new one will be created and applied to the new ThreatDescriptor.

https://graph.facebook.com/v2.7/threat\_descriptors?access\_token=555|aSdF123GhK

POST DATA:
  tags=cows,bar
  &amp;type=DOMAIN
  &amp;indicator=test1466722733.evilevillabs.com
  &amp;description=this is an example with tags
  &amp;privacy\_type=VISIBLE
  &amp;share\_level=GREEN
  &amp;status=UKNOWN

Data returned:

{
  "success": true,
  "id": "1162586023812794"
}

To create a ThreatTag without labeling any objects, you can post to the /threat\_tags endpoint explicitly:

https://graph.facebook.com/v2.7/threat\_tags?access\_token=555|aSdF123GhK

POST DATA:
  text=superlongtagfortestingcreation
  &amp;objects=973966502652751,898684593584287

Data returned:

{
  "success": true,
  "id": "1373232162693002"
}

Example of updating a ThreatDescriptor with more tags. If the tag does not exist, a new one will be created and applied to this ThreatDescriptor.

https://graph.facebook.com/v2.7/1162586023812794?access\_token=555|aSdF123GhK

POST DATA:
  tags=ducks,chicken

Data returned:

{
  "success": true
}

Popular Tags
------------

Here is a list of the most popular tags categorizing data related to attacks:

| Name | Description |
| --- | --- |
| `access_token_theft` | Theft of an OAuth style or similar access token |
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

| Name | Description |
| --- | --- |
| `bad_actor` | Details on a presumed bad actor (e.g. botherder, spammer) |
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
| `malware_sample` | A specific piece of [Malware](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware) |
| `malware_victim` | A victim of [Malware](https://developers.facebook.com/docs/threat-exchange/reference/apis/malware) |
| `proxy_ip` | An IP address known to be a proxy or VPN |
| `signature` | Represents some means or pattern for detecting a threat |
| `web_request` | A full web request, optionally with GET query parameters |
| `whitelist_domain` | An Internet domain that should be treated as non-malicious |
| `whitelist_ip` | An IP address that should be treated as non-malicious |
| `whitelist_url` | An URI that should be treated as non-malicious |

Threat Exchange Impact Report
=============================

Reading
-------

You can't perform this operation on this endpoint.

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

Confidence
==========

The `confidence` field describes the confidence in a particular piece of subjective data on ThreatExchange.

Values
------

The `confidence` field can be any number between 1 and 100. When uploaded, the field must be specified numerically. However, you should use the following guidelines when uploading data: low confidence = 25, medium confidence = 50, high confidence = 75.

IndicatorType
=============

The kind of indicator being described by a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. Despite the name IndicatorType, these values can also be used as values for [ThreatDescriptor's](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor)`type` field.

.

Values
------

| Name | Description | Type | Example |
| --- | --- | --- | --- |
| `ADJUST_TOKEN` | A modification to token permissions in the Windows operating system | `string` | `'Debug'` |
| `API_KEY` | An API key being used within malware | `string` | `'JH52anj9snaQ'` |
| `AS_NUMBER` | An autonomous system number | `number`, `valid ASN` | `'32934'` |
| `BANNER` | A banner reply from a server | `string` | `'Apache/2.2.22 (Ubuntu) Server at localhost Port 80'` |
| `CMD_LINE` | A command line executed in an operating system | `string` | `'cmd.exe C:\tmp\malware.exe'` |
| `COOKIE_NAME` | The name of an HTTP cookie used. | `string` | `'login_name'` |
| `CRX` | A Google Chrome extension ID | `string` | `'aohghmighlieiainnegkcijnfilokake'` |
| `DEBUG_STRING` | A text string found in a binary file | `string` | `'d:\admin\projects\test\test.pdb'` |
| `DEST_PORT` | Network port for the destination host | `number`, bounded to 1-65536 | `'443'` |
| `DIRECTORY_QUERIED` | A string of a file path queried by a process | `string` | `'C:\Windows\tmp'` |
| `DOMAIN` | A valid Internet domain name | `string` | `'facebook.com'` |
| `EMAIL_ADDRESS` | A valid email address | `string` | `'postmaster@facebook.com'` |
| `FILE_CREATED` | File created by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_DELETED` | File deleted by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_MOVED` | File moved by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_NAME` | A file name on a system, can include the path | `string` | `'C:\Temp\bot.exe'` |
| `FILE_OPENED` | File opened by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_READ` | File read by a process | `string` | `'C:\Temp\bot.exe'` |
| `FILE_WRITTEN` | File written by a process | `string` | `'C:\Temp\bot.exe'` |
| `GET_PARAM` | An HTTP GET query parameter name | `string` | `'search'` |
| `HASH_IMPHASH` | The PE Import hash of a Portable Executable file | `string` | `'17de70812f274b0edd9d0afe69bc7fe2'` |
| `HASH_MD5` | An MD5 hash of a file, string, etc | `string` | `286755fad04869ca523320acce0dc6a4` |
| `HASH_PDQ` | A PDQ hash of an image | `string` | `064bc5ede01712654843fe46b16de93956fae0153baba5d47ac31ef8a5905ec0` See also<br><br>[https://github.com/facebook/ThreatExchange/tree/master/hashing/pdq](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fhashing%2Fpdq&h=AT0u4h7l_rO2GWaz08asXlwR1ZASkbNrcc0lmTjqIREG4r09hrP3bHa1_QD_4mxP5fJOoLuRwCqcQQuCIrROHe0H0Xf8bfbMqQJgkMAVC0cIVnibVmSzALAaNFrXeT5NWprNzCnC0RVJdyo4) |
| `HASH_TMK` | A TMK hash of a video | `string` | Binary format documented at<br><br>[https://github.com/facebook/ThreatExchange/tree/master/hashing/tmk](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fhashing%2Ftmk&h=AT3KLKaGngDTWZL7DyVgTEiV1xoiemII9ypGyjSV5RnjxW4CJLkEV2Mh2iVXcQFVqgpUCMcAsJmxvAYEhTG6CZNM0Cgkz2Ca-8a8u9jIxT2P6Q6m6XRZHpdA9aSjCZx0b6Y1YhmDzQdijtTy) |
| `HASH_SHA1` | A SHA1 hash of a file, string, etc. | `string` | `c8fed00eb2e87f1cee8e90ebbe870c190ac3848c` |
| `HASH_SHA256` | A SHA256 hash of a file, string, etc. | `string` | `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` |
| `HASH_SSDEEP` | An SSDeep hash of a file. See http://www.forensicswiki.org/wiki/Ssdeep for more details. | `string` | `768:ZY1jwLjYVmvZDnaB86WaRgAnL4PaxsJc2U0YjpsqANH+Y3b/JgKDiip47502Do1:ZY18LjYUvZDkIrPaxsJ3bxgPcP1` |
| `HASH_VIDEO_MD5` | An MD5 Hash of a video file. | `string` | `460ecaeb03f4870b1db43eda1c7faed7` |
| `HTML_ID` | The value of an ID attribute on an HTML or XHTML tag that identifies malicious or injected markup. | `string` | `my-injected-ad` |
| `HTTP_REQUEST` | The raw DELETE, GET, HEAD or POST. | `string` | `GET /index.html HTTP/1.1` |
| `IP_ADDRESS` | An IP address, version agnostic. | `string` | `127.0.0.1` or `fe80::202:c9ff:fe54:5952` |
| `IP_SUBNET` | A CIDR Mask, version agnostic. | `string` | `128.0.0.0/24` or `fe80::202:c9ff:fe54:5952/64` |
| `ISP` | An Internet service provider. | `string` | `MyInternetServiceProvider Inc.` |
| `LATITUDE` | The latitude for a location, as degrees dotted decimal. | `float` | `37.484924` |
| `LAUNCH_AGENT` | The name of a LaunchAgent on OS X. | `string` | `/System/Library/LaunchAgents/com.apple.quicklook.plist` |
| `LOCATION` | The name of a physical location. Note that there is a separate field `COUNTRY`. | `string` | `Menlo Park, CA` |
| `LONGITUDE` | The longitude for a location, as degrees dotted decimal. | `float` | `-122.148287` |
| `MALWARE_NAME` | The common name for a piece of malware. | `string` | `Zeus` |
| `MEMORY_ALLOC` | The process file name that had memory allocated. | `string` | `C:\Temp\bot.exe` |
| `MEMORY_PROTECT` | The process file name that had memory permissions altered. | `string` | `C:\Temp\bot.exe` |
| `MEMORY_WRITTEN` | The process file name that had its memory written to. | `string` | `C:\Temp\bot.exe` |
| `MUTANT_CREATED` | Mutex created by a process. | `string` | `bot-installed` |
| `MUTEX` | A symbol defined in an OS for synchronization. | `string` |     |
| `NAME_SERVER` | The host name that belongs to a name server. | `string` | `ns1.facebook.com` |
| `OTHER_FILE_OP` | Miscellaneous operations performed on a file. | `string` | `C:\Temp\bot.exe` |
| `PASSWORD` | A password value, **must** be provided as an MD5 hash. | `string` |     |
| `PASSWORD_SALT` | A salt for hashing a password. | `string` |     |
| `PAYLOAD_DATA` | A piece of malicious content (e.g. an image or a document), Base64 encoded. | `string` |     |
| `PAYLOAD_TYPE` | The MIME type format of the content in the PAYLOAD\_DATA field. | `string` | `image/jpeg` |
| `POST_DATA` | Data sent in a POST request. | `string` | `bot_id=1234&field2=Microsoft%20Windows` |
| `PROTOCOL` | The type of data protocol. | `string` | `tcp`, `ftp` |
| `REFERER` | The URI appearing in an HTTP referrer header. | `string` | `http://www.facebook.com/` |
| `REGISTRAR` | The registrar for a domain. | `string` | `REGISTER.COM, INC.` |
| `REGISTRY_KEY` | The name of a registry key in Microsoft Windows. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_CREATED` | Registry key created. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_DELETED` | Registry key deleted. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_ENUMERATED` | Registry key enumerated by a process. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_MONITORED` | Registry key monitored. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_OPENED` | Registry key opened. | `string` | `HKEY_USERS\Software\Microsoft\Visual Basic` |
| `REG_KEY_VALUE_CREATED` | Registry key value created. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_DELETED` | Registry key value deleted. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_MODIFIED` | Registry key value modified. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `REG_KEY_VALUE_QUERIED` | Registry key value queried. | `string` | `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| `SIGNATURE` | The signature string for detecting a threat. | `string` |     |
| `SOURCE_PORT` | Network port of the originating host. | `integer` | `13456` |
| `TELEPHONE` | The full, international version of a telephone number | `string` | `+12225551212` |
| `TEXT_STRING` | A string to match text content | `string` | `This is some text that might be harmful` |
| `TREND_QUERY` | Rules to match text. JSON serialized string. Once deserialized,<br><br>* `"and"` is a list of conditions, ALL of which should match<br>* each AND condition is a JSON object with a single `"or"` key.<br>* The value of the `"or"` key is a list of keywords or Regular expressions, ANY of these causes a match.<br>* Regular expressions begin with `"regex-"`, all other terms are keywords.<br>* `"not"`is a list of keywords, ANY of which should prevent a match.<br><br>  <br><br>Example: The sample to the right would match content that either contains the substring `foo` or matches the regular expression `.*bar.*`, and also contains the substring `zed` but does not contain either the substring `baz` or `ler` | JSON-Serialized `string` | {<br>        "and": [<br>            {"or": ["foo", "regex-/.*bar.*/"]},<br>            {"or": ["zed"]},<br>        ],<br>        "not": [<br>            "baz",<br>            "ler",<br>        ]<br>    } |
| `URI` | An uniform resource identifier. | `string` | `http://www.facebook.com/some_page.php?test=yes` or `/index.html` |
| `USER_AGENT` | A browser\`s user agent string. | `string` | `Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0` |
| `VOLUME_QUERIED` | Volume query action by a process. | `string` |     |
| `WEBSTORAGE_KEY` | The name of a key used in HTML5 local or session storage. | `string` | `malware_session_data` |
| `WEB_PAYLOAD` | The base64 encoded raw payload of a web request, with headers. | `Base64 string` | `R0VUIGh0dHA6Ly9za2V0Y2h5LWRvbWFpbi5iaXovaW1nLTcxNzAwMy5qcGcgSFRUUC8xLjEKSG9zdDogc2tldGNoeS1kb21haW4uYml6ClVzZXItQWdlbnQ6IHdlYmNvbGxhZ2UvMS4xMzVhCgp0ZXN0IGRhdGEK` |
| `WHOIS_NAME` | The name in whois information. | `string` | `Domain Administrator` |
| `WHOIS_ADDR1` | The first address line in whois information. | `string` | `1601 Willow Road` |
| `WHOIS_ADDR2` | The second address line in whois information. | `string` | `Menlo Park, CA 94025` |
| `XPI` | A Firefox addon ID. | `string` | `{e968fc70-8f95-4ab9-9e79-304de2a71ee1}` |

PrecisionType
=============

Defines how accurately an object detects its intended target, victim or actor.

Values
------

| Name | Description |
| --- | --- |
| `UNKNOWN` | There is no known precision information. |
| `LOW` | The object is likely to detect false positives. |
| `MEDIUM` | The object may detect false positives. |
| `HIGH` | The object is unlikely to detect false positives. |

PrivacyType
===========

Defines who may view and search for a specific object within ThreatExchange.

Values
------

| Name | Description |
| --- | --- |
| `HAS_PRIVACY_GROUP` | Only a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) may view or search for the data. |
| `HAS_WHITELIST` | Only specific members of ThreatExchange may view or search for the data. |
| `VISIBLE` | All members of ThreatExchange may view and search for the data. |

ReactionType
============

A possible reaction to a visible piece of ThreatExchange information.

For more info, see the [Reacting To Existing Data](https://developers.facebook.com/docs/threat-exchange/reference/reacting/v2.8) documentation

Values
------

| Value | Meaning |
| --- | --- |
| `HELPFUL` | Indicates the piece of information was valuable. |
| `NOT_HELPFUL` | Indicates the piece of information was NOT valuable. |
| `OUTDATED` | Indicates the piece of information is no longer relevant and should be expired. |
| `SAW_THIS_TOO` | Indicates the reactor saw this in the wild. |
| `WANT_MORE_INFO` | Indicates the reactor wants additional information. |
| `DISAGREE_WITH_TAGS` | Indicates the reactor doesn't agree with the current tags on this object. If the tags change, this reaction is automatically removed. |
| `INGESTED` | Acknowledgement of receipt. Helps contributors get feedback on the usefulness of their data to others. |
| `IN_REVIEW` | Acknowledgement of intention to review. Helps contributors get feedback on the usefulness of their data to others. |
| `ALREADY_KNOWN` | Acknowledgement that a recipient was already aware of the signal. Helps contributors get feedback on the usefulness of their data to others. |
| `REVIEWED` | Acknowledgement of completed review. Helps contributors get feedback on the usefulness of their data to others. |

ReviewStatusType
================

Indicates if the data was reviewed and, if via automation or a human.

Values
------

| Name | Description |
| --- | --- |
| `UNKNOWN` | No review data available. |
| `UNREVIEWED` | The data has not been reviewed. |
| `PENDING` | The data is currently under review. |
| `REVIEWED_MANUALLY` | The data was reviewed manually. |
| `REVIEWED_AUTOMATICALLY` | The data was reviewed by an automated system. Note that you cannot set this value if the current value is REVIEWED\_MANUALLY. This restriction was added to prevent automated systems from clobbering the work of human reviewers. To get around this, you must first change the review status to another value, e.g. PENDING, and then change it to REVIEWED\_AUTOMATICALLY. |

SeverityType
============

A description of the dangerousness of the threat associated with a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object. The order of the values below are ordered from least severe to most severe.

Values
------

| Name | Description |
| --- | --- |
| `UNKNOWN` | No rating of severity is available |
| `INFO` | The indicator is associated with a threat of little or no severity. |
| `WARNING` | The indicator is associated with a threat of some severity. |
| `SUSPICIOUS` | The indicator is associated with a threat that is likely severe. |
| `SEVERE` | The indicator is associated with a threat that is severe. |
| `APOCALYPSE` | The indicator is associated with a threat that is extremely severe and should be addressed immediately. |

SignatureType
=============

The kind or format of signature described by a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object with [ThreatType](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type) of `SIGNATURE`.

Values
------

| Name | Description |
| --- | --- |
| `BRO` | A signature string compatible with a Bro sensor |
| `REGEX_URL` | A PCRE compatible regular expression |
| `SNORT` | A signature string compatible with the Snort format |
| `SURICATA` | A signature string compatible with the Suricata format |
| `UNKNOWN` | An unknown signature type |
| `YARA` | A signature string compatible with the Yara format |

ShareLevelType
==============

The following Share Level Type designations are based on the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT1u3mAAoMs11vUGIUAZkTCJKZB3o3vn9iHBPKmNp2TtUK8V8IXahPxjMqZuBBNMJwO2VFKN9Na6OuPXZe_LVr9Tkq2zrRS_jRYTDHRdrxIlTWLXm3nzDiDZPyUH6CVk7IqoIc7VJ-wl2Fii) and govern how ThreatData may be re-shared both within and outside of ThreatExchange.

These `ShareLevelType` designations are cited in and form part of the [ThreatExchange's Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms) (the "Terms"). Nothing in the following `ShareLevelType` designations prohibit a Developer from using a security service provider to store and process ThreatData it receives, so long as the security service provider only uses the ThreatData on behalf of the Developer and fully complies with the Terms. All capitalized terms used but not defined on this page shall have the meanings assigned to them in the Terms.

Values
------

| Name | Description |
| --- | --- |
| `RED` | Developer may permit access to view Threat Data it receives that is labeled with share level `RED` solely to those employees of Developer who have a strict need to know for the Purpose. Threat Data labeled with share level `RED` must not be reproduced, retransmitted, or otherwise re-distributed within Developer's organization or to any other party, including but not limited to Developer's affiliates, customers, partners or any other party, in each case, without the prior written consent of the original publisher. |
| `AMBER` | Developer may share Threat Data it receives that is labeled with share level `AMBER` solely to Developer and its subsidiaries who have a need to know for the Purpose (as that term is defined in the ThreatExchange Program Terms & Conditions), and solely as widely within Developer's organization(s) as is reasonably necessary for Developer to act on that information. |
| `GREEN` | Developer may share Threat Data it receives that is labeled with share level `GREEN` via a non-publicly accessible channel, solely to Developer's peer and partner organizations, preferred vendors, customers, and/or other entities who would find it useful as part of their existing business relationship with Developer, provided in each instance that the third party with whom Developer shares Threat Data has agreed in writing to keep all Threat Data confidential and not disclose Threat Data to any third party. |
| `WHITE` | Developer may share Threat Data it receives that is labeled with share level `WHITE` without restriction, subject to any attribution requirements specified by the original publisher(s). |

StatusType
==========

StatusType is an important field in ThreatExchange, as it corresponds to whether the upload is referring to malicious or harmful content. This help you determine what the original uploader's intent was in uploading signals, and therefore what you should do when you find matching or corresponding data on your platform.

Values
------

| Name | Cybersecurity Description | Content Safety Description |
| --- | --- | --- |
| `MALICIOUS` | The object is consistently malicious | Corresponds to harmful content or behavior. |
| `SUSPICIOUS` | The object can be malicious, dependent on the context in which it is found | Helps discover harmful content or requires additional investigation to discover harmful content. |
| `NON_MALICIOUS` | The object is not known to be malicious | Informational or trend information that does not lead to the discovery of harmful content. |
| `UNKNOWN` | No maliciousness information available | Do not use this StatusType for content safety. |

/<privacy-group>/threat\_updates
================================

This call is not currently enabled for all PrivacyGroups. A 500 error will be returned if this call is used with PrivacyGroup that doesn't have \`/threat\_updates\` enabled. If you would like to enable this call for your PrivacyGroup please [contact the ThreatExchange team](mailto:threatexchange@fb.com).

ThreatExchange provides [multiple APIs](https://developers.facebook.com/docs/threat-exchange/reference/apis/) for querying data. Most of these APIs will only allow you to know the current state of the object, and if it is later updated or removed, you can only learn of changes by polling the objects again. ThreatExchange API integration works best when you can keep an up-to-date copy of the information that you are interested in, and re-polling all data would be cumbersome.

`/threat_updates` provides a solution to keeping a copy of data within a PrivacyGroup, specifically for the data that users tell us they most need kept up to date. `/threat_updates` allows for a specific projection of the ThreatExchange graph database to turn it into a list of signals with opinions. By tailing `/threat_updates`, you can learn of updates to that projection within seconds, and so the liveness of the data is only limited by how frequently you poll.

When data in the PrivacyGroup is updated, an event is moved to the "end" of the update list. All updates are ordered by `update_time`, and you can save this time to resume fetching from where you left off.

Update Events
-------------

`/threat_updates` entries represent one of two events, which can be differentiated using the `should_delete` flag.

| Event | `should_delete` | Meaning |
| --- | --- | --- |
| Update | false | An opinion connected to the ThreatIndicator has been created or updated. Fetch connected data to get updates. |
| Delete | true | A ThreatIndicator has been removed from the PrivacyGroup or deleted. |

Otherwise, entries returned by this API behave as [ThreatIndicator Objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/), with additional fields described below.

Delete Event TTL, Polling Frequency, and Checkpointing
------------------------------------------------------

Deletion events **are only stored for 90 days**, and so you must poll more frequently than that, or your copy of the database will become invalid. We generally recommend polling daily to prevent a large backlog of updates from accruing, and many platforms will want to poll more frequently than that to have a lower latency between sharing and ingestion. We don't recommend polling more frequently than 1/minute.

To resume from where you last left off, set the `start_time` to the largest `update_time` you have previously seen. It is important that you not attempt to use the time you completed your last fetch as the checkpoint, as there may be a small delay between when updates are written and when they appear in `/threat_updates`.

`start_time` is inclusive, so you may see updates you have already seen when there is not much activity in a PrivacyGroup.

This call may reveal indicators that have been removed from the privacy group. When you recieve notice of a deletion, you should remove it from your copy of ThreatExchange data, as it may have been previously shared in error. See [Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms) for more.

Maintaining a copy of data in a PrivacyGroup using `threat_updates`
-------------------------------------------------------------------

The object emitted by `threat_updates` is [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/), and has the same fields and connections. However, the connections are modified such that only data in the given PrivacyGroup are returned.

This allows you to use `/threat_updates` as an update stream to keep a copy of the data, keyed by the `id` of the [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/). The simplest way to do this is use the `fields=` parameter to fetch all the data you are interested in connected data, and store the resultant data.

### Example Table Schema

Here's is a sample database table schema you could use (for a single PrivacyGroup):

| Column | Type | Note |
| --- | --- | --- |
| indicator\_id | 64 bit integer (Primary Key) | An opinion connected to the ThreatIndicator has been created or updated. Fetch connected data to get updates. |
| indicator\_type | string | The type of the signal (e.g. HASH\_MD5). Each type usually needs type-specific handling, so you could provide a secondary index on (type, update\_time) to checkpoint your own internal processing. This column is an example of parsing specific data out of the payload for the purposes of indexing - you may find you are interested in other fields as well. |
| json\_payload | JSON | The raw JSON, including connections fetched by `fields=` returned by the API. |

### Updating the Table

In order to build your copy of the database, begin polling at `start_time=0`.

For each entry seen:

* Update: `UPSERT INTO MyTableForPrivacyGroup VALUES ($response[id], $response[type], $response)`
* Delete: `DELETE FROM MyTableForPrivacyGroup WHERE indicator_id = $response[id]`

When you completely exhaust `/threat_updates`, you should have a complete and up-to-date copy of the data stored in ThreatExchange.

Store the largest `update_time` that you have seen to use as a the `start_time` for the next time you fetch, as described above.

What changes constitute an Update
---------------------------------

`/threat_updates` will generate an update to changes to [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) that have been shared to the PrivacyGroup. Changes to the fields or connected data will generate an update.

At a minimum, this is:

1. If a [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) is added to the PrivacyGroup, removed from the PrivacyGroup, or deleted.
2. Changes to fields directly stored on the [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/)
3. Changes in which [ThreatTags](https://developers.facebook.com/docs/threat-exchange/reference/apis/docs/threat-exchange/reference/apis/threattags/) are on those ThreatDescriptors
4. Changes in which [Reactions](https://developers.facebook.com/docs/threat-exchange/reference/apis/docs/threat-exchange/reference/apis/threattags/) are on those ThreatDescriptors

Note that not every update will appear to have changed data - `/threat_updates` only stores the last update to an object, and so changes that are rapidly undone may not appear to change your copy of the data. Additionally, if you select only some fields, you will see updates that don't change the fields you selected.

Open Source Fetching Implementation
-----------------------------------

Instead of building an implementation from scratch, you can start with our [Python open source library](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmain%2Fpython-threatexchange&h=AT1ITz-ZEbJi1WbWUNJ0hDz-h5WZxS0jW5go7YWUoWByFPDSm4nxuDzIftJoQbwd2vbuGT9PHcjb-MJdKTRWf1UbDONoSwQfDFMHPUjVwllXBcCf7PfWlZADTYGtgjMLQBLqBAiDofEW_oun) which can also be used as a reference implementation.

Parameters
----------

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API.
    
* `types` - The types of indicators to search for.
    
* `start_time` - Search for indicators that last updated on or after this timestamp.
    
* `stop_time` - Search for indicators that last updated before this timestamp.
    
* `limit` - Defines the maximum size of a page of results
    
* `fields` - A list of fields to return in the response, if not specified all fields are returned.
    
    * `id` - The id of the ThreatIndicator
        
    * `should_delete` - Whether this is an update or deletion event
        
    * `last_updated` - The checkpointable timestamp of the update.
        
    * `type` - Unchanged from [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
        
    * `indicator` \- Unchanged from [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
        
    * `descriptors` - A list of [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) in this PrivacyGroup.
        
        * Clients that want to deeply inspect data should refer to the fields selection in [ThreatDescriptor objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/) - you can nest field selections with curly braces: example: `fields=descriptors{owner{name}}`
            
        
    * `tags` A shortcut for a flattened list of tag names from `descriptors{tags{name}}`
        
    * `status` A shortcut to taking the highest severity status from`descriptors{status, reactions}`
        
    * `applications_with_opinions` A shortcut for a flattened list of ThreatExchange member ids from `descriptors{owner, reactions{owner}}`
        
    

Example query for all indicators that last updated between December 2019 (1575187200) to March 2020 (1583049600) for privacy group 123456789012345:

https://graph.facebook.com/`v18.0`/123456789012345/threat\_updates/?access\_token=555|aSdF123GhK&start\_time=1575187200&stop\_time=1583049600&fields=id,indicator,type,creation\_time,last\_updated,should\_delete,tags,status,applications\_with\_opinions

Data Returned:

{
    "data": \[
        {
            'id': '123456',
            'indicator': 'a\_hash\_that\_was\_created\_or\_updated',
            'type': 'HASH\_PDQ',
            'creation\_time': 1581977111,
            'last\_updated': 1582372222,
            'should\_delete': False,
            'tags': \['tag1', 'another\_tag'\],
            'status': 'MALICIOUS',
            'applications\_with\_opinions': \['1234567890'\]
        },
				{
            'id': '123457',
            'indicator': 'a\_hash\_that\_should\_be\_deleted',
            'type': 'HASH\_PDQ',
            'creation\_time': 1581977111,
            'last\_updated': 1582372222,
            'should\_delete': True,
            'tags': \['tag1', 'another\_tag'\],
            'status': 'MALICIOUS',
            'applications\_with\_opinions': \['1234567890'\]
        },
        ...
    \]
    "paging": {
        "cursors": {
            "before": "MjVFR",
            "after": "MjQZD"
        }
    "next": "https://graph.facebook.com/`v18.0`/123456789012345/threat\_updates/?access\_token=555|aSdF123GhK&start\_time=1575187200&stop\_time=1583049600&types=HASH\_MD5,HASH\_PDQ&fields=id,indicator,type,creation\_time,last\_updated,should\_delete,tags,status,applications\_with\_opinions&after=MjQZD"
    }

/threat\_tags
=============

This API call enables searching for tags in ThreatExchange. With this call you can search for ThreatTag objects by text.

Parameters
----------

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API.
    
* **`text`** - Freeform text field with a value to search for. This value should describe a broader type or class of attack you are interested in.
    
* `fields` - A list of fields to return in the response
    
* `subscribed` - when POSTing to a specific tag, will subscribe you to a tag for Webhooks
    

Example query for all tags which start with `malware`:

https://graph.facebook.com/`v18.0`/threat\_tags?access\_token=555|aSdF123GhK&text=malware

{
  "data": \[
    {
      "id": "1318516441499594",
      "text": "malware"
    },
    {
      "id": "1104531542952223",
      "text": "malwaresite"
    },
    ...
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v14.0/threat\_tags?access\_token=555|7C1234&amp;text=malware"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
text = 'malware'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v14.0/threat\_tags?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

Example query for tags which start with `ducks` and fetching the tagged objects.

https://graph.facebook.com/`v18.0`/threat\_tags/?access\_token=555|aSdF123GhK&text=ducks&fields=id,text,tagged\_objects

Data returned:

{
  "data": \[
    {
      "id": "501159930008561",
      "text": "ducks"
      "tagged\_objects": {
        "data": \[
          {
            "id": "1162586023812794",
            "type": "THREAT\_DESCRIPTOR",
            "name": "test1469481750.evilevillabs.com"
          },
          ...
        \]
      },
    }
  \]
}

/threat\_indicators
===================

This API call enables searching for indicators of compromise stored in ThreatExchange. With this call you can search for indicators by free text, type, or all in a specific time window. Combinations of these query types are also allowed.

Parameters
----------

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API. It is a concatenation of &lt;your-app-id&gt;|&lt;your-app-secret&gt;. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `limit` - Defines the maximum size of a page of results. The maximum is 1,000.
    
* `text` - Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects.
    
* `sort_order` - A given [SortOrderType](https://developers.facebook.com/docs/threat-exchange/reference/apis/sort-order-type)
    
* `sort_by` - Sort results by RELEVANCE or by CREATE\_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query.
    
* `strict_text` - When set to 'true', the API will not do approximate matching on the value in text
    
* `threat_type` - The broad threat type the indicator is associated with (see [ThreatTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-type/))
    
* `type` - The type of indicators to search for (see [IndicatorTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/))
    
* `since` - Returns indicators collected after a timestamp
    
* `until` - Returns indicators collected before a timestamp
    
* `fields` - A list of fields to return in the response
    

Example query for all malicious IP addresses that are proxies:

https://graph.facebook.com/v2.7/threat\_indicators?access\_token=555|aSdF123GhK&amp;type=IP\_ADDRESS&amp;text=proxy

The data returned by this API call changed in Platform version 2.4. Data returned in Platform v2.3:

{
  "data": \[
    {
      "added\_on": "2015-02-25T14:46:37+0000", 
      "confidence": 50, 
      "description": "Localhost IP", 
      "indicator": "127.0.0.1", 
      "severity": "INFO", 
      "share\_level": "GREEN", 
      "status": "NON\_MALICIOUS", 
      "type": "IP\_ADDRESS", 
      "threat\_types": \[
        "MALICIOUS\_IP"
      \], 
      "id": "804745332940593"
    }
  \], 
  "paging": {
    "cursors": {
      "before": "MA==", 
      "after": "MA=="
    }
  }
}

Data returned in Platforms v2.4 and above:

{
  "data": \[
    {
      "indicator": "77.2.132.202",
      "type": "IP\_ADDRESS",
      "id": "675010235935327"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.7/threat\_indicators?access\_token=555|1234&amp;pretty=0&amp;text=proxy&amp;type=IP\_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.7/threat\_indicators?type=IP\_ADDRESS&amp;text=proxy&amp;access\_token=555%7C1234"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
text = 'proxy'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'type' : type\_,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v2.7/threat\_indicators?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

The same query in Java:

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

    public final static void main(String\[\] args) throws Exception {
        String url = "https://graph.facebook.com/v2.7/threat\_indicators?";
        String appID = "5555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP\_ADDRESS";
        String text = "proxy";
        
        String query = String.format("access\_token=%s&amp;type=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
                text
                );
        URLConnection connection = new URL(url + query).openConnection();
        InputStream response = connection.getInputStream();
        System.out.print(convertStreamToString(response));
        response.close();
    }
    
    static String convertStreamToString(InputStream inputStream){
        Scanner scanner = new Scanner(inputStream).useDelimiter("\\\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }
    
}

The same query in PHP:

<?php
  $appID = "555"; // Replace this with your AppID
  $appSecret = "1234"; // Replace this with your App Secret
  $type = 'IP\_ADDRESS';
  $text = 'proxy';
  $access\_token = $appID . "|" . $appSecret;

  $ch = curl\_init();
  curl\_setopt($ch, CURLOPT\_URL,
    "https://graph.facebook.com/v2.7/threat\_indicators?" .
    "access\_token=" . $access\_token .
    "&amp;type=" . $type .
    "&amp;text=" . $text);
  curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
  $response = curl\_exec($ch);
  $json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
  print($json . PHP\_EOL);
  curl\_close($ch);
?>

/threat\_descriptors
====================

NOTE: Queries using this call are not guaranteed to be comprehensive and may only return partial results. See how to do bulk download in [Best Practices](https://developers.facebook.com/docs/threat-exchange/best-practices).

The API call enables searching for subjective opinions on indicators stored in ThreatExchange. With this call you can search by free text, type, submitter, or all in a specific time window. Combinations of these query types are also allowed. This call is only permitted on Platform versions 2.4 and later.  
  
This query may only return partial results and should only be used to find examples of ThreatDescriptors matching the query parameters. To get a comprehensive list of ThreatDescriptors you should use the [`\threat_tags` endpoint](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-tags) and do any necessary post-process filtering

Parameters
----------

The following query parameters are available (bold params are required):

* **`access_token`** - The key for authenticating to the API, in the format <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `include_expired` - When set to true, the API can return data which has expired. Expired data is denoted by having the expire\_time field as non-zero and less than the current time.
    
* `limit` - Defines the maximum size of a page of results. The maximum is 1,000.
    
* `max_confidence` - Define the maximum allowed confidence value for the data returned.
    
* `min_confidence` - Define the minimum allowed confidence value for the data returned.
    
* `owner` - Comma-separated list of AppIDs of the person who submitted the data.
    
* `text` - Freeform text field with a value to search for. This can be a file hash or a string found in other fields of the objects.
    
* `review_status` - A given [ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)
    
* `share_level` - A given [ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type)
    
* `sort_by` - Sort search results by RELEVANCE or by CREATE\_TIME. When sorting by RELEVANCE, your query will return results sorted by similarity against your text query.
    
* `status` - A given [StatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type)
    
* `strict_text` - When set to 'true', the API will not do approximate matching on the value in text
    
* `tags` - Comma-separated list of tags to filter results
    
* `tags_are_anded` - If omitted or set to `false`, with `tags=a,b` shows descriptors having tags `a` or `b`. If set to `true`, shows descriptors having tags `a` and `b`.
    
* `type` - The type of descriptor to search for (see [IndicatorTypes](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type/))
    
* `since` - Returns descriptors collected after a timestamp
    
* `until` - Returns descriptors collected before a timestamp
    
* `fields` - A list of fields to return in the response
    

Optional parameters for POST -- documented with examples [here](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fapi-reference-examples%2Fjava%2Fte-tag-query&h=AT0kQv-WKLFnUo8VkF998eq5q4pamQOazQBSOk-rHuihEqSdXkd62y6IDbWnoSZ6u9VK8TySuuM0ye9Y192V-iG-8ggIKiaBVTBfvVL87vc3L-J0VqN9rKTrPfElyj5X5oyYSAU-R4t9-mtP):

* `related_ids_for_upload`
    
* `related_triples_for_upload`
    

Example query for all IP addresses submitted by Facebook Administrator which contain the word "proxy":

https://graph.facebook.com/v2.8/threat\_descriptors?access\_token=555|asDF&amp;type=IP\_ADDRESS&amp;owner=820763734618599&amp;text=proxy

Data returned:

{
  "data": \[
    {
      "id": "600399050063019",
      "indicator": {
        "indicator": "52.68.54.232",
        "type": "IP\_ADDRESS",
        "id": "1117440484937537"
      },
      "owner": {
        "id": "820763734618599",
        "email": "threatexchange@support.facebook.com",
        "name": "Facebook Administrator"
      },
      "type": "IP\_ADDRESS",
      "raw\_indicator": "52.68.54.232",
      "description": "TOR Proxy IP Address",
      "status": "UNKNOWN"
    },
    ...
  \],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MjQZD"
    },
    "next": "https://graph.facebook.com/v2.8/threat\_descriptors?access\_token=555|1234&amp;pretty=0&amp;owner=820763734618599&amp;text=proxy&amp;type=IP\_ADDRESS&amp;limit=25&amp;after=MjQZD"
  },
}

The same query using a cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.8/threat\_descriptors?type=IP\_ADDRESS&amp;owner=820763734618599&amp;text=proxy&amp;access\_token=555%7C1234"

The same query in Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret
type\_ = 'IP\_ADDRESS'
owner\_app\_id = 820763734618599
text = 'proxy'

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    'type' : type\_,
    'owner' : owner\_app\_id,
    'text' : text
    })

r = requests.get('https://graph.facebook.com/v2.8/threat\_descriptors?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

The same query in Java:

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatDescriptors {

    public final static void main(String\[\] args) throws Exception {
        String url = "https://graph.facebook.com/v2.8/threat\_descriptors?";
        String appID = "555"; // Replace this with your app ID
        String appSecret = "12345"; // Replace this with your app secret
        String type = "IP\_ADDRESS";
        String ownerAppID = "820763734618599";
        String text = "proxy";
        
        String query = String.format("access\_token=%s&amp;type=%s&amp;owner=%s&amp;text=%s",
                appID + "|" + appSecret,
                type,
                ownerAppID,
                text
                );
        URLConnection connection = new URL(url + query).openConnection();
        InputStream response = connection.getInputStream();
        System.out.print(convertStreamToString(response));
        response.close();
    }
    
    static String convertStreamToString(InputStream inputStream){
        Scanner scanner = new Scanner(inputStream).useDelimiter("\\\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }
    
}

The same query in PHP:

<?php
  $appID = "555"; // Replace this with your AppID
  $appSecret = "1234"; // Replace this with your App Secret
  $type = 'IP\_ADDRESS';
  $text = 'proxy';
  $ownerAppID = "820763734618599";
  $access\_token = $appID . "|" . $appSecret;

  $ch = curl\_init();
  curl\_setopt($ch, CURLOPT\_URL,
    "https://graph.facebook.com/v2.8/threat\_descriptors?" .
    "access\_token=" . $access\_token .
    "&amp;type=" . $type .
    "&amp;owner=" . $ownerAppID .
    "&amp;text=" . $text);
  curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
  $response = curl\_exec($ch);
  $json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
  print($json . PHP\_EOL);
  curl\_close($ch);
?>

/threat\_exchange\_members
==========================

Returns a list of current members of the ThreatExchange, alphabetized by application name. Each application may also include an optional contact email address. You can set this address, if desired, under the settings panel for your application. See [here](https://developers.facebook.com/apps).

Parameters
----------

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* `fields` - A list of fields to return in the response
    

Example query:

https://graph.facebook.com/v2.8/threat\_exchange\_members?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "id": "820763734618599",
      "email": "threatexchange@support.facebook.com",
      "name": "Facebook ThreatExchange"
    },
    ...
  \]
}

The same query using cURL:

curl -i -X GET \\
 "https://graph.facebook.com/v2.8/threat\_exchange\_members?access\_token=555%7C1234"

The same query using Python:

import requests
import json
import ast
import urllib

app\_id = '555' # Replace this with your app ID
app\_secret = '1234' # Replace this with your app secret

query\_params = urllib.urlencode({
    'access\_token' : app\_id + '|' + app\_secret,
    })

r = requests.get('https://graph.facebook.com/v2.8/threat\_exchange\_members?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

/threat\_privacy\_groups
========================

This API call enables the creation of a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) via an HTTP POST request. Privacy groups can be used to protect uploaded data. This feature is only available in versions 2.4+ of the Graph API.

Parameters
----------

The following query parameters are available (bold parameters are required):

* **`access_token`** - The key for authenticating to the API. It is a concatenation of \[your-app-id|your-app-secret\]. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    
* **`name`** - The name of the threat privacy group.
    
* **`description`** - A human readable description of the group.
    
* `members` - A list of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) to be added to the group. Can be modified later.
    
* `members_can_see` - If true, group members can view this group, including its name, description, and list of members. Defaults to FALSE.
    
* `members_can_use` - If true, members are allowed to use this group to protect their own threat data. Defaults to FALSE.
    

### Sample Usage

To create a privacy group:

curl -s -X POST \\
'https://graph.facebook.com/v14.0/threat\_privacy\_groups'\\
'?access\_token=REDACTED'\\
'&name=Testing+curl+post'\\
'&description=Testing+curl+post'\\
'&members\_can\_see=TRUE'

Data returned:

{"id":"1200716590320515"}

To edit:

curl -s -X POST \\
'https://graph.facebook.com/v14.0/1200716590320515'\\
'?access\_token=REDACTED'\\
'&name=Testing+curl+post'\\
'&description=Testing+curl+post+update'

Data returned:

{"success":true}

/<app-id>/threat\_privacy\_groups\_owner
========================================

Returns a list of the [ThreatPrivacyGroups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) of which your app is the owner.

Parameters
----------

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    

The following query parameters are optional:

* `name` - Allows filtering by privacy group name
    
* `description` - Allows filtering by privacy group description
    

Example query:

https://graph.facebook.com/v2.8/<your-app-id>/threat\_privacy\_groups\_owner?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "name": "MYNAMEISBOB",
      "description": "MALWARESIGNATURES",
      "group\_id": "7777777777"
    },
    ...
  \]
}

/<app-id>/threat\_privacy\_groups\_member
=========================================

Returns a list of the [ThreatPrivacyGroups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) of which your app is a member.

Parameters
----------

The following query parameter is required:

* **`access_token`** - The key for authenticating to the API. It is a concatenation of <your-app-id>|<your-app-secret>. For example, if our app ID was 555 and our app secret aSdF123GhK, our access\_token would be "555|aSdF123GhK".
    

The following query parameters are optional:

* `name` - Allows filtering by privacy group name
    
* `description` - Allows filtering by privacy group description
    

Example query:

https://graph.facebook.com/v2.4/<your-app-id>/threat\_privacy\_groups\_member?access\_token=555|aSdF123GhK

Data returned:

{
  "data": \[
    {
      "name": "MYNAMEISBOB",
      "description": "MALWARESIGNATURES",
      "group\_id": "7777777777"
    },
    ...
  \]
}

ThreatExchange Privacy Controls
===============================

All submissions to the ThreatExchange API allow for limiting the visibility of any [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) objects. Currently, ThreatExchange supports three levels of visibility:

* allow all members;
    
* allow a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/); and
    
* allow a whitelist of specific members.
    

The desired privacy setting on an object is specified by the values at the time of a create or edit submission to the API. Privacy settings can also be changed retroactively for data you've already submitted.

Privacy settings are propagated as follows: Threat Exchange members can see an indicator if and only if they can see at least one associated descriptor.

Privacy Fields
--------------

There are two fields that combine to define the privacy on an object within ThreatExchange: `privacy_type` and `privacy_members`.

The `privacy_type` field can have one of the following values:

| Name | Description |
| --- | --- |
| `HAS_PRIVACY_GROUP` | The privacy group IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `HAS_WHITELIST` | The App IDs specified in `privacy_members` can see the object, while the rest of the member community cannot. |
| `VISIBLE` | All members of ThreatExchange can see the object. _This is the default, if no value is specified._ |

The `privacy_members` field is a comma-delimited list of App IDs of [ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member) or [ThreatPrivacyGroups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/) that are either given or not given access to the data, based on the value in `privacy_type`.

Setting Privacy: Examples
-------------------------

The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which members of ThreatExchange are allowed to see the data.

### Controlling visibility using the UI

### Allowing all members access using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE

### Limiting privacy to a privacy group using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_PRIVACY\_GROUP
&amp;privacy\_members=123456789

### Limiting privacy To select members using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_WHITELIST
&amp;privacy\_members=123456789,9012345678

### Limiting privacy to only your app using the API

POST https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_WHITELIST
&amp;privacy\_members=555

Submitting New Data
===================

Visit the [**descriptors-tab page**](https://developers.facebook.com/docs/threat-exchange/reference/ui/descriptors) to see more things you can do with threat descriptors within the ThreatExchange UI including searching, bulk download, and more.

Creating
--------

Using the Create button you can upload a new descriptor, with tooltips to provide context. Here's an example of submitting a malicious domain using the UI:

Note : If you set a descriptor's privacy to has-whitelist and include no whitelist apps, the owner's app is automatically included. This is a "visible to self" or "storage mode" option.

Creating with templates
-----------------------

Using the Create button is fine for sharing a single threat descriptor -- but what if you have a hundred or a thousand? As we'll see immediately below, bulk-upload from CSV or JSON files solves this problem in a very general way.

But there's a common case that's simpler -- when you don't really need a CSV file. ThreatExchange users often find they're submitting a number of threat descriptors which have all the same metadata except for the indicator value. The **create-with-templates** feature fits the bill.

To use templates, simply proceed as above by selecting the Create button -- then select the .

Since template mode is selected, once you hit OK you'll be taken to a commit screen (the same as for upload from file) where you can make any revisions, if any, then commit.

The same works for the Copy button as for the Create button -- this way you can easily make "more of the same" as your organization has more data to share on a given topic.

Uploading from CSV/JSON
-----------------------

Both CSV and JSON formats are supported.

* See [below for information on column/attribute names](#parameters).
    
* Alternatively, you can simply save any descriptor-query result to CSV and use that as a template (and likewise for JSON).
    

Start by selecting the Bulk Upload button:

Select your file:

If you wish to revise your data before committing you can do so:

If there are errors detected before committing you'll be notified, and you can revise them. (Note that not all possible errors are surfaced here.)

Within the revision dialog you can fix the errors and hit OK to continue:

Once you hit the Confirm Upload button, your new descriptors are saved and their IDs are entered into the search bar. At that point, you can further revise them if you like.

The following screen recording shows the revise-before-upload feature in more detail:

Something Went Wrong

We're having trouble playing this video.

[Learn more](https://www.facebook.com/help/396404120401278/list)

Uploading using the API
-----------------------

You may submit data using the ThreatExchange API via an HTTP POST to the following URL:

* https://graph.facebook.com/v4.0/threat\_descriptors
    

NOTE: The call to /threat\_indicators is deprecated as of v2.4 of the ThreatExchange API. If you attempt to access this endpoint in v2.4+, it will create a threat descriptor and the associated threat indicator behind the scenes.

Example submission of a malicious domain using the API:

https://graph.facebook.com/v4.0/threat\_descriptors?access\_token=555|aSdF123GhK

POST DATA:
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;tags=testingtags
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE

Data returned:

{
"id": "853037291373757",
"success": true
}

Field names for upload
----------------------

Bold parameters are required.

| API Name and Example | UI CSV Name and Example | Description |
| --- | --- | --- |
| **`access_token`**  <br>`555\|aSdF123GhK` | _Not used for the UI_ | The key for authenticating to the API, in the format<br><br>`your-app-id\|your-app-secret`  <br>  <br><br>Please visit the<br><br>[Access Token Tool](https://developers.facebook.com/tools/accesstoken)<br><br>to find values for your app(s). |
| **`description`**  <br>`This%20domain%20was%20hosting%20malware` | **`td_description`**  <br>`This domain was hosting malware` | A short summary of the indicator and threat. |
| **`indicator`**  <br>`evil-domain.biz` | **`td_raw_indicator`**  <br>`evil-domain.biz` | The indicator data being submitted. |
| **`type`**  <br>`URI` | **`td_indicator_type`**  <br>`URI` | The kind of indicator being described. See<br><br>[IndicatorType](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type)<br><br>for the list of allowed values. |
| **`privacy_type`**  <br>`HAS_PRIVACY_GROUP` | **`td_visibility`**  <br>`HAS_PRIVACY_GROUP` | The kind of privacy for the indicator. See<br><br>[PrivacyType](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type)<br><br>for the list of allowed values. |
| `privacy_members`  <br>`1064060413755420,494491891138576` | `td_whitelist_apps`  <br>`1064060413755420,494491891138576`  <br>  <br>`td_privacy_groups`  <br>`438835087026293,468692780520730`  <br>  <br><br>Or, for compatibility, you can use a column name of<br><br>`td_privacy_members`<br><br>for upload if you like. If visibility is HAS\_WHITELIST, we will proceed as if your td\_privacy\_members column were named td\_whitelist\_apps; if visibility is HAS\_PRIVACY\_GROUP, we will proceed as if your td\_privacy\_members column were named td\_privacy\_groups.<br><br>  <br>  <br><br>See [CSV examples](#csv_examples) and [JSON examples below.](#json_examples) | A list of<br><br>[ThreatExchangeMembers](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-member)<br><br>allowed to see the indicator, and only applies when<br><br>`privacy_type`<br><br>is set to<br><br>`HAS_WHITELIST`<br><br>or<br><br>`HAS_PRIVACY_GROUP`<br><br>. Delimiters are comma for the API and semicolon for the UI. |
| **`share_level`**  <br>`AMBER` | **`td_share_level`**  <br>`AMBER` | A designation of how the indicator may be shared based on the<br><br>[US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp%2F&h=AT0-Twuvtto2WjqCfjHt-WNS6E2ck_niJsoaGF5dEJ_x-ejReS131L45xCx5kchrZB_UhU-IgHLief1N-4EYM5fK-JxCU7f-8PNCywXOEP1Soi3oCj_9ilIkRZmN_l22D1RAAl99jM_bn6Hm)<br><br>. See<br><br>[ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type)<br><br>for the list of allowed values. Note: GREEN/WHITE requires VISIBLE, and AMBER/RED requires HAS\_WHITELIST or HAS\_PRIVACY\_GROUP. |
| **`status`**  <br>`MALICIOUS` | **`td_status`**  <br>`MALICIOUS` | Indicates if the indicator is labeled as malicious. See<br><br>[StatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type)<br><br>for the list of allowed values. |
| `tags`  <br>`testing,pwny` | `td_subjective_tags`  <br>`testing;pwny` | API: a comma-separated list of tags you want to publish. UI: a semicolon-separated list of tags you want to publish. This will replace any existing tags.  <br>Tags are not strictly required but do note that they are essential for your collaborators to discover data you contribute. |
| `add_tags`  <br>`pwny,testing` | _Not used for the UI_ | To add tags to an object without overwriting existing tags. |
| `remove_tags`  <br>`pwny,testing` | _Not used for the UI_ | Remove tags associated with an object. |
| `confidence`  <br>`100` | `td_confidence`  <br>`100` | A score for how likely the indicator's<br><br>`status`<br><br>is accurate, ranging from 0 to 100. |
| `expired_on` | `td_expire_time`  <br>`2019-11-07T22:25:00-05:00` | Time the indicator is no longer considered a threat, in ISO 8601 date format. |
| `first_active` | `td_first_active`  <br>`2019-11-07T22:25:00-05:00` | Time when the opinion first became valid. |
| `last_active` | `td_last_active`  <br>`2019-11-07T22:25:00-05:00` | Time when the opinion stopped being valid. |
| `review_status`  <br>`PENDING` | `td_review_status`  <br>`PENDING` | Describes how the indicator was vetted. See<br><br>[ReviewStatusType](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type)<br><br>for the list of allowed values. |
| `severity`  <br>`SEVERE` | `td_severity`  <br>`SEVERE` | A rating of how severe the indicator is when found in an incident. See<br><br>[SeverityType](https://developers.facebook.com/docs/threat-exchange/reference/apis/severity-type)<br><br>for the list of allowed values. |
| N/A | `td_related_ids_for_upload` | For submitting relations in bulk. Please see the<br><br>[Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)<br><br>for more information. |
| N/A | `td_related_triples_for_upload` | For submitting relations in bulk. Please see the<br><br>[Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)<br><br>for more information. |

CSV examples
------------

When you download as CSV, we put whitelist apps and privacy groups in the format `id1:name1;id2:name2`. Tags are always text-only, delimited by semicolons:

`id                 2494923897281868 td_description     This is an example descriptor td_status          UNKNOWN td_confidence      0 td_severity        SEVERE td_share_level     AMBER td_indicator_type  URI td_raw_indicator   https://evilevillabs.com/evil.php td_visibility      HAS_WHITELIST td_creation_time   2019-11-07T22:25:00-05:00 td_update_time     2019-11-07T22:25:01-05:00 td_expire_time td_owner_id        494491891138576 td_owner_name      Media Hash Sharing RF Test td_subjective_tags testing;pwny td_whitelist_apps  1064060413755420:Media Hash Sharing Test;494491891138576:Media Hash Sharing RF Test`
        

When upload from CSV, you may specify whitelist apps and privacy groups in the format `id1;id2` if you prefer:

`td_description     This is an example descriptor td_status          UNKNOWN td_confidence      0 td_severity        SEVERE td_share_level     AMBER td_indicator_type  URI td_raw_indicator   https://evilevillabs.com/evil.php td_visibility      HAS_WHITELIST td_creation_time   2019-11-07T22:25:00-05:00 td_update_time     2019-11-07T22:25:01-05:00 td_expire_time td_owner_id        494491891138576 td_owner_name      Media Hash Sharing RF Test td_subjective_tags testing;pwny td_whitelist_apps  1064060413755420;494491891138576`
        

JSON examples
-------------

When you download as JSON, we put whitelist app, privacy groups, and tags in nested ID/name pairs:

`{   "id": "2699570156799349",   "td_description": "Testing bulk upload",   "td_status": "NON_MALICIOUS",   "td_confidence": 100,   "td_severity": "UNKNOWN",   "td_share_level": "AMBER",   "td_creation_time": 1575824153,   "td_update_time": 1575824154,   "td_expire_time": 0,   "td_indicator_type": "HASH_MD5",   "td_raw_indicator": "e8b19da37825a3056e84c522f05ed0c0",   "td_owner": {     "id": "1064060413755420",     "name": "Media Hash Sharing Test"   },   "td_subjective_tags": [     {       "id": "2055943881194599",       "td_name": "pwny"     },     {       "id": "1977957082312815",       "td_name": "testing"     }   ],   "td_visibility": "HAS_WHITELIST",   "td_whitelist_apps": [     {       "id": "1064060413755420",       "name": "Media Hash Sharing Test"     },     {       "id": "494491891138576",       "name": "Media Hash Sharing RF Test"     }   ],   "td_privacy_groups": [] }`
        

When you upload from JSON, if you prefer, you can write whitelist apps and privacy groups as simply arrays of IDs, and tags as arrays of text:

`{   "td_description": "This is an example descriptor",   "td_status": "UNKNOWN",   "td_confidence": 0,   "td_severity": "SEVERE",   "td_share_level": "AMBER",   "td_creation_time": 1573183500,   "td_update_time": 1573183501,   "td_expire_time": 0,   "td_indicator_type": "URI",   "td_raw_indicator": "https://evilevillabs.com/evil.php",   "td_subjective_tags": ["testing", "pwny"],   "td_visibility": "HAS_WHITELIST",   "td_whitelist_apps": ["1064060413755420", "494491891138576"] }`
        

See also the [Submitting Connections page](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections) for how to do related descriptors at bulk-upload.

Editing existing data
=====================

The ThreatExchange API allows for editing existing [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) objects. As with all Facebook Graph APIs, editing is performed via an HTTP POST request to the object's unique ID URL.

Editing single threat descriptors using the UI
----------------------------------------------

Using any of various search mechanisms, identify a descriptor you own and click the Edit button:

  

Then, fields are editable as in the Create pop-up:

Bulk-editing using the UI
-------------------------

First, perform any descriptor-search, then choose "Bulk edit". All descriptors in the search that are owned by you (if any) will be bulk-editable.

  

Choose "Select all", then "Bulk-revise selected items".

  

At this point you can edit various attributes. Here, we show that the collection being edited has multiple values for Severity; we can set them all to the same value if we like -- say, INFO. To continue the example, let's add a new tag -- `testing-bulk-edit-for-doc` -- to all selected descriptors.

  

In the create-tag popup we can fill out the attributes and then hit OK.

  

Having bulk-edited some attributes, we can OK the bulk-edit popup.

  

We can now continue editing if we like -- perhaps select any particular descriptor and revise it further using the "Revise" button on a given row. (Or we can abandon the edits entirely -- they're still browser-local only, not yet saved to ThreatExchange.) Instead, let's go ahead and save our changes.

  

We now see the committed descriptors along with their IDs.

Cloning and duplicating
-----------------------

Once you've found a threat descriptor, you may wish to publish a modified copy of it. We use the terms "cloning" for making a copy of your own descriptor (perhaps changing the indicator-text, for example) and "duplicating" for making a copy of someone else's (perhaps changing subjective parameters such as your view of the malicious, the first-active-timestamp, etc.). Regardless, though, Clone and Duplicate both create new threat descriptors owned by you.

Here we search for descriptors visible to us with tag `testing`, then select one to clone.

  

The clone popup is simply a create-descriptor popup -- pre-populated with the cloned-from descriptor's attributes. We can edit whatever we like, then hit OK.

  

Once we hit OK we've got a new descriptor owned by us. We can then go on to duplicate it, if we like.

Using the API, option 1
-----------------------

In this example, we are updating the description field of [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) object with ID `3047058802049882`:

curl -s -X POST \\
'https://graph.facebook.com/v4.0/3047058802049882/'\\
'?access\_token=REDACTED'\\
'&description=Updating+description'

Data returned:

{
"success": true
}

Using the API, option 2
-----------------------

You can use the same API call as in [Submitting Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting).

* If you do that -- resubmit data with the same indicator-type and indicator-text, but different values for other fields -- the same threat descriptor will be edited.
    
* It will insist that you pass it all the minimum parameters necessary for creating a new descriptor even if you only want to edit one attribute of an existing descriptor.
    
* Thus, option 1 is preferred if you want to only specify a single attribute to update.

Delete Data
===========

ThreatExchange currently supports deletion for [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors) objects and relationships between [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) objects. Some objects may also be given an expiration time, which will cause data to be deleted automatically within 90 days of the expiration.

You can delete a ThreatDescriptor using the API with a `DELETE HTTP` request:

DELETE https://graph.facebook.com/v2.11/<object\_id>

After a subjective ThreatDescriptor is deleted, the objective ThreatIndicator may still exist.

To delete a relationship between ThreatIndicators using the API:

DELETE https://graph.facebook.com/v2.11/<object\_id>/related?related\_id=<object\_id\_2>

We do not support deletes for Tags.

ThreatExchange re-sharing controls
==================================

All submissions to the ThreatExchange API allow for defining how the data can be re-shared by its recipients. The level of re-sharing is applied via the `share_level` attribute.

The desired re-share setting on an object can be specified at the time of a create or edit submission to the API. While re-sharing settings can be changed retroactively, those changes will not be pushed as updates to members that have already accessed the data.

Re-sharing options via `share_level`
------------------------------------

The re-sharing definitions adopted by ThreatExchange are derived from those definied in the [US-CERT's Traffic Light Protocol](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.us-cert.gov%2Ftlp&h=AT1MFs82ua9iPdn4man8ytXuwMK1QSmAY-lVuNHUIOORj5XHfJyjD3eYsCKRLJgw5d7uLGVE4E6X8BPk6OFaOGx0gvvGiBj2M67n9WUh2r48lmbh_rdwx9S3BahA_Txxd_kAhUYKZom8zGrp). They have been adapted to accomodate the realities of re-sharing within large corporations with complex subsidiary relationships.

The exact definitions of the permitted values in the `share_level` attribute are defined in the [ShareLevelType](https://developers.facebook.com/docs/threat-exchange/reference/apis/share-level-type/).

Setting re-sharing: examples
----------------------------

The following is an examples are submissions of a new malicious domain to ThreatExchange. In each example, we define which re-sharing level is permitted.

### Specifying re-sharing using the UI

### Allowing re-sharing to anyone, including public channels, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE
&amp;share\_level=WHITE

### Limiting re-sharing to established, non-public channels, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=VISIBLE
&amp;share\_level=GREEN

### Limiting re-sharing to select members and their related entities with a need to know, using the API

POST https://graph.facebook.com/v2.8/threat\_indicators?access\_token=555|aSdF123GhK

indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;threat\_type=MALICIOUS\_DOMAIN
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy\_type=HAS\_WHITELIST
&amp;privacy\_members=555
&amp;share\_level=AMBER

React to Existing Data
======================

You can express a structured opinion on data you see on ThreatExchange by **reacting** to that data. This is a fully optional feature that can be used to provide more context or transparency about your ThreatExchange usage.

.

In general, `SAW_THIS_TOO`, `NON_MALICIOUS`, and `DISAGREE_WITH_TAGS` have well-undestood meaning, and are valuable contributions to any dataset. The rest are sometimes used as part of PrivacyGroup-specific conventions, or to provide a high level of transparency into your own usage of ThreatExchange data.

Values
------

As of Jan 2023:

| Name | Usage Category | Description |
| --- | --- | --- |
| `SAW_THIS_TOO` | Ingestion status. | The object has been observed on-platform by the reactor. Using this reaction can help track platform spread. |
| `NON_MALICIOUS` | Feedback after review. | The object has been reviewed and found to be non-malicious. This is equivalent to uploading the same object but with the [`StatusType`](https://developers.facebook.com/docs/threat-exchange/reference/apis/status-type) of `NON_MALICIOUS`. A reaction is often preferable, as it will not leave extra objects in ThreatExchange if the original object is later retracted. |
| `DISAGREE_WITH_TAGS` | Feedback after review. | The object has been reviewed and the reactor would have tagged it differently. Many PrivacyGroups use tags in order to categorize data by convention. `DISAGREE_WITH_TAGS` without an upload by the same reactor with their preference in tagging is equivalent to a `NON_MALICIOUS` report. If the owner of the object changes the tags, this reaction will automatically be removed. |
| `HELPFUL` | Ad-hoc feedback. | The object helped lead to the discovery of harmful content. |
| `NOT_HELPFUL` | Ad-hoc feedback. | The object seems to lead to non-malicious content. |
| `OUTDATED` | Ad-hoc feedback. | The object is outdated or can no longer be evaluated. |
| `WANT_MORE_INFO` | Request for information. | More information requested about this object. |
| `INGESTED` | Ingestion status. | The object is outdated or can no longer be evaluated. |
| `ALREADY_KNOWN` | Ingestion status. | The object is equivalent to information already known to the reactor. |
| `IN_REVIEW` | Ingestion status. | The object is being reviewed, or the object has been matched to content on platform that is being reviewed. |
| `REVIEWED` | Ingestion status. | The object has been reviewed, or the object has been matched to content on platform thathas been reviewed. |

React Using the UI
------------------

2. Search for threat descriptors using [any method of your choice](https://developers.facebook.com/docs/threat-exchange/reference/ui/descriptors#searching); for example, using the tag `testing-reaction-editing`.

5. You can react to threat descriptors owned by other apps (the **View** button), not to those owned by your app (**Edit** button).

  

10. Click **Add Reaction**.

  

15. Select your reactions and click **Save**.

  

20. Dismiss the popup.

  

25. The next image shows being logged in as the owner app. Click **Edit** to view details.

  

For the owner app the reactions are read-only, formatted as a table.

Bulk React Using the UI
-----------------------

You can update reactions for several descriptors at once.

2. Do any search; a search by tag.

  

The **Bulk react** button applies to all checkboxed rows, where your app doesn't own.

  

10. Select reactions to add to all rows or remove from all rows.

  

15. Click **OK** to commit:

  

20. Select **View** on any of the affected rows, where you can view the reaction.

React Using the API
-------------------

To express an opinion about descriptor 952030561511282 using the API, append your access token and issue a **POST** to:

    https://graph.facebook.com/v4.0/952030561511282?reactions=HELPFUL,SAW_THIS_TOO
    
    

To retrieve the reactions of everyone else, append your access token and issue a `GET` to.

    https://graph.facebook.com/v4.0/952030561511282?fields=id,my_reactions,reactions
    
    

The `my_reactions` field shows your own reactions, and the `reactions` field is a map from the possible [ReactionType](https://developers.facebook.com/docs/threat-exchange/reference/apis/reaction-type) to the apps that reacted with that type. If there are no reactions, the field is empty.

Share Feedback
--------------

_Reactions_ are a growing feature. To provide feedback about reactions, contact threatexchange@fb.com, or use the bug nub in the TEUI.

Submit Connections Between Data
===============================

ThreatExchange supports creating connections (also known as **edges** or **relations**) between [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) objects to express relationships. Examples of when this can be useful are for describing URL redirect chains or domain-to-IP-address relationships.

Use the UI
----------

When you connect one descriptor to another, you must own one or the other.

2. Within the **View**/**Edit** popup for a given descriptor, you need the IDs of the descriptors to connect to. Start with any search results. In this case, `testing-relation-editing`.
3. Connect the first one to the next 2.

  

8. Select the IDs of the next 2 descriptors and click **Copy IDs to clipboard**.

  

13. Click **View**/**Edit** on the first descriptor, paste the IDs, and then click **Add Relation** > **OK**.

  

The results are saved as in the following example.

Use the UI for Bulk Relations
-----------------------------

Just as in the [Use the UI](#using-ui) topic, you can assume that multiple descriptors are related to another one.

2. In the next example, do a query for a particular tag (can be any set of descriptors).
3. Click **Bulk relate**.

  

8. Supply the ID of the related-to indicator and click **OK**.

Use the UI for Bulk Upload
--------------------------

These are optional columns you can use to bulk-relate (see also [Submit Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting):

* The descriptors you want to relate your new one to must already exist.
* You can specify the relate-to descriptors by ID using the `td_related_ids_for_upload` column.
* Alternatively, you can specify the related-to descriptors using the `td_related_triples_for_upload` column. Provide the owner-app ID, indicator type, and indicator text, which will uniquely identify the linked-to descriptors.

#### CSV Example (written vertically for convenience):

`td_description                Testing bulk upload td_status                     NON_MALICIOUS td_confidence                 100 td_severity                   INFO td_share_level                AMBER td_indicator_type             HASH_MD5 td_raw_indicator              e8b19da37825a3056e84c522f05eb000 td_visibility                 HAS_WHITELIST td_subjective_tags            testing td_whitelist_apps             494491891138576:Media Hash Sharing RF Test td_privacy_groups              td_review_status              REVIEWED_MANUALLY td_related_ids_for_upload     2515798535123892,2376386079125415 td_related_triples_for_upload   td_description                Testing bulk upload td_status                     NON_MALICIOUS td_confidence                 100 td_severity                   INFO td_share_level                AMBER td_indicator_type             HASH_MD5 td_raw_indicator              e8b19da37825a3056e84c522f05eb001 td_visibility                 HAS_WHITELIST td_subjective_tags            pwny;testing td_whitelist_apps             494491891138576:Media Hash Sharing RF Test td_privacy_groups              td_review_status              REVIEWED_MANUALLY td_related_ids_for_upload      td_related_triples_for_upload 494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb000,494491891138576:HASH_MD5:e8b19da37825a3056e84c522f05eb002`

#### JSON Example:

`[   {     "td_description": "Testing bulk upload/relate",     "td_status": "NON_MALICIOUS",     "td_confidence": 100,     "td_severity": "INFO",     "td_share_level": "AMBER",     "td_indicator_type": "HASH_MD5",     "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000",     "td_visibility": "HAS_WHITELIST",     "td_subjective_tags": ["testing"],     "td_whitelist_apps": [       {         "id": "494491891138576",         "name": "Media Hash Sharing RF Test"       }     ],     "td_privacy_groups": [],     "td_review_status": "REVIEWED_MANUALLY",     "td_related_ids_for_upload": ["2515798535123892","2376386079125415"]   },   {     "td_description": "Testing bulk upload/relate",     "td_status": "NON_MALICIOUS",     "td_confidence": 100,     "td_severity": "INFO",     "td_share_level": "AMBER",     "td_indicator_type": "HASH_MD5",     "td_raw_indicator": "e8b19da37825a3056e84c522f05eb001",     "td_visibility": "HAS_WHITELIST",     "td_subjective_tags": ["pwny", "testing"],     "td_whitelist_apps": [       {         "id": "494491891138576",         "name": "Media Hash Sharing RF Test"       }     ],     "td_privacy_groups": [],     "td_review_status": "REVIEWED_MANUALLY",     "td_related_triples_for_upload": [       {         "owner_app_id": "494491891138576",         "td_indicator_type": "HASH_MD5",         "td_raw_indicator": "e8b19da37825a3056e84c522f05eb000"       },       {         "owner_app_id": "494491891138576",         "td_indicator_type": "HASH_MD5",         "td_raw_indicator": "e8b19da37825a3056e84c522f05eb002"       }     ]   } ]`
      

Use the API
-----------

Using the API, you can create connections via an `HTTP POST` request to the `/related` URI for a specific object:

https://graph.facebook.com/v2.8/<object\_id>/related

In this example, create a connection between the `facebook.com` domain object (`788497497903212`) and the 173.252.120.6 IP address object (`1061383593887032`), which `facebook.com` can resolve to via DNS.

https://graph.facebook.com/v2.8/788497497903212/related

POST DATA:
related\_id=1061383593887032
&amp;access\_token=<access\_token>

Data returned:

{
"success": true
}

Partner Integrations
====================

To make data shared on ThreatExchange usable and actionable in existing workflows more easily, several third parties have built direct integrations with the ThreatExchange platform.

### Bit9 + CarbonBlack

* [CarbonBlack Integration Documentation](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.carbonblack.com%2Fsolutions%2Fecosystem%2Ffacebook-threatexchange%2F&h=AT1EoKjxgRXqQxsOkcHv5q2jUcI8Fa3ulJpdiijjpNtATWJuT1mvlty0UPXO27EGPzkSEHWhaidUjtcIWyy15aO4rrINpRFL0Oy3LTRY7jxDu3L2Qb10UNAerKzGQfcw1Pb0flH61RmxjX6L)
    
* [CarbonBlack Connector on GitHub](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fcarbonblack%2Fcb-threatexchange-connector&h=AT12Ddy9TwO8zpxDQIKdSuNTyAgvG_wtoHa_ZEfuu2BrPh5leWfuA51MPta3v_QG_UM5aEm3F6Xk8M56BEWNqSB87h_PjqzssZf-8lW60n4Q7y69IaCA0LL9JhjmCsvJ3fctBLiw9VPydcuV)
    

### RiskIQ's PassiveTotal

* [RiskIQ Integration Announcement](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.riskiq.com%2Fresources%2Fpress-releases%2Friskiq-makes-facebook-threatexchange-data-accessible-within-passivetotal&h=AT2OnZz5L2OBT9k2XY_-UBSDreAzduoFxF1In8Me43eLHjZFH0v4p4VE7q8GodKbsSWOakoDl7ZwPbmXw4trMSu8psqaXZD56_9eCSZTcSaEznJ4CEMOieZt5Z0MaoLun19XVHOgB2P_gziM)
    

### Demisto

* [Demisto Partner Integrations](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.demisto.com%2Fpartners%2F&h=AT3W6BGiq06D3MMMwkw5S3HYvpJpOJ--YUA34RWksEiz3esFgpPsRGEYh0c-U3GxLj_4PnbILsQmd-MCcxSEOXcNel-LsudWcczE6CClOGbts_MFmai5gMROaC0pKeSjTLWSaDXimZUCv5fW)
    

### ThreatStream

* [ThreatStream 'Facebook ThreatExchange' Trusted Circle](https://l.facebook.com/l.php?u=https%3A%2F%2Fui.threatstream.com%2Fsearch%3Ftrustedcircles%3D10023&h=AT3cKGCMJUifUrZvyplBdvbykCq_l3nLuPwdR3dNApVwJbLRorH8QmgTQoh18c75AenACCUkSiqJ3w6aT0nI6k-Jus50QT2c-4-382r2naDpCCCGIEk2HbiFFmzIE4Wb0bxvmJ_Nf8eb_CYQ)
    

### Splunk add-on

* [Splunk Add-On documentation](https://l.facebook.com/l.php?u=https%3A%2F%2Fdocs.splunk.com%2FDocumentation%2FES%2F4.1.1%2FAddons%2FFBThreatExchange&h=AT2i3UohqnebnJxCU4hU1iQ3N5OIJID9J6GEvYpC17EM6TNV6-2za9MV_NOLKi6hYnMo5oOoWO2SipN_exuE93tmfKSNbEkUb_3j5v12n3iEjzq2JcvuLFKbXsM1KJmaL1_zmyj38KmYsU0tiKWmB8QFts6fkw)