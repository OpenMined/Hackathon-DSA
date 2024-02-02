Graph API Reference v19.0: Commerce Merchant Settings - Documentation - Meta for Developers

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
Graph API Versionv19.0Commerce Merchant Settings
==========================
Reading
-------
Commerce Merchant Settings object

Starting September 14, 2021, the following fields will throw an error for version 12.0+ calls made by apps that lack the endpoint's required permissions. This change will apply to all versions on December 13, 2021.

* `instagram_channel`
### New Page Experience
This endpoint is supported for New Page Experience.### Permisions

The system user needs to have

* `pages_read_engagement`
* `commerce_account_read_settings`
* Admin access for the Facebook Page connected to the Instagram handle

### Example
HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDKGraph API Explorer
```
GET /v19.0/{commerce-merchant-settings-id} HTTP/1.1
Host: graph.facebook.com
```
```
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
```
```
/* make the API call */
FB.api(
    "/{commerce-merchant-settings-id}",
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
    "/{commerce-merchant-settings-id}",
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
                               initWithGraphPath:@"/{commerce-merchant-settings-id}"
                                      parameters:params
                                      HTTPMethod:@"GET"];
[request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                      id result,
                                      NSError *error) {
    // Handle the result
}];
```
If you want to learn how to use the Graph API, read our Using Graph API guide.### Parameters
This endpoint doesn't have any parameters.### Fields

| Field | Description |
| --- | --- |
| `id`numeric string | ID of the Commerce Merchant Settings
 |
| `braintree_merchant_id`string | The Braintree Merchant ID (for BigCommerce)
 |
| `checkout_message`string | Checkout Message of Commerce Merchant Settings
Default |
| `contact_email`string | Contact email of Commerce Merchant Settings
Default |
| `cta`enum | Shop's CTA (ie. onsite checkout, offsite, or contact-merchant)
 |
| `disable_checkout_urls`bool | Ignore checkout\_urls for offsite links forthis merchant, if they exist on products.
 |
| `display_name`string | Business display name
 |
| `external_merchant_id`string | Merchant Identifier on External Partner Platforms (i.e. Shopify)
 |
| `facebook_channel`CommerceFacebookChannel | Facebook channel settings
 |
| `feature_eligibility`CommerceMerchantSettingsFeatureEligibility | Returns feature eligibilities for the Commerce Merchant Settings
 |
| `has_discount_code`bool | Whether or not this merchant has discount code
 |
| `has_onsite_intent`bool | This merchant selected onsite checkout during setup
 |
| `instagram_channel`CommerceInstagramChannel | Instagram channel settings
 |
| `merchant_alert_email`string | Place to send alert emails for the merchant
 |
| `merchant_page`Profile | Profile of the merchant selling products
Default |
| `merchant_status`enum | Current status of the merchant
 |
| `onsite_commerce_merchant`CommerceMerchantSettingsOnsiteCommerceMerchant | Commerce Merchant Settings Info for the new commerce platform API
 |
| `payment_provider`enum | Payment Provider for Commerce Merchant Settings
Default |
| `privacy_url_by_locale`list<KeyValue:string,string> | Map from locale to merchant privacy policy url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English.
 |
| `review_rejection_messages`list<string> | Descriptive rejection messages corresponding to the given rejection reasons, if applicable
 |
| `review_rejection_reasons`list<enum> | Reasons the merchant was rejected on review (for onboarding requests or performance metrics), if applicable
 |
| `supported_card_types`list<enum> | Credit card types supported by the merchant
 |
| `terms`string | Terms of Commerce Merchant Settings
Default |
| `terms_url_by_locale`list<KeyValue:string,string> | Map from locale to merchant terms url. The locale follows the format of concatenating ISO language and country code with an underscore. For instance, en\_US represents U.S. English.
 |
| `whatsapp_channel`CommerceWhatsAppChannel | WhatsApp Channel Settings
 |
### Edges

| Edge | Description |
| --- | --- |
| `commerce_orders` | Orders for this merchant
 |
| `commerce_payouts` | The commerce payouts of this Page
 |
| `order_management_apps` | App ID that is authorized to manage this shop
 |
| `product_catalogs` | Product catalogs attached to this merchant
 |
| `returns` | Order Returns for this Merchant
 |
| `seller_issues` | seller\_issues
 |
| `setup_status` | Onboarding status for this merchant
 |
| `shops` | The shops associated with the merchant.
 |
| `tax_settings` | Tax settings including information about fulfillment locations
 |
### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |
Creating
--------
You can't perform this operation on this endpoint.Updating
--------
You can't perform this operation on this endpoint.Deleting
--------
You can't perform this operation on this endpoint.