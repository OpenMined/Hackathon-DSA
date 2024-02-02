Best Practices - ThreatExchange - Documentation - Meta for Developers

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
Best Practices for Using ThreatExchange
=======================================
This guide explains some ways to use ThreatExchange that will help improve throughput and usage.
Downloading Data
----------------

When you get access to new data in ThreatExchange (such as by being added to a PrivacyGroup), we recommend you get a sample or complete copy of the data to evaluate it.

You can use these APIs and UI:

* ThreatExchange UI - sample data
* /threat\_descriptors API - samples data
* /threat\_updates API - Recommended API for complete copy
* /<TAG\_ID>/tagged\_objects API - Okay for a 1-time complete copy

Only some of them should be used for automated integration into your own systems, and the others should be used only for sampled evaluation and testing.

### Sample CSVs from the UI

Some privacy groups have a feature where samples of indicators can be downloaded from the UI, which is the fastest way to evaluate potential data. Learn more at ThreatExchange UI.
### Sampling from /threat\_descriptors API

The /threat\_descriptors API allows you to do complex searches on ThreatDescriptors. This can be useful to generate your own narrow samples, but the API is not guaranteed to be contain all data that matches the filters. 
### Tailing /threat\_updates API

**Recommended**—The /threat\_updates API allows you to exactly reproduce a ThreatPrivacyGroup's contents. It also allows you to get deletion events as long as you poll within 30 days of the object being deleted. Tailing /threat\_updates gives you the lowest latency, complete data, and is the only API that notifies of deletes.
Not all PrivacyGroups have this API enabled, reach out to threatexchange@meta.com for questions about enabling it.
### /<TAG\_ID>/tagged\_objects API

 The /<TAG\_ID>/tagged\_objects API allows you to reliably download all ThreatDescriptors tagged with those tags. Because most data is tagged, this is a reliable way to get data. However, you must do client-side filtering to remove unwanted data, but with the same tags (for example, in the wrong privacy group, wrong type, etc). Additionally, because you don't learn of deletions or updates, you must start over from `tagged_since=0` at some interval (for example, 30 days) in order get updates and discard data that has been deleted.
Tag Your Data
-------------

By tagging your data, it makes it easier for yourself and others to find the indicators they care most about. For example, by tagging descriptors with `evil`, this allows others to filter descriptors searches by data with that tag. Another option is that you can then search the `threat_tags` endpoint by that tag and see all the tagged objects visible to you. The tagging endpoint also supports partial matches on tags, so a query for `evil` will surface any tags visible to you which are like `evil*`.
Be Descriptive with Your Tags
-----------------------------

ThreatTags (also known as "subjective tags") contain metadata fields describing what they are. If you create the tag `foo`, others can inspect the metadata to see what means or why the data was tagged. But it's helpful to be more descriptive instead; for example, `campaign_zeusbotnet` or `malicious_ssl_cert`.
Consider Privacy Rules
----------------------

ThreatTags are visible based on the PrivacyType of the tagged data. For example, if the tag `public_tag` is on ANY descriptor that is publically visible (privacy type of VISIBLE), then the tag is visible to all members. Conversely, if the tag `nonpublic_tag` is ONLY on tagged objects shared to specific members (privacy types `HAS\_WHITELIST` or `HAS\_PRIVACY\_GROUP`), then the tag is only visible to those members. Tag your data accordingly. Learn more about PrivacyType tag.
For more uses cases with ThreatTags, see the ThreatTag reference.
Use Batch Requests for Improved Throughput
------------------------------------------

Batch requests allow you to make multiple requests to the Graph API using a single HTTP call. For more information on Graph API Batch Requests, review the following:
* Making multiple API requests
* Batch requests documentation
You can also query for multiple objects by ID using the following syntax:

```
https://graph.facebook.com/v2.8/?ids=[id1,id2]&amp;access_token=<access_token>
```
If you need to query for a specific field:

```
https://graph.facebook.com/v2.8/?ids=[id1,id2]&amp;fields=field1,field2&amp;access_token=<access_token>
```
Include Nested Fields and Objects in Result Data
------------------------------------------------

It can sometimes be more efficient to include various nested fields or related objects in your search results. The following syntax shows how, for the `facebook.com` indicator object, to pull all of its descriptors without issuing additional API calls:

```
https://graph.facebook.com/v2.8/788497497903212?fields=descriptors{owner,description,status,share_level},indicator,type&amp;access_token=<access_token>
RESULT:
{
  "descriptors": {
    "data": [
      {
        "owner": {
          "id": "820763734618599",
          "name": "Facebook Administrator"
        },
        "description": "Facebook",
        "status": "NON_MALICIOUS",
        "share_level": "GREEN",
        "id": "834469179976904"
      },
      {
        "owner": {
          "id": "588498724619612",
          "name": "Facebook CERT ThreatExchange"
        },
        "description": "Non malicious",
        "status": "NON_MALICIOUS",
        "share_level": "GREEN",
        "id": "1202389109786630"
      }
    ],
    "paging": {
      "cursors": {
        "before": "ODM0NDY5MTc5OTc2OTA0",
        "after": "MTIwMjM4OTEwOTc4NjYzMAZDZD"
      }
    }
  },
  "indicator": "facebook.com",
  "type": "DOMAIN",
  "id": "788497497903212"
}
```