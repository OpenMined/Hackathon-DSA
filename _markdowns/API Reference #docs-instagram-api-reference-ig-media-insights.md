::: {._4-u3 ._588p}
::: {._57yz ._57z1 ._3-8p}
::: _57y-
The metrics listed below are new and will gradually be made available to
all developers. These metrics will eventually replace the legacy metrics
listed above. If you see this message you are able to use the new
metrics described below.
:::
:::

``` {._5s-8 .prettyprint .lang-http}
GET https://graph.facebook.com/{api-version}/{ig-media-id}/insights
  ?metric={metric}
  &breakdown={breakdown}
  &access_token={access-token}
```

::: _57-c
Placeholder
:::
:::

Value

` {api-version} `

API [version](/docs/graph-api/guides/versioning) .

` {ig-media-id} `

**Required.** [IG Media](/docs/instagram-api/reference/ig-media) ID.

::: _57-c
Key
:::

Placeholder

Value

` access_token `

` {access-token} `

**Required.** The app user\'s
[User](/docs/facebook-login/guides/access-tokens#usertokens) access
token.

` breakdown `

` {breakdown} `

Designates how to break down result set into subsets. See
[Breakdown](#breakdown) .

` metric `

` {metric} `

**Required.** Comma-separated list of [Metrics](#metrics) you want
returned.

You can also specify one or more breakdowns, and the results will be
broken down into smaller sets based on the specified breakdown. Values
can be:

-   ` action_type ` --- Only compatible with the profile_activity
    metric. Break down results by profile UI component that viewers
    tapped or clicked after viewing the app user\'s profile. Response
    values can be:
    -   ` BIO_LINK_CLICKED `
    -   ` CALL `
    -   ` DIRECTION `
    -   ` EMAIL `
    -   ` OTHER `
    -   ` TEXT `
-   ` story_navigation_action_type ` --- Break down results by
    navigation action taken by the viewer upon viewing the media.
    -   ` TAP_BACK `
    -   ` TAP_EXIT `
    -   ` TAP_FORWARD `
    -   ` SWIPE_FORWARD `

Refer to the [Metrics](#metrics) table to determine which metrics
support breakdowns and which breakdowns they support. If you request a
metric that doesn\'t support breakdowns, the API will return an error
(\" ` An unknown error has occurred. ` \"), so be careful if requesting
multiple metrics in a single query.

### Metrics

#### Post Metrics

The following metrics are available on image and video IG Media
published as a Post. Album carousels and IGTV are not supported.

::: _57-c
Metric
:::

Breakdown

Description

` comments `

n/a

The number of comments on your post.

` follows `

n/a

The number of accounts that started following you.

` likes `

n/a

The number of likes on your post.

` profile_activity `

` action_type `

The number of actions people take when they visit your profile after
engaging with your post.

` profile_visits `

n/a

The number of times your profile was visited.

` shares `

n/a

The number of shares of your post.

` total_interactions `

n/a

The number of likes, saves, comments and shares on your post minus the
number of unlikes, unsaves and deleted comments.

#### Story Metrics

The following metrics are available on IG Media published as a Story.

::: _57-c
Metric
:::

Breakdown

Description

` follows `

n/a

This is how many accounts started following you.

` navigation `

` story_navigation_action_type `

This is the total number of actions taken from your story. These are
made up of metrics like exited, forward, back and next story.

` profile_activity `

` action_type `

The number of actions people take when they visit your profile after
engaging with your story.

` profile_visits `

n/a

The number of times your profile was visited.

` shares `

n/a

The number of shares of your story.

` total_interactions `

n/a

The number of replies and shares for your story.

### Response

A JSON object containing the results of your query. Results can include
the following data, based on your query specifications:

``` {._5s-8 .prettyprint .lang-json}
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

::: _57-c
Property
:::

Value Type

Description

` data `

Array

An array containing an object describing your request results.

` name `

String

[Metric](#metrics) name.

` period `

String

Period requested. Period is automatically set to ` lifetime ` in the
request and cannot be changed, so this value will always be ` lifetime `
.

` values `

Array

An array containing an object describing requested [metric](#metrics)
values.

` value `

Integer

For ` data.values.value ` , sum of requested [metric](#metrics) values.

\

For ` data.total_value.value ` , sum of requested
[breakdown](#breakdown) values.

\

For ` data.total_value.breakdowns.results.value ` , sum of
[breakdown](#breakdown) set values.

` title `

String

[Metric](#metrics) title.

` description `

String

[Metric](#metrics) description.

` id `

String

A string describing the query\'s path parameters.

` total_value `

Object

Object describing requested [breakdown](#breakdown) values (if
breakdowns were requested).

` breakdowns `

Array

An array of objects describing the [breakdowns](#breakdown) requested
and their results.

` dimension_keys `

Array

Array of strings describing [breakdowns](#breakdown) requested.

` results `

Array

An array of objects describing each [breakdown](#breakdown) set.

` dimension_values `

String

An array of strings describing [breakdown](#breakdown) set values.
Values can be mapped to ` dimension_keys ` .

` paging `

Object

An object containing URLs used to request the next set of results. See
[Paginated Results](docs/graph-api/results) for more information.

` previous `

String

URL to retrieve the previous page of results. See [Paginated
Results](docs/graph-api/results) for more information.

` next `

String

URL to retrieve the next page of results. See [Paginated
Results](docs/graph-api/results) for more information.

### Sample Post Metric Request

``` {._5s-8 .prettyprint .lang-curl}
curl -i -X GET \ "https://graph.facebook.com/v18.0/17932174733377207/insights?metric=profile_activity&breakdown=action_type&access_token=EAAOc..."
```

### Sample Post Metric Response

``` {._5s-8 .prettyprint .lang-json}
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

``` {._5s-8 .prettyprint .lang-curl}
curl -i -X GET \ "https://graph.facebook.com/v18.0/17969782069736348/insights?metric=navigation&breakdown=story_navigation_action_type&access_token=EAAOc..."
```

### Sample Story Metric Response

``` {._5s-8 .prettyprint .lang-json}
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
