
Submitting Data - ThreatExchange - Documentation - Meta for Developers














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
Submitting New Data
===================

Visit the **descriptors-tab page** to see more things you can do with threat descriptors within the ThreatExchange UI including searching, bulk download, and more.

Creating
--------

Using the Create button you can upload a new descriptor, with tooltips to provide context. Here's an example of submitting a malicious domain using the UI:

Note : If you set a descriptor's privacy to has-whitelist and include no whitelist apps,
 the owner's app is automatically included. This is a "visible to self" or "storage mode" 
 option.

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

* See below for information on column/attribute names.
* Alternatively, you can simply save any descriptor-query result to CSV and use that as a template (and likewise for JSON).

Start by selecting the Bulk Upload button:

Select your file:

If you wish to revise your data before committing you can do so:

If there are errors detected before committing you'll be notified, and you can revise them. (Note that not all possible errors are surfaced here.)

Within the revision dialog you can fix the errors and hit OK to continue:

Once you hit the Confirm Upload button, your new descriptors are saved and their IDs are entered into the search bar. At that point, you can further revise them if you like.

The following screen recording shows the revise-before-upload feature in more detail:

Something Went WrongWe're having trouble playing this video.Learn moreUploading using the API
-----------------------

You may submit data using the ThreatExchange API via an HTTP POST to the following URL:

* https://graph.facebook.com/v4.0/threat\_descriptors

NOTE: The call to /threat\_indicators is deprecated as of v2.4 of the ThreatExchange API. If you attempt to access this endpoint in v2.4+, it will create a threat descriptor and the associated threat indicator behind the scenes.

Example submission of a malicious domain using the API:


```
https://graph.facebook.com/v4.0/threat_descriptors?access_token=555|aSdF123GhK

POST DATA:
indicator=evil-domain.biz
&amp;type=DOMAIN
&amp;tags=testingtags
&amp;status=MALICIOUS
&amp;description=This%20domain%20was%20hosting%20malware
&amp;privacy_type=VISIBLE
```
Data returned:


```
{
"id": "853037291373757",
"success": true
}
```
Field names for upload
----------------------

Bold parameters are required.



 API Name and Example | UI CSV Name and Example | Description || **`access_token`**`555|aSdF123GhK` | *Not used for the UI* | The key for authenticating to the API, in the format
`your-app-id|your-app-secret`Please visit the
Access Token Toolto find values for your app(s). |
| **`description`**`This%20domain%20was%20hosting%20malware` | **`td_description`**`This domain was hosting malware` | A short summary of the indicator and threat. |
| **`indicator`**`evil-domain.biz` | **`td_raw_indicator`**`evil-domain.biz` | The indicator data being submitted. |
| **`type`**`URI` | **`td_indicator_type`**`URI` | The kind of indicator being described. See
IndicatorTypefor the list of allowed values. |
| **`privacy_type`**`HAS_PRIVACY_GROUP` | **`td_visibility`**`HAS_PRIVACY_GROUP` | The kind of privacy for the indicator. See
PrivacyTypefor the list of allowed values. |
| `privacy_members``1064060413755420,494491891138576` | `td_whitelist_apps``1064060413755420,494491891138576``td_privacy_groups``438835087026293,468692780520730`Or, for compatibility, you can use a column name of
`td_privacy_members`for upload if you like. If visibility is HAS\_WHITELIST, we will proceed as if your td\_privacy\_members column were named td\_whitelist\_apps; if visibility is HAS\_PRIVACY\_GROUP, we will proceed as if your td\_privacy\_members column were named td\_privacy\_groups.
See CSV examples and JSON examples below. | A list of
ThreatExchangeMembersallowed to see the indicator, and only applies when
`privacy_type`is set to
`HAS_WHITELIST`or
`HAS_PRIVACY_GROUP`. Delimiters are comma for the API and semicolon for the UI. |
| **`share_level`**`AMBER` | **`td_share_level`**`AMBER` | A designation of how the indicator may be shared based on the
US-CERT's Traffic Light Protocol. See
ShareLevelTypefor the list of allowed values. Note: GREEN/WHITE requires VISIBLE, and AMBER/RED requires HAS\_WHITELIST or HAS\_PRIVACY\_GROUP. |
| **`status`**`MALICIOUS` | **`td_status`**`MALICIOUS` | Indicates if the indicator is labeled as malicious. See
StatusTypefor the list of allowed values. |
| `tags``testing,pwny` | `td_subjective_tags``testing;pwny` | API: a comma-separated list of tags you want to publish. 
UI: a semicolon-separated list of tags you want to publish.
This will replace any existing tags.
Tags are not strictly required but do note that they are essential for your collaborators to discover data you contribute. |
| `add_tags``pwny,testing` | *Not used for the UI* | To add tags to an object without overwriting existing tags. |
| `remove_tags``pwny,testing` | *Not used for the UI* | Remove tags associated with an object. |
| `confidence``100` | `td_confidence``100` | A score for how likely the indicator's
`status`is accurate, ranging from 0 to 100. |
| `expired_on` | `td_expire_time``2019-11-07T22:25:00-05:00` | Time the indicator is no longer considered a threat, in ISO 8601 date format. |
| `first_active` | `td_first_active``2019-11-07T22:25:00-05:00` | Time when the opinion first became valid. |
| `last_active` | `td_last_active``2019-11-07T22:25:00-05:00` | Time when the opinion stopped being valid. |
| `review_status``PENDING` | `td_review_status``PENDING` | Describes how the indicator was vetted. See
ReviewStatusTypefor the list of allowed values. |
| `severity``SEVERE` | `td_severity``SEVERE` | A rating of how severe the indicator is when found in an incident. See
SeverityTypefor the list of allowed values. |
| N/A | `td_related_ids_for_upload` | For submitting relations in bulk. Please see the
Submitting Connections pagefor more information. |
| N/A | `td_related_triples_for_upload` | For submitting relations in bulk. Please see the
Submitting Connections pagefor more information. |

CSV examples
------------

When you download as CSV, we put whitelist apps and privacy groups in the format `id1:name1;id2:name2`. Tags are always text-only, delimited by semicolons:

````

id                 2494923897281868
td_description     This is an example descriptor
td_status          UNKNOWN
td_confidence      0
td_severity        SEVERE
td_share_level     AMBER
td_indicator_type  URI
td_raw_indicator   https://evilevillabs.com/evil.php
td_visibility      HAS_WHITELIST
td_creation_time   2019-11-07T22:25:00-05:00
td_update_time     2019-11-07T22:25:01-05:00
td_expire_time
td_owner_id        494491891138576
td_owner_name      Media Hash Sharing RF Test
td_subjective_tags testing;pwny
td_whitelist_apps  1064060413755420:Media Hash Sharing Test;494491891138576:Media Hash Sharing RF Test
        
````When upload from CSV, you may specify whitelist apps and privacy groups in the format `id1;id2` if you prefer:

````

td_description     This is an example descriptor
td_status          UNKNOWN
td_confidence      0
td_severity        SEVERE
td_share_level     AMBER
td_indicator_type  URI
td_raw_indicator   https://evilevillabs.com/evil.php
td_visibility      HAS_WHITELIST
td_creation_time   2019-11-07T22:25:00-05:00
td_update_time     2019-11-07T22:25:01-05:00
td_expire_time
td_owner_id        494491891138576
td_owner_name      Media Hash Sharing RF Test
td_subjective_tags testing;pwny
td_whitelist_apps  1064060413755420;494491891138576
        
````JSON examples
-------------

When you download as JSON, we put whitelist app, privacy groups, and tags in nested ID/name pairs:

````

{
  "id": "2699570156799349",
  "td_description": "Testing bulk upload",
  "td_status": "NON_MALICIOUS",
  "td_confidence": 100,
  "td_severity": "UNKNOWN",
  "td_share_level": "AMBER",
  "td_creation_time": 1575824153,
  "td_update_time": 1575824154,
  "td_expire_time": 0,
  "td_indicator_type": "HASH_MD5",
  "td_raw_indicator": "e8b19da37825a3056e84c522f05ed0c0",
  "td_owner": {
    "id": "1064060413755420",
    "name": "Media Hash Sharing Test"
  },
  "td_subjective_tags": [
    {
      "id": "2055943881194599",
      "td_name": "pwny"
    },
    {
      "id": "1977957082312815",
      "td_name": "testing"
    }
  ],
  "td_visibility": "HAS_WHITELIST",
  "td_whitelist_apps": [
    {
      "id": "1064060413755420",
      "name": "Media Hash Sharing Test"
    },
    {
      "id": "494491891138576",
      "name": "Media Hash Sharing RF Test"
    }
  ],
  "td_privacy_groups": []
}
        
````When you upload from JSON, if you prefer, you can write whitelist apps and privacy groups as simply arrays of IDs, and tags as arrays of text:

````

{
  "td_description": "This is an example descriptor",
  "td_status": "UNKNOWN",
  "td_confidence": 0,
  "td_severity": "SEVERE",
  "td_share_level": "AMBER",
  "td_creation_time": 1573183500,
  "td_update_time": 1573183501,
  "td_expire_time": 0,
  "td_indicator_type": "URI",
  "td_raw_indicator": "https://evilevillabs.com/evil.php",
  "td_subjective_tags": ["testing", "pwny"],
  "td_visibility": "HAS_WHITELIST",
  "td_whitelist_apps": ["1064060413755420", "494491891138576"]
}
        
````See also the Submitting Connections page for how to do related descriptors at bulk-upload.








































 
