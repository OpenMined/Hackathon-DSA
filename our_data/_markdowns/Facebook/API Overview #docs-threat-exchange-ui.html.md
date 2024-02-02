UI Overview - ThreatExchange - Documentation - Meta for Developers

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
ThreatExchange UI Overview
==========================

This guide describes the most basic subset of what you can do with the ThreatExchange APIs. See the ThreatExchange API Reference for a comprehensive list of the ThreatExchange APIs and the related endpoints.

ThreatExchange UI Use Cases
---------------------------

* People at various organizations want to share information about **threats**: malicious URLs, harmful content hashes, malware signatures, and so on.
* A **threat indicator** is the **objective part**: a file hash, a URL, and so on, with a type (MD5, SHA1, URL, and so on).
* A **threat descriptor** contains an indicator and the **subjective parts**: how malicious a team thinks it is, when they first saw it, and so on.
* Meta privacy revolves around **user IDs,** ThreatExchange revolves around **app IDs**. For example, app ID 1064060413755420 is Media Hash Sharing Test. These are generally of the form *Team T at company C*.
* When people share threat data, they can specify who they want to see each datum. This is referred to as a **visibility** or **privacy type**.

	+ *Visible/public* means all ThreatExchange members can see it.
	+ Or, for each datum the members can create an app-whitelist of specific teams at specific companies.
	+ Or, for each datum the members can specify a privacy-group that is simply a predefined list of app IDs.
* People can **tag** their descriptors. These are tags in any other tool, except that ThreatExchange tags have their own metadata, including the subjective parts that descriptors have, and they also have their own visiblity (public/app-whitelist/privacy-group).
* There's more about threat descriptors (review status and others) and other types of data shareable on ThreatExchange. For the purpose of this walkthrough, we're focused on indicators, descriptors, visibility, and tags.
Find the UI
-----------

Navigate to https://developers.facebook.com/apps and select your app:

Then, find the ThreatExchange product within the navbar on the left:
Add Team Members
----------------

1. Navigate to https://developers.facebook.com/apps and select your app.
2. Select **Roles** > **Roles**.
3. Add teammate roles as **Administrators** or **Developers**.
 **Note**: Do not add teammates as **Test Users** or **Analytics Users**. These roles have no meaning for ThreatExchange apps.
4. If your organization has a ThreatExchange app ID, but the assigned administrators/developers have since left your organization, please contact us at **threatexchange@meta.com** so that we can reset an admin to be a current employee of your organization. From there, you'll be able to self-service add everyone else in your organization.
Search Data Using the UI
------------------------

A variety of search options are supported.

Search for all malicious URLs uploaded in the last week:
Publish Data Using the UI
-------------------------

See the Submit Data page for examples.
Feedback
--------

Contact **threatexchange@meta.com** with any and all feedback on how we can better enable your success in using ThreatExchange.
You can also use the bugnub to report issues:

Learn more about the UI Reference.