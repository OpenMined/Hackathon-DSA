
IG Hashtag Search - Instagram Platform - Documentation - Meta for Developers










Instagram Platform* Instagram Graph API
* Instagram Basic Display API
* Sharing to Feed
* Sharing to Stories
* oEmbed
* Embed Button
* Business Login for Instagram
IG Hashtag Search
=================


This root edge allows you to get IG Hashtag IDs.


Creating
--------


This operation is not supported.


Reading
-------


### Getting a Hashtag ID


`GET /ig_hashtag_search?user_id={user-id}&q={q}`


Returns the ID of an IG Hashtag. IDs are both static and global (i.e, the ID for `#bluebottle` will always be `17843857450040591` for all apps and all app users).


#### Query String Parameters


* `{user_id}` (required) — The ID of the IG User performing the request.
* `{q}` (required) — The hashtag name to query.


#### Limitations


* You can query a maximum of 30 unique hashtags within a 7 day period.
* The API will return a generic error for any queries that include hashtags that we have deemed sensitive or offensive.


**Requirements**




 Type | Description || Features | `Instagram Public Content Access` |
| Permissions | `instagram_basic`
If the token is from a User whose Page role was granted via the Business Manager, one of the following permissions is also required: `ads_management`, `business_management`, or `pages_read_engagement`. |
| Tokens | A User access token of a Facebook User who has been approved for tasks on the connected Facebook Page. |

#### Sample Request



```

curl -X GET \
 "https://graph.facebook.com/v18.0/ig_hashtag_search?user_id=17841405309211844&q=bluebottle&access_token={access-token}"
```
#### Sample Response



```
{
    "data": [
        {
            "id": "17843857450040591"
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







































 
