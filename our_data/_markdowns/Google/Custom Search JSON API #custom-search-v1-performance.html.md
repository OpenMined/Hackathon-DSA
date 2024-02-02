
Performance Tips  |  Programmable Search Engine  |  Google for Developers

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

Performance Tips
================

 Stay organized with collections

 Save and categorize content based on your preferences.

This document covers some techniques you can use to improve the performance of your application. In some cases, examples from other APIs or generic APIs are used to illustrate the ideas presented. However, the same concepts are applicable to the Custom Search JSON API.

Compression using gzip
----------------------

An easy and convenient way to reduce the bandwidth needed for each request is to enable gzip compression. Although this requires additional CPU time to uncompress the results, the trade-off with network costs usually makes it very worthwhile.

In order to receive a gzip-encoded response you must do two things: Set an `Accept-Encoding` header, and modify your user agent to contain the string `gzip`. Here is an example of properly formed HTTP headers for enabling gzip compression:

```
Accept-Encoding: gzip
User-Agent: my program (gzip)
```

Working with partial resources
------------------------------

Another way to improve the performance of your API calls is by requesting only the portion of the data that you're interested in. This lets your application avoid transferring, parsing, and storing unneeded fields, so it can use resources including network, CPU, and memory more efficiently.

### Partial response

By default, the server sends back the full representation of a resource after processing requests. For better performance, you can ask the server to send only the fields you really need and get a *partial response* instead.

To request a partial response, use the `fields` request parameter to specify the fields you want returned. You can use this parameter with any request that returns response data.

#### Example

The following example shows the use of the `fields` parameter with a generic (fictional) "Demo" API.

**Simple request:** This HTTP `GET` request omits the `fields` parameter and returns the full resource.

```
https://www.googleapis.com/demo/v1
```
**Full resource response:** The full resource data includes the following fields, along with many others that have been omitted for brevity.

```
{
  "kind": "demo",
  ...
  "items": [
  {
    "title": "First title",
    "comment": "First comment.",
    "characteristics": {
      "length": "short",
      "accuracy": "high",
      "followers": ["Jo", "Will"],
    },
    "status": "active",
    ...
  },
  {
    "title": "Second title",
    "comment": "Second comment.",
    "characteristics": {
      "length": "long",
      "accuracy": "medium"
      "followers": [ ],
    },
    "status": "pending",
    ...
  },
  ...
  ]
}
```
**Request for a partial response:** The following request for this same resource uses the `fields` parameter to significantly reduce the amount of data returned.

```
https://www.googleapis.com/demo/v1?**fields=kind,items(title,characteristics/length)**
```
**Partial response:** In response to the request above, the server sends back a response that contains only the kind information along with a pared-down items array that includes only HTML title and length characteristic information in each item.

```
**200 OK**
```

```
{
  "kind": "demo",
  "items": [{
    "title": "First title",
    "characteristics": {
      "length": "short"
    }
  }, {
    "title": "Second title",
    "characteristics": {
      "length": "long"
    }
  },
  ...
  ]
}
```
Note that the response is a JSON object that includes only the selected fields and their enclosing parent objects.

Details on how to format the `fields` parameter is covered next, followed by more details about what exactly gets returned in the response.

#### Fields parameter syntax summary

The format of the `fields` request parameter value is loosely based on XPath syntax. The supported syntax is summarized below, and additional examples are provided in the following section.

* Use a comma-separated list to select multiple fields.
* Use `a/b` to select a field `b` that is nested within field `a`; use `a/b/c` to select a field `c` nested within `b`.   
**Exception:** For API responses that use "data" wrappers, where the response is nested within a `data` object that looks like `data: { ... }`, do not include "`data`" in the `fields` specification. Including the data object with a fields specification like `data/a/b` causes an error. Instead, just use a `fields` specification like `a/b`.
* Use a sub-selector to request a set of specific sub-fields of arrays or objects by placing expressions in parentheses "`( )`".
 For example: `fields=items(id,author/email)` returns only the item ID and author's email for each element in the items array. You can also specify a single sub-field, where `fields=items(id)` is equivalent to `fields=items/id`.
* Use wildcards in field selections, if needed.
 For example: `fields=items/pagemap/*` selects all objects in a pagemap.

#### More examples of using the fields parameter

The examples below include descriptions of how the `fields` parameter value affects the response.

**Note:** As with all query parameter values, the `fields` parameter value must be URL encoded. For better readability, the examples in this document omit the encoding.

Identify the fields you want returned, or make field selections.
The `fields` request parameter value is a comma-separated list of fields, and each field is specified relative to the root of the response. Thus, if you are performing a list operation, the response is a collection, and it generally includes an array of resources. If you are performing an operation that returns a single resource, fields are specified relative to that resource. If the field you select is (or is part of) an array, the server returns the selected portion of all elements in the array.  

 Here are some collection-level examples:  

| Examples | Effect |
| --- | --- |
| `items` | Returns all elements in the items array, including all fields in each element, but no other fields. |
| `etag,items` | Returns both the `etag` field and all elements in the items array. |
| `items/title` | Returns only the `title` field for all elements in the items array.
 Whenever a nested field is returned, the response includes the enclosing parent objects. The parent fields do not include any other child fields unless they are also selected explicitly. |
| `context/facets/label` | Returns only the `label` field for all members of the `facets` array, which is itself nested under the `context` object. |
| `items/pagemap/*/title` | For each element in the items array, returns only the `title` field (if present) of all objects that are children of `pagemap`. |

 Here are some resource-level examples:  

| Examples | Effect |
| --- | --- |
| `title` | Returns the `title` field of the requested resource. |
| `author/uri` | Returns the `uri` sub-field of the `author` object in the requested resource. |
| `links/*/href` | Returns the `href` field of all objects that are children of `links`. |

Request only parts of specific fields using sub-selections.
By default, if your request specifies particular fields, the server returns the objects or array elements in their entirety. You can specify a response that includes only certain sub-fields. You do this using "`( )`" sub-selection syntax, as in the example below.

| Example | Effect |
| --- | --- |
| `items(title,author/uri)` | Returns only the values of the `title` and author's `uri` for each element in the items array. |

#### Handling partial responses

After a server processes a valid request that includes the `fields` query parameter, it sends back an HTTP `200 OK` status code, along with the requested data. If the `fields` query parameter has an error or is otherwise invalid, the server returns an HTTP `400 Bad Request` status code, along with an error message telling the user what was wrong with their fields selection (for example, `"Invalid field selection a/b"`).

Here is the partial response example shown in the introductory section above. The request uses the `fields` parameter to specify which fields to return.

```
https://www.googleapis.com/demo/v1?**fields=kind,items(title,characteristics/length)**
```
The partial response looks like this:

```
**200 OK**
```

```
{
  "kind": "demo",
  "items": [{
    "title": "First title",
    "characteristics": {
      "length": "short"
    }
  }, {
    "title": "Second title",
    "characteristics": {
      "length": "long"
    }
  },
  ...
  ]
}
```
**Note:** For APIs that support query parameters for data pagination (`maxResults` and `nextPageToken`, for example), use those parameters to reduce the results of each query to a manageable size. Otherwise, the performance gains possible with partial response might not be realized.

 Send feedback

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-02-01 UTC.

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