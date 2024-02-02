Insights - Instagram Platform - Documentation - Meta for Developers

Instagram Graph API* Overview
* Getting Started
* Guides
* Reference
* Changelog
Instagram User Insights
=======================

Represents social interaction metrics on an Instagram User.

Creating
--------

This operation is not supported.

Reading
-------

**`GET /{ig-user-id}/insights`**

Returns insights on an IG User.

### Limitations

* `follower_count`, `online_followers`, and all `audience_*` metrics are not available on IG Users with fewer than 100 followers.
* Insights data for the `online_followers` metric is only available for the last 30 days.
* If insights data you are requesting does not exist or is currently unavailable, the API will return an empty data set instead of `0` for individual metrics.
* Demographic metrics only return the top 45 performers (e.g., for `audience_city`, up to 45 cities with the highest number of followers can be returned).
* Only viewers for whom we have demographic data are used in demographic metric calculations.
* Summing demographic metric values may result in a value less than the follower count (see previous bullet point).
* `audience_*` metrics do not support `since` and `until` range parameters.
* Data used to calculate metrics may be delayed up to 48 hours.

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
GET https://graph.facebook.com/{api-version}/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &since={since}
  &until={until}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** IG User ID. |
### Query String Parameters

 Parameter | Value || `{access-token}`
**Required**
*String* | The app user's User Access Token. |
| `{metric}`
**Required**
*Comma-separated list* | A comma-separated list of Metrics you want returned. If requesting multiple metrics, they must all have the same compatible Period. |
| `{period}`
**Required**
*String* | A Period that is compatible with the metrics you are requesting. |
| `{since}`
*Unix timestamp* | Used in conjunction with `{until}` to define a Range. If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.
**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |
| `{until}`
*Unix timestamp* | Used in conjunction with `{since}` to define a Range. If you omit `since` and `until`, the API defaults to a 2 day range: yesterday through today.
**Note**: The pagination cursors (`previous` and `next`) fetch the next time window of results, not the next batch of results within the current time window. |
### Metrics and Periods

Some of these metrics are deprecated for v18.0. They will be deprecated for all versions beginning Dec 11, 2023. Please use the alternative metrics listed. See the Changelog for more information.

Metrics that support `lifetime` periods will have results returned in an array of 24 hour periods, with periods ending on UTC−07:00. `audience_*` metrics do not support `since` and `until` range parameters.

 Metric | Compatible Period | Description || `audience_city`
*Deprecated for v18.0+* | `lifetime` | Cities of followers for whom we have demographic data.
* Does not include current day's data.
* Not available on IG Users with fewer than 100 followers.
* Only top 45 cities with highest values returned.
* Does not support `since` and `until` parameters.
* Response does not include the `end_time` JSON property.
**Alternative metric:** `follower_demographics`
**Breakdown:** `city` |
| `audience_country`
*Deprecated for v18.0+* | `lifetime` | Countries of followers for whom we have demographic data.
* Does not include current day's data.
* Not available on IG Users with fewer than 100 followers.
* Only top 45 countries with highest values returned.
* Does not support `since` and `until` parameters.
* Response does not include the `end_time` JSON property.
**Alternative metric:** `follower_demographics`
**Breakdown:** `country` |
| `audience_gender_age`
*Deprecated for v18.0+* | `lifetime` | The gender and age distribution of followers for whom we have demographic data. Possible values: `M` (male), `F` (female), `U` (Uncategorised).
* Does not include current day's data.
* Not available on IG Users with fewer than 100 followers.
* Does not support `since` and `until` parameters.
* Response does not include the `end_time` JSON property.
**Alternative metric:** `follower_demographics`
**Breakdown:** `age`, `gender` |
| `audience_locale`
*Deprecated for v18.0+* | `lifetime` | **Note:** This metric is no longer supported.
Locales by country codes of followers for whom we have demographic data.
* Does not include current day's data.
* Not available on IG Users with fewer than 100 followers.
* Only top 45 locales with highest values returned.
* Does not support `since` and `until` parameters.
* Response does not include the `end_time` JSON property.
**Alternative metric:** N/A |
| `email_contacts` | `day` | Total number of taps on the email link in the IG User's profile. |
| `follower_count` | `day` | Total number of new followers each day within the specified range. Returns a maximum of 30 days worth of data. Not available on IG Users with fewer than 100 followers. |
| `get_directions_clicks` | `day` | Total number of taps on the directions link in the IG User's profile. |
| `impressions` | `day`, `week`, `days_28` | Total number of times the IG User's IG Media have been viewed. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. Does not include profile views. |
| `online_followers` | `lifetime` | Total number of the IG User's followers who were online during the specified range. Not available on IG Users with fewer than 100 followers. |
| `phone_call_clicks` | `day` | Total number of taps on the call link in the IG User's profile. |
| `profile_views` | `day` | Total number of users who have viewed the IG User's profile within the specified period. |
| `reach` | `day`, `week`, `days_28` | Total number of unique users who have viewed at least one of the IG User's IG Media. Repeat views and views across different IG Media owned by the IG User by the same user are only counted as a single view. Includes ad activity generated through the API, Facebook ads interfaces, and the Promote feature. |
| `text_message_clicks` | `day` | Total number of taps on the text message link in the IG User's profile. |
| `website_clicks` | `day` | Total number of taps on the website link in the IG User's profile. |
### Range

This edge supports time-based pagination, so you can include the `since` and `until` parameters with Unix timestamps to define a *range*. For example, to get 28 days worth of impressions — *every day for the last 10 days* — you could generate Unix timestamps for *10 days ago* and *today*, assign them to the `since` and `until` parameters, and include them in your request:

```
metric=impressions&period=days_28&since=1501545600&until=1502493720
```
The `since` and `until` parameters are inclusive, so if your range includes a day that hasn't ended (i.e, today), subsequent queries throughout the day may return increased values. If you do not include the `since` and `until` parameters, the API will default to a 2 day range: yesterday through today.

### Sample Request

```
curl -X GET \
  'https://graph.facebook.com/v19.0/17841405822304914/insights?metric=impressions,reach,profile_views&period=day&access_token=IGQVJ...'
```
### Sample Response

```
{
  "data": [
    {
      "name": "impressions",
      "period": "day",
      "values": [
        {
          "value": 4,
          "end_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 66,
          "end_time": "2017-05-05T07:00:00+0000"
        }
      ],
      "title": "Impressions",
      "description": "Total number of times this profile has been seen",
      "id": "17841400008460056/insights/impressions/day"
    },
    {
      "name": "reach",
      "period": "day",
      "values": [
        {
          "value": 3,
          "end_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 36,
          "end_time": "2017-05-05T07:00:00+0000"
        }
      ],
      "title": "Reach",
      "description": "Total number of unique accounts that have seen this profile",
      "id": "17841400008460056/insights/reach/day"
    },
    {
      "name": "profile_views",
      "period": "day",
      "values": [
        {
          "value": 0,
          "end_time": "2017-05-04T07:00:00+0000"
        },
        {
          "value": 2,
          "end_time": "2017-05-05T07:00:00+0000"
        }
      ],
      "title": "Profile Views",
      "description": "Total number of unique accounts that have viewed this profile within the specified period",
      "id": "17841400008460056/insights/profile_views/day"
    }
  ]
}
```
Notice that the sample request above did not include the `since` and `until` parameters, so the API returned data for a default range of 2 days. Each day is identified by an ISO 8601 formatted UTC timestamp with zero offset, which has been assigned to an `end_time` property.

The `end_time` property indicates a data set's lookback cutoff date; data older than this value is not included in the data set's calculation.

Updating
--------

This operation is not supported.

Deleting
--------

This operation is not supported.

New Metrics
-----------

The metrics listed below are new and will gradually be made available to all developers. These metrics will eventually replace the legacy metrics listed above. If you see this message you are able to use the new metrics described below.

### Request Syntax

```
GET https://graph.facebook.com/{api-version}/{ig-user-id}/insights
  ?metric={metric}
  &period={period}
  &timeframe={timeframe}
  &metric_type={metric-type}
  &breakdown={breakdown}
  &since={since}
  &until={until}
  &access_token={access-token}
```
### Path Parameters

 Placeholder | Value || `{api-version}` | API version. |
| `{ig-user-id}` | **Required.** IG User ID. |
### Query String Parameters

 Key
  | 
 Placeholder
  | 
 Value
  || `access_token` | `{access-token}` | **Required.** The app user's User access token. |
| `breakdown` | `{breakdown}` | Designates how to break down result set into subsets. See Breakdown. |
| `metric` | `{metric}` | **Required.** Comma-separated list of Metrics you want returned. |
| `metric_type` | `{metric-type}` | Designates if you want the responses aggregated by time period or as a simple total. See Metric Type. |
| `period` | `{period}` | **Required.** Period aggregation. |
| `since` | `{since}` | Unix timestamp indicating start of range. See Range. |
| `timeframe` | `{timeframe}` | **Required for demographics-related metrics.** Designates how far to look back for data. See Timeframe. |
| `until` | `{until}` | Unix timestamp indicating end of range. See Range. |
### Breakdown

If you request `metric_type=total_value`, you can also specify one or more breakdowns, and the results will be broken down into smaller sets based on the specified breakdown. Values can be:

* `contact_button_type` — Break down results by profile UI component that viewers tapped or clicked. Response values can be:
	+ `BOOK_NOW`
	+ `CALL`
	+ `DIRECTION`
	+ `EMAIL`
	+ `INSTANT_EXPERIENCE`
	+ `TEXT`
	+ `UNDEFINED`
* `follow_type` — Break down results by followers or non-followers. Response values can be:
	+ `FOLLOWER`
	+ `NON_FOLLOWER`
	+ `UNKNOWN`
* `media_product_type` — Break down results by the surface where viewers viewed or interacted with the app user's media. Response values can be:
	+ `AD`
	+ `FEED`
	+ `REELS`
	+ `STORY`

Refer to the Metrics table to determine which metrics are compatible with a breakdown. If you request a metric that doesn't support a breakdown, the API will return an error (`"An unknown error has occurred."`), so be careful if requesting multiple metrics in a single query.

If you request `metric_type=time_series`, breakdowns will not be included in the response.

### Metric Type

You can designate how you want results aggregated, either by time period or as a simple total (with breakdowns, if requested). Values can be:

* `time_series` — Tells the API to aggregate results by time period. See Period.
* `total_value` — Tells the API to return results as a simple total. If breakdowns are included in the request, the result set will be further broken down by the specific breakdowns. See Breakdown.

### Period

Tells the API which time frame to use when aggregating results. Only compatible with interaction-related metrics.

### Timeframe

Tells the API how far to look back for data when requesting demographic-related metrics. This value overrides the `since` and `until` parameters.

### Range

Assign UNIX timestamps to the `since` and `until` parameters to define a range. The API will only include data created within this range (inclusive). If you do not include these parameters, the API will look back 24 hours.

For demographics-related metrics, the `timeframe` parameter overrides these values. See Timeframe.

### Metrics

#### Interaction Metrics

 Metric
  | 
 Period
  | 
 Timeframe
  | 
 Breakdown
  | 
 Metric Type
  | 
 Description
  || `impressions` | `day` | n/a | n/a | `total_value`,
`time_series` | The number of times your posts, stories, reels, videos and live videos were on screen, including in ads. |
| `reach` | `day` | n/a | `media_product_type`,
`follow_type` | `total_value`,
`time_series` | The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts.
This metric is estimated and in development. |
| `total_interactions` | `day` | n/a | `media_product_type` | `total_value` | The total number of post interactions, story interactions, reels interactions, video interactions and live video interactions, including any interactions on boosted content. |
| `accounts_engaged` | `day` | n/a | n/a | `total_value` | The number of accounts that have interacted with your content, including in ads. Content includes posts, stories, reels, videos and live videos. Interactions can include actions such as likes, saves, comments, shares or replies.
This metric is estimated and in development. |
| `likes` | `day` | n/a | `media_product_type` | `total_value` | The number of likes on your posts, reels, and videos. |
| `comments` | `day` | n/a | `media_product_type` | `total_value` | The number of comments on your posts, reels, videos and live videos.
This metric is in development. |
| `saved` | `day` | n/a | `media_product_type` | `total_value` | The number of saves of your posts, reels, and videos. |
| `shares` | `day` | n/a | `media_product_type` | `total_value` | The number of shares of your posts, stories, reels, videos and live videos. |
| `replies` | `day` | n/a | n/a | `total_value` | The number of replies you received from your story, including text replies and quick reaction replies. |
| `follows_and_unfollows` | `day` | n/a | `follow_type` | `total_value` | The number of accounts that followed you and the number of accounts that unfollowed you or left Instagram in the selected time period.
Not returned if the IG User has less than 100 followers. |
| `profile_links_taps` | `day` | n/a | `contact_button_type` | `total_value` | The number of taps on your business address, call button, email button and text button. |
| `website_clicks` | `day` | n/a | n/a | `total_value` | The number of times the link to your website was tapped. |
| `profile_views` | `day` | n/a | n/a | `total_value` | The number of times your profile was visited. |
#### Demographic Metrics

 Metric
  | 
 Period
  | 
 Timeframe
  | 
 Breakdown
  | 
 Metric Type
  | 
 Description
  || `engaged_audience_demographics` | `lifetime` | One of:
`last_14_days`,
`last_30_days`,
`last_90_days`,
`prev_month`,
`this_month`,
`this_week` | `age`,
`city`,
`country`,
`gender` | `total_value` | The demographic characteristics of the engaged audience, including countries, cities and gender distribution.
Does not support `since` or `until`. See Range for more information.
Not returned if the IG User has less than 100 followers. |
| `reached_audience_demographics` | `lifetime` | One of:
`last_14_days`,
`last_30_days`,
`last_90_days`,
`prev_month`,
`this_month`,
`this_week` | `age`,
`city`,
`country`,
`gender` | `total_value` | The demographic characteristics of the reached audience, including countries, cities and gender distribution.
Does not support `since` or `until`. See Range for more information.
Not returned if the IG User has less than 100 followers. |
| `follower_demographics` | `lifetime` | One of:
`last_14_days`,
`last_30_days`,
`last_90_days`,
`prev_month`,
`this_month`,
`this_week` | `age`,
`city`,
`country`,
`gender` | `total_value` | The demographic characteristics of followers, including countries, cities and gender distribution.
Does not support `since` or `until`. See Range for more information.
Not returned if the IG User has less than 100 followers. |
### Response

A JSON object containing the results of your query. Results can include the following data, based on your query specifications:

```
{
  "data": [
    {
      "name": "{data}",
      "period": "{period}",
      "title": "{title}",
      "description": "{description}",
      "total_value": {
        "value": {value},
        "breakdowns": [
          {
            "dimension_keys": [
              "{key-1}",
              "{key-2",
              ...
            ],
            "results": [
              {
                "dimension_values": [
                  "{value-1}",
                  "{value-2}",
                  ...
                ],
                "value": {value},
                "end_time": "{end-time}"
              },
              ...
            ]
          }
        ]
      },
      "id": "{id}"
    }
  ],
  "paging": {
    "previous": "{previous}",
    "next": "{next}"
  }
}
```
### Response Contents

 Property | Value Type | Description || `breakdowns` | Array | An array of objects describing the breakdowns requested and their results.
Only returned if `metric_type=total_values` is requested. |
| `data` | Array | An array of objects describing your results. |
| `description` | String | Metric description. |
| `dimension_keys` | Array | An array of strings describing breakdowns requested in the query. Can be used as keys corresponding to values in individual breakdown sets.
Only returned if `metric_type=total_values` is requested. |
| `dimension_values` | Array | An array of strings describing breakdown set values. Values can be mapped to `dimension_keys`.
Only returned if `metric_type=total_values` is requested. |
| `end_time` | String | ISO 8601 timestamp with time and offset. For example: `2022-08-01T07:00:00+0000` |
| `id` | String | A string describing the query's path parameters. |
| `name` | String | Metric requested. |
| `next` | String | URL to retrieve the next page of results. See Paginated Results for more information. |
| `paging` | Object | An object containing URLs used to request the next set of results. See Paginated Results for more information. |
| `period` | String | Period requested. |
| `previous` | String | URL to retrieve the previous page of results. See Paginated Results for more information. |
| `results` | Array | An array of objects describing each breakdown set.
Only returned if `metric_type=total_values` is requested. |
| `title` | String | Metric title. |
| `total_value` | Object | Object describing requested breakdown values (if breakdowns were requested). |
| `value` | Integer | For `data.total_value.value`, sum of requested metric values.
For `data.total_value.breakdowns.results.value`, sum of breakdown set values. Only returned if `metric_type=total_values` is requested. |
### Sample Interaction Metric Request

```
curl -i -X GET \
  "https://graph.facebook.com/v19.0/17841405822304914/insights?metric=reach&period=day&breakdown=media_product_type&metric_type=total_value&since=1658991600&access_token=EAAOc..."
```
### Sample Interaction Metric Response

```
{
  "data": [
    {
      "name": "reach",
      "period": "day",
      "title": "Accounts reached",
      "description": "The number of unique accounts that have seen your content, at least once, including in ads. Content includes posts, stories, reels, videos and live videos. Reach is different from impressions, which may include multiple views of your content by the same accounts. This metric is estimated and in development.",
      "total_value": {
        "value": 224,
        "breakdowns": [
          {
            "dimension_keys": [
              "media_product_type"
            ],
            "results": [
              {
                "dimension_values": [
                  "CAROUSEL_CONTAINER"
                ],
                "value": 100
              },
              {
                "dimension_values": [
                  "POST"
                ],
                "value": 124
              }
            ]
          }
        ]
      },
      "id": "17841405309211844/insights/reach/day"
    }
  ],
  "paging": {
    "previous": "https://graph.face...",
    "next": "https://graph.face..."
  }
```
### Sample Demographic Metric Request

```
curl -i -X GET \
  "https://graph.facebook.com/v19.0/17841405822304914/insights?metric=engaged_audience_demographics&period=lifetime&timeframe=last_90_days&breakdowns=country&metric_type=total_value&access_token=EAAOc..."
```
### Sample Demographic Metric Response

```
{
  "data": [
    {
      "name": "engaged_audience_demographics",
      "period": "lifetime",
      "title": "Engaged audience demographics",
      "description": "The demographic characteristics of the engaged audience, including countries, cities and gender distribution.",
      "total_value": {
        "breakdowns": [
          {
            "dimension_keys": [
              "timeframe",
              "country"
            ],
            "results": [
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "AR"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "RU"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "MA"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "LA"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "IQ"
                ],
                "value": 2
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "MX"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "FR"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "ES"
                ],
                "value": 3
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "NL"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "TR"
                ],
                "value": 1
              },
              {
                "dimension_values": [
                  "LAST_90_DAYS",
                  "US"
                ],
                "value": 7
              }
            ]
          }
        ]
      },
      "id": "17841401130346306/insights/engaged_audience_demographics/lifetime"
    }
  ]
}
```