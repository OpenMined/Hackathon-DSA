
Collaborators - Instagram Platform - Documentation - Meta for Developers










Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Collaborators
=============


Represents a list of users who are added as collaborators on an IG Media object.


Creating
--------


This operation is not supported.


Reading
-------


Get a list of Instagram users as collaborators and their invitation status on an IG Media object.


**`GET /{ig-media-id}`**


### Limitations


* Up to 3 Instagram accounts can be added as collaborators
* Only IG users who have enabled collaborator tagging will be returned in the response
* Collaborators tagging supports Feed image, Reels and Carousel, Stories is not supported


### Requirements




 Type | Description || Access Tokens | User – User must have created the IG Media object |
| Permissions | `instagram_basic`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you also need one of the following:
`ads_management`
`business_management` |

### Request syntax



```
GET https://graph.facebook.com/{appi-version}/{ig-media-id}/collaborators
```
### Sample Response



```
{
  "data": [
    {
      "id": "90010775360791",
      "username": "realtest1",
      "invite_status": "Accpeted"
    },
    {
      "id": "17841449208283139",
      "username": "realtest2",
      "invite_status": "Pending"
    },
    {
      "id": "90011117049518",
      "username": "realtest3",
      "invite_status": "Declined"
    }
  ]
}
```
### Path Parameters




 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** IG User ID. |

### Query String Parameters




 Key | Placeholder | Value || `access_token` | `{access-token}` | **Required.** App user's User access token. |

### Response fields




 Field Name | Description || `id` | The App-scoped ID for the Instagram account of the potential collaborator |
| `invite_status` | The status for the invitation sent to a potential collaborator. Can be one of the following:* `Accepted`
* `Declined`
* `Pending`
 |
| `username` | Instagram profile username for the potential collaborator |

Updating
--------


This operation is not supported.


Deleting
--------


This operation is not supported.







































 
