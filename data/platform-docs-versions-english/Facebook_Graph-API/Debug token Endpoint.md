This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/debug_token)

Debug-Token `/debug_token`
==========================

This endpoint returns metadata about a given access token. This includes data such as the user for which the token was issued, whether the token is still valid, when it expires, and what permissions the app has for the given user.

This may be used to programatically debug issues with large sets of access tokens.

Reading
-------

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=debug_token%3Finput_token%3D%257Binput-token%257D&version=v19.0)

    GET /v19.0/debug_token?input_token={input-token} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/debug_token?input_token={input-token}',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/debug_token?input_token={input-token}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/debug_token?input_token={input-token}",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/debug_token?input_token={input-token}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An [app access token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/#apptokens) or an app developer's [user access token](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/#usertokens) for the app associated with the `input_token` beiing inspected is required to access this endpoint.
    

### Parameters

| Name | Description | Type |
| --- | --- | --- |
| `input_token` | The Access Token that is being inspected. This parameter must be specified. | `string` |

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `data` | Data wrapper around the result. | `object` |
| `app_id` | The ID of the application this access token is for. | `string` |
| `application` | Name of the application this access token is for. | `string` |
| `error` | Any error that a request to the graph api would return due to the access token. | `object` |
| `code` | The error code for the error. | `int` |
| `message` | The error message for the error. | `string` |
| `subcode` | The error subcode for the error. | `int` |
| `expires_at` | Timestamp when this access token expires. | `unixtime` |
| `data_access_expires_at` | Timestamp when app's access to user data expires. | `unixtime` |
| `is_valid` | Whether the access token is still valid or not. | `bool` |
| `issued_at` | Timestamp when this access token was issued. | `unixtime` |
| `metadata` | General metadata associated with the access token. Can contain data like 'sso', 'auth\_type', 'auth\_nonce' | `object` |
| `profile_id` | For impersonated access tokens, the ID of the page this token contains. | `string` |
| `scopes` | List of permissions that the user has granted for the app in this access token. | `string[]` |
| `granular_scopes` | List of granular permissions that the user has granted for the app in this access token. If permission applies to all, targets will not be shown. | `shape('scope' => string,'target_ids' => ?int[],)[]` |
| `user_id` | The ID of the user this access token is for. | `string` |

Publishing and Deleting
-----------------------

You cannot perform these actions on this edge.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)