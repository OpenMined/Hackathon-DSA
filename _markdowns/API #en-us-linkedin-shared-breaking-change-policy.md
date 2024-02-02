
















































LinkedIn API Breaking Change Policy - LinkedIn | Microsoft Learn













Skip to main content



This browser is no longer supported.


Upgrade to Microsoft Edge to take advantage of the latest features, security updates, and technical support.



Download Microsoft Edge
More info about Internet Explorer and Microsoft Edge





















Table of contents 



Exit focus mode
































Read in English




Save













Table of contents

Read in English




Save

Edit




Print


Twitter
LinkedIn
Facebook
Email











Table of contents




LinkedIn API Breaking Change Policy
===================================




* Article
* 05/08/2023
* 3 contributors








Feedback





In this article
---------------




Overview
--------


As our APIs evolve, LinkedIn will make reasonable efforts to notify you of breaking changes in advance with sufficient time to adapt to these changes.



Important


We may make changes without prior notice if the change is considered non-breaking, or if it is a breaking change being made to address critical product bugs or legal, security, or privacy concerns.



Review this guide carefully to understand what kind of changes we consider to be breaking and non-breaking, and how to ensure that your application can adapt automatically to any change we categorize as non-breaking.


Definition
----------


A **breaking change** is a change that may require you to make changes to your application in order to avoid disruption to your integration. The following are a few examples of changes we consider breaking:


* Changes to existing permission definitions
* Removal of an allowed parameter, request field or response field
* Addition of a required parameter or request field without default values
* Changes to the intended functionality of an endpoint. *For example, if a DELETE request previously used to archive the resource but now hard deletes the resource.*
* Introduction of a new validation


A **non-breaking change** is a change that you can adapt to at your own discretion and pace without disruption. In most cases, we will communicate non-breaking changes after they are already made. Ensure that your application is designed to be able to handle the following types of non-breaking changes without prior notice from LinkedIn:


* Addition of new endpoints
* Addition of new methods to existing endpoints
* Addition of new fields in the following scenarios:
	+ New fields in responses
	+ New optional request fields or parameters
	+ New required request fields that have default values
* Addition of a new value returned for an existing text field
* Changes to the order of fields returned within a response
* Addition of an optional request header
* Removal of redundant request header
* Changes to the length of data returned within a field
* Changes to the overall response size
* Changes to error messages. *We do not recommend parsing error messages to perform business logic. Instead, you should only rely on HTTP response codes and error codes.*
* Fixes to HTTP response codes and error codes from incorrect code to correct code


Communication
-------------


Please look out for email communication from LinkedIn where we may notify you about breaking and non-breaking changes to our APIs. For breaking change notices, the email notice will usually include the future release date of the breaking change as well as instructions on what actions you need to take. To avoid disruption to your users, ensure that you perform the recommended actions by LinkedIn before the release date of the breaking change.













---


Feedback
--------



Was this page helpful?







Yes





No





Provide product feedback




Feedback
--------



Submit and view feedback for



This product
This page



View all page feedback








---


Additional resources
--------------------












California Consumer Privacy Act (CCPA) Opt-Out Icon





Your Privacy Choices







Theme





* Light
* Dark
* High contrast






* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2023







Additional resources
--------------------






### In this article






















California Consumer Privacy Act (CCPA) Opt-Out Icon





Your Privacy Choices







Theme





* Light
* Dark
* High contrast






* 
* Previous Versions
* Blog
* Contribute
* Privacy
* Terms of Use
* Trademarks
* © Microsoft 2023







