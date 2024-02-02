::: content
::: {.display-flex .justify-content-space-between .align-items-center .flex-wrap-wrap .page-metadata-container}
:::

To improve our network infrastructure and better serve API traffic
globally, LinkedIn will begin rejecting API calls not meeting new
criteria.

::: NOTE
Note

For more information about API specific examples, see our [*Migration
Guide*](../../references/migrations/query-tunneling-migration) .
:::

## Requirements

Ensure your LinkedIn API requests comply with the following size
requirements. If your request exceeds any of the size requirements
listed below, your request will receive a 414 response.

  Request parameter   Size in KB
  ------------------- -----------------------------------------------------------------------------------
  Raw URL             8 KB max length (scheme + hostname + port + path + query string of the URL)
  Query String        4 KB max length
  Request URL         28 KB max length (headers + cookies + URI + queryString, but excluding POST data)
  URL path segment    4 KB max characters (the area between slashes in a URL)

## Query Tunneling {#query-tunneling-1}

To support these requirements, we're introducing the concept of query
tunneling. This feature allows you to modify your existing requests with
a custom header to easily resolve offending requests.

### Requests without Body

1.  Change the request from ` GET ` to ` POST ` .
2.  Add the ` X-HTTP-Method-Override ` header, using the original HTTP
    method (-H \"X-HTTP-Method-Override: GET\").
3.  Add the ` Content-Type ` header (-H \"Content-Type:
    application/x-www-form-urlencoded\").
4.  Move the query string to the body of the request.

#### Example

Let's use the example request below to see how we can quickly convert
our existing request to the organizationalEntityAcls API using query
tunneling.

##### Current Request

``` lang-curl
curl -X GET 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
-H 'Authorization: Bearer redacted'
```

1.  Change the request type from GET to POST.

``` lang-curl
curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
-H 'Authorization: Bearer redacted'
```

1.  Add the method override header and append the original GET request
    type.

``` lang-curl
curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
-H 'X-HTTP-Method-Override: GET'
-H 'Authorization: Bearer redacted'
```

1.  Add the ` Content-Type ` header.

``` lang-curl
curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee&projection=(elements*(organizationalTarget~))' \
-H 'X-HTTP-Method-Override: GET'
-H 'Content-Type: application/x-www-form-urlencoded'
-H 'Authorization: Bearer redacted'
```

1.  Move the query string of the request URL to the request body.

``` lang-curl
curl -X POST 'https://api.linkedin.com/v2/organizationalEntityAcls' \
-H 'X-HTTP-Method-Override: GET'
-H 'Content-Type: application/x-www-form-urlencoded' 
-H 'Authorization: Bearer redacted'
--data 'q=roleAssignee&projection=(elements*(organizationalTarget~))'
```

### Requests with Body

1.  Change the request type from PUT to POST if the original request
    type was PUT. If the original request type was POST, keep it as
    POST.
2.  Add the X-HTTP-Method-Override header using the original HTTP method
    ` -H 'X-HTTP-Method-Override: POST' ` for POSTs or
    ` -H 'X-HTTP-Method-Override: PUT' ` for PUTs.
3.  Add the Content-Type header
    ` -H 'Content-Type: multipart/mixed; boundary=xyz' ` . Note that
    here we need to specify a boundary delimiter (here we use ` xyz `
    for illustration) for multipart body, this delimiter needs to be
    unique and not appearing in your request content body or url.
4.  Move the query string and original request body to body as two
    sections explained above.

#### Example

Let's use the example request below to see how we can quickly convert
our existing request to the adCreativesV2 API using query tunneling.

###### Current Request

``` lang-curl
curl -X POST 'https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196)' \
-H 'Authorization: Bearer redacted' \
-H 'Content-Type: application/json' \
-H 'X-Restli-Protocol-Version: 2.0.0' \
-H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
--data '{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}'
```

1.  Change the request type from PUT to POST if the original request
    type was PUT. If the original request type was POST, keep it as
    POST.

``` lang-curl
curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
  -H 'Authorization: Bearer redacted' \
  -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
  -H 'X-RestLi-Protocol-Version: 2.0.0' \
  --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
```

1.  Add the X-HTTP-Method-Override header using the original HTTP method
    ` -H 'X-HTTP-Method-Override: POST' ` for POSTs or
    ` -H 'X-HTTP-Method-Override: PUT' ` for PUTs.

``` lang-curl
curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
  -H 'X-HTTP-Method-Override: POST' \
  -H 'Authorization: Bearer redacted' \
  -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
  -H 'X-RestLi-Protocol-Version: 2.0.0' \
  --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
```

1.  Add the Content-Type header
    ` -H 'Content-Type: multipart/mixed; boundary=xyz' ` .

``` lang-curl
curl -X POST https://api.linkedin.com/v2/adCreativesV2?ids=List(47770196) \
  -H 'X-HTTP-Method-Override: POST' \
  -H 'Content-Type: multipart/mixed; boundary=xyz' \
  -H 'Authorization: Bearer redacted' \
  -H 'X-RestLi-Method: BATCH_PARTIAL_UPDATE' \
  -H 'X-RestLi-Protocol-Version: 2.0.0' \
  --data ${"entities": {{"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}}'
```

1.  Move the query string and original request body to body as two
    sections.

``` lang-curl
curl -X POST https://api.linkedin.com/v2/adCreativesV2 \
  -H 'X-HTTP-Method-Override: POST' \
  -H 'Content-Type: multipart/mixed; boundary=xyz' \
  -H 'Authorization: Bearer redacted' \
  -H 'X-Restli-Protocol-Version: 2.0.0' \
  -H 'X-RestLi-Method:  BATCH_PARTIAL_UPDATE' \
  --data $'--xyz\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\nids=List(47770196)\r\n--xyz\r\n 
         Content-Type: application/json\r\n\r\n{"entities": {"47770196": {"patch": {"$set": {"status": "ACTIVE"}}}}}\r\n--xyz--' 
```
:::
