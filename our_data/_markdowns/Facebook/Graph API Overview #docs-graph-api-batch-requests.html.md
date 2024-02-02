Batch Requests - Graph API - Documentation - Meta for Developers

Graph API* Overview
* Get Started
* Batch Requests
* Debug Requests
* Handle Errors
* Field Expansion
* Secure Requests
* Resumable Upload API
* Changelog
* Features Reference
* Permissions Reference
* Reference
Batch Requests
==============

Send a single HTTP request that contains multiple Facebook Graph API calls. Independent operations are processed in parallel while dependent operations are processed sequentially. Once all operations are complete, a consolidated response is passed back to you and the HTTP connection is closed.

The ordering of responses correspond with the ordering of operations in the request. You should process responses accordingly to determine which operations were successful and which should be retried in a subsequent operation.

### Limitations

* Batch requests are limited to 50 requests per batch. Each call within the batch is counted separately for the purposes of calculating API call limits and resource limits. For example, a batch of 10 API calls will count as 10 calls and each call within the batch contributes to CPU resource limits in the same manner. Please see our Rate Limiting Guide for more information.
* Batch requests cannot include multiple Adsets under the same Campaign. Learn more about batching Marketing API requests.

Batch Request
-------------

A batch request takes a JSON object consisting of an array of your requests. It returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array, and an optional body (which is a JSON encoded string).

To make a batched request, send a `POST` request to an endpoint where the `batch` parameter is your JSON object.

```
POST /ENDPOINT?batch=[JSON-OBJECT]
```
**Sample Batch Request**

In this example, we are getting information about two Pages that our app manages.

*Formatted for readability.*
```
curl -i -X POST 'https://graph.facebook.com/me?batch=  
  [
    {
      "method":"GET",
      "relative_url":"PAGE-A-ID"
    },  
    {
      "method":"GET",
      "relative_url":"PAGE-B-ID"
    }
  ]
  &include_headers=false             // Included to remove header information
  &access_token=ACCESS-TOKEN'
```
Once all operations are complete, a response is sent with the result of each operation. Because the headers returned can sometimes be much larger than the actual API response, you might want to remove them for efficiency. To include header information, remove the `include_headers` parameter or set it to `true`.

**Sample Response**

The body field contains a string encoded JSON object:

```
[
  {
    "code": 200,
    "body": "{
      \"name\": \"Page A Name\",
      \"id\": \"PAGE-A-ID\"
      }"
  },
  {
    "code": 200,
    "body": "{
      \"name\": \"Page B Name\",
      \"id\": \"PAGE-B-ID\"
      }"
  }
]
```
Complex Batch Requests
----------------------

It is possible to combine operations that would normally use different HTTP methods into a single batch request. While `GET` and `DELETE` operations can only have a `relative_url` and a `method` field, `POST` and `PUT` operations may contain an optional `body` field. The body should be formatted as a raw HTTP POST string, similar to a URL query string.

**Sample Request**

The following example publishes a post to a Page we manage and have publish permissions and then the Page's feed in a single operation:

```
curl "https://graph.facebook.com/PAGE-ID?batch=
  [
    { 
      "method":"POST",
      "relative_url":"PAGE-ID/feed",
      "body":"message=Test status update"
    },
    { 
      "method":"GET",
      "relative_url":"PAGE-ID/feed"
    }
  ]
  &access_token=ACCESS-TOKEN"
```
The output of this call would be:

```
[
    { "code": 200,
      "headers": [
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"}
       ],
      "body":"{\"id\":\"…\"}"
    },
    { "code": 200,
      "headers": [
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"
          },
          { "name":"ETag", 
            "value": "…"
          }
      ],
      "body": "{\"data\": [{…}]}
    }
]
```
The following example creates a new ad for a campaign, and then gets the details of the newly created object. Note the **URLEncoding** for the body param:

```
curl \
-F 'access_token=...' \
-F 'batch=[
  {
    "method":"POST",
    "name":"create-ad",
    "relative_url":"11077200629332/ads",
    "body":"ads=%5B%7B%22name%22%3A%22test_ad%22%2C%22billing_entity_id%22%3A111200774273%7D%5D"
  }, 
  {
    "method":"GET",
    "relative_url":"?ids={result=create-ad:$.data.*.id}"
  }
]' \
https://graph.facebook.com
```
The following example adds multiple pages to a Business Manager:

```
curl \
-F 'access_token=<ACCESS_TOKEN>' \
-F 'batch=[
  {
    "method":"POST",
    "name":"test1",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_1>"
  }, 
  {
    "method":"POST",
    "name":"test2",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_2>"
  }, 
  {
    "method":"POST",
    "name":"test3",
    "relative_url":"<BUSINESS_ID>/owned_pages",
    "body":"page_id=<PAGE_ID_3>"
  }, 
]' \
"https://graph.facebook.com/v12.0"
```
Where:

* `<ACCESS_TOKEN>` is an access token with the `business_management` permission.
* `<BUSINESS_ID>` is the ID of the Business Manager to which the pages should be claimed.
* `<PAGE_ID_n>` are the Page IDs to be claimed.

Errors
------

Its possible that one of your requested operations may throw an error. This could be because, for example, you don't have permission to perform the requested operation. The response is similiar to the standard Graph API, but encapsulated in the batch response syntax:

```
[
    { "code": 403,
      "headers": [
          {"name":"WWW-Authenticate", "value":"OAuth…"},
          {"name":"Content-Type", "value":"text/javascript; charset=UTF-8"} ],
      "body": "{\"error\":{\"type\":\"OAuthException\", … }}"
    }
]
```
Other requests within the batch should still complete successfully and will be returned, as normal, with a `200` status code.

Timeouts
--------

Large or complex batches may timeout if it takes too long to complete all the requests within the batch. In such a circumstance, the result is a partially-completed batch. In a partially-completed batch, requests that are completed successful will return the normal output with the `200` status code. Responses for requests that are not successful will be `null`. You can retry any unsuccessful request.

Batch calls with JSONP
----------------------

The Batch API supports JSONP, just like the rest of the Graph API - the JSONP callback function is specified using the `callback` query string or form post parameter.

Using Multiple Access Tokens
----------------------------

Individual requests of a single batch request can specify its own access tokens as a query string or form post parameter. In that case the top level access token is considered a fallback token and is used if an individual request has not explicitly specified an access token.

This may be useful when you want to query the API using several different User or Page access tokens, or if some of your calls need to be made using an app access token.

You must include an access token as a top level parameter, even when all individual requests contain their own tokens.

Upload Binary Data
------------------

You can upload multiple binary items as part of a batch call. In order to do this, you need to add all the binary items as multipart/mime attachments to your request, and need each operation to reference its binary items using the `attached_files` property in the operation. The `attached_files` property can take a comma separated list of attachment names in its value.

The following example shows how to upload 2 photos in a single batch call:

```
curl 
     -F 'access_token=…' \
     -F 'batch=[{"method":"POST","relative_url":"me/photos","body":"message=My cat photo","attached_files":"file1"},{"method":"POST","relative_url":"me/photos","body":"message=My dog photo","attached_files":"file2"},]' \
     -F 'file1=@cat.gif' \
     -F 'file2=@dog.jpg' \
    https://graph.facebook.com
```

 -->