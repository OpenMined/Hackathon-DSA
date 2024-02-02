
Payment - Graph API - Documentation - Meta for Developers












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
This document refers to an outdated version of Graph API. Please use the latest version.Graph API Versionv18.0Payment `/{payment-id}`
=======================

The details of a payment made in an app using Facebook Payments.

Reading
-------

HTTPPHP SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{payment-id} HTTP/1.1
Host: graph.facebook.com
```

```
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
```

```
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
```

```
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
```
### Permissions

* An app access token for the app that created the payment is required.

### Fields



 
Name
 | 
Description
 | 
Type
 || `id` | The payment ID | `string` |
| `user` | The consumer's first and last name along with their user `id`. May be omitted in some cases. | `User` |
| `request_id` | The unique, optional app-created identifier passed into the JS function (255 character maximum) | `string` |
| `application` | The app associated with this payment | `App` |
| `actions` | The list of different action types that have occurred in this payment. | object[] |
| `type` | The type of this particular action. `type` can be:* `charge`: This designates the type of action that was taken on this payment was a charge. If the charge has a status of completed, then you should fulfill the order.
* `refund`: The refund type designates the payment has been refunded and the item sold to the consumer should be retracted if possible as you will no longer be paid out for this transaction.
* `chargeback`: A chargeback is initiated by a consumer with their bank disputing the payment in question. When a chargeback occurs, you should retract the in-game item from the costumer where possible as you will not be paid out for this order.
* `chargeback_reversal`: A chargeback\_reversal occurs when a chargeback is retroactively reversed. In this case, you should reinstate the consumer's in-game item if possible as you will now be paid out for this payment.
* `decline`: A decline occurs when a funding source used to create a bundled transaction is declined at the moment of processing the payment. You should retract the in-game item from the consumer where possible as you will not be paid out for this order. More information on bundled transactions and declines can be found in Handling Disputes and Refunds.
 | `string` |
| `status` | The status for this particular action. `status` can be:* `initiated`: An initiated payment designates the payment was only initiated but not yet fully completed. You should not fulfill an order of this type with the consumer and you should not receive a real time update for a payment with this status. You will however get a real time update when the corresponding transaction is completed. Developers may see initiated state for certain payment methods which requires long time to settle, for example, certain methods require the costumer to fill-in a form online, print out a receipt and go to the bank offline to pay.
* `completed`: A completed status means the action was successfully completed. If the type was a charge you will want to fulfill the order to the consumer at this time. Similarly, if the action type was a refund you will want to retract the item from the consumer.
* `failed`: This designates a failed action for the underlying type. This value can be present for both a charge action type as well as a refund action type.
 | `string` |
| `amount` | The amount of money covered by this action. | `string` |
| `currency` | The currency of the above `amount` in this action. | `string` |
| `time_created` | When this action occurred. | `datetime` |
| `time_updated` | When this action was last updated. | `datetime` |
| `tax_amount` | The amount reduced from your payout for any taxes remitted by Facebook. If `tax` is equal to `not_taxed` or `already_paid` this field will be omitted. | `string` |
| `items` | The items associated with the payment. | object[] |
| `type` | The type of this item. | `enum{IN_APP_PURCHASE, SUBSCRIPTION}` |
| `product` | The product URL of this item. | `string` |
| `quantity` | The number of this item purchased. | `integer` |
| `country` | Buyer's ISO Country Code, for tax purposes. | `string` |
| `tax` | The tax parameter specifies if a payment is subject to tax (VAT or sales tax) and, if so, how the tax was paid. This can take on the following values:* `not_taxed`: There's no VAT on this payment because it came from outside the European Union.
* `already_paid`: The tax on this payment has already been paid by the user's mobile carrier or other upstream party
* `tax_remitted`: Facebook paid the VAT on this payment on your behalf. The tax amount will be deducted from your payout. See here for more information.
* `tax_remitted_USMPF`: Facebook collected and paid sales tax on this payment on your behalf. The tax amount will be deducted from your payout but will not affect your net payout as tax amount charged is in addition to the price of the good. See here for more information.
 | `string` |
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

You can create payments by using Facebook Payments.

Deleting
--------

You cannot delete payments using this API.

Updating
--------

You cannot update payments using this edge.

Edges
-----



 
Name
 | 
Description
 || /dispute | Updates the dispute status of a payment. |
| /refunds | Refunds a payment. |




































 
