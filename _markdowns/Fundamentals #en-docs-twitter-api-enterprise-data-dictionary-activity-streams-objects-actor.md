::: {#twtr-dtc-main .dtc-rebrand-flag-on}
::: {#twtr-main .twtr-color-bg--white-neutral role="main"}
::: {.page-wrapper .documentation-page .twtr-color-bg--white-neutral}
::: {.page-content .twtr-container-wide .left-rail-container}
::: {.main-content .twtr-col-lg-6}
::: main-content__wrapper
::: c01-rich-text-editor
::: is-table-default
The actor object contains Twitter User account metadata that describes
the Twitter User which created the activity.

### []{#actor-object-dictionary} Data Dictionary

+-----------------------+-----------------------+-----------------------+
| Attribute             | Type                  | Description           |
+-----------------------+-----------------------+-----------------------+
| objectType            | string                | **\"objectType\":**   |
|                       |                       | \"person\"            |
+-----------------------+-----------------------+-----------------------+
| id                    | string                | The string            |
|                       |                       | representation of the |
|                       |                       | unique identifier for |
|                       |                       | this author. Example: |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |     "id:tw            |
|                       |                       | itter.com:2244994945" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| link                  |                       | \"http://www.t        |
|                       |                       | witter.com/TwitterDev |
+-----------------------+-----------------------+-----------------------+
| displayName           | String                | The name of the user, |
|                       |                       | as they've defined    |
|                       |                       | it. Not necessarily a |
|                       |                       | person's name.        |
|                       |                       | Typically capped at   |
|                       |                       | 50 characters, but    |
|                       |                       | subject to change.    |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |     "displa           |
|                       |                       | yName": "Twitter Dev" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| preferredUsername     | string                | The screen name,      |
|                       |                       | handle, or alias that |
|                       |                       | this user identifies  |
|                       |                       | themselves with.      |
|                       |                       | Unique but subject to |
|                       |                       | change. Use           |
|                       |                       | ` `{.docutils         |
|                       |                       | .lite                 |
|                       |                       | ral}[` id `{.docutils |
|                       |                       | .literal              |
|                       |                       | }]{.pre}` `{.docutils |
|                       |                       | .literal} as a user   |
|                       |                       | identifier whenever   |
|                       |                       | possible. Typically a |
|                       |                       | maximum of 15         |
|                       |                       | characters long, but  |
|                       |                       | some historical       |
|                       |                       | accounts may exist    |
|                       |                       | with longer names.    |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |     "preferredUs      |
|                       |                       | ername": "TwitterDev" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| location              | object                | **\"location\": {**   |
|                       |                       |                       |
|                       |                       | **\"objectType\":**   |
|                       |                       | \"place\" **,**       |
|                       |                       |                       |
|                       |                       | **\"displayName\":**  |
|                       |                       | \"127.0.0.1\"         |
|                       |                       |                       |
|                       |                       | **}**                 |
+-----------------------+-----------------------+-----------------------+
| links                 | array                 | *Nullable* . A URL    |
|                       |                       | provided by the user  |
|                       |                       | in association with   |
|                       |                       | their profile.        |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |            "links": [ |
|                       |                       |                       |
|                       |                       | **{**                 |
|                       |                       |                       |
|                       |                       | **\"href\":**         |
|                       |                       | \"ht                  |
|                       |                       | tps://developer.twitt |
|                       |                       | er.com/en/community\" |
|                       |                       | **,**                 |
|                       |                       |                       |
|                       |                       | **\"rel\":** \"me\"   |
|                       |                       |                       |
|                       |                       | **}**                 |
|                       |                       |                       |
|                       |                       | **\]**                |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| summary               | string                | *Nullable* . The      |
|                       |                       | user-defined UTF-8    |
|                       |                       | string describing     |
|                       |                       | their account.        |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |     "summar           |
|                       |                       | y": "The voice of the |
|                       |                       |  #TwitterDev team..." |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| protected             | Boolean               | When true, indicates  |
|                       |                       | that this user has    |
|                       |                       | chosen to protect     |
|                       |                       | their Tweets. See     |
|                       |                       | [About Public and     |
|                       |                       | Protected             |
|                       |                       | Tweets](http          |
|                       |                       | s://support.twitter.c |
|                       |                       | om/articles/14016-abo |
|                       |                       | ut-public-and-protect |
|                       |                       | ed-tweets){.reference |
|                       |                       | .external} . Example: |
+-----------------------+-----------------------+-----------------------+
| verified              | Boolean               | When true, indicates  |
|                       |                       | that the user has a   |
|                       |                       | verified account. See |
|                       |                       | [Verified             |
|                       |                       | Accounts](            |
|                       |                       | https://support.twitt |
|                       |                       | er.com/articles/11913 |
|                       |                       | 5-faqs-about-verified |
|                       |                       | -accounts){.reference |
|                       |                       | .external} . Example: |
+-----------------------+-----------------------+-----------------------+
| followersCount        | Int                   | The number of         |
|                       |                       | followers this        |
|                       |                       | account currently     |
|                       |                       | has. Under certain    |
|                       |                       | conditions of duress, |
|                       |                       | this field will       |
|                       |                       | temporarily indicate  |
|                       |                       | "0". Example:         |
+-----------------------+-----------------------+-----------------------+
| friendsCount          | Int                   | The number of users   |
|                       |                       | this account is       |
|                       |                       | following (AKA their  |
|                       |                       | "followings"). Under  |
|                       |                       | certain conditions of |
|                       |                       | duress, this field    |
|                       |                       | will temporarily      |
|                       |                       | indicate "0".         |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| listedCount           | Int                   | The number of public  |
|                       |                       | lists that this user  |
|                       |                       | is a member of.       |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| favoritesCount        | Int                   | The number of Tweets  |
|                       |                       | this user has liked   |
|                       |                       | in the account's      |
|                       |                       | lifetime. British     |
|                       |                       | spelling used in the  |
|                       |                       | field name for        |
|                       |                       | historical reasons.   |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| statusesCount         | Int                   | The number of Tweets  |
|                       |                       | (including retweets)  |
|                       |                       | issued by the user.   |
|                       |                       | Example:              |
+-----------------------+-----------------------+-----------------------+
| postedTime            | date                  | The UTC datetime that |
|                       |                       | the user account was  |
|                       |                       | created on Twitter.   |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |                       |
|                       |                       |   "postedTime": "2013 |
|                       |                       | -12-14T04:35:55.036Z" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+
| image                 | string                | A HTTPS-based URL     |
|                       |                       | pointing to the       |
|                       |                       | user's profile image. |
|                       |                       | Example:              |
|                       |                       |                       |
|                       |                       | ::: {                 |
|                       |                       | .code .javascript .la |
|                       |                       | st .highlight-python} |
|                       |                       | ::: highlight         |
|                       |                       |                       |
|                       |                       |     "im               |
|                       |                       | age": "https://pbs.tw |
|                       |                       | img.com/profile_image |
|                       |                       | s/1283786620521652229 |
|                       |                       | /lEODkLTh_normal.jpg" |
|                       |                       | :::                   |
|                       |                       | :::                   |
+-----------------------+-----------------------+-----------------------+

###  No longer supported (deprecated) attributes

###  []{#author-object-examples} Examples:
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
       "actor": {
        "objectType": "person",
        "id": "id:twitter.com:2244994945",
        "link": "http://www.twitter.com/TwitterDev",
        "displayName": "Twitter Dev",
        "postedTime": "2013-12-14T04:35:55.036Z",
        "image": "https://pbs.twimg.com/profile_images/1283786620521652229/lEODkLTh_normal.jpg",
        "summary": "The voice of the #TwitterDev team and your official source for updates, news, and events, related to the #TwitterAPI.",
        "friendsCount": 2039,
        "followersCount": 512197,
        "listedCount": 1662,
        "statusesCount": 3632,
        "twitterTimeZone": null,
        "verified": true,
        "utcOffset": null,
        "preferredUsername": "TwitterDev",
        "languages": [],
        "links": [
          {
            "href": "https://developer.twitter.com/en/community",
            "rel": "me"
          }
        ],
        "location": {
          "objectType": "place",
          "displayName": "127.0.0.1"
        },
        "favoritesCount": 2147
      }
    
```
:::
:::
:::

::: {.b19-code-snippet .twtr-component-space--md}
::: {.b19-snippet .b19__theme--light}
::: t05-inline-code-snippet
``` {.line-numbers .t05__pre--with-button}
 "actor": {
    "objectType": "person",
    "id": "id:twitter.com:6253282",
    "link": "http://www.twitter.com/TwitterAPI",
    "displayName": "Twitter API",
    "postedTime": "2007-05-23T06:01:13.000Z",
    "image": "https://pbs.twimg.com/profile_images/942858479592554497/BbazLO9L_normal.jpg",
    "summary": "Tweets about changes and service issues. Follow @TwitterDev for more.",
    "friendsCount": 39,
    "followersCount": 6054164,
    "listedCount": 12285,
    "statusesCount": 3689,
    "twitterTimeZone": null,
    "verified": true,
    "utcOffset": null,
    "preferredUsername": "TwitterAPI",
    "languages": [
      
    ],
    "links": [
      {
        "href": "https://developer.twitter.com",
        "rel": "me"
      }
    ],
    "favoritesCount": 4
  }
    
```
:::
:::
:::
:::
:::
:::
:::
:::
:::
