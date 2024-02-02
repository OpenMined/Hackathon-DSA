Paginated Results - Graph API - Documentation - Meta for Developers

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
Paginated Results
=================

We cover the basics of Graph API terminology and structure in the Graph API overview. This document goes into more detail about the results from your API requests.

Traversing Paged Results
------------------------

When making an API request to a node or edge, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.

### Cursor-based Pagination

Cursor-based pagination is the most efficient method of paging and should always be used when possible. A cursor refers to a random string of characters which marks a specific item in a list of data. The cursor will always point to the item, however it will be invalidated if the item is deleted or removed. Therefore, your app shouldn't store cursors or assume that they will be valid in the future.

When reading an edge that supports cursor pagination, you see the following JSON response:

```
{
  "data": [
     ... Endpoint data is here
  ],
  "paging": {
    "cursors": {
      "after": "MTAxNTExOTQ1MjAwNzI5NDE=",
      "before": "NDMyNzQyODI3OTQw"
    },
    "previous": "https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw"
    "next": "https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE="
  }
}
```
A cursor-paginated edge supports the following parameters:

* `before` : This is the cursor that points to the start of the page of data that has been returned.
* `after` : This is the cursor that points to the end of the page of data that has been returned.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.

Don't store cursors. Cursors can quickly become invalid if items are added or deleted.

### Time-based Pagination

Time pagination is used to navigate through results data using Unix timestamps which point to specific times in a list of data.

When using an endpoint that uses time-based pagination, you see the following JSON response:

```
{
  "data": [
     ... Endpoint data is here
  ],
  "paging": {
    "previous": "https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754",
    "next": "https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774"
  }
}
```
A time-paginated edge supports the following parameters:

* `until` : A Unix timestamp or `strtotime` data value that points to the end of the range of time-based data.
* `since` : A Unix timestamp or `strtotime` data value that points to the start of the range of time-based data.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data.
* `previous` : The Graph API endpoint that will return the previous page of data.

For consistent results, specify both `since` and `until` parameters. Also, it is recommended that the time difference is a maximum of 6 months.

### Offset-based Pagination

Offset pagination can be used when you do not care about chronology and just want a specific number of objects returned. Only use this if the edge does not support cursor or time-based pagination.

An offset-paginated edge supports the following parameters:

* `offset` : This offsets the start of each page by the number specified.
* `limit` : This is the maximum number of objects that *may* be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.

Note that if new objects are added to the list of items being paged, the contents of each offset-based page will change.

Offset based pagination is not supported for all API calls. To get consistent results, we recommend you to paginate using the previous/next links we return in the response.

For objects that have many items returned, such as comments which can number in the tens of thousands, you may encounter limits while paging. The API will return an error when your app has reached the cursor limit:

```
{
  "error": {
    "message": "(#100) The After Cursor specified exceeds the max limit supported by this endpoint",
    "type": "OAuthException",
    "code": 100
  }
}
```
Next Steps
----------

Now that you are more familiar with the Graph API visit our Graph Explorer Tool Guide to explore the Graph without writing code, Common Uses to view the most common tasks performed, and the SDKs available.