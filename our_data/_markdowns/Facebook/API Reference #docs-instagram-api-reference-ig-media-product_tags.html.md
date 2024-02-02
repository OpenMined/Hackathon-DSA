Product Tags - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG Media Product Tags
=====================

Represents product tags on an IG Media. See Product Tagging guide for complete usage details.

Creating
--------

**`POST /{ig-media-id}/product_tags`**

Create or update product tags on an existing IG Media.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Live, and Mentions are not supported.
* Tagging media is additive until the 5 tag limit has been reached. If the targeted media has already been tagged by a product in the request, the old tag's `x` and `y` values will be updated with their new values (a new tag will not be added).

### Requirements

 Type | Requirement || Access Tokens | User |
| Business Roles | The app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | The IG User that owns the IG Media must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `catalog_management`
`instagram_basic`
`instagram_shopping_tag_products`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
POST https://graph.facebook.com/{api-version}/{ig-media-id}/product_tags
  ?updated_tags={updated-tags}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `updated_tags` | `{updated-tags}` | **Required. Applies only to images and videos**. An array of objects specifying which product tags to tag the image or video with (maximum of 5; tags and product IDs must be unique). Each object should have the following information:
* `product_id` — **Required.** Product ID.
* `x` — **Images only.** An optional float that indicates percentage distance from left edge of the published media image. Value must be within `0.0`–`1.0` range.
* `y` — **Images only.** An optional float that indicates percentage distance from top edge of the published media image. Value must be within `0.0`–`1.0` range.
For example:
`[{product_id:'3231775643511089',x:0.5,y:0.8}]` |
### Response

An object indicating success or failure.

```
{
  "success": {success}
}
```
#### Response Contents

 Property | Value || `success` | Returns `true` if able to update the IG Media's product tags, otherwise returns `false`. |
### cURL Example

#### Request

```
curl -i -X POST \
 "https://graph.facebook.com/v19.0/90010778325754/product_tags?updated_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3859448974125379'%2C%0A%20%20%20%20x%3A%200.5%2C%0A%20%20%20%20y%3A%200.8%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:

```
https://graph.facebook.com/v19.0/90010778325754/product_tags?updated_tags=[
  {
    product_id:'3859448974125379',
    x: 0.5,
    y: 0.8
  }
]&access_token=EAAOc...
```
#### Response

```
{
  "success": true
}
```
Reading
-------

**`GET /{ig-media-id}/product_tags`**

Get a collection of product tags on an IG Media. See the Product Tagging guide for complete product tagging steps.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

 Type | Requirement || Access Tokens | User |
| Business Roles | The app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | The IG User that owns the IG Media must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `catalog_management`
`instagram_basic`
`instagram_shopping_tag_products`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-media-id}/product_tags
  ?access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
### Response

A JSON-formatted object containing an array of product tags on an IG Media. Responses can include the following product tag fields:

```
{
  "data": [
    {
      "product_id": {product-id},
      "merchant_id": {merchant-id},
      "name": "{name}",
      "price_string": "{price-string}",
      "image_url": "{image-url}",
      "review_status": "{review-status}",
      "is_checkout": {is-checkout},
      "stripped_price_string": "{stripped-price-string}",
      "string_sale_price_string": "{string-sale-price-string}",
      "x": {x},
      "y": {y}
    }
  ]
}
```
#### Response Contents

 Property | Value || `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `name` | Product name. |
| `price_string` | Price string. |
| `image_url` | Product image URL. |
| `review_status` | Product review status. Values can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
 |
| `is_checkout` | If `true`, product can be purchased directly through the Instagram app. If `false`, product can only be purchased on the merchant's website. |
| `stripped_price_string` | Product short price string (price displayed in constrained spaces, such as `$100` instead of `100 USD`). |
| `string_sale_price_string` | Product sale price. |
| `x` | A float that indicates percentage distance from left edge of media image. Value within `0.0`–`1.0` range. |
| `y` | A float that indicates percentage distance from top edge of media image. Value within `0.0`–`1.0` range. |
### cURL Example

#### Request

```
curl -i -X GET \
 "https://graph.facebook.com/v19.0/90010778325754/product_tags?access_token=EAAOc..."
```
#### Response

```
{
  "data": [
    {
      "product_id": 3231775643511089,
      "merchant_id": 90010177253934,
      "name": "Gummy Bears",
      "price_string": "$3.50",
      "image_url": "https://scont...",
      "review_status": "approved",
      "is_checkout": true,
      "stripped_price_string": "$3.50",
      "stripped_sale_price_string": "$3",
      "x": 0.5,
      "y": 0.80000001192093
    }
  ]
}
```
Updating
--------

See Creating.

Deleting
--------

**`DELETE /{ig-media-id}/product_tags`**

Delete product tags on an existing IG Media.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

 Type | Requirement || Access Tokens | User |
| Business Roles | The app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | The IG User that owns the IG Media must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `catalog_management`
`instagram_basic`
`instagram_shopping_tag_products`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
DELETE https://graph.facebook.com/{api-version}/{ig-media-id}/product_tags
  ?deleted_tags={deleted-tags}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `deleted_tags` | `{deleted-tags}` | **Required.** An array containing the following information for each product tag to be deleted
* `merchant_id` — **Required.** Merchant ID.
* `product_id` — **Required.** Product ID.
 |
### Response

An object indicating success or failure.

```
{
  "success": {success}
}
```
#### Response Contents

 Property | Value || `success` | Returns `true` if able to delete the specified product tags on the IG Media, otherwise returns `false`. |
### cURL Example

#### Request

```
curl -i -X DELETE \
  "https://graph.facebook.com/v19.0/90010778325754/product_tags?deleted_tags=%5B%0A%20%20%7B%0A%20%20%20%20product_id%3A'3859448974125379'%2C%0A%20%20%20%20merchant_id%3A'90010177253934'%0A%20%20%7D%0A%5D&access_token=EAAOc..."
```
For reference, here is the HTML-decoded POST payload string:

```
https://graph.facebook.com/v12.0/90010778325754/product_tags?deleted_tags=[
  {
    product_id:'3859448974125379',
    merchant_id:'90010177253934'
  }
]&access_token=EAAOc...
```
#### Response

```
{
  "success": true
}
```