
IG User - Instagram Platform - Documentation - Meta for Developers










Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG User
=======


Represents an Instagram Business Account or an Instagram Creator Account.


Creating
--------


This operation is not supported.


Reading
-------


**`GET /{ig-user-id}`**


Get fields and edges on an Instagram Business or Creator Account.


### Requirements




 Type | Description || Access Tokens | User. |
| Business Roles | If you are requesting the `shopping_product_tag_eligibility` field for product tagging, the app user must have an admin role on the Business Manager that owns the IG User's Instagram Shop. |
| Instagram Shop | If you are requesting the `shopping_product_tag_eligibility` field for product tagging, the IG User must have an approved Instagram Shop with a product catalog containing products. |
| Permissions | `instagram_basic`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you also need one of the following:
`ads_management`
`business_management`
If you are requesting the `shopping_product_tag_eligibility` field for product tagging, you will also need:
`catalog_management`
`instagram_shopping_tag_products` |

### Request Syntax



```

GET https://graph.facebook.com/{api-version}/{ig-user-id}
  ?fields={fields}
  &access_token={access-token}

```
### Path Parameters




 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters




 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |
| `fields` | `{fields}` | Comma-separated list of IG User fields you want returned for each IG User in the result set. |

### Fields


Public fields can be returned by an edge using field expansion.




 Field Name | Description || `biography`
Public | Profile bio text. |
| `id`
Public | App-scoped User ID. |
| `ig_id` | Instagram User ID. Used with Legacy Instagram API, now deprecated. Use `id` instead. |
| `followers_count`
Public | Total number of Instagram users following the user. |
| `follows_count` | Total number of Instagram users the user follows. |
| `media_count`
Public | Total number of IG Media published on the user. |
| `name` | Profile name. |
| `profile_picture_url` | Profile picture URL. |
| `shopping_product_tag_eligibility` | Returns `true` if the app user has set up an Instagram Shop and is therefore eligible for product tagging, otherwise returns `false`. |
| `username`
Public | Profile username. |
| `website`
Public | Single profile website URL. |

### Edges




 Edge | Description || `business_discovery` | Get data about other Instagram Business or Instagram Creator IG Users. |
| `content_publishing_limit` | Represents an IG User's current content publishing usage. |
| `insights` | Represents social interaction metrics on an IG User. |
| `live_media` | Represents a collection of live video IG Media on an IG User. |
| `media` | Represents a collection of IG Media on an IG User. |
| `media_publish` | Publish an IG Container on an Instagram Business IG User. |
| `mentions` | Create an IG Comment on an IG Comment or captioned IG Media that an IG User has been @mentioned in by another Instagram user. |
| `mentioned_comment` | Get data on an IG Comment in which an IG User has been @mentioned by another Instagram user. |
| `mentioned_media` | Get data on an IG Media in which an IG User has been @mentioned in a caption by another Instagram user. |
| `recently_searched_hashtags` | Get IG Hashtags that an IG User has searched for within the last 7 days. |
| `stories` | Represents a collection of story IG Media objects on an IG User. |
| `tags` | Represents a collection of IG Media in which an IG User has been tagged by another Instagram user. |

### Response


A JSON-formatted object containing default and requested fields and edges.



```

{
  "{field}":"{value}",
  ...
}
```
### cURL Example


#### Request



```

curl -X GET \
  'https://graph.facebook.com/v18.0/17841405822304914?fields=biography%2Cid%2Cusername%2Cwebsite&access_token=EAACwX...'

```
#### Response



```

{
  "biography": "Dino data crunching app",
  "id": "17841405822304914",
  "username": "metricsaurus",
  "website": "http://www.metricsaurus.com/"
}
```
Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
