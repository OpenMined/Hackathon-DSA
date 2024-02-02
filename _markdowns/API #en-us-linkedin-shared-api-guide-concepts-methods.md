::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

LinkedIn\'s APIs have an expressive set of methods for interacting.

## GET

The GET method requests a single, specific entity/object from a service.
This method leverages the traditional HTTP GET method.

``` lang-https
GET https://api.linkedin.com/v2/{service}/{resourceIdentifier}
```

## GET_ALL

The GET_ALL method requests all entities/objects from a service. GET_ALL
requests never provide resource identifiers to a service. This method
uses the traditional HTTP GET method.

``` lang-https
GET https://api.linkedin.com/v2/{service}
```

## BATCH_GET

The BATCH_GET method requests more than one specific entity/object from
a service. This method uses the traditional HTTP GET method.

``` lang-https
GET https://api.linkedin.com/v2/{service}?ids=List(resourceIdentifier_1,...,resourceIdentifier_n)
```

## FINDER {finderName}

Conceptually, FINDER methods are similar to GET/BATCH_GET calls. The
main difference between these methods is that you use FINDER queries
when you don\'t have an identifier to directly retrieve an entity. These
methods use the HTTP GET method with a ` q={finderName} ` request
parameter which identifies the type of query being made. FINDER methods
can return zero, one, or more results, depending on the number of
entities that match the query input.

``` lang-https
GET https://api.linkedin.com/v2/{service}?q={finderName}
```

## CREATE

The CREATE method indicates to a service that it should use the
information provided in the request body to create a new entity. This
method uses the traditional HTTP POST method.

``` lang-https
POST https://api.linkedin.com/v2/{service}/{Request Body}
```

## BATCH_CREATE

The BATCH_CREATE method indicates to a service that it should use the
information provided in the request body to create multiple new
entities. This method uses the traditional HTTP POST method.

``` lang-https
POST https://api.linkedin.com/v2/{service}/{Request Body}
```

The UPDATE method indicates to a service that it should use the
information provided in the request body to overwrite the entire
definition of an existing entity. This method uses the traditional HTTP
PUT method.

``` lang-https
PUT https://api.linkedin.com/v2/{service}/{Request Body}
```

The BATCH_UPDATE method indicates to a service that it should use the
information provided in the request body to overwrite the entire
definitions of multiple existing entities. This method uses the
traditional HTTP ` PUT ` method.

``` lang-https
PUT https://api.linkedin.com/v2/{service}/{Request Body}
```

The PARTIAL_UPDATE method indicates to a service that it should use the
information provided in the request body to update only specific
portions of an existing entity rather than overwriting the entire
definition of the entity. This method uses the traditional HTTP POST
method.

::: NOTE
Note

For the server to differentiate between a PARTIAL_UPDATE and an UPDATE,
you must include ` X-Restli-Method: PARTIAL_UPDATE ` as the header value
in your request.
:::

``` lang-https
POST https://api.linkedin.com/v2/{service}/{Request Body}
```

The BATCH_PARTIAL_UPDATE method indicates to a service that it should
use the multiple pieces of information provided in the request body to
update specific portions of multiple specified entities, rather than
overwriting them entirely. This method uses the traditional HTTP POST
method.

::: NOTE
Note

For the server to differentiate between a ` BATCH_PARTIAL_UPDATE ` and a
` BATCH_UPDATE ` , you must include
` X-Restli-Method: BATCH_PARTIAL_UPDATE ` as the header value in your
request.
:::

``` lang-https
POST https://api.linkedin.com/v2/{service}/{Request Body}
```

## DELETE

The DELETE method indicates to a service that it should delete an
identified object/entity. This method uses the traditional HTTP DELETE
method.

``` lang-https
DELETE https://api.linkedin.com/v2/{service}/{resourceIdentifier}
```

## BATCH_DELETE

The BATCH_DELETE method indicates to a service that it should delete
multiple identified objects/entities. This method uses the traditional
HTTP DELETE method.

``` lang-https
DELETE https://api.linkedin.com/v2/{service}?ids=List({resourceIdentifier_1},...,{resourceIdentifier_n})
```

## BATCH_FINDER {finderName}

Conceptually, BATCH_FINDER methods are similar to BATCH_GET calls. The
main difference between these methods is that you use BATCH_FINDER
queries when you don\'t have identifiers to directly retrieve entities.
These methods use the HTTP GET method with a bq={batchFinderName}
request parameter which identifies the type of query being made.
BATCH_FINDER methods accept a list of filters set. Instead of calling
multiple finders with different filter values, we call one BATCH_FINDER
method with a list of filters. BATCH_FINDER methods can return zero,
one, or more results, depending on the number of entities that match the
query input.

``` lang-https
GET https://api.linkedin.com/v2/{service}?bq={batchFinderName}
```

## ACTION {actionName}

The ACTION method is a flexible method that does not specify any type of
standard behavior. It uses the HTTP POST method, with a special
` action={actionName} ` request parameter, which identifies the specific
type of action to take.

``` lang-https
POST https://api.linkedin.com/v2/{service}?action={actionName}
```
:::
