Field Expansion - Graph API - Documentation - Meta for Developers

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
Field Expansion
===============

If you test the `GET /me/feed` query in the Graph API Explorer, you will noticed that the request returned many objects and paginated the results. This is common for most edges.

#### Example Response

```
{
  "data": [
   {
      "created_time": "2021-04-30T01:37:07+0000",
      "message": "I’ll never forget it has a head.",
      "id": "10211998223264288_10222340566616408"
    },
    ...
    {
      "created_time": "2021-04-25T22:29:26+0000",
      "message": "Things you hear at my house: \"I accidentally made a cake.\"",
      "id": "10211998223264288_10222314489524497"
    }
  ],
  "paging": {
    "previous": "https://graph.facebook.com/v11.0/USER-ID/feed?access_token=ACCESS-TOKEN&pretty=0&__previous=1&since=1627322627&until&__paging_token=enc_AdB2fX...",
    "next": "https://graph.intern.facebook.com/v11.0/USER-ID/feed?access_token=ACCESS-TOKEN&pretty=0&until=1619389766&since&__paging_token=enc_AdAamX...&__previous"
  }
}
```
Field expansion allows you not only to limit the number of objects returned but also perform nested requests.

Limiting Results
----------------

Limiting allows you to control the number of objects returned in each set of paginated results. To limit results, add a `.limit()` argument to any field or edge.

For example, performing a GET request on your `/feed` edge may return hundreds of Posts. You can limit the number of Posts returned for each page of results by doing this:

```
curl -i -X GET "https://graph.facebook.com/USER-ID?fields=feed.limit(3)&access_token=ACCESS-TOKEN"
```
This returns all of the Posts on your User node, but limits the number of objects in each page of results to three. Notice that instead of specifying the Feed edge in the path URL (`/user/feed`), you specify it in the `fields` parameter (`?fields=feed`), which allows you to append the `.limit(3)` argument.

Here are the query results:

```
{
  "feed": {
    "data": [
      {
        "created_time": "2021-12-12T01:24:21+0000",
        "message": "This picture of my grandson with Santa",
        "id": "POST-ID"
      },
      {
        "created_time": "2021-12-11T23:40:17+0000",
        "message": ":)",
        "id": "POST-ID"      
      },
      {
        "created_time": "2021-12-11T23:31:38+0000",
        "message": "Thought you might enjoy this.",
        "id": "POST-ID"      
      }
    ],
    "paging": {
      "previous": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&since=1542820440&access_token=ACCESS-TOKEN&__paging_token=enc_AdC...&__previous=1",
      "next": "https://graph.facebook.com/v8.0/USER-ID/feed?format=json&limit=3&access_token=ACCESS-TOKEN&until=1542583212&__paging_token=enc_AdD..."
    }
  },
  "id": "USER-ID"
}
```
As you can see, only three objects appear in this page of paginated results. However, the response included a `next` field and URL which you can use to fetch the next page.

Nested Requests
---------------

The field expansion feature of the Graph API allows you to effectively nest multiple graph queries into a single call. For example, in a single call, you can ask for the first N photos of the first K albums. The response maintains the data hierarchy so developers do not have to weave the data together on the client. This is different from the batch requests feature which allows you to make multiple, potentially unrelated, Graph API calls in a single request.

Here is the general format that field expansion takes:

```
GET graph.facebook.com/{node-id}?fields=LEVEL-ONE{LEVEL-TWO}
```
`LEVEL-ONE` in this case would be one or more (comma-separated) fields or edges from the parent node. 
`LEVEL-TWO` would be one or more (comma-separated) fields or edges from the first level node.

There is no limitation to the amount of nesting of levels that can occur here. You can also use a `.limit(n)` argument on each field or edge to restrict how many objects you want to get.

This is easier to understand by seeing it in action, so here's an example query that will retrieve up to five posts your published, with the text from each individual post.

```
GET graph.facebook.com/me?fields=posts.limit(5){message}
```
We can then extend this a bit more and for each post object, we get the text and privacy setting of each post. By default the `privacy` field returns an object that contains information about five key:value pairs, `allow`, `deny`, `description`, `friends`, and `value`. In this query we only want one returned, the `value` key:value pair.

```
GET graph.facebook.com/me?fields=posts.limit(5){message,privacy{value}}
```
Now we can extend it again by retrieving the name of each photo, the picture URL, and the people tagged:

```
GET graph.facebook.com
  /me?fields=albums.limit(5){name, photos.limit(2){name, picture, tags.limit(2)}},posts.limit(5)
```
Let's look at an example using cursor-based pagination:

```
GET graph.facebook.com
  /me?fields=albums.limit(5){name,photos.limit(2).after(MTAyMTE1OTQwNDc2MDAxNDkZD){name,picture,tags.limit(2)}},posts.limit(5)
```
You can see how field expansion can work across nodes, edges, and fields to return really complex data in a single request.

#### Limitations

* Certain resources, including most of Marketing API, are unable to utilize field expansion on some or all connections.

Field Aliases
-------------

Many nodes and edges allow you to provide aliases for fields by using the `as` parameter. This will return data using fields that you already have in your application logic.

For example, you can retrieve an image in two sizes and alias the returned object fields as `picture_small` and `picture_larger`:

```
me?fields=id,name,picture.width(100).height(100).as(picture_small),picture.width(720).height(720).as(picture_large)
```
On success, Graph API returns this result:

```
{
  "id": "993363923726",
  "name": "Benjamin Golub",
  "picture_small": {
    "data": {
      "height": 100,
      "is_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/p100x100/11700890_10100330450676146_2622493406845121288_n.jpg?oh=82b9abe469c78486645783c9e70e8797&amp;oe=561D10AE&amp;__gda__=1444247939_661c0f48363f1d1a7d42b6f836687a04",
      "width": 100
    }
  },
  "picture_large": {
    "data": {
      "height": 720,
      "is_silhouette": false,
      "url": "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xft1/v/t1.0-1/11700890_10100330450676146_2622493406845121288_n.jpg?oh=dd86551faa2de0cd6b359feb5665b0a5&amp;oe=561E0B46&amp;__gda__=1443979219_f1abbbdfb0fb7dac361d7ae02b460638",
      "width": 720
    }
  }
}
```
Please note that not all nodes and edges support field aliasing. Endpoints that do not support aliasing will return an error. For example, the `User` node does not support aliasing, so if you tried to alias the `name` field as `my_name` you would receive an error like this:

```
{
  "error": {
    "message": "(#100) Unknown fields: my_name.",
    "type": "OAuthException",
    "code": 100
  }
}
```
Next Steps
----------

* Learn about Paginated Results.