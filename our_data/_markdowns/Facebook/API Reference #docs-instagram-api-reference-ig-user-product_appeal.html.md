Product Appeal - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Product Appeal
======================

Represents a rejected product's appeal status. See Product Tagging guide for complete usage details.

Creating
--------

**`POST /{ig-user-id}/product_appeal`**

Appeal a rejected product.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

 Type | Requirement || Access Tokens | User |
| Business Roles | The app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | The IG User must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `catalog_management`
`instagram_basic`
`instagram_shopping_tag_products`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/product_appeal
  ?appeal_reason={appeal-reason}
  &product_id={product-id}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `appeal_reason` | `{appeal-reason}` | **Required.** Explanation of why the product should be approved. |
| `product_id` | `{product-id}` | **Required.** Product ID. |
### Response

An object indicating success or failure. Response does not indicate appeal outcome.

```
{
  "success": {success}
}
```
#### Response Contents

 Property | Value || `success` | Indicates if API accepted request (`true`) or did not accept request (`false`). Response does not indicate appeal outcome. |
### cURL Example

#### Request

```
curl -i -X POST \
 "https://graph.facebook.com/v19.0/90010177253934/product_appeal?appeal_reason=product%20is%20a%20toy%20and%20not%20a%20real%20weapon&product_id=4382881195057752&access_token=EAAOc..."
```
#### Response

```
{
  "success": true
}
```
Reading
-------

**`GET /{ig-user-id}/product_appeal`**

Get appeal status of a rejected product.

### Limitations

* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.

### Requirements

 Type | Requirement || Access Tokens | User |
| Business Roles | The app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | The IG User must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `catalog_management`
`instagram_basic`
`instagram_shopping_tag_products`
`pages_show_list`
If the app user was granted a role via the Business Manager on the Page connected to the targeted IG User, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-user-id}/product_appeal
  ?product_id={product-id}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |
### Query String Parameters

 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `product_id` | `{product-id}` | **Required.** Product ID. |
### Response

A JSON-formatted object containing an array of appeal status metadata.

```
{
  "data": [
    {
      "eligible_for_appeal": {eligible-for-appeal},
      "product_id": {product-id},
      "review_status": "{review-status}"
    }
  ]
}
```
#### Response Contents

 Property | Value || `eligible_for_appeal` | Indicates if decision can be appealed (yes if `true`, no if `false`). |
| `product_id` | Product ID. |
| `review_status` | Review status. Value can be:
* `approved` — Product is approved.
* `rejected` — Product was rejected
* `pending` — Still undergoing review.
* `outdated` — Product was approved but has been edited and requires reapproval.
* `""` — No review status.
* `no_review` — No review status.
 |
### cURL Example

#### Request

```
curl -i -X GET \
 "https://graph.facebook.com/v19.0/90010177253934/product_appeal?product_id=4029274203846188&access_token=EAAOc..."
```
#### Response

```
{
  "data": [
    {
      "product_id": 4029274203846188,
      "review_status": "approved",
      "eligible_for_appeal": false
    }
  ]
}
```
Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.