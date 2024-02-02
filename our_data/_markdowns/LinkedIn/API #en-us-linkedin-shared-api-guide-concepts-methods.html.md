
LinkedIn API Request Methods - LinkedIn | Microsoft Learn

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

Request Methods
===============

* Article
* 05/08/2023
* 5 contributors

Feedback

In this article
---------------

LinkedIn's APIs have an expressive set of methods for interacting.

GET
---

The GET method requests a single, specific entity/object from a service. This method leverages the traditional HTTP GET method.

```
GET https://api.linkedin.com/v2/{service}/{resourceIdentifier}
```
GET\_ALL
--------

The GET\_ALL method requests all entities/objects from a service. GET\_ALL requests never provide resource identifiers to a service. This method uses the traditional HTTP GET method.

```
GET https://api.linkedin.com/v2/{service}
```
BATCH\_GET
----------

The BATCH\_GET method requests more than one specific entity/object from a service. This method uses the traditional HTTP GET method.

```
GET https://api.linkedin.com/v2/{service}?ids=List(resourceIdentifier_1,...,resourceIdentifier_n)
```
FINDER {finderName}
-------------------

Conceptually, FINDER methods are similar to GET/BATCH\_GET calls. The main difference between these methods is that you use FINDER queries when you don't have an identifier to directly retrieve an entity. These methods use the HTTP GET method with a `q={finderName}` request parameter which identifies the type of query being made. FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

```
GET https://api.linkedin.com/v2/{service}?q={finderName}
```
CREATE
------

The CREATE method indicates to a service that it should use the information provided in the request body to create a new entity. This method uses the traditional HTTP POST method.

```
POST https://api.linkedin.com/v2/{service}/{Request Body}
```
BATCH\_CREATE
-------------

The BATCH\_CREATE method indicates to a service that it should use the information provided in the request body to create multiple new entities. This method uses the traditional HTTP POST method.

```
POST https://api.linkedin.com/v2/{service}/{Request Body}
```
UPDATE
------

The UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definition of an existing entity. This method uses the traditional HTTP PUT method.

```
PUT https://api.linkedin.com/v2/{service}/{Request Body}
```
BATCH\_UPDATE
-------------

The BATCH\_UPDATE method indicates to a service that it should use the information provided in the request body to overwrite the entire definitions of multiple existing entities. This method uses the traditional HTTP `PUT` method.

```
PUT https://api.linkedin.com/v2/{service}/{Request Body}
```
PARTIAL\_UPDATE
---------------

The PARTIAL\_UPDATE method indicates to a service that it should use the information provided in the request body to update only specific portions of an existing entity rather than overwriting the entire definition of the entity. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a PARTIAL\_UPDATE and an UPDATE, you must include `X-Restli-Method: PARTIAL_UPDATE` as the header value in your request.

```
POST https://api.linkedin.com/v2/{service}/{Request Body}
```
BATCH\_PARTIAL\_UPDATE
----------------------

The BATCH\_PARTIAL\_UPDATE method indicates to a service that it should use the multiple pieces of information provided in the request body to update specific portions of multiple specified entities, rather than overwriting them entirely. This method uses the traditional HTTP POST method.

Note

For the server to differentiate between a `BATCH_PARTIAL_UPDATE` and a `BATCH_UPDATE`, you must include `X-Restli-Method: BATCH_PARTIAL_UPDATE` as the header value in your request.

```
POST https://api.linkedin.com/v2/{service}/{Request Body}
```
DELETE
------

The DELETE method indicates to a service that it should delete an identified object/entity. This method uses the traditional HTTP DELETE method.

```
DELETE https://api.linkedin.com/v2/{service}/{resourceIdentifier}
```
BATCH\_DELETE
-------------

The BATCH\_DELETE method indicates to a service that it should delete multiple identified objects/entities. This method uses the traditional HTTP DELETE method.

```
DELETE https://api.linkedin.com/v2/{service}?ids=List({resourceIdentifier_1},...,{resourceIdentifier_n})
```
BATCH\_FINDER {finderName}
--------------------------

Conceptually, BATCH\_FINDER methods are similar to BATCH\_GET calls. The main difference between these methods is that you use BATCH\_FINDER queries when you don't have identifiers to directly retrieve entities. These methods use the HTTP GET method with a bq={batchFinderName} request parameter which identifies the type of query being made. BATCH\_FINDER methods accept a list of filters set. Instead of calling multiple finders with different filter values, we call one BATCH\_FINDER method with a list of filters. BATCH\_FINDER methods can return zero, one, or more results, depending on the number of entities that match the query input.

```
GET https://api.linkedin.com/v2/{service}?bq={batchFinderName}
```
ACTION {actionName}
-------------------

The ACTION method is a flexible method that does not specify any type of standard behavior. It uses the HTTP POST method, with a special `action={actionName}` request parameter, which identifies the specific type of action to take.

```
POST https://api.linkedin.com/v2/{service}?action={actionName}
```

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