::: {._4-u3 ._588p}
If you subscribe to the ` story_insights ` field, we send your endpoint
a webhook notification containing user interaction metrics on a story,
after the story has expired.

#### Sample Story Insights Payload

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
[ { "entry": [ { "changes": [ { "field": "story_insights", "value": { "media_id": "18023345989012587", "exits": 1, "replies": 0, "reach": 17, "taps_forward": 12, "taps_back": 0, "impressions": 28 } } ], "id": "17841405309211844", // Instagram Business or Creator Account ID "time": 1547687043 } ], "object": "instagram" }
]
```

If you subscribe to the ` mentions ` field, we send your endpoint a
webhook notification whenever an Instagram user \@mentions an Instagram
Business or Creator Account in a comment or caption.

For example, here\'s a sample comment webhook notification payload sent
for an Instagram Business Account ( ` 17841405726653026 ` ):

#### Sample Comment \@Mention Payload

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
[ { "entry": [ { "changes": [ { "field": "mentions", "value": { "comment_id": "17894227972186120", "media_id": "17918195224117851" } } ], "id": "17841405726653026", "time": 1520622968 } ], "object": "instagram" }
]
```

### Get the Comment\'s Contents {#get-the-comment-s-contents}

To get the comment\'s contents, use the ` comment_id ` property to query
the
[` GET /{ig-user-id}/mentioned_comment `](/docs/instagram-api/reference/ig-user/mentioned_comment)
edge:

#### Sample Query

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
GET https://graph.facebook.com/17841405726653026 ?fields=mentioned_comment.comment_id(17894227972186120)
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "mentioned_comment": { "timestamp": "2018-03-20T00:05:29+0000", "text": "@bluebottle challenge?", "id": "17894227972186120" }, "id": "17841405726653026"
}
```

When you get the response, parse the payload for the ` text ` property
to determine if you want to respond to the comment. To respond, use the
webhook notification payload\'s ` caption_id ` and ` media_id ` property
values to query the
[` POST /{ig-user-id}/mentions `](/docs/instagram-api/reference/ig-user/mentions)
endpoint:

#### Sample Query

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
curl -i -X POST \ -d "comment_id=17894227972186120" \ -d "media_id=17918195224117851" \ -d "message=Challenge%20accepted!" \ -d "access_token={access-token}" \ "https://graph.facebook.com/17841405726653026/mentions"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "17911496353086895"
}
```

### Reply to Caption \@Mentions {#reply-caption-mention}

If you subscribe to the ` mentions ` field, we send your endpoint a
webhook notification whenever a user \@mentions an Instagram Business or
Creator Account in a comment or caption on a media object not owned by
the Business or Creator.

For example, here\'s a sample caption \@mention webhook notification
sent for an Instagram Business Account ( ` 17841405726653026 ` ):

#### Sample Caption \@Mention Webhook Notification

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
[ { "entry": [ { "changes": [ { "field": "mentions", "value": { "media_id": "17918195224117851" } } ], "id": "17841405726653026", "time": 1520622968 } ], "object": "instagram" }
]
```

### Get the Caption\'s Contents {#get-the-caption-s-contents}

To get the caption\'s contents, use the ` media_id ` property to query
the
[` GET /{ig-user-id}/mentioned_media `](/docs/instagram-api/reference/ig-user/mentioned_media)
edge:

#### Sample Query

``` {._5s-8 .prettyprint .lang-html .prettyprinted}
GET https://graph.facebook.com/17841405726653026 ?fields=mentioned_media.media_id(17918195224117851){caption,media_type}
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-js .prettyprinted}
{ "mentioned_media": { "caption": "@bluebottle There can be only one!", "media_type": "IMAGE", "id": "17918195224117851" }, "id": "17841405726653026"
}
```

### Parse the Payload and Respond

When you get the response, parse the payload for the ` caption `
property to determine if you want to respond to the comment. To respond,
use the webhook ` media_id ` property to query the
[` POST /{ig-user-id}/mentions `](/docs/instagram-api/reference/ig-user/mentions)
edge:

#### Sample Query

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
curl -i -X POST \ -d "media_id=17918195224117851" \ -d "message=MacLeod%20agrees!" \ -d "access_token={access-token}" \ "https://graph.facebook.com/17841405726653026/mentions"
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "17911496353086895"
}
```
:::
