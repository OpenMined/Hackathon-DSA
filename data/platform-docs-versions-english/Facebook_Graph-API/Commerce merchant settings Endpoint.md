Commerce Merchant Settings
==========================

[](#)

Reading
-------

Commerce Merchant Settings object

Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

* `instagram_channel`
    

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Permisions

The system user needs to have

* `pages_read_engagement`
* `commerce_account_read_settings`
* Admin access for the Facebook Page connected to the Instagram handle

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}',
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
        "/{commerce-merchant-settings-id}",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

| Field | Description |
| --- | --- |
| `id`<br><br>numeric string | ID of the Commerce Merchant Settings |
| `braintree_merchant_id`<br><br>string | The Braintree Merchant ID (for BigCommerce) |
| `checkout_message`<br><br>string | Checkout Message of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `contact_email`<br><br>string | Contact email of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `cta`<br><br>enum | Shop's CTA (ie. onsite checkout, offsite, or contact-merchant) |
| `disable_checkout_urls`<br><br>bool | Ignore checkout\_urls for offsite links forthis merchant, if they exist on products. |
| `display_name`<br><br>string | Business display name |
| `external_merchant_id`<br><br>string | Merchant Identifier on External Partner Platforms (i.e. Shopify) |
| `facebook_channel`[](#)<br><br>CommerceFacebookChannel | Facebook channel settings |
| `feature_eligibility`<br><br>CommerceMerchantSettingsFeatureEligibility | Returns feature eligibilities for the Commerce Merchant Settings |
| `has_discount_code`<br><br>bool | Whether or not this merchant has discount code |
| `has_onsite_intent`<br><br>bool | This merchant selected onsite checkout during setup |
| `instagram_channel`[](#)<br><br>CommerceInstagramChannel | Instagram channel settings |
| `merchant_alert_email`<br><br>string | Place to send alert emails for the merchant |
| `merchant_page`<br><br>[Profile](https://developers.facebook.com/docs/graph-api/reference/profile/) | Profile of the merchant selling products<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `merchant_status`<br><br>enum | Current status of the merchant |
| `onsite_commerce_merchant`<br><br>CommerceMerchantSettingsOnsiteCommerceMerchant | Commerce Merchant Settings Info for the new commerce platform API |
| `payment_provider`<br><br>enum | Payment Provider for Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `privacy_url_by_locale`<br><br>list<KeyValue:string,string> | Map from locale to merchant privacy policy url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English. |
| `review_rejection_messages`<br><br>list<string> | Descriptive rejection messages corresponding to the given rejection reasons, if applicable |
| `review_rejection_reasons`<br><br>list<enum> | Reasons the merchant was rejected on review (for onboarding requests or performance metrics), if applicable |
| `supported_card_types`<br><br>list<enum> | Credit card types supported by the merchant |
| `terms`<br><br>string | Terms of Commerce Merchant Settings<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `terms_url_by_locale`<br><br>list<KeyValue:string,string> | Map from locale to merchant terms url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English. |
| `whatsapp_channel`[](#)<br><br>CommerceWhatsAppChannel | WhatsApp Channel Settings |

### Edges

| Edge | Description |
| --- | --- |
| [`commerce_orders`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/commerce_orders/) | Orders for this merchant |
| [`commerce_payouts`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/commerce_payouts/) | The commerce payouts of this Page |
| [`order_management_apps`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/order_management_apps/) | App ID that is authorized to manage this shop |
| [`product_catalogs`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/product_catalogs/) | Product catalogs attached to this merchant |
| [`returns`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/returns/)[](#) | Order Returns for this Merchant |
| [`seller_issues`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/seller_issues/) | seller\_issues |
| [`setup_status`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/setup_status/) | Onboarding status for this merchant |
| [`shops`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/shops/) | The shops associated with the merchant. |
| [`tax_settings`](https://developers.facebook.com/docs/graph-api/reference/commerce-merchant-settings/tax_settings/) | Tax settings including information about fulfillment locations |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Acknowledge Orders
=============================================

[](#)

Reading
-------

You can't perform this operation on this endpoint.

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Commerce Orders
==========================================

[](#)

Reading
-------

CommerceMerchantSettingsCommerceOrders

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fcommerce_orders&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/commerce_orders HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/commerce_orders',
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
        "/{commerce-merchant-settings-id}/commerce_orders",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/commerce_orders",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/commerce_orders"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `filters`<br><br>array<enum {HAS\_FULFILLMENTS, HAS\_CANCELLATIONS, HAS\_REFUNDS, NO\_SHIPMENTS, NO\_CANCELLATIONS, NO\_REFUNDS}> | Various filters to sort through the orders |
| `state`<br><br>array<enum {FB\_PROCESSING, CREATED, IN\_PROGRESS, COMPLETED}> | The state of the order (added support for multi-item in v3.3+) |
| `updated_after`<br><br>datetime/timestamp | Updated after time |
| `updated_before`<br><br>datetime/timestamp | Updated before time |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [CommerceOrder](https://developers.facebook.com/docs/graph-api/reference/commerce-order/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Commerce Payouts
===========================================

[](#)

Reading
-------

The edge from a cms to all the commerce payouts made for that cms

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fcommerce_payouts&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/commerce_payouts HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/commerce_payouts',
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
        "/{commerce-merchant-settings-id}/commerce_payouts",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/commerce_payouts",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/commerce_payouts"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `end_time`<br><br>datetime/timestamp | The end time until which the payouts should be fetched |
| `start_time`<br><br>datetime/timestamp | The start time from which the payouts should be fetched |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommercePayout nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Order Management Apps
================================================

[](#)

Reading
-------

Apps authorized to manage orders for this shop

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Forder_management_apps&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/order_management_apps HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/order_management_apps',
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
        "/{commerce-merchant-settings-id}/order_management_apps",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/order_management_apps",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/order_management_apps"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [Application](https://developers.facebook.com/docs/graph-api/reference/application/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Product Catalogs
===========================================

[](#)

Reading
-------

CommerceMerchantSettingsProductCatalogs

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fproduct_catalogs&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/product_catalogs HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/product_catalogs',
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
        "/{commerce-merchant-settings-id}/product_catalogs",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/product_catalogs",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/product_catalogs"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of [ProductCatalog](https://developers.facebook.com/docs/marketing-api/reference/product-catalog/) nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Returns
==================================

[](#)

Reading
-------

All Returns on all channels for a particular Merchant

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Freturns&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/returns HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/returns',
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
        "/{commerce-merchant-settings-id}/returns",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/returns",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/returns"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `end_time_created`<br><br>datetime/timestamp | Default value: `1706026156`<br><br>Limit to returns created before a certain time |
| `merchant_return_id`<br><br>string | Filter to find returns with matching merchant\_return\_id, which was provided when approving/disapproving a return. |
| `start_time_created`<br><br>datetime/timestamp | Default value: `0`<br><br>Limit to returns created after a certain time |
| `statuses`<br><br>array<enum {APPROVED, DISAPPROVED, MERCHANT\_MARKED\_COMPLETED, REFUNDED, REQUESTED}> | Default value: `[]`<br><br>Filter by return status |

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommerceReturn nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Seller Issues
========================================

[](#)

Reading
-------

Seller Issues object which surfaces problems with sellers' accounts as well as suggested actions to fix.

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fseller_issues&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/seller_issues HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/seller_issues',
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
        "/{commerce-merchant-settings-id}/seller_issues",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/seller_issues",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/seller_issues"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommerceAPISellerIssue nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Setup Status
=======================================

[](#)

Reading
-------

This is the edge between the CommerceMerchantSettings and the onboarding status of the shop

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fsetup_status&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/setup_status HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/setup_status',
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
        "/{commerce-merchant-settings-id}/setup_status",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/setup_status",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/setup_status"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommerceMerchantSettingsSetupStatus nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Shops
================================

[](#)

Reading
-------

Returns the list of shops associated with merchant configuration.

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Fshops&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/shops HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/shops',
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
        "/{commerce-merchant-settings-id}/shops",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/shops",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/shops"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of Shop nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)

Commerce Merchant Settings Tax Settings
=======================================

[](#)

Reading
-------

This is the tax settings associated with this merchant - it will show you the fulfillment locations that you can use with purchases.

### New Page Experience

This endpoint is supported for [New Page Experience](https://developers.facebook.com/docs/pages/new-pages-experience/).

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bcommerce-merchant-settings-id%7D%2Ftax_settings&version=v18.0)

    GET /v18.0/{commerce-merchant-settings-id}/tax_settings HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{commerce-merchant-settings-id}/tax_settings',
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
        "/{commerce-merchant-settings-id}/tax_settings",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{commerce-merchant-settings-id}/tax_settings",
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
                                   initWithGraphPath:@"/{commerce-merchant-settings-id}/tax_settings"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

This endpoint doesn't have any parameters.

### Fields

Reading from this edge will return a JSON formatted result:

{
    "`data`": \[\],
    "`paging`": {}
}

#### `data`

A list of CommerceMerchantTaxSettings nodes.

#### `paging`

For more details about pagination, see the [Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/#paging).

### Error Codes

| Error | Description |
| --- | --- |
| 200 | Permissions error |

[](#)

Creating
--------

You can't perform this operation on this endpoint.

[](#)

Updating
--------

You can't perform this operation on this endpoint.

[](#)

Deleting
--------

You can't perform this operation on this endpoint.

[](#)