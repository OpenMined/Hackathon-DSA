Overview - Content Library and API - Documentation - Meta for Developers

Content Library and API* Get access
* Quick links
* Content Library
* Content Library API
* Appendix
* Get help
* Citations
Overview
========

Meta Content Library API provides access to real-time data from public discussions on Facebook and Instagram, equipping researchers to study existing topics of interest as well as understand evolving or emerging topics on our platforms.

Content Library API can be accessed either through Meta's Researcher Platform or through an approved third-party cleanroom environment. The following third-party cleanroom environments are approved as of Content Library API version 2.0:

* Inter-university Consortium for Political and Social Research (ICPSR) at the University of Michigan

User documentation for third-party cleanroom interfaces is outside the scope of the Meta Content Library API documentation and can instead be provided by the third-party's system administrator.

Content Library API client
--------------------------

When you access the API through Meta's Researcher Platform, you use our Content Library API Client which runs on Jupyter and with which you can create Jupyter notebooks. Once you have created a notebook, you can import our Python3 or R Content Library API client module which allows you to perform queries using the API. See Getting started.

The Content Library API Client allows you to access a variety of fields on the following data. Information and content from public entities listed below will be returned; however, certain data that could potentially identify users (such as tags in Facebook) will be redacted or omitted in API responses.

* Facebook Pages
* Facebook groups
* Facebook events
* Facebook posts
* Instagram business and creator accounts, and a subset of personal accounts that match qualification criteria
* Instagram posts

Note that public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription.
VPN
---

You access the API through our virtual private network (VPN) using OpenVPN. Follow the OpenVPN Setup instructions in Getting started to learn how to install and configure the OpenVPN client.

Data dictionary
---------------

We provide a detailed Data dictionary that describes the data names displayed in the Meta Content Library (the Name column) if applicable, and the corresponding API fields returned in Content Library API search responses (the API field column).

Meta Content Library
--------------------

Meta Content Library is a web-based tool that allows researchers to explore and understand data across Facebook and Instagram by offering a comprehensive, visual, searchable collection of publicly accessible content—the same content that is also accessible through the Content Library API. The web-based user interface allows you to explore data, test out search parameters, and assess whether the resulting data is appropriate for your planned research. No knowledge of query or programming languages is needed.
Code examples
-------------

Code examples in this documentation use a tabbed code block with tabs for R and Python. Click the tab for the language of your choice to display the appropriate code. This is an example:

RPython
```
Click the R tab to display R code here
```
```
Click the Python tab to display Python code here
```
You can copy the code in either tab and paste it into a Jupyter notebook cell for the same language (R or Python).

Learn more
----------

* Frequently asked questions
* Search quality approach
* Researcher Platform
* Meta Content Library