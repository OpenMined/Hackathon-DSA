
Custom Search Site Restricted JSON API  |  Programmable Search Engine  |  Google for Developers

* Programmable Search Engine

* English
* Deutsch
* Español
* Español – América Latina
* Français
* Indonesia
* Italiano
* Polski
* Português – Brasil
* Tiếng Việt
* Türkçe
* Русский
* עברית
* العربيّة
* فارسی
* हिंदी
* বাংলা
* ภาษาไทย
* 中文 – 简体
* 中文 – 繁體
* 日本語
* 한국어

Sign in

Home

Guides

Reference

Support

* Programmable Search Engine

* Home
* Guides
* Reference
* Support

* Overview
* Programmable Search Engine Tutorial
	+ Get Started
	+ Create a Programmable Search Engine
	+ Implement Search Box
	+ Enable Autocomplete
	+ Customize Search Results
	+ Next Steps
* Search Configuration
	+ Configuration Files
	+ Context File
	+ Annotations File
	+ Custom Ranking
	+ Refining Searches
	+ Rewriting Queries
	+ Promotions
	+ Making Money
	+ Admin Accounts
	+ Programmable Search Element API
	+ Programmable Search Element Ads-Free Paid API
	+ More Callback Examples
* Look and Feel
	+ Search UI Components
	+ Context File
* Structured Data
	+ Provide Structured Data
	+ Filter Search Results
	+ Customize Result Snippets
* JSON API
	+ Overview
	+ Introduction
	+ Using REST
	+ Performance Tips
	+ Libraries and Samples
	+ Site Restricted JSON API
* Advanced Topics
	+ Topical Engines

* Home
* Products
* Programmable Search Engine
* Guides

 Send feedback

Custom Search Site Restricted JSON API
======================================

 Stay organized with collections

 Save and categorize content based on your preferences.

**Note:** The Custom Search Site Restricted JSON API endpoints will cease to serve
traffic on December 18, 2024.All Custom Search Site Restricted JSON API
customers must begin their transition to
Google Cloud's Vertex AI Search.
Detailed transition guidance can be found
here.
If you experience issues, you can contact
us here.

This document describes how to use the Custom Search Site Restricted JSON API.

About the Custom Search Site Restricted JSON API
------------------------------------------------

If your Programmable Search Engine is restricted to only searching specific sites (10 or fewer),
you can use the Custom Search Site Restricted JSON API. This API is similar to the
Custom Search JSON API except this version has no daily query limit. To use this
version, confirm that you see 10 or fewer sites to search in the “Sites to
Search” section of your Programmable Search Engine control panel, there are no global top level
domain patterns, and that “Search the entire web” is set to OFF.

When using the Custom Search Site Restricted JSON API endpoint, be mindful that if your
Programmable Search Engine configuration is changed so that it does not conform with the site
restriction rules above, the Custom Search Site Restricted JSON API may not return the
expected results.

Making a request
----------------

Making a request to Custom Search Site Restricted JSON API is similar to making a request to
Custom Search JSON API; however, the URI is different. The format for the
Custom Search Site Restricted JSON API is

https://www.googleapis.com/customsearch/v1/siterestrict?[parameters]

The `[parameters]` are the same as the Custom Search JSON API parameters

Pricing
-------

Custom Search Site Restricted JSON API requests cost $5 per 1000 queries and there is no
daily query limit. You may sign up for billing in the
API Console.

 Send feedback

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-01-23 UTC.

 [{
 "type": "thumb-down",
 "id": "missingTheInformationINeed",
 "label":"Missing the information I need"
 },{
 "type": "thumb-down",
 "id": "tooComplicatedTooManySteps",
 "label":"Too complicated / too many steps"
 },{
 "type": "thumb-down",
 "id": "outOfDate",
 "label":"Out of date"
 },{
 "type": "thumb-down",
 "id": "samplesCodeIssue",
 "label":"Samples / code issue"
 },{
 "type": "thumb-down",
 "id": "otherDown",
 "label":"Other"
 }]

 [{
 "type": "thumb-up",
 "id": "easyToUnderstand",
 "label":"Easy to understand"
 },{
 "type": "thumb-up",
 "id": "solvedMyProblem",
 "label":"Solved my problem"
 },{
 "type": "thumb-up",
 "id": "otherUp",
 "label":"Other"
 }]

 Need to tell us more?

* Help Community
Get help in the Programmable Search Engine Help Community
* Stack Overflow
Ask a question under the google-custom-search tag
* Blog
Read our blog

* ### Product Info

	+ Terms of Service
	+ Control Panel
* ### Programs

	+ Women Techmakers
	+ Google Developer Groups
	+ Google Developer Experts
	+ Accelerators
	+ Google Developer Student Clubs
* ### Developer consoles

	+ Google API Console
	+ Google Cloud Platform Console
	+ Google Play Console
	+ Firebase Console
	+ Actions on Google Console
	+ Cast SDK Developer Console
	+ Chrome Web Store Dashboard

* Android
* Chrome
* Firebase
* Google Cloud Platform
* All products

* Terms
* Privacy
* Sign up for the Google for Developers newsletter
Subscribe

* English
* Deutsch
* Español
* Español – América Latina
* Français
* Indonesia
* Italiano
* Polski
* Português – Brasil
* Tiếng Việt
* Türkçe
* Русский
* עברית
* العربيّة
* فارسی
* हिंदी
* বাংলা
* ภาษาไทย
* 中文 – 简体
* 中文 – 繁體
* 日本語
* 한국어