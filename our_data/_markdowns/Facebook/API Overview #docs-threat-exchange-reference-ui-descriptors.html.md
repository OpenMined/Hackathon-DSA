Descriptors Tab - ThreatExchange - Documentation - Meta for Developers

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
ThreatExchange UI Descriptors Tab
=================================
Searching
---------
You have multiple ways to search for ThreatDescriptors (and more to come -- see status here):
Search results are rendered as a table. You can view (or clone) ones you do not own, or edit ones you do own:
Details are shown in a popup -- here is a descriptor owned by another app:
Broadening your searches
------------------------
Given search results, you may wish to fan out to similar results. In this example, let's start with sample data. 

From there, we can find other descriptors with the same indicator (hash):

We can also find other descriptors which have been related to these (see Submitting Connections):

Note that we can poke the fanout buttons multiple times to traverse deeper depths of connection.
Saved searches
--------------
Given any search, simply poke the "Copy search URL to clipboard" button.

Then you can paste the URL into a message to share with coworkers, or what have you. Additionally, you can paste the URL into the browser bar and bookmark it:

You can even make a bookmark folder for your favorite searches:
Editing
-------
When you click Edit on a descriptor your app owns, you are able to mutate all editable attributes, with tooltips to provide context. (ID, indicator text, and indicator type are immutable after a particular descriptor is created.) Note: reactions and connections are not exposed yet in the UI -- see status here.
Downloading as CSV/JSON
-----------------------
You can download query results as CSV or JSON:
If you like, you can edit the CSV/JSON outside of the ThreatExchange UI and then re-upload the modified file to the ThreatExchange UI as one way of updating your data.
Creating
--------
Using the Create button you can upload a new descriptor, with tooltips to provide context:
Note : If you set a descriptor's privacy to has-whitelist and include no whitelist apps, the owner's app is automatically included. This is a "visible to self" or "storage mode" option.
Uploading from CSV/JSON
-----------------------
Please see the Submitting Data page for file formats, examples, and more.