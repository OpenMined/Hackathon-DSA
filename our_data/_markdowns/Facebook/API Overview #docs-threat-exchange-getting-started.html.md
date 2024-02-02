Get Started - ThreatExchange - Documentation - Meta for Developers

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
Get Started with ThreatExchange
===============================

ThreatExchange is a simple-to-use platform that supports signal sharing among predefined groups of members in a secure, privacy-compliant, and automated way. Today, ThreatExchange (aka TX or TE) is used by multiple companies to share signals on a variety of topics intended to prevent real world harm. Some examples of how TX is currently used include sharing malware, phishing scams, and terrorism signals with the goal of helping all participating organizations tackle these problems based on their terms of service.

ThreatExchange is built on these core concepts:

* Signals (aka ThreatIndicators)
* Opinions about signals (aka ThreatDescriptors)
* Who can see signals (aka Privacy)

These concepts allow a group of ThreatExchange members to share signals, react to and describe signals other members upload, and decide individually on how a signal aligns with their policies.

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

In ThreatExchange, we refer to the signals being shared as Indicators. Over 80 types of Indicators can be shared on ThreatExchange and the full list can be found here. There are, however, a few data types that are particularly common.

### Indicator Types

 Match Text | Indicator Type || Raw Text | `TEXT_STRING` |
| Trend Queries (keywords+regex) | `TREND_QUERY` |

 Match URLs | Indicator Type || URLs | `URI` |
| Domains | `DOMAIN` |

 Match Photos | Indicator Type || PDQ Hashes details | `HASH_PDQ` |
| PDQ Hashes + OCR Text | `HASH_PDQ_OCR` |

 Match Videos | Indicator Type || MD5 Hash details | `HASH_MD5` |
| TMK+PDQF Hash details | `HASH_TMK` |
What is the Cost of Integration?
--------------------------------

Partners who have onboarded have reported the process takes take 1-2 weeks of engineering time to get a basic integration plus another 1-2 weeks for fully automated ingestion and contribution. The cost will vary by company and will depend on a number of factors including the maturity of internal systems and the number of signal types you are attempting to use.

Some questions that might be useful in determining how long it will take your company to integrate are:

* Which of the above signal types are you planning to integrate with? (Text tends to be quick, photos moderate)
* Can you currently search your platform for matches of those signal types? (You can likely piggyback on existing infrastructure, saving time)

How do I Start Reading and Sharing Signals?
-------------------------------------------

Here are the ways to share signals on ThreatExchange:

* **UI**: ThreatExchange has a graphical user interface you can use to quickly and interactively do things like read and share signals and run queries. This is the best place to quickly explore the data in ThreatExchange. Learn more about ThreatExchange.
* **Python**: To build an inital integration and to preform validation we recommend using the python open source library we’ve developed. This allows you fetch a copy of shared signals in a simple format.
* **API**: Lastly, there is also a powerful HTTP API which has greater functionality than the python wrapper for an advanced integration. Learn more about these APIs.

To use any of these methods you will first need to get access to ThreatExchange. ThreatExchange requires you (or someone on your team) to have a Facebook account, or to create one, and then will require creating a new application. Afterwards, you can apply for access to ThreatExchange, which requires you to confirm that your application belongs to your business. After that, you can add more accounts to the application, or store a token to gain access to the API.

Follow these steps to create an App and get access to ThreatExchange.