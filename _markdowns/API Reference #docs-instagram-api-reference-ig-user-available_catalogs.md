
Available Catalogs - Instagram Platform - Documentation - Meta for Developers










Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Available Catalogs
==========================


Represents a collection of product catalogs in an IG User's Instagram Shop. See Product Tagging guide for complete usage details.


Creating
--------


This operation is not supported.


Reading
-------


**`GET /{ig-user-id}/available_catalogs`**


Get the product catalog in an IG User's Instagram Shop.


### Limitations


* Instagram Creator accounts are not supported.
* Stories, Instagram TV, Reels, Live, and Mentions are not supported.
* Only returns data on a single catalog because Instagram Shops are limited to a single catalog.
* Collaborative catalogs (shopping partner or affiliate creator catalogs) are not supported.


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

GET https://graph.facebook.com/{api-version}/{ig-user-id}/available_catalogs
  ?fields={fields}
  &access_token={access-token}
```
### Path Parameters




 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** App user's app-scoped user ID. |

### Query String Parameters




 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `fields` | `{fields}` | Comma-separated list of catalog fields you want returned for each catalog in the result set. |

### Response


A JSON-formatted object containing the data you requested.



```

{
  "data": [
    {
      "catalog_id": "{catalog-id}",
      "catalog_name": "{catalog-name}",
      "shop_name": "{shop-name}",
      "product_count": {product-count}
    }
  ]
}
```
#### Response Contents




 Property | Value || `catalog_id` | Catalog ID. |
| `catalog_name` | Catalog name. |
| `shop_name` | Shop name. |
| `product_count` | Number of products in catalog. Includes all products regardless of review status. |

### cURL Example


#### Request



```

curl -i -X GET \
 "https://graph.facebook.com/v18.0/90010177253934/available_catalogs?access_token=EAAOc..."
```
#### Response



```

{
  "data": [
    {
      "catalog_id": "960179311066902",
      "catalog_name": "Jay's Favorite Snacks",
      "shop_name": "Jay's Bespoke",
      "product_count": 11
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







































 
