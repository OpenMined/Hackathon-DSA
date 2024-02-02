
React to Data - ThreatExchange - Documentation - Meta for Developers












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
React to Existing Data
======================

You can express a structured opinion on data you see on ThreatExchange by **reacting** to that data. This is a fully optional feature that can be used to provide more context or transparency about your ThreatExchange usage.

.


In general, `SAW_THIS_TOO`, `NON_MALICIOUS`, and `DISAGREE_WITH_TAGS` have well-undestood meaning, and are valuable contributions to any dataset. The rest are sometimes used as part of PrivacyGroup-specific conventions, or to provide a high level of transparency into your own usage of ThreatExchange data.

Values
------

As of Jan 2023:



 
 Name
  | 
 Usage Category
  | 
 Description
  || `SAW_THIS_TOO` | Ingestion status. | The object has been observed on-platform by the reactor. Using this reaction can help track platform spread. |
| `NON_MALICIOUS` | Feedback after review. | The object has been reviewed and found to be non-malicious. This is equivalent to uploading the same object but with the `StatusType` of `NON_MALICIOUS`. A reaction is often preferable, as it will not leave extra objects in ThreatExchange if the original object is later retracted. |
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


2. Search for threat descriptors using any method of your choice; for example, using the tag `testing-reaction-editing`.
4. You can react to threat descriptors owned by other apps (the **View** button), not to those owned by your app (**Edit** button).
  
8. Click **Add Reaction**.
  
12. Select your reactions and click **Save**.
  
16. Dismiss the popup.
  
20. The next image shows being logged in as the owner app. Click **Edit** to view details.
  
For the owner app the reactions are read-only, formatted as a table.

Bulk React Using the UI
-----------------------


You can update reactions for several descriptors at once.

2. Do any search; a search by tag.
  
The **Bulk react** button applies to all checkboxed rows, where your app doesn't own.

  
9. Select reactions to add to all rows or remove from all rows.
  
13. Click **OK** to commit:
  
17. Select **View** on any of the affected rows, where you can view the reaction.
React Using the API
-------------------


To express an opinion about descriptor 952030561511282 using the API, append your access token and issue a **POST** to:


```
  
https://graph.facebook.com/v4.0/952030561511282?reactions=HELPFUL,SAW_THIS_TOO


```

To retrieve the reactions of everyone else, append your access token and issue a `GET` to.


```
  
https://graph.facebook.com/v4.0/952030561511282?fields=id,my_reactions,reactions


```

The `my_reactions` field shows your own reactions, and the `reactions` field is a map from the possible ReactionType to the apps that reacted with that type. If there are no reactions, the field is empty.


Share Feedback
--------------


*Reactions* are a growing feature. To provide feedback about reactions, contact threatexchange@fb.com, or use the bug nub in the TEUI.



































 
