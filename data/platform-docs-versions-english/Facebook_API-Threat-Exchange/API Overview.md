ThreatExchange
==============

Most threat-intelligence solutions suffer because the data is too hard to standardize and verify. Meta created the ThreatExchange platform so that participating organizations can share threat data using a convenient, structured, and easy-to-use API that provides privacy controls to enable sharing with only desired groups. You can [apply for membership](https://developers.facebook.com/products/threat-exchange) today!

|     |     |
| --- | --- |
| #### [Get Started](https://developers.facebook.com/docs/threat-exchange/getting-started/)<br><br>Learn how ThreatExchange is structured and walk through steps to get started.<br><br>#### [Get Access](https://developers.facebook.com/docs/threat-exchange/getting-access/)<br><br>Learn the steps required to apply to ThreatExchange and how to add the product.<br><br>#### [API Structure](https://developers.facebook.com/docs/threat-exchange/api-structure/)<br><br>Learn how the ThreatExchange API makes use of the Graph API and try a few calls to get started. | #### [Best Practices](https://developers.facebook.com/docs/threat-exchange/best-practices)<br><br>Make the most effective use of the API by following these tips.<br><br>#### [Reference Code on GitHub](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2F&h=AT2kQVEStuZHZgpBRzkogs7FuoICL5QD5e_KeuLTptKI1bTc1AiEb94S6l-6DG3DCwYP7rkKJNf3ivZ5WY9Ne_awWf2tTRDF0F8lkuavwPV9bD7-O6h9jXEa4nGe7_scPicx8ViogqSpyAyz)<br><br>Use freely available libraries in JavaScript, PHP, Python, and Ruby to speed up your integration and development.<br><br>#### [Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms/)<br><br>Learn about terms of use. |

ThreatExchange UI
-----------------

The UI contains point-and-click management for tags, privacy groups, small-scale descriptor download and upload, and more—while bulk data-processing is best deferred to the API.

|     |     |
| --- | --- |
| ### [UI Overview](https://developers.facebook.com/docs/threat-exchange/ui)<br><br>Essential information about the UI. | ### [UI Reference](https://developers.facebook.com/docs/threat-exchange/reference/ui)<br><br>Full documentation for the ThreatExchange UI. |

ThreatExchange API
------------------

Your one-stop shop for ThreatExchange resources. The API contains the complete feature-set of what is possible in ThreatExchange.

|     |     |
| --- | --- |
| ### [API Reference](https://developers.facebook.com/docs/threat-exchange/reference/apis)<br><br>Full documentation for all of the ThreatExchange APIs. | ### [Privacy Controls](https://developers.facebook.com/docs/threat-exchange/reference/privacy)<br><br>Understand the ways you control who sees the data you publish. |
| ### [Resharing Controls](https://developers.facebook.com/docs/threat-exchange/reference/resharing)<br><br>Understand how to permit re-sharing of your data. | ### [Submit Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting)<br><br>Learn how to submit your data. |
| ### [Submit Connections](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)<br><br>Learn how to create connections between pieces of data to express relationships. | ### [Edit Data](https://developers.facebook.com/docs/threat-exchange/reference/editing)<br><br>Learn how to edit your data. |
| ### [Delete Data](https://developers.facebook.com/docs/threat-exchange/reference/deleting)<br><br>Learn how to delete your data. |     |

Learn More
----------

Look here for anything else you may be missing.

|     |     |
| --- | --- |
| ### [Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms)<br><br>The complete terms and conditions for ThreatExchange. | ### [Changelog](https://developers.facebook.com/docs/threat-exchange/reference/changelog)<br><br>See how the ThreatExchange API has changed. |
| ### [Open Source Terms of Use](https://opensource.facebook.com/legal/terms)<br><br>Terms of use for general Facebook Open Source projects. | ### [Open Source Privacy Policy](https://opensource.facebook.com/legal/privacy)<br><br>Privacy Policy for general Facebook Open Source projects. |

Get Started with ThreatExchange
===============================

ThreatExchange is a simple-to-use platform that supports signal sharing among predefined groups of members in a secure, privacy-compliant, and automated way. Today, ThreatExchange (aka TX or TE) is used by multiple companies to share signals on a variety of topics intended to prevent real world harm. Some examples of how TX is currently used include sharing malware, phishing scams, and terrorism signals with the goal of helping all participating organizations tackle these problems based on their terms of service.

ThreatExchange is built on these core concepts:

* [Signals (aka ThreatIndicators)](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/)
* [Opinions about signals (aka ThreatDescriptors)](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor/)
* [Who can see signals (aka Privacy)](https://developers.facebook.com/docs/threat-exchange/reference/privacy)

These concepts allow a group of ThreatExchange members to share signals, [react to](https://developers.facebook.com/docs/threat-exchange/reference/reacting) and describe signals other members upload, and decide individually on how a signal aligns with their policies.

What is Signal Sharing?
-----------------------

Signal sharing is a tactic to prevent harm on the internet where platforms work together to combat global threats like malware, terrorism, and other harmful content. Platforms help each other by sharing signals from content that they found and labeled on their platform. For example, Platform A might find a video of terrorism on their platform. By sharing the hash of that video (a type of signal) with Platform B, Platform B can find and review that video, which they might have otherwise missed. By sharing signals, the platforms can compound their individual trust & safety efforts and prevent more harm faster.

Signal Sharing is **not** a way for platforms to align on content policies or to coordinate on what content they remove. Each platform reviews content independently according to its own community standards policies and takes actions according to those standards.

Why Would I Contribute?
-----------------------

There are many problems in the Trust & Safety space that affect all platforms jointly, and lead to real world harm. Signal sharing on ThreatExchange tries to reduce this harm by helping platforms find and remove more harmful content. Platforms come in all shapes and sizes, and not all can afford to hire a myriad of reviewers or invest millions in specialized machine learning models. For these platforms, investing in ThreatExchange can be an effective way to use their trust and safety resources.

Even for platform’s which already have robust trust and safety programs, there are still tangible benefits to joining and contributing to ThreatExchange. Namely, the harmful content found on those platform often doesn’t go away, it just goes somewhere else. A rising tide lifts all boats, and by all pitching in, we can improve the baseline safety level for the entire internet. Even if you aren’t uploading new signals to ThreatExchange simply confirming (or disputing!) labels will improve that baseline, build trust in our platforms, and help make the internet safer.

What Signals are Commonly Shared?
---------------------------------

In ThreatExchange, we refer to the signals being shared as [Indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator/). Over 80 types of Indicators can be shared on ThreatExchange and the full list can be found [here](https://developers.facebook.com/docs/threat-exchange/reference/apis/indicator-type). There are, however, a few data types that are particularly common.

### Indicator Types

| Match Text | Indicator Type |
| --- | --- |
| Raw Text | `TEXT_STRING` |
| Trend Queries (keywords+regex) | `TREND_QUERY` |

| Match URLs | Indicator Type |
| --- | --- |
| URLs | `URI` |
| Domains | `DOMAIN` |

| Match Photos | Indicator Type |
| --- | --- |
| PDQ Hashes [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fpdq&h=AT04zdQw1m0wu_8mlBgqvngVFjYTbMMP5Nz5RZNjEn_8Q1m_7ft0DCI9aKaIhONN8bOQ6WhYicJYOHpqhVCvvEcuyjOMCeq_izzBxlPeyApwY14eQL7nfrm7FGvBZrTGKpKQzuDrFVjVsIeW) | `HASH_PDQ` |
| PDQ Hashes + [OCR](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOptical_character_recognition&h=AT1uuibT72UWAPuLSxo8vPIKQuUiEhtiFxNn9oMEqlpt85fKlYXvnPxTwPy-JC8RnGhwdDji0pslsxf4SHQCUpiwBOdzjtl9HQE6pkSaw_gnVoj8xsVq5IRF-AwQcaNDilrAjhpCZCfNIqnO) Text | `HASH_PDQ_OCR` |

| Match Videos | Indicator Type |
| --- | --- |
| MD5 Hash [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMD5&h=AT3KTFnw7xZXk5QkRppj6leaf-7Xdz3Zlh1ASRFUr0Z0j_hyHxd7LWF21WkFNOhZ4U10ZVinHBDcICuE4VYVvwf0mKGCkJ3KkmIR4DzOAhtqWTAjMLvVuRPb6c9DmJ6D7usqzHwEdosnfPPt) | `HASH_MD5` |
| TMK+PDQF Hash [details](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Ftmk&h=AT3Ihm4wwEIJjmqX2IZzgYRUqpBTPQUzP29R22XMBVtyG9z1rSyOTgSoOvQ9VTCd04WEJOprQu1yRIWuwV8pMRW9TRCweZ_H027RqO5FbauqTt1_zIIvh0H9kqmBuSkL_tYW6WgWUfbwrFTe) | `HASH_TMK` |

What is the Cost of Integration?
--------------------------------

Partners who have onboarded have reported the process takes take 1-2 weeks of engineering time to get a basic integration plus another 1-2 weeks for fully automated ingestion and contribution. The cost will vary by company and will depend on a number of factors including the maturity of internal systems and the number of signal types you are attempting to use.

Some questions that might be useful in determining how long it will take your company to integrate are:

* Which of the above signal types are you planning to integrate with? (Text tends to be quick, photos moderate)
* Can you currently search your platform for matches of those signal types? (You can likely piggyback on existing infrastructure, saving time)

How do I Start Reading and Sharing Signals?
-------------------------------------------

Here are the ways to share signals on ThreatExchange:

* **UI**: ThreatExchange has a graphical user interface you can use to quickly and interactively do things like read and share signals and run queries. This is the best place to quickly explore the data in ThreatExchange. Learn more about [ThreatExchange](https://developers.facebook.com/docs/threat-exchange/ui).
    
* **Python**: To build an inital integration and to preform validation we recommend using the python [open source library](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fpython-threatexchange&h=AT22unYY_pituBKadb-EScGZerV-EGeuF0oO9hKHtPwHvOFrpmfoaj66Y_6kMzgy4BLmKbBpWFMxWhC5lQ2JgJjgTW6XgLHoACcmcqSTnJk6c158Te8KQBvdu7VOihUi1gIUJ2fS12bBXHyUJpc1CeNcuJpLSQ) we’ve developed. This allows you fetch a copy of shared signals in a simple format.
    
* **API**: Lastly, there is also a powerful HTTP API which has greater functionality than the python wrapper for an advanced integration. Learn more about these [APIs](https://developers.facebook.com/docs/threat-exchange/reference/apis).

To use any of these methods you will first need to get access to ThreatExchange. ThreatExchange requires you (or someone on your team) to have a Facebook account, or to create one, and then will require creating a new application. Afterwards, you can apply for access to ThreatExchange, which requires you to confirm that your application belongs to your business. After that, you can add more accounts to the application, or store a token to gain access to the API.

Follow [these steps](https://developers.facebook.com/docs/threat-exchange/reference/ui/app-review) to create an App and get access to ThreatExchange.

Get Access
==========

Getting access to ThreatExchange is done through Facebook Developer Applications, and has a few steps:

1. Creating a Facebook account if you do not already have one.
2. Find your company's business account, or creating a new account if your company doesn't have one.
3. Creating a ThreatExchange application connected to your business account and adding the ThreatExchange product.
4. If your business account is not already business verified, you'll need to verify it. This is the longest step and can take 2 or more weeks with multiple submissions.
5. Making a ThreatExchange App Submission. This usually takes 1-2 business days to complete.

Creating the Application and Business Verification
--------------------------------------------------

To get access to Threat Exchange, you will need to have a business verified Application. We recommend creating a dedicated app to handle your ThreatExchange integration, with a name like "YourCompany ThreatExchange".

* To create a new Business app, follow the instructions [here](https://developers.facebook.com/docs/development/create-an-app/). Make sure to select type "Business" during creation.
* To get your business verified, follow the instructions [here](https://developers.facebook.com/docs/development/release/business-verification).

### Terms of Use

Please see the [Terms and Conditions](https://www.facebook.com/legal/threatexchange_terms)—depending on your company, you may want to obtain sign-off from your company's legal team.

Add the ThreatExchange Product
------------------------------

If your application category is Business, you can find ThreatExchange on the [Products](https://developers.facebook.com/docs/development/create-an-app/app-dashboard#products-2) section of your application dashboard. If you don't see it there, confirm that your app type is "Business" (circled red area in the banner at the top of your dashboard). If your app type is not Business, unfortunately you will have to create a new application, as it is currently not possible to change it after creation.

When you click on "Set Up" on ThreatExchange, it will add the ThreatExchange product in your sidebar, where you can continue the submission.

### Start the Submission

[](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/292791084_475834287638346_3341843078967238976_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=d9FMAf_ZoaMAX9YwoFl&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDcryF-sOfpxncoMppl059pOlG2Gh9Z0YqG83k9u-72Sg&oe=65BF1AF9)

### Fill Out App Settings

[](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/292890012_627854204928767_1789413238663381649_n.png?_nc_cat=102&ccb=1-7&_nc_sid=e280be&_nc_ohc=kq8-JJAIbIgAX_cB0uM&_nc_ht=scontent-cdg4-1.xx&oh=00_AfDNhJrMqFuDs_wtN7CIdMAXJ7Pmb0nqZVzsHs-u1fEwnQ&oe=65BF2BBA)

  

ThreatExchange uses the app-ID framework, but there is no installable app per se.

* Enter URLs appropriate for your organization and any company logo for the "app icon".
* For "platform", use "website" and your company's URL.
* Business verification can take some amount of time to get through. Please contact us at threatexchange@meta.com with any issues.

  

[](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/292466362_397227655570395_1131662562722176425_n.png?_nc_cat=102&ccb=1-7&_nc_sid=e280be&_nc_ohc=dOX94czvS0IAX8w4gN7&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCtf6vs9VuiVWdq1YRdOAj8TjJNFtMETySbGPwD6uaAfg&oe=65BF0FEE)

  
  

[](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/292403367_3349426345285401_742102408421089417_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=aCbtaEb20kEAX8cO4wv&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAhgiT6Z66lUTinJoRTeaErtWqzi8ZrYPpkg7xR9wCVjw&oe=65BF050A)

  
  

[](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/292694456_457967432359085_5508285514533748348_n.png?_nc_cat=102&ccb=1-7&_nc_sid=e280be&_nc_ohc=zT7907D25GkAX9J_zV6&_nc_ht=scontent-cdg4-1.xx&oh=00_AfCZ9zz80pb757tJmNn_4lUOg2SMDkIz4iSXgUyPW5BHIg&oe=65BF3783)

  
  

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292580731_412383744172096_2305975966123374119_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=95xEV-OMS40AX8NcNPF&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCgvN95bUZhA1vYVlI5YrAhnrvd94IdxH0O7YMZve6O5A&oe=65BF1183)

  
  

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292809995_764249381371075_1589826872236914997_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=kFVbNSaF_uAAX8VlfTW&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCSwQdAdjhf5vDCS8giWZptymUfZc7UEws6-ua9cmy5_A&oe=65BF33C8)

  

### Fill Out Your Use Case

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292713607_397769922179949_2193932156581216740_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=2-jHN3tYc78AX8OHWsG&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCFflifAg37MkofhsJRuAO1TBulo94O_UbVI65IJgIV3A&oe=65BF2195)

  

### Make the App Public

If you haven't already done so, check that you have changed the app's status to "Live".

[](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/292609215_718318572763124_9222290415658146657_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=AZQYH94PoJQAX8dCxL6&_nc_ht=scontent-cdg4-1.xx&oh=00_AfAfQuOVIzrbPJKep83XCoQNc6L5iXTzpnGCV1rZ-xbs3Q&oe=65BF1474)

  

### Submit for Review

If you get a message about needing to upload an Android or iOS version of your app (ThreatExchange does not use installable apps), go back to **Settings** -> **Basic**. Ensure that for "platform", you have used "website" with your company's URL.

  

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292590954_1100503220545003_3825931399270878094_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=65Keof1fASMAX-aks5e&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDd2Ybp2bVsABusP7nGLc4Prpbn1If_grLJuRlbUDUEbg&oe=65BF2C17)

  
  

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292621568_452732026275021_2109765007626020073_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=nyemtfAkstYAX-Tw6O3&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBUwBAqVZm859p7nfpWTV1xymWGDWNqnJUiPBxbM53Tfg&oe=65BF3039)

  

### Once Review Is Complete

The name **ThreatExchange** appears with a green checkmark, and you see the subproducts "Descriptors", "Tags", and so on, in addition to "App Review", which you had seen up until now.

[](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/292462360_766059234838101_426983120944602255_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=hEE10nkBCXMAX9crMW4&_nc_ht=scontent-cdg4-1.xx&oh=00_AfDXuSwqb1LnFQAY7AfrqZrHBurjCvpmAJFlKziAa0wpIg&oe=65BF1FDC)

  

Do a power search for tag "testing"—you should see results.

[](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/292752818_558509602491530_7162809144311194941_n.png?_nc_cat=103&ccb=1-7&_nc_sid=e280be&_nc_ohc=9bUWY47S-Y4AX-qpbdF&_nc_ht=scontent-cdg4-2.xx&oh=00_AfC39p3_cCIcJrN3Q8iq4zKEvxGynvIFsUIQf4pZRolLEQ&oe=65BF2A9D)

Adding Users to an ThreatExchange Account
-----------------------------------------

If your company already has a business account, here are the steps for adding users:

1) Users must do the following before being added to the account:

* a) create their own Facebook account if they don't already have one.
* b) register as a Facebook developer by following [these steps](https://developers.facebook.com/docs/development/register/).

2) There are two options to be added to a ThreatExchange app account. One uses "business accounts", and the other is for an admin to directly add a personal account to the application. Using the business account allows you to separate your work and personal usage more cleanly. Learn more about adding people to a business account [here](https://www.facebook.com/business/help/2169003770027706). From [business.facebook.com/settings/people/](https://business.facebook.com/settings/people/) for your business, you can invite people to your business.

3) Using the person's work email, invite them to your business account. You don't need to give them any permissions at this point.

As of July 2023, this is what the "Add Person" flow looks like:

You'll be leaving all the defaults and not assigning any permissions at this stage.

4) After the person has accepted the invite, you can then assign them to the ThreatExchange Application:

You'll need to assign at least at the "Develop App" level, but "Manage App" can also simplify fixing settings.

  
  

Next, learn about [Best Practices for Using ThreatExchange](https://developers.facebook.com/docs/threat-exchange/best-practices).

Best Practices for Using ThreatExchange
=======================================

This guide explains some ways to use ThreatExchange that will help improve throughput and usage.

Downloading Data
----------------

When you get access to new data in ThreatExchange (such as by being added to a PrivacyGroup), we recommend you get a sample or complete copy of the data to evaluate it.

You can use these APIs and UI:

* [ThreatExchange UI](#sample-csvs) - sample data
* [/threat\_descriptors API](#threat-descriptors-api) - samples data
* [/threat\_updates API](#threat-updates-api) - Recommended API for complete copy
* [/<TAG\_ID>/tagged\_objects API](#tagged-objects-api) - Okay for a 1-time complete copy

Only some of them should be used for automated integration into your own systems, and the others should be used only for sampled evaluation and testing.

### Sample CSVs from the UI

Some privacy groups have a feature where samples of indicators can be downloaded from the UI, which is the fastest way to evaluate potential data. Learn more at [ThreatExchange UI.](https://developers.facebook.com/docs/threat-exchange/reference/ui/collaborations)

### Sampling from /threat\_descriptors API

[The /threat\_descriptors API](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors) allows you to do complex searches on ThreatDescriptors. This can be useful to generate your own narrow samples, but the API is not guaranteed to be contain all data that matches the filters.

### Tailing /threat\_updates API

**Recommended**—[The /threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates) API allows you to exactly reproduce a [ThreatPrivacyGroup](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-group/)'s contents. It also allows you to get deletion events as long as you poll within 30 days of the object being deleted. Tailing /threat\_updates gives you the lowest latency, complete data, and is the only API that notifies of deletes.

Not all PrivacyGroups have this API enabled, reach out to threatexchange@meta.com for questions about enabling it.

### /<TAG\_ID>/tagged\_objects API

The [/<TAG\_ID>/tagged\_objects](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags) API allows you to reliably download all ThreatDescriptors tagged with those tags. Because most data is tagged, this is a reliable way to get data. However, you must do client-side filtering to remove unwanted data, but with the same tags (for example, in the wrong privacy group, wrong type, etc). Additionally, because you don't learn of deletions or updates, you must start over from `tagged_since=0` at some interval (for example, 30 days) in order get updates and discard data that has been deleted.

Tag Your Data
-------------

By [tagging your data](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/), it makes it easier for yourself and others to find the indicators they care most about. For example, by tagging descriptors with `evil`, this allows others to filter descriptors searches by data with that tag. Another option is that you can then search the `threat_tags` endpoint by that tag and see all the tagged objects visible to you. The tagging endpoint also supports partial matches on tags, so a query for `evil` will surface any tags visible to you which are like `evil*`.

Be Descriptive with Your Tags
-----------------------------

ThreatTags (also known as "subjective tags") contain metadata fields describing what they are. If you create the tag `foo`, others can inspect the metadata to see what means or why the data was tagged. But it's helpful to be more descriptive instead; for example, `campaign_zeusbotnet` or `malicious_ssl_cert`.

Consider Privacy Rules
----------------------

ThreatTags are visible based on the [PrivacyType](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type/) of the tagged data. For example, if the tag `public_tag` is on ANY descriptor that is publically visible (privacy type of VISIBLE), then the tag is visible to all members. Conversely, if the tag `nonpublic_tag` is ONLY on tagged objects shared to specific members (privacy types \`HAS\_WHITELIST\` or \`HAS\_PRIVACY\_GROUP\`), then the tag is only visible to those members. Tag your data accordingly. Learn more about [PrivacyType tag](https://developers.facebook.com/docs/threat-exchange/reference/apis/privacy-type/).

For more uses cases with ThreatTags, see the [ThreatTag reference](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags/).

Use Batch Requests for Improved Throughput
------------------------------------------

Batch requests allow you to make multiple requests to the Graph API using a single HTTP call. For more information on Graph API Batch Requests, review the following:

* [Making multiple API requests](https://developers.facebook.com/docs/graph-api/making-multiple-requests)
    
* [Batch requests documentation](https://developers.facebook.com/docs/reference/ads-api/batch-requests)
    

You can also query for multiple objects by ID using the following syntax:

https://graph.facebook.com/v2.8/?ids=\[id1,id2\]&amp;access\_token=<access\_token>

If you need to query for a specific field:

https://graph.facebook.com/v2.8/?ids=\[id1,id2\]&amp;fields=field1,field2&amp;access\_token=<access\_token>

Include Nested Fields and Objects in Result Data
------------------------------------------------

It can sometimes be more efficient to include various nested fields or related objects in your search results. The following syntax shows how, for the `facebook.com` indicator object, to pull all of its descriptors without issuing additional API calls:

https://graph.facebook.com/v2.8/788497497903212?fields=descriptors{owner,description,status,share\_level},indicator,type&amp;access\_token=<access\_token>

RESULT:
{
  "descriptors": {
    "data": \[
      {
        "owner": {
          "id": "820763734618599",
          "name": "Facebook Administrator"
        },
        "description": "Facebook",
        "status": "NON\_MALICIOUS",
        "share\_level": "GREEN",
        "id": "834469179976904"
      },
      {
        "owner": {
          "id": "588498724619612",
          "name": "Facebook CERT ThreatExchange"
        },
        "description": "Non malicious",
        "status": "NON\_MALICIOUS",
        "share\_level": "GREEN",
        "id": "1202389109786630"
      }
    \],
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

ThreatExchange UI Overview
==========================

This guide describes the most basic subset of what you can do with the ThreatExchange APIs. See the [ThreatExchange API Reference](https://developers.facebook.com/docs/threat-exchange/reference/apis) for a comprehensive list of the ThreatExchange APIs and the related endpoints.

  

ThreatExchange UI Use Cases
---------------------------

* People at various organizations want to share information about **threats**: malicious URLs, harmful content hashes, malware signatures, and so on.
    
* A [**threat indicator**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) is the **objective part**: a file hash, a URL, and so on, with a type (MD5, SHA1, URL, and so on).
    
* A [**threat descriptor**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) contains an indicator and the **subjective parts**: how malicious a team thinks it is, when they first saw it, and so on.
    
* Meta privacy revolves around **user IDs,** ThreatExchange revolves around **app IDs**. For example, app ID 1064060413755420 is Media Hash Sharing Test. These are generally of the form _Team T at company C_.
    
* When people share threat data, they can specify who they want to see each datum. This is referred to as a **visibility** or **privacy type**.
    
    * _Visible/public_ means all ThreatExchange members can see it.
        
    * Or, for each datum the members can create an app-whitelist of specific teams at specific companies.
        
    * Or, for each datum the members can specify a privacy-group that is simply a predefined list of app IDs.
        
    
* People can [**tag**](https://developers.facebook.com/docs/threat-exchange/reference/apis/threattags) their descriptors. These are tags in any other tool, except that ThreatExchange tags have their own metadata, including the subjective parts that descriptors have, and they also have their own visiblity (public/app-whitelist/privacy-group).
    
* There's more about threat descriptors ([review status](https://developers.facebook.com/docs/threat-exchange/reference/apis/review-status-type) and [others](https://developers.facebook.com/docs/threat-exchange/reference/apis)) and other types of data shareable on ThreatExchange. For the purpose of this walkthrough, we're focused on indicators, descriptors, visibility, and tags.
    

Find the UI
-----------

Navigate to [https://developers.facebook.com/apps](https://developers.facebook.com/apps) and select your app:

  

Then, find the ThreatExchange product within the navbar on the left:

Add Team Members
----------------

1. Navigate to [https://developers.facebook.com/apps](https://developers.facebook.com/apps) and select your app.
2. Select **Roles** > **Roles**.
3. Add teammate roles as **Administrators** or **Developers**. **Note**: Do not add teammates as **Test Users** or **Analytics Users**. These roles have no meaning for ThreatExchange apps.
4. If your organization has a ThreatExchange app ID, but the assigned administrators/developers have since left your organization, please contact us at **threatexchange@meta.com** so that we can reset an admin to be a current employee of your organization. From there, you'll be able to self-service add everyone else in your organization.

Search Data Using the UI
------------------------

A variety of search options are supported.

  

Search for all malicious URLs uploaded in the last week:

Publish Data Using the UI
-------------------------

See the [Submit Data](https://developers.facebook.com/docs/threat-exchange/reference/submitting) page for examples.

Feedback
--------

Contact **threatexchange@meta.com** with any and all feedback on how we can better enable your success in using ThreatExchange.

You can also use the bugnub to report issues:

  

Learn more about the [UI Reference](https://developers.facebook.com/docs/threat-exchange/reference/ui).

ThreatExchange UI Reference
===========================

Learn more about the information organized by the UI tab.

|     |     |
| --- | --- |
| #### [Collaborations Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/collaborations)<br><br>Download data and see statistics from collaborations in which you participate.<br><br>#### [Tags Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/tags/)<br><br>Find and organize the data you share.<br><br>#### [Members Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/members)<br><br>Discover a Partner. | #### [Descriptors Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/descriptors)<br><br>Understand fundamental components of threat-data sharing.<br><br>#### [Privacy Groups Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/privacy-groups/)<br><br>Control which partner organizations you want to have access to the threat data you share.<br><br>#### [App Review Tab](https://developers.facebook.com/docs/threat-exchange/reference/ui/app-review)<br><br>Apply to use ThreatExchange. |

ThreatExchange UI Collaborations Tab
====================================

The **Collaborations** tab allows you to see statistics about and download data from collaborations in which you participate.

Things you can do on this tab:

* See all the collaborations in which you participate.
    
* Select a collaboration to show the number of indicators of each type that are currently a part of the collaboration's dataset.
    
* Select **Download Sample Dataset** to download indicators for one or all indicator types (CSV format).

ThreatExchange UI Descriptors Tab
=================================

Searching
---------

You have multiple ways to search for ThreatDescriptors (and more to come -- see [status here](https://developers.facebook.com/docs/threat-exchange/ui#status)):

Search results are rendered as a table. You can view (or clone) ones you do not own, or edit ones you do own:

Details are shown in a popup -- here is a descriptor owned by another app:

Broadening your searches
------------------------

Given search results, you may wish to fan out to similar results. In this example, let's start with sample data.

  

From there, we can find other descriptors with the same indicator (hash):

  

We can also find other descriptors which have been related to these (see [Submitting Connections](https://developers.facebook.com/docs/threat-exchange/reference/submitting-connections)):

  

Note that we can poke the fanout buttons multiple times to traverse deeper depths of connection.

Saved searches
--------------

Given any search, simply poke the "Copy search URL to clipboard" button.

  

Then you can paste the URL into a message to share with coworkers, or what have you. Additionally, you can paste the URL into the browser bar and bookmark it:

  

You can even make a bookmark folder for your favorite searches:

Editing
-------

When you click Edit on a descriptor your app owns, you are able to mutate all editable attributes, with tooltips to provide context. (ID, indicator text, and indicator type are immutable after a particular descriptor is created.) Note: reactions and connections are not exposed yet in the UI -- see [status here](https://developers.facebook.com/docs/threat-exchange/ui#status).

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

Please see the [Submitting Data page](https://developers.facebook.com/docs/threat-exchange/reference/submitting#uploading) for file formats, examples, and more.

ThreatExchange UI Tags Tab
==========================

The tags tab allows you to interact with the tags on threat descriptors.

  

You create the tag by adding tag text and descriptions. Note: You can have multiple tags of the same tag text. You can either use the default settings or select your own status, review status, confidence, severity, share level, visibility, expire time, first active time, and last active time, privacy groups (if applicable), and whitelists (if applicable). Hover over the dropdowns for extra information provided about the options. The source, owner app id and owner app name is autogenerated for you. Select the OK button at the bottom of the popup to create the tag or CANCEL to exit the flow without creating a new tag. An example of this popup is shown below.

  

You can view tags by searching for the exact text, a substring of the text, or by ID. To search for these select the type from the "by exact text" dropdown, type the phrase in the textbox next to the dropdown, and click search or press the enter key.

  

If you have permissions, you can edit tags by selecting the edit button in the first column of the tag search results. Clicking the edit button will allow you to change all fields that you have access to during a tag create. Click the OK button at the bottom to save results or the CANCEL button to discard any changes you have made to the popup.

  

For tags you cannot edit, the view button will appear in the first column of the table. Clicking the VIEW button provides additional information about the selected tag.

ThreatExchange UI Privacy Groups Tab
====================================

The **Privacy Groups** tab shows the Privacy Groups in ThreatExchange and allows for detailed viewing of each group and editing actions (if available).

  

Click **View** next to each Privacy Group entry to show the detailed page. From this page, you can see additional information about the privacy group and a documentation link.

  

Privacy Groups that you have access to change will have an **Edit** button. Click **Edit** to change the name, description, visibility and joining settings, and member apps. It also displays a documentation link.

  

Click **Create** to create a new Privacy Group. You can select the name, descriptions, joining and visibility settings, and who can use it. You can not select the owner App ID or the owner app name; this is autogenerated for you. An example of this popup is shown below.

ThreatExchange UI Members Tab
=============================

The members tab shows the available list of participating members. This is an informative table; you can not change the state of member information from this tab.

You can sort members ascending or descending by id, name, and email by clicking on the table header for the corresponding field.

You can filter the member results based on the name of the member by using the text box above the table.

You can also download all query results by clicking the download query results drop-down box. Select either JSON or CSV to download the results in the corresponding format. Note that it will download the list of all members even if you have filtered by name.

Graph API Version

[v18.0](#)

ThreatExchange API Overview
===========================

Authenticate via an Access Token
--------------------------------

The ThreatExchange APIs perform authentication via access tokens. After Facebook notifies you that your App can access ThreatExchange, use the [access token tool](https://developers.facebook.com/tools/accesstoken) to get an **App Token**. _Please note, app tokens give access to sensitive details to your app and should be treated like a password._

With the access token, test your access to ThreatExchange by retrieving the list of members in the exchange:

https://graph.facebook.com/threat\_exchange\_members?access\_token=<access\_token>

If this request does not return an error, you are now ready to begin exploring the ThreatExchange API!

Searching Data Using the API
----------------------------

With your newly activated access token, perform a search for malicious URLs added in the last week:

https://graph.facebook.com/threat\_descriptors?type=URI&amp;status=MALICIOUS&amp;since=a week ago&amp;access\_token=<access\_token>

Please note that not all fields are returned by default. Consult the reference documentation and specify the fields you are looking to read by appending the fields parameter. See the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#reading) for more details.

Publishing Data Using the API
-----------------------------

**Test publish** a domain, `my-test-example.com`, ensuring only you are able to see the data:

https://graph.facebook.com/threat\_descriptors

POST DATA

type=DOMAIN
indicator=my-test-example.com
privacy\_type=HAS\_WHITELIST
status=UNKNOWN
description=Test data publishing
share\_level=RED
privacy\_members=<your\_app\_id>
access\_token=555|1235

The return value will be a JSON map with a success or failure code and, if the call is successful, the unique ThreatExchange ID for the descriptor you published!

**Publish** a descriptor for your own domain, `my-company-domain.com`, and share it with Facebook's app ID, `820763734618599`:

https://graph.facebook.com/threat\_descriptors

POST DATA

type=DOMAIN
indicator=my-company-domain.com
privacy\_type=HAS\_WHITELIST
status=NON\_MALICIOUS
description=The domain owned by <your\_app\_id>
share\_level=WHITE
privacy\_members=820763734618599
access\_token=555|1235

More API Examples
-----------------

**Search** for all compromised credentials found on the Internet within the last day:

https://graph.facebook.com/`v18.0`/threat\_indicators?type=COMPROMISED\_CREDENTIAL&since=yesterday&access\_token=555|1235\]
        

**Find** the unique ThreatExchange ID for a specific indicator, such as `facebook.com`:

https://graph.facebook.com/`v18.0`/threat\_indicators?text=facebook.com&access\_token=555|1235
        

**Explore** related indicators for a specific indicator with ThreatExchange ID `898557073557972`:

https://graph.facebook.com/898557073557972/descriptors?access\_token=555|1235

**Explore** all of the descriptors for a specific indicator with ThreatExchange ID `898557073557972`:

https://graph.facebook.com/898557073557972/descriptors?access\_token=555|1235

See more examples on our [Github](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange&h=AT0G93GK32CULfytqMA5agSBfyOPo_NQseEGPOsFOqreBLAVdsvPS9H-pcgn3Vos92CN7iVLghpNyOZoN-hoeGJ7zaM6DMprd-KxIIYNsV4_BMWdXHopNkQ9vXUFckI-9BSEj2Hiygl7ms1M), or on the endpoint pages for [threat indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators), [threat descriptors](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors).

Python/Ruby/Java/Curl wrappers
------------------------------

The above snippets showed you some examples of the bare REST API. For an easier path to integration please see [our Python wrapper](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Fblob%2Fmaster%2Fpython-threatexchange%2FREADME.md&h=AT3r5RLsPd6JqW1bronN8uzfqDz_zidVivsv6Jwi-hasIipaMrEaTlRYFWtbrvmhl0YLGQ15o4MVMRxIU9-xPPKXADshMOgrh251_lTXiTIBn1jjjDhxKUrvs_ZyfUCzDr2nsk_hKnp9TLJr).

Please also see our descriptor-focused reference designs in [Ruby](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fapi-reference-examples%2Fruby%2Fte-tag-query%2FREADME.md&h=AT3ukxjswQB3XRf1j0yvvTMzNOp3Ma4KlI5xUznZYk-XmI_hpqha3DanKTBkzEBr0oiOKPyFZDxzNTE43iJF5r-huhyfmh5TA-9Bpc7y3P1vmR1nGzDwJRTURCTe-SUqItbeQ6EI4-fwhue4), [Java](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fapi-reference-examples%2Fjava%2Fte-tag-query%2FREADME.md&h=AT1c1eNx1LNVV4K0YGp69-WHZ8_WVBFimzlO1a_FaMI8y8ZgHHuwF6hvqNwnZNTgPJ5z2SSAmxisY5YuURK-xphyAruoLHq0uQvU_IJ3OxaUJkzyyNuOTr4Fyi2O4cYG0TXx3BStv7xrjK3f), and [bare-curl](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebook%2FThreatExchange%2Ftree%2Fmaster%2Fapi-reference-examples%2Fcurl%2Fte-tag-query%2FREADME.md&h=AT0KCp3XkQuVnulhg2jI0UZhi2bpnZAAJj2UYpfaYLQ4zuGeeyHEMyNJy7lcYUaFdGuPV05hOWMtCKb-PxJE9B0cK9Js9SIa5J0vq3y5iI8AtcO0b_3EyD_w7fvT5I0lepRNoEQMyf0Obbiz).

API Examples
============

This page has various API examples in [Python](#python_examples), [Java](#java_examples), [PHP](#php_examples), and using [cURL](#curl_examples).

Python
------

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

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

r = requests.get('https://graph.facebook.com/v2.4/threat\_indicators?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

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

r = requests.get('https://graph.facebook.com/v2.4/threat\_descriptors?' + query\_params)

print json.dumps(ast.literal\_eval(r.text), sort\_keys=True,indent=4,separators=(',', ': '))

Java
----

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatIndicators {

public final static void main(String\[\] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat\_indicators?";
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

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;

public class ThreatDescriptors {

public final static void main(String\[\] args) throws Exception {
String url = "https://graph.facebook.com/v2.4/threat\_descriptors?";
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

PHP
---

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

<?php
$appID = "555"; // Replace this with your AppID
$appSecret = "1234"; // Replace this with your App Secret
$type = 'IP\_ADDRESS';
$text = 'proxy';
$access\_token = $appID . "|" . $appSecret;

$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL,
"https://graph.facebook.com/v2.5/threat\_indicators?" .
"access\_token=" . $access\_token .
"&amp;type=" . $type .
"&amp;text=" . $text);
curl\_setopt($ch, CURLOPT\_RETURNTRANSFER, 1);
$response = curl\_exec($ch);
$json = json\_encode(json\_decode($response), JSON\_PRETTY\_PRINT);
print($json . PHP\_EOL);
curl\_close($ch);
?>

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

<?php
$appID = "555"; // Replace this with your AppID
$appSecret = "1234"; // Replace this with your App Secret
$type = 'IP\_ADDRESS';
$text = 'proxy';
$ownerAppID = "820763734618599";
$access\_token = $appID . "|" . $appSecret;

$ch = curl\_init();
curl\_setopt($ch, CURLOPT\_URL,
"https://graph.facebook.com/v2.5/threat\_descriptors?" .
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

cURL
----

Example 1: A query to get all threat indicators which are IP Addresses of proxies in ThreatExchange.

curl -i -X GET \\
"https://graph.facebook.com/v2.4/threat\_indicators"\\
"?type=IP\_ADDRESS&text=proxy&access\_token=555%7C1234"

Example 2: A query to get all IP Addresses of proxies uploaded by the Facebook Administrator app in ThreatExchange.

curl -i -X GET \\
"https://graph.facebook.com/v2.4/threat\_descriptors"\\
"?type=IP\_ADDRESS&owner=820763734618599&text=proxy&access\_token=555%7C1234"

API Structure for ThreatExchange
================================

ThreatExchange is a subset of API endpoints within the larger ecosystem of Facebook Graph APIs. It is recommended to review the [Graph API documentation](https://developers.facebook.com/docs/graph-api), as it covers key concepts: usage of access tokens for authentication, result pagination, and batching.

The ThreatExchange APIs are made up of various [objects](https://developers.facebook.com/docs/threat-exchange/reference/apis) and each object can have connections to other objects. For instance, a threat indicator is an object that can be connected to other threat indicators.

ThreatExchange also allows for multiple members to share the same threat indicator. Because there is the potential for a collision, we separate each member's submission into distinct [ThreatDescriptor](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor) objects, which are connected to their respective [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator)

Viewing Individual Objects
--------------------------

You can access a Graph object’s properties with its unique ID, e.g. for a [ThreatIndicator](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object:

* [/{threat\_indicator\_id}](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator)
    

You can do the same for all other objects type within ThreatExchange:

* [/{threat\_descriptor\_id}](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptor)
    

Queries For Multiple Objects
----------------------------

Queries into ThreatExchange are HTTP GET requests to one of the following URLs:

* [/threat\_descriptors](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-descriptors)
    
* [/threat\_indicators](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicators)
    
* [/threat\_exchange\_members](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-exchange-members)
    
* [/threat\_privacy\_groups](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-privacy-groups)
    
* [/{privacy\_group\_id}/threat\_updates](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-updates)
    

**All Graph API objects work in a similar way. After you have [authenticated](https://developers.facebook.com/docs/threat-exchange/getting-started), try some calls with the [`threat_indicator`](https://developers.facebook.com/docs/threat-exchange/reference/apis/threat-indicator) object.**

To ensure consistency, the ThreatExchange APIs and its consumers use JSON objects as their default currency. Using these APIs gives you a lot of things for free:

* Field validation
    
* Type checking
    
* Persistence to Facebook's Graph
    
* Everyone else can use what you share and be better protected!
    

All objects are formatted as maps using a predefined set of field names, with expected value types. They can be of arbitrary size and field order in the map is, generally, not important.