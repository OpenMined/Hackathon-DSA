If you are a Facebook user and are having trouble signing into your account, visit our [Help Center](https://www.facebook.com/help/1573156092981768/).

Graph API
=========

|     |     |
| --- | --- |
| **The latest version is**: | `v18.0` |

The Graph API is the primary way for apps to read and write to the Facebook social graph. All of our SDKs and products interact with the Graph API in some way, and our other APIs are extensions of the Graph API, so understanding how the Graph API works is crucial.

If you are unfamiliar with the Graph API, we recommend that you start with these documents:

1. [Overview](https://developers.facebook.com/docs/graph-api/overview) – Learn how the Graph API is structured, and how it works.
2. [Get Started](https://developers.facebook.com/docs/graph-api/get-started) – Explore the Graph API endpoints using the Graph API Explorer tool and run your first request.
3. [Batch requests](https://developers.facebook.com/docs/graph-api/batch-requests) – Learn how to send multiple API requests in one call.
4. [Debug requests](https://developers.facebook.com/docs/graph-api/guides/debugging) – Learn how to debug API requests.
5. [Handle errors](https://developers.facebook.com/docs/graph-api/guides/error-handling) – Learn how to handle common errors encountered when using the Graph API.
6. [Field expansion](https://developers.facebook.com/docs/graph-api/guides/field-expansion) – Learn how to limit the number of objects returned in a request and perform nested requests.
7. [Secure requests](https://developers.facebook.com/docs/graph-api/guides/secure-requests) – Learn how to make secure requests to the Graph API.
8. [Resumable Uploads API](https://developers.facebook.com/docs/graph-api/guides/upload) – Learn how to upload files to the Graph API.

#### [Reference](https://developers.facebook.com/docs/graph-api/reference)

Learn how to read our reference documents so you can easily find what you're looking for.

Where to Start
--------------

We strongly recommend you start with the [**Graph API Overview**](https://developers.facebook.com/docs/graph-api/overview) to learn the structure of the Facebook Social Graph.

[](#)

[](#)

Overview
========

The Graph API is the primary way to get data into and out of the Facebook platform. It's an HTTP-based API that apps can use to programmatically query data, post new stories, manage ads, upload photos, and perform a wide variety of other tasks.

The Graph API is named after the idea of a "social graph" — a representation of the information on Facebook. It's composed of nodes, edges, and fields. Typically you use nodes to get data about a specific object, use edges to get collections of objects on a single object, and use fields to get data about a single object or each object in a collection. Throughout our documentation, we may refer to both a node and edge as an "endpoint". For example, "send a `GET` request to the User endpoint".

HTTP
----

All data transfers conform to HTTP/1.1, and all endpoints require HTTPS. Because the Graph API is HTTP-based, it works with any language that has an HTTP library, such as cURL and urllib. This means you can use the Graph API directly in your browser. For example, requesting this URL in your browser...

[https://graph.facebook.com/facebook/picture?redirect=false](https://graph.facebook.com/facebook/picture?redirect=false)

... is equivalent to performing this cURL request:

curl \-i \-X GET "https://graph.facebook.com/facebook/picture?redirect=false"

We have also enabled the `includeSubdomains` HSTS directive on `facebook.com`, but this should not adversely affect your Graph API calls.

[](#)

Host URL
--------

Almost all requests are passed to the `graph.facebook.com` host URL. The single exception is video uploads, which use `graph-video.facebook.com`.

[](#)

Access Tokens
-------------

Access tokens allow your app to access the Graph API. Almost all Graph API endpoints require an access token of some kind, so each time you access an endpoint, your request may require one. They typically perform two functions:

* They allow your app to access a User's information without requiring the User's password. For example, your app needs a User's email to perform a function. If the User agrees to allow your app to retrieve their email address from Facebook, the User will not need to enter their Facebook password for your app to get their email address.
* They allow us to identify your app, the User who is using your app, and the type of data the User has permitted your app to access.

Visit our [access token documentation](https://developers.facebook.com/docs/facebook-login/access-tokens) to learn more.

[](#)

Nodes
-----

A node is an individual object with a unique ID. For example, there are many User node objects, each with a unique ID representing a person on Facebook. Pages, Groups, Posts, Photos, and Comments are just some of the nodes of the Facebook Social Graph.

The following cURL example represents a call to the User node.

curl \-i \-X GET \\
  "https://graph.facebook.com/USER-ID?access\_token=ACCESS-TOKEN"

This request would return the following data by default, formatted using JSON:

{
  "name": "Your Name",
  "id": "YOUR-USER-ID"
}

### Node Metadata

You can get a list of all fields, including the field name, description, and data type, of a node object, such as a User, Page, or Photo. Send a `GET` request to an object ID and include the `metadata=1` parameter:

curl \-i \-X GET \\
  "https://graph.facebook.com/USER-ID?
    metadata=1&access\_token=ACCESS-TOKEN"

The resulting JSON response will include the `metadata` property that lists all the supported fields for the given node:

{
  "name": "Jane Smith",
  "metadata": {
    "fields": \[
      {
        "name": "id",
        "description": "The app user's App-Scoped User ID. This ID is unique to the app and cannot be used by other apps.",
        "type": "numeric string"
      },
      {
        "name": "age\_range",
        "description": "The age segment for this person expressed as a minimum and maximum age. For example, more than 18, less than 21.",
        "type": "agerange"
      },
      {
        "name": "birthday",
        "description": "The person's birthday.  This is a fixed format string, like \`MM/DD/YYYY\`.  However, people can control who can see the year they were born separately from the month and day so this string can be only the year (YYYY) or the month + day (MM/DD)",
        "type": "string"
      },
...

[](#)

/me
---

The `/me` node is a special endpoint that translates to the object ID of the person or Page whose access token is currently being used to make the API calls. If you had a User access token, you could retrieve a User's name and ID by using:

curl \-i \-X GET \\
  "https://graph.facebook.com/me?access\_token=ACCESS-TOKEN"

[](#)

Edges
-----

An edge is a connection between two nodes. For example, a User node can have photos connected to it, and a Photo node can have comments connected to it. The following cURL example will return a list of photos a person has published to Facebook.

curl \-i \-X GET \\
  "https://graph.facebook.com/USER-ID/photos?access\_token=ACCESS-TOKEN"

Each ID returned represents a Photo node and when it was uploaded to Facebook.

    {
  "data": \[
    {
      "created\_time": "2017-06-06T18:04:10+0000",
      "id": "1353272134728652"
    },
    {
      "created\_time": "2017-06-06T18:01:13+0000",
      "id": "1353269908062208"
    }
  \],
}

[](#)

Fields
------

Fields are node properties. When you query a node, or an edge, it returns a set of fields by default, as the examples above show. However, you can specify which fields you want returned by using the `fields` parameter and listing each field. This overrides the defaults and returns only the fields you specify, and the ID of the object, which is always returned.

The following cURL request includes the `fields` parameter and the User's name, email, and profile picture.

curl \-i \-X GET \\
  "https://graph.facebook.com/USER-ID?fields=id,name,email,picture&access\_token=ACCESS-TOKEN"

#### Data Returned

{
  "id": "USER-ID",
  "name": "EXAMPLE NAME",
  "email": "EXAMPLE@EMAIL.COM",
  "picture": {
    "data": {
      "height": 50,
      "is\_silhouette": false,
      "url": "URL-FOR-USER-PROFILE-PICTURE",
      "width": 50
    }
  }
}

### Complex Parameters

Most parameter types are straightforward primitives such as `bool`, `string` and `int`, but there are also `list` and `object` types that can be specified in the request.

The `list` type is specified in JSON syntax, for example: `["firstitem", "seconditem", "thirditem"]`

The `object` type is also specified in JSON syntax, for example: `{"firstkey": "firstvalue", "secondKey": 123}`

[](#)

Publishing, Updating, and Deleting
----------------------------------

Visit our [Facebook Sharing guide](https://developers.facebook.com/docs/sharing) to learn how to publish to a User's Facebook or our [Pages API documentation](https://developers.facebook.com/docs/pages) to publish to a Page's Facebook feed.

Some nodes allow you to update fields with `POST` operations. For example, you could update your `email` field like this:

curl \-i \-X POST \\
  "https://graph.facebook.com/USER-ID?email=YOURNEW@EMAILADDRESS.COM&access\_token=ACCESS-TOKEN"

### Read-After-Write

For create and update endpoints, the Graph API can immediately read a successfully published or updated object and return any fields supported by the corresponding read endpoint.

By default, an ID of the object created or updated will be returned. To include more information in the response, include the `fields` parameter in your request and list the fields you want returned. For example, to publish the message “Hello” to a Page's feed, you could make the following request:

curl \-i \- X POST "https://graph.facebook.com/PAGE-ID/feed?message=Hello&
  fields=created\_time,from,id,message&access\_token=ACCESS-TOKEN"

_The above code example is formatted for readability._

This would return the specified fields as a JSON-formatted response, like this:

{
  "created\_time": "2017-04-06T22:04:21+0000",
  "from": {
    "name": "My Facebook Page",
    "id": "PAGE-ID"
  },
  "id": "POST\_ID",
  "message": "Hello",
}

Refer to each endpoint's [reference documentation](https://developers.facebook.com/docs/graph-api/reference) to see if it supports **read-after-write** and what fields are available.

#### Errors

If the read fails for any reason (for example, requesting a non-existent field), the Graph API will respond with a standard error response. Visit our [Handling Errors guide](https://developers.facebook.com/docs/graph-api/guides/error-handling) for more information.

You can usually delete a node, such as a Post or Photo node, by performing a DELETE operation on the object ID:

curl \-i \-X DELETE \\
  "https://graph.facebook.com/PHOTO-ID?access\_token=ACCESSS-TOKEN"

Usually you can only delete nodes that you created, but check each node's reference guide to see requirements for delete operations.

[](#)

Webhooks
--------

You can be notified of changes to nodes or interactions with nodes by subscribing to webhooks. See [Webhooks](https://developers.facebook.com/docs/graph-api/webhooks).

[](#)

Versions
--------

The Graph API has multiple versions with quarterly releases. You can specify the version in your calls by adding "v" and the version number to the start of the request path. For example, here's a call to version 4.0:

curl \-i \-X GET \\
  "https://graph.facebook.com/v4.0/USER-ID/photos
    ?access\_token=ACCESS-TOKEN"

If you do not include a version number we will default to the oldest available version, so it's recommended to include the version number in your requests.

You can read more about versions in our [Versioning guide](https://developers.facebook.com/docs/graph-api/guides/versioning) and learn about all available versions in the [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog).

[](#)

Facebook APIs, SDKs, and Platforms
----------------------------------

Connect interfaces and develop across platforms using Facebook's various [APIs, SDKs, and platforms](https://developers.facebook.com/docs#apis-and-sdks).

[](#)

Next Steps
----------

[**Get Started with Graph API**](https://developers.facebook.com/docs/graph-api/get-started) – Let's explore the Facebook Social Graph using the Graph Explorer tool and run a couple requests to get data.

[](#)

[](#)

Access Levels
=============

This document is only applicable to apps created using an App Type.

**[Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) now requires Business Verification**

As of February 1, 2023 apps requesting [advanced access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) for permissions may have to be connected to a verified business. [See this blog post for more information.](https://developers.facebook.com/blog/post/2023/02/01/developer-platform-requiring-business-verification-for-advanced-access/)

Access levels are an additional layer of Graph API authorization that apply to [permissions](https://developers.facebook.com/docs/permissions/reference) and [features](https://developers.facebook.com/docs/apps/features-reference) for [Business](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#business), [Consumer](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#consumer), and [Gaming](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#gaming-services) apps.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/130946061_668701493796906_1998528720072373367_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=8r2dyotWRwsAX_dseAb&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAhG_4UzPZPf_uMQ1XI-6nA5AF9byS9ZOcqS_Y83C1spw&oe=65CA0BA0)

There are two access levels: [Standard](#standard-access) and [Advanced](#advanced-access). Apps can request permissions with Advanced Access from any app user, and features with Advanced Access are active for all app users. Permissions with Standard Access, however, can only be requested from app users who have a role on the requesting app, and features with Standard Access are only active for app users who have a role on the app.

If your app will only be used by people who have a role on it, the permissions and features your app requires will only need Standard Access. If your app will be used by people who do not have a role on it, the permissions and features that your app requires will need Advanced Access.

All Business, Consumer, and Gaming apps are automatically approved for Standard Access for all permissions and features. Advanced Access, however, must be approved on an individual permission and feature basis through the [App Review](https://developers.facebook.com/docs/app-review) process.

Standard Access
---------------

[Permissions](https://developers.facebook.com/docs/permissions/reference) with Standard Access can only be requested from app users who have a [role](https://developers.facebook.com/docs/development/build-and-test/app-roles) on the requesting app. Similarly, [features](https://developers.facebook.com/docs/apps/features-reference) with Standard Access are only active for app users who have a role on the app.

[Business](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#business), [Consumer](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#consumer), and [Gaming](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/app-types#gaming-services) apps are automatically approved for Standard Access for all permissions and features available to their app type.

Standard Access is intended for apps that will only be used by people who have roles on them, or used during app development, when testing API endpoints that the calling app has not been approved for.

[](#)

Advanced Access
---------------

[Permissions](https://developers.facebook.com/docs/permissions/reference) with Advanced Access can be requested from any app user, and [features](https://developers.facebook.com/docs/apps/features-reference) with Advanced Access are active for all app users. However, [Business Verification](https://developers.facebook.com/docs/development/release/business-verification) is required to get Advanced Access. In some cases additional [App Review](https://developers.facebook.com/docs/app-review) on an individual permission and feature basis might be required.

### Automatic Approval

Business and Gaming apps created before February 16, 2021 were automatically approved for Advanced Access for the [email](https://developers.facebook.com/docs/permissions/reference/email) and [public\_profile](https://developers.facebook.com/docs/permissions/reference/public_profile) permissions, as well as any permissions or features that were already approved through App Review, if they were using them.

All newly created Consumer apps are automatically approved for Advanced Access for the email and public\_profile permissions. However, both permissions are set to Standard Access by default and must be manually switched to Advanced Access. In addition, consumer apps must be in Live mode before they can request permissions with Advanced Access from non-role app users, and before features with Advanced Access will be active for non-role users.

[](#)

Data Use Checkup
----------------

Apps that have Advanced Access for a permission or feature must complete [Data Use Checkup](https://developers.facebook.com/docs/development/maintaining-data-access/data-use-checkup/), which is an annual process to certify that the app accesses Facebook APIs, products, and data in compliance with our [Platform Terms](https://developers.facebook.com/terms) and [Developer Policies](https://developers.facebook.com/devpolicy).

[](#)

Remove Access
-------------

If you want to signify that your app does not need a specific permission or feature, you can remove it by clicking the trash can icon alongside the permission or feature in the **App Review** > **Permissions and Features** panel. You can restore access to a removed permission or feature by searching for it again in the same panel and clicking its **Get Standard Access** button or **Get Advanced Access** button. Restoring Advanced Access to previously approved permissions or features does not require re-review.

All permissions and features can be removed except for [public\_profile](https://developers.facebook.com/docs/permissions/reference/public_profile).

[](#)

Changing Access Levels
----------------------

App administrators can change access levels for individual permissions and features. Restoring Advanced Access to permissions and features does not require [re-review](https://developers.facebook.com/docs/app-review), but changing from Advanced to Standard will invalidate/deactivate any permission/feature for any app users who do not have a role on your app.

[](#)

[](#)

The Facebook SDKs
=================

Facebook SDKs have built-in methods and objects to get data in and out of the Meta social graph.

Available SDKs
--------------

* [Meta Business SDK](https://developers.facebook.com/docs/business-sdk)
    
* [Facebook SDK for Android](https://developers.facebook.com/docs/android)
    
* [Facebook SDK for iOS](https://developers.facebook.com/docs/ios)
    
* [Facebook SDK for JavaScript](https://developers.facebook.com/docs/javascript)
    
* [Facebook SDK for PHP](https://l.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Ffacebookarchive%2Fphp-graph-sdk&h=AT3pz5sApos5j3FcPjarLsC2bg0e8zJK_T_dXFyvwr9Lx3xNVfQYLxfKzuBACg5oxv7tL2jbRLHxM-e7-JN8HuoEmMfL1IZ-16pd8XtVnPWsyJlw5Wgh5NbwDhWI99g3SV7WVDfnq5I6ZMFIaqHXsg)
    
* [Facebook SDK for tvOS](https://developers.facebook.com/docs/tvos)
    
* [Facebook SDK for Unity](https://developers.facebook.com/docs/unity)
    

[](#)

Paginated Results
=================

We cover the basics of Graph API terminology and structure in the [Graph API overview](https://developers.facebook.com/docs/graph-api/overview). This document goes into more detail about the results from your API requests.

Traversing Paged Results
------------------------

When making an API request to a node or edge, you usually don't receive all of the results of that request in a single response. This is because some responses could contain thousands of objects so most responses are paginated by default.

### Cursor-based Pagination

Cursor-based pagination is the most efficient method of paging and should always be used when possible. A cursor refers to a random string of characters which marks a specific item in a list of data. The cursor will always point to the item, however it will be invalidated if the item is deleted or removed. Therefore, your app shouldn't store cursors or assume that they will be valid in the future.

When reading an edge that supports cursor pagination, you see the following JSON response:

{
  "data": \[
     ... Endpoint data is here
  \],
  "paging": {
    "cursors": {
      "after": "MTAxNTExOTQ1MjAwNzI5NDE=",
      "before": "NDMyNzQyODI3OTQw"
    },
    "previous": "https://graph.facebook.com/{your-user-id}/albums?limit=25&before=NDMyNzQyODI3OTQw"
    "next": "https://graph.facebook.com/{your-user-id}/albums?limit=25&after=MTAxNTExOTQ1MjAwNzI5NDE="
  }
}

A cursor-paginated edge supports the following parameters:

* `before` : This is the cursor that points to the start of the page of data that has been returned.
* `after` : This is the cursor that points to the end of the page of data that has been returned.
* `limit` : This is the maximum number of objects that _may_ be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.

Don't store cursors. Cursors can quickly become invalid if items are added or deleted.

### Time-based Pagination

Time pagination is used to navigate through results data using Unix timestamps which point to specific times in a list of data.

When using an endpoint that uses time-based pagination, you see the following JSON response:

{
  "data": \[
     ... Endpoint data is here
  \],
  "paging": {
    "previous": "https://graph.facebook.com/{your-user-id}/feed?limit=25&since=1364849754",
    "next": "https://graph.facebook.com/{your-user-id}/feed?limit=25&until=1364587774"
  }
}

A time-paginated edge supports the following parameters:

* `until` : A Unix timestamp or [`strtotime`](https://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php&h=AT3bTaGcI6fbO-u6Y1yb0JLCpYjHB1G2aB8JDis8fAzMGAca4ER7LEhW5JwTeO4IcE4V_4_ZuRDvp3RyDF5Y-LQMnt_dFFbCAQIGSUPN8gDnvFfLyExbQfIbem96xIY7FkiZipIn--8WoWEiLKlMvA) data value that points to the end of the range of time-based data.
* `since` : A Unix timestamp or [`strtotime`](https://l.facebook.com/l.php?u=http%3A%2F%2Fphp.net%2Fmanual%2Fen%2Ffunction.strtotime.php&h=AT3HdxNjInavkuGRCLvz_Dh-B_Qo-Vp9WAfP_bs9CXDoNVNHVZTNAH7xVwapSvdJshbKry1NNUx6W8MmQCttV9QqQfZUdIMNhVC4IwEIAUc3-Npj36LUvVAvY4ZMSh3dNU8il6Akd8hUhRInvoYYdQ) data value that points to the start of the range of time-based data.
* `limit` : This is the maximum number of objects that _may_ be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data.
* `previous` : The Graph API endpoint that will return the previous page of data.

For consistent results, specify both `since` and `until` parameters. Also, it is recommended that the time difference is a maximum of 6 months.

### Offset-based Pagination

Offset pagination can be used when you do not care about chronology and just want a specific number of objects returned. Only use this if the edge does not support cursor or time-based pagination.

An offset-paginated edge supports the following parameters:

* `offset` : This offsets the start of each page by the number specified.
* `limit` : This is the maximum number of objects that _may_ be returned. A query may return fewer than the value of `limit` due to filtering. Do not depend on the number of results being fewer than the `limit` value to indicate that your query reached the end of the list of data, use the absence of `next` instead as described below. For example, if you set `limit` to 10 and 9 results are returned, there may be more data available, but one item was removed due to privacy filtering. Some edges may also have a maximum on the `limit` value for performance reasons. In all cases, the API returns the correct pagination links.
* `next` : The Graph API endpoint that will return the next page of data. If not included, this is the last page of data. Due to how pagination works with visibility and privacy, it is possible that a page may be empty but contain a `next` paging link. Stop paging when the `next` link no longer appears.
* `previous` : The Graph API endpoint that will return the previous page of data. If not included, this is the first page of data.

Note that if new objects are added to the list of items being paged, the contents of each offset-based page will change.

Offset based pagination is not supported for all API calls. To get consistent results, we recommend you to paginate using the previous/next links we return in the response.

For objects that have many items returned, such as [comments](https://developers.facebook.com/docs/graph-api/reference/object/comments) which can number in the tens of thousands, you may encounter limits while paging. The API will return an error when your app has reached the cursor limit:

{
  "error": {
    "message": "(#100) The After Cursor specified exceeds the max limit supported by this endpoint",
    "type": "OAuthException",
    "code": 100
  }
}

[](#)

Next Steps
----------

Now that you are more familiar with the Graph API visit our [Graph Explorer Tool Guide](https://developers.facebook.com/docs/graph-api/explorer) to explore the Graph without writing code, [Common Uses](https://developers.facebook.com/docs/graph-api/using-graph-api/common-scenarios) to view the most common tasks performed, and [the SDKs available](https://developers.facebook.com/docs/graph-api/using-graph-api/using-with-sdks).

[](#)

[](#)

Rate Limits
===========

A rate limit is the number of API calls an app or user can make within a given time period. If this limit is exceeded or if CPU or total time limits are exceeded, the app or user may be throttled. API requests made by a throttled user or app will fail.

All API requests are subject to rate limits. Graph API and [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) requests are subject to [Platform Rate Limits](#platform-rate-limits), while [Marketing API](https://developers.facebook.com/docs/marketing-api/) and [Instagram Graph API](https://developers.facebook.com/docs/instagram-graph-api) requests are subject to [Business Use Case (BUC) Rate Limits](#buc-rate-limits).

Pages API requests are subject to either Platform or BUC Rate Limits, depending on the token used in the request; requests made with [application](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) or [user access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) are subject to Platform Rate Limits, while requests made with [system user](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser#generate-token) or [page access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) are subject to Business Use Case Rate Limits.

Real time rate limit usage statistics are described in headers that are included with most API responses once enough calls have been made to an endpoint. Platform Rate Limit usage statistics are also displayed in the [App Dashboard](https://developers.facebook.com/apps/). Once a rate limit is reached, any subsequent requests made by your app will fail and the API will return an error code until enough time has passed for the call count to drop below the limit.

If both Platform and Business Use Case rate limits can be applied to a request, BUC rate limits will be applied.

Platform Rate Limits
--------------------

Platform Rate Limits are tracked on an individual application or user level, depending on the type of token used in the request.

### Applications

Graph API requests made with an [application access token](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) are counted against that app’s rate limit. An app’s call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

`Calls within one hour = 200 * Number of Users`

The Number of Users is based on the number of unique daily active users an app has. In cases where there are slow periods of daily usage, such as if your app has high activity on weekends but low activity over weekdays, the weekly and monthly active Users are used to calculate the number of Users for your app. Apps with high daily engagement will have higher rate limits than apps with low daily engagement, regardless of the actual number of app installs.

Note that this is not a per User limit but a limit on calls made by your app. Any individual User can make more than 200 calls per hour using your app, as long as the total calls from your app does not exceed the app maximum. For example, if your app has 100 Users, your app can make 20,000 calls per hour. However, your top ten most engaged Users could make 19,000 of those calls.

### Users

Graph API requests made with a [user access token](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) are counted against that user’s call count. A user’s call count is the number of calls a user can make during a rolling one hour window. Due to privacy concerns, we do not reveal actual call count values for users.

Note that a user’s call count can be spread over multiple apps. For example, a user could make X calls through App1 and Y calls through App2. If X+Y exceeds the user’s call count that user will be rate limited. This does not necessarily mean that any app is doing something wrong; it could be that the user is using multiple apps or is misusing the API.

### Headers

Endpoints that receive enough requests from your app will include a `X-App-Usage` or `X-Ad-Account-Usage` (for v3.3 and older Ads API calls) HTTP header in their responses. The header will contain a JSON-formatted string that describes current application rate limit usage.

#### Header Contents

  

| Key | Value Description |
| --- | --- |
| `call_count` | A whole number expressing the percentage of calls made by your app over a rolling one hour period. |
| `total_cputime` | A whole number expressing the percentage of CPU time allotted for query processing. |
| `total_time` | A whole number expressing the percentage of total time allotted for query processing. |

#### X-Ad-Account-Usage Header Contents

| Key | Value Description |
| --- | --- |
| `acc_id_util_pct` | The percentage of calls made for this ad account before the rate limit is reached. |
| `reset_time_duration` | Time duration (in seconds) it takes to reset the current rate limit to 0. |
| `ads_api_access_tier` | Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature. |

#### Total CPU Time

The amount of CPU time the request takes to process. When `total_cputime` reaches 100, calls may be throttled.

#### Total Time

The length of time the request takes to process. When `total_time` reaches 100, calls may be throttled.

#### Sample X-App-Usage Header Value

x\-app\-usage: {
    "call\_count": 28,         //Percentage of calls made 
    "total\_time": 25,         //Percentage of total time
    "total\_cputime": 25       //Percentage of total CPU time
}

#### Sample X-Ad-Account-Usage Header Value

x\-ad\-account\-usage: {
    "acc\_id\_util\_pct": 9.67,   //Percentage of calls made for this ad account.
    "reset\_time\_duration": 100,   //Time duration (in seconds) it takes to reset the current rate limit score.
    "ads\_api\_access\_tier": 'standard\_access'   //Tiers allows your app to access the Marketing API. standard\_access enables lower rate limiting.
}

### Dashboard

The [app dashboard](https://developers.facebook.com/apps/) displays the number of rate limited app users, the app’s current Application Rate Limits usage percentage, and displays average activity for the past 7 days. In the **Application Rate Limit** card, click **View Details** and hover over any point on the graph to see more details about usage for that particular moment. Because usage depends on call volume, this graph may not show a full 7 days. Apps with a higher volume of calls will show more days.

### Error Codes

When an app or user has reached their rate limit, requests made by that app or user will fill and the API will respond with an error code.

#### Throttle Error Codes

  

| Error Code | Description |
| --- | --- |
| `4` | Indicates that the app whose token is being used in the request has reached its rate limit. |
| `17` | Indicates that the User whose token is being used in the request has reached their rate limit. |
| `17 with subcode 2446079` | Indicates that the token being used in the Ads API v3.3 or older request has reached its rate limit. |
| `32` | Indicates that the User or app whose token is being used in the Pages API request has reached its rate limit. |
| `613` | Indicates that a custom rate limit has been reached. To help resolving this issue, visit the supporting docs for the specific API you are calling for custom rate limits that may be applied. |
| `613 with subcode 1996` | Indicates that we have noticed inconsistent behavior in the API request volume of your app. If you have made any recent changes that affect the number of API requests, you may be encountering this error. |

#### Sample Response

{
  "error": {
    "message": "(#32) Page request limit reached",
    "type": "OAuthException",
    "code": 32,
    "fbtrace\_id": "Fz54k3GZrio"
  }
}

### Facebook Stability Throttle Codes

  

| Error Code | Description |
| --- | --- |
| `throttled` | Whether the query is throttled or not. Values: `True`, `False` |
| `backend_qps` | First throttling factor `backend_qps`. Supported values:<br><br>* `actual_score`—Actual `backend_qps` of this app. Value: `8`<br>* `limit`—`backend_qps` limit of this app. Value: `5`<br>* `more_info`—Queries need a large number of backend requests to handle. We suggest to send fewer queries or simplify queries with narrower time ranges, fewer object IDs, and so on. |
| `complexity_score` | Second throttling factor `complexity_score`. Supported values:<br><br>* `actual_score`—Actual `complexity_score` of this app. Value: `0.1`<br>* `limit`—`complexity_score` limit of this app. Value: `0.01`<br>* `more_info`—High `complexity_score` means your queries are very complex and request large amounts of data. We suggest to simplify queries with shorter time ranges, fewer object IDs, metrics or breakdowns, and so on. Split large, complex queries into multiple smaller queries and space them out. |

### Best Practices

* When the limit has been reached, stop making API calls. Continuing to make calls will continue to increase your call count, which will increase the time before calls will be successful again.
    
* Spread out queries evenly to avoid traffic spikes.
    
* Use filters to limit the data response size and avoid calls that request overlapping data.
    
* Check the `X-App-Usage` HTTP header to see how close your app is to its limit and when you can resume making calls when the limit has been reached.
    
* If Users are being throttled, be sure your app is not the cause. Reduce the user’s calls or spread the user’s calls more evenly over time.
    

[](#)

Business Use Case Rate Limits
-----------------------------

All Marketing API requests, and Pages API requests made with a system or page access token, are subject to Business Use Case (BUC) Rate Limits, and depend on the endpoints you are querying.

For Marketing API, the rate limit is applied to the ad account across the same Business Use Case. For example, all endpoints with the Ads Management business use case will share the total quota within the same ad account. If a certain endpoint makes a lot of API requests and causes throttling, other endpoints configured with the same business use case will also receive rate limiting errors. The quota depends on the app's Marketing API Access Tier. The standard access Marketing API tier will have more quotas than the development access Marketing API tier. By default, an new app should be on the development tier. If you need to upgrade to get more rate limiting quota, upgrade to Advanced Access of [Ads Management Standard Access](https://developers.facebook.com/docs/features-reference/ads-management-standard-access/) in App Review.

|     |     |
| --- | --- |
| * [Ad Insights](#ads-insights)<br>* [Ads Management](#ads-management)<br>* [Catalog](#catalog)<br>* [Custom Audience](#custom-audience)<br>* [Instagram Graph API](#instagram-graph-api)<br>* [Lead Generation](#leadgen) | * [Messenger](#messenger)<br>* [Pages](#pages)<br>* [Spark AR Commerce Effect Management](#spark-ar)<br>* [WhatsApp Business Management API](#wa-biz-api) |

### Ads Insights

Requests made by your app to the Ads Insights API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access) to the Ads Management Standard Access feature:

`Calls within one hour = 600 + 400 * Number of Active ads - 0.001 * User Errors`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 190000 + 400 * Number of Active ads - 0.001 * User Errors`

The Number of Active ads is the number of ads currently running per ad account. User Errors is the number of errors received when calling the API. To get a higher rate limit, you can apply for the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.

### Ads Management

Requests made by your app to the Ads Management API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access)to the Ads Management Standard Access feature:

`Calls within one hour = 300 + 40 * Number of Active ads`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 100000 + 40 * Number of Active ads`

The Number of Active Ads is the number of ads for each ad account.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.

### Catalog

#### Catalog Batch

Requests made by your app are counted against the rate limit metrics such as call count, total CPU time and total time your app can make in a rolling one hour period per each catalog ID and is calculated as follows:

`Calls within one hour = 200 + 200 * log2(unique users)`

The unique users is a number of unique users of the business (on all catalogs) with intent in the last 28 days. The more users see products from your catalogs, the more call quota is allocated.

| Type of Call | Endpoint |
| --- | --- |
| POST | /{catalog\_id}/items\_batch |
| POST | /{catalog\_id}/localized\_items\_batch |
| POST | /{catalog\_id}/batch |

#### Catalog Management

Requests made by your app are counted against the number of calls your app can make in a rolling one hour period per each catalog ID and is calculated as follows:

`Calls within one hour = 20,000 + 20,000 * log2(unique users)`

The unique users is a number of unique users of the business (on all catalogs) with intent in the last 28d. The more users see products from your catalogs, the more call quota is allocated.

This formula is applied on various catalog endpoints.

For more information on how to get your current rate usage, see [Headers](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers).

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.

### Custom Audience

Requests made by your app to the Custom Audience API are counted against the app's rate limit metrics such as call count, total CPU time and total time. An app's call count is the number of calls it can make during a rolling one hour window and is calculated as follows but will never exceed 700000:

For apps with [Standard Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#standard-access) to the Ads Management Standard Access feature:

`Calls within one hour = 5000 + 40 * Number of Active Custom Audiences`

For apps with [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels/#advanced-access) to the Ads Management Standard Access feature:

`Calls within one hour = 190000 + 40 * Number of Active Custom Audiences`

The Number of Active Custom Audiences is the number of active [custom audiences](https://developers.facebook.com/docs/marketing-api/audiences-api) for each ad account.

Rate limiting may also be subject to the total CPU time and total wall time during a rolling one hour window. For more details, check the HTTP [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header `total_cputime` and `total_time`.

If you are receiving rate limiting errors, you can also refer to `estimated_time_to_regain_access` in the [`X-Business-Use-Case`](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers-2) header for the estimated blocking time.

### Instagram Graph API

Calls to the [Instagram Graph API](https://developers.facebook.com/docs/instagram-api) are counted against the calling app's call count. An app's call count is unique for each app and app user pair, and is the number of calls the app has made in a rolling 24 hour window. It is calculated as follows:

`Calls within 24 hours = 4800 * Number of Impressions`

The Number of Impressions is the number of times any content from the app user's Instagram account has entered a person's screen within the last 24 hours.

#### Notes

* The [Instagram Basic Display API](https://developers.facebook.com/docs/instagram-basic-display-api) uses [Platform Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).
* [Business Discovery](https://developers.facebook.com/docs/instagram-api/guides/business-discovery) and [Hashtag Search](https://developers.facebook.com/docs/instagram-api/guides/hashtag-search) are subject to [Platform Rate Limits](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits).

### LeadGen

Requests made by your app to the LeadGen API are counted against the app’s call count. An app’s call count is the number of calls it can make during a rolling 24 hour window and is calculated as follows:

`Calls within 24 hours = 4800 * Leads Generated`

The Number of Leads Generated is the number of leads generated per Page for this Ad Account over the past 90 days.

### Messenger Platform

Rate limits for the Messenger Platform are dependent on the API used and, in some instances, the message content.

#### Messenger API

Requests made by your app are counted against the number of calls your app can make in a rolling 24 hour period and is calculated as follows:

`Calls within 24 hours = 200 * Number of Engaged Users`

The Number of Engaged Users is the number of people the business can message via Messenger.

#### Messenger API for Instagram

Requests made by your app are counted against the number of calls your app can make per Instagram Professional account and the API used.

**Conversations API**

* Your app can make 2 calls per second per Instagram Professional account

**Send API**

* Your app can make 100 calls per second per Instagram Professional account for messages that contain text, links, reactions, and stickers
* Your app can make 10 calls per second per Instagram Professional account for messages that contain audio or video content

**Private Replies API**

* Your app can make 100 calls per second per Instagram Professional account for private replies to Instagram Live comments
* Your app can make 750 calls per hour per Instagram Professional account for private replies to comments on Instagram posts and reels

[](#)

### Pages

The Page Rate Limits may use either the Platform or BUC rate limit logic depending on the type of token used. Any Pages API calls that are made using a [Page](https://developers.facebook.com/docs/facebook-login/access-tokens#pagetokens) or [system user access token](https://developers.facebook.com/docs/marketing-api/businessmanager/systemuser#systemusertoken) use the rate limit calculation below. Any calls made with [application](https://developers.facebook.com/docs/facebook-login/access-tokens#apptokens) or [user access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#usertokens) are subject to application or User rate limits.

Requests made by your app to the Pages API using a Page access token or system User access token are counted against the app’s call count. An app’s call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

`Calls within one hour = 4800 * Number of Engaged Users`

The Number of Engaged Users is the number of Users who engaged with the Page per 24 hours.

Requests made by your app to the Pages API using a User access token or App access token follow the [Platform Rate Limit logic](#platform-rate-limits).

To avoid [rate limiting](https://developers.facebook.com/docs/graph-api/overview/rate-limiting#pages) issues when using the [Page Public Access Content feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features), using a [system user access token](https://www.facebook.com/business/help/503306463479099) is recommended.

### Spark AR Commerce Effect Management

Requests made by your app to any Commerce endpoints are counted against the app’s call count. An app’s call count is the number of calls it can make during a rolling one hour window and is calculated as follows:

`Calls within one hour = 200 + 40 * Number of Catalogs`

The Number of Catalogs is the total number of catalogs across all commerce accounts managed by your app.

### WhatsApp Business Management API

Requests made by your app to the [WhatsApp Business Management API](https://developers.facebook.com/docs/whatsapp/business-management-api) are counted against your app’s count. An app’s call count is the number of calls it can make during a rolling one hour. For the following WhatsApp Business Management API, your app can make 200 calls per hour, per app, per WhatsApp Business Account (WABA) by default. For active WABAs with at least one registered phone number, your app can make 5000 calls per hour, per app, per active WABA.

| Type of Call | Endpoint |
| --- | --- |
| `GET` | `/{whatsapp-business-account-id}` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/assigned_users` |
| `GET` | `/{whatsapp-business-account-id}/phone_numbers` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/message_templates` |
| `GET`, `POST`, and `DELETE` | `/{whatsapp-business-account-id}/subscribed_apps` |
| `GET` | `/{whatsapp-business-account-to-number-current-status-id}` |

For the following [Credit Line APIs](https://developers.facebook.com/docs/whatsapp/embedded-signup/manage-accounts/share-and-revoke-credit-lines), your app can make 5000 calls per hour, per app.

| Type of Call | Endpoint |
| --- | --- |
| `GET` | `/{business-id}/extendedcredits` |
| `POST` | `/{extended-credit-id}/whatsapp_credit_sharing_and_attach` |
| `GET` and `DELETE` | `/{allocation-config-id}` |
| `GET` | `/{extended-credit-id}/owning_credit_allocation_configs` |

To avoid hitting rate limits, we recommend using [webhooks](https://developers.facebook.com/docs/graph-api/webhooks/getting-started/webhooks-for-whatsapp#setup) to keep track of status updates for message templates, phone numbers, and WABAs.  
  
For more information on how to get your current rate usage, see [Headers](https://developers.facebook.com/docs/graph-api/overview/rate-limiting/#headers).

### Headers

All API responses made by your app that are rate limited using the BUC logic include an `X-Business-Use-Case-Usage` (for v3.3 and older Ads API calls) HTTP header with a JSON-formatted string that describes current application rate limit usage. This header can return up to 32 objects in one call.

#### X-Business-Use-Case Usage Header Contents

| Error Code | Value Description |
| --- | --- |
| `business-id` | The ID of the business associated with the token making the API calls. |
| `call_count` | A whole number expressing the percentage of allowed calls made by your app over a rolling one hour period. |
| `estimated_time_to_regain_access` | Time, in minutes, until calls will not longer be throttled. |
| `total_cputime` | A whole number expressing the percentage of CPU time allotted for query processing. |
| `total_time` | A whole number expressing the percentage of total time allotted for query processing. |
| `type` | Type of rate limit applied. Value can be one of the following: `ads_insights`, `ads_management`, `custom_audience`, `instagram`, `leadgen`, `messenger`, or `pages`. |
| `ads_api_access_tier` | For `ads_insights` and `ads_management` types only. Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature. |

#### Total CPU Time

The amount of CPU time the request takes to process. When total\_cputime reaches 100, calls may be throttled.

#### Total Time

The length of time the request takes to process. When total\_time reaches 100, calls may be throttled.

#### Ads API Access Tier

For `ads_insights` and `ads_management` types only. Tiers allows your app to access the Marketing API. By default, apps are in the `development_access` tier. `Standard_access` enables lower rate limiting. To get a higher rate limit and get to the standard tier, you can apply for the "Advanced Access" to the [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/overview/authorization#layer-2--access-levels--permissions--and-features) feature.

#### Sample X-Business-Use-Case-Usage Header Value

x\-business\-use\-case\-usage: {
    "{business-object-id}": \[
        {
            "type": "{rate-limit-type}",           //Type of BUC rate limit logic being applied.
            "call\_count": 100,                     //Percentage of calls made. 
            "total\_cputime": 25,                   //Percentage of the total CPU time that has been used.
            "total\_time": 25,                      //Percentage of the total time that has been used.   
            "estimated\_time\_to\_regain\_access": 19,  //Time in minutes to regain access.
            "ads\_api\_access\_tier": "standard\_access"  //Tiers allows your app to access the Marketing API. standard\_access enables lower rate limiting.
        }
    \],      
    "66782684": \[
        {
            "type": "ads\_management",
            "call\_count": 95,
            "total\_cputime": 20,
            "total\_time": 20,
            "estimated\_time\_to\_regain\_access": 0,
            "ads\_api\_access\_tier": "development\_access" 
        }
    \],
    "10153848260347724": \[
        {
            "type": "ads\_insights",
            "call\_count": 97,
            "total\_cputime": 23,
            "total\_time": 23,
            "estimated\_time\_to\_regain\_access": 0,
            "ads\_api\_access\_tier": "development\_access"
        }
    \],
    "10153848260347724": \[
        {
            "type": "pages",
            "call\_count": 97,
            "total\_cputime": 23,
            "total\_time": 23,
            "estimated\_time\_to\_regain\_access": 0
        }
    \],
...
}

### Error Codes

When your app reaches its Business Use Case rate limit, subsequent requests made by your app will fail and the API will respond with an error code.

| Error Code | BUC Rate Limit Type |
| --- | --- |
| `error code 80000, error subcode 2446079` | Ads Insights |
| `error code 80004, error subcode 2446079` | Ads Management |
| `error code 80003, error subcode 2446079` | Custom Audience |
| `error code 80002` | Instagram |
| `error code 80005` | LeadGen |
| `error code 80006` | Messenger |
| `error code 32` | Page calls made with a User access token |
| `error code 80001` | Page calls made with a Page or System User access token |
| `error code 17, error subcode 2446079` | V3.3 and Older Ads API excluding Ads Insights |
| `error code 80008` | WhatsApp Business Management API |
| `error code 80014` | Catalog Batch |
| `error code 80009` | Catalog Management |

#### SampleError Code Message

{   
"error": {      
    "message": "(#80001) There have been too many calls to this Page account. Wait a bit and try again. For more info, please refer to https://developers.facebook.com/docs/graph-api/overview/rate-limiting.",      
    "type": "OAuthException",      
    "code": 80001,      
    "fbtrace\_id": "AmFGcW\_3hwDB7qFbl\_QdebZ"   
    }
}

### Best Practices

* When the limit has been reached, stop making API calls. Continuing to make calls will continue to increase your call count, which will increase the time before calls will be successful again.
* Check the `X-Business-Use-Case-Usage` HTTP header to see how close your ad account is to its limit and when you can resume making calls.
* Verify the error code and API endpoint to confirm the throttling type.
* Switch to other ad accounts and come back to this account later.
* It is better to create a new ad than to change existing ones.
* Spread out queries evenly between two time intervals to avoid sending traffic in spikes.
* Use filters to limit the data response size and avoid calls that request overlapping data.

[](#)

FAQ
---

#### What do we consider an API call?

All calls count towards the rate limits, not just individual API requests. For example, you can make a single API request specifying multiple IDs, but each ID counts as one API call.

The following table illustrates this concept.

| Example Request(s) | Number of API Calls |
| --- | --- |
| `GET https://graph.facebook.com/photos?ids=4`<br><br>`GET https://graph.facebook.com/photos?ids=5`<br><br>`GET https://graph.facebook.com/photos?ids=6` | 3   |
| `GET https://graph.facebook.com/photos?ids=4,5,6` | 3   |

We strongly recommend specifying multiple IDs in one API request when possible, as this improves performance of your API responses.

#### I'm building a scraper, is there anything else I should worry about?

If you are building a service that scrapes data, please read [our scraping terms](https://www.facebook.com/apps/site_scraping_tos_terms.php?hc_location=ufi).

[](#)

[](#)

Platform Versioning
===================

Facebook's Platform supports versioning so that app builders can roll out changes over time. This document explains how SDKs and APIs affected by versions and how to use those versions in your requests.

Versioning
----------

Not all APIs and SDKs share the same versioning system. For example, the Graph API is versioned with a different pace and numbering compared to the Facebook SDK for iOS. All Facebook SDKs support the ability to interact with different versions of our APIs. Multiple versions of APIs or SDKs can exist at the same time with different functionality in each version.

### What is the latest Graph API Version?

The latest Graph API version is `v18.0`

### Why do we have versions?

The goal for having versioning is for developers building apps to be able to understand in advance when an API or SDK might change. They help with web development, but are critical with mobile development because a person using your app on their phone may take a long time to upgrade (or may never upgrade).

Each version will remain for at least 2 years from release giving you a solid timeline for how long your app will remain working, and how long you have to update it to newer versions.

### Version Schedules

Each version is guaranteed to operate for at least two years. **A version will no longer be usable two years after the date that the subsequent version is released.** For example, if API version v2.3 is released on March 25th, 2015 and API version v2.4 is released August 7th, 2015 then v2.3 would expire on August 7th, 2017, two years after the release of v2.4.

For APIs, once a version is no longer usable, any calls made to it will be defaulted to the next oldest, usable version. Here is a timeline example:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2178-6/10333112_605697729514600_969655318_n.png?_nc_cat=106&ccb=1-7&_nc_ohc=saSXtnTXdQkAX_aXEBr&_nc_ht=scontent-cdg4-3.xx&stp=dst-emg0_q75&ur=34156e&_nc_sid=a284aa&oh=00_AfAlaCEeCem6W5wbLhbnVTJWyW9ij4GhQ9GBhgzq7wPdrQ&oe=65B4388B)

For SDKs, a version will always remain available as it is a downloadable package. However, the SDK may rely upon APIs or methods which no longer work, so you should assume an end-of-life SDK is no longer functional.

You can find specific information about our version timelines, changes, and release dates on our [changelog page](https://developers.facebook.com/docs/graph-api/changelog).

### Will everything remain completely unchanged in a version?

Facebook does reserve the right to make changes in any API in a short period of time for issues related to security or privacy. These changes don't happen often, but they do happen.

### What happens if I don't specify a version for an API?

We refer to an API call made without specifying a version as an **unversioned** call. For example, let's say the current version is v4.0. The call is as follows:

curl \-i \-X "https://graph.facebook.com/v4.0/{my-user-id}&access\_token={access-token}"

The same unversioned call is as follows:

curl \-i \-X "https://graph.facebook.com/{my-user-id}&access\_token={access-token}"

An unversioned call uses the version set in the app dashboard **Upgrade API Version** card under **Settings > Advanced**. In following example, the version set in the app dashboard is v2.10 and the unversioned call is equivalent to:

curl \-i \-X "https://graph.facebook.com/v2.10/{my-user-id}&access\_token={access-token}"

We recommend you always specify the version where possible.

#### Limitations

* You can not make unversioned API calls to the Facebook JavaScript SDK.

### Can my app make calls to versions older than the current version?

You can specify older versions in your API calls as long as they are available and your app has made calls to that version. For example, if your app was created after v2.0 was released and makes calls using v2.0, it will be able to make calls to v2.0 until the version expires even after newer versions have been released. If you created your app after v2.0 but did not make any calls until v2.2, your app will not be able to make calls using v2.0 or to v2.1. It will only be able to make calls using v2.2 and newer versions.

### Marketing API Versioning

The [Marketing API](https://developers.facebook.com/docs/marketing-apis) has its own versioning scheme. Both version numbers and their schedules are different from the Graph API's state of things.

[Learn more about Marketing API Versioning](https://developers.facebook.com/docs/marketing-api/versions)

[](#)

Making Versioned Requests
-------------------------

### Graph API

Whether core or extended, almost all Graph API endpoints are available through a versioned path. We've a [full guide to using versions with the Graph API](https://developers.facebook.com/docs/graph-api/quickstart#versions) in our [Graph API quickstart guide](https://developers.facebook.com/docs/graph-api/quickstart).

### Dialogs

Versioned paths aren't just true for API endpoints, they're also true for dialogs and social plugins. For example, if you want to generate the Facebook Login dialog for a web app, you can prepend a version number to the endpoint that generates the dialog:

https://www.facebook.com/`v18.0`/dialog/oauth?
  client\_id\={app\-id}
  &redirect\_uri\={redirect\-uri}

### Social Plugins

If you're using the HTML5 or xfbml versions of [our social plugins](https://developers.facebook.com/docs/plugins/), the version rendered will be determined by the version specified when you're [initialising the JavaScript SDK](#jssdk).

If you're inserting an iframe or plain link version of one of our plugins, you'd prepend the version number to the source path of the plugin:

<iframe
  src\="//www.facebook.com/`v18.0`/plugins/like.php?href=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;width&amp;layout=standard&amp;action=like&amp;show\_faces=true&amp;share=true&amp;height=80&amp;appId=634262946633418" 
  scrolling\="no" 
  frameborder\="0" 
  style\="border:none; overflow:hidden; height:80px;" 
  allowTransparency\="true"\>
</iframe>

[](#)

Making Versioned Requests from SDKs
-----------------------------------

If you're using the Facebook SDK for iOS, Android or JavaScript, making versioning calls is largely automatic. Note that this is distinct from each SDKs own versioning system.

### JavaScript

The JavaScript SDK can only use different API versions if you're [using the `sdk.js` path](https://developers.facebook.com/docs/apps/changelog/#v2_0_js_sdk).

If you're using `FB.init()` from the [JavaScript SDK](https://developers.facebook.com/docs/javascript), you need to use the version parameter, like this:

FB.init({
  appId      : '{app-id}',
  version    : '`v18.0`'
});

If you set the version flag in the init, then any calls to [`FB.api()`](https://developers.facebook.com/docs/javascript/reference/FB.api) will automatically have the version prepended to the path that's called. The same is true for any dialogs for Facebook Login that happen to get called. You will get the Facebook Login dialog for that version of the API.

If you need to, you can override a version by just prepending the version to the path of the endpoint in the `FB.api()` call.

### iOS

Each version of the Facebook SDK for iOS that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with [`[FBSDKGraphRequest initWithGraphPath]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequest/#initWithGraphPath:parameters:)). The API version is listed with the release of each version of the [Facebook SDK for iOS](https://developers.facebook.com/docs/ios).

Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for iOS. For example, if `v2.7` was the most recent version of the API, the call `/me/friends` - used in the following code sample - will actually call `/v2.7/me/friends`:

\[\[\[FBSDKGraphRequest alloc\] initWithGraphPath:@"me/friends"
  parameters:@{@"fields": @"cover,name,start\_time"}\]
    startWithCompletionHandler:^(FBSDKGraphRequestConnection \*connection, id result, NSError \*error) {
        (...)
    }\];

You can override the version of the call with [`[FBSDKGraphRequestConnection overrideVersionPartWith]`](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKGraphRequestConnection/#overrideVersionPartWith:).

### Android

Each version of the Facebook SDK for Android that's released is tied to the version that's available on the date of release. This means that if you're upgrading to a new SDK you're also upgrading to the latest API version as well (although you can manually specify any earlier, available API version with `GraphRequest.setVersion()`). The API version is listed with the release of each version of the Facebook SDK for Android.

Much like the JavaScript SDK, the version is prepended to any calls you make to the graph API through the Facebook SDK for Android. For example, if `v2.7` was the most recent version of the API, the call `/me` - used in the following code sample - will actually call `/v2.7/me`:

GraphRequest request \= GraphRequest.newGraphPathRequest (
        accessToken,
        "/me/friends",
        new GraphRequest.GraphJSONObjectCallback() {
            @Override
            public void onCompleted(
                   JSONObject object,
                   GraphResponse response) {
                // Application code
            }
        });
Bundle parameters \= new Bundle();
parameters.putString("fields", "id,name,link");
request.setParameters(parameters); 
request.executeAsync();

You can override the version of the call with `GraphRequest.setVersion()`.

[](#)

[](#)

Get Started
===========

This guide explains how to get started with receiving data from the Facebook Social Graph.

Before You Start
----------------

You will need:

* [Register as a Meta Developer](https://developers.facebook.com/docs/development/register)
    
* A [Meta App](https://developers.facebook.com/docs/development/create-an-app) – This app will be for testing so there is no need to involve your app code when creating this Meta App.
    
* The [Graph API Explorer tool](https://developers.facebook.com/tools/explorer) open in a separate browser window
    
* A brief understanding of the structure of the Meta's social graph from our [Graph API Overview](https://developers.facebook.com/docs/graph-api/overview#nodes) guide
    

[](#)

Your First Request
------------------

### Step 1: Open the Graph API Explorer tool

[Open the Graph API Explorer in a new browser window.](https://developers.facebook.com/tools/explorer) This allows you to execute the examples as you read this tutorial.

The explorer loads with a default query with the `GET` method, the lastest version of the Graph API, the `/me` node and the `id` and `name` fields in the [Query String Field](https://developers.facebook.com/docs/graph-api/guides/explorer#query-string-field), and your Facebook App.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232068365_563091814813799_6070357364579520404_n.png?_nc_cat=100&ccb=1-7&_nc_sid=e280be&_nc_ohc=Jb0X_FjdtXMAX_lx8OB&_nc_ht=scontent-cdg4-2.xx&oh=00_AfDcXmBaXCzJaLkQrjTEqC_Pzy282lrE0XR4m6CAeQK_9g&oe=65CA33E4)

### Step 2. Generate an Access Token

Click the **Generate Access Token** button. A **Log in With Facebook** window will pop up. This popup is your app asking for your permission to get your name and profile picture from Facebook.

|     |     |
| --- | --- |
| This flow is our [Facebook Login](https://developers.facebook.com/docs/facebook-login) product that allows a person to log into an app using their Facebook credentials. Facebook Login allows an app to ask a person to access the person's Facebook data, and for the person to accept or decline access. Your name and profile picture are public, to allow people to find you on Facebook, so no additional requirements are needed to run this request.<br><br>Click **Continue as...**<br><br>A User Access Token is created. This token contains information such as the app making the request, the person using the app to make a request, if the access token is still valid (it expires in about an hour), the expiration time, and the scope of data the app can request. In this request the scope is `public_profile` which includes your name and profile picture. | ![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/231956490_308313234407833_1605768375436620205_n.png?_nc_cat=106&ccb=1-7&_nc_sid=e280be&_nc_ohc=H78Z8HX0lowAX-2lrh4&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCcEVCId2_KiCorvd-1lgmyZ_a_PN13TK3dDbqXrJ7ovg&oe=65CA18AE) |

|     |     |
| --- | --- |
| ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/232991718_592378688435455_3147910228443606263_n.png?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=XOaDXvshUrQAX85c1c1&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBikv7WdelGSDzKdXlytSaL4ArPPAciM4EtrUt01PxdqQ&oe=65CA1D34) | Click the information circle icon next to the acces token to view the token's information. |

### Step 3. Submit the Request

Click the **Submit** button in the upper right corner.

#### What You Should See

In the [Response Window](https://developers.facebook.com/docs/graph-api/guides/explorer#response-window), you will see a JSON response with your Facebook User ID and your name.

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.2365-6/232902382_904467853476103_7217229934737479641_n.png?_nc_cat=105&ccb=1-7&_nc_sid=e280be&_nc_ohc=qaKGbtV383YAX9NR_jP&_nc_oc=AQlrv7X5tLdtKcm_RDT-b3lLC602uyQqOHDHJ9O5i2xtLgcIWzxid1Ym85wQhnGOdJU&_nc_ht=scontent-cdg4-1.xx&oh=00_AfD94oqz2Xj2w23lhOzdDwOaEy-2VGvUvo7HT-42XDZufg&oe=65CA1063)

If you remove `?fields=id,name` from the query string field and click **Submit**, you will see the same result since `name` and `id` are the User node fields returned by default.

[](#)

Your Second Request
-------------------

### Step 1. Let's Add a Field

Let's make the First Request a little more complex by adding another field, `email`. There are two ways to add fields:

* Click the search dropdown menu in the [Node Field Viewer](https://developers.facebook.com/docs/graph-api/guides/explorer#node-field-viewer) to the left of the response window
* Start typing in the query string field.

Let's add the `email` field and click **Submit**.

#### What You Should See

While the call did not fail, only the `name` and `id` fields were returned along with a debug message. Click the (Show) link to debug the request.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/233410295_959323958245691_7180707304587023135_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=9blxrTg0eRsAX-fjOiW&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCbZuTf86yXE9qKzprBUju7J-ic5o2CMFyhLPIXBAbb7Q&oe=65CA0E56)

Almost all nodes and fields need a specific permission to access them. The debug message is telling you that you need to give your app permission to access the email address that you have associated with your Facebook account.

### Step 2. Add a Permission

|     |     |
| --- | --- |
| In the right side panel, under **Permissions**, click the **Add a Permission** dropdown menu. Click **User Data Permissions** and select **email**.<br><br>#### Generate A New User Access Token<br><br>Because you are changing the scope of the access token, you need to create a new one. Click **Generate Access Token**. Just like your first request, you must give your app permission to access your email in the Facebook Login dialog.<br><br>Once the new token has been created, click **Submit**. Now all fields in your request will be returned. | ![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.2365-6/234580746_367949518031866_340317674627083357_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e280be&_nc_ohc=GGMp-Li8JUwAX84Imei&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDAkH2KxoG191VRZuS3zcVgUIa04kwOm8RzPkEm2EWrKQ&oe=65CA2EDE) |

Try getting your Facebook posts.

[See the steps.](#)

#### Links in the Response

Notice that `id` values returned in the response window are links. These links can represent nodes, such as User, Page, or Post. If you click on a link, the ID will replace the contents of the query string field. Now you can run requests on that node. Because this node is connected to the parent node, a Post of a User, you may not need to add permissions. You can click on a Post ID now since we will be using it in the next example.

Notice: Some IDs are a combination of the parent ID and a new ID string. For example, a User's Post will have a Post ID that looks something like this: `1028223264288_102224043055529` where `1028223264288` is the User ID.

[](#)

Let's Look at an Edge
---------------------

The User node does not have many edges that can return data. Access to User objects can only be given by the User who owns the object. In most cases, a User owns an object if they created it.

For example, if you publish a post you can see information about the post such as when it was created, text, photos, and links shared in the post, and the number of reactions the post received. If you comment on your post, you will be able to get that comment, but if another person publishes a comment on your post, you will not be able to see the comment or who published it.

Try getting the number of reactions for one of your posts. You will want to take a look at the

[Object Reactions reference.](https://developers.facebook.com/docs/graph-api/reference/v13.0/object/reactions)

[See the steps.](#)

[](#)

Get the Code for your Request
-----------------------------

The explorer tool lets you test requests and once you have a successful response, you can get the code to insert into your app code. At the bottom of the response window, click **Get Code**. The explorer offers Android, iOS, JavaScript, PHP, and cURL code. The code is pre-selected so you can just copy and paste.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/231948896_1065545040645743_5920314088559660186_n.png?_nc_cat=101&ccb=1-7&_nc_sid=e280be&_nc_ohc=RwigMkJPRiEAX9cZF-8&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBI50RlJHHI8xsJjdgCgNqEDzLCqEFYTEgqPD7jMia_sw&oe=65CA346C)

We recommend that you implement the Facebook SDK for your app. This SDK will include Facebook Login which allows your app to ask for permissions and get access tokens.

[](#)

Learn More
----------

You can use the Graph API Explorer to test any request for Users, Pages, Groups, and more. Visit the [reference](https://developers.facebook.com/docs/graph-api/reference) for each node or edge to determine the permission and access token type required.

|     |     |
| --- | --- |
| * [Access Token](https://developers.facebook.com/docs/facebook-login/access-tokens)<br>* [Facebook Login](https://developers.facebook.com/docs/facebook-login)<br>* [Facebook SDKs](https://developers.facebook.com/docs#apis-and-sdks) | * [Graph API References](https://developers.facebook.com/docs/graph-api/reference)<br>* [Graph API Explorer Guide](https://developers.facebook.com/docs/graph-api/guides/explorer)<br>* [Login Security](https://developers.facebook.com/docs/facebook-login/security)<br>* [Permissions Reference](https://developers.facebook.com/docs/permissions/reference) |

[](#)

[](#)

Graph API Explorer Guide
========================

|     |     |
| --- | --- |
| The Graph API Explorer tool allows you to construct and perform Graph API queries and see their responses for any apps on which you have an admin, developer, or tester role. | [Open the Graph API Explorer tool](https://developers.facebook.com/tools/explorer) |

Common Uses
-----------

* Quickly generate access tokens
* Get code samples for your queries
* Generate debug information to include in support requests
* Test API queries with your production app's settings including permissions, features, and settings for your use cases
* Test API queries with your test or development app using permission and features on test users or test data

Requirements
------------

* A [Facebook Developer Account](https://developers.facebook.com/apps)
    
* An app for which you have a role, such as an [admin, developer, or tester role](https://developers.facebook.com/docs/apps#roles)
    

[](#)

Components
----------

### Access Token

When you get an access token, it is displayed in the upper right of the tool. This is the token that is included in your Graph API query. You can copy this token and use it in your app to test your code.

Click the information icon to see information about the current token, including the app that it's tied to, and any permissions that have been granted by the User who is using the app (which is you).

You can generate a new access token if the token has expired or if you add new permissions.

### Meta App

The Meta App dropdown menu in the upper right displays all the apps on which you have an admin, developer, or tester role. Use the dropdown to select the app settings that you wish to test.

### User or Page

The User or Page dropdown menu allows you to get and exchange App, User, and Page access tokens for the currently selected app. You can also use it to uninstall your app from your User node, which destroys the current access token.

### Permissions

Whenever you request a User access token, only one permission is given by default, `public_profile`. The Permission dropdown menu allows you to select User Data Permissions, such as `email` and `user_photos`, Events, Groups, and Pages Permissions, such as `manage_pages` and `ads_management`, and Other permissions, such as `instagram_basic` and `publish_video` permissions. This allows the current app User (which is you) to grant the app specific permissions. Only grant permissions that your app actually needs.

If your app is in development, you can grant your app any permission and your queries respect them for data owned by people with a role on your app. If your app is live, however, granting a permission that your app has not been approved for by the [App Review](https://developers.facebook.com/docs/apps/review) process causes your query to fail whenever you submit it.

### Query string Field

When you first enter the tool a default query appears. You can edit the query by typing in a new one, or by searching for and selecting fields in the field viewer after executing the query. You can also use the dropdown menus to switch between operation methods, and target different versions of the Graph API.

If you click the star icon at the end of the query field, the query is saved as a favorite. You can view your favorite queries by clicking the book icon.

### Node Field Viewer

When you submit a `GET` query on a node, the field viewer located in the left side of the window displays the name of the node and the fields returned by the Graph API. You can modify your query by searching for and selecting new fields, clicking the plus icon, and choosing from available fields, or unchecking unnecessary fields. These actions dynamically update your query in the query string field.

### Response Window

The response, located below the query string, shows the results returned from your last submitted query.

### Get Code

If you are happy with your query, click the Get Code button located in the botton center below the response, to generate sample code based on the query. Typically you won't be able to copy and paste the sample code directly in your code base, but it gives you a useful starting point.

### Copy Debug Information

If your query keeps failing and you can't figure out why, and you decide to contact Developer Support, click this button, located at the bottom center, to copy your query and response details to your clipboard. You can submit this information with your support request to help us figure out what's going on.

### Save Session

Click the Save Session button, located at the bottom center, to save the state of your query, with the access token removed. Include the link to this session if you decide to contact Developer Support.

[](#)

Sample Query
------------

Try executing the default query that appears when you first load the Graph API Explorer. If you haven't already, [open the Graph API Explorer in a new window](https://developers.facebook.com/tools/explorer), select the app you want to test from the application dropdown menu, and get a User access token.

The default query appears in the query string field:

GET https://developers.facebook.com/`v18.0`/me?fields=id,name

The default query is requesting the `id` and `name` fields on the `/me` node, which is a special node that maps to either the `/User` or `/Page` node identified by the token. Since your are using a User access token, this maps to your User node.

The `id` and `name` fields are publicly available and can be returned if the User has granted your app the `default` or `public_profile` permissions. These permissions are pre-approved for all apps (you can confirm this by clicking the information icon in the **Access Token Field**), so you don't have to grant your app any additional permissions for the query to work. Click **Get Access Token** and confirm that you want to grant your app access to your publicly available User information.

Submit your query, and you should see your app-scoped User ID and name appear in the response window.

[](#)

[](#)

Batch Requests
==============

Send a single HTTP request that contains multiple Facebook Graph API calls. Independent operations are processed in parallel while dependent operations are processed sequentially. Once all operations are complete, a consolidated response is passed back to you and the HTTP connection is closed.

The ordering of responses correspond with the ordering of operations in the request. You should process responses accordingly to determine which operations were successful and which should be retried in a subsequent operation.

### Limitations

* Batch requests are limited to 50 requests per batch. Each call within the batch is counted separately for the purposes of calculating API call limits and resource limits. For example, a batch of 10 API calls will count as 10 calls and each call within the batch contributes to CPU resource limits in the same manner. Please see our [Rate Limiting Guide](https://developers.facebook.com/docs/graph-api/overview/rate-limiting) for more information.
* Batch requests cannot include multiple [Adsets](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign) under the same [Campaign](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group). Learn more about [batching Marketing API requests](https://developers.facebook.com/docs/marketing-api/asyncrequests).

Batch Request
-------------

A batch request takes a JSON object consisting of an array of your requests. It returns an array of logical HTTP responses represented as JSON arrays. Each response has a status code, an optional headers array, and an optional body (which is a JSON encoded string).

To make a batched request, send a `POST` request to an endpoint where the `batch` parameter is your JSON object.

POST /ENDPOINT?batch\=\[JSON\-OBJECT\]

**Sample Batch Request**

In this example, we are getting information about two Pages that our app manages.

_Formatted for readability._

curl \-i \-X POST 'https://graph.facebook.com/me?batch=  
  \[
    {
      "method":"GET",
      "relative\_url":"PAGE-A-ID"
    },  
    {
      "method":"GET",
      "relative\_url":"PAGE-B-ID"
    }
  \]
  &include\_headers=false             // Included to remove header information
  &access\_token=ACCESS-TOKEN'

Once all operations are complete, a response is sent with the result of each operation. Because the headers returned can sometimes be much larger than the actual API response, you might want to remove them for efficiency. To include header information, remove the `include_headers` parameter or set it to `true`.

**Sample Response**

The body field contains a string encoded JSON object:

\[
  {
    "code": 200,
    "body": "{
      \\"name\\": \\"Page A Name\\",
      \\"id\\": \\"PAGE-A-ID\\"
      }"
  },
  {
    "code": 200,
    "body": "{
      \\"name\\": \\"Page B Name\\",
      \\"id\\": \\"PAGE-B-ID\\"
      }"
  }
\]

[](#)

Complex Batch Requests
----------------------

It is possible to combine operations that would normally use different HTTP methods into a single batch request. While `GET` and `DELETE` operations can only have a `relative_url` and a `method` field, `POST` and `PUT` operations may contain an optional `body` field. The body should be formatted as a raw HTTP POST string, similar to a URL query string.

**Sample Request**

The following example publishes a post to a Page we manage and have publish permissions and then the Page's feed in a single operation:

curl "https://graph.facebook.com/PAGE-ID?batch=
  \[
    { 
      "method":"POST",
      "relative\_url":"PAGE\-ID/feed",
      "body":"message\=Test status update"
    },
    { 
      "method":"GET",
      "relative\_url":"PAGE\-ID/feed"
    }
  \]
  &access\_token=ACCESS-TOKEN"

The output of this call would be:

\[
    { "code": 200,
      "headers": \[
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"}
       \],
      "body":"{\\"id\\":\\"…\\"}"
    },
    { "code": 200,
      "headers": \[
          { "name":"Content-Type", 
            "value":"text/javascript; charset=UTF-8"
          },
          { "name":"ETag", 
            "value": "…"
          }
      \],
      "body": "{\\"data\\": \[{…}\]}
    }
\]

The following example creates a new ad for a campaign, and then gets the details of the newly created object. Note the **URLEncoding** for the body param:

curl \\
\-F 'access\_token=...' \\
\-F 'batch=\[
  {
    "method":"POST",
    "name":"create-ad",
    "relative\_url":"11077200629332/ads",
    "body":"ads=%5B%7B%22name%22%3A%22test\_ad%22%2C%22billing\_entity\_id%22%3A111200774273%7D%5D"
  }, 
  {
    "method":"GET",
    "relative\_url":"?ids={result=create-ad:$.data.\*.id}"
  }
\]' \\
https://graph.facebook.com

The following example adds multiple pages to a Business Manager:

curl \\
\-F 'access\_token=<ACCESS\_TOKEN>' \\
\-F 'batch=\[
  {
    "method":"POST",
    "name":"test1",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_1>"
  }, 
  {
    "method":"POST",
    "name":"test2",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_2>"
  }, 
  {
    "method":"POST",
    "name":"test3",
    "relative\_url":"<BUSINESS\_ID>/owned\_pages",
    "body":"page\_id=<PAGE\_ID\_3>"
  }, 
\]' \\
"https://graph.facebook.com/v12.0"

Where:

* `<ACCESS_TOKEN>` is an access token with the `business_management` permission.
* `<BUSINESS_ID>` is the ID of the Business Manager to which the pages should be claimed.
* `<PAGE_ID_n>` are the Page IDs to be claimed.

[](#)

Errors
------

Its possible that one of your requested operations may throw an error. This could be because, for example, you don't have permission to perform the requested operation. The response is similiar to the standard Graph API, but encapsulated in the batch response syntax:

\[
    { "code": 403,
      "headers": \[
          {"name":"WWW-Authenticate", "value":"OAuth…"},
          {"name":"Content-Type", "value":"text/javascript; charset=UTF-8"} \],
      "body": "{\\"error\\":{\\"type\\":\\"OAuthException\\", … }}"
    }
\]

Other requests within the batch should still complete successfully and will be returned, as normal, with a `200` status code.

[](#)

Timeouts
--------

Large or complex batches may timeout if it takes too long to complete all the requests within the batch. In such a circumstance, the result is a partially-completed batch. In a partially-completed batch, requests that are completed successful will return the normal output with the `200` status code. Responses for requests that are not successful will be `null`. You can retry any unsuccessful request.

[](#)

Batch calls with JSONP
----------------------

The Batch API supports JSONP, just like the rest of the Graph API - the JSONP callback function is specified using the `callback` query string or form post parameter.

[](#)

Using Multiple Access Tokens
----------------------------

Individual requests of a single batch request can specify its own access tokens as a query string or form post parameter. In that case the top level access token is considered a fallback token and is used if an individual request has not explicitly specified an access token.

This may be useful when you want to query the API using several different User or Page access tokens, or if some of your calls need to be made using an app access token.

You must include an access token as a top level parameter, even when all individual requests contain their own tokens.

[](#)

Upload Binary Data
------------------

You can upload multiple binary items as part of a batch call. In order to do this, you need to add all the binary items as multipart/mime attachments to your request, and need each operation to reference its binary items using the `attached_files` property in the operation. The `attached_files` property can take a comma separated list of attachment names in its value.

The following example shows how to upload 2 photos in a single batch call:

curl 
     \-F 'access\_token=…' \\
     \-F 'batch=\[{"method":"POST","relative\_url":"me/photos","body":"message=My cat photo","attached\_files":"file1"},{"method":"POST","relative\_url":"me/photos","body":"message=My dog photo","attached\_files":"file2"},\]' \\
     \-F 'file1=@cat.gif' \\
     \-F 'file2=@dog.jpg' \\
    https://graph.facebook.com

[](#)

\-->

[](#)

Debug Requests
==============

Graph API Debug Mode
--------------------

When Debug Mode is enabled, Graph API response may contain additional fields that explain potential issues with the request.

To enable debug mode, use the `debug` query string parameter. For example:

cURLAndroid SDKObjective-CJava SDKPHP SDK

    curl -i -X GET \
      "https://graph.facebook.com/{user-id}
        ?fields=friends
        &debug=all
        &access_token={your-access-token}"

    GraphRequest request = GraphRequest.newMeRequest(
      accessToken,
      new GraphRequest.GraphJSONObjectCallback() {
        @Override
        public void onCompleted(JSONObject object, GraphResponse response) {
          // Insert your code here
        }
    });
    
    Bundle parameters = new Bundle();
    parameters.putString("fields", "friends");
    parameters.putString("debug", "all");
    request.setParameters(parameters);
    request.executeAsync();

    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
        initWithGraphPath:@"/{user-id}"
               parameters:@{ @"fields": @"friends",@"debug": @"all",}
               HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
        // Insert your code here
    }];

    FB.api(
      '/{user-id}',
      'GET',
      {"fields":"friends","debug":"all"},
      function(response) {
          // Insert your code here
      }
    );

    try {
      // Returns a `FacebookFacebookResponse` object
      $response = $fb->get(
        '/{user-id}',
        '{access-token}'
      );
    } catch(FacebookExceptionsFacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(FacebookExceptionsFacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();

If `user_friends` permission was not granted, this produces the following response:

{
  "data": \[
  \], 
  "\_\_debug\_\_": {
    "messages": \[
      {
        "message": "Field friends is only accessible on User object, if user\_friends permission is granted by the user", 
        "type": "warning"
      }, 
      {
        "link": "https://developers.facebook.com/docs/apps/changelog#v2\_0", 
        "message": "Only friends who have installed the app are returned in versions greater or equal to v2.0.", 
        "type": "info"
      }
    \]
  }
}

The `debug` parameter value can be set to "all" or to a minimal requested severity level that corresponds to `type` of the message:

| Debug Param Value | What Will Be Returned |
| --- | --- |
| all | All available debug messages. |
| info | Debug messages with type _info_ and _warning_. |
| warning | Only debug messages with type _warning_. |

Debug information, when available, is returned as a JSON object under the `__debug__` key in the `messages` array. Every element of this array is a JSON object that contains the following fields:

| Field | Datatype | Description |
| --- | --- | --- |
| message | String | The message. |
| type | String | The message severity. |
| link | String | \[Optional\] A URL pointing to related information. |

You can also use Debug Mode with [Graph API Explorer](https://developers.facebook.com/tools/explorer).

### Determining Version used by API Requests

When you're building an app and making Graph API requests, you might find it useful to determine what API version you're getting a response from. For example, if you're making calls without a version specified, the API version that responds may not be known to you.

The Graph API supplies a request header with any response called `facebook-api-version` that indicates the exact version of the API that generated the response. For example, a Graph API call that generates a request with v2.0 produces the following HTTP header:

facebook\-api\-version:v2.0

This `facebook-api-version` header allows you to determine whether API calls are being returned from the version that you expect.

### Debug Info for Reporting Bugs

When [reporting a bug](https://developers.facebook.com/bugs/) in the Graph API, we include some additional request headers to send with your bug report to help us pinpoint and reproduce your issue. These request headers are `X-FB-Debug`, `x-fb-rev`, and `X-FB-Trace-ID`.

[](#)

Handling Errors
===============

Requests made to our APIs can result in several different error responses. The following document describes the recovery tactics and provides a list of error values with a map to the most common recovery tactic to use.

Error Responses
---------------

The following represents a common error response resulting from a failed API request:

{
  "error": {
    "message": "Message describing the error", 
    "type": "OAuthException", 
    "code": 190,
    "error\_subcode": 460,
    "error\_user\_title": "A title",
    "error\_user\_msg": "A message",
    "fbtrace\_id": "EJplcsCHuLu"
  }
}

* `message`: A human-readable description of the error.
* `code`: An error code. Common values are listed below, along with common recovery tactics.
* `error_subcode`: Additional information about the error. Common values are listed below.
* `error_user_msg`: The message to display to the user. The language of the message is based on the locale of the API request.
* `error_user_title`: The title of the dialog, if shown. The language of the message is based on the locale of the API request.
* `fbtrace_id`: Internal support identifier. When [reporting a bug](https://developers.facebook.com/bugs/) related to a Graph API call, include the `fbtrace_id` to help us find log data for debugging. However, this ID will expire shortly. To help the support team reproduce your issue, please attach a saved [graph explorer session](https://developers.facebook.com/tools/explorer/).

### Error Codes

| Code or Type | Name | What To Do |
| --- | --- | --- |
| OAuthException |     | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors).<br><br>If a subcode is present, see the subcode. |
| 102 | API Session | If no subcode is present, the login status or access token has expired, been revoked, or is otherwise invalid. [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors).<br><br>If a subcode is present, see the subcode. |
| 1   | API Unknown | Possibly a temporary issue due to downtime. Wait and retry the operation. If it occurs again, check that you are requesting an existing API. |
| 2   | API Service | Temporary issue due to downtime. Wait and retry the operation. |
| 3   | API Method | Capability or permissions issue. Make sure your app has the necessary capability or permissions to make this call. |
| 4   | API Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 17  | API User Too Many Calls | Temporary issue due to throttling. Wait and retry the operation, or examine your API request volume. |
| 10  | API Permission Denied | Permission is either not granted or has been removed. [Handle the missing permissions](https://developers.facebook.com/docs/facebook-login/permissions#handling). |
| 190 | Access token has expired | [Get a new access token](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 200-299 | API Permission (Multiple values depending on permission) | Permission is either not granted or has been removed. [Handle the missing permissions](https://developers.facebook.com/docs/facebook-login/permissions#handling). |
| 341 | Application limit reached | Temporary issue due to downtime or throttling. Wait and retry the operation, or examine your API request volume. |
| 368 | Temporarily blocked for policies violations | Wait and retry the operation. |
| 506 | Duplicate Post | Duplicate posts cannot be published consecutively. Change the content of the post and try again. |
| 1609005 | Error Posting Link | There was a problem scraping data from the provided link. Check the URL and try again. |

### Authentication Error Subcodes

| Code | Name | What To Do |
| --- | --- | --- |
| 458 | App Not Installed | The User has not logged into your app. Reauthenticate the User. |
| 459 | User Checkpointed | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 460 | Password Changed | On iOS 6 and above, if the person logged in using the OS-integrated flow, direct them to Facebook OS settings on the device to update their password. Otherwise, they must log in to the app again. |
| 463 | Expired | Login status or access token has expired, been revoked, or is otherwise invalid. [Handle expired access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 464 | Unconfirmed User | The User needs to log in at https://www.facebook.com or https://m.facebook.com to correct an issue. |
| 467 | Invalid Access Token | Access token has expired, been revoked, or is otherwise invalid. [Handle expired access tokens](https://developers.facebook.com/docs/facebook-login/access-tokens#errors). |
| 492 | Invalid Session | User associated with the Page access token does not have an appropriate role on the Page. |

### Rate Limiting Error Codes

Visit the [Graph API Rate Limits guide](https://developers.facebook.com/docs/graph-api/overview/rate-limiting) for more information about Rate Limiting Error Codes.

[](#)

[](#)

Field Expansion
===============

If you test the `GET /me/feed` query in the Graph API Explorer, you will noticed that the request returned many objects and paginated the results. This is common for most edges.

#### Example Response

{
  "data": \[
   {
      "created\_time": "2021-04-30T01:37:07+0000",
      "message": "I’ll never forget it has a head.",
      "id": "10211998223264288\_10222340566616408"
    },
    ...
    {
      "created\_time": "2021-04-25T22:29:26+0000",
      "message": "Things you hear at my house: \\"I accidentally made a cake.\\"",
      "id": "10211998223264288\_10222314489524497"
    }
  \],
  "paging": {
    "previous": "https://graph.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&\_\_previous=1&since=1627322627&until&\_\_paging\_token=enc\_AdB2fX...",
    "next": "https://graph.intern.facebook.com/v11.0/USER-ID/feed?access\_token=ACCESS-TOKEN&pretty=0&until=1619389766&since&\_\_paging\_token=enc\_AdAamX...&\_\_previous"
  }
}

Field expansion allows you not only to limit the number of objects returned but also perform nested requests.

Limiting Results
----------------

Limiting allows you to control the number of objects returned in each set of paginated results. To limit results, add a `.limit()` argument to any field or edge.

For example, performing a GET request on your `/feed` edge may return hundreds of Posts. You can limit the number of Posts returned for each page of results by doing this:

curl \-i \-X GET "https://graph.facebook.com/USER-ID?fields=feed.limit(3)&access\_token=ACCESS-TOKEN"

This returns all of the Posts on your User node, but limits the number of objects in each page of results to three. Notice that instead of specifying the Feed edge in the path URL (`/user/feed`), you specify it in the `fields` parameter (`?fields=feed`), which allows you to append the `.limit(3)` argument.

Here are the query results:

{
  "feed": {
    "data": \[
      {
        "created\_time": "2021-12-12T01:24:21+0000",
        "message": "This picture of my grandson with Santa",
        "id": "POST-ID"
      },
      {
        "created\_time": "2021-12-11T23:40:17+0000",
        "message": ":)",
        "id": "POST-ID"      
      },
      {
        "created\_time": "2021-12-11T23:31:38+0000",
        "message": "Thought you might enjoy this.",
        "id": "POST-ID"      
      }
    \],
    "paging": {
      "previous": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&since=1542820440&access\_token=ACCESS-TOKEN&\_\_paging\_token=enc\_AdC...&\_\_previous=1",
      "next": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&access\_token=ACCESS-TOKEN&until=1542583212&\_\_paging\_token=enc\_AdD..."
    }
  },
  "id": "USER-ID"
}

As you can see, only three objects appear in this page of paginated results. However, the response included a `next` field and URL which you can use to fetch the next page.

[](#)

Nested Requests
---------------

The field expansion feature of the Graph API allows you to effectively nest multiple graph queries into a single call. For example, in a single call, you can ask for the first N photos of the first K albums. The response maintains the data hierarchy so developers do not have to weave the data together on the client. This is different from the [batch requests](https://developers.facebook.com/docs/graph-api/making-multiple-requests/) feature which allows you to make multiple, potentially unrelated, Graph API calls in a single request.

Here is the general format that field expansion takes:

GET graph.facebook.com/{node\-id}?fields\=LEVEL\-ONE{LEVEL\-TWO}

`LEVEL-ONE` in this case would be one or more (comma-separated) fields or edges from the parent node. `LEVEL-TWO` would be one or more (comma-separated) fields or edges from the first level node.

There is no limitation to the amount of nesting of levels that can occur here. You can also use a `.limit(n)` argument on each field or edge to restrict how many objects you want to get.

This is easier to understand by seeing it in action, so here's an example query that will retrieve up to five posts your published, with the text from each individual post.

GET graph.facebook.com/me?fields\=posts.limit(5){message}

We can then extend this a bit more and for each post object, we get the text and privacy setting of each post. By default the `privacy` field returns an object that contains information about five key:value pairs, `allow`, `deny`, `description`, `friends`, and `value`. In this query we only want one returned, the `value` key:value pair.

GET graph.facebook.com/me?fields\=posts.limit(5){message,privacy{value}}

Now we can extend it again by retrieving the name of each photo, the picture URL, and the people tagged:

GET graph.facebook.com
  /me?fields\=albums.limit(5){name, photos.limit(2){name, picture, tags.limit(2)}},posts.limit(5)

Let's look at an example using cursor-based pagination:

GET graph.facebook.com
  /me?fields\=albums.limit(5){name,photos.limit(2).after(MTAyMTE1OTQwNDc2MDAxNDkZD){name,picture,tags.limit(2)}},posts.limit(5)

You can see how field expansion can work across nodes, edges, and fields to return really complex data in a single request.

#### Limitations

* Certain resources, including most of Marketing API, are unable to utilize field expansion on some or all connections.

[](#)

Field Aliases
-------------

Many nodes and edges allow you to provide aliases for fields by using the `as` parameter. This will return data using fields that you already have in your application logic.

For example, you can retrieve an image in two sizes and alias the returned object fields as `picture_small` and `picture_larger`:

me?fields\=id,name,picture.width(100).height(100).as(picture\_small),picture.width(720).height(720).as(picture\_large)

On success, Graph API returns this result:

{
  "id": "993363923726",
  "name": "Benjamin Golub",
  "picture\_small": {
    "data": {
      "height": 100,
      "is\_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/p100x100/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=82b9abe469c78486645783c9e70e8797&amp;oe=561D10AE&amp;\_\_gda\_\_=1444247939\_661c0f48363f1d1a7d42b6f836687a04",
      "width": 100
    }
  },
  "picture\_large": {
    "data": {
      "height": 720,
      "is\_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/11700890\_10100330450676146\_2622493406845121288\_n.jpg?oh=dd86551faa2de0cd6b359feb5665b0a5&amp;oe=561E0B46&amp;\_\_gda\_\_=1443979219\_f1abbbdfb0fb7dac361d7ae02b460638",
      "width": 720
    }
  }
}

Please note that not all nodes and edges support field aliasing. Endpoints that do not support aliasing will return an error. For example, the `User` node does not support aliasing, so if you tried to alias the `name` field as `my_name` you would receive an error like this:

{
  "error": {
    "message": "(#100) Unknown fields: my\_name.",
    "type": "OAuthException",
    "code": 100
  }
}

[](#)

Next Steps
----------

* Learn about [Paginated Results](https://developers.facebook.com/docs/graph-api/results).

[](#)

[](#)

Secure Graph API Calls
======================

Almost every Graph API call requires an [access token](https://developers.facebook.com/docs/facebook-login/access-tokens/). Malicious developers can steal access tokens and use them to send spam from your app. Meta has automated systems to detect this, but you can help us secure your app. This document covers some of the ways you can improve security in your app.

Meta Crawler
------------

A number of platform services such as Social Plugins and Open Graph require our systems to be able to reach your web pages. We recognize that there are situations where you might not want these pages on the public web, during testing or for other security reasons.

We've provided information on IP allow lists and User Agent strings for Meta's crawlers in our [Meta Crawler guide](https://developers.facebook.com/docs/sharing/webmasters/crawler).

[](#)

Login Security
--------------

There are a large number of settings you can change to improve the security of your app. Please see our [Login Security](https://developers.facebook.com/docs/facebook-login/security/) documentation for a checklist of things you can do.

It's also worth looking at our [access token](https://developers.facebook.com/docs/facebook-login/access-tokens/) documentation which covers various architectures and the security trade-offs that you should consider.

[](#)

Server Allow List
-----------------

We also enable you to restrict some of your API calls to come from a list of servers that you have allowed to make calls. Learn more in our [login security](https://developers.facebook.com/docs/facebook-login/security#surfacearea) documentation.

[](#)

Social Plugin Confirmation Steps
--------------------------------

In order to protect users from unintentionally liking content around the web, our systems will occasionally require them to confirm that they intended to interact with one of our Social Plugins via a "confirm" dialog. This is expected behavior and once the system has verified your site as a good actor, the step will be removed automatically.

[](#)

Encryption
----------

When connecting to our servers your client must use TLS and be able to verify a certificate signed using [`sha256WithRSAEncryption`](https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.alvestrand.no%2Fobjectid%2F1.2.840.113549.1.1.11.html&h=AT0PfEgqOCOqvvnwLtREimTlJAEjHrWbx6MIEc4tz15Nt8jTZh6PDGY00QOdxgohsOLsQbilgkfPtVUGXMd7dCLB4EmUVsPOFTogufNXvkotAcdJwvvg_KUQ8kfrmmxIqf8s5GylLf6jiAPOmhJ-bA).

Graph API supports TLS 1.2 and 1.3 and non-static RSA cipher suites. We are currently deprecating support for older TLS versions and static RSA cipher suites. Version 16.0 no longer supports TLS versions older than 1.1 or static RSA cipher suites. This change will apply to all API versions on May 3, 2023.

[](#)

Verify Graph API Calls with `appsecret_proof`
---------------------------------------------

Access tokens are portable. It's possible to take an access token generated on a client by Meta's SDK, send it to a server and then make calls from that server on behalf of the client. An access token can also be stolen by malicious software on a person's computer or a man in the middle attack. Then that access token can be used from an entirely different system that's not the client and not your server, generating spam or stealing data.

Calls from a server can be better secured by adding a parameter called `appsecret_proof`. The app secret proof is a sha256 hash of your access token, using your app secret as the key. The app secret can be found in your app dashboard in **Settings > Basic**.

If you're using the official PHP SDK, the `appsecret_proof` parameter is automatically added.

### Generate the Proof

The following code example is what the call looks like in PHP:

$appsecret\_proof\= hash\_hmac('sha256', $access\_token, $app\_secret); 

### Add the Proof

You add the result as an `appsecret_proof` parameter to each call you make:

curl \\
  \-F 'access\_token=<access\_token>' \\
  \-F 'appsecret\_proof=<app secret proof>' \\
  \-F 'batch=\[{"method":"GET", "relative\_url":"me"},{"method":"GET", "relative\_url":"me/friends?limit=50"}\]' \\
  https://graph.facebook.com

### Require the Proof

In the **Settings > Advanced** section of your app dashboard in the **Security** section, you enable **Require App Secret**. When this is enabled, we will only allow API calls that include the `appsecret_proof`.

[](#)

[](#)

Resumable Upload API
====================

The Resumable Upload API allows you to upload large files to the Graph API and resume interrupted upload sessions without having to start over. Once uploaded, you can use an uploaded file's handle with other Graph API endpoints that support them.

Note that the Resumable Upload API is not the only way to upload files. Many nodes have an edge that supports uploading, but most do not have a way to handle large files or a way to resume an interrupted upload session.

References for endpoints that support uploaded file handles will indicate if the endpoints support handles returned by the Resumable Upload API.

Upload Steps
------------

Uploading a file is a two step process:

1. Use the [Application Uploads](https://developers.facebook.com/docs/graph-api/reference/application/uploads/) endpoint to describe your file and create an upload session.
2. Use the returned upload session ID to initiate the upload process.

If successful, a file handle will be returned which you can then use with other endpoints that support file handles returned by the Resumable Upload API.

### Step 1: Create a Session

Send a `POST` request that describes your file to the [Application Uploads](https://developers.facebook.com/docs/graph-api/reference/application/uploads/) endpoint (`{app-id}/uploads`) . Upon success an upload session ID will be returned that you can use in the next step to initiate the upload.

#### Request Syntax

POST https://graph.facebook.com/{api-version}/{app-id}/uploads
  &file\_length\={file\-length}
  &file\_type\={file\-type}
  &access\_token\={access\-token}

Parameters Placeholders:

* `{api-version}` — The Graph API version.
* `{app-id}` — The application ID. The uploaded file that will be associated with this app. The app user must have an administrator or developer role on this app.
* `file-length` — The file's size, in bytes.
* `file-type` — The file's MIME type. Valid values are: `application/pdf`, `image/jpeg`, `image/jpg`, `image/png`, and `video/mp4`
* `{access-token}` — The app user's User Access Token.

Refer to the [Application Uploads](https://developers.facebook.com/docs/graph-api/guides/docs/graph-api/reference/application/uploads/) endpoint reference for a complete list of available query parameters and supported file types.

#### Response

{
  "id": "{id}"
}

Response property values:

* `{id}` — Upload session ID.

#### Sample Request

curl \-X POST \\
 "https://graph.facebook.com/`v18.0`/584544743160774/uploads?file\_length=109981&file\_type=image/png&access\_token=EAAIT..."

#### Sample Response

{
    "id": "upload:MTphd..."
}

### Step 2: Initiate Upload

Initiate the upload session by sending a `POST` request to Graph API host address and append your upload session `{id}` along with the required headers indicated below. Upon success, a file handle, `{h}`, is returned that you can then use with any Graph API endpoints that support file handles returned by the Resumable Upload API.

If the upload session is taking longer than expected or has been interrupted, follow the steps described in the [Interruptions](#interruptions) section.

#### Request Syntax

POST https://graph.facebook.com/{api-version}/{upload-session-id}
  \--header 'Authorization: OAuth {access-token}' 
  \--header 'file\_offset: 0'
  \--data\-binary @{file\-name}

**Placeholder Values**

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in step 1.
* `{access-token}` — App user's User Access Token. The app user must have a role on the app that was targeted in step 1.
* `{file-name}` — Name of the file to upload.

You must include the access token in the header or your request will fail.

#### Response

{
  "h": "{h}"
}

Response property values:

* `{h}` — The uploaded file's file handle

#### Sample Request

curl \-X POST \\
 "https://graph.facebook.com/`v18.0`/upload:MTphd..." \\
 \--header "Authorization: OAuth EAAIT..." \\
 \--header "file\_offset: 0" \\
 \--data\-binary @cats\_are\_jerks.png

#### Sample Response

{
    "h": "2:c2FtcGxl..."
}

[](#)

Interruptions
-------------

If you have initiated an upload session but it is taking longer than expected or has been interrupted, send a `GET` request to Graph API host address and append your upload session ID. The API returns a `file_offset` value that you can use to resume the upload process from the point of interruption.

### Request Syntax

GET https://graph.facebook.com/{api-version}/{upload-session-id}
  ?access\_token\={access\-token}

Placeholder values:

* `{api-version}` — Graph API version.
* `{upload-session-id}` — Upload session ID returned in [Step 1: Create a Session](#step-1--create-a-session).
* `{access-token}` — App user's User Access Token.

### Response

{
  "id": "{id}",
  "file\_offset": {file\-offset}
}

Response property values:

* `{id}` — The upload session ID that was queried.
* `{file-offset}` — An integer that indicates the number of bytes that have been successfully uploaded.

Capture the `file_offset` value and repeat [Step 2: Initiate Upload](#step-2--initiate-upload), assigning the value to the corresponding `file_offset` header. This will resume the upload process from the point of interruption.

### Sample Request

curl \-X GET \\
 "https://graph.facebook.com/`v18.0`/upload:MTphd...&access\_token=EAAIT..." \\

### Sample Response

{
  "id": "upload:MTphd",
  "file\_offset": 5238
}

[](#)

[](#)

Changelog
=========

|     |     |
| --- | --- |
| The latest Graph API version is: | `v18.0` |

The Graph API and Marketing API changelogs document [versioned](#versioned) and [out-of-cycle](#outofcycle) changes, respective to the API.

### Related Changelogs

* [Instagram Graph API Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/instagram-api/changelog) 
    
* [Marketing API Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog) 
    
* [Messenger Platform Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/messenger-platform/changelog/) (includes Instagram Messaging)
    
* [WhatsApp Business Platform Changelog ![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.2365-6/310307727_3347317042262105_1088877051262827250_n.png?_nc_cat=107&ccb=1-7&_nc_sid=e280be&_nc_ohc=831MNFLSQwkAX_NBYJc&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBFzfp_r0uP87LWhIW9LbUGV2HepuPyhHSxWkm3ugn0Bg&oe=65CA3DE2)](https://developers.facebook.com/docs/whatsapp/business-platform/changelog) 
    

### Versioned Changes

Versioned changes are changes introduced with the release of a new API [version](https://developers.facebook.com/docs/apps/versions). Versioned changes typically apply to the newest version immediately and often will apply to other versions at a future date. The changelog accompanying each release indicates which changes apply to the current release and which changes apply to other versions.

Refer to our [Upgrade Guide](https://developers.facebook.com/docs/apps/upgrading) to learn how to upgrade to a new API version.

### Out-Of-Cycle Changes

Out-of-cycle changes are changes introduced outside of our normal, versioned release schedule and typically do not apply to a specific version. Instead, out-of-cycle changes usually apply to all API versions immediately. Because of this, out-of-cycle changes are introduced infrequently.

Available Graph API Versions
----------------------------

| Version | Date Introduced | Available Until |
| --- | --- | --- |
| [v18.0](https://developers.facebook.com/docs/graph-api/changelog/version18.0#graph-api) | September 12, 2023 | TBD |
| [v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#graph-api) | May 23, 2023 | TBD |
| [v16.0](https://developers.facebook.com/docs/graph-api/changelog/version16.0#graph-api) | February 2, 2023 | TBD |
| [v15.0](https://developers.facebook.com/docs/graph-api/changelog/version15.0#graph-api) | September 15, 2022 | TBD |
| [v14.0](https://developers.facebook.com/docs/graph-api/changelog/version14.0#graph-api) | May 25, 2022 | September 17, 2024 |
| [v13.0](https://developers.facebook.com/docs/graph-api/changelog/version13.0#graph-api) | February 8, 2022 | May 28, 2024 |
| [v12.0](https://developers.facebook.com/docs/graph-api/changelog/version12.0#graph-api) | September 14, 2021 | February 8, 2024 |
| [v11.0](https://developers.facebook.com/docs/graph-api/changelog/version11.0#graph-api) | June 8, 2021 | September 14, 2023 |

[](#)

Available Marketing API Versions
--------------------------------

| Version | Date Introduced | Available Until |
| --- | --- | --- |
| [v18.0](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/version18.0) | September 12, 2023 | August 13, 2024 |
| [v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#marketing-api) | May 23, 2023 | May 14, 2024 |
| [v16.0](https://developers.facebook.com/docs/graph-api/changelog/version16.0#marketing-api) | February 2, 2023 | February 6, 2024 |

[](#)

Out-Of-Cycle Changes
--------------------

* [2023 out-of-cycle changes](https://developers.facebook.com/docs/graph-api/changelog/non-versioned-changes/nvc-2023)

[](#)

[](#)

Upgrade to the Latest Graph API Version
=======================================

This guide describes how to prepare your app to test different versions of the Graph API and to upgrade to the latest version.

The [API Upgrade Tool](https://developers.facebook.com/tools/api_versioning/) shows the API calls from your app that may be affected by changes in newer versions of the API. You will be able to quickly see which changes you need to make to upgrade from your current version to a newer version.

Learn How a Change Affects Your App
-----------------------------------

The API Upgrade Tool displays a customized list of changes that impact an app when upgrading to a specified target version. This allows you to view all relevant changes between the source and target versions.

Step 1. In the [Upgrade tool](https://developers.facebook.com/tools/api_versioning/), select your app from the dropdown menu or type in the name of the app.

The dropdown menu only lists up to ten apps. To view more apps than those listed, use the search bar in the dropdown menu.

Step 2. Use the dropdown menus to the right to select the version you would like to **Upgrade from** and the version you would like to **Upgrade to**.

### Read the Results

The tool displays the number of changes that need to be made to update your app to the selected version. If your app makes API calls that will not be affected by a newer version no data will be returned.

Methods are color coded by the version affecting the call. Hover over the bar chart to see how many changes are in each version. The dates associated with each version are when the changes will be enforced for all apps.

The table shows the type of change (deprecation, new feature or change), which methods are affected, the number of calls made in the last 7 days, and the percentage of API calls affected by that specific change.

### Limitations

* You must be an admin or developer of the app to view the app in the tool.
* No data will be returned if your app has not made any, or too few, API calls from the **Update from** version.
* Call volumes may appear incorrect. API call logging is sampled and aggregated over the previous week. It is compared with the call volume to estimate how many of your calls could be affected by a given version change.

**Note:** Not all changes may affect each API call. Use your best judgment on whether a particular change needs to be handled by your app. Be sure to test your API calls in the newer version to ensure it works properly.

[](#)

Implement a New Version
-----------------------

In the App Dashboard **Settings > Advanced**, scroll to the **Upgrade API Version** section.

#### Upgrading Developers and Admins

This upgrades all developers and admins of an app to the next available version. This allows you to test changes with a small subset of real users before releasing the new version to the public.

#### Upgrading All Calls

This upgrades all calls made by an app to the next available version. Upgrading early is useful since it preserves the option of going back to the original version in case of unforeseen bugs or issues.

[](#)

Learn More
----------

* [Graph API Changelog](https://developers.facebook.com/docs/graph-api/changelog) – Learn about the latest version changes.
* [Versioning](https://developers.facebook.com/docs/graph-api/guides/versioning) – Learn all about Graph API versioning, requests to different versions, and more.
* [Test Apps](https://developers.facebook.com/docs/development/build-and-test/test-apps) – Learn how to create test apps to test changes to your app before public release.
* [Test Users](https://developers.facebook.com/docs/development/build-and-test/test-users) – Learn how to create test users to test changes to your app before public release.

[](#)

[](#)

Versions
========

The changelogs listed below document changes introduced in new Graph API and Marketing API versions. To learn more about versions, please see our [Platform Versioning](https://developers.facebook.com/docs/apps/versions) document.

Changes introduced outside of a version release are documented in our [Out-Of-Cycle Changes](https://developers.facebook.com/docs/graph-api/changelog/out-of-cycle-changes) document.

Graph API
---------

| Version | Release Date | Expiration Date |
| --- | --- | --- |
| [v18.0](https://developers.facebook.com/docs/graph-api/changelog/version18.0#graph-api) | September 12, 2023 | TBD |
| [v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#graph-api) | May 23, 2023 | TBD |
| [v16.0](https://developers.facebook.com/docs/graph-api/changelog/version16.0#graph-api) | February 2, 2023 | TBD |
| [v15.0](https://developers.facebook.com/docs/graph-api/changelog/version15.0#graph-api) | September 15, 2022 | TBD |
| [v14.0](https://developers.facebook.com/docs/graph-api/changelog/version14.0#graph-api) | May 25, 2022 | September 17, 2024 |
| [v13.0](https://developers.facebook.com/docs/graph-api/changelog/version13.0#graph-api) | February 8, 2022 | May 28, 2024 |
| [v12.0](https://developers.facebook.com/docs/graph-api/changelog/version12.0#graph-api) | September 14, 2021 | February 8, 2024 |
| [v11.0](https://developers.facebook.com/docs/graph-api/changelog/version11.0#graph-api) | June 8, 2021 | September 14, 2023 |
| [v10.0](https://developers.facebook.com/docs/graph-api/changelog/version10.0#graph-api) | February 23, 2021 | June 8, 2023 |
| [v9.0](https://developers.facebook.com/docs/graph-api/changelog/version9.0#graph-api) | November 10, 2020 | February 23, 2023 |
| [v8.0](https://developers.facebook.com/docs/graph-api/changelog/version8.0#graph-api) | August 4, 2020 | November 1, 2022 |
| [v7.0](https://developers.facebook.com/docs/graph-api/changelog/version7.0#graph-api) | May 5, 2020 | August 4, 2022 |
| [v6.0](https://developers.facebook.com/docs/graph-api/changelog/version6.0) | February 3, 2020 | May 5, 2022 |
| [v5.0](https://developers.facebook.com/docs/graph-api/changelog/version5.0) | October 29, 2019 | February 3, 2022 |
| [v4.0](https://developers.facebook.com/docs/graph-api/changelog/version4.0) | July 29, 2019 | November 2, 2021 |
| [v3.3](https://developers.facebook.com/docs/graph-api/changelog/version3.3) | April 30, 2019 | August 3, 2021 |
| [v3.2](https://developers.facebook.com/docs/graph-api/changelog/version3.2) | October 23, 2018 | May 4, 2021 |
| [v3.1](https://developers.facebook.com/docs/graph-api/changelog/version3.1) | July 26, 2018 | October 27, 2020 |
| [v3.0](https://developers.facebook.com/docs/graph-api/changelog/version3.0) | May 1, 2018 | July 28, 2020 |
| [v2.12](https://developers.facebook.com/docs/graph-api/changelog/version2.12) | January 30, 2018 | May 5, 2020 |
| [v2.11](https://developers.facebook.com/docs/graph-api/changelog/version2.11) | November 7, 2017 | January 28, 2020 |
| [v2.10](https://developers.facebook.com/docs/graph-api/changelog/version2.10) | July 18, 2017 | November 7, 2019 |
| [v2.9](https://developers.facebook.com/docs/graph-api/changelog/version2.9) | April 18, 2017 | July 22, 2019 |
| [v2.8](https://developers.facebook.com/docs/graph-api/changelog/version2.8) | October 5, 2016 | April 18, 2019 |
| [v2.7](https://developers.facebook.com/docs/graph-api/changelog/version2.7) | July 13, 2016 | October 5, 2018 |
| [v2.6](https://developers.facebook.com/docs/graph-api/changelog/version2.6) | April 12, 2016 | July 13, 2018 |
| [v2.5](https://developers.facebook.com/docs/graph-api/changelog/version2.5) | October 7, 2015 | April 12, 2018 |
| [v2.4](https://developers.facebook.com/docs/graph-api/changelog/version2.4) | July 8, 2015 | October 9, 2017 |
| [v2.3](https://developers.facebook.com/docs/graph-api/changelog/version2.3) | March 25, 2015 | July 10, 2017 |
| [v2.2](https://developers.facebook.com/docs/graph-api/changelog/version2.2) | October 30, 2014 | March 27, 2017 |
| [v2.1](https://developers.facebook.com/docs/graph-api/changelog/version2.1) | August 7, 2014 | October 31, 2016 |
| v2.0 | April 30, 2014 | August 8, 2016 |
| v1.0 | April 21, 2010 | April 30, 2015 |

[](#)

Marketing API
-------------

| Version | Release Date | Expiration Date |
| --- | --- | --- |
| [v18.0](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog/version18.0) | September 12, 2023 | August 13, 2024 |
| [v17.0](https://developers.facebook.com/docs/graph-api/changelog/version17.0#marketing-api) | May 23, 2023 | May 14, 2024 |
| [v16.0](https://developers.facebook.com/docs/graph-api/changelog/version16.0#marketing-api) | February 2, 2023 | February 6, 2024 |
| [v15.0](https://developers.facebook.com/docs/graph-api/changelog/version15.0#marketing-api) | September 15, 2022 | September 20, 2023 |
| [v14.0](https://developers.facebook.com/docs/graph-api/changelog/version14.0#marketing-api) | May 25, 2022 | September 20, 2023 |
| [v13.0](https://developers.facebook.com/docs/graph-api/changelog/version13.0#marketing-api) | February 8, 2022 | January 25, 2023 |
| [v12.0](https://developers.facebook.com/docs/graph-api/changelog/version12.0#marketing-api) | September 14, 2021 | August 9, 2022 |
| [v11.0](https://developers.facebook.com/docs/graph-api/changelog/version11.0#marketing-api) | June 8, 2021 | February 23, 2022 |
| [v10.0](https://developers.facebook.com/docs/graph-api/changelog/version10.0#marketing-api) | February 23, 2021 | October 4, 2021 |
| [v9.0](https://developers.facebook.com/docs/graph-api/changelog/version9.0#marketing-api) | November 10, 2020 | August 25, 2021 |
| [v8.0](https://developers.facebook.com/docs/graph-api/changelog/version8.0#marketing-api) | August 4, 2020 | May 4, 2021 |
| [v7.0](https://developers.facebook.com/docs/graph-api/changelog/version7.0#marketing-api) | May 5, 2020 | March 3, 2021 |
| [v6.0](https://developers.facebook.com/docs/graph-api/changelog/version6.0#marketing-api) | February 3, 2020 | Extended to February 8, 2021 |
| [v5.0](https://developers.facebook.com/docs/graph-api/changelog/version5.0#marketing-api) | October 29, 2019 | September 28, 2020 |
| [v4.0](https://developers.facebook.com/docs/graph-api/changelog/version4.0) | July 29, 2019 | March 31, 2020 |
| [v3.3](https://developers.facebook.com/docs/graph-api/changelog/version3.3) | April 30, 2019 | January 13, 2020 |
| [v3.2](https://developers.facebook.com/docs/graph-api/changelog/version3.2) | October 23, 2018 | August 13, 2019 |
| [v3.1](https://developers.facebook.com/docs/graph-api/changelog/version3.1) | July 26, 2018 | May 14, 2019 |
| [v3.0](https://developers.facebook.com/docs/graph-api/changelog/version3.0) | May 1, 2018 | February 1, 2019 |
| [v2.12](https://developers.facebook.com/docs/graph-api/changelog/version2.12) | January 30, 2018 | August 7, 2018 |
| [v2.11](https://developers.facebook.com/docs/graph-api/changelog/version2.11) | November 7, 2017 | August 7, 2018 |
| [v2.10](https://developers.facebook.com/docs/graph-api/changelog/version2.10) | July 18, 2017 | May 8, 2018 |
| [v2.9](https://developers.facebook.com/docs/graph-api/changelog/version2.9) | April 18, 2017 | November 6, 2017 |
| [v2.8](https://developers.facebook.com/docs/graph-api/changelog/version2.8) | October 5, 2016 | July 26, 2017 |
| [v2.7](https://developers.facebook.com/docs/graph-api/changelog/version2.7) | July 13, 2016 | April 25, 2017 |
| [v2.6](https://developers.facebook.com/docs/graph-api/changelog/version2.6) | April 12, 2016 | October 5, 2016 |
| [v2.5](https://developers.facebook.com/docs/graph-api/changelog/version2.5) | October 7, 2015 | July 13, 2016 |
| [v2.4](https://developers.facebook.com/docs/graph-api/changelog/version2.4) | July 8, 2015 | April 11, 2016 |
| [v2.3](https://developers.facebook.com/docs/graph-api/changelog/version2.3) | March 25, 2015 | October 8, 2015 |
| [v2.2](https://developers.facebook.com/docs/graph-api/changelog/version2.2) | October 30, 2014 | July 8, 2015 |
| [v2.1](https://developers.facebook.com/docs/graph-api/changelog/version2.1) | October 1, 2014 | March 11, 2015 |
| v2.0 | October 1, 2014 | March 11, 2015 |
| v1.0 | October 1, 2014 | March 11, 2015 |

[](#)

[](#)