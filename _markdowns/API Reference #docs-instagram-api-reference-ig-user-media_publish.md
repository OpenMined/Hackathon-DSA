
Media Publish - Instagram Platform - Documentation - Meta for Developers










Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG User Media Publish
=====================


Publish an IG Container on an Instagram Business IG User. Refer to the Content Publishing guide for complete publishing steps.


Creating
--------


**`POST /{ig-user-id}/media_publish`**


Publish an IG Container object on an Instagram Business IG User.


### Limitations


* Instagram accounts are limited to 25 API-published posts within a 24 hour moving period.
* If the Page connected to the targeted Instagram Business account requires Page Publishing Authorization (PPA), PPA must be completed or the request will fail.
* If the Page connected to the targeted Instagram Business account requires two-factor authentication, the Facebook User must also have performed two-factor authentication or the request will fail.
* Publishing to Instagram TV is not supported.


### Requirements




 Type | Description || Access Tokens | User |
| Business Roles | If publishing containers for product tagging, the app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | If publishing containers for product tagging, the IG User must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `instagram_basic`
`instagram_content_publish`
`pages_read_engagement` or `pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you will also need one of:
`ads_management`
`business_management`
If publishing containers for product tagging, you will also need:
`catalog_management`
`instagram_shopping_tag_products` |
| Tasks | The app user whose token is used in the request must be able to perform `MANAGE` or `CREATE_CONTENT` tasks on the Page connected to the targeted Instagram account. |

### Request Syntax



```
POST https://graph.facebook.com/{api-version}/{ig-user-id}/media_publish
  ?creation_id={creation-id}
  &access_token={access-token}
```
### Path Parameters




 Placeholder | Value || `{api-version}`
*String* | API version. |
| `{ig-user-id}`
**Required**
*String* | App user's app-scoped user ID. |

### Query String Parameters




 Key | Placeholder | Description || `access_token`
Required | `{access-token}` | The app user's User access token. |
| `creation_id`
Required | `{creation-id}` | The ID of the IG Container to be published. |

### Sample Request



```
POST graph.facebook.com
  /17841405822304914/media_publish
    ?creation_id=17889455560051444
```
### Sample Response



```

{
  "id": "17920238422030506"
}

```
Reading
-------


This operation is not supported.


Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
