Insights - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
IG Media Insights
=================

Represents social interaction metrics on an IG Media object.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-media-id}/insights`**

Get insights data on an IG Media object.

### Limitations

* Insights data is not available for any media within an album IG Media.
* Story media metrics are only available for 24 hours, even if the stories are archived or highlighted. To get the latest insights for a story before it expires, set up a Webhook for the `Instagram` topic and subscribe to the `story_insights` field.
* Story media metrics with values less than 5 return an error code `10` with the message `(#10) Not enough viewers for the media to show insights`.
* For Stories created by users in Europe and Japan, the `replies` metric now returns a value of `0`.
* For Stories, replies made by users in Europe and Japan are not included in `replies` calculations.
* If insights data you are requesting does not exist or is currently unavailable, the API returns an empty data set instead of `0` for individual metrics.
* Data used to calculate metrics can be delayed up to 48 hours.

### Requirements

 Type | Description || Access Tokens | User |
| Permissions | `instagram_basic`
`instagram_manage_insights`
`pages_read_engagement`
`pages_show_list`
If the app user was granted a role on the Page via the Business Manager, you will also need one of:
`ads_management`
`business_management` |
### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Parameter | Value || `{access-token}`
Type: string | **Required**. App user's User access token. |
| `{metric}`
Type: Comma-separated list | **Required**. Comma-separated list of Metrics you want returned. |
### Metrics

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed.

`total_interactions`, which is listed as an alternative for some of the deprecated metrics, is currently only available using version 18.0 and does not work with older versions. When querying older versions before Dec 11, 2023, please use the `engagement` metric.

See the Changelog for more information.

#### Album Metrics

 Metric | Description || `carousel_album_engagement`
*Deprecated for v18.0+* | Total number of likes and IG Comments on the album IG Media object.
**Alternative metric:** `total_interactions` |
| `carousel_album_impressions`
*Deprecated for v18.0+* | Total number of times the album IG Media object has been seen.
**Alternative metrics:** `impressions` |
| `carousel_album_reach`
*Deprecated for v18.0+* | Total number of unique Instagram accounts that have seen the album IG Media object.
**Alternative metric:** `reach` |
| `carousel_album_saved`
*Deprecated for v18.0+* | Total number of unique Instagram accounts that have saved the album IG Media object.
**Alternative metric:** `saved` |
| `carousel_album_video_views`
*Deprecated for v18.0+* | Total number of unique Instagram accounts that have viewed video IG Media within the album.
**Alternative metric:** `video_views` |
#### Photo and Video Metrics

Metrics on media within an album are not supported. Get metrics on the album instead.

 Metric | Description || `engagement`
*Deprecated for v18.0+* | Sum of `likes_count`, `comment_count`, and `saved` counts on the IG Media.
**Alternative metric:** `total_interactions`
**Note:** You may see different results. `engagement` includes likes, comments and saves count while `total_interactions` includes likes, comments, saved and shares count. |
| `impressions` | Total number of times the IG Media object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the IG Media object. |
| `saved` | Total number of unique Instagram accounts that have saved the IG Media object. |
| `video_views` | Total number of times the video IG Media has been seen. For album IG Media, the number of times all videos within the album have been seen. |
#### Reels Metrics

 Metric | Description || `clips_replays_count` | The number of times your reel starts to play again after an initial play of your reel. This is defined as replays of 1ms or more in the same reel session. |
| `comments` | Number of comments on the reel. Metric in development. |
| `ig_reels_aggregated_all_plays_count` | The number of times your reel starts to play or replay after an impression is already counted. This is defined as plays of 1ms or more. Replays are counted after the initial play in the same reel session. |
| `ig_reels_avg_watch_time` | The average amount of time spent playing the reel. Metric in development. |
| `ig_reels_video_view_total_time` | The total amount of time the reel was played, including any time spent replaying the reel. Metric in development. |
| `likes` | Number of likes on the reel. Metric in development. |
| `plays` | Number of times the reels starts to play after an impression is already counted. This is defined as video sessions with 1 ms or more of playback and excludes replays. Metric in development. |
| `reach` | Number of unique accounts that have seen the reel at least once. Reach is different from impressions, which can include multiple views of a reel by the same account. Metric is estimated and in development. |
| `saved` | Number of saves of the reel. Metric in development. |
| `shares` | Number of shares of the reel. Metric in development. |
| `total_interactions` | Number of likes, saves, comments, and shares on the reel, minus the number of unlikes, unsaves, and deleted comments. Metric in development. |
#### Story Metrics

 Metric | Description || `exits`
*Deprecated for v18.0+* | Total number of times someone exited the story IG Media object.
**Alternative metric:** `navigation`
**Breakdown:** `story_navigation_action_type` |
| `impressions` | Total number of times the story IG Media object has been seen. |
| `reach` | Total number of unique Instagram accounts that have seen the story IG Media object. |
| `replies` | Total number of replies (IG Comments) on the story IG Media object. Value does not include replies made by users in some regions. These regions include: Europe starting December 1, 2020 and Japan starting April 14, 2021. If the Story was created by a user in one of these regions, returns a value of `0`. |
| `taps_forward`
*Deprecated for v18.0+* | Total number of taps to see this story IG Media object's next photo or video.
**Alternative metric:** `navigation`
**Breakdown:** `story_navigation_action_type` |
| `taps_back`
*Deprecated for v18.0+* | Total number of taps to see this story IG Media object's previous photo or video.
**Alternative metric:** `navigation`
**Breakdown:** `story_navigation_action_type` |
#### Sample Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17895695668004550/insights?metric=impressions,reach&access_token=IGQVJ...'
```
#### Sample Response

```
{
  "data": [
    {
      "name": "impressions",
      "period": "lifetime",
      "values": [
        {
          "value": 264
        }
      ],
      "title": "Impressions",
      "description": "Total number of times the media object has been seen",
      "id": "17855590849148465/insights/impressions/lifetime"
    },
    {
      "name": "reach",
      "period": "lifetime",
      "values": [
        {
          "value": 103
        }
      ],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen the media object",
      "id": "17855590849148465/insights/reach/lifetime"
    }
  ]
}
```
New Metrics
-----------

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &breakdown={breakdown}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-media-id}` | **Required.** IG Media ID. |
### Query String Parameters

 Key
  | 
 Placeholder
  | 
 Value
  || `access_token` | `{access-token}` | **Required.** The app user's User access token. |
| `breakdown` | `{breakdown}` | Designates how to break down result set into subsets. See Breakdown. |
| `metric` | `{metric}` | **Required.** Comma-separated list of Metrics you want returned. |
### Breakdown

You can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `action_type` — Only compatible with the profile\_activity metric. Break down results by profile UI component that viewers tapped or clicked after viewing the app user's profile. Response values can be:
	+ `BIO_LINK_CLICKED`
	+ `CALL`
	+ `DIRECTION`
	+ `EMAIL`
	+ `OTHER`
	+ `TEXT`
* `story_navigation_action_type` — Break down results by navigation action taken by the viewer upon viewing the media.
	+ `TAP_BACK`
	+ `TAP_EXIT`
	+ `TAP_FORWARD`
	+ `SWIPE_FORWARD`

Refer to the Metrics table to determine which metrics support breakdowns and which breakdowns they support. If you request a metric that doesn't support breakdowns, the API will return an error ("`An unknown error has occurred.`"), so be careful if requesting multiple metrics in a single query.

### Metrics

#### Post Metrics

The following metrics are available on image and video IG Media published as a Post. Album carousels and IGTV are not supported.

 Metric | Breakdown | Description || `comments` | n/a | The number of comments on your post. |
| `follows` | n/a | The number of accounts that started following you. |
| `likes` | n/a | The number of likes on your post. |
| `profile_activity` | `action_type` | The number of actions people take when they visit your profile after engaging with your post. |
| `profile_visits` | n/a | The number of times your profile was visited. |
| `shares` | n/a | The number of shares of your post. |
| `total_interactions` | n/a | The number of likes, saves, comments and shares on your post minus the number of unlikes, unsaves and deleted comments. |
#### Story Metrics

The following metrics are available on IG Media published as a Story.

 Metric
  | 
 Breakdown
  | 
 Description
  || `follows` | n/a | This is how many accounts started following you. |
| `navigation` | `story_navigation_action_type` | This is the total number of actions taken from your story. These are made up of metrics like exited, forward, back and next story. |
| `profile_activity` | `action_type` | The number of actions people take when they visit your profile after engaging with your story. |
| `profile_visits` | n/a | The number of times your profile was visited. |
| `shares` | n/a | The number of shares of your story. |
| `total_interactions` | n/a | The number of replies and shares for your story. |
### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

```
{
  "data": [
    {
      "name": "{name}",
      "period": "{period}",
      "values": [
        {
          "value": {value}
        }
      ],
      "title": "{title}",
      "description": "{description}",
      "total_value": {
        "value":{value},
        "breakdowns": [
          {
            "dimension_keys": [
              "{dimension-key-1}",
              "{dimension-key-2}"
              ...
            ],
            "results": [
              {
                "dimension_values": [
                  "dimension-value-1",
                  "dimension-value-2"
                  ...
                ],
                "value": {value}
              },
              ...
            ]
          }
        ]
      },
      "id": "{id}"
    }
  ]
}
```
### Response Contents

 Property
  | 
 Value Type
  | 
 Description
  || `data` | Array | An array containing an object describing your request results. |
| `name` | String | Metric name. |
| `period` | String | Period requested. Period is automatically set to `lifetime` in the request and cannot be changed, so this value will always be `lifetime`. |
| `values` | Array | An array containing an object describing requested metric values. |
| `value` | Integer | For `data.values.value`, sum of requested metric values.
For `data.total_value.value`, sum of requested breakdown values.
For `data.total_value.breakdowns.results.value`, sum of breakdown set values. |
| `title` | String | Metric title. |
| `description` | String | Metric description. |
| `id` | String | A string describing the query's path parameters. |
| `total_value` | Object | Object describing requested breakdown values (if breakdowns were requested). |
| `breakdowns` | Array | An array of objects describing the breakdowns requested and their results. |
| `dimension_keys` | Array | Array of strings describing breakdowns requested. |
| `results` | Array | An array of objects describing each breakdown set. |
| `dimension_values` | String | An array of strings describing breakdown set values. Values can be mapped to `dimension_keys`. |
| `paging` | Object | An object containing URLs used to request the next set of results. See Paginated Results for more information. |
| `previous` | String | URL to retrieve the previous page of results. See Paginated Results for more information. |
| `next` | String | URL to retrieve the next page of results. See Paginated Results for more information. |
### Sample Post Metric Request

```
curl -i -X GET \
 "https://graph.facebook.com/v19.0/17932174733377207/insights?metric=profile_activity&breakdown=action_type&access_token=EAAOc..."
```
### Sample Post Metric Response

```
{
  "data": [
    {
      "name": "profile_activity",
      "period": "lifetime",
      "values": [
        {
          "value": 4
        }
      ],
      "title": "Profile activity",
      "description": "[IG Insights] This header is the name of a metric that appears on an educational info sheet for a particular post, story, video or promotion. This metric is the sum of all profile actions people take when they engage with this content.",
      "total_value": {
        "value": 4,
        "breakdowns": [
          {
            "dimension_keys": [
              "action_type"
            ],
            "results": [
              {
                "dimension_values": [
                  "email"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "text"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "direction"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "bio_link_clicked"
                ],
                "value": 1
              }
            ]
          }
        ]
      },
      "id": "17932174733377207/insights/profile_activity/lifetime"
    }
  ]
}
```
### Sample Story Metric Request

```
curl -i -X GET \
 "https://graph.facebook.com/v19.0/17969782069736348/insights?metric=navigation&breakdown=story_navigation_action_type&access_token=EAAOc..."
```
### Sample Story Metric Response

```
{
  "data": [
    {
      "name": "navigation",
      "period": "lifetime",
      "values": [
        {
          "value": 25
        }
      ],
      "title": "Navigation",
      "description": "This is the total number of actions taken from your story. These are made up of metrics like exited, forward, back and next story.",
      "total_value": {
        "value": 25,
        "breakdowns": [
          {
            "dimension_keys": [
              "story_navigation_action_type"
            ],
            "results": [
              {
                "dimension_values": [
                  "tap_forward"
                ],
                "value": 19
              },
              {
                "dimension_values": [
                  "tap_back"
                ],
                "value": 4
              },
              {
                "dimension_values": [
                  "tap_exit"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "swipe_forward"
                ],
                "value": 1
              }
            ]
          }
        ]
      },
      "id": "17969782069736348/insights/navigation/lifetime"
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