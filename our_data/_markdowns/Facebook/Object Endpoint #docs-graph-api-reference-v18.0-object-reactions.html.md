Object Reactions - Graph API - Documentation - Meta for Developers

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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Object Reactions
================

This reference describes the `/reactions` edge that is common to multiple Graph API nodes. The structure and operations are the same for each node. The following objects have a `/reactions` edge:

|  |  |
| --- | --- |
| * Comment
* PagePost
* Post
 |  |
Reading
-------

Get reactions on an object.

View Insights for more information on Page and Post reactions.

### New Page Experience

This endpoint is supported for New Page Experience.

### Requirements

**Marketing Apps**

* `ads_management`
* `pages_read_engagement`
* `pages_show_list`

**Page Management Apps**

* `pages_show_list`

### Sample Request

The following example is a `GET` request made by a User who has reacted to their own object.

cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-post-id/reactions?access_token=your-user-access-token"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/your-post-id/reactions",
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/your-post-id/reactions"
           parameters:nil
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
```
FB.api(
  '/your-post-id/reactions',
  'GET',
  {},
  function(response) {
      // Insert your code here
  }
);
```
```
try {
  // Returns a `FacebookFacebookResponse` object
  $response = $fb->get(
    '/your-post-id/reactions',
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
```
#### The JSON Response

```
{
  "data": [
    {
      "id": "your-user-id",
      "name": "Your Name",
      "type": "HAHA"
    }
  ],
  "paging": {
    "cursors": {
      "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
      "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
    }
  }
}
```
If the User or Page has not reacted to the object being queried, `data` will be empty.

The following example is a `GET` request for the total reactions to an object.

cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-post-id
   ?fields=reactions.summary(total_count)
   &access_token=your-access-token"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/your-post-id",
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
Bundle parameters = new Bundle();
parameters.putString("fields", "reactions.summary(total_count)");
request.setParameters(parameters);
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/your-post-id"
           parameters:@{ @"fields": @"reactions.summary(total_count)",}
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
```
FB.api(
  '/your-post-id',
  'GET',
  {"fields":"reactions.summary(total_count)"},
  function(response) {
      // Insert your code here
  }
);
```
```
try {
  // Returns a `FacebookFacebookResponse` object
  $response = $fb->get(
    '/your-post-id',
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
```
The JSON Response if the User or Page has reacted to their own object.

```
{
  "reactions": {
    "data": [
      {
        "id": "your-user-id",
        "name": "Your Name",
        "type": "HAHA"
      }
    ],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total_count": 28
    }
  },
  "id": "your-post-id"
}
```
The JSON Response if the User or Page has **not** reacted to their own object.

```
{
  "reactions": {
    "data": [
    ],
    "paging": {
      "cursors": {
        "before": "QVFIUk5YbXFFbG8yVWVOa2w0ZAGhmSUNKMkZAZAOXZARbzJOMHM0TUFtZAnhJbWdPdkF4OURUTHJrQjFqQ2RQZAVN1UGxSVU5FWURENnE4OUFPeXFreU1jV09pdFJR",
        "after": "QVFIUkpsWVRkcVl6SlhsdWlrcGdudl8xVEhwVEJ5ZA3FXdG90bTRxam13NmJDUGpQVnB5ZA29lMG9FVmFaeU1BLW1hc2oZD"
      }
    },
    "summary": {
      "total_count": 28
    }
  },
  "id": "your-post-id"
}
```
A User or Page can only query their own reactions. Other Users' or Pages' reactions are unavailable due to privacy concerns.

The "like" reaction counts include both "like" and "care" reactions.

### Parameters

 Name | Description || `type`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |
### Fields

Reading from this edge will return a JSON formatted result

```
{
    "data": [],
    "paging": {},
    "summary": {}
}
```
`data`

The Profile of the Page or User running the query, if the object being queried was reacted to by the Page or User, and a list of reaction types:

 Field | Description || `type`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |
For reactions on Posts, this edge does not return a Profile except for the current user, if read with a user access token.

#### View the count of an individual reaction

cURLAndroid SDKObjective-CJava SDKPHP SDK
```
curl -i -X GET \
 "https://graph.facebook.com/your-object-id
   ?fields=reactions.type(LOVE).limit(0).summary(total_count)
   &access_token=your-access-token"
```
```
GraphRequest request = GraphRequest.newGraphPathRequest(
  accessToken,
  "/your-object-id",
  new GraphRequest.Callback() {
    @Override
    public void onCompleted(GraphResponse response) {
      // Insert your code here
    }
});
Bundle parameters = new Bundle();
parameters.putString("fields", "reactions.type(LOVE).limit(0).summary(total_count)");
request.setParameters(parameters);
request.executeAsync();
```
```
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
    initWithGraphPath:@"/your-object-id"
           parameters:@{ @"fields": @"reactions.type(LOVE).limit(0).summary(total_count)",}
           HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection, id result, NSError *error) {
    // Insert your code here
}];
```
```
FB.api(
  '/your-object-id',
  'GET',
  {"fields":"reactions.type(LOVE).limit(0).summary(total_count)"},
  function(response) {
      // Insert your code here
  }
);
```
```
try {
  // Returns a `FacebookFacebookResponse` object
  $response = $fb->get(
    '/your-object-id',
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
```
#### Example JSON Returned

```
{
  "reactions": {
    "data": [
    ],
    "summary": {
      "total_count": 3498
    }
  },
  "id": "your-object-id"
}
```
`paging`

For more details about pagination, see the Graph API's paging documentation. Adding `limit(0)` to `reactions` will remove `paging` from the output.

`summary`

Aggregated information about the edge, such as counts. Specify the fields to fetch in the summary param (like `summary=total_count`).

 Field | Description || `total_count`
unsigned int32 | Total number of reactions |
| `viewer_reaction`
enum {NONE, LIKE, LOVE, WOW, HAHA, SORRY, ANGRY} | The type of reaction a Page or User marked an object. |
### Error Codes

 Error | Description || 100 | Invalid parameter |
Creating
--------

This operation is not supported.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.