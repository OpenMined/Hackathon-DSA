
Graph API Reference v19.0: Page Call To Action - Documentation - Meta for Developers











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
Graph API Versionv19.0Page Call To Action
===================

Reading
-------



 
 Returns data on PageCallToAction node.
 
 
 ### New Page Experience

This endpoint is supported for New Page Experience.### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{page-call-to-action-id} HTTP/1.1
Host: graph.facebook.com
```

```
/* PHP SDK v5.0.0 */
/* make the API call */
try {
  // Returns a `Facebook\FacebookResponse` object
  $response = $fb->get(
    '/{page-call-to-action-id}',
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
```

```
/* make the API call */
FB.api(
    "/{page-call-to-action-id}",
    function (response) {
      if (response && !response.error) {
        /* handle the result */
      }
    }
);
```

```
/* make the API call */
new GraphRequest(
    AccessToken.getCurrentAccessToken(),
    "/{page-call-to-action-id}",
    null,
    HttpMethod.GET,
    new GraphRequest.Callback() {
        public void onCompleted(GraphResponse response) {
            /* handle the result */
        }
    }
).executeAsync();
```

```
/* make the API call */
FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                               initWithGraphPath:@"/{page-call-to-action-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Requirements



 Type | Description || App Review | Your app must be be approved for the following login permissions and features. |
| Login permissions | None |
| Features | Page Public Content Access |
| Tokens | A User access token for a User who has a role on the Page |
| Permissions | None |

### Parameters

This endpoint doesn't have any parameters.### Fields



| Field | Description |
| --- | --- |
| `id`numeric string | ID of the call-to-action
Default |
| `android_app`Application | App that stores the destination info on Android
 |
| `android_deeplink`string | Destination deeplink for the call-to-action on Android
 |
| `android_destination_type`enum | Destination type for the call-to-action on Android
 |
| `android_package_name`string | Destination app for the call-to-action on Android
 |
| `android_url`string | Destination url for the call-to-action on Android
 |
| `created_time`datetime | Time when the call-to-action was created
 |
| `email_address`string | Email address that can be contacted by a user
 |
| `from`Page | Page that owns the call-to-action
 |
| `intl_number_with_plus`string | International phone number with plus that can be called by a phone
 |
| `iphone_app`Application | App that stores the destination info on iPhone
 |
| `iphone_deeplink`string | Destination deeplink for the call-to-action on iPhone
 |
| `iphone_destination_type`enum | Destination type for the call-to-action on iPhone
 |
| `iphone_url`string | Destination url for the call-to-action on iPhone
 |
| `status`enum | Current running status of this action
Default |
| `type`enum | The type of action
Default |
| `updated_time`datetime | Time when the call-to-action was last updated
 |
| `web_destination_type`enum | Destination type for the call-to-action on desktop
 |
| `web_url`string | Destination url for the call-to-action on desktop
 |

### Error Codes



| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

Creating
--------

You can't perform this operation on this endpoint.Updating
--------

You can update a PageCallToAction by making a POST request to `/{page_call_to_action_id}`.### Requirements



 Type | Description || App Review | Your app must be be approved for the following login permissions and features. |
| Login permissions | `pages_manage_cta` |
| Features | None |
| Tokens | A Page access token for an admin of the Page |
| Permissions | `pages_manage_cta` |

### Parameters



| Parameter | Description |
| --- | --- |
| `android_app_id`int | ID of the App that stores the destination info on Android
 |
| `android_destination_type`enum {WEBSITE, APP\_DEEPLINK, FACEBOOK\_APP, PHONE\_CALL, MESSENGER, EMAIL, SHOP\_ON\_FACEBOOK, NONE, BECOME\_A\_VOLUNTEER, FOLLOW, MINI\_SHOP, MARKETPLACE\_INVENTORY\_PAGE, MOBILE\_CENTER, MENU\_ON\_FACEBOOK} | Destination type for the call-to-action on Android
 |
| `android_package_name`string | Destination app for the call-to-action on Android
 |
| `android_url`URL | Destination url for the call-to-action on Android
 |
| `email_address`string | Email address that can be contacted by a user
 |
| `intl_number_with_plus`string | International phone number with plus that can be called through a phone
 |
| `iphone_app_id`int | ID fo the App that stores the destination info on iPhone
 |
| `iphone_destination_type`enum {WEBSITE, APP\_DEEPLINK, FACEBOOK\_APP, PHONE\_CALL, MESSENGER, EMAIL, SHOP\_ON\_FACEBOOK, NONE, BECOME\_A\_VOLUNTEER, FOLLOW, MINI\_SHOP, MARKETPLACE\_INVENTORY\_PAGE, MENU\_ON\_FACEBOOK} | Destination type for the call-to-action on iPhone
 |
| `iphone_url`URL | Destination url for the call-to-action on iPhone
 |
| `type`enum {BOOK\_NOW, REQUEST\_QUOTE, CALL\_NOW, CHARITY\_DONATE, CONTACT\_US, DONATE\_NOW, MESSAGE, OPEN\_APP, PLAY\_NOW, SHOP\_NOW, SIGN\_UP, WATCH\_NOW, GET\_OFFER, GET\_OFFER\_VIEW, BOOK\_APPOINTMENT, LISTEN, EMAIL, LEARN\_MORE, REQUEST\_APPOINTMENT, GET\_DIRECTIONS, BUY\_TICKETS, PLAY\_MUSIC, VISIT\_GROUP, SHOP\_ON\_FACEBOOK, LOCAL\_DEV\_PLATFORM, INTERESTED, WOODHENGE\_SUPPORT, BECOME\_A\_VOLUNTEER, VIEW\_SHOP, PURCHASE\_GIFT\_CARDS, FOLLOW\_PAGE, ORDER\_FOOD, VIEW\_INVENTORY, MOBILE\_CENTER, VIEW\_MENU} | The type of action
 |
| `web_destination_type`enum {EMAIL, MESSENGER, NONE, WEBSITE, SHOP\_ON\_FACEBOOK, BECOME\_SUPPORTER, BECOME\_A\_VOLUNTEER, FOLLOW, MOBILE\_CENTER} | Destination type for the call-to-action on desktop
 |
| `web_url`URL | Destination url for the call-to-action on desktop
 |

### Return Type

This endpoint supports read-after-write and will read the node to which you POSTed. Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |
| 100 | Invalid parameter |

Deleting
--------

You can delete a PageCallToAction by making a DELETE request to `/{page_call_to_action_id}`.### Requirements



 Type | Description || App Review | Your app must be be approved for the following login permissions and features. |
| Login permissions | `pages_manage_cta` |
| Features | None |
| Tokens | A Page access token for an admin of the Page |
| Permissions | `pages_manage_cta` |

### Parameters

This endpoint doesn't have any parameters.### Return Type

 Struct {`success`: bool, }### Error Codes



| Error | Description |
| --- | --- |
| 200 | Permissions error |


































