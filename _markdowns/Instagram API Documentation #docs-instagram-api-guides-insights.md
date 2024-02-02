::: {._4-u3 ._588p}
To get metrics on an Instagram Business or Creator Account, query the
[` GET /{ig-user-id}/insights `](/docs/instagram-api/reference/ig-user/insights)
edge and specify the metrics you want returned.

#### Sample Request

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
GET graph.facebook.com/17841405822304914/insights ?metric=impressions,reach,profile_views &period=day
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "data": [ { "name": "impressions", "period": "day", "values": [ { "value": 32, "end_time": "2018-01-11T08:00:00+0000" }, { "value": 32, "end_time": "2018-01-12T08:00:00+0000" } ], "title": "Impressions", "description": "Total number of times the Business Account's media objects have been viewed", "id": "instagram_business_account_id/insights/impressions/day" }, { "name": "reach", "period": "day", "values": [ { "value": 12, "end_time": "2018-01-11T08:00:00+0000" }, { "value": 12, "end_time": "2018-01-12T08:00:00+0000" } ], "title": "Reach", "description": "Total number of times the Business Account's media objects have been uniquely viewed", "id": "instagram_business_account_id/insights/reach/day" }, { "name": "profile_views", "period": "day", "values": [ { "value": 15, "end_time": "2018-01-11T08:00:00+0000" }, { "value": 15, "end_time": "2018-01-12T08:00:00+0000" } ], "title": "Profile Views", "description": "Total number of users who have viewed the Business Account's profile within the specified period", "id": "instagram_business_account_id/insights/profile_views/day" } ]
}
```

To get metrics on a media object, query the
[` GET /{ig-media-id}/insights `](/docs/instagram-api/reference/ig-media/insights)
edge and specify the metrics you want returned.

#### Sample Request

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
GET graph.facebook.com/{media-id}/insights ?metric=engagement,impressions,reach
```

#### Sample Response

``` {._5s-8 .prettyprint .lang-code .prettyprinted}
{ "data": [ { "name": "engagement", "period": "lifetime", "values": [ { "value": 8 } ], "title": "Engagement", "description": "Total number of likes and comments on the media object", "id": "media_id/insights/engagement/lifetime" }, { "name": "impressions", "period": "lifetime", "values": [ { "value": 13 } ], "title": "Impressions", "description": "Total number of times the media object has been seen", "id": "media_id/insights/impressions/lifetime" }, { "name": "reach", "period": "lifetime", "values": [ { "value": 13 } ], "title": "Reach", "description": "Total number of unique accounts that have seen the media object", "id": "media_id/insights/reach/lifetime" } ]
}
```
:::
