This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/payment)

Payment `/{payment-id}`
=======================

The details of a payment made in an app using [Facebook Payments](https://developers.facebook.com/docs/payments).

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=%7Bpayment-id%7D&version=v19.0)

    GET /v19.0/{payment-id} HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/{payment-id}',
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
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{payment-id}",
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
                                   initWithGraphPath:@"/{payment-id}"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token for the app that created the payment is required.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `id` | The payment ID | `string` |
| `user` | The consumer's first and last name along with their user `id`. May be omitted [in some cases](https://developers.facebook.com/docs/howtos/payments/fulfillment#graphapiverification). | [`User`](https://developers.facebook.com/docs/graph-api/reference/user) |
| `request_id` | The unique, optional app-created identifier passed into the JS function (255 character maximum) | `string` |
| `application` | The app associated with this payment | [`App`](https://developers.facebook.com/docs/graph-api/reference/app) |
| `actions` | The list of different action types that have occurred in this payment. | object\[\] |
| `type` | The type of this particular action. `type` can be:<br><br>* `charge`: This designates the type of action that was taken on this payment was a charge. If the charge has a status of completed, then you should fulfill the order.<br>* `refund`: The refund type designates the payment has been refunded and the item sold to the consumer should be retracted if possible as you will no longer be paid out for this transaction.<br>* `chargeback`: A chargeback is initiated by a consumer with their bank disputing the payment in question. When a chargeback occurs, you should retract the in-game item from the costumer where possible as you will not be paid out for this order.<br>* `chargeback_reversal`: A chargeback\_reversal occurs when a chargeback is retroactively reversed. In this case, you should reinstate the consumer's in-game item if possible as you will now be paid out for this payment.<br>* `decline`: A decline occurs when a funding source used to create a bundled transaction is declined at the moment of processing the payment. You should retract the in-game item from the consumer where possible as you will not be paid out for this order. More information on bundled transactions and declines can be found in [Handling Disputes and Refunds](https://developers.facebook.com/docs/howtos/payments/disputesrefunds#declines). | `string` |
| `status` | The status for this particular action. `status` can be:<br><br>* `initiated`: An initiated payment designates the payment was only initiated but not yet fully completed. You should not fulfill an order of this type with the consumer and you should not receive a real time update for a payment with this status. You will however get a real time update when the corresponding transaction is completed. Developers may see initiated state for certain payment methods which requires long time to settle, for example, certain methods require the costumer to fill-in a form online, print out a receipt and go to the bank offline to pay.<br>* `completed`: A completed status means the action was successfully completed. If the type was a charge you will want to fulfill the order to the consumer at this time. Similarly, if the action type was a refund you will want to retract the item from the consumer.<br>* `failed`: This designates a failed action for the underlying type. This value can be present for both a charge action type as well as a refund action type. | `string` |
| `amount` | The amount of money covered by this action. | `string` |
| `currency` | The currency of the above `amount` in this action. | `string` |
| `time_created` | When this action occurred. | `datetime` |
| `time_updated` | When this action was last updated. | `datetime` |
| `tax_amount` | The amount reduced from your payout for any taxes remitted by Facebook. If `tax` is equal to `not_taxed` or `already_paid` this field will be omitted. | `string` |
| `items` | The items associated with the payment. | object\[\] |
| `type` | The type of this item. | `enum{IN_APP_PURCHASE, SUBSCRIPTION}` |
| `product` | The product URL of this item. | `string` |
| `quantity` | The number of this item purchased. | `integer` |
| `country` | Buyer's ISO Country Code, for tax purposes. | `string` |
| `tax` | The tax parameter specifies if a payment is subject to tax (VAT or sales tax) and, if so, how the tax was paid. This can take on the following values:<br><br>* `not_taxed`: There's no VAT on this payment because it came from outside the European Union.<br>* `already_paid`: The tax on this payment has already been paid by the user's mobile carrier or other upstream party<br>* `tax_remitted`: Facebook paid the VAT on this payment on your behalf. The tax amount will be deducted from your payout. See here for [more information](https://developers.facebook.com/docs/payments/reference/taxes/euvat_overview).<br>    <br>* `tax_remitted_USMPF`: Facebook collected and paid sales tax on this payment on your behalf. The tax amount will be deducted from your payout but will not affect your net payout as tax amount charged is in addition to the price of the good. See here for [more information](https://developers.facebook.com/docs/payments/reference/taxes/us_overview). | `string` |
| `tax_country` | The country determined by Facebook for tax calculation of this purchase, given as an ISO 3166-1 alpha-2 country code. Note: This field is for your information only and it should not be used for any recalculation or reconciliation purposes. If `tax` is equal to `not_taxed` or `already_paid` this field will be omitted. | `string` |
| `created_time` | The time the payment was originally created. | `string` |
| `payout_foreign_exchange_rate` | Exchange rate used to calculate payout amount which is remitted in USD. | `float` |
| `disputes` | Contains the information related to a dispute, including the `user_comment` and `user_email` which is provided by the consumer when the dispute is initiated. Additionally contains the current status of the dispute, the time the dispute was created an an resolution reason, if available. | `object[]` |
| `user_comment` | Comment provided by the consumer when the dispute is initiated. | `string` |
| `user_email` | Email provided by the consumer when the dispute is initiated. | `string` |
| `time_created` | The time the dispute was created. | `datetime` |
| `status` | Current status of the dispute. | `enum{resolved, pending}` |
| `reason` | The reason the developer or Facebook gave to resolve the dispute, after it has been resolved. | `enum{pending, refunded_in_cash, granted_replacement_item, denied_refund, banned_user, refunded_by_facebook}` |
| `test` | Optional parameter that shows up when a payment is made by a payment tester listed in the app's dashboard. This represents a transaction that has not been charged to the consumer's payment instrument | `boolean` |

Publishing
----------

You can create payments by using [Facebook Payments](https://developers.facebook.com/docs/payments).

Deleting
--------

You cannot delete payments using this API.

Updating
--------

You cannot update payments using this edge.

Edges
-----

| Name | Description |
| --- | --- |
| [/dispute](https://developers.facebook.com/docs/graph-api/reference/payment/dispute) | Updates the dispute status of a payment. |
| [/refunds](https://developers.facebook.com/docs/graph-api/reference/payment/refunds) | Refunds a payment. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/payment/dispute)

[`/{payment-id}`](https://developers.facebook.com/docs/graph-api/reference/payment/)`/dispute`
==============================================================================================

Used to settle any payment disputes.

Reading
-------

You can't read this edge, use the `disputes` field on the parent Payment object.

Publishing
----------

You can use this edge to settle disputes:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{payment-id}/dispute HTTP/1.1
    Host: graph.facebook.com
    
    reason=DENIED_REFUND

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{payment-id}/dispute',
        array (
          'reason' => 'DENIED_REFUND',
        ),
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

    Bundle params = new Bundle();
    params.putString("reason", "DENIED_REFUND");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{payment-id}/dispute",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"reason": @"DENIED_REFUND",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{payment-id}/dispute"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to settle any disputes for that app.
    
* If the payment has not been disputed yet, the call will return an error.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `reason` | The reason you are settling this dispute. This is required. | `enum{GRANTED_REPLACEMENT_ITEM, DENIED_REFUND, BANNED_USER}` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

Deleting
--------

You can't delete using this edge.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

This document refers to an outdated version of Graph API. Please [use the latest version.](https://developers.facebook.com/docs/graph-api/reference/v19.0/payment/refunds)

[`/{payment-id}`](https://developers.facebook.com/docs/graph-api/reference/payment/)`/refunds`
==============================================================================================

Used to issue any payment refunds.

Reading
-------

You can't read this edge.

Publishing
----------

You can use this edge to initiate refunds:

HTTPPHP SDKAndroid SDKiOS SDK

    POST /v19.0/{payment-id}/refunds HTTP/1.1
    Host: graph.facebook.com
    
    currency=EUR&amount=1.00

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->post(
        '/{payment-id}/refunds',
        array (
          'currency' => 'EUR',
          'amount' => '1.00',
        ),
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

    Bundle params = new Bundle();
    params.putString("currency", "EUR");
    params.putString("amount", "1.00");
    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/{payment-id}/refunds",
        params,
        HttpMethod.POST,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    NSDictionary *params = @{
      @"currency": @"EUR",
      @"amount": @"1.00",
    };
    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/{payment-id}/refunds"
                                          parameters:params
                                          HTTPMethod:@"POST"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

### Permissions

* An app access token is required to issue any refunds for that app.
    

### Fields

| Name | Description | Type |
| --- | --- | --- |
| `currency` | The three-letter ISO code of the currency in which the refund amount is specified; it must be the same as the currency in which the original purchase was denominated. This is required. | `string` |
| `amount` | The amount to refund. This is required. It must be less than or equal to the `refundable_amount` field on the parent Payment object. | `string` |
| `reason` | The reason you are refunding this order. | `enum{MALICIOUS_FRAUD, FRIENDLY_FRAUD, CUSTOMER_SERVICE}` |

### Response

If successful:

{
  "success": true
}

Otherwise a relevant error message will be returned.

Deleting
--------

You can't delete using this edge.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)