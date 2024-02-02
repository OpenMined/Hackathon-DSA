
Editing Existing Data - ThreatExchange - Documentation - Meta for Developers











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
Editing existing data
=====================

The ThreatExchange API allows for editing existing ThreatIndicator objects. As with all Facebook Graph APIs, editing is performed via an HTTP POST request to the object's unique ID URL.

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

In this example, we are updating the description field of ThreatDescriptor object with ID `3047058802049882`:


```
curl -s -X POST \
'https://graph.facebook.com/v4.0/3047058802049882/'\
'?access_token=REDACTED'\
'&description=Updating+description'
```
Data returned:


```
{
"success": true
}
```
Using the API, option 2
-----------------------

You can use the same API call as in Submitting Data.

* If you do that -- resubmit data with the same indicator-type and indicator-text, but different values for other fields -- the same threat descriptor will be edited.
* It will insist that you pass it all the minimum parameters necessary for creating a new descriptor even if you only want to edit one attribute of an existing descriptor.
* Thus, option 1 is preferred if you want to only specify a single attribute to update.


































 
