
Tags - Instagram Platform - Documentation - Meta for Developers










Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Tags
====


Represents a collection of IG Media objects in which an IG User has been tagged by another Instagram user.


Creating
--------


This operation is not supported.


Reading
-------


**`GET /{ig-user-id}/tags`**


Returns a list of IG Media objects in which an IG User has been tagged by another Instagram user.


### Limitations


Private IG Media objects will not be returned.


### Requirements




 Type | Description || Access Tokens | User |
| Features | Not applicable. |
| Permissions | `instagram_basic`
`instagram_manage_comments`
`pages_read_engagement`
`pages_show_list`
If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| Tasks | The app user must be able to perform appropriate Tasks on the Page based on the Permissions requested by the app. |

### Request Syntax



```

GET https://graph.facebook.com/{ig-user-id}/tags
  ?fields={fields}
  &access_token={access-token}
```
### Query String Parameters


Include the following query string parameters to augment the request.




 Key | Value || `access_token`
**Required**
*String* | The app user's Instagram User Access Token. |
| `fields`
*Comma-separated list* | A comma-separated list of Fields and Edges you want included in the response. If omitted, default fields will be returned. |

### Fields


Use the `fields` query string parameter to specify fields you want included on any returned IG Media objects.


**v10.0 and older calls until September 7, 2021:** The `like_count` field on an IG Media will return `0` if the media owner has hidden like counts on it.


**v11.0+ calls, and all versions on September 7, 2021:** If indirectly querying an IG Media through another endpoint or field expansion, the `like_count` field will be omitted from API responses if the media owner has hidden like counts on it. Directly querying the IG Media (which can only be done by the IG Media owner) will return the actual like count, however, even if like counts have been hidden.


### Edges


Use the `fields` query string parameter to specify Edges you want included on any returned IG Media objects.


### Response


A JSON-formatted object containing IG Media objects.



```

{
  "{field}":"{value}",
  ...
}
```
### Pagination


This edge supports cursor-based pagination so the response will include `before` and `after` cursors if the response contains multiple pages of data. Unlike standard cursor-based pagination, however, the response will not include `previous` or `next` fields, so you will have to use the `before` and `after` cursors to construct `previous` and `next` query strings manually in order to page through the returned data set.


### Sample Request



```
GET graph.facebook.com/17841405822304914/tags
    ?fields=id,username
    &access_token=EAADd...
```
### Sample Response



```
{
  "data": [
    {
      "id": "18038...",
      "username": "keldo..."
    },
    {
      "id": "17930...",
      "username": "ashla..."
    },
    {
      "id": "17931...",
      "username": "jaypo..."
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







































 
