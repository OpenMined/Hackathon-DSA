<div>

``` {._5s-8 .prettyprint .lang-curl .prettyprinted}
curl -X GET "https://graph.facebook.com/v18.0/video-id/thumbnails?access_token=page_access_token"
```

On success your app receives a list of VideoThumbnail objects for the
video.

``` {._5s-8 .prettyprint .lang-json .prettyprinted}
{
"id": "video-id-1",
"height": 1280,
"scale": 1,
"uri": "url-for-video-1",
"width": 720,
"is_preferred": false
},
{
"id": "video-id-2",
"height": 1280,
"scale": 1,
"uri": "url-for-video-2",
"width": 720,
"is_preferred": false
},
...
```

</div>
