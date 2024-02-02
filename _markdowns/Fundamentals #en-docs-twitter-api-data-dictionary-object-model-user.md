::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The user object contains Twitter user account metadata describing the
referenced user. The user object is the primary object returned in the
[users lookup](/en/docs/twitter-api/users/lookup/introduction.html)
endpoint. When requesting additional user fields on this endpoint,
simply use the fields parameter ` user.fields ` .

The user object can also be found as a child object and expanded in the
Tweet object. The object is available for expansion with
` ?expansions=author_id ` or ` ?expansions=in_reply_to_user_id ` to get
the condensed object with only default fields. Use the expansion with
the field parameter: ` user.fields ` when requesting additional fields
to complete the object.\

+-----------------+-----------------+-----------------+-----------------+
| Field value     | Type            | Description     | How it can be   |
|                 |                 |                 | used            |
+-----------------+-----------------+-----------------+-----------------+
| id (default)    | string          | The unique      | Use this to     |
|                 |                 | identifier of   | p               |
|                 |                 | this user.      | rogrammatically |
|                 |                 |                 | retrieve        |
|                 |                 | ` "id":         | information     |
|                 |                 |  "2244994945" ` | about a         |
|                 |                 |                 | specific        |
|                 |                 |                 | Twitter user.   |
+-----------------+-----------------+-----------------+-----------------+
| name (default)  | string          | The name of the |                 |
|                 |                 | user, as        |                 |
|                 |                 | they've defined |                 |
|                 |                 | it on their     |                 |
|                 |                 | profile. Not    |                 |
|                 |                 | necessarily a   |                 |
|                 |                 | person's name.  |                 |
|                 |                 | Typically       |                 |
|                 |                 | capped at 50    |                 |
|                 |                 | characters, but |                 |
|                 |                 | subject to      |                 |
|                 |                 | change.         |                 |
|                 |                 |                 |                 |
|                 |                 | ` "name":       |                 |
|                 |                 | "Twitter Dev" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| username        | string          | The Twitter     |                 |
| (default)       |                 | screen name,    |                 |
|                 |                 | handle, or      |                 |
|                 |                 | alias that this |                 |
|                 |                 | user identifies |                 |
|                 |                 | themselves      |                 |
|                 |                 | with. Usernames |                 |
|                 |                 | are unique but  |                 |
|                 |                 | subject to      |                 |
|                 |                 | change.         |                 |
|                 |                 | Typically a     |                 |
|                 |                 | maximum of 15   |                 |
|                 |                 | characters      |                 |
|                 |                 | long, but some  |                 |
|                 |                 | historical      |                 |
|                 |                 | accounts may    |                 |
|                 |                 | exist with      |                 |
|                 |                 | longer names.   |                 |
|                 |                 |                 |                 |
|                 |                 | ` "username":   |                 |
|                 |                 |  "TwitterDev" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| created_at      | date (ISO 8601) | The UTC         | Can be used to  |
|                 |                 | datetime that   | determine how   |
|                 |                 | the user        | long a someone  |
|                 |                 | account was     | has been using  |
|                 |                 | created on      | Twitter         |
|                 |                 | Twitter.        |                 |
|                 |                 |                 |                 |
|                 |                 | ` "created_at"  |                 |
|                 |                 | : "2013-12-14T0 |                 |
|                 |                 | 4:35:55.000Z" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| description     | string          | The text of     |                 |
|                 |                 | this user\'s    |                 |
|                 |                 | profile         |                 |
|                 |                 | description     |                 |
|                 |                 | (also known as  |                 |
|                 |                 | bio), if the    |                 |
|                 |                 | user provided   |                 |
|                 |                 | one.            |                 |
|                 |                 |                 |                 |
|                 |                 | ` "             |                 |
|                 |                 | description": " |                 |
|                 |                 | The voice of Tw |                 |
|                 |                 | itter's #DevRel |                 |
|                 |                 |  team, and your |                 |
|                 |                 |  official sourc |                 |
|                 |                 | e for updates,  |                 |
|                 |                 | news, & events  |                 |
|                 |                 | about Twitter's |                 |
|                 |                 |  API. \n\n#Blac |                 |
|                 |                 | kLivesMatter" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| entities        | object          | Contains        | Entities are    |
|                 |                 | details about   | JSON objects    |
|                 |                 | text that has a | that provide    |
|                 |                 | special meaning | additional      |
|                 |                 | in the user\'s  | information     |
|                 |                 | description.    | about hashtags, |
|                 |                 |                 | urls, user      |
|                 |                 | ` "ent          | mentions, and   |
|                 |                 | ities": { "url" | cashtags        |
|                 |                 | : { "urls": [ { | associated with |
|                 |                 |  "start": 0, "e | the             |
|                 |                 | nd": 23, "url": | description.    |
|                 |                 |  "https://t.co/ | Reference each  |
|                 |                 | 3ZX3TNiZCY", "e | respective      |
|                 |                 | xpanded_url": " | entity for      |
|                 |                 | /content/develo | further         |
|                 |                 | per-twitter/en/ | details.        |
|                 |                 | community", "di |                 |
|                 |                 | splay_url": "de | All user [      |
|                 |                 | veloper.twitter | start           |
|                 |                 | .com/en/communi | ]{.code-inline} |
|                 |                 | ty" } ] }, "des | indices are     |
|                 |                 | cription": { "u | inclusive,      |
|                 |                 | rls": [ { "star | while all user  |
|                 |                 | t": 0, "end": 2 | [ end           |
|                 |                 | 3, "url": "http | ]{.code-inline} |
|                 |                 | s://t.co/3ZX3TN | indices are     |
|                 |                 | iZCY", "expande | exclusive.      |
|                 |                 | d_url": "/conte |                 |
|                 |                 | nt/developer-tw |                 |
|                 |                 | itter/en/commun |                 |
|                 |                 | ity", "display_ |                 |
|                 |                 | url": "develope |                 |
|                 |                 | r.twitter.com/e |                 |
|                 |                 | n/community" }, |                 |
|                 |                 |  "hashtags": [  |                 |
|                 |                 | { "start": 23,  |                 |
|                 |                 | "end": 30, "tag |                 |
|                 |                 | ": "DevRel" },  |                 |
|                 |                 | { "start": 113, |                 |
|                 |                 |  "end": 130, "t |                 |
|                 |                 | ag": "BlackLive |                 |
|                 |                 | sMatter" }, "me |                 |
|                 |                 | ntions": [ { "s |                 |
|                 |                 | tart": 0, "end" |                 |
|                 |                 | : 10, "tag": "T |                 |
|                 |                 | witterDev" }, " |                 |
|                 |                 | cashtags": [ {  |                 |
|                 |                 | "start": 12, "e |                 |
|                 |                 | nd": 16, "tag": |                 |
|                 |                 |  "twtr" } ] } ` |                 |
|                 |                 |                 |                 |
|                 |                 | }               |                 |
+-----------------+-----------------+-----------------+-----------------+
| location        | string          | The location    |                 |
|                 |                 | specified in    |                 |
|                 |                 | the user\'s     |                 |
|                 |                 | profile, if the |                 |
|                 |                 | user provided   |                 |
|                 |                 | one. As this is |                 |
|                 |                 | a freeform      |                 |
|                 |                 | value, it may   |                 |
|                 |                 | not indicate a  |                 |
|                 |                 | valid location, |                 |
|                 |                 | but it may be   |                 |
|                 |                 | fuzzily         |                 |
|                 |                 | evaluated when  |                 |
|                 |                 | performing      |                 |
|                 |                 | searches with   |                 |
|                 |                 | location        |                 |
|                 |                 | queries.        |                 |
|                 |                 |                 |                 |
|                 |                 | ` "location"    |                 |
|                 |                 | : "127.0.0.1" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| pinned_tweet_id | string          | Unique          | Determine the   |
|                 |                 | identifier of   | Tweet pinned to |
|                 |                 | this user\'s    | the top of the  |
|                 |                 | pinned Tweet.   | user's profile. |
|                 |                 |                 | Can potentially |
|                 |                 | ` "pinned_twee  | be used to      |
|                 |                 | t_id": "1255542 | determine the   |
|                 |                 | 774432063488" ` | user's          |
|                 |                 |                 | language.       |
+-----------------+-----------------+-----------------+-----------------+
| pr              | string          | The URL to the  | Can be used to  |
| ofile_image_url |                 | profile image   | download this   |
|                 |                 | for this user,  | user\'s profile |
|                 |                 | as shown on the | image.          |
|                 |                 | user\'s         |                 |
|                 |                 | profile.        |                 |
|                 |                 |                 |                 |
|                 |                 | ` "profile_im   |                 |
|                 |                 | age_url": "http |                 |
|                 |                 | s://pbs.twimg.c |                 |
|                 |                 | om/profile_imag |                 |
|                 |                 | es/126717536400 |                 |
|                 |                 | 3901441/tBZNFAg |                 |
|                 |                 | A_normal.jpg" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| protected       | boolean         | Indicates if    |                 |
|                 |                 | this user has   |                 |
|                 |                 | chosen to       |                 |
|                 |                 | protect their   |                 |
|                 |                 | Tweets (in      |                 |
|                 |                 | other words, if |                 |
|                 |                 | this user\'s    |                 |
|                 |                 | Tweets are      |                 |
|                 |                 | private).       |                 |
|                 |                 |                 |                 |
|                 |                 | ` "prot         |                 |
|                 |                 | ected": false ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| public_metrics  | object          | Contains        | Can potentially |
|                 |                 | details about   | be used to      |
|                 |                 | activity for    | determine a     |
|                 |                 | this user.      | Twitter user's  |
|                 |                 |                 | reach or        |
|                 |                 | ` "public_      | influence,      |
|                 |                 | metrics": {     | quantify the    |
|                 |                 |          "follo | user's range of |
|                 |                 | wers_count": 50 | interests, and  |
|                 |                 | 7902,           | the user's      |
|                 |                 |    "following_c | level of        |
|                 |                 | ount": 1863,    | engagement on   |
|                 |                 |           "twee | Twitter.        |
|                 |                 | t_count": 3561, |                 |
|                 |                 |              "l |                 |
|                 |                 | isted_count": 1 |                 |
|                 |                 | 550         } ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| url             | string          | The URL         | A URL provided  |
|                 |                 | specified in    | by a Twitter    |
|                 |                 | the user\'s     | user in their   |
|                 |                 | profile, if     | profile. This   |
|                 |                 | present.        | could be a      |
|                 |                 |                 | homepage, but   |
|                 |                 | ` "url          | is not always   |
|                 |                 | ": "https://t.c | the case.       |
|                 |                 | o/3ZX3TNiZCY" ` |                 |
+-----------------+-----------------+-----------------+-----------------+
| verified        | boolean         | Indicates if    | Indicates       |
|                 |                 | this user is a  | whether or not  |
|                 |                 | verified        | this Twitter    |
|                 |                 | Twitter User.   | user has a      |
|                 |                 |                 | verified        |
|                 |                 | ` "ve           | account. A      |
|                 |                 | rified": true ` | verified        |
|                 |                 |                 | account lets    |
|                 |                 |                 | people know     |
|                 |                 |                 | that an account |
|                 |                 |                 | of public       |
|                 |                 |                 | interest is     |
|                 |                 |                 | authentic.      |
+-----------------+-----------------+-----------------+-----------------+
| withheld        | object          | Contains        |                 |
|                 |                 | withholding     |                 |
|                 |                 | details for     |                 |
|                 |                 | [withheld       |                 |
|                 |                 | content         |                 |
|                 |                 | ](https://help. |                 |
|                 |                 | twitter.com/en/ |                 |
|                 |                 | rules-and-polic |                 |
|                 |                 | ies/tweet-withh |                 |
|                 |                 | eld-by-country) |                 |
|                 |                 | , if            |                 |
|                 |                 | applicable.     |                 |
|                 |                 |                 |                 |
|                 |                 | \               |                 |
+-----------------+-----------------+-----------------+-----------------+
:::
:::

::: c01-rich-text-editor
::: is-table-default
In the following request, we are requesting fields for the user on the
[users lookup](/en/docs/twitter-api/users/lookup/introduction.html)
endpoint. Be sure to replace ` $BEARER_TOKEN ` with your own generated
[Bearer Token](/en/docs/authentication/oauth-2-0/bearer-tokens) .\
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button .t05__pre--wrap-text}
 curl --request GET 'https://api.twitter.com/2/users?ids=2244994945&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,url,username,verified,withheld&expansions=pinned_tweet_id' --header 'Authorization: Bearer $BEARER_TOKEN'

    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` line-numbers
 {
    "data": [
        {
            "id": "2244994945",
            "name": "Twitter Dev",
            "username": "TwitterDev",
            "location": "127.0.0.1",
            "entities": {
                "url": {
                    "urls": [
                        {
                            "start": 0,
                            "end": 23,
                            "url": "https://t.co/3ZX3TNiZCY",
                            "expanded_url": "/content/developer-twitter/en/community",
                            "display_url": "developer.twitter.com/en/community"
                        }
                    ]
                },
                "description": {
                    "hashtags": [
                        {
                            "start": 23,
                            "end": 30,
                            "tag": "DevRel"
                        },
                        {
                            "start": 113,
                            "end": 130,
                            "tag": "BlackLivesMatter"
                        }
                    ]
                }
            },
            "verified": true,
            "description": "The voice of Twitter's #DevRel team, and your official source for updates, news, & events about Twitter's API. \n\n#BlackLivesMatter",
            "url": "https://t.co/3ZX3TNiZCY",
            "profile_image_url": "https://pbs.twimg.com/profile_images/1267175364003901441/tBZNFAgA_normal.jpg",
            "protected": false,
            "pinned_tweet_id": "1255542774432063488",
            "created_at": "2013-12-14T04:35:55.000Z"
        }
    ],
    "includes": {
        "tweets": [
            {
                "id": "1255542774432063488",
                "text": "During these unprecedented times, what’s happening on Twitter can help the world better understand &amp; respond to the pandemic. \n\nWe're launching a free COVID-19 stream endpoint so qualified devs &amp; researchers can study the public conversation in real-time. https://t.co/BPqMcQzhId"
            }
        ]
    }
}
    
```
:::
:::
:::
:::
