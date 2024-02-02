::: {._4-u3 ._588p}
` POST /{ig-user-id}/mentions?media_id={media_id}&message={message} `

Creates an [IG Comment](/docs/instagram-api/reference/ig-comment) on an
[IG Media](/docs/instagram-api/reference/ig-media) object in which an
[IG User](/docs/instagram-api/reference/ig-user) has been \@mentioned in
a caption.

#### Limitations

-   Mentions on Stories are not supported.
-   Commenting on photos in which you were tagged is not supported.
-   Webhooks will not be sent if the Media upon which the comment or
    \@mention appears was created by an account that is set to private.

Query string parameters are optional unless indicated as required.

-   ` {media_id} ` (required) --- the media ID contained in the [Webhook
    notification](/docs/instagram-api/guides/webhooks#reply-caption-mention)
    payload
-   ` {message} ` (required) --- text to include in the commment

#### Permissions

A Facebook User [access
token](/docs/instagram-api/overview#authentication) with the following
permissions:

-   ` instagram_basic `
-   ` instagram_manage_comments `
-   ` pages_read_engagement `
-   ` pages_show_list `

<div>

If the token is from a User whose **Page role was granted via the
Business Manager** , one of the following permissions is also required:

-   ` ads_management `
-   ` pages_read_engagement `
-   ` business_management `

</div>

``` {._5s-8 .prettyprint .lang-curl}
curl -i -X POST \
 -d "media_id=17920112008063024" \
 -d "message=Thanks%20for%20the%20dinosaur!" \
 -d "access_token=a-valid-access-token-goes-here" \
 "https://graph.facebook.com/17841405309211844/mentions"
```

``` {._5s-8 .prettyprint .lang-js}
{
  "id": "17846319838228163"
}
```

` POST /{ig-user-id}/mentions?media_id={media_id}&comment_id={comment_id}&message={message} `

Creates an [IG Comment](/docs/instagram-api/reference/ig-comment) on an
[IG Comment](/docs/instagram-api/reference/ig-comment) in which an [IG
User](/docs/instagram-api/reference/ig-user) has been \@mentioned.

#### Limitations

-   Mentions on Stories are not supported.
-   Commenting on photos in which you were tagged is not supported.
-   Webhooks will not be sent if the Media upon which the comment or
    \@mention appears was created by an account that is set to private.

Query string parameters are optional unless indicated as required.

-   ` {comment_id} ` (required) --- the comment ID contained in the
    [Webhook
    notification](/docs/instagram-api/guides/webhooks#reply-comment-mention)
    payload
-   ` {media_id} ` (required) --- the media ID contained in the [Webhook
    notification](/docs/instagram-api/guides/webhooks#reply-caption-mention)
    payload
-   ` {message} ` (required) --- text to include in the commment

#### Permissions

A Facebook User [access
token](/docs/instagram-api/overview#authentication) with the following
permissions:

-   ` instagram_basic `
-   ` instagram_manage_comments `
-   ` pages_read_engagement `
-   ` pages_show_list `

<div>

If the token is from a User whose **Page role was granted via the
Business Manager** , one of the following permissions is also required:

-   ` ads_management `
-   ` pages_read_engagement `
-   ` business_management `

</div>

-   ` comment_id ` (required)
-   ` media_id ` (required)
-   ` message `

``` {._5s-8 .prettyprint .lang-code}
curl -i -X POST \
 -d "media_id=17920112008063024" \
 -d "comment_id=17918718562020960" \
 -d "message=Hope%20you%20enjoy%20your%20new%20T-Rex!" \
 -d "access_token=a-valid-access-token-goes-here" \
 "https://graph.facebook.com/17841405309211844/mentions"
```

``` {._5s-8 .prettyprint .lang-code}
{
  "id": "17846319838254687"
}
```
:::
