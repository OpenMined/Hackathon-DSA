
Catalog Product Search - Instagram Platform - Documentation - Meta for Developers










Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Catalog Product Search
==============================


Represents products and product variants that match a given search string in an IG User's Instagram Shop product catalog. See Product Tagging guide for complete usage details.


Creating
--------


This operation is not supported.


Reading
-------


**`GET /{ig-user-id}/catalog_product_search`**


Get a collection of products that match a given search string within the targeted IG User's Instagram Shop catalog.


### Limitations


* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.
* Products with a `review_status` of `rejected` will be returned, however, IG Media cannot be tagged with rejected products.
* Although the API will not return an error when publishing a post tagged with an unapproved product, the tag will not appear on the published post until the product has been approved. Therefore, we recommend that you only allow your app users to publish posts with tags whose products have a `review_status` of `approved`. This field is returned for each product by default when you get an app user's eligible products.


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

GET https://graph.facebook.com/{api-version}/{ig-user-id}/catalog_product_search
  ?catalog_id={catalog-id}
  &q={q}
  &access_token={access-token}
```
### Path Parameters




 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters




 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `catalog_id` | `{catalog-id}` | **Required.** ID of catalog to search. |
| `q` | `{q}` | A string to search for in each product's name or SKU number (SKU numbers can be added in the **Content ID** column in the catalog management interface). If no string is specified, all tag-eligible products will be returned. |

### Response


A JSON-formatted object containing an array of tag-eligible products and their metadata. Supports cursor-based pagination.



```

{
  "data": [
    {
      "product_id": {product-id},
      "merchant_id": {merchant-id},
      "product_name": "{product-name}",
      "image_url": "{image-url}",
      "retailer_id": "{retailer-id}",
      "review_status": "{review-status}",
      "is_checkout_flow": {is-checkout-flow}
    }
  ]
}
```
#### Response Contents




 Property | Value || `product_id` | Product ID. |
| `merchant_id` | Merchant ID. |
| `product_name` | Product name. |
| `image_url` | Product image URL. |
| `retailer_id` | Retailer ID. |
| `review_status` | Review status. Values can be `approved`, `outdated`, `pending`, `rejected`. An approved product can appear in the app user's Instagram Shop, but an approved status does not indicate product availability (e.g, the product could be out of stock). Only tags associated with products that have a `review_status` of `approved` can appear on published posts. |
| `is_checkout_flow` | If `true`, product can be purchased directly in the Instagram app. If `false`, product must be purchased in the app user's app/website. |
| `product_variants` | Product IDs (`product_id`) and variant names (`variant_name`) of product variants. |

### cURL Example


#### Request



```

curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934/catalog_product_search?catalog_id=960179311066902&q=gummy&access_token=EAAOc"
```
#### Response



```

{
  "data": [
    {
      "product_id": 3231775643511089,
      "merchant_id": 90010177253934,
      "product_name": "Gummy Wombats",
      "image_url": "https://scont...",
      "retailer_id": "oh59p9vzei",
      "review_status": "approved",
      "is_checkout_flow": true,
      "product_variants": [
            {
              "product_id": 5209223099160494
            },
            {
              "product_id": 7478222675582505,
              "variant_name": "Green Gummy Wombats"
            }
          ]
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







































 
