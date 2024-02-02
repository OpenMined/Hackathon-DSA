<div>

<div>

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
This reference describes the ` /comments ` edge that is common to
multiple Graph API nodes. The structure and operations are the same for
each node. The following objects have a ` /comments ` edge:

  -- -- --
        
  -- -- --

It is possible for comment objects to have a ` /comments ` edge, which
is called *comment replies* . The structure is the same for these, but
attention should be paid to the [modifiers](#readmodifiers) for these
edges.
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Returns a comment on an object.

::: {._57yz ._7_72 ._3-8p}
::: _57y-
The ` id ` field for the ` /PAGEPOST-ID/comments ` endpoint will no
longer be returned for apps using the [Page Public Content Access
feature](https://developers.facebook.com/docs/pages/overview/permissions-features#features)
. To access the comment IDs for a Page post you must be able to perform
the [MODERATE
task](https://developers.facebook.com/docs/pages/overview/permissions-features#tasks)
on the Page being queried. This change is in effect for v11.0+ and will
be implement for all versions on September, 7, 2021.
:::
:::

### New Page Experience {#-new-page-experience}

The following objects ` /comments ` endpoint are supported for New Page
Experience:

+-----------------------------------+-----------------------------------+
|                                   | -   PagePost                      |
|                                   | -   Photo                         |
|                                   | -   Post                          |
|                                   | -   PostComment                   |
+-----------------------------------+-----------------------------------+

### Permissions {#readperms}

-   The same permissions required to view the parent object are required
    to view comments on that object.

### Limitations

-   Other users\' profile information and comments will not be returned
    when accessing user posts, photos, albums, videos, likes, and
    reactions unless authorized by those users.

-   Comments returned in a query are based on default filtering. To get
    all comments that can be returned depending on your permissions, set
    the ` filter ` parameter to ` stream ` or use the ` order ` field.

-   ::: fcb
    A [new
    Page](https://www.facebook.com/business/help/2752670058165459?id=418112142508425)
    can comment as the Page on new Pages or classic Pages. However, a
    classic Page can not comment on a new Page.
    :::

-   

-   

-   

### Example

::: _5z09
::: {#u_0_5_xt ._51xa ._5gt2 ._51xb}
[Graph API Explorer
](/tools/explorer/?method=GET&path=%7Bobject-id%7D%2Fcomments&version=v18.0){._42ft
._51tl .selected}
:::

::: _xmu
``` {#u_0_b_uY ._5gt1 .prettyprint .prettyprinted}
GET /v18.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com
```
:::
:::

### Parameters {#readmodifiers}

::: _5z09
::: _xmu
``` {#u_0_m_fH ._5gt1 .prettyprint .prettyprinted}
GET /v18.0/{object-id}/comments?summary=1&filter=toplevel HTTP/1.1
Host: graph.facebook.com
```
:::
:::

::: _57-c
+-----------------------------------+-----------------------------------+
| Parameter                         | Description                       |
+===================================+===================================+
| ` summary `                       | A summary of metadata about the   |
|                                   | comments on the object.           |
| *bool*                            | Importantly this metadata         |
|                                   | includes ` order ` which          |
|                                   | indicates how the comments are    |
|                                   | being sorted.                     |
+-----------------------------------+-----------------------------------+
| ` filter `                        | If a person can reply to a        |
|                                   | comment, you can filter comments  |
| *enum { toplevel, stream }*       | based on top level comments,      |
|                                   | comments that are made directly   |
|                                   | on the post, or the chronological |
|                                   | order of all comments.            |
|                                   |                                   |
|                                   | -   ` toplevel ` - This is the    |
|                                   |     default. It returns all       |
|                                   |     top-level comments in         |
|                                   |     chronological order, as       |
|                                   |     ordered on Facebook. This     |
|                                   |     filter is useful for          |
|                                   |     displaying comments in the    |
|                                   |     same structure as they appear |
|                                   |     on Facebook.                  |
|                                   | -   ` stream ` - All-level        |
|                                   |     comments in ` chronological ` |
|                                   |     order. This filter is useful  |
|                                   |     for comment moderation tools  |
|                                   |     where it is helpful to see a  |
|                                   |     chronological list of all     |
|                                   |     comments.                     |
+-----------------------------------+-----------------------------------+
:::

### Fields {#readfields}

An array of [Comment objects](/docs/graph-api/reference/comment/) in
addition to the following fields when ` summary ` is ` true ` in the
request.

::: _57-c
+-----------------------------------+-----------------------------------+
| Field                             | Description                       |
+===================================+===================================+
| ` order `                         | Order in which comments were      |
|                                   | returned.                         |
| *enum { chronological,            |                                   |
| reverse_chronological }*          | -   ` chronological ` : Comments  |
|                                   |     sorted by the oldest comments |
|                                   |     first.                        |
|                                   | -   ` reverse_chronological ` :   |
|                                   |     Comments sorted by the newest |
|                                   |     comments first.               |
+-----------------------------------+-----------------------------------+
| ` total_count `                   | The count of comments on this     |
|                                   | node. It is important to note     |
| *int32*                           | that this value changes depending |
|                                   | on the ` filter ` being used      |
|                                   | (where comment replies are        |
|                                   | available):                       |
|                                   |                                   |
|                                   | -   if ` filter ` is ` stream `   |
|                                   |     then ` total_count ` will be  |
|                                   |     a count of all comments       |
|                                   |     (including replies) on the    |
|                                   |     node.                         |
|                                   | -   if ` filter ` is ` toplevel ` |
|                                   |     then ` total_count ` will be  |
|                                   |     a count of all top-level      |
|                                   |     comments on the node.         |
|                                   |                                   |
|                                   | Note: ` total_count ` can be      |
|                                   | greater than or equal to the      |
|                                   | actual number of comments         |
|                                   | returned due to comment privacy   |
|                                   | or deletion.                      |
+-----------------------------------+-----------------------------------+
:::
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
Publish new comments to any object.

### New Page Experience {#-new-page-experience-2}

The following objects ` /comments ` endpoint are supported for New Page
Experience:

+-----------------------------------+-----------------------------------+
| -   Comments                      |                                   |
| -   PagePosts                     |                                   |
| -   Photo                         |                                   |
| -   Post                          |                                   |
+-----------------------------------+-----------------------------------+

### Permissions {#pubperms}

-   A Page access token requested by a person who can perform the
    ` MODERATE ` task on the Page

-   The ` pages_manage_engagement ` permission

Note, the ` can_comment ` field on individual [comment
objects](/docs/graph-api/reference/comment/) indicates whether it is
possible to reply to that comment.

### Example {#example-2}

::: _5z09
::: _xmu
``` {#u_0_z_3y ._5gt1 .prettyprint .prettyprinted}
POST /v18.0/{object-id}/comments HTTP/1.1
Host: graph.facebook.com message=This+is+a+test+comment
```
:::
:::

### Fields {#pubfields}

::: _57-c
+-----------------------------------+-----------------------------------+
| Name                              | Description                       |
+===================================+===================================+
| ` attachment_id `                 | An optional ID of a unpublished   |
|                                   | photo (see ` no_story ` field in  |
| *string*                          | [` /{                             |
|                                   | user-id}/photos `](/docs/graph-ap |
|                                   | i/reference/user/photos/#publish) |
|                                   | ) uploaded to Facebook to include |
|                                   | as a photo comment. One of        |
|                                   | ` attachment_id ` ,               |
|                                   | ` attachment_share_url ` ,        |
|                                   | ` attachment_url ` , ` message `  |
|                                   | , or ` source ` must be provided  |
|                                   | when publishing.                  |
+-----------------------------------+-----------------------------------+
| ` attachment_share_url `          | The URL of a GIF to include as a  |
|                                   | animated GIF comment. One of      |
| *string*                          | ` attachment_id ` ,               |
|                                   | ` attachment_share_url ` ,        |
|                                   | ` attachment_url ` , ` message `  |
|                                   | , or ` source ` must be provided  |
|                                   | when publishing.                  |
+-----------------------------------+-----------------------------------+
| ` attachment_url `                | The URL of an image to include as |
|                                   | a photo comment. One of           |
| *string*                          | ` attachment_id ` ,               |
|                                   | ` attachment_share_url ` ,        |
|                                   | ` attachment_url ` , ` message `  |
|                                   | , or ` source ` must be provided  |
|                                   | when publishing.                  |
+-----------------------------------+-----------------------------------+
| ` source `                        | A photo, encoded as form data, to |
|                                   | use as a photo comment. One of    |
| *[                                | ` attachment_id ` ,               |
| multipart/form-data](https://l.fa | ` attachment_share_url ` ,        |
| cebook.com/l.php?u=https%3A%2F%2F | ` attachment_url ` , ` message `  |
| www.w3.org%2FTR%2Fhtml401%2Finter | , or ` source ` must be provided  |
| act%2Fforms.html%23h-17.13.4.2&h= | when publishing.                  |
| AT1B_welIoHVZ_yCIjRGO_mTq55r0_1w5 |                                   |
| ocMHXx4ZpCyULkGJXrC7qP3EeIktScqVb |                                   |
| nInKiftqSwhHkpipWPNurdpUqlPoRuQPk |                                   |
| aRbL5rkcVomRXSP_7drlzDgWPKihGHOOe |                                   |
| 34mg9IaAGPTCYpyVBEXMYaDM0w6S5u8)* |                                   |
+-----------------------------------+-----------------------------------+
| ` message `                       | The comment text. One of          |
|                                   | ` attachment_id ` ,               |
| *string*                          | ` attachment_share_url ` ,        |
|                                   | ` attachment_url ` , ` message `  |
|                                   | , or ` source ` must be provided  |
|                                   | when publishing.                  |
|                                   |                                   |
|                                   | Mention other Facebook Pages in   |
|                                   | your ` message ` text using the   |
|                                   | following syntax:                 |
|                                   |                                   |
|                                   | ` @[page-id] `                    |
|                                   |                                   |
|                                   | Usage of [this feature is subject |
|                                   | to                                |
|                                   | review](/docs/apps/rev            |
|                                   | iew/feature#reference-MENTIONING) |
|                                   | .                                 |
+-----------------------------------+-----------------------------------+
:::

### Return Type {#pubresponse}

If successful, you will receive a JSON response with the newly created
comment ID. In addition, this endpoint supports
[read-after-write](/docs/graph-api/using-graph-api#read-after-write) and
can immediately return any fields returned by
[read](/docs/graph-api/reference/object/comments#read) operations.

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "{comment-id}"
}
```
:::
:::

::: {._4-u2 ._57mb ._1u44 ._3fw6 ._4-u8 ._3la3}
::: {._4-u3 ._588p}
You can\'t update using this edge.
:::
:::

</div>

</div>
