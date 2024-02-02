::: {._4-u3 ._588p}
You can get all of the comments on a media object, analyze and filter
the returned data set against specific criteria, then reply to any
comments that match your criteria.

First, query the
[` GET /{ig-media-id}/comments `](/docs/instagram-api/reference/ig-media/comments#read)
endpoint to get all of the comments and their IDs on the media object:

#### Sample Request

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
GET graph.facebook.com /17895695668004550/comments
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "data": [ { "timestamp": "2017-08-31T18:10:30+0000", "text": "I love this!", "id": "17873440459141021" }, { "timestamp": "2017-08-31T19:16:02+0000", "text": "This is awesome!", "id": "17870913679156914" }, ... // results truncated for brevity ]
}
```

Next, parse the returned results for comments that match whatever
criteria you are using and use the matching comments to [reply in the
comment thread to the Instagram
users](/docs/instagram-api/reference/ig-comment/replies#replying) who
made the comments:

#### Sample Request

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
POST graph.facebook.com /17870913679156914/replies?message=Thanks%20for%20sharing!
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "id": "17873440459141029"
}
```

If you have a lot of comments that you want to reply to, you could
[batch the replies into a single
request](/docs/graph-api/making-multiple-requests/) .
:::
