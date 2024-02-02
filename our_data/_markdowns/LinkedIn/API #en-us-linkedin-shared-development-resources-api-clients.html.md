
API Clients - LinkedIn | Microsoft Learn

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

LinkedIn API Clients
====================

* Article
* 03/30/2023
* 1 contributor

Feedback

In this article
---------------

Background
----------

The Rest.li protocol defines 14 resource methods as a higher-level abstraction on top of the standard HTTP methods, each with its own standardized interface and intended semantics.

For example, to retrieve one or more entities, any one of these Rest.li methods can be implemented for a resource, depending on the use case: GET, BATCH\_GET, GET\_ALL, FINDER, or BATCH\_FINDER. Each of those Rest.li methods would have its own standard request and response interfaces.

The Rest.li protocol also supports complex resource keys and query parameters, and it has a custom protocol for encoding them.

Nearly all of LinkedIn's APIs are built on the Rest.li framework with additional LinkedIn-specific details, which results in a robust yet complex protocol that can be challenging to implement correctly.

API Client Overview
-------------------

To simplify development, we have released API client libraries in the following languages, each of which contains comprehensive documentation and examples in their corresponding GitHub repository:

| Language | Installation and API Reference Docs | Examples |
| --- | --- | --- |
| JavaScript | link | link |
| Python | link | link |

Note that these client libraries do not support specific APIs - they provide an abstraction on top of the Rest.li protocol, making it easier to construct API requests to LinkedIn. This simplifies the process for you to build your higher-level clients for specific APIs.

Some of the key features of the LinkedIn API Client Libraries include:

* RestliClient with support for all Rest.li methods
* AuthClient with support for token creation/management
* Typed interfaces to enable code completion and inline documentation in IDEs
* Rest.li protocol 2.0 support
* Automatic key/query parameter encoding
* Support for versioned APIs
* Automatic query tunneling of requests, if required

Example
-------

To illustrate the benefits of using these API clients, consider searching for ad accounts using our Advertising API. For a NodeJS application using an HTTP client library like axios, there are quite a few details to get right to perform a working request, as shown in the following sample code: base URL, resource prefix, auth and custom headers, and correct encoding of complex query parameters. The result can be difficult to write and maintain and doesn’t account for edge cases requiring query tunneling.

```
const axios = require('axios');
const ACCESS_TOKEN = "AQX5…";
const API_VERSION = '202302';
// Define a generic function to search ad accounts by references
function searchForAdAccountsByReferences(
 references,
 count = 10,
 sortField = 'ID',
 sortOrder = 'ASCENDING'
) {
 return axios.request({
   baseURL: 'https://api.linkedin.com',
   url: '/rest/adAccounts',
   method: 'get',
   headers: {
     'Authorization': `Bearer ${ACCESS_TOKEN}`,
     'X-RestLi-Method': 'finder',
     'X-RestLi-Protocol-Version': '2.0.0',
     'Connection': 'Keep-Alive',
     'LinkedIn-Version': API_VERSION
   },
   params: {
     q: 'search',
     search: `(reference:(values:List(${references.map(encodeURIComponent).join(',')})))`,
     count,
     sort: `(field:${sortField},order:${sortOrder})`
   },
   paramsSerializer: {
     // Can't use default encoding
     encode: (val) => val
   }
 }).then(response => response.data.elements);
}
// Search for ad accounts by a list of organizations, with up to 20 results
const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
 console.log(adAccounts);
});
```
Compare that to this code utilizing the LinkedIn API client. The client abstracts much of the complexities of constructing the request. It allows passing in objects, arrays, and strings with special characters as is, making the code easy to write and maintain. Furthermore, it handles edge cases where query tunneling may be required.

```
const { RestliClient } = require('linkedin-api-client');
const restliClient = new RestliClient();
const ACCESS_TOKEN = "AQX5...";
const API_VERSION = '202302';
// Define a generic function to search ad accounts by references
function searchForAdAccountsByReferences(
  references,
  count = 10,
  sortField = 'ID',
  sortOrder = 'ASCENDING'
) {
  return restliClient.finder({
    resourcePath: '/adAccounts',
    finderName: 'search',
    queryParams: {
      search: {
        reference: {
          values: references
        },
      },
      count,
      sort: {
        field: sortField,
        order: sortOrder
      }
    },
    versionString: API_VERSION,
    accessToken: ACCESS_TOKEN
  }).then(response => response.data.elements);
}
// Search for ad accounts by a list of organizations, with up to 20 results
const orgs = ['urn:li:organization:123', 'urn:li:organization:456'];
searchForAdAccountsByReferences(orgs, 20).then(adAccounts => {
  console.log(adAccounts);
});
```
In summary, using these API clients can speed up and simplify the development process and make your application code maintainable and robust. If any issues arise, the corresponding Github repository is available for bug reports and enhancement suggestions.

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
* © Microsoft 2024

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
* © Microsoft 2024