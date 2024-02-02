
IG Hashtag - Instagram Platform - Documentation - Meta for Developers










Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG Hashtag
==========


Represents an Instagram hashtag.


Creating
--------


This operation is not supported.


Reading
-------


**`GET /{ig-hashtag-id}`**


Returns Fields and Edges on an IG Hashtag.


### Limitations


You can query a maximum of 30 unique hashtags within a 7 day period.


### Requirements




 Type | Description || Features | `Instagram Public Content Access` |
| Permissions | `instagram_basic`
If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| Tokens | The app user's User access token. |

### Request Syntax



```

GET https://graph.facebook.com/{ig-hashtag-id}
  ?fields={fields}
  &access_token={access-token}
```
### Query String Parameters


Include the following query string parameters to augment the request.




 Key | Value || `access_token`
**Required**
*String* | The app user's Instagram User Access Token. |
| `fields`
*Comma-separated list* | A comma-separated list of Fields and Edges you want returned. If omitted, default fields will be returned. |

### Fields


You can use the `fields` query string parameter to request the following Fields on an IG Hashtag.




 Field Name | Description || `id` | The hashtag's ID (included by default). IDs are static and global. |
| `name` | The hashtag's name, without the leading hash symbol. |

### Edges


You can request the following edges as path parameters or by using the `fields` query string parameter.




 Edge | Description || `recent_media` | Get a list of the most recently published photo and video IG Media objects published with a specific hashtag. |
| `top_media` | Returns the most popular photo and video IG Media objects that have been tagged with the hashtag. |

### Response


A JSON-formatted object containing default and requested Fields.



```

{
  "{field}":"{value}",
  ...
}
```
### Sample Request



```
GET https://graph.facebook.com/17841593698074073
  ?fields=id,name
  &access_token=EAADd...
```
### Sample Response



```
{
  "id": "17841593698074073",
  "name": "coke"
}
```
Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
