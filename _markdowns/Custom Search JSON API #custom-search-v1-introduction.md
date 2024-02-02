
















Custom Search JSON API: Introduction  |  Programmable Search Engine  |  Google for Developers
















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
 
 

Custom Search JSON API: Introduction
====================================




 
 Stay organized with collections
 

 
 Save and categorize content based on your preferences.
 






This document will help you to get familiar with Custom Search JSON API and its usage.


Before you start
----------------


### Create Programmable Search Engine


By calling the API user issues requests against an existing instance of
Programmable Search Engine.
Therefore, before using the API, you need to create one in the
Control Panel
. Follow the tutorial
to learn more about different configuration options.
Once it is created, you can find the **Search Engine ID** in the **Overview**
page's **Basic** section. This is the `cx` parameter used by the API.


### Identify your application to Google with API key


Custom Search JSON API requires the use of an API key. An API key is a way to identify your client to Google.


* Programmable Search Engine (free edition) users:
Get a Key


After you have an API key, your application can append the query parameter
`key=yourAPIKey` to all request URLs. The API key is safe for embedding in URLs,
 it doesn't need any encoding.


API overview
------------


### API operations


There is only one method to invoke in the Custom Search JSON API:




| Operation | Description | REST HTTP mapping |
| --- | --- | --- |
| list | Returns the requested search results from a Programmable Search Engine. | `GET` |


### API data model


The result of a search query to the Custom Search JSON API is a JSON object that includes three types of data: 


* Metadata describing the requested search (and, possibly, related search requests)
* Metadata describing the Programmable Search Engine
* Search results


See the Response data section of Using REST for more details.


The data model is based on the OpenSearch 1.1 Specification. In addition to the standard OpenSearch properties, the Custom Search JSON API defines two custom properties and two custom query roles:


* Custom properties
	+ `cx`: The identifier of the Programmable Search Engine.
	+ `safe`: A description of the safe search level for filtering the returned results.
* Custom query roles
	+ `nextPage`: A role that indicates the query can be used to
	 access the next logical page of results, if any.
	+ `previousPage`: A role that indicates the query can be used
	 to access the previous logical page of results, if any.


Try it
------


To play around and see what the API can do, without writing any code, visit the
"Try this API" tool.


For a full description of parameters visit the
cse.list reference.


To learn how to use the API via HTTP requests, continue to
Using REST.









 
 
 Send feedback
 
 




Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.


Last updated 2023-06-22 UTC.







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





















